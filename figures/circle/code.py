default_radius = 5
__all__ = ["circle_perimeter", "circle_area"]

def circle_perimeter(radius: int = default_radius):  # Длина окружности
    return 2 * 3.14 * radius


def circle_area(radius: int = default_radius):  # Лощадь окружности
    return 3.14*(radius**2)
