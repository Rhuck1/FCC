from prob_calculator import Hat, experiment

hat1 = Hat(yellow=3, green=2, blue=6)


attempt2 = hat1.draw(15)
print(attempt2)

experiment(hat1, {"red":2, "green":1}, 5, 2000)