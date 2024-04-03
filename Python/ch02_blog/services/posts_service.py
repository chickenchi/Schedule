from models.posts_db import PostDB

class PostService:
    def __init__(self):
        self.posts_db = PostDB()

    def get(self):
        return self.posts_db.get()
    
    def call(self, index):
        return self.posts_db.call(index)

    def add(self, posts):
        return self.posts_db.add(posts)
    
    def delete(self, index):
        return self.posts_db.delete(index)
    
    def revision(self, posts, index):
        return self.posts_db.revision(posts, index)