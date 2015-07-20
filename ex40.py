class Song(object):
    # 这里的__init__()为两个下划线self为python创建的空对象
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def __str__(self):
        return str(self.lyrics)

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# 创建对象，__init__函数被调用来初始化对象
birthday = ["Happy brithday to you", "I don't want to get sued"]
happy_bday = Song(birthday)
print(Song(birthday))
parade = ["They rally round the family"]
bulls_on_parade = Song(parade)
print(Song(Song(parade)))

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
