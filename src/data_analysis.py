import sys
import matplotlib.pyplot as plt

# Define the data file

data_file = sys.argv[1]
output_file = sys.argv[2]

# Initialize empty lists for x and y values
x_values = []
y_values = []

# Read the data file and extract x and y values
with open(data_file, 'r') as f:
    for line in f:
        # Split the line into tokens
        tokens = line.split(' ')

        # Extract x and y values (assuming x is the first and y is the last)
        x = float(tokens[0])
        y = float(tokens[-1])

        # Append the values to the lists
        x_values.append(x)
        y_values.append(y)

# Create the plot
plt.plot(x_values, y_values)

# Add labels and title
plt.xlabel('Tempo de execução')
plt.ylabel('N')

# Show the plot
plt.show()
plt.savefig(output_file)