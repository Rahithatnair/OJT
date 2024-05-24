import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # gravity (m/s^2)
e = 0.75  # coefficient of restitution (bounciness)
initial_height = 10  # initial height of the ball (meters)
dt = 0.02  # time step (seconds)

# Initialize position and velocity
y = initial_height
v = 0

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, initial_height + 1)
ball, = ax.plot([], [], 'o', markersize=20)

def init():
    ball.set_data([], [])
    return ball,

def update(frame):
    global y, v
    v += -g * dt
    y += v * dt

    if y <= 0:
        y = 0
        v = -v * e

    ball.set_data([0], [y])
    return ball,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 10, dt), init_func=init, blit=True, interval=dt*1000)

# Display the animation
plt.show()



 
 	