import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page Config
st.set_page_config(page_title="Swiggy Analytics Dashboard", layout="wide")

# Custom CSS to match Swiggy Branding
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stMetric { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 5px solid #FC8019; }
    h1 { color: #FC8019; font-weight: 800; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    file_path = 'data/swiggy_delivery_data.csv'
    if not os.path.exists(file_path):
        st.error("Data file not found! Please run 'python scripts/generate_data.py' first.")
        return None
    df = pd.read_csv(file_path)
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    return df

df = load_data()

if df is not None:
    # Sidebar Filters
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Swiggy_logo.svg/1200px-Swiggy_logo.svg.png", width=150)
    st.sidebar.title("Dashboard Filters")
    
    city_filter = st.sidebar.multiselect("Select City", options=df['City'].unique(), default=df['City'].unique())
    food_filter = st.sidebar.multiselect("Food Category", options=df['Food_Type'].unique(), default=df['Food_Type'].unique())
    
    # Filter Data
    filtered_df = df[(df['City'].isin(city_filter)) & (df['Food_Type'].isin(food_filter))]
    
    # Header
    st.title("SWIGGY RESTAURANT DATA ANALYSIS")
    st.caption("End-to-End Business Insights Dashboard (Dynamic Python Version)")
    
    # KPI Row
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    avg_rating = filtered_df['Ratings'].mean()
    avg_price = filtered_df['Order_Value'].mean()
    total_rest = filtered_df['Restaurant_Name'].nunique()
    avg_delivery = filtered_df['Delivery_Time'].mean()
    
    kpi1.metric("Avg Rating", f"{avg_rating:.2f} ★")
    kpi2.metric("Avg Price", f"₹{avg_price:.2f}")
    kpi3.metric("# Restaurants", f"{total_rest}")
    kpi4.metric("Avg Delivery Time", f"{avg_delivery:.0f} mins")
    
    st.markdown("---")
    
    # Charts Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 5 Most Served Food Types")
        fig1 = px.pie(filtered_df, names='Food_Type', hole=0.4, color_discrete_sequence=px.colors.sequential.Oranges_r)
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        st.subheader("Top 10 Areas with Most Restaurants")
        area_counts = filtered_df.groupby('Area').size().reset_index(name='Count').sort_values('Count', ascending=False).head(10)
        fig2 = px.bar(area_counts, x='Area', y='Count', color_discrete_sequence=['#FC8019'])
        st.plotly_chart(fig2, use_container_width=True)
        
    # Charts Row 2
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Avg Price-wise Most Expensive Areas")
        area_price = filtered_df.groupby('Area')['Order_Value'].mean().reset_index().sort_values('Order_Value', ascending=False).head(10)
        fig3 = px.bar(area_price, y='Area', x='Order_Value', orientation='h', color_discrete_sequence=['#ffe8cc'])
        fig3.update_traces(marker_line_color='#FC8019', marker_line_width=1.5)
        st.plotly_chart(fig3, use_container_width=True)
        
    with col4:
        st.subheader("Order Distribution by City")
        fig4 = px.histogram(filtered_df, x="City", color="Payment_Method", barmode="group", color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig4, use_container_width=True)

    st.sidebar.markdown("---")
    st.sidebar.info("Learn Data Analysis @Slidescope")
