promotions: list[tuple[str, str]] = [
    ("Monday", "Tomato"),
    ("Tuesday", "Taco"),
    ("Friday", "Mac Cheese")
]

for p in promotions:
    print(p[0], p[1])