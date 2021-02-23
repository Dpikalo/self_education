class A:
    pass


b = {10: 'daw'}
a = A()
b[A()] = 'adw'
b[a] = 'dawdawdwa'

print(b)