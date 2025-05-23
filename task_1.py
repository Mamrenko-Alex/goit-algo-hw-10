from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="production-optimization", sense=LpMaximize)

x = LpVariable(name="lemonade", lowBound=0, cat='Integer')
y = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

model += x + y, "Total_Products"

model += (2*x + y <= 100, "Water")
model += (1*x <= 50, "Sugar")
model += (1*x <= 30, "Lemon_Juice")
model += (2*y <= 40, "Fruit_Puree")

model.solve(PULP_CBC_CMD(msg=False))

print(f"Кількість лимонаду: {x.value()}")
print(f"Кількість фруктового соку: {y.value()}")
print(f"Загальна кількість продуктів: {x.value() + y.value()}")
