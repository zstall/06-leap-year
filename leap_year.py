# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence
def is_leap_year(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    elif year%4==0:
        return True
    else:
        return False
