import numpy as np

def parse_shape(s):
    try:
        parts = s.lower().replace(' ', '').split('x')
        return int(parts[0]), int(parts[1])
    except:
        raise ValueError("Invalid format. Use format like 2x3")

def get_matrix(shape):
    rows, cols = shape
    print(f"Enter values for a {rows}x{cols} matrix (row-wise, space-separated):")
    data = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").strip().split()))
                if len(row) != cols:
                    raise ValueError
                data.append(row)
                break
            except ValueError:
                print(f"Invalid input. Expected {cols} values.")
    return np.array(data)

def main():
    shape1 = parse_shape(input("Enter size of first matrix (e.g. 2x3): "))
    mat1 = get_matrix(shape1)

    shape2 = parse_shape(input("Enter size of second matrix (e.g. 3x2): "))
    mat2 = get_matrix(shape2)

    # Determine valid operations
    options = {}
    option_id = 1

    if mat1.shape == mat2.shape:
        options[str(option_id)] = ('add', lambda a, b: a + b)
        option_id += 1
        options[str(option_id)] = ('subtract', lambda a, b: a - b)
        option_id += 1

    if mat1.shape[1] == mat2.shape[0]:
        options[str(option_id)] = ('multiply', lambda a, b: a @ b)

    if not options:
        print("No valid operations can be performed on the given matrices.")
        return

    # Show valid options
    print("Choose operation:")
    for key, (name, _) in options.items():
        print(f"{name} ({key})")

    choice = input("Enter choice number: ").strip()

    if choice in options:
        operation_name, operation_func = options[choice]
        result = operation_func(mat1, mat2)
        print("Result:")
        for row in result:
            print(' '.join(map(str, row)))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
