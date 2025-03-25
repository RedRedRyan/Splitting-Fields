import sympy as sp
from sympy import S, symbols, sympify, solveset, factor

def factor_polynomial(polynomial_str):
    try:
        # Define the variable
        x = symbols('x')
        
        # Parse the polynomial from the string input
        polynomial = sympify(polynomial_str)
        
        # Check if input is a valid polynomial in x
        if not polynomial.has(x):
            print("Error: Input must be a polynomial in 'x'.")
            return
        
        # Find the roots over the real numbers
        roots = solveset(polynomial, x, domain=S.Reals)
        
        # Display roots (formatted)
        print("\nRoots of the polynomial:")
        if roots:
            for i, root in enumerate(roots, 1):
                print(f"Root {i}: {root.evalf(3)}")  # Display roots with 3 decimal places
        else:
            print("No real roots found.")
        
        # Factorize the polynomial
        factorization = factor(polynomial)
        
        print("\nFactorization:")
        print(factorization)
    
    except (sp.SympifyError, ValueError) as e:
        print(f"Error: Invalid input. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Polynomial Factorization Tool")
    print("----------------------------")
    print("Enter a polynomial in terms of 'x' (e.g., 'x**3 - 2*x + 1'):")
    
    while True:
        polynomial_str = input("> ").strip()
        if polynomial_str.lower() in ('exit', 'quit'):
            break
        
        factor_polynomial(polynomial_str)
        print("\nEnter another polynomial or type 'exit' to quit.")

if __name__ == "__main__":
    main()
