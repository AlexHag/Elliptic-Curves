import matplotlib.pyplot as plt

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

curve = Edward(123, 2503)

x_values, y_values = zip(*curve.points)

plt.scatter(x_values, y_values, color='blue', marker='o', s=5)

plt.title(f"Edwards Curve: x^2 + y^2 = 1 + {curve.d} * x^2 * y^2 mod {curve.p}")
plt.legend()

plt.show()
