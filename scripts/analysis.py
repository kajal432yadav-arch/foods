import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load data
try:
    df = pd.read_csv('data/swiggy_delivery_data.csv')
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
except FileNotFoundError:
    print("Error: Data file not found. Please run scripts/generate_data.py first.")
    exit()

# 1. Customer Segmentation
def customer_segmentation(df):
    customer_stats = df.groupby('Customer_ID').agg({
        'Order_ID': 'count',
        'Order_Value': 'sum'
    }).rename(columns={'Order_ID': 'Total_Orders', 'Order_Value': 'Total_Revenue'})
    
    # Simple segmentation
    low_threshold = customer_stats['Total_Revenue'].quantile(0.33)
    high_threshold = customer_stats['Total_Revenue'].quantile(0.66)
    
    def segment(rev):
        if rev <= low_threshold: return 'Low Value'
        if rev <= high_threshold: return 'Medium Value'
        return 'High Value'
    
    customer_stats['Segment'] = customer_stats['Total_Revenue'].apply(segment)
    print("\n--- Customer Segmentation ---")
    print(customer_stats['Segment'].value_counts())
    return customer_stats

# 2. Delivery Time Prediction (Basic ML)
def predict_delivery_time(df):
    X = df[['Distance']]
    y = df['Delivery_Time']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    print(f"\n--- Delivery Time Prediction (R^2 Score) ---")
    print(f"Model Accuracy: {score:.2f}")
    
    # Predict for a 5km delivery
    prediction = model.predict([[5]])[0]
    print(f"Predicted delivery time for 5km: {prediction:.2f} mins")

# 3. Peak Time Analysis
def peak_time_analysis(df):
    df['Hour'] = df['Order_Date'].dt.hour
    hourly_orders = df.groupby('Hour')['Order_ID'].count()
    
    print("\n--- Peak Order Times ---")
    print(hourly_orders.sort_values(ascending=False).head(5))
    
    # Save a plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=hourly_orders.index, y=hourly_orders.values, palette='viridis')
    plt.title('Orders by Hour of Day')
    plt.xlabel('Hour')
    plt.ylabel('Number of Orders')
    
    # Ensure directory exists
    import os
    if not os.path.exists('notebooks'):
        os.makedirs('notebooks')
        
    plt.savefig('notebooks/peak_time_analysis.png')
    print("Chart saved to notebooks/peak_time_analysis.png")

# 4. Discount Impact Analysis
def discount_impact(df):
    # Profit calculation (Assumed 25% margin - discount)
    df['Profit'] = (df['Order_Value'] * 0.25) - df['Discount']
    
    avg_profit_discounted = df[df['Discount'] > 0]['Profit'].mean()
    avg_profit_non_discounted = df[df['Discount'] == 0]['Profit'].mean()
    
    print("\n--- Discount Impact Analysis ---")
    print(f"Avg Profit (Discounted): {avg_profit_discounted:.2f}")
    print(f"Avg Profit (Non-Discounted): {avg_profit_non_discounted:.2f}")

if __name__ == "__main__":
    customer_segmentation(df)
    predict_delivery_time(df)
    peak_time_analysis(df)
    discount_impact(df)
