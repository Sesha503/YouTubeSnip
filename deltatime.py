from dateutil import parser
from datetime import timedelta

def delta(dt_str1,dt_str2):
    # Parse the strings into datetime objects
    dt1 = parser.parse(dt_str1)
    dt2 = parser.parse(dt_str2)

    # Calculate the difference
    delta = dt1 - dt2
    # Subtract 60 seconds
    delta_minus_45 = delta - timedelta(seconds=45)
    # Output the result
    print(f"Time difference: {delta}")
    print(delta_minus_45)
    print(f"Total seconds: {delta.total_seconds()} seconds")
    print(delta_minus_45.total_seconds())
    sec=delta_minus_45.total_seconds()
    l=[sec,delta_minus_45]
    
    return l