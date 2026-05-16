class restaurant:
    '''Describing restaurants by food type'''
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')
    def rest_open(self):
        print(f'{self.rest_name} is open')
tb = restaurant('Taco Bell', 'Mexican food')
ob = restaurant('Out Back', 'Steak')
jb = restaurant('Jack in the Box', 'Burgers')

tb.describe_rest()
tb.rest_open()
ob.describe_rest()
ob.rest_open()
jb.describe_rest()
jb.rest_open()