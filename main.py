from src.data_loader import load_data

"""
Deliver 40 packages using 3 trucks under 140 miles total.

Meet package-specific constraints (deadlines, delivery address corrections).

Output delivery progress for packages (time delivered, status, etc.).

Write clean, modular, and maintainable code.
"""

packages = load_data()
packages.print()