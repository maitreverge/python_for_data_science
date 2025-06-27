import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a Pandas DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame or None if an error occurred.
    """
    try:
        extension = path.split(".")[-1]

        if not os.access(path, os.R_OK) or extension != "csv":
            print(f"{path} can't be accessed")
            return None
    except Exception as e:
        print(f"Error : {e}")
        return None

    result = pd.read_csv(path)
    print(f"Loading dataset of dimensions: {result.shape}")
    return result


def main() -> None:
    """
    Main function to run the CSV loading application.
    """
    name_file = "life_expectancy_years.csv"
    print(load(name_file))


if __name__ == "__main__":
    main()
