# Max of Three Numbers

# Take 3 numbers from user
# Print the largest number (without using max())

def max_3(a, b, c):
    return (
        ("Largest is ")+
        (f"{a}" if a>=b and a>=c else "") +
        (f"{b}" if b>=a and b>=c else "")  +
        (f"{c}" if c>=a and c>=b else "") 
                )

print(max_3(0, 5, 4))