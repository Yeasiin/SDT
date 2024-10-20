class Star_Cinema:
    def __init__(self):
        self.__hall_list = []

    def entry_hall(self,hall):
        self.__hall_list.append(hall)

    def all_Show(self):
        for hall in self.__hall_list:
            hall.view_show_list()



class Hall:
    def __init__(self,hall_no,rows,cols) -> None:
        self.__hall_no = hall_no
        self.__seats = dict()
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols

    def entry_show(self,id, movie_name,date):
        show = tuple((id,movie_name,date))
        self.__show_list.append(show)
        seat = [[0]*self.__cols for _ in [0]*self.__rows]
        self.__seats[id] = seat

    def book_seats(self,id,list_of_seat):
        if(self.__seats[id]):
            for seat in list_of_seat:
                if(seat[0] >= self.__rows or seat[1] >=self.__cols):
                    print("Invalid Seat")
                    continue
                if(self.__seats[id][seat[0]][seat[1]] ==1):
                    print(f"Seat {seat[0]} {seat[1]} already booked")
                else:
                    self.__seats[id][seat[0]][seat[1]] = 1
                    print(f"Seat {seat[0]} {seat[1]} Booked for Show {id}")

        else:
            print("Show Not Found")

    def view_show_list(self,):
        for show in self.__show_list:
            print(f"Show id: {show[0]} Name: {show[1]} Date: {show[2]}")

    def view_available_seats(self,id):
        if(id in self.__seats):
            print("Seat For Show:", id)
            for seat in self.__seats[id]:
                print(seat)
        else:
            print("No Show Found")


starCin = Star_Cinema()
hall1 = Hall(101,5,5)
starCin.entry_hall(hall1)

hall1.entry_show('A101',"Man Of Steel",'9/30/2024')
hall1.entry_show('B101',"Batman VS Superman",'9/30/2024')
hall1.entry_show("C101","DeadPool & Wolverine","10-01-2024")
hall1.entry_show("D101","Last of us", "10-05-2024")

option = '1'


while option !='4':
    print(" 1. VIEW ALL SHOW \n 2. VIEW AVAILABLE SEAT \n 3. BOOK SEAT\n 4. Exit")
    option = (input("Enter Option: "))

    if(option=='1'):
        # View All Show
        starCin.all_Show()

    elif (option=='2'):
        showId = input("Show id: ")
        hall1.view_available_seats(showId)

    elif (option=='3'):
        # Error handling Are done on Class Level
        showId = input("Show id: ")
        seats = int(input("Number of Ticket?: "))

        seatPlace = []
        for i in range(seats):
            x = int(input("Enter Seat Row: "))
            y = int(input("Enter Seat Col: "))
            seatPlace.append((x,y))

        hall1.book_seats(showId,seatPlace)




