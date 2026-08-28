import math


def get_coeff(name: str) -> float:
    raw = input(f"  {name}: ").strip()
    return float(raw) if raw else 0.0


def build_equation(a: float, b: float, c: float) -> str:
    parts = []

    if a != 0:
        if a == 1:
            parts.append("x²")
        elif a == -1:
            parts.append("-x²")
        else:
            parts.append(f"{a:g}x²")

    if b != 0:
        if parts:
            if b == 1:
                parts.append("+ x")
            elif b == -1:
                parts.append("- x")
            elif b > 0:
                parts.append(f"+ {b:g}x")
            else:
                parts.append(f"- {abs(b):g}x")
        else:
            if b == 1:
                parts.append("x")
            elif b == -1:
                parts.append("-x")
            else:
                parts.append(f"{b:g}x")

    if c != 0:
        if parts:
            if c > 0:
                parts.append(f"+ {c:g}")
            else:
                parts.append(f"- {abs(c):g}")
        else:
            parts.append(f"{c:g}")

    return (" ".join(parts) if parts else "0") + " = 0"


def main():
    print("Quadratic equation: ax² + bx + c = 0  (Enter = 0)\n")
    a = get_coeff("a")
    b = get_coeff("b")
    c = get_coeff("c")

    print(f"\n  {build_equation(a, b, c)}\n")

    if a == 0:
        if b == 0:
            print("No resolution." if c != 0 else "Infinite solutions (0 = 0).")
        else:
            print(f"Linear solution: x = {-c / b:g}")
        return

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Two solutions:\n  x₁ = {x1:g}\n  x₂ = {x2:g}")
    elif discriminant == 0:
        print(f"One solution: x = {-b / (2 * a):g}")
    else:
        print("No resolution (discriminant < 0).")


if __name__ == "__main__":
    main()
