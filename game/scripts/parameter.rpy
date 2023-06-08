
label GG_character_update:
    $ GG_Health[0] = GG_Health[1]
    $ GG_Stamina[0] = GG_Stamina[1]
    $ GG_Infection[0] = 0
    return

label GG_character_update_forest:
    $ GG_Health[0] = GG_Health[1]
    $ GG_Stamina[0] = GG_Stamina[1]
    $ GG_Infection[0] = 0
    return

label GG_character:

    default GG_Level = [1, 10, 0, 4, 0]
    #1 Уровень гг / 2 Max кол-во опыта для поднятия уровня / 3 Текущее кол-во опыта / 4 Очко доступное при достижение нового уровня / 5 Множитель получаемого опыта(зависит от интелекта)

    default GG_Strength = [0, 5, 0, 0]
    default GG_Agility = [0,5,0, 0]
    default GG_Intellect = [0,5,0, 0]
    default GG_Luck = [0,5,0, 0]
    #1 Текущий уровень навыка / 2 Сколько нужно очков для его поднятия(увеличивается на 5) / 3 сколько сейчас у игрока / 4 в сумме сколько

    default GG_Health = [100, 100]
    default GG_Stamina = [50, 50]
    default GG_Infection = [0, 100]
    #1 Текущее кол-во здоровья / выносливости / заражения игрока
    #2 Max кол-во здоровья / выносливости / заражения игрока


    default GG_Damage = 10
    default GG_Defense = 0
    #1 сила игрока / 2 защита игрока

    default GG_Inventory_Items = [0,0,0,0]
    # 1 кол-во еды / 2 кол-во медикаментов / 3 кол-во материалов / 4 топливо / 5 вес?
    default GG_character_bool = False
    default GG_forest_visited = False

    #Расходники
    default lockpick = 5
    default lockpick_nobroke_chance = 0

    default loot_find_chance = 0

    # Навыки которыми влаждеет гг
    default GG_forest_book_read = False
    default GG_city_lockpick = False

screen healthbar:
    zorder 10
    bar:
        xsize 300  ysize 40
        xpos 140   ypos 800
        value AnimatedValue(value = GG_Health[0], range = GG_Health[1], delay = 1)
        left_bar Frame("gui/bar/left_healthbar.png", 10,10)
        right_bar Frame("gui/bar/right_healthbar.png",10,10)
    text "{size=30}{color=#000000}[GG_Health[0]] / [GG_Health[1]] {/color}{/size}" xpos 220 ypos 800

screen healthbar_balle:
    zorder 10
    bar:
        xsize 300  ysize 40
        xpos 100   ypos 800
        value AnimatedValue(value = GG_Health[0], range = GG_Health[1], delay = 1)
        left_bar Frame("gui/bar/left_healthbar.png", 10,10)
        right_bar Frame("gui/bar/right_healthbar.png",10,10)
    text "{size=30}{color=#000000}[GG_Health[0]] / [GG_Health[1]] {/color}{/size}" xpos 200 ypos 800


screen staminabar:
    zorder 10
    bar:
        xsize 300  ysize 40
        xpos 140   ypos 850
        value AnimatedValue(value = GG_Stamina[0], range = GG_Stamina[1], delay = 1)
        left_bar Frame("gui/bar/left_staminabar.png", 10,10)
        right_bar Frame("gui/bar/right_staminabar.png",10,10)
    text "{size=30}{color=#000000}[GG_Stamina[0]] / [GG_Stamina[1]] {/color}{/size}" xpos 220 ypos 850

screen staminabar_2:
    bar:
        xsize 300  ysize 40
        xpos 30 ypos 50
        value AnimatedValue(value = GG_Stamina[0], range = GG_Stamina[1], delay = 1)
        left_bar Frame("gui/bar/left_staminabar.png", 10,10)
        right_bar Frame("gui/bar/right_staminabar.png",10,10)
    text "{size=30}{color=#000000} [GG_Stamina[0]] / [GG_Stamina[1]] {/color}{/size}"  xpos 130 ypos 50

screen staminabar_battle:
    zorder 10
    bar:
        xsize 300  ysize 40
        xpos 100 ypos 850
        value AnimatedValue(value = GG_Stamina[0], range = GG_Stamina[1], delay = 1)
        left_bar Frame("gui/bar/left_staminabar.png", 10,10)
        right_bar Frame("gui/bar/right_staminabar.png",10,10)
    text "{size=30}{color=#000000} [GG_Stamina[0]] / [GG_Stamina[1]] {/color}{/size}"  xpos 200 ypos 850


screen infectionbar:
    zorder 10
    bar:
        xsize 300  ysize 40
        xpos 140   ypos 900
        value AnimatedValue(value = GG_Infection[0], range = GG_Infection[1], delay = 1)
        left_bar Frame("gui/bar/left_virusbar.png", 10,10)
        right_bar Frame("gui/bar/right_virusbar.png",10,10)
    text "{size=30}{color=#000000}[GG_Infection[0]] / [GG_Infection[1]] {/color}{/size}" xpos 220 ypos 900

screen infectionbar_battle:
    zorder 10
    bar:
        xsize 300  ysize 40
        xpos 100   ypos 900
        value AnimatedValue(value = GG_Infection[0], range = GG_Infection[1], delay = 1)
        left_bar Frame("gui/bar/left_virusbar.png", 10,10)
        right_bar Frame("gui/bar/right_virusbar.png",10,10)
    text "{size=30}{color=#000000}[GG_Infection[0]] / [GG_Infection[1]] {/color}{/size}" xpos 200 ypos 900


label GG_character_open:
    show screen healthbar
    show screen staminabar
    show screen infectionbar
    call screen GG_character_screen

label GG_character_close:
    hide screen healthbar
    hide screen staminabar
    hide screen infectionbar
    call screen school_hub

label GG_rest_outside:
    $ GG_Health[0] += (GG_Health[1]/10)
    $ GG_Stamina[0] += (GG_Stamina[1]/2)
    $ GG_Infection[0] -= (GG_Infection[1]/10)

    if GG_Stamina[0] > GG_Stamina[1]:
        $ GG_Stamina[0] = GG_Stamina[1]
    if GG_Health[0] > GG_Health[1]:
        $ GG_Health[0] = GG_Health[1]
    if GG_Infection[0] < 0:
        $ GG_Infection[0] = 0
    return

label GG_Death:
    hide screen healthbar_balle
    hide screen staminabar_battle
    hide screen infectionbar_battle
    hide screen zombie_bar

    if GG_Health[0] <= 0:
        "Вы исчерпали все свои жизни"
        "Вы мертвы"
        return
    elif GG_Infection[0] >= GG_Infection[1]:
        "В вашем теле слишком много вируса"
        "Не в силах его контролировать, вы обратились в зомби"
        "Вы мертвы"
        return

# Экран - Прокачка персонажа
screen GG_character_screen:
    imagemap:
        idle 'game_menu_2'
        text "{size=30}Доступно очков для прокачки: %s{/size}" % GG_Level[3] xpos 700 ypos 60
        vbox xpos 1500 ypos 100 spacing 10:
            text "Уровень: %s" % GG_Level[0]
            text "{size=20}Текущее количество опыта: %s {/size}" % GG_Level[2]
            text ""
            text "Ваши текущие \nхарактеристики"
            text "{size=20}Сила: %s{/size}" % GG_Damage
            text "{size=20}Зашита: %s{/size}" % GG_Defense
            text ""
            text "{size=20}Текщий параметр ''Сила'': %s{/size}" % GG_Strength[2]
            text "{size=20}Для подняния нужно: %s {/size}" % GG_Strength[1]
            text ""
            text "{size=20}Текщий параметр ''Ловкость'': %s{/size}" % GG_Agility[2]
            text "{size=20}Для подняния нужно: %s {/size}" % GG_Agility[1]
            text ""
            text "{size=20}Текщий параметр ''Интелект'': %s{/size}" % GG_Intellect[2]
            text "{size=20}Для подняния нужно: %s {/size}" % GG_Intellect[1]
            text ""
            text "{size=20}Текщий параметр ''Удача'': %s{/size}" % GG_Luck[2]
            text "{size=20}Для подняния нужно: %s {/size}" % GG_Luck[1]
        hbox xpos 640 ypos 150 spacing 60:
            text "Сила"
            text "Ловкость"
            text "Интелект"
            text "Удача"
        hbox xpos 670 ypos 350 spacing 180:
            text "%s" % GG_Strength[0]
            text "%s" % GG_Agility[0]
            text "%s" % GG_Intellect[0]
            text "%s" % GG_Luck[0]
    # Выход из прокачки
    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/backpack.webp', 100, 100)
            hover im.Scale('icon/backpack_hover.webp', 100, 100)
            action Jump('GG_character_close')
    # Прокачка навыков
    hbox xpos 630 ypos 250 spacing 100:
        imagebutton: # СИЛА
            idle im.Scale('icon/strong.webp', 100, 100)
            hover im.Scale('icon/strong_hover.webp', 100, 100)
            action Call('GG_Strength_label')
        imagebutton: # ЛОВКОСТЬ
            idle im.Scale('icon/acrobatic.webp', 100, 100)
            hover im.Scale('icon/acrobatic_hover.webp', 100, 100)
            action Call('GG_Agility_label')
        imagebutton: # ИНТЕЛЕКТ
            idle im.Scale('icon/brain.webp', 100, 100)
            hover im.Scale('icon/brain_hover.webp', 100, 100)
            action Call('GG_Intellect_label')
        imagebutton: # УДАЧА
            idle im.Scale('icon/star-struck.webp', 100, 100)
            hover im.Scale('icon/star-struck_hover.webp', 100, 100)
            action Call('GG_Luck_label')

label GG_Strength_label: # Прокачка навыка силы
    hide screen healthbar
    hide screen staminabar
    hide screen infectionbar
    show screen GG_character_screen
    "Навык сила"
    "Чем больше шкаф, тем громче падает."
    "Благодаря силе вы способны выдерживать и наносить больше урона. Увеличивает ваше max здоровье и силу атаки. "
    "Хотите прокачать?"
    menu Chose_skill_1:
        "Да":
            if GG_Level[3] >= 1 and GG_Strength[1] <= GG_Strength[2]:
                $ GG_Strength[0] += 1
                $ GG_Level[3] -= 1
                $ GG_Damage += 5
                $ GG_Health[1] += 10
                $ GG_Strength[1] += 5
            else:
                "Недостаточно очков для прокачки навыка"
            jump GG_character_open
        "Нет":
            jump GG_character_open

label GG_Agility_label: # Прокачка навыка ловкости
    hide screen healthbar
    hide screen staminabar
    hide screen infectionbar
    show screen GG_character_screen
    "Навык ловкость"
    "Рожденный бегать пизды не получит."
    "Выносливость не раз спасала жизнь людей, которые попали в неприятности.
    Увеличивает вашу max выносливость, а так же шанс уворота в битве. "
    "Хотите прокачать?"
    menu Chose_skill_2:
        "Да":
            if GG_Level[3] >= 1 and GG_Agility[1] <= GG_Agility[2]:
                $ GG_Agility[0] += 1
                $ GG_Level[3] -= 1
                $ GG_Stamina[1] += 10
                $ GG_Agility[1] += 5
            else:
                "Недостаточно очков для прокачки навыка"
            jump GG_character_open
        "Нет":
            jump GG_character_open

label GG_Intellect_label: # Прокачка навыка интелект
    hide screen healthbar
    hide screen staminabar
    hide screen infectionbar
    show screen GG_character_screen
    "Навык интеллект"
    "Знания — это сила, а сила есть ума не надо."
    "Интеллект важный навык. Без него мы бы … о чем это я? Увеличивает получаемый опыт c врагов. Так же может повлиять во время диалогов. "
    "Хотите прокачать?"
    menu Chose_skill_3:
        "Да":
            if GG_Level[3] >= 1 and GG_Intellect[1] <= GG_Intellect[2]:
                $ GG_Intellect[0] += 1
                $ GG_Level[3] -= 1
                $ GG_Intellect[1] += 5
            else:
                "Недостаточно очков для прокачки навыка"
            jump GG_character_open
        "Нет":
            jump GG_character_open

label GG_Luck_label: # Прокачка навыка удача
    hide screen healthbar
    hide screen staminabar
    hide screen infectionbar
    show screen GG_character_screen
    "Навык удача"
    "I smell pennies."
    "Быть сильным и ловким конечно поможет вам во время выживания, но ничто не спасет вас от кирпича который случайно может упасть на вас с неба.
    Увеличивает шанс выпадения большего количества лута. Меньше шанс поломки отмычек."
    "Хотите прокачать?"
    menu Chose_skill_4:
        "Да":
            if GG_Level[3] >= 1 and GG_Luck[1] <= GG_Luck[2]:
                $ GG_Luck[0] += 1
                $ GG_Level[3] -= 1
                $ GG_Luck[1] += 5
                $ loot_find_chance += 1
                $ lockpick_nobroke_chance += 0.5
            else:
                "Недостаточно очков для прокачки навыка"
            jump GG_character_open
        "Нет":
            jump GG_character_open

label GG_Skill_update_strength:
    $ GG_Damage += GG_Strength[2] * 0.1
    $ GG_Health[1] += GG_Strength[2] * 0.2
    return

label GG_Skill_update_agility:
    $ GG_Stamina[1] += GG_Agility[2] * 0.2
    return

label GG_Skill_update_intellect:
    $ GG_Level[4] += GG_Intellect[2] * 0.1
    return

label GG_Skill_update_luck:
    $ loot_find_chance += GG_Luck[2] * 0.1
    return













# так для
