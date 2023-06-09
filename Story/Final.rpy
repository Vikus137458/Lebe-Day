# Финал: “Счастье близко…“

# Персонажы:
#   Author
#   Dima
#   Dean
#   Curator

# Спрайты персонажей:
#   ch_Dima
#   ch_Dean
#   ch_Curator

# Локации:
#   bg_Phon
#   bg_UniverEntry 
#   bg_CabinetDean
#   bg_Happy_end
#   bg_Lost_end

label Final:
    scene bg_Phon
    Author "Финал: “Счастье близко…“" with dissolve

    scene bg_UniverEntry
    Author "Вход в университет"
    Author "Дима наконец-то закрыл все долги у отправился на встречу с деканом."
    scene bg_CabinetDean
    Author "Кабинет Декана"
    Author "Он постучал в дверь и ему открыла женщина." #стук в дверь
    Author "Сначала он подумал, что перед ним снизошел ангел, но вскоре об убедился в обратном."
    show ch_Dima at left with dissolve
    Dima "Здравствуйте, я ищу Декана факультета, не знаете где его носит?"
    show ch_Dean at right with hpunch
    Dean "Ну конечно я знаю его, ОН - ЭТО Я!"
    Author "Дима занервничал и понял, что если ты уверен, что что-то пойдёт не так, так оно и будет."
    Dean "Ладно, не будем о грустном. Говори зачем пришел."
    Dima "Я закрыл все долги, поэтому не выгоняйте меня пожалуйста, мне негде жить, вы моя последняя надежда."
    Dima "Я в разводе, а еще у меня шестеро детей, которым нужно платить алименты."
    Dean "Хахахаха, чего ты так испугался? Раз все закрыл, то конечно никуда не выгоним."
    Dean "Подскажи ка мне свою фамилию, отмечу тебя в списке."
    Dima "Лебедев, Дмитрий Лебедев!"
    show ch_Dean at right with hpunch
    Dean "ЧТО? ЛЕБЕДЕВ!!!!"
    Dean "Тот самый, у кого 100%% непосещаемость! Как ты смог закрыть все долги в такой короткий срок!"
    Dean "Что за чушь? Черная магия! Колдун е***ий!!!"
    Dima "Нет, Вы не правы! Я добился всего честным путем!"
    Dean "Мне плевать! Я щас сяду за стол, а ты вылетишь отсюда!"
    Dima "НЕЕЕЕЕЕЕТ!"
    Author "Тут неожиданно для всех участников этой картины, в дверь с ноги врывается Куратор."
    show ch_Curator with hpunch
    Curator "Оружие на пол! Руки за голову! Всем лежать! Морды в пол!"
    Dima "О моя спасительница! Вы пришли за мной?"
    Curator "Ой, как неловко получилось то. Я видимо кабинетом ошиблась. ХЕ."
    Dima "Помогите! Прошу, не бросайте меня!"
    if carma > 3:
        Curator "Хорошо, я знаю, что ты следовал моей просьбе, оставаться человеком до конца, поэтому я помогу тебе!"
        Dima "Ладно, мне кажется, я смогу тебе верить... немного..."
        Curator "Не верь никому…"
        show ch_Curator at left with easeinleft
        hide ch_Dima
        Dean "Не важно кто будет на его стороне, это ему не поможет!"
        Curator "Ошибаешься, я спасу его!"
        Curator "Скажи, почему ты так хочешь его отчислить?!"
        Dean "Я ненавижу зачетки. У меня начинает болеть голова, когда я вспоминаю, как мне тыкали ими в затылок."
        Dean "Я ненавижу студентов. Особенно тех, которые отключают свой мозг и тупо подчиняются приказам."
        Dean "От них несёт хуже, чем от разлагающихся трупов."
        Dean "Отца переполняет печаль от потери своего ребёнка в университете, а через год он заводит нового со словами:"
        Dean "«Я выращу из него дипломника». Скажи, разве не идиот?"
        Dean "Я ненавижу людей. Мысль, что я из того же вида, удручает меня."
        Curator "Ты сказала, что ненавидишь людей, что люди не меняются, но это не правда."
        Curator "Люди тоже могут сильно измениться, но порой не в лучшую сторону. Ты этому отличный пример…"
        Dean "Ты хоть знаешь, что если абсолютно нормальному человеку дать в руки зачетку, он может такое натворить..."
        Dean "Причём он даже не поймёт, что его на это толкнуло. Такая вот в ней дьявольская сила."
        Curator "И что? Имеет значение лишь то, ради чего ты ее берешь."
        Dean "Ха, а ты играешь со мной на равных, что ж, тогда скажи, как считаешь, у кого больше всего заслуг по закрытию долгов твоего подопечного?"
        Curator "У Димы?!"
        Dean "Увы, это не так, 60%% всех заслуг находится в руках у преподавателей. Каждый второй хотел ему помочь."
        Dean "Еще 37%% — это Ты. Да у вас тут заговоры на каждом углу."
        Curator "Да, есть такое. На этом и строится наш мир. Хахахаха!"
        Dean "Боже, да что же с тобой делать…"
        Dean "Думаю, я все же не смогу выиграть. Как жаль.."
        Curator "Yes! Я всегда в себя верила!"
        Dean "Ей ты, юродивый, подойди и распишись в документах. Так и быть оставлю тебя до следующей сессии."
        Dima "Урааааа! Я смог!!!"
        Dean "Не зазнавайся, просто тебе повезло с куратором."
        scene bg_Happy_end with dissolve
        Author "В конце своего приключения Дима наконец-то обрел покой (от него все отстали) и он отправился в свой рай…"
        Author "В Мак"
    else:
        Curator "Прости, но ты не сдержал своего обещания и перешел на темную сторону. Я не хочу тебе помогать."
        Dima "Что… Почему… Зачем… Как….Вы не можете со мной так поступить. Я же ваш любимчик!"
        Curator "ЧТО? С чего ты взял? Мой любимчик - Алияр. У него 150%% пропусков, Он намного круче тебя."
        Dean "Ха-ха-ха-ха-ха! Даже твой куратор не хочет тебе помочь. Ты просто нулевый чел."
        Dima "НЕЕЕЕЕЕТ!!!"
        scene bg_Lost_end
        Author "Как бы нам не хотелось помочь Диме, он не справился с этим испытанием. За все в этой жизни нужно платить."
        Author "На следующий день Дима собрал свои вещи и покинул общежитие. После этого его никто не видел."
    return
