
import unittest
from bookParser import *

class BookTest(unittest.TestCase):
    def test_countBooks(self):
        '''
        Tests number of books
        '''
        filename='dev.txt'
        parser = ParseBook()
        output = parser.parse_book(filename)

        # test book count
        self.assertEqual(5, len(output.keys()))
        # test chapter count
        self.assertEqual(28, len(output["BOOK ONE: 1805"].keys()))
        self.assertEqual(16, len(output["BOOK FOUR: 1806"].keys()))
        self.assertEqual(19, len(output["BOOK THREE: 1805"].keys()))
        self.assertEqual(0, len(output["BOOK SIX: 1805"].keys()))
        # test paragraphs count
        para = output["BOOK ONE: 1805"]["CHAPTER I"]
        self.assertEqual(42, len(para.keys()))

    def test_no_book_name(self):
        filename='NoBookname.txt'
        parser = ParseBook()
        output = parser.parse_book(filename)
        self.assertTrue(None in output.keys())

    def test_no_chapter_name(self):
        filename='NoChapter.txt'
        parser = ParseBook()
        output = parser.parse_book(filename)
        self.assertEqual(0, len(output['BOOK ONE: 1805'].keys()))

    def test_empty_file(self):
        filename=''
        parser = ParseBook()
        self.assertRaises(IOError, parser.parse_book, filename)

    def test_no_headers(self):
        filename='noHeader.txt'
        parser = ParseBook()
        output = parser.parse_book(filename)
        self.assertEqual(1, len(output.keys()))

    def test_no_footers(self):
        filename='noFooter.txt'
        parser = ParseBook()
        output = parser.parse_book(filename)
        self.assertEqual(4, len(output.keys()))


if __name__ == '__main__':
    unittest.main()
