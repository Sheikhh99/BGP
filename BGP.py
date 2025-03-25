import paramiko

host = '192.168.1.1'
username = 'admin'
password = 'mypassword'

try:
    print("Attempting SSH connection to", host)

    ssh = paramiko.SSHClient()
    ssh.connect(host, username=username, password=password, look_for_keys=False, timeout=15)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    stdin, stdout, stderr = ssh.exec_command("show ip interface brief")
    output = stdout.read().decode()

    print("SSH Connection Successful! Output:\n", output)
    ssh.close()

except paramiko.AuthenticationException:
    print("SSH Connection Failed: Authentication error (wrong username/password)")
except paramiko.SSHException as e:
    print("SSH Connection Failed: SSH error -", str(e))
except Exception as e:
    print("SSH Connection Failed: General error -", str(e))



