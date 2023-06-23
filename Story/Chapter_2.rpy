# Глава 2: “Обитель желаний“

# Персонажы: 
#   Dima
#   Author
#   Inter
#   Misli
#   Vika
#   Korean
#   Translator

# Спрайты персонажей:
#   ch_Dima
#   ch_DimaTired
#   ch_DimaDance
#   ch_DimaHappy
#   ch_Inter
#   ch_Vika
#   ch_Korean
#   ch_Translator
#   ch_InterSad

# Локации:
#   bg_Phon
#   bg_UniverEntry
#   bg_UniverStairs
#   bg_ShopK_pop
#   bg_DanceHall
#   bg_AssemblyHall
#   bg_Scene
#   bg_Backstage
#   bg_EndTVShow



label Chapter_2:
    scene bg_Phon
    Author "Глава 2: “Обитель желаний“" with dissolve
    
    scene bg_UniverEntry
    Author "Вход в университет"
    show ch_Dima with dissolve
    Dima "Ну и денек вчера был, еще чуть-чуть и мне была бы крышка!"
    scene bg_UniverStairs
    Author "Дима поднимается по лестнице" #звук шагов
    scene bg_UniverCorridor
    show ch_Inter at right with dissolve
    Inter "О, Дима, я как раз тебя искал, ты единственный кто согласился бы на мое предложение…"
    Inter "потому что у тебя нет выбора, ХЕ."
    show ch_DimaTired at left with dissolve
    Misli "Ёк макарёк, укуси меня пчела."
    hide ch_DimaTired
    show ch_Dima at left
    with dissolve
    Dima "Хорошо, ради зачета я готов на все!"
    Inter "В МЯГУ приезжают студенты по обмену из Кореи, нам нужно устроить им теплый прием, поэтому Я решил провести концерт,"
    Inter "на котором хочу выступить со своим номером под названием “Гей-Поп”!"
    Dima "Какое интересное название, как раз нам подходит ( ˘ ³˘)♥︎."
    Inter "Я вижу ты воодушевлен, ну что ж, начнем наше грандиозное погружение в Корейскую культуру."
    scene bg_ShopK_pop #звуки к-поп
    Author "Магазин k-pop товаров"
    show ch_Inter at right with dissolve
    Inter "Мы находимся в святая святых К-Поп культуры, выбирай всё, что понравится."
    menu:
        Dima "Что же мне выбрать?"

        "Look Чимина из BTS":
            show expression "Characters/DimaHappy.png" at left with dissolve

        "Look Хёнджина из StrayKids":
            show expression "Characters/DimaHappy.png" at left with dissolve

        "Look Дахён из Twise":
            show expression "Characters/DimaHappy.png" at left with dissolve
    Dima "Ну как я вам?"
    Inter "Отлично выглядишь, мне такое нравится."
    Dima "Спасибо, я знаю."
    Inter "Теперь тебе нужно обучиться их главному искусству."
    Dima "Какому? Поедание собак?"
    Inter "Идиот, конечно же нет, их главное искусство - это ТАНЦЫ!"
    Author "Дима в недоумении поправляет свой костюм."
    scene bg_DanceHall #песня к-поп
    Author "Зал хореографии"
    show ch_Inter at right with dissolve
    Inter "Раз! Два! Три! Четыре! Раз! Два! Три! Четыре!"
    show ch_DimaTired at left with dissolve
    Dima "Господи, помереть спокойно не дадут."
    hide ch_DimaTired
    show ch_DimaDance with dissolve
    Author "Дима старается повторить непонятные для него движения, больше похожие на конвульсии бегемота перед смертью."
    Inter "А у тебя хорошо получается, я всегда знал, что интерактивчики делают обучения быстрыми и качественными."
    Inter "А мне никто не верил!!!"
    show ch_Vika at left with easeinleft
    Vika "Я Вам до сих пор не верю..."
    hide ch_Vika with easeoutleft
    scene bg_Phon
    Author "Спустя пару часов"
    scene bg_AssemblyHall
    Author "Все собрались в актовом зале на Е15. Людей было много, но студентов по-корейски еще больше."
    Author "Зрители затаили дыхание в ожидании чуда, и вдруг на сцене появились два красивых молодых человека…"
    Author "Это были ведущие. Они начали объявлять номера. И наконец дошла очередь до нашей пары."
    Author "Заиграла загадочная музыка, свет потускнел, появился дым, и они начали свое выступление."
    scene bg_Scene #песня к-поп
    Author "Все зрители были в шоке, ведь они не ожидали такого профессионализма от новичков."
    Author "Они были в экстазе, начали подтанцовывать и подпевать."
    Author "Это было лучшее выступление в истории МЯГУ."
    Author "*Аплодисменты*" #звук аплодисментов
    scene bg_Backstage
    Author "За кулисами"
    Author "После концерта Дима и Любитель интерактивчиков отдыхали в своей гримерке"
    show ch_DimaHappy at left with dissolve
    Dima "Ну что, я заслужил зачет?)"
    show ch_Inter at right with dissolve
    Inter "Конечно, мой золотой"
    Author "Дима протягивает зачетку, “Любитель интерактивчиков” расписывается."
    Author "На этом их совместное приключение закончилось, и они просто сидели друг напротив друга и молчали."
    scene bg_Backstage
    Author "Через полчаса"
    Author "Раздался стук в дверь." #стук в дверь
    Author "Это были представители студентов по-корейски - Чим Чин Пак, Кум Чун Пук и их переводчик Алексей."
    show ch_Korean at right with dissolve
    Korean "Что-то на корейском."
    show ch_Translator at left with dissolve
    Translator "Вы нам понравились. Мы бы хотели пригласить вас в Корею на наше шоу “Молодость с тобой”,"
    Translator "но перед этим хотелось бы поговорить с вами и узнать, как вы достигли такого мастерства."
    Translator "Расскажите, в чем ваш секрет?"
    hide ch_Korean
    show ch_Inter at right with dissolve
    Inter "На самом деле никакого секрета нет, просто я безумно талантлив."
    Inter "Мне стоит только увидеть танец, чтобы воспроизвести его. Не буду хвастаться, но так не только с танцами…))."
    Inter "Рисовать картины, руководить хором, принимать роды, подковать блоху, кастрировать жеребца - все это мне не составит никакого труда) Хехе."
    hide ch_Inter
    menu:
        "Да-да, он такой.":
            $ carma += 1
            show ch_Dima at right
            Dima "Именно благодаря ему у нас все получилось."
            Translator "Нам понравился Ваш ответ. Вы согласны отправиться на шоу?"
            show ch_Inter at right with easeinleft
            hide ch_Dima
            Inter "Да! Да! И еще раз да! Я согласен!"
            hide ch_Inter with easeoutright
            show ch_DimaHappy at right with easeinright
            Dima "Я бы с радостью, но, к сожалению, я не могу."
            Dima "Сейчас передо мной стоит великая цель - образование, и отказаться от неё я не в силах."
            jump EndChapter_2

        "Да что ты несешь?!":
            show ch_Dima at right
            Dima "Это все подлог, ложь и провокация! Без меня ты бы не справился. Ты выглядел так хорошо только на моем ужасном фоне!"
            Translator "Вы что себе позволяете! Вся Корея в вас разочарована!"
            Translator "Мы и подумать не могли, кто вы на самом деле! Мы уезжаем! БЕЗ ВАС!"
            hide ch_Dima
            show ch_InterSad at right 
            with dissolve
            Inter "Что…"
            hide ch_Translator with easeoutleft
            Author "Они ушли."
            Author "Дима взял зачетку, посмотрел на “Любителя интерактивчиков” и молча вышел."
            Author "А он остался в комнате, продолжая с пустым взглядом смотреть в стену. Сможет ли он справиться с этим?"
            jump EndChapter_2

        "У меня есть другое мнение на этот счёт.":
            show ch_Dima at right
            Dima "Я считаю, что мы так хорошо выступили благодаря вашей огромной поддержке."
            Translator "Именно такого ответа мы и ждали, ведь в нашей стране каждый знает, что лучшего критика, чем зритель, не найти."
            Author "“Любитель интерактивчиков” одевается, начинает собирать вещи, но его прерывают слова Алексея."
            Translator "Нет-нет, это я не Вам, а Дмитрию."
            Translator "Дима, Вы согласны отправиться в незабываемое путешествие?"
            hide ch_Dima
            show ch_DimaHappy at right
            with dissolve
            Dima "Конечно, я за любой движ, кроме голодовки!"
            scene bg_EndTVShow
            Author "Дима улетает в Корею и становится участником тв-шоу."
    return
