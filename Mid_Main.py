class Star_Cinema:
    hall_list=[]
    @classmethod
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self._seats={}
        self._showL=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self,show_id,movie_name,time):
        show_detail = (show_id,movie_name,time)
        self._showL.append(show_detail)
        list=[['O' for i in range(self.__cols)] for j in range(self.__rows)]
        self._seats[show_id] =list

    def book_seats(self,show_id,seat_book):
        cnt=0
        for showId in self._showL:
            if showId[0]==show_id:
                cnt=1
                for row,col in seat_book:
                    if row < 1 or row > self.__rows or col < 1 or col > self.__cols:
                        print("Invalid row and col",'\n')
                    elif self._seats[show_id][row-1][col-1] == '$':
                        print("Seat already booked,take another seat",'\n')
                    else:
                        self._seats[show_id][row-1][col-1] = '$'
                        print("Your seat had been booked",'\n')
        if cnt==0:
            print("Wrong show_id",'\n')
    def view_showL(self):
        for movie in self._showL:
            print(f'Movie name:-{movie}')
        print()

    def view_available_seats(self,show_id):
        cnt=0
        for showId in self._showL:
            if showId[0]==show_id:
                cnt=1
                available_seats=[]
                for i in range(self.__rows):
                    for j in range(self.__cols):
                        if self._seats[show_id][i][j]=='O':
                            available_seats.append((i+1,j+1))               
        if cnt==1:
            for hall, seat_list in self._seats.items():
                if hall==show_id:
                    print(f'Show {hall} Available Seat:-')
                    for row in seat_list:
                        print(row)
            for i in available_seats:
                print(f'Seat {i}')

        else:
            print()
            print("Wrong show_id",'\n')

class counter_view:
    def __init__(self,cinema) -> None:
        self.cinema=cinema

    def view_shows(self):
        for hall in self.cinema.hall_list:
            return hall.view_showL()
        
    def Seat_that_available(self,show_id):
        for hall in self.cinema.hall_list:
            return hall.view_available_seats(show_id)

    def Book_tickets(self,show_id,seats_to_book):
        for hall in self.cinema.hall_list:
            return hall.book_seats(show_id,seats_to_book)
            
hall1=Hall(5,5,1)
hall1.entry_show("S1", "Iron man", "2:00 PM")
hall1.entry_show("S2", "Avengers", "10:00 AM")

cinema = Star_Cinema()
counter=counter_view(cinema)

while True:
    print()
    print("1. View all show list")
    print("2. View Available seats")
    print("3. Book Tickets")
    print("4. Exit")
    n=int(input("Enter option: "))
    print()

    if n==1:
        counter.view_shows()
    elif n==2:
        m=input("Enter show id:")
        counter.Seat_that_available(m)
    elif n==3:
        d=input("Enter show id:") 
        e=int(input("Number of ticket:"))
        listin=[]
        line=()
        while(e!=0):
           a=int(input("Enter row :"))
           b=int(input("Enter coloum :"))
           l=line+(a,b)
           listin.append(l)
           e=e-1
        print()
        counter.Book_tickets(d,listin)
    elif n==4:
       break
    