class Book():
    def __init__(self,author,pages):
      self.author=author
      self.pages= pages
     
class Ebook(Book):
    def __init__(self,author,pages,filesize):
         super().__init__(author,pages)
         self.filesize=filesize
    def details(self):
        print("Author of the book:",self.author)
        print("NUmber of pages:",self.pages)
        print("File Size:",self.filesize,"MB")

book_1=Ebook("nikky",220,6)
book_1.details()
