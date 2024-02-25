import matplotlib.pyplot as plt

# Lists to store data
data_x = []
data_y = []

# Read data from file
with open("plotted_data.txt", "r") as file:
    for line in file:
        x_val, y_val = map(float, line.strip().split())
        data_x.append(x_val)
        data_y.append(y_val)

# Plot the data
plt.figure(figsize=(10, 8))
plt.plot(data_x, data_y)
plt.xlabel('Time')
plt.ylabel('Pulse Count')
plt.title('Pulse Count vs Time')
plt.grid(True)
plt.show()
