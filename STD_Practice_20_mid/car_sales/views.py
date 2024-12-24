from django.shortcuts import render
from django.views.generic  import DetailView,ListView
from car_model.models import CarModel
from brand.models import CarBrand
from django.contrib import messages
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from order.models import OrderModel
from comment.models import CommentModel
from comment.forms import CommentForm



class HomeView(ListView):
    model = CarModel
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("query")   
     
        if query:
            context["items"] = CarModel.objects.filter(brand__name=query)
        else:
            context["items"] = CarModel.objects.all()
            
        context["brands"] = CarBrand.objects.all()
        return context
    


class SingleProduct(DetailView):
    model = CarModel
    template_name = "single-product.html"
    context_object_name = 'data'
    
    http_method_names = ['get','post']
    
    def dispatch(self, request, *args, **kwargs):
        query_params = self.request.GET.copy()
        # Check and remove 'order=true' if it exists
        if 'order' in query_params:
            
            car = self.get_object()
            car.quantity = car.quantity - 1
            car.save()
            user_id = self.request.user
            order = OrderModel.objects.create(user = user_id ,car= car)
            order.save()
            messages.success(self.request, "Purchase successful")            
            
            query_params.pop('order')
            new_url = f"{self.request.path}?{urlencode(query_params)}" if query_params else self.request.path
            return HttpResponseRedirect(new_url)
        
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self,request,*args,**kwargs):
        carObj = self.get_object()
        form = CommentForm(self.request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = carObj
            comment.user = self.request.user
            comment.save()
            messages.success(self.request,"Comment Added Successfully!")
        else:
            messages.error(self.request,"Failed to add comment!")
        
        return self.get(request,*args,**kwargs)
            
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        carObj = self.get_object()
        comments = CommentModel.objects.filter(car=carObj)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['comments'] = comments
                
        return context




def orders(request):
    items = OrderModel.objects.filter(user__id=request.user.id)
    return render(request,'order.html',{'items':items})
    

