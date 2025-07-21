import libpy as lp

print(f"fonction : gcd\n")
print(lp.gcd(50, 20))
print(f"fonction : clamp\n")
print(lp.clamp(41, 50.5, 60))
print(f"fonction : chunk\n")
print(lp.chunk([10, 20 , 30, 40, 50, 60], 1))
print(f"fonction : unique\n")
print(lp.unique(
    [10, 11, 12, 20, 13, 21, 33, 30, 0, 1],
    key=lambda n: n // 10
))