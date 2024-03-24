from mapReduce import mapReduce
import sys, re

class Grep(mapReduce):

  searchInput = None
  isRegex = False

  def printLine(self, start, end, line):
    parte1 = ''
    parte3 = ''
    
    if start > 0:
      parte1 = line[:start]
    if end < len(line):
      parte3 = line[end]

    parte2 = line[start:end]
    print(parte1 + '\033[92m' + parte2 + '\033[0m' + parte3)

  def checkRegex(self, line):
    expression = self.searchInput
    if self.isRegex:
      expression = expression.replace('"', "")
      regexResult = re.search(expression, line)
      if regexResult == None:
        return True
      else:
        self.printLine(
          regexResult.span()[0],
          regexResult.span()[1],
          line
        )
        return False
    else:
      startPos = line.find(expression)
      if startPos > -1:
        endPos = startPos + len(expression)
        self.printLine(startPos, endPos, line)
        return False
      else:
        return True

  def mapper(self, file):
    f = open(file, "r")
    text = f.read()
    for line in text.split("\n"):
      if self.checkRegex(line): continue
      self.emit(file, line)
    f.close()

  def reducer(self, key, value):
    result = len(value)
    for line in value:
      self.result_file.write("{0} {1}\n".format(key, line))

if __name__ == '__main__':
  args = sys.argv

  isRegex = False
  searchInput = args[1]
  fileIndexStart = 2

  if searchInput == '-e':
    isRegex = True
    searchInput = args[2]
    fileIndexStart = 3

  files = [args[index] for index in range(fileIndexStart, len(args))]

  grepper = Grep()
  grepper.searchInput = searchInput
  grepper.isRegex = isRegex
  grepper.files = files
  grepper.activate()
