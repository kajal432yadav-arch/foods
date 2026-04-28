import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_food_delivery_data(num_orders=5000):
    np.random.seed(42)
    random.seed(42)
    
    # Constants
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Pune', 'Chennai', 'Kolkata', 'Ahmedabad']
    restaurants = [
        'Biryani Blues', 'Pizza Hut', 'Burger King', 'KFC', 'Dominos', 
        'Wow! Momo', 'Subway', 'Haldirams', 'Paradise Biryani', 'Mc Donalds',
        'Taco Bell', 'Chai Point', 'Rolls Mania', 'The Good Bowl', 'Faasos'
    ]
    payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Cash on Delivery', 'Net Banking']
    delivery_statuses = ['Delivered', 'Cancelled', 'Delivered', 'Delivered', 'Delivered'] # Weighting 'Delivered'
    
    food_types = ['North Indian', 'Chinese', 'Biryani', 'South Indian', 'Desserts', 'Fast Food', 'Street Food', 'Continental']
    areas = ['Koramangala', 'HSR Layout', 'Indiranagar', 'Whitefield', 'Jayanagar', 'Gachibowli', 'Banjara Hills', 'Cyberabad', 'Powai', 'Andheri']
    
    data = []
    
    start_date = datetime(2023, 1, 1)
    
    for i in range(num_orders):
        order_id = f'ORD{10000 + i}'
        customer_id = f'CUST{random.randint(100, 1000)}'
        restaurant = random.choice(restaurants)
        city = random.choice(cities)
        area = random.choice(areas)
        food_type = random.choice(food_types)
        address = f"Street {random.randint(1, 100)}, {area}, {city}"
        
        # Order Date & Time
        days_offset = random.randint(0, 365)
        hour = random.choices(range(24), weights=[1,1,1,1,1,2,5,10,12,8,6,10,15,12,10,8,12,18,25,20,15,10,5,2])[0]
        order_date = start_date + timedelta(days=days_offset, hours=hour, minutes=random.randint(0, 59))
        
        # Order Value & Distance
        order_value = round(random.uniform(150, 2500), 2)
        distance = round(random.uniform(0.5, 15.0), 1)
        
        # Delivery Time (influenced by distance and random traffic)
        base_time = 15
        time_per_km = 3
        traffic_delay = random.randint(5, 20)
        delivery_time_mins = int(base_time + (distance * time_per_km) + traffic_delay)
        
        # Discount (10-30% on some orders)
        discount = 0
        if random.random() < 0.4:
            discount = round(order_value * random.choice([0.1, 0.15, 0.2, 0.5]), 2)
        
        # Rating (1 to 5)
        if delivery_time_mins > 45:
            rating = random.choices([1, 2, 3, 4, 5], weights=[20, 30, 20, 20, 10])[0]
        else:
            rating = random.choices([1, 2, 3, 4, 5], weights=[5, 5, 10, 40, 40])[0]
            
        status = random.choice(delivery_statuses)
        payment = random.choice(payment_methods)
        
        data.append([
            order_id, customer_id, restaurant, city, area, food_type, address, order_date, 
            delivery_time_mins, order_value, payment, rating, 
            status, distance, discount
        ])
    
    columns = [
        'Order_ID', 'Customer_ID', 'Restaurant_Name', 'City', 'Area', 'Food_Type', 'Address', 'Order_Date', 
        'Delivery_Time', 'Order_Value', 'Payment_Method', 'Ratings', 
        'Delivery_Status', 'Distance', 'Discount'
    ]
    
    df = pd.DataFrame(data, columns=columns)
    
    # Ensure directory exists
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
        
    # Save to CSV
    df.to_csv('data/swiggy_delivery_data.csv', index=False)
    print(f"Dataset generated with {num_orders} rows in 'data/swiggy_delivery_data.csv'")

if __name__ == "__main__":
    generate_food_delivery_data()
