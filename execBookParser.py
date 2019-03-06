import bookParser
import os

def main():
    try:
        #filename='/Users/sujeet/Desktop/TolstoysWarNPeace/dev.txt'
        filename = os.environ["FILE_PATH"]
        result = bookParser.ParseBook()
        output = result.parse_book(filename)
        print output
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

if __name__ == '__main__':
    main()
