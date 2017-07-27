class Page:
    def __init__(self, id, title, content, sectionID):
        self.id = int(id)
        self.title = title
        self.content = content
        self.sectionID = sectionID
    def toDictionary(self):
        dictionary = {
            "title" : self.title,
            "postId" : self.id,
            "content" : self.content,
        }
        return dictionary

art1sections = { 1 : open("template/satPrep1readingSection1.html").read(),
                 2 : open("template/satPrep1readingSection2.html").read(),
                 3 : open("template/satPrep1readingSection3.html").read(),
                 4 : open("template/satPrep1endPage.html")
}

home = Page(0, "Home",  open("template/id0content.html").read(), [])
page1 = Page(1, "Basic Read Mode", open("template/id1content.html").read(), [])
page2 = Page(2, "Categories", open("template/categoryHomeContent.html").read(), [])
page3 = Page(3, "Challenges", open("template/challengeHomeContent.html").read(), [])
art1 = Page(1, "SAT Prep 1", art1sections[1] , 1)
#art1 = Page(2, "SAT Prep 1", open("template/satPrep1Content.html").read(), [])
pages = { 0 : home,
          1 : page1,
          2 : page2,
          3 : page3
        }
excerptPages = {
          1 : art1
}
transitionDictionary = {
    1 : 2,
    2 : 3
}
