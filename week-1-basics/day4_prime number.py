def prime_number(numbers):
    prime_nums = []
    for i in numbers:
        if i<2:
            continue
        is_prime = True
        for j in range(2, i//2+1):
            if i%j == 0:
                is_prime = False
                break
                

        if is_prime == True:
            prime_nums.append(i)   
    return prime_nums

print(prime_number([1, 2, 3, 4, 5, 8]))

        
        