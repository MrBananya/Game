
# задание 1 2 3 и т.д
# 0 - задание не активно. 1 - задание находится в процессе выполнения(активо). 2 - задание выполнено.

default tasks = [
        {"code_name": "+2 или -2?",             "description": "Задание: Нужно найти очки для одной девочки",   "state": 0},
        {"code_name": "Ты не ешь грибы?",       "description": "Задание: Узнать больше о лесных растениях. Возможно в библиотеке будет книга об этом.",  "state": 0},
        {"code_name": "А где моя книга?",         "description": "Задание: Верните книгу в библиотеку",           "state": 1},
        {"code_name": "Сезам откройся",         "description": "Задание: Найти способ открыт запертый сейф",           "state": 0}
    ]

# Так для
#python:
#    for task in tasks:
#        task["state"] = 1


# ______________________________________________ Закрытие открытия доски заданий
label tasks_label_open:
    scene darkscreen
    call screen tasks_screen

label tasks_label_close:
    call screen school_hub


# ______________________________________________ Сама доска заданий
screen tasks_screen:
    imagemap:
        idle 'game_menu_2'
        text "{size=30}Ваш текущий список заданий{/size}" xpos 700 ypos 60
    vbox xalign 0.03 yalign 0.05 spacing 5:
        for task in tasks:
            if task["state"] == 1: # Если задание не выполнено
                text "{color=#918c6a}{size=24}%s {/size}{/color}" %task['code_name'] xpos 300 ypos 100
                text "{color=#b5a748}{size=20}%s (в процессе выполнения){/size}{/color}" %task['description'] xpos 300 ypos 100
            if task["state"] == 2: # Если задание не выполнено
                text "{size=20}{s} %s {/s} - задание выполнено {/size}" % (task['description']) xpos 300 ypos 100

    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/checklist.webp', 100, 100)
            hover im.Scale('icon/checklist_hover.webp', 100, 100)
            action Jump('tasks_label_close')


# ______________________________________________ Взаимодействие с нпс в качалке
# Рандомный чел в качалке утром
label talk_gym_1:
    scene gym_1
    Ch1 "♂️ Fuck you ♂️"
    call screen Gym_screen

# Разговор с Изамой по поводу прокачки персонажа утром
label talk_gym_2:
    scene gym_1_talk_2
    MCh1 "Ты что-то хотел?"
    scene gym_1_talk_1
    menu gym_job:
        "Хочу прокачать силу":
            scene gym_job_1 with fade
            pause 1
            scene gym_job_2 with dissolve
            pause 1
            scene gym_job_3 with dissolve
            "Тренировка силы прошла успешно"
            $ GG_Strength[2] += 1
            $ Hours += 4
            call GG_Skill_update_strength
            call screen Gym_screen
        "Хочу прокачать ловкость":
            scene gym_job_4 with fade
            pause
            "Тренировка ловкости прошла успешно"
            $ GG_Agility[2] += 1
            $ Hours += 4
            call GG_Skill_update_agility
            call screen Gym_screen
        "Пока ничего":
            call screen Gym_screen

# попытка разговора с Акане вечером
label talk_gym_3:
    scene gym_2
    "Не думаю что она сейчас будет разговаривать"
    call screen Gym_screen




# ______________________________________________ Взаимодействие с нпс в библиотеке
# Разговор с Касуми в библиотеке утром
label talk_library_1:
    if Hours >= 6 and Hours < 16:
        scene library_1_talk_1
        pause 1
        scene library_1_talk_2 with dissolve
        scene library_1_talk_3
        FCh6 "Ты что-то хотел?"
        scene library_1_talk_2
        menu library_job:
            "Прокачать свой интелект":
                scene library_job_1 with fade
                pause 1
                "Тренировка интелекта прошла успешно"
                $ GG_Intellect[2] += 1
                $ Hours += 4
                call GG_Skill_update_intellect
                call screen Library_screen
            "Поговорить":
                # Задание с получением книги для сбора ягод и растений
                if GG_forest_visited == True and tasks[1]['state'] == 1:
                    GG "У тебя есть какая-нибудь книга о растениях?"
                    scene library_1_talk_3
                    FCh6 "Да, я могу дать тебе парочку"
                    scene library_1_talk_2
                    GG "Спасибо"
                    $ tasks[1]['state'] = 2
                    $ GG_forest_book_read = True
                    call screen Library_screen
                GG "Да так, пока ничего"
                call screen Library_screen
    if Hours >= 16 and Hours < 20:
        scene library_2
        "Кажется она сейчас занята"
        call screen Library_screen



# Кинуть взглядом Хикару утром
label talk_library_2:
    scene library_1
    "Кажется Хикару сейчас спит. Не красиво будет его будить."
    call screen Library_screen


# ______________________________________________ Взаимодействие с нпс в главном оффисе
label talk_main_office_1:
    if Hours >= 6 and Hours < 16:
            scene main_office_1_talk_1
            pause 1
            scene main_office_1_talk_2 with dissolve
            scene main_office_1_talk_3
            MCh3 "Что такое?"
            scene main_office_1_talk_2
    if Hours >= 16 and Hours < 20:
            scene main_office_2_talk_1
            pause 1
            scene main_office_2_talk_2 with dissolve
            scene main_office_2_talk_3
            MCh3 "Что такое?"
            scene main_office_2_talk_2

    menu main_office_job:
        "Что ты хотел?"
        "Посмотреть что можно улучшить / построить":
            call screen build_update_screen
        "Хочу спросить совета":
            call screen Main_office_screen
        "Ничего":
            call screen Main_office_screen
    call screen Main_office_screen


label talk_main_office_3:
    scene main_office_2_2_talk_1
    pause 1
    scene main_office_2_2_talk_2 with dissolve
    pause 1
    scene main_office_2_2_talk_4 with dissolve
    FCh1 "Что такое?"
    scene main_office_2_2_talk_3
    menu main_office_job_3:
        "Что ты хотел?"
        "Хочу спросить совета":
            call screen Main_office_screen
        "Ничего":
            call screen Main_office_screen
    call screen Main_office_screen

# ______________________________________________ Комната отдыха
label talk_restroom_1:

    if Hours >= 6 and Hours < 16:
        if Totaly_Days >= 1 and tasks[0]['state'] == 0: # Получение первого задания
            scene task_1_talk_1 with fade
            GG "Привет Чика. Что-то случилось?"
            scene task_1_talk_4 with dissolve
            FCh3 "Привет Казума"
            scene task_1_talk_5 with dissolve
            FCh3 "Да, есть небольная проблема"
            FCh3 "У одной девочки есть проблемы со зрением"
            FCh3 "По ее словам ей должны были сделать на неделе новые очки, но ты сам знаешь что случилось потом"
            FCh3 "Не мог бы ты зайти в одно место, я тебе дам адрес?"
            scene task_1_talk_2
            GG "Да конечно, попробую что-нибудь узнать"
            scene task_1_talk_4
            FCh3 "Спасибо большое"
            "Добавлено новое задание"
            $ tasks[0]['state'] = 1
            call screen restroom_screen
        scene restroom_1
        "Кажется Чика сейчас занята"
        call screen restroom_screen
    if Hours >= 16 and Hours < 20:
        scene restroom_2
        "Кажется Чика сейчас занята"
        call screen restroom_screen

label talk_restroom_2:
    "Не сейчас"
    call screen restroom_screen

label talk_restroom_3:
    if Hours >= 6 and Hours < 16:
        scene restroom_1
        Ch2 "Ты что совсем играть не умеешь?"
        Ch2_1 "Ходи лошадью! Лошадью ходи, дурак!"
        call screen restroom_screen
    if Hours >= 16 and Hours < 20:
        scene restroom_2
        Ch3 "Ты будешь переводить или подкидывать?"
        Ch3_1 "Погоди, я думаю"
        pause 2
        Ch3 "В следующий раз я раздаю"
        call screen restroom_screen
# ______________________________________________ Задания
# 1 Задание
label Task_1:
    menu otladka:
        "поменять задание 1 на"
        "Choice 1":
            python:
                for task in tasks:
                    task["state"] = 1
        "Choice 2":
            python:
                for task in tasks:
                    task["state"] = 2
    call screen school_hub
