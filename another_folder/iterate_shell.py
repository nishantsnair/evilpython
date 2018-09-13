import subprocess

def clean_run(cmd):
	output = subprocess.run([cmd],capture_output=True,shell=True).stdout.decode().splitlines()
	print(output)
	return output

i = 0
while i < 10:
	clean_run("touch file_" + str(i) + ".txt")
	i = i + 1
