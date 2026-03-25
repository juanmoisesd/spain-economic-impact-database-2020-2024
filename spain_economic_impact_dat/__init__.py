"""This dataset compiles key macroeconomic and financial indicators for Spain covering the period 2020&
DOI: https://github.com/juanmoisesd/spain-economic-impact-database-2020-2024 | GitHub: https://github.com/juanmoisesd/spain-economic-impact-database-2020-2024"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/spain-economic-impact-database-2020-2024".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). This dataset compiles key macroeconomic and financial indicators for Spain cover. Zenodo. https://github.com/juanmoisesd/spain-economic-impact-database-2020-2024'
def info(): print(f"Dataset: This dataset compiles key macroeconomic and financial indicators for Spain cover\nDOI: https://github.com/juanmoisesd/spain-economic-impact-database-2020-2024\nGitHub: https://github.com/juanmoisesd/spain-economic-impact-database-2020-2024")