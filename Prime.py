def prime(x):
    if x > 0:
        for i in range(2, x):
            if (x % i) == 0:
                return False
            else:
                return True

def palindrome(a):
    b = a[::-1]
    if b == a:
        return True
    else:
        return False

if __name__=="__main__":
    x = int(input('enter the integer:'))
    print(prime(x))
    a = input("Enter the data")
    print(palindrome(a))