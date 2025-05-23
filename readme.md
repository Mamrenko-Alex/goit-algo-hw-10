# Метод Монте-Карло для обчислення площі трикутника

## Завдання

Реалізовано алгоритм обчислення визначеного інтеграла методом Монте-Карло. Для прикладу використано обчислення площі прямокутного трикутника з катетами `a = 10` та `b = 5`.

## Опис методу

Метод Монте-Карло полягає у генерації великої кількості випадкових точок у прямокутнику, що містить фігуру (у даному випадку — трикутник). Частка точок, які потрапляють всередину фігури, дозволяє оцінити її площу.

## Реалізація

- Задано розміри прямокутного трикутника: `a = 10`, `b = 5`.
- Згенеровано `N = 10 000` випадкових точок у прямокутнику розміру `a × b`.
- За допомогою функції `is_inside_triangle(x, y)` перевірено, чи потрапляє кожна точка в межі трикутника.
- Відношення кількості точок, що потрапили у трикутник, до загальної кількості точок помножено на площу прямокутника для отримання оцінки площі трикутника.

## Результати

- **Оцінена площа (метод Монте-Карло):** ≈ `24.95`
- **Аналітичне значення:** `25.0`  
  (за формулою площі прямокутного трикутника)
- **Відносна похибка:** `< 0.5%`

## Висновки

Реалізація алгоритму Монте-Карло дозволяє отримати результат, що практично збігається з аналітичним. Це свідчить про правильність розрахунків і ефективність методу. Похибка знаходиться у допустимих межах та може бути зменшена шляхом збільшення кількості випадкових точок (`N`).
