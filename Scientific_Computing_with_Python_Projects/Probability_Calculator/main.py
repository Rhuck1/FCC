from prob_calculator import Hat, experiment

hat1 = Hat(red=2, green=2)


# attempt2 = hat1.draw(15)
# print(attempt2)

res = experiment(hat1, {"red":1, "green":1}, 2, 200)

print(res)

