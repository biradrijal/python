def prime (a):
        for i in range (2, a):
            if a % 2 == 0:
                return False
        return True

print(prime(10))

