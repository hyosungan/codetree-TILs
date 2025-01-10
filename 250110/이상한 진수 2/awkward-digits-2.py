a = input()

if '0' not in a:
    a=a[:len(a)-1]+'0'

else:
    for i in range(len(a)):
        if a[i]=='0':
            a=a[:i]+'1'+a[i+1:]
            break

decimal=0
for i in a:
    decimal=decimal*2+int(i)

print(decimal)