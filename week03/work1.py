from concurrent.futures import ThreadPoolExecutor
import sys
import os
import socket
import threading


class Work1:

    def ipPing(self, ip):
        """
        ping命令监测IP是否可以ping通
        -c 1 :发送报文1次
        -w 1 :等待时间1s
        :return: ip
        """
        backInfo = os.system(f'ping -c 1 {ip} ')
        print(backInfo)
        if backInfo != 0:
            print(f'不能通过的IP为：{ip}')
        else:
            print(f'通过的IP为：{ip}')
            return ip

    def scan(self, ip):
        s = socket.socket()
        try:
            for i in range(1, 1024):
                if s.connect_ex((ip, i)) == 0:
                    return f'{i} : open'
        except Exception as ex:
            print('端口扫描错误')
        finally:
            s.close()


class ThreadingWork1(threading.Thread):
    def __init__(self, ):
        super().__init__()
        self.args = sys.argv
        self.ipList = []
        try:
            self.num = self.args[self.args.index('-n') + 1]
            self.type = self.args[self.args.index('-f') + 1]
            self.host = self.args[self.args.index('-ip') + 1]
            if '-' in self.host:
                ip = self.host.split('-')
                self.start = int(ip[0].split('.')[-1])
                self.end = int(ip[1].split('.')[-1])
                ips = ip[0].split('.')
                for i in range(self.start, self.end):
                    ip = f'{ips[0]}.{ips[1]}.{ips[2]}.{i}'
                    self.ipList.append(ip)
            if self.type == 'tcp':
                self.fileName = self.args[self.args.index('-w') + 1]

        except KeyError as ex:
            print('命令有误，请重新输入')

    def run(self,) -> None:
        with ThreadPoolExecutor(max_workers=int(self.num)) as executor:
            if self.type == 'ping':
                executor.submit(Work1().ipPing(self.ipList))
            else:
                executor.submit(Work1().scan(self.host))


if __name__ == '__main__':
    ThreadingWork1().run()
    # Work1().ipPing('127.0.0.1')
