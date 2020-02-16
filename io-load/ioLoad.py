import os

def main():
    large_file = open("path/to/large_file","rb")
    lines = large_file.readlines()
    for x in lines:
        print (x.len())
    large_file.close()
if __name__== "__main__":
  main()