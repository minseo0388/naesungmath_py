import sys
import math
from formulas.geometric_progression import GeometricProgression

def run_verify():
    print("Verifying GeometricProgression Solver (Python)...")
    errors = 0

    def assert_close(actual, expected, name):
        nonlocal errors
        if actual is None:
            print(f"[FAIL] {name} is None, expected {expected}")
            errors += 1
            return
        if abs(actual - expected) > 1e-9:
            print(f"[FAIL] {name}: got {actual}, expected {expected}")
            errors += 1
        else:
            # print(f"[PASS] {name}: got {actual}")
            pass

    try:
        # Case 1: Given a, r, n -> Find an, s
        # a=2, r=3, n=4 -> an=162, s=80
        res1 = GeometricProgression.solve(a=2, r=3, n=4)
        print(f"Case 1 (a=2, r=3, n=4) -> an={res1['an']}, s={res1['s']}")
        assert_close(res1['an'], 162, "Case 1 an")
        assert_close(res1['s'], 80, "Case 1 s")

        # Case 2: Given a, n, an -> Find r
        # a=2, n=4, an=162 -> r=3
        res2 = GeometricProgression.solve(a=2, n=4, an=162)
        print(f"Case 2 (a=2, n=4, an=162) -> r={res2['r']}")
        assert_close(res2['r'], 3, "Case 2 r")

        # Case 3: Given a, r, s -> Find n
        # a=2, r=3, s=80 -> n=4
        res3 = GeometricProgression.solve(a=2, r=3, s=80)
        print(f"Case 3 (a=2, r=3, s=80) -> n={res3['n']}")
        assert_close(res3['n'], 4, "Case 3 n")

        # Case 4: Infinity Sum
        # a=10, r=0.5 -> infinity_sum=20
        res4 = GeometricProgression.solve(a=10, r=0.5)
        print(f"Case 4 (a=10, r=0.5) -> infinity_sum={res4['infinity_sum']}")
        assert_close(res4['infinity_sum'], 20, "Case 4 infinity_sum")

        # Case 5: Find a from infinity_sum
        # infinity_sum=20, r=0.5 -> a=10
        res5 = GeometricProgression.solve(infinity_sum=20, r=0.5)
        print(f"Case 5 (inf=20, r=0.5) -> a={res5['a']}")
        assert_close(res5['a'], 10, "Case 5 a")

        if errors == 0:
            print("All Python Solver tests passed!")
        else:
            print(f"{errors} tests failed.")
            sys.exit(1)

    except Exception as e:
        print(f"Error running validation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_verify()
