import copy
import random
# Consider using the modules imported above.

class Hat:

    contents = []

    def __init__(self, **args):

        # Assign to self object
        self.args = args

        # Actions to execute
        for key, val in self.args.items():
            Hat.contents.extend([key for idx in range(val)])

    def draw(self, draws: int):

        assert draws > 0, "Number of draws must be greater than 0"

        if draws > len(Hat.contents):
            return Hat.contents
        else:
            return random.sample(Hat.contents, draws)
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    def count_balls(lst, x):
        return lst.count(x)
    
    experiments = 0
    N = num_experiments
    M = 0
    while experiments != num_experiments:



        draw = hat.draw(num_balls_drawn)
        # draw_set = set(draw)
        # for color in draw_set:
        #     color_count = draw.count(color)
            
        exp_results = {color: draw.count(color) for color in set(draw)}
        # You are returning experiment results!!!
        # compare exp_results to expected_balls and if you get at least then M += 1
        print(exp_results)

        experiments += 1


    return M / N