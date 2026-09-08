import numpy as np
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

        #line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="sin(x)", color='blue')
plt.title("Sine Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()

#bar chat

cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai']
population = [18, 20, 12, 8]

plt.figure(figsize=(6,4))
plt.bar(cities, population, color='green')
plt.title("Population of Cities (in millions)")
plt.xlabel("Cities")
plt.ylabel("Population")
plt.show()
