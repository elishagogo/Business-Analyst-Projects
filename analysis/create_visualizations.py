"""
Data Visualization Script for Sales Analysis
Creates charts and graphs for business insights
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data(file_path):
    """Load sales data from CSV file"""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def plot_revenue_by_category(df, output_dir):
    """Create bar chart of revenue by product category"""
    category_revenue = df.groupby('Product_Category')['Total_Amount'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    category_revenue.plot(kind='bar', color='steelblue')
    plt.title('Total Revenue by Product Category', fontsize=16, fontweight='bold')
    plt.xlabel('Product Category', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/revenue_by_category.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: revenue_by_category.png")

def plot_sales_trend(df, output_dir):
    """Create line chart showing sales trend over time"""
    daily_sales = df.groupby('Date')['Total_Amount'].sum().reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(daily_sales['Date'], daily_sales['Total_Amount'], marker='o', linewidth=2, markersize=4, color='darkgreen')
    plt.title('Daily Sales Trend', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/sales_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: sales_trend.png")

def plot_regional_performance(df, output_dir):
    """Create pie chart of sales by region"""
    region_sales = df.groupby('Region')['Total_Amount'].sum()
    
    plt.figure(figsize=(10, 8))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', 
            startangle=90, colors=colors, textprops={'fontsize': 12})
    plt.title('Sales Distribution by Region', fontsize=16, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/regional_performance.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: regional_performance.png")

def plot_payment_methods(df, output_dir):
    """Create bar chart of payment method usage"""
    payment_counts = df['Payment_Method'].value_counts()
    
    plt.figure(figsize=(10, 6))
    payment_counts.plot(kind='bar', color='coral')
    plt.title('Payment Method Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Payment Method', fontsize=12)
    plt.ylabel('Number of Transactions', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/payment_methods.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: payment_methods.png")

def plot_top_products(df, output_dir):
    """Create horizontal bar chart of top 10 products by revenue"""
    product_revenue = df.groupby('Product_Name')['Total_Amount'].sum().sort_values(ascending=True).tail(10)
    
    plt.figure(figsize=(10, 8))
    product_revenue.plot(kind='barh', color='mediumpurple')
    plt.title('Top 10 Products by Revenue', fontsize=16, fontweight='bold')
    plt.xlabel('Revenue ($)', fontsize=12)
    plt.ylabel('Product', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/top_products.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: top_products.png")

def plot_category_quantity(df, output_dir):
    """Create bar chart of quantity sold by category"""
    category_quantity = df.groupby('Product_Category')['Quantity'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    category_quantity.plot(kind='bar', color='teal')
    plt.title('Quantity Sold by Product Category', fontsize=16, fontweight='bold')
    plt.xlabel('Product Category', fontsize=12)
    plt.ylabel('Quantity Sold', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/category_quantity.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: category_quantity.png")

def create_dashboard(df, output_dir):
    """Create a comprehensive dashboard with multiple visualizations"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Sales Analytics Dashboard', fontsize=20, fontweight='bold')
    
    # Revenue by Category
    category_revenue = df.groupby('Product_Category')['Total_Amount'].sum().sort_values(ascending=False)
    axes[0, 0].bar(range(len(category_revenue)), category_revenue.values, color='steelblue')
    axes[0, 0].set_xticks(range(len(category_revenue)))
    axes[0, 0].set_xticklabels(category_revenue.index, rotation=45, ha='right')
    axes[0, 0].set_title('Revenue by Category')
    axes[0, 0].set_ylabel('Revenue ($)')
    
    # Regional Distribution
    region_sales = df.groupby('Region')['Total_Amount'].sum()
    axes[0, 1].pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=90)
    axes[0, 1].set_title('Regional Distribution')
    
    # Payment Methods
    payment_counts = df['Payment_Method'].value_counts()
    axes[0, 2].bar(range(len(payment_counts)), payment_counts.values, color='coral')
    axes[0, 2].set_xticks(range(len(payment_counts)))
    axes[0, 2].set_xticklabels(payment_counts.index, rotation=45, ha='right')
    axes[0, 2].set_title('Payment Methods')
    axes[0, 2].set_ylabel('Transactions')
    
    # Sales Trend
    daily_sales = df.groupby('Date')['Total_Amount'].sum().reset_index()
    axes[1, 0].plot(daily_sales['Date'], daily_sales['Total_Amount'], marker='o', linewidth=2, markersize=3, color='darkgreen')
    axes[1, 0].set_title('Daily Sales Trend')
    axes[1, 0].set_xlabel('Date')
    axes[1, 0].set_ylabel('Revenue ($)')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # Top Products
    top_products = df.groupby('Product_Name')['Total_Amount'].sum().sort_values(ascending=False).head(5)
    axes[1, 1].barh(range(len(top_products)), top_products.values, color='mediumpurple')
    axes[1, 1].set_yticks(range(len(top_products)))
    axes[1, 1].set_yticklabels(top_products.index)
    axes[1, 1].set_title('Top 5 Products')
    axes[1, 1].set_xlabel('Revenue ($)')
    
    # Key Metrics
    metrics_text = f"""
    KEY METRICS
    
    Total Revenue: ${df['Total_Amount'].sum():,.2f}
    Total Orders: {len(df)}
    Avg Order Value: ${df['Total_Amount'].mean():.2f}
    Total Customers: {df['Customer_ID'].nunique()}
    Products Sold: {df['Quantity'].sum()}
    """
    axes[1, 2].text(0.1, 0.5, metrics_text, fontsize=12, verticalalignment='center', 
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Summary Metrics')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/sales_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Created: sales_dashboard.png")

def generate_all_visualizations(data_path, output_dir):
    """Generate all visualizations"""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    df = load_data(data_path)
    
    print("\nGenerating visualizations...")
    print("=" * 60)
    
    # Generate all plots
    plot_revenue_by_category(df, output_dir)
    plot_sales_trend(df, output_dir)
    plot_regional_performance(df, output_dir)
    plot_payment_methods(df, output_dir)
    plot_top_products(df, output_dir)
    plot_category_quantity(df, output_dir)
    create_dashboard(df, output_dir)
    
    print("=" * 60)
    print(f"\n✓ All visualizations saved to: {output_dir}")

if __name__ == "__main__":
    data_path = "../data/sample_sales_data.csv"
    output_dir = "../visualizations"
    generate_all_visualizations(data_path, output_dir)
