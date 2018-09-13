import subprocess
output = subprocess.run(['ls'],capture_output=True).stdout.decode().splitlines()
print(output)
