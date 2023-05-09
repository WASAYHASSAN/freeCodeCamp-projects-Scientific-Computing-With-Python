
import random
from collections import Counter

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents += [ball] * count

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        balls = random.sample(self.contents, num)
        for ball in balls:
            self.contents.remove(ball)
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**Counter(hat.contents))
        balls_drawn = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = Counter(balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if drawn_balls_count[color] < count:
                success = False
                break
        if success:
            num_success += 1
    return num_success / num_experiments


# Create a hat object with 5 blue balls, 4 red balls, and 2 green balls
hat = Hat(blue=5, red=4, green=2)

# Define the expected balls to draw
expected_balls = {"red": 1, "green": 2}

# Draw 3 balls in each experiment and perform 1000 experiments
num_balls_drawn = 3
num_experiments = 1000

# Run the experiment and get the probability
probability = experiment(hat=hat, expected_balls=expected_balls,
                          num_balls_drawn=num_balls_drawn, num_experiments=num_experiments)

# Print the result
print("Probability:", probability)
