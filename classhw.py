class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner


vehicle1 = Vehicle("12345", "car", "noach")

vehicle2 = Vehicle("45678", "van", "john")



print("first owners")
print( vehicle1.owner)
print( vehicle2.owner)



vehicle1.update_owner("jason")
vehicle2.update_owner("josh")


print( vehicle1.owner)
print( vehicle2.owner)




class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.count = 0

      

        def add(self):
            self.count += 1  

        def get_count(self):
            return self.count