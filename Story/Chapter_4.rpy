﻿# Глава 4: “В дурмане“

# Персонажы:
#   Author
#   Dima
#   Miss
#   Vika

#   ch_Dima
#   ch_DimaTired
#   ch_DimaHappy
#   ch_Miss
#   ch_Vika
#   ch_Inquisitor

# Локации:
#   bg_Phon
#   bg_UniverEntry
#   bg_UniverStairs
#   bg_UniverCorridor
#   bg_Cabinet228
#   bg_CandyBan
#   bg_Cabinet307
#   bg_EndMadhouse

label Chapter_4:
    scene bg_Phon
    Author "Глава 4: “В дурмане“" with dissolve

    scene bg_UniverEntry
    Author "Вход в университет"
    Author "Сегодня Дима наконец-то решил встретиться с Мисс Определитель, она была той, у кого была власть,"
    Author "которая и не снилась моему отцу, одним своим словом она могла разрушать целые миры."
    scene bg_UniverStairs
    Author "Дима, не спеша, поднимался по лестнице и искал глазами 228 кабинет." #звук шагов
    Author "Закончив поиски, он тихо приоткрыл дверь и попросил разрешение войти."
    scene bg_Cabinet228
    show ch_Miss at right
    with dissolve
    Author "В центре кабинета за столом сидела женщина, напоминающая хитрую лисицу."
    Author "Ее огненные волосы развивались по всему кабинету, словно ее окутал огонь инквизиции."
    Author "На вид ей было около 30 лет, но на самом деле она была старше пирамид."
    show ch_Dima at left with dissolve
    Dima "Здравствуйте, я ищу Мисс Определитель, Вы не знаете, где она?"
    Miss "А как Вас зовут, сударь?"
    Dima "Дмитрий, а Вас?"
    Miss "А меня нет!"
    Author "Дима стоял в недоумении, не понимая, что на это ответить. Тишину прервал смех этой загадочной женщины."
    Miss "Ахахахаха!" #звук - смех Алисы
    Miss "Ладно, пошутили и хватит. Я та, кого ты ищешь. Зачем ты меня искал?"
    Dima "Мне нужно закрыть долг по вашему предмету."
    Miss "Я буду принимать долги через час в 307 кабинете, приходи один и никому не говори о нашей встрече."
    hide ch_Dima
    show ch_DimaTired at left 
    with dissolve
    Dima "Хорошо, я приду."
    menu:
        Miss "Кстати, сегодня Радоница, нужно вспоминать умерших и дарить людям конфетки, возьми себе несколько."
        
        "Взять одну конфетку":
            show ch_Vika at center with easeinbottom
            Vika "НЕТ! НЕЛЬЗЯ! Нужно взять хотя бы две, а то на всю жизнь останешься один!"
            hide ch_Vika with easeoutbottom
        
        "Взять охапку":
            pass
    Author "Мисс Определитель дает Диме чашу с конфетами и выталкивает его за дверь."
    Author "Дима не понял, что произошло, но поплелся в 307 кабинет, уплетая конфеты."
    scene bg_CandyBan
    Author "Конфеты от незнакомцев вредят вашей жизни"
    scene bg_Cabinet307
    Author "307 кабинет"
    Author "Дима не понимал, что с ним происходит, но у него появилось чувство, будто он знает все не свете."
    Author "Его голову раздувало от переизбытка информации."
    show ch_Miss at right with dissolve
    Author "В кабинет зашла Мисс Определитель и села на свое место."
    show ch_DimaHappy at left with dissolve
    Author "Напротив нее сел Дима. На слоте между ними она разложила свои билеты."
    Author "Они встретились глазами, и, словно мурча, она сказала."
    Miss "Выбиррррррай, у тебя есть полчасика на подготовочку."
    Author "Дима был настолько в себе уверен, что решил ответить сразу на все билеты."
    Author "Спустя 5 минут он ответил на все билеты и был таков."
    Miss "Ты был просто великолепен! Меня поразили твои глубоко - обширные знания."
    Dima "Я рад, что вы остались довольны."
    Miss "Ты меня настолько поразил, что я хочу тебе кое-что предложить."
    Miss "Скажу тебе сразу, что отказаться ты не сможешь."
    Author "У нее в руках Дима увидел свою зачетку и сразу понял, что у него нет выбора."
    Misli "Что же ей от меня нужно?..."
    Miss "Я всего-навсего хочу сделать тебя своим помощником."
    Miss "Ты будешь помогать мне принимать экзамены."
    Dima "Я согласен!"
    Miss "Молодец, ты сделал правильный выбор. Вот твоя зачетка!"
    Misli "Как будто он у меня был…"
    scene bg_UniverCorridor
    Author "Следующие несколько дней Дима помогал ей в приеме экзаменов, но с каждым днем студентов приходило все меньше и меньше."
    Author "Сначала он думал, что все так и должно быть, но в один дождливый день Дима вышел из кабинета и увидел пустой коридор."
    Author "На полу валялись разорванные зачетки. Он подошел к стенду с информацией, на котором было вывешено много списков."
    Author "Подойдя ближе, он понял, что это."
    show ch_DimaTired at left with dissolve
    Dima "Что?! Их всех отчисляют?! Я же принимал у них экзамен, все было хорошо."
    scene bg_Cabinet228
    Author "Дима решил выяснить, в чем дело, потому отправился в кабинет Мисс Определитель."
    Author "Дверь была приоткрыта, он заглянул в щель и увидел ее."
    Author "Она со зловещей улыбкой, растянутой до ушей, быстро ставила печати на документах об отчислении."
    show ch_DimaTired at left with dissolve
    Dima "О нет! Что вы делаете?"
    show ch_Miss at right with dissolve
    Miss "Как жаль, что ты застал меня в таком виде. Я не хотела этого."
    Miss "Придется рассказать тебе мой секрет"
    Miss "Когда-то давно мой клан был уничтожен этими жалкими людишками, и чтобы отомстить, я решила стать самым страшным существом на этой планете..."
    Miss "Старшим преподавателем факультета “Информационных и математических наук”, ахахахаха."
    Miss "Я отомщу этим ублюдкам. Они будут страдать в агонии, просить меня о прощении, но все их попытки будут тщетны, я никогда не изменю свое решение."
    menu:
        Miss "А что насчет тебя, Дима, ты со мной?"

        "Сдать":
            $ carma += 1
            Dima "Вы все это время использовали меня! Как вы могли!"
            Dima "Я просто хотел помочь Вам, а вместо этого стал соучастников Вашего преступления против человечества. Я никогда не присоединюсь к Вам. Я сообщу о Вас инквизиции!"
            Dima "Ищадье тьмы, гореть Вас сизым пламенем, в кромешном аду!"
            show ch_Inquisitor at center with easeinbottom
            Author "За Мисс Определитель пришли инквизиторы."
            Miss "Встретимся в следующей жизни!!! ХАХАХА!" #звук - смех Алисы
            hide ch_Inquisitor
            hide ch_Miss 
            with easeoutbottom
            Author "и увезли ее с собой."
            jump EndChapter_4

        "Сбежать":
            Dima "Вы меня не видели, я Вас не видел!"
            Miss "Это твой выбор. Прощай."
            hide ch_Miss with easeoutright
            hide ch_DimaTired with easeoutleft
            Author "Дверь захлопнулась сама по себе, а Дима вернулся в общежитие."
            jump EndChapter_4

        "Присоединится":
            hide ch_DimaTired
            show ch_DimaHappy at left
            with dissolve
            Dima "Да, моя королева! Я буду служить Вам до конца жизни!"
            scene bg_EndMadhouse with dissolve
            Author "Каждый день Мисс Определитель давала ему вкусные конфетки."
            Author "Дима окончательно сошел с ума."
            Author "Он провел остаток своих дней не со своей королевой, а рядом с Толиком - соседом по палате в психоневрологическом диспансере."  
    return
