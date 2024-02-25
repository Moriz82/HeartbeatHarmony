import matplotlib.pyplot as plt
import matplotlib.animation as animation
import paramiko
from io import StringIO
import time

# SSH credentials
hostname = 'raspi.local'
username = 'moriz'
password = 'toor'

# Initialize SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the Raspberry Pi over SSH
    ssh.connect(hostname, username=username, password=password)

    # Command to run the Python script remotely
    command = 'python3 light_test2.py'

    # Execute the command and open an SSH session
    stdin, stdout, stderr = ssh.exec_command(command)
    time.sleep(1)  # Wait for the script to start running

    # Initialize lists to store data
    data_x = []
    data_y = []

    # Function to update the plot
    def animate(i):
        global data_x, data_y
        try:
            # Read the latest data from the SSH session
            stdout_data = stdout.readline().strip()
            if stdout_data:
                x_val, y_val = map(float, stdout_data.split(','))
                data_x.append(x_val)
                data_y.append(y_val)
                plt.cla()  # Clear the current plot
                plt.plot(data_x, data_y)
                plt.xlabel('Time')
                plt.ylabel('Pulse Count')
                plt.title('Pulse Count vs Time')
                plt.grid(True)
        except Exception as e:
            print(f"Error: {e}")

    # Create a Matplotlib animation
    ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)  # Update every second

    plt.show()

except paramiko.AuthenticationException:
    print("Authentication failed, please verify your credentials.")
except paramiko.SSHException as ssh_ex:
    print(f"Unable to establish SSH connection: {ssh_ex}")
finally:
    # Close the SSH connection
    ssh.close()
