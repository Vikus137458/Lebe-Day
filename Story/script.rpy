
#Персонажы:

define Dima = Character('Дима', color="#6B8E23") #оливковый
define Author = Character('', color="#c8ffc8")
define Unknown = Character('Неизвестный', color="#B22222") #кирпичный
define Curator = Character('Куратор', color="#B22222") #кирпичный
define Slava = Character('Слава', color="#ff00ff")
define Pasha = Character('Паша', color="#00bfff")
define Ilya = Character('Илья', color="#99e00bd8")
define Misha = Character('Миша', color="#242424")

define Philosopher = Character('Безумный Алекс', color="#4B0082") #индиго
define Vika = Character('Вика', color="#FFD700") #золотой

define Alex = Character('Безумный Алекс', color="#4B0082") #индиго
define Inter = Character('Любитель интерактивчиков', color="#C71585") #среднее между фиолетовым и красным
define Misli = Character('В мыслях у Димы', color="#006400") #темно-зеленый
define Alecsey = Character('Алексей', color="#00CED1") #темно-бирюзовый
define Koreec = Character('Кум Чун Пук', color="#F0E68C") #хаки


define Physical = Character('Зала Стадионовна', color="#ffffff")
define Thounght_swan = Character('Гуси в мыслях', color="#ffffff")
define Swan = Character('Гуси', color="#ffffff")

#image bg_Room66 = "Background/Room66.png"


# Персонажы:
#image ch_Unknown = "Characters/Unknown.png"
#image ch_Dima = "Characters/Dima.png"
#image ch_Curator = "Characters/Curator.png"


# Фон:
#image bg_NextDay = "Background/NextDay.png"
label start:
    $ carma = 0
    #call Introduction

    #jump Chapter_1
    label EndChapter_1:

    #jump Chapter_2
    label EndChapter_2:

    #jump Chapter_3
    label EndChapter_3:

    jump Chapter_4
    label EndChapter_4:
    return
