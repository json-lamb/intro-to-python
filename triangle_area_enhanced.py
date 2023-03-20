import math
import matplotlib.pyplot as plt
import numpy as np

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def plot_triangle(a, b, c):
    A = (0, 0)
    B = (c, 0)
    C = (a**2 - (b - c)**2) / (2 * a), math.sqrt(abs(a**2 - ((a**2 - (b - c)**2) / (2 * a))**2))
    coords = np.array([A, B, C, A])
    plt.plot(coords[:, 0], coords[:, 1], 'o-')
    
    # Annotate side lengths
    plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2, f'{c}', ha='center', va='center')
    plt.text((A[0] + C[0]) / 2, (A[1] + C[1]) / 2, f'{b}', ha='center', va='center')
    plt.text((B[0] + C[0]) / 2, (B[1] + C[1]) / 2, f'{a}', ha='center', va='center')
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))
    c = float(input("Enter the length of side C: "))

    if is_valid_triangle(a, b, c):
        area = herons_formula(a, b, c)
        print("The area of the triangle is:", area)
        plot_triangle(a, b, c)
    else:
        print("The sides do not form a valid triangle.")
