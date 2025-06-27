from load_csv import load
import pandas as pd

def ft_aff_file(data: pd.DataFrame) -> None:
    country = input("Select your country: ").strip().title()

    print(f"Data of {country} = \n{data.loc(country)}")
    # try:
    #     ...
    # except Exception as e:
    #     ...

def main() -> None:
    name_file = "life_expectancy_years.csv"
    data = load(name_file)

    print(f"ORIGINAL DATA = \n{data}")

    ft_aff_file(data)


if __name__ == "__main__":
    main()