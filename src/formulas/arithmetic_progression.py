
class ArithmeticProgression:
    @staticmethod
    def solve(a: float = None, d: float = None, n: float = None, an: float = None, s: float = None) -> dict:
        # Check consistency if all provided???
        # We will attempt to calculate missing values.
        
        # 3 variables needed to define AP usually (a, d, n) -> an, s.
        # Or (a, an, n) -> d, s.
        # Logic from JS implementation:
        
        # Loop to resolve dependencies?
        # a, d, n => an = a + (n-1)d
        # a, d, n => s = n/2 * (2a + (n-1)d)
        # s, n => a + an = 2s/n.
        
        # We can use a simple iterative approach or just if-branches.
        # JS implementation was cleaner.
        
        # Calculate N
        if n is None:
            if a is not None and d is not None and an is not None and d != 0:
                n = (an - a) / d + 1
            elif a is not None and an is not None and s is not None and (a + an) != 0:
                n = 2 * s / (a + an)
            elif d is not None and a is not None and s is not None:
                # s = n/2 * (2a + (n-1)d) -> quadratic for n?
                # 2s = n(2a - d + dn) = n(2a-d) + d*n^2
                # d*n^2 + (2a-d)*n - 2s = 0
                if d != 0:
                    delta = (2 * a - d) ** 2 - 4 * d * (-2 * s)
                    if delta >= 0:
                        n1 = (-(2 * a - d) + delta ** 0.5) / (2 * d)
                        n2 = (-(2 * a - d) - delta ** 0.5) / (2 * d)
                        if n1 > 0 and abs(n1 - round(n1)) < 1e-9:
                             n = n1
                        elif n2 > 0 and abs(n2 - round(n2)) < 1e-9:
                             n = n2

        # Calculate A
        if a is None:
            if an is not None and n is not None and d is not None:
                a = an - (n - 1) * d
            elif s is not None and n is not None and an is not None:
                a = 2 * s / n - an
            elif s is not None and n is not None and d is not None:
                # s = n/2 * (2a + (n-1)d)
                # 2s/n = 2a + (n-1)d
                a = (2 * s / n - (n - 1) * d) / 2

        # Calculate D
        if d is None:
            if an is not None and a is not None and n is not None and n != 1:
                d = (an - a) / (n - 1)
            elif s is not None and n is not None and a is not None:
                # s = n/2 * (2a + (n-1)d)
                # 2s/n - 2a = (n-1)d
                if n != 1:
                    d = (2 * s / n - 2 * a) / (n - 1)
            elif a is None and an is not None and n is not None and s is not None:
                # s = n/2 * (a + an) => a = 2s/n - an
                pass # Handled by finding a first?
        
        # Calculate AN
        if an is None:
            if a is not None and n is not None and d is not None:
                an = a + (n - 1) * d
        
        # Calculate S
        if s is None:
            if n is not None and a is not None and an is not None:
                s = n * (a + an) / 2
            elif n is not None and a is not None and d is not None:
                s = n * (2 * a + (n - 1) * d) / 2

        return {
            "a": a,
            "d": d,
            "n": n,
            "an": an,
            "sum": s
        }

    @staticmethod
    def get_a(an: float, n: float, d: float) -> float:
        return an - (n - 1) * d

    @staticmethod
    def get_d(a: float, an: float, n: float) -> float:
        if n == 1:
            return 0
        return (an - a) / (n - 1)

    @staticmethod
    def get_n(a: float, an: float, d: float) -> float:
        if d == 0:
            return 0 # Or Exception?
        return (an - a) / d + 1

    @staticmethod
    def get_an(a: float, n: float, d: float) -> float:
        return a + (n - 1) * d

    @staticmethod
    def get_sum(a: float, n: float, d: float) -> float:
        return n * (2 * a + (n - 1) * d) / 2

    @staticmethod
    def get_sum_term(a: float, an: float, n: float) -> float:
        return n * (a + an) / 2
