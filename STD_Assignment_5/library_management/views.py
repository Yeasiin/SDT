from django.shortcuts import render
from django.views.generic  import DetailView,ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from book.models import BookModel
from genre.models import BookGenre
from borrow.models import BorrowModel
from review.forms import ReviewForm
from review.models import ReviewModel
from urllib.parse import urlencode



class HomeView(ListView):
    model = BookModel
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query")   
     
        if query:
            context["items"] = BookModel.objects.filter(genres__name=query)
        else:
            context["items"] = BookModel.objects.all()
            
        context["genres"] = BookGenre.objects.all()
        
        
        
        for i in context["items"]:
            print(i.genres.name,"-")
        
        
        
        
 
        
        return context
    


class SingleProduct(DetailView):
    model = BookModel
    template_name = "single-product.html"
    context_object_name = 'data'
    
    http_method_names = ['get','post']
    
    def dispatch(self, request, *args, **kwargs):
        query_params = self.request.GET.copy()
        # Check and remove 'order=true' if it exists
        if 'borrow' in query_params:
            book = self.get_object()
            book.quantity = book.quantity - 1
            book.save()
            user = self.request.user
            
            if(user.userprofile.balance >= book.price):
                user.userprofile.balance -= book.price
                balance_after_record = user.userprofile.balance
                user.userprofile.save()
                
                order = BorrowModel.objects.create(user = user ,book = book, balance_after_record = balance_after_record  )
                order.save()
                messages.success(self.request, "Book Borrow successful")
            else:
                messages.error(self.request, "Balance is insufficient")       
            
            query_params.pop('borrow')
            new_url = f"{self.request.path}?{urlencode(query_params)}" if query_params else self.request.path
            return HttpResponseRedirect(new_url)
        
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self,request,*args,**kwargs):
        carObj = self.get_object()
        form = ReviewForm(self.request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = carObj
            review.user = self.request.user
            review.save()
            messages.success(self.request,"Review Added Successfully!")
        else:
            messages.error(self.request,"Failed to add review!")
        
        return self.get(request,*args,**kwargs)
            
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        bookObj = self.get_object()
        reviews = ReviewModel.objects.filter(book=bookObj)
        review_form = ReviewForm()
        context['review_form'] = review_form
        context['reviews'] = reviews
        if(self.request.user.is_anonymous):
            context['has_taken'] = False
        else:
            context['has_taken'] = BorrowModel.objects.filter(user=self.request.user, book=bookObj).exists()
            
        

        return context


def borrows(request):
    items = BorrowModel.objects.filter(user__id=request.user.id)
    
    if request.method== "POST":
        id  = request.POST.get("trxid")
        record =  BorrowModel.objects.filter(id=id).first()
        user = request.user
        user.userprofile.balance += record.book.price
        user.userprofile.save()  
        record.is_returned = True
        record.save()
    
    return render(request,'borrow.html',{'items':items})



