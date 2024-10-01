N=int(input())
def print_HelloWorld(n):
    if n==0:
        return

    else:
        print_HelloWorld(n-1)
        print("HelloWorld")

print_HelloWorld(N)