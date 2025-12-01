from load_csv import load
import matplotlib.pyplot as plt


def main():
    """displays the projection of life expectancy in
    relation to the gross national product of
    the year 1900 for each country"""
    try:
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df_life = load("life_expectancy_years.csv")
        gdp_1900 = gdp[["country", "1900"]]
        life_1900 = df_life[["country", "1900"]]
        merged = gdp_1900.merge(life_1900,
                                on="country", suffixes=("_gdp", "_life"))
        merged["1900_gdp"] = merged["1900_gdp"].apply(float)
        merged["1900_life"] = merged["1900_life"].apply(float)
        plt.scatter(merged["1900_gdp"], merged["1900_life"], label="Countries")
        plt.title("Life Expectancy vs GDP per person (1900)")
        plt.xlabel("GDP per person (1900)")
        plt.ylabel("Life expectancy (1900)")
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
