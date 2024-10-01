def print_HelloWorld(n):
    if n==1:
        return

    else:
        print_HelloWorld(n-1)
        print("HelloWorld")

print_HelloWorld(5)