# Глава 5: “За все в этой жизни нужно платить“

# Персонажы:
#   Author
#   Dima
#   Bool
#   Vika

# Спрайты персонажей:
#   ch_Dima
#   ch_DimaFear
#   ch_DimaBlood
#   ch_Bool
#   ch_Vika

# Локации:
#   bg_Phon
#   bg_UniverCorridor
#   bg_UniverEntry 
#   bg_Cabinet214
#   bg_Room66

label Chapter_5:
    scene bg_Phon
    "Глава 5: “За все в этой жизни нужно платить“" with dissolve

    scene bg_UniverCorridor
    Author "Наконец-то Дима расправился со всеми предметами, кроме одного - дискретная математика. Сегодня он должен с этим разобраться."
    Author "Для этого ему придется встретиться с самым опасным человеком в университете -  с Булевым отцом."
    Author "Он был известен как самый влиятельный человек в этом городе. Его боялись главы всех синдикатов, и даже Мисс Определитель."
    show ch_DimaFear at left with dissolve
    Author "Дима настолько боялся зайти, что первые пару минут стоял перед дверью, затаив дыхание."
    Author "Но неожиданно дверь открылась сама собой, видимо кто-то на той стороне учуял его страх и решил помочь ему его преодолеть."
    scene bg_Cabinet214
    show ch_DimaFear at left with easeinleft
    Author "Зайдя в кабинет, Дима увидел человека невысокого роста, в черном костюме с бабочкой, который сидел в кожаном кресле."
    show ch_Bool at right with dissolve
    Bool "Проходи, сын мой."
    show ch_DimaFear at center with easeinleft
    Author "Дима подошел к нему, трясясь от страха."
    Bool "Зачем ты пришел?"
    Dima "Мне нужен зачёт."
    Bool "Ты просишь у меня зачет, но делаешь это без уважения..."
    Author "Булев отец протянул Диме руку, но тот не понял этого жеста."
    Dima "Простите, но мне нужен зачет."
    Bool "Каждому человеку при рождении даруется его истинное имя. Ты знаешь, что означают наши?"
    Bool "Я Властелин этого мира, а ты презренный раб."
    Bool "Давай проверим, так ли это? Тяни билет."
    Author "Дима протянул руку к столу, на котором лежали пять билетов. Они были испачканы в какой-то красной жидкости. Он выбрал самый дальний от себя."
    Author "Дима перевернул билет, там было написано лишь одно слово…"
    Author "“Палец“"
    Dima "Что это значит?"
    Bool "Это твоя задача, ты должен ее решить."
    menu:
        Bool "А как ты это сделаешь, решать тебе."

        "Принести настоящий палец":
            $ carma -= 1
            hide ch_DimaFear with easeoutleft
            Author "Дима решил не рисковать своей жизнью и принести Булевому отцу настоящий палец. Сначала он не знал, где его достать"
            scene bg_Room66 with dissolve
            Author "Но потом вспомнил, что под кроватью у Ильи, у его соседа, лежит Карина, поэтому он решил позаимствовать ее палец."
            Author "Сделав дела, за зачетем смело."
            Author "С такими словами Дима пошел к Булевому отцу"
            scene bg_Cabinet214
            show ch_Bool at right with dissolve
            show ch_DimaBlood at center with easeinleft
            Dima "Я все сделал"
            Dima "Вот палец"
            Bool "Молодец, сынок, ты выполнил мое задание, так что забирай свою зачетку."
            Dima "Может нужно еще кого-нибудь убить?"
            Bool "ИИИИИИИДИИИИИ ОТСЮДА!"
            hide ch_DimaBlood with easeoutleft
            Bool "Что за манйак!?"
            show ch_Vika at center with easeinbottom
            Vika "Соглашусь с вами"
            hide ch_Vika with easeoutbottom
            jump EndChapter_5
        
        "Изготовить фальшивку":
            $ carma += 1
            hide ch_DimaFear with easeoutleft
            Author "Дима решил не переступать закон и сделать фальшивый палец из гипса."
            scene bg_UniverEntry with dissolve 
            Author "Для этого он обратился к знакомому гончару Андрею."
            Author "Он изготовил для него очень реалистичный палец."
            Author "Дима поблагодарил и пошел к Булевому отцу"
            scene bg_Cabinet214 with dissolve
            show ch_Bool at right with dissolve
            show ch_DimaFear at center with easeinleft
            Dima "Я все сделал"
            Dima "Вот палец"
            Bool "Молодец, сынок, ты выполнил мое задание, так что забирай свою зачетку."
            Dima "Спасибо, я пойду"
            hide ch_DimaFear with easeoutleft
            Bool "Ужас"
            show ch_Vika at center with easeinbottom
            Vika "Соглашусь с вами"
            hide ch_Vika with easeoutbottom
            jump EndChapter_5

        "Принести сосиску":
            hide ch_DimaFear with easeoutleft
            Author "Дима решил, что все это всего лишь глупая шутка"
            scene bg_UniverEntry with dissolve 
            Author "Поэтому тоже решил пошутить и принес вместо пальца сосиску “Мама может” в кетчупе."
            scene bg_Room66
            Author "На следующий день он был найден мертвым в своей постели, с пулей в груди и без пальцев."
    return