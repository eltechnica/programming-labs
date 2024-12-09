import math

def color_distance():
    print("First color")
    r1 = int(input("R: "))
    g1 = int(input("G: "))
    b1 = int(input("B: "))
    
    print("\nSecond color")
    r2 = int(input("R: "))
    g2 = int(input("G: "))
    b2 = int(input("B: "))
    
    distance = math.sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)
    
    print("\Color Distance: {:.4f}".format(distance))
    
color_distance()
