from formulas.solid_3d import Solid3D
from formulas.triangle import Triangle
from formulas.basic_math import BasicMath
from formulas.circle import Circle
from formulas.quadrilateral import Quadrilateral

def run():
    print("--- Python Smart Solver Examples ---")

    # 1. Before vs After
    base_side = 5
    height = 10
    
    # Before (Risky Manual Formula)
    vol_old = (1/3) * (base_side ** 2) * height
    
    # After (Safe Function)
    vol_new = Solid3D.square_pyramid_volume(base_side=5, height=10)
    print(f"Volume: Old={vol_old}, New={vol_new}")

    # 2. Smart Logic (Auto-detection)
    # Scenario: Database record has 'slant_edge' but 'height' is null.
    db_record = {'a': 5, 'b': 12, 'h': None}
    
    # Just pass what you have
    vol_slant = Solid3D.square_pyramid_volume(
        base_side=db_record['a'], 
        slant_edge=db_record['b'] # Smart Solver calculates height internally
    )
    print(f"Volume from Slant: {vol_slant}")

    # 3. Nesting (Pipeline)
    # Scenario: Volume of a pyramid where height is the hypotenuse of a right triangle (3, 4)
    complex_vol = Solid3D.square_pyramid_volume(
        base_side=6,
        height=Triangle.pythagoras(3, 4) # Returns 5, used as height
    )
    print(f"Complex Volume (h=5): {complex_vol}")

    # 4. Data Science Integration
    # Summing generic areas without caring about formula details
    total_area = BasicMath.add(
        Circle.area(radius=5),
        Quadrilateral.square_area(side=5)
    )
    print(f"Total Area: {total_area}")

if __name__ == "__main__":
    run()
