from orchestrator import Orchestrator
import matplotlib.pyplot as plt

orch = Orchestrator()

def run_query(query):
    result = orch.query(query)
    
    if isinstance(result, str):
        print(result)
    else:
        print(result.head())  # preview
    
        # Simple auto-viz
        if "Revenue" in result.columns:
            result.plot(x=result.columns[0], y="Revenue", kind="bar", figsize=(8,4))
            plt.title(query)
            plt.show()
        elif "Amount" in result.columns:
            result.plot(x=result.columns[0], y="Amount", kind="bar", figsize=(8,4))
            plt.title(query)
            plt.show()

if __name__ == "__main__":
    while True:
        q = input("Ask a question (or 'exit'): ")
        if q.lower() == "exit":
            break
        run_query(q)
