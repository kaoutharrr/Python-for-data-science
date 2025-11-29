from load_csv import load
import matplotlib.pyplot as plt


def converter(val) -> float:
    "covert strings ending with M or K  to floats"
    s = str(val)
    if s.endswith('K'):
        return float(s[:-1]) * 1000
    if s.endswith('M'):
        return float(s[:-1] ) * 1_000_000
    return float(s)

def main():
    """displays the country information of two countries as a graph"""
    
    try:
        df = load("population_total.csv")
        # my_country = 'Morocco'
        # other_campus = 'Japan'
        target_years = [str(year) for year in range(1800, 2051) ]
        my_campus = df[df['country'] == 'Morocco'][target_years]
        other_campus = df[df['country'] == 'Japan'][target_years]
        pop_campus = [converter(val) for val in my_campus.values[0]]
        pop_other = [converter(val) for val in other_campus.values[0]]
        years_int = [int(year) for year in target_years]
        
        plt.plot(years_int, pop_campus, label="Morocco")
        plt.plot(years_int, pop_other, label="Japan")

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(range(1800, 2051, 40))
        ax = plt.gca()  # Get current axes
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M'))
        
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Errr : {e}")


if __name__ == "__main__":
    main()