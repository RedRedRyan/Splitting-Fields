import sympy as sp
from sympy import S, QQ

def factor_polynomial(polynomial_str):
    # Define the variable
    x = sp.symbols('x')
    
    # Parse the polynomial from the string input
    polynomial = sp.sympify(polynomial_str)
    
    # Find the roots of the polynomial using sympy's solveset function over the rational numbers (QQ)
    roots = sp.solveset(polynomial, x, domain=sp.S.Reals)
    
    # Output the roots
    print("The roots of the polynomial are:")
    for root in roots:
        print(root)
    
    # Factorize the polynomial
    factorization = sp.factor(polynomial)
    
    print("\nThe factorization of the polynomial is:")
    print(factorization)
def main():
    # user input
    print("Enter the polynomial (e.g., 'x**3 - 2'):")
    polynomial_str = input()
    
    factor_polynomial(polynomial_str)

if __name__ == "__main__":
    main()
