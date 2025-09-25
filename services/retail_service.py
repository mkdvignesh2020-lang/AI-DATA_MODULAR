import pandas as pd

class RetailService:
    def __init__(self, file_path="data/retail_sales.xlsx"):
        self.df = pd.read_excel(file_path)
    
    def get_total_revenue_by_region(self):
        return self.df.groupby("Region")["Revenue"].sum().reset_index()
    
    def top_products_by_profit(self, n=5):
        return self.df.groupby("Product")["Profit"].sum().reset_index().sort_values("Profit", ascending=False).head(n)
    
    def monthly_sales_trend(self):
        self.df["Month"] = pd.to_datetime(self.df["Date"]).dt.to_period("M")
        return self.df.groupby("Month")["Revenue"].sum().reset_index()
