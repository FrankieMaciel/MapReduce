from glob import glob
from threading import Thread

files = glob("./data/*.txt")

tempFile = []
tempFile2 = {}
tempFile3 = {}

def theMap(file):
  f = open(file, "r")
  text = f.read()
  for word in text.split("\n"):
    tempFile.append([word, "1"])


def theProcessor():
  for key, value in tempFile:
    if key in tempFile2:
      tempFile2[key].append(value)
    else:
      tempFile2[key] = [value]


def theReduce(key, value):
  tempFile3[key] = len(value)


def main():
  threads = []
  for file in files:
    t = Thread(target=theMap, args=(file,))
    threads.append(t)
    t.start()

  for t in threads:
    t.join()

  threads = []

  theProcessor()

  for key in tempFile2:
    t = Thread(target=theReduce, args=(key, tempFile2[key],))
    threads.append(t)
    t.start()

  for t in threads:
    t.join()

  print(tempFile3)

main()