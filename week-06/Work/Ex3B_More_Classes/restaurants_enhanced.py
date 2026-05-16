class restaurant:
    '''Describing restaurants by food type'''
    def __init__(self, rest_name, food_type, cust_rate=None, num_served=0):
        self.rest_name = rest_name
        self.food_type = food_type
        self.num_served = num_served 
        self.cust_rate = cust_rate or []
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')
    def rest_open(self):
        print(f'{self.rest_name} is open')
    def add_num_served(self):
        self.num_served += int(input("How Many people were served: "))
    def print_num_served(self):
        print(f"{self.rest_name} served {self.num_served} customers")
    def add_rating(self):
        rating = int(input("How would you rate your experience today on a scale of 1-5 (5 being excellent)?"))
        if 1 <= rating <= 5:
            self.cust_rate.append(rating)
            avg = sum(self.cust_rate) / len(self.cust_rate)
            print(f"Your rating was {self.cust_rate} \n"
                  f"The average rating for this restuarant is {avg}")
        else:
            print(f"Invalid rating, please rate 1-5 ")
tb = restaurant('Taco Bell', 'Mexican food', [], 13)
ob = restaurant('Out Back', 'Steak', [], 120)
jb = restaurant('Jack in the Box', 'Burgers', [], 20)

tb.describe_rest()
tb.rest_open()
tb.print_num_served()
tb.add_rating()
ob.describe_rest()
ob.rest_open()
ob.print_num_served()
ob.add_rating()
jb.describe_rest()
jb.rest_open()
jb.print_num_served()
jb.add_rating()