import math

class GeometricProgression:
    """
    Smart Solver for Geometric Progression.
    Identifies the given variables and calculates the missing ones.
    
    Logic based on existing formulas:
    an = a * r^n
    s = a * (1 - r^n) / (1 - r)
    infinity_sum = a / (1 - r)  (if -1 < r < 1)
    n = log(an / a) / log(r)
    """
    @staticmethod
    def solve(a=None, r=None, n=None, an=None, s=None, infinity_sum=None):
        """
        Solves for missing Geometric Progression variables.
        
        Args:
            a (float, optional): First term
            r (float, optional): Common ratio
            n (float, optional): Number of terms (0-indexed logic)
            an (float, optional): Term at index n
            s (float, optional): Sum of first n terms
            infinity_sum (float, optional): Sum to infinity
            
        Returns:
            dict: Dictionary with keys 'a', 'r', 'n', 'an', 's', 'infinity_sum'
        """
        # Iteratively solve until no more changes or all found.
        changed = True
        loop_count = 0
        
        # Helper to check if defined
        def is_def(v):
            return v is not None

        while changed and loop_count < 5:
            changed = False
            
            # 1. Calculate an if a, r, n exist
            if not is_def(an) and is_def(a) and is_def(r) and is_def(n):
                an = a * (r ** n)
                changed = True

            # 2. Calculate s if a, r, n exist
            if not is_def(s) and is_def(a) and is_def(r) and is_def(n):
                if r == 1:
                    s = a * n
                else:
                    try:
                        s = a * (1 - r ** n) / (1 - r)
                        changed = True
                    except ZeroDivisionError:
                        pass

            # 2b. Calculate infinity_sum if a, r exist and |r| < 1
            if not is_def(infinity_sum) and is_def(a) and is_def(r):
                if abs(r) < 1:
                    infinity_sum = a / (1 - r)
                    changed = True

            # 3. Calculate n if a, an, r exist
            if not is_def(n) and is_def(a) and is_def(an) and is_def(r):
                if a != 0:
                    try:
                        n = math.log(an / a) / math.log(r)
                        changed = True
                    except (ValueError, ZeroDivisionError):
                        pass
            
            # 4. Calculate a if an, r, n exist
            if not is_def(a) and is_def(an) and is_def(r) and is_def(n):
                if r != 0:
                    a = an / (r ** n)
                    changed = True
                elif an == 0:
                    # if r=0 and an=0, a can be anything usually, or a=0. 
                    pass

            # 4b. Calculate a if infinity_sum, r exist
            if not is_def(a) and is_def(infinity_sum) and is_def(r):
                a = infinity_sum * (1 - r)
                changed = True
            
            # 5. Calculate r if a, an, n exist
            if not is_def(r) and is_def(a) and is_def(an) and is_def(n):
                if a != 0 and n != 0:
                    try:
                        # Only real root support for simplicity as per JS
                        val = an / a
                        if val < 0 and n % 2 == 0:
                            pass # No real root
                        else:
                            # Python pow handles negative bases with fractional exponents differently
                            # Use abs and sign for simple logic if needed or just complex.
                            # For consistency with JS (which returns NaN for negative base fractional power usually),
                            # let's try direct pow.
                            r = (an / a) ** (1 / n)
                            # If result is complex, we might want to skip or handle.
                            if isinstance(r, complex):
                                # If imaginary part is tiny, take real
                                if abs(r.imag) < 1e-9:
                                    r = r.real
                                    changed = True
                            else:
                                changed = True
                    except:
                        pass
                        
            # 5b. Calculate r if a, infinity_sum exist
            if not is_def(r) and is_def(a) and is_def(infinity_sum):
                 if infinity_sum != 0:
                     r = 1 - (a / infinity_sum)
                     changed = True

            # 6. S related inversions
            # If a, r, s known => find n
            if not is_def(n) and is_def(a) and is_def(r) and is_def(s):
                if r != 1 and a != 0:
                    term = 1 - (s * (1 - r) / a)
                    if term > 0:
                        try:
                            n = math.log(term) / math.log(r)
                            changed = True
                        except:
                            pass

            # If r, n, s known => find a
            if not is_def(a) and is_def(r) and is_def(n) and is_def(s):
                 if r == 1:
                     if n != 0:
                         a = s / n
                         changed = True
                 else:
                     denom = 1 - r ** n
                     if denom != 0:
                         a = s * (1 - r) / denom
                         changed = True
            
            loop_count += 1

        return {
            'a': a,
            'r': r,
            'n': n,
            'an': an,
            's': s,
            'infinity_sum': infinity_sum
        }
