import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **args):

        # Assign to self object
        self.args = args
        self.contents = []
        self.contents_copy = copy.deepcopy(self.contents)

        # Actions to execute
        for key, val in self.args.items():
            self.contents.extend([key for idx in range(val)])

    def draw(self, draws: int):

        assert draws > 0, "Number of draws must be greater than 0"

        if draws > len(self.contents):
            return self.contents
        else:
            samp_draw = random.sample(self.contents, draws)
            for color in samp_draw:
                self.contents.remove(color)
            return samp_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    experiments = 0
    N = num_experiments
    M = 0
    while experiments != num_experiments:

        hat_copy = copy.deepcopy(hat)

        draw = hat_copy.draw(num_balls_drawn)
            
        draw_results = {color: draw.count(color) for color in set(draw)}

        try:
            comparison = all((draw_results.get(key) >= val for key, val in expected_balls.items()))

        except:
            comparison = False

        if not comparison:
            experiments += 1
            continue
        else:
            M += 1
            experiments += 1

    return M / N