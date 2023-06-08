
# Противники
                    # 1min 2 текущее 3max  - здоровье / 4 - броня / 5 и 6 - урон(диапазон) / 7 - выпадаемый опыт
define enemy_1 = [          0, 50, 50,                      1,          3, 8,                   5]

# вывод хп врага
screen zombie_bar:
    zorder 10
    bar:
        xsize 300  ysize 40
        xpos 1200   ypos 150
        value AnimatedValue(value = enemy_1[1], range = enemy_1[2], delay = 1)
        left_bar Frame("gui/bar/left_healthbar.png", 10,10)
        right_bar Frame("gui/bar/right_healthbar.png",10,10)
    text "{size=30}{color=#000000}[enemy_1[1]] / [enemy_1[2]] {/color}{/size}" xpos 1200 ypos 150

# Экран битвы
screen battle_screen:
    imagemap:
        idle 'b_stand'
        add im.Scale('gui/frame_2.webp', 600, 200) xpos 1200 ypos 800
        #add im.Scale('gui/frame_2.webp', 400, 200) xpos 100 ypos 800

    imagebutton:
        idle im.Scale('icon/saber-slash.png', 100, 100) xpos 1400 ypos 850
        hover im.Scale('icon/saber-slash _hover.png', 100, 100)
        action Jump('gg_attack_1')
    imagebutton:
        idle im.Scale('icon/shield.png', 100, 100) xpos 1500 ypos 850
        hover im.Scale('icon/shield_hover.png', 100, 100)
        action Jump('gg_defense')



label battle_label:
    "Приготовтесь к бою"
    show screen healthbar_balle
    show screen staminabar_battle
    show screen infectionbar_battle
    show screen zombie_bar

    hide screen back_data
    hide screen staminabar_2
    call screen battle_screen

label gg_attack:
    play sound "audio/light_punch.wav" volume 0.25
    scene b_attack
    pause 0.3
    $ enemy_1[1] -= GG_Damage - enemy_1[3]
    $ GG_Stamina[0] -= 10
    if GG_Stamina[0] <= 0:
        $ GG_Stamina[0] = 0
    if enemy_1[1] <= enemy_1[0]:
        hide screen healthbar_balle
        hide screen staminabar_battle
        hide screen infectionbar_battle
        hide screen zombie_bar
        "Враг побежден"
        "Получено [enemy_1[5]] опыта"
        $ enemy_1[1] = enemy_1[2]
        call screen city_hub

    jump zombie_attack

label gg_attack_1:
    if GG_Stamina [0] <= 0:
        hide screen healthbar_balle
        hide screen staminabar_battle
        hide screen infectionbar_battle
        hide screen zombie_bar
        scene b_stand
        "Недостаточно выносливости"
        show screen healthbar_balle
        show screen staminabar_battle
        show screen infectionbar_battle
        show screen zombie_bar
        call screen battle_screen
    else:
        jump gg_attack

label gg_defense:
    scene b_block
    pause 0.3
    $ GG_Stamina[0] += 25
    if GG_Stamina[0] >= GG_Stamina[1]:
        $ GG_Stamina[0] = GG_Stamina[1]
    $ GG_Defense += 3
    jump zombie_attack

label zombie_attack:
    $ tmp_attack = renpy.random.randint(enemy_1[4], enemy_1[5])
    # если урон который наносит враг меньше брони игрока, то игрок получает 0 урона. Чтобы игрок не хилился
    if tmp_attack <= GG_Defense:
        $ tmp_attack = 0
    else:
        $ tmp_attack -= GG_Defense
        $ GG_Health[0] -= tmp_attack

    $ GG_Infection[0] += renpy.random.randint(1,10)
    if GG_Infection[0] >= GG_Infection[1] or GG_Health[0] <= 0:
        jump GG_Death
    $ GG_Defense -= 3
    call screen battle_screen





#mesto
