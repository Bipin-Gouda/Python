# Function gives nth Fibonacci number  0 1 1 2 3 5 8

def F(n):
    if n == 0 or n == 1:
     return n
    else:
     return F(n-1)+F(n-2)

if __name__ == '__main__':
    
    n=int(input())
    for i in range(n):
        print(F(i),end=" ")





