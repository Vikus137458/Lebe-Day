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

define Inter = Character('Любитель интерактивчиков', color="#C71585") #среднее между фиолетовым и красным
define Misli = Character('В мыслях у Димы', color="#006400") #темно-зеленый
define Translator = Character('Алексей', color="#00CED1") #темно-бирюзовый
define Korean = Character('Кум Чун Пук', color="#F0E68C") #хаки

define Physical = Character('Зала Стадионовна', color="#bb109c")
define Thounght_swan = Character('Гуси в мыслях', color="#adadad")
define Swan = Character('Гуси', color="#cfcfcf")

define Miss = Character('Мисс Определитель', color="#FF4500") #оранжево-красный

define Bool = Character('Булевый Отец', color="#8B0000") #бордовый

define Dean = Character('Декан', color="#8B008B") #темно-фиолетовый


# Спрайты персонажей:
image ch_Dima = "Characters/Dima.png"
image ch_Unknown = "Characters/Unknown.png"
image ch_Curator = "Characters/Curator.png"
image ch_Slava = "Characters/Slava.png"
image ch_Pasha = "Characters/Pasha.png"
image ch_Ilya = "Characters/Ilya.png"
image ch_Misha = "Characters/Misha.png"
image ch_Dasha = "Characters/Dasha.png"

image ch_Philosopher = "Characters/Philosophe.png"
image ch_Vika = "Characters/Vika.png"

image ch_DimaTired = "Characters/DimaTired.png"
image ch_DimaDance = "Characters/Dima.png"
image ch_DimaHappy = "Characters/DimaHappy.png"
image ch_Inter = "Characters/Inter.png"
image ch_Korean = "Characters/Korean.png"
image ch_Translator = "Characters/Translator.png"
image ch_InterSad = "Characters/InterSad.png"

image ch_Swan = "Characters/Swan.png"
image ch_Physical = "Characters/Physical.png"
image ch_Barbell = "Characters/Barbell.png"
image ch_DimaBlood = "Characters/DimaBlood.png"

image ch_Miss = "Characters/Miss.png"
image ch_Inquisitor = "Characters/Inquisitor.png"

image ch_DimaFear = "Characters/Dima.png"
image ch_Bool = "Characters/Bool.png"

image ch_Dean = "Characters/Dean.png"

# Локации:
image bg_Room66 = "Background/Room66.png"
image bg_Phon = "Background/Phon.png"

image bg_UniverCorridor = "Background/UniverCorridor.png"
image bg_Cabinet214 = "Background/Cabinet214.png"
image bg_BlackList = "Background/BlackList.png"
image bg_ClosetUnderStairs = "Background/Stairs.png"
image bg_Swamp = "Background/Swamp.png"
image bg_EndArrest = "Background/Police.png"

image bg_UniverEntry = "Background/UniverEntry.png"
image bg_UniverStairs = "Background/UniverStairs.png"
image bg_ShopK_pop = "Background/ShopK_pop.png"
image bg_DanceHall = "Background/DanceHall.png"
image bg_AssemblyHall = "Background/AssemblyHall.png"
image bg_Scene = "Background/Scene.png"
image bg_Backstage = "Background/Backstage.png"
image bg_EndTVShow = "Background/EndTVShow.png"

image bg_Street = "Background/Street.png"
image bg_Stadium = "Background/Stadium.png"
image bg_Tower = "Background/Tower.png"
image bg_FightBarbell = "Background/FightBarbell.png"
image bg_Lenin = "Background/Lenin.png"
image bg_FightSwan = "Background/FightSwan.png"

image bg_Cabinet228 = "Background/Cabinet228.png"
image bg_CandyBan = "Background/CandyBan.png"
image bg_Cabinet307 = "Background/Cabinet307.png"
image bg_EndMadhouse = "Background/EndMadhouse.png"


image bg_CabinetDean = "Background/CabinetDean.png"
image bg_Happy_end = "Background/Happy_end.png"
image bg_Lost_end = "Background/Lost_end.png"


label start:
    $ carma = 0
    call Introduction from _call_Introduction

    jump Chapter_1
    label EndChapter_1:

    jump Chapter_2
    label EndChapter_2:

    jump Chapter_3
    label EndChapter_3:

    jump Chapter_4
    label EndChapter_4:
    
    jump Chapter_5
    label EndChapter_5:

    jump Final
    return
