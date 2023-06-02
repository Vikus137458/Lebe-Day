﻿# Глава 2: Обитель желаний/Мальчик с другой планеты

define Unknown = Character('Неизвестный', color="#B22222") #кирпичный
define Dima = Character('Дима', color="#6B8E23") #оливковый
define Curator = Character('Куратор', color="#B22222") #кирпичный
define Alex = Character('Безумный Алекс', color="#4B0082") #индиго
define Vika = Character('Вика', color="#FFD700") #золотой
define Inter = Character('Любитель интерактивчиков', color="#C71585") #среднее между фиолетовым и красным
define Misli = Character('В мыслях у Димы', color="#006400") #темно-зеленый
define Alecsey = Character('Алексей', color="#00CED1") #темно-бирюзовый
define Koreec = Character('Кум Чун Пук', color="#F0E68C") #хаки

# Фотокарточки персонажей
image Вика = "Персонажи/Вика.png"
image Дима = "Персонажи/Дима.png"
image Дима_уставший = "Персонажи/Дима_уставший.png"
image Интерактив = "Персонажи/Интерактив.png"
image Дима_танцует = "Персонажи/Дима_танцует.png"
image Дима_кпоп_танцует = "Персонажи/Дима_кпоп_танцует.png"
image Интерактив_кпоп_танцует = "Персонажи/Интерактив_кпоп_танцует.png"
image Дима_радостный = "Персонажи/Дима_радостный.png"
image Чим Чин Пак_Кум Чун Пук = "Персонажи/Чим Чин Пак_Кум Чун Пук.png"
image Алексей = "Персонажи/Алексей.png"
image Интерактив_грустный = "Персонажи/Интерактив_грустный.png"

# Фотокарточки локаций
image Вход_универ = "Локации/Вход_универ.png"
image Лестница_универ = "Локации/Лестница_универ.png"
image Коридор_универ = "Локации/Коридор_универ.png"
image Магазин_кпоп = "Локации/Магазин_кпоп.png"
image Зал_хорео = "Локации/Зал_хорео.png"
image Актовый_зал = "Локации/Актовый_зал.png"
image Сцена = "Локации/Сцена.png"
image Глава2_надпись = "Локации/Глава2_надпись.png"
image Спустя_пару_часов_надпись = "Локации/Спустя_пару_часов_надпись.png"
image За_кулисами = "Локации/За_кулисами.png"
image Через_полчаса_надпись = "Локации/Через_полчаса_надпись.png"

label start:
    $ carma = 0
    #Введение
    #Глава 1: Преступление и наказание
    scene Глава2_надпись
    "Глава 2: Обитель желаний"
    scene Вход_универ
    "Вход в университет"
    show Дима
    with dissolve
    Dima "Ну и денек вчера был, еще чуть-чуть и мне была бы крышка!"
    scene Лестница_универ
    "Дима поднимается по лестнице" #звук шагов
    scene Коридор_универ
    show Интерактив at right
    with dissolve
    Inter "О, Дима, я как раз тебя искал, ты единственный кто согласился бы на мое предложение…"
    Inter "потому что у тебя нет выбора, ХЕ."
    show Дима_уставший at left
    with dissolve
    Misli "Ёк макарёк, укуси меня пчела."
    hide Дима_уставший
    show Дима at left
    with dissolve
    Dima "Хорошо, ради зачета я готов на все!"
    Inter "В МЯГУ приезжают студенты по обмену из Кореи, нам нужно устроить им теплый прием, поэтому Я решил провести концерт,"
    Inter "на котором хочу выступить со своим номером под названием “Гей-Поп”!"
    Dima "Какое интересное название, как раз нам подходит ( ˘ ³˘)♥︎."
    Inter "Я вижу ты воодушевлен, ну что ж, начнем наше грандиозное погружение в Корейскую культуру."
    scene Магазин_кпоп #звуки к-поп
    "Магазин k-pop товаров"
    show Интерактив at right
    with dissolve
    Inter "Мы находимся в святая святых К-Поп культуры, выбирай всё, что понравится."
    show Дима at left
    with dissolve
    Dima "Что же мне выбрать?"
    hide Дима
    menu:
        "Look Чимина из BTS":
            image Дима_кпоп = "Персонажи/Дима_кпоп1.png"
        "Look Хёнджина из StrayKids":
            image Дима_кпоп = "Персонажи/Дима_кпоп2.png"
        "Look Дахён из Twise":
            image Дима_кпоп = "Персонажи/Дима_кпоп3.png"
    show Дима_кпоп at left
    with dissolve
    Dima "Ну как я вам?"
    Inter "Отлично выглядишь, мне такое нравится."
    Dima "Спасибо, я знаю."
    Inter "Теперь тебе нужно обучиться их главному искусству."
    Dima "Какому? Поедание собак?"
    Inter "Идиот, конечно же нет, их главное искусство - это ТАНЦЫ!"
    "Дима в недоумении поправляет свой костюм."
    scene Зал_хорео #песня к-поп
    "Зал хореографии"
    show Интерактив at right
    with dissolve
    Inter "Раз! Два! Три! Четыре! Раз! Два! Три! Четыре!"
    show Дима_уставший at left
    with dissolve
    Dima "Господи, помереть спокойно не дадут."
    hide Дима_уставший
    show Дима_танцует
    "Дима старается повторить непонятные для него движения, больше похожие на конвульсии бегемота перед смертью."
    Inter "А у тебя хорошо получается, я всегда знал, что интерактивчики делают обучения быстрыми и качественными."
    Inter "А мне никто не верил!!!"
    show Вика at left
    with dissolve
    Vika "Я Вам до сих пор не верю..."
    hide Вика
    scene Спустя_пару_часов_надпись
    "Спустя пару часов"
    scene Актовый_зал
    "Все собрались в актовом зале на Е15. Людей было много, но студентов по-корейски еще больше."
    "Зрители затаили дыхание в ожидании чуда, и вдруг на сцене появились два красивых молодых человека…"
    "Это были ведущие. Они начали объявлять номера. И наконец дошла очередь до нашей пары."
    "Заиграла загадочная музыка, свет потускнел, появился дым, и они начали свое выступление."
    scene Сцена #песня к-поп
    show Дима_кпоп_танцует at left
    show Интерактив_кпоп_танцует at right
    "Все зрители были в шоке, ведь они не ожидали такого профессионализма от новичков."
    "Они были в экстазе, начали подтанцовывать и подпевать."
    "Это было лучшее выступление в истории МЯГУ."
    "Аплодисменты" #звук аплодисментов
    scene За_кулисами
    "За кулисами"
    "После концерта Дима и Любитель интерактивчиков отдыхали в своей гримерке"
    show Дима_радостный at left
    with dissolve
    Dima "Ну что, я заслужил зачет?)"
    show Интерактив at right
    Inter "Конечно, мой золотой"
    "Дима протягивает зачетку, “Любитель интерактивчиков” расписывается."
    "На этом их совместное приключение закончилось, и они просто сидели друг напротив друга и молчали."
    scene За_кулисами
    "Через полчаса"
    "Раздался стук в дверь." #стук в дверь
    "Это были представители студентов по-корейски - Чим Чин Пак, Кум Чун Пук и их переводчик Алексей."
    show Чим Чин Пак_Кум Чун Пук at right
    with dissolve
    Koreec "Что-то на корейском."
    show Алексей at left
    with dissolve
    Alecsey "Вы нам понравились. Мы бы хотели пригласить вас в Корею на наше шоу “Молодость с тобой”,"
    Alecsey "но перед этим хотелось бы поговорить с вами и узнать, как вы достигли такого мастерства."
    Alecsey "Расскажите, в чем ваш секрет?"
    hide Чим Чин Пак_Кум Чун Пук
    show Интерактив at right
    with dissolve
    Inter "На самом деле никакого секрета нет, просто я безумно талантлив."
    Inter "Мне стоит только увидеть танец, чтобы воспроизвести его. Не буду хвастаться, но так не только с танцами…))."
    Inter "Рисовать картины, руководить хором, принимать роды, подковать блоху, кастрировать жеребца - все это мне не составит никакого труда) Хехе."
    hide Inter
    menu:
        "Да-да, он такой. Именно благодаря ему у нас все получилось.":
            jump good_ending
        "Да что ты несешь?! Это все подлог, ложь и провокация! Без меня ты бы не справился. Ты выглядел так хорошо только на моем ужасном фоне!":
            jump bad_ending
        "У меня есть другое мнение на этот счёт. Я считаю, что мы так хорошо выступили благодаря вашей огромной поддержке.":
            jump side_ending
    label good_ending:
        $ carma += 1
        Alecsey "Нам понравился Ваш ответ. Вы согласны отправиться на шоу?"
        Inter "Да! Да! И еще раз да! Я согласен!"
        hide Интерактив
        show Дима_радостный at right
        with dissolve
        Dima "Я бы с радостью, но, к сожалению, я не могу."
        Dima "Сейчас передо мной стоит великая цель - образование, и отказаться от неё я не в силах."
        return
    label bad_ending:
        Alecsey "Вы что себе позволяете! Вся Корея в вас разочарована!"
        Alecsey "Мы и подумать не могли, кто вы на самом деле! Мы уезжаем! БЕЗ ВАС!"
        hide Алексей
        show Интерактив_грустный at right
        with dissolve
        Inter "Что…"
        "Они ушли. Дима взял зачетку, посмотрел на “Любителя интерактивчиков” и молча вышел."
        "А он остался в комнате, продолжая с пустым взглядом смотреть в стену. Сможет ли он справиться с этим?"
        return
    label side_ending:
        Alecsey "Именно такого ответа мы и ждали, ведь в нашей стране каждый знает, что лучшего критика, чем зритель, не найти."
        "“Любитель интерактивчиков” одевается, начинает собирать вещи, но его прерывают слова Алексея."
        Alecsey "Нет-нет, это я не Вам, а Дмитрию."
        hide Интерактив
        Alecsey "Дима, Вы согласны отправиться в незабываемое путешествие?"
        show Дима_радостный at right
        with dissolve
        Dima "Конечно, я за любой движ, кроме голодовки!"
        "Дима улетает в Корею и становится участником тв-шоу."
        return
