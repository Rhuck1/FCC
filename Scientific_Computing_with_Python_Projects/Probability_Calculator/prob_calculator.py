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
            count = 0
            while count != val:
                Hat.contents.append(str(key))
                count += 1

    def draw(self, draws: int):

        assert draws > 0, "Number of draws must be greater than 0"

        if draws > len(Hat.contents):
            return Hat.contents
        else:
            pass
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass