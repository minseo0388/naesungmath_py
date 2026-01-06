from src.Sequence.Arithmetic import Arithmetic
import sys

print("Verifying Sequence.Arithmetic Solver (Python)...")

# Case 1: Given a, d, n -> Find an, s
try:
    res1 = Arithmetic.solve(a=2, d=3, n=4)
    print(f"Case 1 (a,2, d,3, n,4): {res1}")
    if res1['an'] != 11 or res1['s'] != 26:
        raise Exception("Case 1 failed")
except Exception as e:
    print(e)
    sys.exit(1)

# Case 2: Given d, n, s -> Find a, an
try:
    res2 = Arithmetic.solve(d=3, n=4, s=26)
    print(f"Case 2 (d,3, n,4, s,26): {res2}")
    if res2['a'] != 2 or res2['an'] != 11:
        raise Exception("Case 2 failed")
except Exception as e:
    print(e)
    sys.exit(1)

# Case 3: Given a, an, s -> Find n, d
try:
    res3 = Arithmetic.solve(a=2, an=11, s=26)
    print(f"Case 3 (a,2, an,11, s,26): {res3}")
    if res3['n'] != 4 or res3['d'] != 3:
        raise Exception("Case 3 failed")
except Exception as e:
    print(e)
    sys.exit(1)

# Case 4: Given a, d, s -> Find n (Quadratic case)
try:
    res4 = Arithmetic.solve(a=2, d=3, s=26)
    print(f"Case 4 (a,2, d,3, s,26): {res4}")
    if res4['n'] != 4 or res4['an'] != 11:
        raise Exception("Case 4 failed")
except Exception as e:
    print(e)
    sys.exit(1)

print("All Python Solver tests passed!")
