import os
from glob import glob
from threading import Thread

class mapReduce:
  data_dir = './data'
  temp_dir = './tmp'
  result_dir = './result'

  data_name = '/*.txt'
  temp_name = '/tmp.txt'
  result_name = '/out.txt'

  files = None
  temp_file = None
  result_file = None

  dic = {}

  def checkDirs(self):
    # verifica se os diretorios padrões existem, se não, as cria
    os.makedirs(self.data_dir, exist_ok=True)
    os.makedirs(self.temp_dir, exist_ok=True)
    os.makedirs(self.result_dir, exist_ok=True)

  def mapper(self, file):
    f = open(file, "r")
    text = f.read()
    for word in text.split("\n"):
      self.emit(word, "1")
    f.close()

  def reducer(self, key, value):
    result = len(value)
    self.result_file.write("{0} {1}\n".format(key, result))

  def emit(self, key, value):
    self.temp_file.write("{0} {1}\n".format(key, value))

  def collector(self):
    dic = {}
    self.temp_file.close()
    f = open(self.temp_dir + self.temp_name, "r")
    text = f.read()
    for line in text.split("\n"):
      if line == '': continue
      parts = line.split(' ')
      key = parts[0]
      parts.pop(0)
      value = ' '.join(parts)
      if key in self.dic:
        self.dic[key].append(value)
      else:
        self.dic[key] = [value]

  def activate(self):

    self.checkDirs()

    temp_file_dir = self.temp_dir + self.temp_name
    if os.path.exists(temp_file_dir):
      open(temp_file_dir, 'w').close()
    
    result_file_dir = self.result_dir + self.result_name
    if os.path.exists(result_file_dir):
      open(result_file_dir, 'w').close()

    self.temp_file = open(temp_file_dir, "a")
    self.result_file = open(result_file_dir, "a")

    # retorna uma array com o diretorio de todos os arquivos
    if self.files == None:
      self.files = glob(self.data_dir + self.data_name)

    for file in self.files:
      t = Thread(
        target=self.mapper,
        args=(file,)
      )
      t.start()
      t.join()
    
    self.collector()
    self.dic = dict(sorted(self.dic.items()))

    for key in self.dic:
      t = Thread(
        target=self.reducer,
        args=(key, self.dic[key],)
      )
      t.start()
      t.join()

    self.result_file.close()