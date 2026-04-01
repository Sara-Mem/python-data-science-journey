# Take an integer from user and print:

# Even or Odd
# Positive or Negative
# Divisible by 5 or not

def analysis_num():
    num =  int(input("Pleas enter a number:"))
    if num !=0: 
          return (
               ("Even" if num%2 == 0 else "Odd") 
               + (", positive" if num>0 else ", negative" )
               + (", divisible by 5"  if num%5 ==0 else ", is not divisible by 5")
          )

print(analysis_num())