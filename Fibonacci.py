# David Prato CIS 261 Lab Fibonacci

def fib(n):
    if n == 0:
        return 0 # exit 
    elif n == 1:
        return 1 # exit 2
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    for i in range(16): # 1 to 16
        print(fib(i), end=",")
    print("...")

if __name__ == "__main__":
    main()

#So when we reach n == 2 we have already 0, 1, 
#Remember returns goes into the fib(n) We are not going directly in the for loop until we output
