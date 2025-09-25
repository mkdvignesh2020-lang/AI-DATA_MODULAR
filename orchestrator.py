from services.retail_service import RetailService
from services.finance_service import FinanceService
from governance.logger import GovernanceLogger

class Orchestrator:
    def __init__(self):
        self.retail = RetailService()
        self.finance = FinanceService()
        self.logger = GovernanceLogger()

    def query(self, user_input):
        user_input = user_input.lower()
        
        if "revenue by region" in user_input:
            result = self.retail.get_total_revenue_by_region()
            self.logger.log(user_input, "RetailService", result.head())
            return result
        
        elif "overspent" in user_input:
            result = self.finance.overspent_departments()
            self.logger.log(user_input, "FinanceService", result.head())
            return result
        
        elif "monthly sales" in user_input:
            result = self.retail.monthly_sales_trend()
            self.logger.log(user_input, "RetailService", result.head())
            return result
        
        elif "expense vs budget" in user_input:
            result = self.finance.expense_vs_budget()
            self.logger.log(user_input, "FinanceService", result.head())
            return result
        
        else:
            self.logger.log(user_input, "UnknownService", "No match")
            return "I don’t know how to handle that query yet."
