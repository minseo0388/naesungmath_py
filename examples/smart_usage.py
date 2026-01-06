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
    
    # After (Keyword Arguments MANDATORY due to *)
    vol_new = Solid3D.square_pyramid_volume(base_side=5, height=10)
    print(f"Volume: {vol_new}")

    # 2. Smart Logic
    db_record = {'a': 5, 'b': 12}
    
    # Dictionary unpacking works great with keyword-only args if keys match!
    # vol_slant = Solid3D.square_pyramid_volume(**db_record) 
    # But for manual call:
    vol_slant = Solid3D.square_pyramid_volume(base_side=5, slant_edge=12)
    print(f"Volume from Slant: {vol_slant}")

    # 3. Nesting
    complex_vol = Solid3D.square_pyramid_volume(
        base_side=6,
        height=Triangle.pythagoras(a=3, b=4) # Named args
    )
    print(f"Complex Volume (h=5): {complex_vol}")

    # 4. Data Science Integration
    total_area = BasicMath.add(
        Circle.area(radius=5),
        Quadrilateral.square_area(side=5)
    )
    print(f"Total Area: {total_area}")

if __name__ == "__main__":
    run()
