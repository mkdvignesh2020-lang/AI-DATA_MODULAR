import datetime

class GovernanceLogger:
    def __init__(self, logfile="data/governance.log"):
        self.logfile = logfile
    
    def log(self, user_query, service_used, result_preview):
        with open(self.logfile, "a") as f:
            f.write(f"[{datetime.datetime.now()}] QUERY: {user_query} | SERVICE: {service_used} | RESULT: {str(result_preview)[:200]}\n")
