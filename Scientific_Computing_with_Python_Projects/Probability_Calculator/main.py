from prob_calculator import Hat, experiment

hat1 = Hat(red=2, green=2)

res = experiment(hat1, {"red":1, "green":1}, 2, 200)


# def test_prob_experiment(self):
hat2 = Hat(blue=3,red=2,green=6)
# probability2 = experiment(hat=hat2, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
# actual2 = probability2
# expected2 = 0.272
# print("hat 2 contents copy", hat2.contents_copy)
# print("actual 2 prob:", actual2)
# print("expected 2 prob:", expected2)
# print('Expected experiment 2 method to return a different probability.')
# hat3 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# probability3 = experiment(hat=hat3, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
# actual3 = probability3
# expected3 = 1.0
# print("hat 3 contents copy", hat3.contents_copy)
# print("actual 3 prob:", actual3)
# print("expected 3 prob:", expected3)
# print('Expected experiment 3 method to return a different probability.')



actual = hat2.draw(4)
print("actual:", actual)
print("length:", len(hat2.contents))