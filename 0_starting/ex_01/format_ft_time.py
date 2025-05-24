import time
import datetime

# See https://www.w3schools.com/python/gloss_python_date_format_codes.asp

def main():
    time_in_seconds = time.time()

    # :, Displays the thousands separators, .4f is the decimal precision.
    print(f"Seconds since January 1, 1970: {time_in_seconds:,.4f} ", end="")
    print(f"or {time_in_seconds:e} in scientific notation")

    # Extract the current date, and format it.
    simple_date = datetime.datetime.now().strftime("%b %d %Y") 
    print(simple_date)

if __name__ == "__main__":
    main()