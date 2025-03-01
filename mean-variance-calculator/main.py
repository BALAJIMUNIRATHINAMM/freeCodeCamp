from mean_var_std import calculate

if __name__ == "__main__":
    test_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    try:
        result = calculate(test_input)
        print("Calculation Result:")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
