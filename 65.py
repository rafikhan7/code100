from datetime import datetime

age =int(input("what is your age?"))
age_years = datetime.now().year-age
print("We think you were born back in %s" % age_years)