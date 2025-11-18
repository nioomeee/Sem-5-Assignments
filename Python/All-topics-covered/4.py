# Process a large log file efficiently.

# Create a generator function read_logs(filename) that yields one line at a time from a text file (simulating reading a massive file).

# Use a with statement to write a summary to summary.txt.

# Inside the write block, use enumerate() to number the lines as you write them.

# Use assert to ensure the file name passed to the function is not empty.

# writing to the log file 1st

with open("server.log", "w") as f:
    f.write("User: admin\n")
    f.write("Timeout: Error on port 80\n")
    f.write("User logout: admin\n")
    f.write("Warning: Low disk space\n")

def read_logs(filename):
    assert filename and len(filename) > 0, "Filename cannot be empty!"

    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

source = "server.log"

with open("summary.txt", "w") as f:
    for index, content in enumerate(read_logs(source), start = 1):
        f.write(f"\n Line: {index}, Content: {content}")