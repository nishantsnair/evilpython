import subprocess

def clean_run(cmd):
	output = subprocess.run([cmd],capture_output=True,shell=True).stdout.decode().splitlines()
	print(output)
	return output

clean_run("cd ~/Desktop; ls")
