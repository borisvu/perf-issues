import os, time

# Could use fcntl.flock instead.

class FileLock:
    def __init__(self, filename):
        self.filename = filename
        self.fd = None
        self.pid = os.getpid()
    
    def acquire(self):
        try:
            self.fd = os.open(self.filename, os.O_CREAT|os.O_EXCL|os.O_RDWR)
            os.write(self.fd, "%d".encode() % self.pid)
            return 1
        except OSError:
            self.fd = None
            return 0
    
    def release(self):
        if not self.fd:
            return 0
        try:
            os.close(self.fd)
            os.remove(self.filename)
            self.fd = None
            return 1
        except OSError:
            return 0
    
    def __del__(self):
        self.release

def main():
    lock = FileLock("lock.file")
    while 1:
        if lock.acquire():
            print("Acquired lock.")
            time.sleep(1)
            print("Forgot to release lock.")

if __name__ == "__main__":
    main()