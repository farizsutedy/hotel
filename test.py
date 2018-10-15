print("Marina Bay Sand")
class Desk():
    def __init__(self):
        self.regulerRoom = ["","",""]
        self.suiteRoom = ["","",""]
        self.leghtStay = ["","","","","",""]
        self.listCustomer = ["","","","","",""]
        self.regulerRoomType = ["","","","","",""]
        self.suiteRoomType = ["","","","","",""]
        self.priceDeluxe = 2000000
        self.priceNormal = 1000000
        self.revenue = 0

    def check_revenue(self):
        print("Total Revenue : Rp.", self.revenue)

    def check_room(self):
        print("Which Room You Want To Check ?")
        print("1.Room Normal")
        print("2.Room Deluxe")
        choice = int(input("Enter Choice :"))
        if choice == 1:
            print("Normal Room : ",self.regulerRoom)
        if choice == 2:
            print("Deluxe Room : ",self.suiteRoom)


class Customer(Desk):

    def check_in(self):
        customerName = input("Enter Customer Name : ")
        stay = int(input("How Long Will You Stay ? :"))
        print("Which Category of Rooms")
        print("1. Room Normal")
        print("2. Room Deluxe")
        choice = int(input("Enter Choice :\n"))

        if choice == 1 :
            if self.regulerRoom[2] != "":
                print("\nSorry Room Is Full\n")
            elif self.regulerRoom[0] == "":
                self.regulerRoom[0]= customerName
                self.listCustomer[0] = customerName
                self.leghtStay[0] = stay
                self.regulerRoomType[0] = "Normal"
                print("Customer Name :",customerName)
                print("Room Number :",self.regulerRoom.index(customerName))
                print("Room Type :",self.regulerRoomType[0])
                print("Stay For : ", stay, "Night")
            elif self.regulerRoom[1] == "":
                self.regulerRoom[1]= customerName
                self.listCustomer[1] = customerName
                self.leghtStay[1] = stay
                self.regulerRoomType[1] = "Normal"
                print("Customer Name :",customerName)
                print("Room Number :",self.regulerRoom.index(customerName))
                print("Room Type :",self.regulerRoomType[1])
                print("Stay For : ", stay, "Night")
            elif self.regulerRoom[2] == "":
                self.regulerRoom[2]= customerName
                self.listCustomer[2] = customerName
                self.leghtStay[2] = stay
                self.regulerRoomType[2] = "Normal"
                print("Customer Name :",customerName)
                print("Room Number :",self.regulerRoom.index(customerName))
                print("Room Type :",self.regulerRoomType[2])
                print("Stay For : ", stay, "Night")

        if choice == 2 :
            if self.suiteRoom[2] != "":
                print("\nSorry Room Is Full\n")
            elif self.suiteRoom[0] == "":
                self.suiteRoom[0]= customerName
                self.listCustomer[3] = customerName
                self.leghtStay[3] = stay
                self.suiteRoomType[0] = "Deluxe"
                print("Customer Name :",customerName)
                print("Room Number :",self.listCustomer.index(customerName))
                print("Room Type :",self.suiteRoomType[0])
                print("Stay For : ", stay, "Night")
            elif self.suiteRoom[1] == "":
                self.suiteRoom[1]= customerName
                self.listCustomer[4] = customerName
                self.leghtStay[4] = stay
                self.suiteRoomType[1] = "Deluxe"
                print("Customer Name :",customerName)
                print("Room Number :",self.listCustomer.index(customerName))
                print("Room Type :",self.suiteRoomType[1])
                print("Stay For : ", stay, "Night")
            elif self.suiteRoom[2] == "":
                self.suiteRoom[2]= customerName
                self.listCustomer[5] = customerName
                self.leghtStay[5] = stay
                self.suiteRoomType[2] = "Deluxe"
                print("Customer Name :",customerName)
                print("Room Number :",self.listCustomer.index(customerName))
                print("Room Type :",self.suiteRoomType[2])
                print("Stay For : ", stay, "Night")

    def check_out(self):
        customerRoom = int(input("Which Room Number Did You Stay?: "))
        print("Which Room Type Did You Stay ?:")
        print("1.Normal Room")
        print("2.Deluxe Room")
        choice = int(input("Enter Choice :\n"))

        if choice == 1 :
            if self.regulerRoom[customerRoom] != "":
                self.regulerRoom[customerRoom] = ""
            if customerRoom == 0:
                print("Customer Name :",self.listCustomer[0])
                print("Room Number : 0")
                print("Room Type :",self.regulerRoomType[0])
                print("Stay For : ", self.leghtStay[0], "Night")
                print("\nPrice :Rp.",self.priceNormal*self.leghtStay[0])
                self.revenue += self.priceNormal*self.leghtStay[0]
            if customerRoom == 1:
                print("Customer Name :",self.listCustomer[1])
                print("Room Number : 1")
                print("Room Type :",self.regulerRoomType[1])
                print("Stay For : ", self.leghtStay[1], "Night")
                print("\nPrice :Rp.",self.priceNormal*self.leghtStay[1])
                self.revenue += self.priceNormal*self.leghtStay[1]
            if customerRoom == 2:
                print("Customer Name :",self.listCustomer[2])
                print("Room Number : 2")
                print("Room Type :",self.regulerRoomType[2])
                print("Stay For : ", self.leghtStay[2], "Night")
                print("\nPrice :Rp.",self.priceNormal*self.leghtStay[2])
                self.revenue += self.priceNormal*self.leghtStay[2]
        if choice == 2:
            jumlah = customerRoom - 3
            if self.suiteRoom[jumlah] != "":
                self.suiteRoom[jumlah] = ""
            if customerRoom == 3:
                print("Customer Name :",self.listCustomer[3])
                print("Room Number : 3")
                print("Room Type :",self.suiteRoomType[0])
                print("Stay For : ", self.leghtStay[3], "Night")
                print("\nPrice :Rp.",self.priceDeluxe*self.leghtStay[3])
                self.revenue += self.priceDeluxe*self.leghtStay[3]
            if customerRoom == 4:
                print("Customer Name :",self.listCustomer[4])
                print("Room Number : 4")
                print("Room Type :",self.suiteRoomType[1])
                print("Stay For : ", self.leghtStay[4], "Night")
                print("\nPrice :Rp.",self.priceDeluxe*self.leghtStay[4])
                self.revenue += self.priceDeluxe*self.leghtStay[4]
            if customerRoom == 5:
                print("Customer Name :",self.listCustomer[5])
                print("Room Number : 5")
                print("Room Type :",self.suiteRoomType[2])
                print("Stay For : ", self.leghtStay[5], "Night")
                print("\nPrice :Rp.",self.priceDeluxe*self.leghtStay[5])
                self.revenue += self.priceDeluxe*self.leghtStay[5]


c = Customer()

while True :
    print("\n1. Check In")
    print("2. Check Out")
    print("3. Check Room")
    print("4. Check Revenue")
    choice = int(input("\nEnter Choice :"))

    if choice == 1 :
        c.check_in()

    elif choice == 2:
        c.check_out()

    elif choice == 3:
        c.check_room()

    elif choice == 4:
        c.check_revenue()

    else :
        print("Invalid Input")
