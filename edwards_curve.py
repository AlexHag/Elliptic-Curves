import matplotlib.pyplot as plt
import os

class Edward:
    def __init__(self, d, p):
        self.d = d
        self.p = p
        self.points = []
        self.definePoints()
    
    def definePoints(self):
        for x in range(self.p):
            for y in range(self.p):
                if self.equalModp(x*x + y*y, 1 + self.d*x*x*y*y):
                    self.points.append((x, y))

    def reduceModp(self, x):
        return x % self.p

    def equalModp(self, x, y):
        return self.reduceModp(x - y) == 0

    def printPoints(self):
        print(self.points)

out_dir = "edwards_curve_images"
if not os.path.exists(out_dir):
        os.makedirs(out_dir)

plt.ion()
fig, ax = plt.subplots()

# primes = [73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
primes = [113, 131, 137, 151, 163, 179, 191, 193, 211, 173, 181, 197, 199, 223, 227, 229]
for prime in primes:
    curve = Edward(123, prime)
    x_values, y_values = zip(*curve.points)
    ax.clear()
    ax.set_axis_off()
    ax.scatter(x_values, y_values, color='blue', marker='o', s=5)

    # plt.title(f"Edwards Curve: x^2 + y^2 = 1 + {curve.d} * x^2 * y^2 mod {curve.p}")
    plt.savefig(f"{out_dir}/ed_d_{curve.d}_p_{prime}.png", bbox_inches='tight')
    plt.legend()
    plt.draw()
    plt.pause(1)