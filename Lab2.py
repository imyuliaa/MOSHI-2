import random
import matplotlib.pyplot as plt
import numpy as np

# Тестова функція (x^2)
def test_function(x):
    return x ** 2

# Основна функція (e^x^2)
def main_function(x):
    return np.exp(x ** 2)

# Генерація випадкової точки на площині
def generate_random_point(a, b, f):
    x = random.uniform(a, b)
    y = random.uniform(0, max(f(np.array([a, b]))))
    return x, y

# Обчислення методом Монте-Карло
def monte_carlo_integration(f, a, b, num_samples=1000000):
    total_area = (b - a) * max(f(np.array([a, b])))
    num_points_inside = 0
    points_inside = []

    for i in range(num_samples):
        x, y = generate_random_point(a, b, f)
        if y <= f(x):
            num_points_inside += 1
            points_inside.append((x, y))

    integral = total_area * (num_points_inside / num_samples)
    return integral, points_inside, total_area

# Обчислення похибок
def errors(integral, exact_integral):
    if integral != 0:
        error_abs = abs(exact_integral - integral)
        if exact_integral == 0:
            error_rel = 0
        else:
            error_rel = error_abs / abs(exact_integral)
        print(f"Абсолютна похибка: {error_abs}")
        print(f"Відносна похибка: {error_rel}")
    else:
        print("Апроксимація нульова. Відносна похибка не визначена.")

# Визначення інтервалу
a = 1
b = 2

# Обчислення точного значення інтегралу для тестової та основної функцій
exact_integral1 = monte_carlo_integration(test_function, a, b, num_samples=1000000)[0]
exact_integral2 = monte_carlo_integration(main_function, a, b, num_samples=1000000)[0]

# Обчислення інтегралу методом Монте-Карло та виведення результатів
integral, points_inside, total_area = monte_carlo_integration(main_function, a, b, num_samples=10000)
print(f"Приблизне значення головного інтегралу за допомогою методу Монте-Карло: {integral}")
errors(integral, exact_integral2)

integral_test, points_inside_test, total_area_test = monte_carlo_integration(test_function, a, b, num_samples=10000)
print(f"Приблизне значення тестового інтегралу за допомогою методу Монте-Карло: {integral_test}")
errors(integral_test, exact_integral1)

print(f"Точне значення тестового інтегралу: {exact_integral1}")
print(f"Точне значення головного інтегралу: {exact_integral2}")

# Графіки точних функцій та областей під графіками
x = np.linspace(a, b, 1000)
y = main_function(x)

plt.plot(x, y, color='black', label='Точна функція') 
plt.fill_between(x, y, color='gray', alpha=0.2, label='Область') 
plt.scatter([p[0] for p in points_inside], [p[1] for p in points_inside], s=1, color='purple', label='Точки всередині') 

plt.legend()
plt.show()

x_test = np.linspace(a, b, 1000)
y_test = test_function(x_test)

plt.plot(x_test, y_test, color='black', label='Точна тестова функція')
plt.fill_between(x_test, y_test, color='gray', alpha=0.2, label='Область (тест)') 
plt.scatter([p[0] for p in points_inside_test], [p[1] for p in points_inside_test], s=1, color='pink', label='Точки всередині (тест)')

plt.legend()
plt.show()
