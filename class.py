# Parent Class
class Book:
    def __init__(self, title, author, genre, chapters):
        self.title = title
        self.author = author
        self.genre = genre
        self.chapters = chapters
    
    def info(self):
        return f"📖 '{self.title}' by {self.author} | Genre: {self.genre} | Chapters: {self.chapters}"
    
    def read(self, chapter):
        if 1 <= chapter <= self.chapters:
            print(f"📘 Reading chapter {chapter} of '{self.title}'...")
        else:
            print(f"⚠️ Chapter {chapter} does not exist in '{self.title}'!")


# Child Class (LightNovel inherits from Book)
class LightNovel(Book):
    def __init__(self, title, author, genre, chapters, web_serial=True):
        super().__init__(title, author, genre, chapters)  
        self.web_serial = web_serial
    
    def special_feature(self):
        if self.web_serial:
            print(f"🌐 '{self.title}' is also available as a web novel online!")
        else:
            print(f"📚 '{self.title}' is only available in print format.")



supreme_magus = LightNovel(
    title="Supreme Magus",
    author="Legion20",
    genre="Fantasy",
    chapters=3820,
    web_serial=True
)

#
print(supreme_magus.info())
supreme_magus.read(2431)
supreme_magus.read(4000)   # Invalid chapter test
supreme_magus.special_feature()
