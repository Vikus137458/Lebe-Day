# Глава 3: “Лебединый хаос“

# Персонажы:
#   Author
#   Dima
#   Misli
#   Physical
#   Thounght_swan
#   Swan
#   Vika

# Спрайты персонажей:
#   ch_Dima
#   ch_Swan
#   ch_Unknown
#   ch_Physical
#   ch_Barbell
#   ch_DimaBlood

# Локации:
#   bg_Phon
#   bg_Street
#   bg_Stadium
#   bg_Tower
#   bg_FightBarbell
#   bg_Lenin
#   bg_FightSwan

label Chapter_3:
    scene bg_Phon
    "Глава 3: “Лебединый хаос“" with dissolve

    scene bg_Street
    Author "Светило по-настоящему летнее, яркое солнце."
    Author "Была прекрасная погода, поэтому Дима решил прогуляться."
    show ch_Dima at right with move
    show ch_Dima at center with easeinleft
    Author "Но вдруг из-за угла на него выбежала стая лебедей."
    show ch_Swan at right with hpunch
    Author "В своих миленьких клювиках они держали перочинные ножи, а к их шеям была привязана записка от Залы Стадионовны."
    Author "В записке было “Я знаю, что ты целыми днями сидишь за компьютером. Я переживаю за тебя и за твою больную спинку, нам нужно заняться ссс…"
    Author "спортом."
    Author "Дима в шоке, потрясен,  шокирован,  в ужасе. Я килькА?"
    Dima "Зала Стадионовна, конечно, ужас, но я не умру на ее глазах. Я буду жить!!!"
    scene bg_Stadium
    Author "Дима выбегает на стадион."
    show ch_Dima at left with moveinleft
    Dima "Ух-ах-эх-ох."
    show ch_Unknown at center with dissolve
    Author "Там его в безумно-пафосной позе ожидает темный силуэт и рядом  могучая кучка лебедей." 
    Author "Когда Дима подходит ближе, черты таинственной личности проявляются."
    Author "Но вдруг его стопа подворачивается. Он теряет равновесие и падает перед величественной личностью."
    hide ch_Dima with moveoutbottom
    Misli "Это она - моя богиня! Зала Стадионовна!"
    hide ch_Unknown
    show ch_Physical at center 
    with dissolve
    Misli "Как я люблю ее мягкие булочки, которые она печет в своей жаркой духовке!"
    Misli "Кто бы мог подумать, что преподаватель физкультуры увлекается кулинарией. Надеюсь, она научит меня жарить кокет…ой! Котлетки!"
    show ch_Dima at left with easeinbottom
    Dima "Я пришел к Вам, чтобы доказать, что киберспорт - это тоже спорт!"
    Physical "Ну раз ты так уверен в своих силах, начнем с чего-нибудь посложнее."
    menu:
        Physical "Раз ты сам ко мне явился, я дам тебе право выбрать свое первое задание."

        "Прыгнуть с вышки рядом со стадионом с парашютом в круг из лебедей.":
            scene bg_Tower
            Author "Из широких штанин он достает свой среднестатистический парашют."
            Author "Берет всю свою храбрость в кулак и поднимается на вышку."
            Author "С высоты вышки открывается шикарный вид на Мурмянск. Но этот вид не поможет ему достичь своей цели, ведь для этого ему нужно сделать шаг вперед."
            Author "Дима прыгает бомбочкой с вышки. Но он не знал как прыгать с парашютом."
            show ch_Dima at top with moveintop 
            hide ch_Dima with moveoutbottom  
            Dima "ААААААААААСПАСИТЕПОМОГИТЕУМИРАЮ"
            Physical "Давай, давай, ты сможешь! В ТикиТаке точно в реки залетит."
            Author "За секунду до непоправимого его своими крыльями подхватили лебеди, стоявшие в кругу. Благодаря этому он смог выжить."
            scene bg_Stadium
            show ch_Dima at center with easeinbottom 
            Author "Дима встает на ноги, отряхивается."
            Dima "ЕЩЕ СЕКУНДА И Я БЫ УМЕР! ВЫ ЧТО, НЕ МОГЛИ МЕНЯ РАНЬШЕ ПОДХВАТИТЬ?!?!?!?! ОШИБКА ЭВОЛЮЦИИ!!!"
            show ch_Dima at left with easeinleft
            show ch_Swan at center with dissolve
            Author "Лебеди искоса посмотрели на Диму, держа в клювиках перочинные ножички"
            Thounght_swan "Он слишком жалок, чтобы убивать его."
            Swan "Га-га-га  га-га-га"
            Dima "Шо вы гагочите? Я ничего не понимаю."
            hide ch_Swan with easeouttop
            show ch_Physical at center with easeinright
            Physical "Они поздравляют тебя с прохождением задания! :)"

        "Метание лебедем на дальнюю дистанцию.":
            Author "Что, вы правда выбрали этот вариант?! Нас же за это забанит GreenPeace! Мы не хотим проблем, поэтому продолжение вы сможете увидеть в нашем Телеграмм - канале @LebeDay"
    Physical "Молодец, Дима, так держать!"
    Physical "Ты справился с первым заданием!"
    menu:
        Physical "Приступаем к следующему испытанию. Без права выбора ты как женщина из XVII века."

        "Перетягивание каната":
            Physical "Что ж, тебе придется состязаться в этом с моей замечательной любимой младшей дочуркой, которую я ласково называю Гантелька."
            show ch_Barbell at right with hpunch 
            Author "Выходит Гантелька"
            Dima "ОГООООО, ничего себе ГАНТЕЛЬКА, это же целый шкаф!"
            Physical "В качестве каната вы будете использовать лебединую цепь. Не переживай, они крепкие, не порвутся. Можешь использовать всю свою силу."
            Dima "Пффф, изи"
            scene bg_FightBarbell
            Author "Начинается битва мощнейших:"
            Author "C одной стороны Дима с чакрой в ногах, а с другой - Гантелька Стадионовна."
            Author "Сначала они идут на равных, но Гантелька перехватывает инициативу, и Дима оказывается в шаге от проигрыша."
            Author "Лебеди, видя то, что Дима проигрывает, решают вступить в этот бой вместе с ним."
            
            Author "Они начинают лететь в его сторону, помогая ему победить."
            Author "Гантелька расплакалась и, содрогая землю, побежала домой."
            scene bg_Stadium with hpunch
            show ch_Dima at left with easeinbottom
            Dima "Ура, победа!"
            show ch_Physical at right with easeinright

        "Растяжка по-Стадионовски":
            Physical "Теперь тебе придется преодолеть не только свои возможности, но и законы природы."
            Physical "Ты должен будешь одной рукой коснуться ледокола “Ленин”, а другой - клавиши Enter на своей клавиатуре."
            Dima "Что?! Вы сошли с ума? "
            Author "Но подумав, Дима решил использовать свой опыт геймера."
            scene bg_Lenin with dissolve
            show ch_Dima at center with easeinleft
            Author "Он снял с клавиатуры клавишу Enter и пошел вместе с ней к ледоколу “Ленин”."
            Author "Так он выполнил второе задание Залы Стадионовны!"
            scene bg_Stadium with dissolve
            show ch_Dima at left with easeinbottom
            Dima "Ура, победа!"
            show ch_Physical at right with easeinright
    Physical "Ну ладно, так уж и быть, зачту."
    Dima "Ну что, на этом всё?"
    Physical "Ха-ха, глупенький, ты думал, что два простейших задания и на этом всё? Нет! Тебя ждет финальная битва с лебедями."
    Physical "Ты должен победить их в честном бою."
    menu:
        Dima "И как же мне это сделать?"

        "Сражаться насмерть":
            scene bg_FightSwan
            Author "Дима вступает в неистовую схватку с лебедями: первому он сворачивает шею, второму - отрывает лапки, третьему - выбивает зубки, а на четвертого накидывает наушники с песней Бузовой."
            Author "Дима оказывается среди кровавого месива лебедей."
            scene bg_Stadium
            show ch_Physical at right with moveinright
            Physical "*зловеще* ХАХАХА."
            Physical "Я давно хотела от них избавиться!"
            show ch_DimaBlood at left with moveinleft
            Physical "Спасибо тебе!"
            Physical "Держи свой зачёт!"
            jump EndChapter_3

        "Устроить переговоры":
            $ carma += 1
            show ch_Swan at center with easeintop
            Author "Дима встает перед лебедями. Встает перед ними на колени и кланяется."
            Dima "Многоуважаемые лебеди, хотел бы предложить вам мирное урегулирование конфликта."
            Dima "Я готов предоставить вам годовое обеспечение хлебных крошек. Вы согласны?)"
            Thounght_swan "Нам кажется, или он нас обманывает?! Ладно, поверим ему."
            Swan "Га-га-га-га-га"
            Dima "Без б."
            Physical "Интересно где ты возьмешь сколько хлебных крошек ахахах, но ладно давай свою зачетку!"
            jump EndChapter_3

        "Попытаться сбежать":
            hide ch_Dima with moveoutright
            hide ch_Physical 
            Author "Дима, не думая ни секунды, бежит к выходу из стадиона."
            Author "Но вдруг понимает, что теперь агрессия лебедей направлена не в его сторону, а на Залу Стадионовну."
            show ch_Dima at right with easeinleft
            Author "Тут он понимает, что не может бросить ее в такой ситуации, и, собрав всю волю в кулак,  вступает с ними в бой."
            show ch_Dima at left with easeinright
            Dima "Не трогайте ее! Ваш противник - это я."
            show ch_Physical at right with easeinbottom
            Physical "Дима, я всегда ждала героя, как ты."
            Author "Дима одним ударом выносит всех лебедей и бросается навстречу Зале Стадионовне."
            show ch_Dima at center with easeinright
            Author "Они целуются и уезжают в закат."
            Author "И жили они долго и счастливо!"
    return
   
    