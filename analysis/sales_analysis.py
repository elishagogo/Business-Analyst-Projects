"""
Sales Data Analysis Script
This script analyzes e-commerce sales data to provide business insights
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_data(file_path):
    """Load sales data from CSV file"""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def calculate_metrics(df):
    """Calculate key business metrics"""
    metrics = {
        'total_revenue': df['Total_Amount'].sum(),
        'total_orders': len(df),
        'average_order_value': df['Total_Amount'].mean(),
        'total_customers': df['Customer_ID'].nunique(),
        'total_products_sold': df['Quantity'].sum()
    }
    return metrics

def analyze_by_category(df):
    """Analyze sales by product category"""
    category_analysis = df.groupby('Product_Category').agg({
        'Total_Amount': ['sum', 'mean', 'count'],
        'Quantity': 'sum'
    }).round(2)
    return category_analysis

def analyze_by_region(df):
    """Analyze sales by region"""
    region_analysis = df.groupby('Region').agg({
        'Total_Amount': ['sum', 'mean', 'count'],
        'Customer_ID': 'nunique'
    }).round(2)
    return region_analysis

def analyze_payment_methods(df):
    """Analyze preferred payment methods"""
    payment_analysis = df.groupby('Payment_Method').agg({
        'Order_ID': 'count',
        'Total_Amount': 'sum'
    }).round(2)
    return payment_analysis

def top_customers(df, n=5):
    """Identify top N customers by revenue"""
    customer_analysis = df.groupby('Customer_ID').agg({
        'Total_Amount': 'sum',
        'Order_ID': 'count'
    }).sort_values('Total_Amount', ascending=False).head(n)
    return customer_analysis

def generate_report(df):
    """Generate comprehensive analysis report"""
    print("=" * 60)
    print("SALES ANALYSIS REPORT")
    print("=" * 60)
    print()
    
    # Overall Metrics
    metrics = calculate_metrics(df)
    print("OVERALL METRICS")
    print("-" * 60)
    print(f"Total Revenue: ${metrics['total_revenue']:,.2f}")
    print(f"Total Orders: {metrics['total_orders']}")
    print(f"Average Order Value: ${metrics['average_order_value']:.2f}")
    print(f"Total Customers: {metrics['total_customers']}")
    print(f"Total Products Sold: {metrics['total_products_sold']}")
    print()
    
    # Category Analysis
    print("SALES BY CATEGORY")
    print("-" * 60)
    print(analyze_by_category(df))
    print()
    
    # Region Analysis
    print("SALES BY REGION")
    print("-" * 60)
    print(analyze_by_region(df))
    print()
    
    # Payment Methods
    print("PAYMENT METHOD ANALYSIS")
    print("-" * 60)
    print(analyze_payment_methods(df))
    print()
    
    # Top Customers
    print("TOP 5 CUSTOMERS")
    print("-" * 60)
    print(top_customers(df))
    print()

if __name__ == "__main__":
    # Load and analyze data
    data_path = "../data/sample_sales_data.csv"
    df = load_data(data_path)
    generate_report(df)
