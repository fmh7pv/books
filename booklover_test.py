import unittest 
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        book_lover =  BookLover("James", "james@vt.edu", "nonfic")
        fake_book = "Harry Potter and the Screaming idk wolves"
        fake_rating = 1
        book_lover.add_book(fake_book, fake_rating)
        self.assertTrue(book_lover.has_read(fake_book))

    def test_2_add_book(self):
        book_lover =  BookLover("James", "james@vt.edu", "nonfic")
        fake_book = "Harry Potter and the Screaming idk wolves"
        fake_rating = 1
        book_lover.add_book(fake_book, fake_rating)
        book_lover.add_book(fake_book, fake_rating)
        expected = 1
        actual = len(book_lover.book_list[book_lover.book_list.book_name == fake_book])
        self.assertEqual(expected, actual)
                
    def test_3_has_read(self): 
        book_lover =  BookLover("James", "james@vt.edu", "nonfic")
        fake_book = "Harry Potter and the Screaming idk wolves"
        fake_rating = 1
        book_lover.add_book(fake_book, fake_rating)
        self.assertTrue(book_lover.has_read(fake_book))
        
    def test_4_has_read(self): 
        book_lover =  BookLover("James", "james@vt.edu", "nonfic")
        fake_book = "Harry Potter and the Screaming idk wolves"
        self.assertFalse(book_lover.has_read(fake_book))
        
    def test_5_num_books_read(self): 
        book_lover =  BookLover("James", "james@vt.edu", "nonfic")
        test_books = [
        ("Jane Eyre", 4),
        ("Fight Club", 3),
        ("The Divine Comedy", 5),
        ("The Popol Vuh", 5)]
        for book in test_books: book_lover.add_book(*book)
        self.assertEqual(len(test_books), book_lover.num_books_read())

    def test_6_fav_books(self):
        book_lover =  BookLover("James", "james@vt.edu", "nonfic")
        test_books =[("Jane Eyre", 4),
        ("Fight Club", 3),
        ("The Divine Comedy", 5),
        ("The Popol Vuh", 5)]
        for book in test_books: book_lover.add_book(*book)
        actual = len(book_lover.fav_books())
        expected = len([x for x, y in test_books if y >3])
        self.assertEqual(actual, expected )
    
if __name__ == '__main__':
    
    unittest.main(verbosity=3)     