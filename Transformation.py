import math
import sys
import matplotlib.pyplot as plt


def rotate_points(points, degrees, direction):
    """Rotate points about the origin by the given degrees.
    direction: "CW" or "CCW" (case-insensitive).
    """
    theta = math.radians(float(degrees))
    if direction.lower() == "cw":
        theta = -theta  # CW is negative angle in standard math coords
    elif direction.lower() == "ccw":
        pass
    else:
        raise ValueError("direction must be 'CW' or 'CCW'")

    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    rotated = []
    for (x, y) in points:
        xr = x * cos_t - y * sin_t
        yr = x * sin_t + y * cos_t
        rotated.append((xr, yr))
    return rotated


def choose_transformation():
    print("Choose a transformation:")
    print("1) Translation")
    print("2) Rotation")
    print("3) Reflection")
    print("4) Enlargement")
    choice = input("Enter 1, 2, 3, or 4: ").strip()
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Defaulting to Rotation.")
        return "2"
    return choice


def choose_shape():
    print("Choose a shape:")
    print("1) Shape 1 (a–h, 8 points)")
    print("2) Shape 2 (a–f, 6 points)")
    sel = input("Enter 1 or 2: ").strip()
    if sel == "1":
        labels = ["a", "b", "c", "d", "e", "f", "g", "h"]
        points = [
            (6, 10),
            (6, 8),
            (8, 8),
            (8, 2),
            (10, 2),
            (10, 8),
            (12, 8),
            (12, 10),
        ]
        return points, labels, "Shape 1"
    else:
        # Default to Shape 2
        labels = ["a", "b", "c", "d", "e", "f"]
        points = [
            (4, 2),
            (6, 2),
            (6, 6),
            (2, 6),
            (2, 4),
            (4, 4),
        ]
        return points, labels, "Shape 2"


def run_translation(shape_name):
    # Shapes for translation as specified by the user
    if shape_name == "Shape 1":
        labels = ["a", "b", "c", "d", "e", "f", "g", "h"]
        points = [
            (1, -1),
            (1, -3),
            (3, -3),
            (3, -9),
            (5, -9),
            (5, -3),
            (7, -3),
            (7, -1),
        ]
    else:
        labels = ["a", "b", "c", "d", "e", "f"]
        points = [
            (3, -5),
            (5, -5),
            (5, -1),
            (1, -1),
            (1, -3),
            (3, -3),
        ]

    # Translation vector (-2, 3)
    dx, dy = -2, 3
    translated_points = [(x + dx, y + dy) for (x, y) in points]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    txs = [p[0] for p in translated_points]
    tys = [p[1] for p in translated_points]

    all_x = xs + txs
    all_y = ys + tys

    plt.figure(figsize=(10, 10), dpi=120)

    # Original shape (closed)
    plt.plot(xs, ys, "-o", color="#1f77b4", linewidth=2, markersize=6, label=f"original ({shape_name})")
    plt.plot([xs[-1], xs[0]], [ys[-1], ys[0]], "-", color="#1f77b4", linewidth=2)

    # Translated shape (closed)
    plt.plot(txs, tys, "-o", color="#9467bd", linewidth=2, markersize=6, label=f"translated by (-2, 3)")
    plt.plot([txs[-1], txs[0]], [tys[-1], tys[0]], "-", color="#9467bd", linewidth=2)

    # Labels
    for (x, y), label in zip(points, labels):
        plt.annotate(f"{label} ({x}, {y})", (x, y), textcoords="offset points", xytext=(6, 6), ha="left", fontsize=10, color="#1f77b4")
    for (x, y), label in zip(translated_points, labels):
        plt.annotate(f"{label} ({x}, {y})", (x, y), textcoords="offset points", xytext=(6, 6), ha="left", fontsize=10, color="#9467bd")

    plt.title("Original and Translated Shape by (-2, 3)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":", alpha=0.6)
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")

    # Limits with padding
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    x_range = max(1.0, x_max - x_min)
    y_range = max(1.0, y_max - y_min)
    pad_x = 0.08 * x_range
    pad_y = 0.08 * y_range
    plt.xlim(x_min - pad_x, x_max + pad_x)
    plt.ylim(y_min - pad_y, y_max + pad_y)

    plt.legend(loc="best")

    # Console tables
    print("\nOriginal points:")
    for lbl, (x, y) in zip(labels, points):
        print(f"{lbl} {x},{y}")
    print("\nTranslated points (by -2, 3):")
    for lbl, (x, y) in zip(labels, translated_points):
        print(f"{lbl} {x},{y}")

    plt.tight_layout()
    plt.show()


def run_rotation(points, labels):
    try:
        deg_str = input("Enter rotation degrees (e.g., 90): ").strip()
        direction = input("Direction (CW or CCW): ").strip()
        degrees = float(deg_str)
    except Exception:
        print("Invalid input. Using default: 90 degrees CW.")
        degrees = 90.0
        direction = "CW"

    rotated_points = rotate_points(points, degrees, direction)
    rot_labels = [f"{lbl}′" for lbl in labels]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    rxs = [p[0] for p in rotated_points]
    rys = [p[1] for p in rotated_points]

    # Aggregate for limits (include both shapes)
    all_x = xs + rxs
    all_y = ys + rys

    # Single figure for both shapes
    plt.figure(figsize=(10, 10), dpi=120)

    # Original shape (closed)
    plt.plot(xs, ys, "-o", color="#1f77b4", linewidth=2, markersize=6, label="original")
    plt.plot([xs[-1], xs[0]], [ys[-1], ys[0]], "-", color="#1f77b4", linewidth=2)

    # Rotated shape (closed)
    plt.plot(rxs, rys, "-o", color="#ff7f0e", linewidth=2, markersize=6, label=f"rotated {degrees:g}° {direction.upper()}")
    plt.plot([rxs[-1], rxs[0]], [rys[-1], rys[0]], "-", color="#ff7f0e", linewidth=2)

    # Label each original point with letter and coordinates
    for (x, y), label in zip(points, labels):
        text = f"{label} ({x}, {y})"
        plt.annotate(
            text,
            (x, y),
            textcoords="offset points",
            xytext=(6, 6),
            ha="left",
            fontsize=10,
            color="#1f77b4",
        )

    # Label each rotated point with letter′ and coordinates
    for (x, y), label in zip(rotated_points, rot_labels):
        text = f"{label} ({x:.2f}, {y:.2f})"
        plt.annotate(
            text,
            (x, y),
            textcoords="offset points",
            xytext=(6, 6),
            ha="left",
            fontsize=10,
            color="#ff7f0e",
        )

    # Styling
    plt.title(f"Original and Rotated Shape ({degrees:g}° {direction.upper()})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":", alpha=0.6)
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")

    # Dynamic limits with proportional padding to show the full graph
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    x_range = max(1.0, x_max - x_min)
    y_range = max(1.0, y_max - y_min)
    pad_x = 0.08 * x_range
    pad_y = 0.08 * y_range
    plt.xlim(x_min - pad_x, x_max + pad_x)
    plt.ylim(y_min - pad_y, y_max + pad_y)

    plt.legend(loc="best")

    # ---- Console tables ----
    print("\nOriginal points:")
    for lbl, (x, y) in zip(labels, points):
        print(f"{lbl} {x},{y}")

    print(f"\nRotated points ({degrees:g}° {direction.upper()}):")
    for lbl, (x, y) in zip(rot_labels, rotated_points):
        print(f"{lbl} {x:.2f},{y:.2f}")

    plt.tight_layout()
    plt.show()


def run_reflection(points, labels):
    # Reflect across the x-axis: (x, y) -> (x, -y)
    reflected_points = [(x, -y) for (x, y) in points]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    rxs = [p[0] for p in reflected_points]
    rys = [p[1] for p in reflected_points]

    all_x = xs + rxs
    all_y = ys + rys

    plt.figure(figsize=(10, 10), dpi=120)

    # Original shape (closed)
    plt.plot(xs, ys, "-o", color="#1f77b4", linewidth=2, markersize=6, label="original")
    plt.plot([xs[-1], xs[0]], [ys[-1], ys[0]], "-", color="#1f77b4", linewidth=2)

    # Reflected shape (closed)
    plt.plot(rxs, rys, "-o", color="#2ca02c", linewidth=2, markersize=6, label="reflected over x-axis")
    plt.plot([rxs[-1], rxs[0]], [rys[-1], rys[0]], "-", color="#2ca02c", linewidth=2)

    # Labels
    for (x, y), label in zip(points, labels):
        plt.annotate(f"{label} ({x}, {y})", (x, y), textcoords="offset points", xytext=(6, 6), ha="left", fontsize=10, color="#1f77b4")
    for (x, y), label in zip(reflected_points, labels):
        plt.annotate(f"{label} ({x}, {y})", (x, y), textcoords="offset points", xytext=(6, 6), ha="left", fontsize=10, color="#2ca02c")

    plt.title("Original and Reflected Shape over x-axis (y -> -y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":", alpha=0.6)
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")

    # Limits
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    x_range = max(1.0, x_max - x_min)
    y_range = max(1.0, y_max - y_min)
    pad_x = 0.08 * x_range
    pad_y = 0.08 * y_range
    plt.xlim(x_min - pad_x, x_max + pad_x)
    plt.ylim(y_min - pad_y, y_max + pad_y)

    plt.legend(loc="best")

    # Console tables
    print("\nOriginal points:")
    for lbl, (x, y) in zip(labels, points):
        print(f"{lbl} {x},{y}")
    print("\nReflected points (y -> -y):")
    for lbl, (x, y) in zip(labels, reflected_points):
        print(f"{lbl} {x},{y}")

    plt.tight_layout()
    plt.show()


def run_enlargement(shape_name):
    # Scale factor and center as specified
    k = 2.0
    cx, cy = 1.0, 0.0

    # Use provided Shape 2 points A–F; Shape 1 uses current 8-point set unless overridden later
    if shape_name == "Shape 2":
        labels = ["A", "B", "C", "D", "E", "F"]
        points = [
            (3, 2),
            (5, 2),
            (5, 6),
            (1, 6),
            (1, 4),
            (3, 4),
        ]
    else:
        labels = ["A", "B", "C", "D", "E", "F", "G", "H"]
        points = [
            (2, 10),
            (2, 8),
            (4, 8),
            (4, 2),
            (6, 2),
            (6, 8),
            (8, 8),
            (8, 10),
        ]

    # Apply enlargement about (cx, cy)
    enlarged_points = [(cx + k * (x - cx), cy + k * (y - cy)) for (x, y) in points]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    exs = [p[0] for p in enlarged_points]
    eys = [p[1] for p in enlarged_points]

    all_x = xs + exs
    all_y = ys + eys

    plt.figure(figsize=(10, 10), dpi=120)

    # Original shape (closed)
    plt.plot(xs, ys, "-o", color="#1f77b4", linewidth=2, markersize=6, label=f"original ({shape_name})")
    plt.plot([xs[-1], xs[0]], [ys[-1], ys[0]], "-", color="#1f77b4", linewidth=2)

    # Enlarged shape (closed)
    plt.plot(exs, eys, "-o", color="#17becf", linewidth=2, markersize=6, label=f"enlarged k={k:g} about ({cx:g},{cy:g})")
    plt.plot([exs[-1], exs[0]], [eys[-1], eys[0]], "-", color="#17becf", linewidth=2)

    # Labels
    for (x, y), label in zip(points, labels):
        plt.annotate(f"{label} ({x}, {y})", (x, y), textcoords="offset points", xytext=(6, 6), ha="left", fontsize=10, color="#1f77b4")
    for (x, y), label in zip(enlarged_points, labels):
        plt.annotate(f"{label} ({x:.2f}, {y:.2f})", (x, y), textcoords="offset points", xytext=(6, 6), ha="left", fontsize=10, color="#17becf")

    # Mark center
    plt.scatter([cx], [cy], color="#2ca02c", s=80, zorder=5, label="center")

    plt.title(f"Original and Enlarged Shape (k={k:g}, center=({cx:g},{cy:g}))")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle=":", alpha=0.6)
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")

    # Limits with padding
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    x_range = max(1.0, x_max - x_min)
    y_range = max(1.0, y_max - y_min)
    pad_x = 0.08 * x_range
    pad_y = 0.08 * y_range
    plt.xlim(x_min - pad_x, x_max + pad_x)
    plt.ylim(y_min - pad_y, y_max + pad_y)

    plt.legend(loc="best")

    # Console tables
    print("\nOriginal points:")
    for lbl, (x, y) in zip(labels, points):
        print(f"{lbl} {x},{y}")
    print(f"\nEnlarged points (k={k:g}, center=({cx:g},{cy:g})):")
    for lbl, (x, y) in zip(labels, enlarged_points):
        print(f"{lbl} {x:.2f},{y:.2f}")

    plt.tight_layout()
    plt.show()


def plot_labeled_points():
    # After choosing transformation, ask which shape to use.
    choice = choose_transformation()

    points, labels, shape_name = choose_shape()

    if choice == "1":
        run_translation(shape_name)
    elif choice == "2":
        run_rotation(points, labels)
    elif choice == "3":
        run_reflection(points, labels)
    elif choice == "4":
        run_enlargement(shape_name)


if __name__ == "__main__":
    plot_labeled_points()
