import pandas as pd

class FinanceService:
    def __init__(self, file_path="data/finance_data.xlsx"):
        self.df = pd.read_excel(file_path)
    
    def expense_vs_budget(self):
        return self.df.groupby("Department")[["Amount", "Budget"]].sum().reset_index()
    
    def overspent_departments(self):
        self.df["Overspend"] = self.df["Amount"] - self.df["Budget"]
        return self.df.groupby("Department")["Overspend"].sum().reset_index().sort_values("Overspend", ascending=False)
    
    def monthly_expense_trend(self, dept="IT"):
        dept_df = self.df[self.df["Department"] == dept]
        dept_df["Month"] = pd.to_datetime(dept_df["Date"]).dt.to_period("M")
        return dept_df.groupby("Month")["Amount"].sum().reset_index()
