# src/runner.py
import time
from src.metrics import test_runs_total, test_failures_total, test_duration_seconds

def run_test(test_func):
    """
    Runs a single test function and records metrics
    """
    start = time.time()
    test_runs_total.inc()
    
    try:
        test_func()
    except Exception:
        test_failures_total.inc()
        raise
    finally:
        duration = time.time() - start
        test_duration_seconds.set(duration)
        print(f"Test {test_func.__name__} completed in {duration:.2f}s")

# Example of running all tests
if __name__ == "__main__":
    import importlib
    import os

    test_dir = os.path.join(os.path.dirname(__file__), '../tests')
    for file in os.listdir(test_dir):
        if file.startswith('test_') and file.endswith('.py'):
            module_name = f"tests.{file[:-3]}"
            module = importlib.import_module(module_name)
            # Run all functions in the module that start with 'test_'
            for attr in dir(module):
                if attr.startswith('test_'):
                    test_func = getattr(module, attr)
                    if callable(test_func):
                        run_test(test_func)

    print("All tests executed. Metrics available at http://localhost:8000/metrics")
