#configure file name per test case and run the test cases below
filename='/Users/sujeet/Desktop/TolstoysWarNPeace/dev.txt'


# 1.) count the number of books in the file
def countBooks(output):
    #count the number of books
    result = ParseBook()
    output = result.parse_book(filename)
    return len(output.keys())

assert(countBooks(output))==5


# 2.) count the number of chapters per book name
def countChapters(output):
    #count the number of chapters in each book
    for book, chapter in output.iteritems():
        return (book, len(chapter.keys()))

book_name = 'BOOK ONE: 1805'
assert(countChapters(output, book_name)) == 28

book_name = 'BOOK FOUR: 1806'
assert(countChapters(output, book_name)) == 16

book_name = 'BOOK THREE: 1805'
assert(countChapters(output, book_name)) == 19

book_name = 'BOOK SIX: 1805'
assert(countChapters(output, book_name)) == 0

book_name= 'BOOK TWO: 1805'
assert(countChapters(output, book_name)) == 21


# 3.) count the no of paragraphs per a chapter
def countParagraph(output, book_name, chapter_name):
    #count the no of paragraphs in a chapter
    for book, chapter in output.iteritems():
        if book == book_name:
            for chapter, para in chapter.iteritems():
                if chapter == chapter_name:
                    return len(para.keys())


assert(countParagraph(output, book_name = 'BOOK ONE: 1805', chapter_name='CHAPTER I')) == 42


# 4.) If the books contain no chapter name,
#the program appends the lines to the last chapter name and/or ignore all lines if no chapter name found

filename='/Users/sujeet/Desktop/TolstoysWarNPeace/NoChapter.txt'
def noChapterName(filename):
    result = ParseBook()
    output = result.parse_book(filename)
    return output



# 5.) if the file contain no book names, Book Name is assigned as None. Review the output

filename='/Users/sujeet/Desktop/TolstoysWarNPeace/NoBookname.txt'

def noBookName(filename):
    result = ParseBook()
    output = result.parse_book(filename)
    return output.keys()

assert(noBookName(filename))==[0, u'BOOK ONE: 1805']


# 6.) incorrect filename should throw exception. Review the output
filename=' '

def checkEmptyFile(filename):
    result = ParseBook()
    output = result.parse_book(filename)
    return output

checkEmptyFile(filename)


# 7.) file with no headers.File with no hearders should run without failing the program. Review the output

filename='/Users/sujeet/Desktop/TolstoysWarNPeace/NoHeader.txt'

def no_headers(filename):
    result = ParseBook()
    output = result.parse_book(filename)
    return output

no_headers(filename)

# 8.) file with no footers. The program should run successfully. Review the output
filename='/Users/sujeet/Desktop/TolstoysWarNPeace/NoFooter.txt'

def no_footers(filename):
    #multiple new lines in a chapter. shouldn't fail. return the same output
    result = ParseBook()
    output = result.parse_book(filename)
    return output

no_footers(filename)
