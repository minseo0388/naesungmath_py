import sys
import math
from formulas.basic_math import BasicMath
from formulas.equation import Equation
from formulas.calculus import Calculus
from formulas.linear_algebra import LinearAlgebra
from formulas.triangle import Triangle
from formulas.quadrilateral import Quadrilateral
from formulas.polygon import Polygon
from formulas.solid_3d import Solid3D
from formulas.circle import Circle
from formulas.analytic_geometry import AnalyticGeometry
from formulas.trigonometry import Trigonometry

def assert_almost_equal(actual, expected, test_name, tolerance=0.001):
    if abs(actual - expected) > tolerance:
        print(f"[FAIL] {test_name}. Expected ~{expected}, Got {actual}")
        sys.exit(1)
    print(f"[PASS] {test_name}")

def main():
    print("Verifying Python Refactored Formulas (Zero-Omission)...")
    
    try:
        # 1. BasicMath
        assert_almost_equal(BasicMath.add(2, 3), 5, "BasicMath.add")
        assert_almost_equal(BasicMath.subtract(5, 3), 2, "BasicMath.subtract")
        assert_almost_equal(BasicMath.multiply(2, 3), 6, "BasicMath.multiply")
        assert_almost_equal(BasicMath.divide(6, 3), 2, "BasicMath.divide")
        assert_almost_equal(BasicMath.pow(2, 3), 8, "BasicMath.pow")
        assert_almost_equal(BasicMath.sqrt(4), 2, "BasicMath.sqrt")
        assert_almost_equal(BasicMath.round(2.6), 3, "BasicMath.round")
        assert_almost_equal(BasicMath.factorial(5), 120, "BasicMath.factorial")
        assert_almost_equal(BasicMath.gcd(12, 18), 6, "BasicMath.gcd")

        # 2. Equation
        roots = Equation.quadratic_roots(1, -3, 2)
        assert_almost_equal(roots[0], 2, "Equation.quadratic_roots x1")
        assert_almost_equal(roots[1], 1, "Equation.quadratic_roots x2")

        # 3. Calculus
        assert_almost_equal(Calculus.sigma(1, 5, lambda x: x), 15, "Calculus.sigma")
        assert_almost_equal(Calculus.diff(lambda x: x*x, 2), 4, "Calculus.diff", 0.01)
        assert_almost_equal(Calculus.integral(lambda x: x*x, 0, 1), 0.333, "Calculus.integral", 0.01)

        # 4. LinearAlgebra
        matA = [[1, 2], [3, 4]]
        matB = [[5, 6], [7, 8]]
        matAdd = LinearAlgebra.add(matA, matB)
        assert_almost_equal(matAdd[0][0], 6, "LinearAlgebra.add[0][0]")
        assert_almost_equal(LinearAlgebra.determinant(matA), -2, "LinearAlgebra.determinant")
        assert_almost_equal(LinearAlgebra.trace(matA), 5, "LinearAlgebra.trace")
        vec = [3, 4]
        assert_almost_equal(LinearAlgebra.sqrt_dot_product(vec, vec), 5, "LinearAlgebra.sqrt_dot_product")

        # 5. Triangle
        assert_almost_equal(Triangle.area(base_side=10, height=5), 25, "Triangle.area")
        assert_almost_equal(Triangle.pythagoras(3, 4), 5, "Triangle.pythagoras")

        # 6. Quadrilateral
        assert_almost_equal(Quadrilateral.square_area(5), 25, "Quadrilateral.square_area")
        assert_almost_equal(Quadrilateral.rectangle_area(5, 10), 50, "Quadrilateral.rectangle_area")
        assert_almost_equal(Quadrilateral.trapezoid_area(2, 4, 5), 15, "Quadrilateral.trapezoid_area")

        # 7. Polygon
        assert_almost_equal(Polygon.pentagon_area(5), 43.0119, "Polygon.pentagon_area")
        assert_almost_equal(Polygon.diagonal_count(5), 5, "Polygon.diagonal_count")

        # 8. Solid3D
        assert_almost_equal(Solid3D.cube_area(5), 150, "Solid3D.cube_area")
        assert_almost_equal(Solid3D.square_pyramid_volume(base_side=5, slant_edge=10), 77.9512, "Solid3D.square_pyramid_volume")

        # 9. Circle
        assert_almost_equal(Circle.area(10), 314.159, "Circle.area")
        assert_almost_equal(Circle.sector_angle(10, 5), 28.6479, "Circle.sector_angle")

        # 10. AnalyticGeometry
        cg = AnalyticGeometry.center_gravity(0, 0, 4, 0, 2, 3) 
        assert_almost_equal(cg[0], 2, "AnalyticGeometry.center_gravity X")
        assert_almost_equal(cg[1], 1, "AnalyticGeometry.center_gravity Y")
        assert_almost_equal(AnalyticGeometry.eccentricity(5, 3), 0.8, "AnalyticGeometry.eccentricity")

        # 11. Trigonometry
        assert_almost_equal(Trigonometry.degree_to_rad(180), math.pi, "Trigonometry.degree_to_rad")

        print("All Python Tests Passed!")

    except Exception as e:
        print(f"Test Failed with Exception: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
