def is_prime_number(n):
    end = int(n**(1/2))
    for i in range(2, end + 1):
        if n % i == 0:
            return False
    return True