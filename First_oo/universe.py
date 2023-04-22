from first_oo.some_module import point, circle, triangle, retangle
    
def workspace():
    
    pointp = point(30, -17)
    print(f'\n{pointp.PrintCoord()}')   
    
    circlep = circle(10, 40, 20)
    print(f'\n{circlep.show()}') 
    circlep.perimeter()
    circlep.area()
    
    trianglep = triangle(4, 6, 8, 10, 2, 4)
    print(f'\n{trianglep.show()}')
    trianglep.perimeter()
    
    retanglep = retangle(6, 8, -6, -8)
    print(f'\n{circlep.show()}')
    retanglep.perimeter()
    
    print("\nSucessfull exit!")
    
