import random

products = ['Laptop', 'Monitor', 'Keyboard',
            'Mouse', 'Webcam','Headset', 'Docking Station',
            'USB Hub', 'Desk Lamp', 'Surge Protector']
print(f"The Product of the Day is: {random.choice(products)}")

print(random.sample(products, 3))

random.shuffle(products)

print(products)

print(f"Transaction Count: {random.randint(50, 300)}")