from load_csv import load
import matplotlib.pyplot as plt

def main():
    """displays the country information of two countries as a graph"""
    
    try:
        df = load("population_total.csv")
        country_data = df[df['country'] == 'Morocco']
        
    except Exception as e:
        print(f"Errr : {e}")


if __name__ == "__main__":
    main()