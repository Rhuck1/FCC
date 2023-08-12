from prob_calculator import Hat, experiment

hat1 = Hat(red=2, green=2)

res = experiment(hat1, {"red":1, "green":1}, 2, 200)


# def test_hat_class_contents(self):
hat = Hat(red=3,blue=2)
# actual = hat.contents
# expected = ["red","red","red","blue","blue"]
hat2 = Hat(purp=4, diggin=3)
# print(actual)
# print(expected)


print(hat1.contents)