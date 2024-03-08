from glob import glob
from threading import Thread

class mapReduce:
  data_dir = './data/*.txt'
  temp_dir = './tmp/tmp.txt'
  result_dir = './result/out.txt'

  dic = {}

  def mapper(self, file):
    f = open(file, "r")
    text = f.read()
    for word in text.split("\n"):
      self.emit(word, "1")

  def reducer(self, key, value):
    result = len(value)
    open(self.result_dir, "a").write("{0} {1}\n".format(key, result))

  def emit(self, key, value):
    open(self.temp_dir, "a").write("{0} {1}\n".format(key, value))

  def collector(self):
    dic = {}
    f = open(self.temp_dir, "r")
    text = f.read()
    for line in text.split("\n"):
      if line == '': continue
      parts = line.split(' ')
      key = parts[0]
      value = parts[1]
      if key in self.dic:
        self.dic[key].append(value)
      else:
        self.dic[key] = [value]

  def activate(self):

    files = glob(self.data_dir)

    for file in files:
      t = Thread(
        target=self.mapper,
        args=(file,)
      )
      t.start()
      t.join()
    
    self.collector()

    for key in self.dic:
      t = Thread(
        target=self.reducer,
        args=(key, self.dic[key],)
      )
      t.start()
      t.join()