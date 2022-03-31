a=100
b=100
palindromes=[0]
while a<1000:
    while b<1000:
        p=a*b
        sp=str(p)
        ip=sp[::-1]
        if sp==ip:
            palindromes.append(p)
        b=b+1
    b=100
    a=a+1
palindromes.sort()
print(palindromes[-1])