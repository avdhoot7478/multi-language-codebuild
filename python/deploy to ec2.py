import paramiko

host = "13.201.166.8 "

username = "ec2-user"

key = "key.pem"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy()
)

ssh.connect(
    host,
    username=username,
    key_filename=key
)

stdin, stdout, stderr = ssh.exec_command(
    "python3 app.py"
)

print(stdout.read().decode())

ssh.close()
