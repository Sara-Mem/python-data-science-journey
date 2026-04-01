def Profile_formatter():
    name, age, country = input("Please enter your name, age, country:").split(", ")
    print(f"Hello {name} from {country}. Next year you will be {int(age)+1}.")

Profile_formatter()