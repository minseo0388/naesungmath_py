from formulas.geometric_progression import GeometricProgression

def test_gp_distinction():
    print("--- Testing GeometricProgression Distinction ---")

    # Case 1: Given a, r, n -> Find an
    # We pass 'r' but NOT 'an'
    print("\n[Case 1] Input: a=2, r=2, n=3 (Target: an=16)")
    # Note: Using Keyword Arguments is MANDATORY for Smart Solvers to avoid ambiguity
    res1 = GeometricProgression.solve(a=2, r=2, n=3)
    print(f"Result: an={res1['an']}, r={res1['r']}")
    
    if res1['an'] == 16:
        print("✅ Correctly identified (a,r,n) case.")
    else:
        print("❌ Failed Case 1")

    # Case 2: Given a, an, n -> Find r
    # We pass 'an' but NOT 'r'
    print("\n[Case 2] Input: a=2, an=16, n=3 (Target: r=2)")
    res2 = GeometricProgression.solve(a=2, an=16, n=3)
    print(f"Result: an={res2['an']}, r={res2['r']}")

    if res2['r'] == 2:
        print("✅ Correctly identified (a,an,n) case.")
    else:
        print("❌ Failed Case 2")

if __name__ == "__main__":
    test_gp_distinction()
