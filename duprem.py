def no_duplicate(l):
    dup = []
    [dup.append(x) for x in l if x not in dup]
    return dup

a= input("Enter a sentence with duplicates: ")
a=' '.join(no_duplicate(a.split()))
print(a)