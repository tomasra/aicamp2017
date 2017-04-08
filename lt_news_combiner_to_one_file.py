import os

# fill with the file names
filenames = []
directory = '/Users/tp/dev/ml/articles/data/lt-news-201501-201506/2014-12-29/'

def iterate_dirs(inside_dir):
  with open('/Users/tp/dev/ml/articles/aicamp2017/articles.txt', 'w') as outfile:
    for filename in os.listdir(directory):
      if filename.endswith(".txt"):
        with open(directory + filename) as infile:
          txt = infile.read().split('\n')
          txt = ' '.join(txt)
          outfile.write(txt + '\n')
      else:
        iterate_dirs(inside_dir + '/' + filename) 

if __name__ == '__main__':
  iterate_dirs(directory)