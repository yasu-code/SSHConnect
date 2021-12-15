import json
import paramiko


class SSHConnect():
    def __init__(self):
        self.json_open = open('connection_address.json', 'r')
        self.json_load = json.load(self.json_open)
        self.connection_info = []

        for v in self.json_load:
            self.connection_info.append(v)


    def connection(self, ip, port, user):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(ip, port=port, username=user)
        self.sftp_connection = self.client.open_sftp()

    def put(self, local_file, remote_file):
        try:
            for info in self.connection_info:
                self.connection(info["ip"], info["port"], info["user"])
                self.sftp_connection.put(local_file, remote_file)
                print(info["ip"] + " completed!!")
                self.client.close()
        except(e):
            print(e)
        finally:
            self.client.close()
        
# ssh = SSHConnect()
# ssh.put("text.txt", "/tmp/text.txt")
