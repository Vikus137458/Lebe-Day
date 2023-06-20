# Вступление: “Начало конца?!“

# Персонажы: 
#   Dima
#   Author
#   Unknown
#   Curator
#   Slava
#   Pasha
#   Ilya
#   Misha
#   'Карина из - под кровати Ильи'
#   'Голубь на карнизе за окном'
#   'Даша с шестого этажа'

# Спрайты персонажей:
#   ch_Dima
#   ch_Unknown
#   ch_Curator
#   ch_Slava
#   ch_Pasha
#   ch_Ilya
#   ch_Misha

# Локации:
#   bg_Room66


label Introduction:
    "“Начало конца?!“" with dissolve

    scene bg_Room66
    Author "Дима играет в игру"
    Author "*Звонок с незнакомого номера*"
    show ch_Unknown at right
    with dissolve
    Unknown "Дима, привет!"
    show ch_Dima at left
    with dissolve
    Dima "Кто это!"
    Unknown "Это твой куратор, Наталья Станиславовна."
    hide ch_Unknown
    show ch_Curator at right
    with dissolve 
    Curator "У меня для тебя печальная новость, в связи с объединением вузов, деканат решил, что нам не нужны такие бездарные ученики как ты, поэтому если в течение недели ты не закроешь все долги, тебя вышвырнут из универа." 
    Curator "Пока)"
    hide ch_Curator with dissolve
    Author "*Бип бип бип*"
    Author "Дима продолжает играть"
    hide ch_Dima with dissolve
    Author "На следующий день"
    Author "Дима неожиданно проснулся от кошмара, ему приснилось, что его хотят отчислить"
    show ch_Dima with zoomin
    Dima "АААААААААААААААААААААААААААА!!!"
    Dima "Слава Богу! Это был просто кошмар!"
    Author "Слава врывается в комнату"
    show ch_Dima at left with easeinleft
    show ch_Slava at right
    Slava "Звал меня?!"
    hide ch_Slava
    show ch_Dima at center with move
    Author "Дима вздыхает"
    Dima "Эхх..."
    Dima "Каждый день одно и то же."
    Dima "Доброе утро!"
    show ch_Slava at right
    Slava "Доброе утро!"
    show ch_Pasha at left
    Pasha "Доброе утро!"
    hide ch_Slava
    show ch_Ilya at right
    Ilya "Доброе утро!"
    hide ch_Pasha
    show ch_Misha at left
    Misha "Доброе утро!"
    Character('Карина из - под кровати Ильи', color="#76e2e4") "Доброе утро!"
    Character('Голубь на карнизе за окном', color="#76e2e4") "Доброе утро!"
    Character('Даша с шестого этажа', color="#76e2e4") "За****ли! Утро добрым не бывает!"
    hide ch_Ilya
    hide ch_Misha
    Author "Ребята встали, собрались и побежали на зарядку."
    Author "Каждый день они бегали по квартирам и предлагали свои услуги. Так они отрабатывали свой долг."
    Author "Спустя время ребята возвращаются домой."
    Author "Дима решает заглянуть в телефон и вдруг неожиданно для себя и его друзей обнаруживает, что на самом деле его кошмар, не такой уж и кошмар, а реальность."
    Author "Дима в шоке, что же он будет делать дальше?"
    return