
# markers in matplotlib (circle,triangle,square,star)
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]
plt.plot(x,y,marker='o',linestyle='-.',color='b',markersize=6,markerfacecolor='r')
plt.title("line plot with markers")
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.show()
