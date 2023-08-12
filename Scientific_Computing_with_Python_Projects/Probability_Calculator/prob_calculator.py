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
    
    print("experiment")