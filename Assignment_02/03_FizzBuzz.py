def fizzBuzz(n):
    result = []
    
    # Loop from 1 up to n (inclusive)
    for i in range(1, n + 1):
        # Check for multiples of BOTH 3 and 5 first!
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))  # Convert number to string
            
    return result


# --- Hardcoded Test Run ---
n = 15
print(fizzBuzz(n))