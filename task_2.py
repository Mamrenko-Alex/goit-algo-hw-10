import random

# 1. Визначення параметрів
a = 10
b = 5

# 2. Генерація випадкових вхідних даних
def is_inside_triangle(x, y):
    """
    Перевіряє, чи точка (x, y) знаходиться всередині прямокутного трикутника,
    утвореного гіпотенузою (0,0) -> (a,b) та сторонами прямокутника.
    """
    return y <= (b / a) * x

# 3. Виконання обчислень
def monte_carlo_triangle_area(a, b, num_points):
    """
    Оцінка площі трикутника методом Монте-Карло.
    """
    points_inside = 0

    for _ in range(num_points):
        x = random.uniform(0, a)
        y = random.uniform(0, b)
        if is_inside_triangle(x, y):
            points_inside += 1

    # 4. Агрегування та аналіз результатів
    rectangle_area = a * b
    triangle_area_estimate = (points_inside / num_points) * rectangle_area
    return triangle_area_estimate

# 5. Визначення кількості точок для оцінки
N = 10000

# Результат
approx_area = monte_carlo_triangle_area(a, b, N)
print(f"Оцінка площі трикутника методом Монте-Карло з {N} точок: {approx_area:.4f}")

# Порівняння з точною площею
exact_area = 0.5 * a * b
print(f"Точна площа трикутника: {exact_area}")
print(f"Відносна похибка: {abs(approx_area - exact_area) / exact_area:.2%}")
