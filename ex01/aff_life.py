import matplotlib.pyplot as plt
from load_csv import load


def main():
    """displays the information of your campus from a csv file in a graph """

    df = load("life_expectancy_years.csv")
    if df is None:
        return
    try:
        country_data = df[df['country'] == 'Morocco']
        years = df.columns[1:].to_numpy()
        values = country_data.values[0][1:]
        plt.plot(years, values)
        plt.title("Morocco Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.xticks(years[::40])
        plt.show()
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
