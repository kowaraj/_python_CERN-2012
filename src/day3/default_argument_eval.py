def foo(a, x = []):
    x.append(a)
    return x

print foo(1)
print foo(2)
print foo(3)
print foo(4)

# [1, 1]
# [1, 1, 2]
# [1, 1, 2, 3]
# [1, 1, 2, 3, 4]


# correct:
def foo(a, x = []):
    if x is None:
        x = []
    x.append(a)
    return x

print foo(1)
print foo(2)
print foo(3)
print foo(4)
