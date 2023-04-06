def factorial(x):
    if(x >= 1):
        x *= factorial(x-1)
        return x
    if(x<0):
        return None
    elif x==0:
        return 1
    
def main():
    for i in range(15):
        if(i%2 == 0):
            print(factorial(i))

if __name__ == '__main__':

    main()
