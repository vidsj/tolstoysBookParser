import codecs
import re

class ParseBook(object):

        #this function is used to parse every word in a sentence, with the word id
        def parseWords(self, sentence):
            result={}
            for wid, word in enumerate(sentence.split()):
                #remove special characters from the words. Only include alpha numeric characters
                result[wid] = re.sub('[^a-zA-Z0-9 \n\.]', '', word)
            return result

        #this function parses every line in a paragraph, attaches sentence & sentence ID
        def parseParagraph(self, para_lines):
            result = {}
            new_arr = []
            #print "processing paragraphs..."
            for sid, sentence in enumerate(para_lines):
                result[sid] = {sentence: self.parseWords(sentence)}
            return result

        # Start of the program. Read the file in utf-8 encoding, parse books & chapters.
        # If the book has missing chapter name, the program appends the lines to the last chapter name.
        # If no chapter name found at all, then the program ignore all lines and returns an empty dictionary
        # If book name and chapter_names are correctly present, then inside a chapter whenever a new line is encountered,
        # then the paragraph lines are accumulated in a into list and processed later for sentences and words
        def parse_book(self, filename):
            result = {}
            para_lines = []
            para_id = 0
            in_chapter = False
            book_num_yr = None

            try:
                with codecs.open(filename, encoding='utf-8', mode = 'r') as f:
                    for lineid, line in enumerate(f):

                        if line.startswith("End of the Project"):
                            #reached the end of the book.
                            return result

                        if line.startswith('BOOK'):
                            #initialize the 1st level of the dictionary
                            print "processing books..."
                            book_num_yr = line.strip()
                            result[book_num_yr] = {}
                            continue

                        if line.startswith('CHAPTER'):
                            #initialize the 2nd level of the dictionary
                            print "processing chapters..."
                            chapter_index = line.strip()

                            # reset and initialize for the next chapter
                            in_chapter = True
                            para_lines = []
                            para_id = 0
                            if not book_num_yr:
                                result[book_num_yr] = {}
                            result[book_num_yr][chapter_index] = {}
                            continue

                        if in_chapter:

                            if line == '\n' and para_lines:
                                # A new line with non-empty para_lines list inside the paragraph, indicates the end of paragraph!
                                result[book_num_yr][chapter_index][para_id] = self.parseParagraph(para_lines)

                                #reset for next para or next chapter
                                para_id = para_id + 1
                                para_lines = []
                            else:
                                if(line == '\n'):
                                    continue
                                # begining of a paragraph. accumulate lines in a paragraph
                                para_lines.append(line)
                    return result

            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
