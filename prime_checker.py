def is_prime(num):
    numbers = list(range(2, int(num ** 0.5) + 1))  
    for number in numbers:
        if num % number == 0:
            return False
    return True
  
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 10, 17, 18, 23, 25, 29]
    for n in test_numbers:
        print(f"{n} is prime: {is_prime(n)}")
