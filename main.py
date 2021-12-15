import SSHConnect as SSHConnect

ssh = SSHConnect.SSHConnect()
ssh.put("text.txt", "/tmp/text.txt")
