screen city_map_2:
    imagemap:

        add im.Scale('gui/frame_2.webp', 800, 50) xpos 600 ypos 0
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        text "{color=#ffffff}[Days] день {/color} " xpos 1600 ypos 10
        text "{color=#ffffff} %s {/color}" % WeekDays[WeekDayNumber] xpos 1600 ypos 44
        text "{color=#ffffff}[Hours]:[MinutesStr]{/color}" xpos 1800 ypos 10

        add im.Scale('icon/opened-food-can.webp', 45, 45) xpos 610 ypos 0
        text "{size=20}{color=#ffffff}: %i {/color}{/size}" %GG_Inventory_Items[0] xpos 660 ypos 10
        add im.Scale('icon/medical-pack-alt.webp', 45, 45) xpos 750 ypos 0
        text "{size=20}{color=#ffffff}: [GG_Inventory_Items[1]] {/color}{/size}" xpos 800 ypos 10
        add im.Scale('icon/half-log.webp', 45, 45) xpos 870 ypos 0
        text "{size=20}{color=#ffffff}: [GG_Inventory_Items[2]] {/color}{/size}" xpos 920 ypos 10

        if Hours >= 6 and Hours < 16:
            idle 'city_1_map_1'
            hover 'city_1_map_1_hover'
            hotspot (655, 167, 294, 368) action Jump('city_wait')
            hotspot (998, 240, 257, 302) action Jump('city_wait')
            hotspot (644, 556, 278, 251) action Jump('city_wait')
            hotspot (997, 553, 318, 253) action Jump('city_wait')
        if Hours >= 16 and Hours < 20:
            idle 'city_1_map_2'
            hover 'city_1_map_2_hover'
            hotspot (655, 167, 294, 368) action Jump('city_wait')
            hotspot (998, 240, 257, 302) action Jump('city_wait')
            hotspot (644, 556, 278, 251) action Jump('city_wait')
            hotspot (997, 553, 318, 253) action Jump('city_wait')
        if Hours >= 20 and Hours < 25:
            idle 'city_1_map_3'
            hover 'city_1_map_3_hover'
            hotspot (655, 167, 294, 368) action Jump('city_wait')
            hotspot (998, 240, 257, 302) action Jump('city_wait')
            hotspot (644, 556, 278, 251) action Jump('city_wait')
            hotspot (997, 553, 318, 253) action Jump('city_wait')

    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/compass.png', 100, 100)
            hover im.Scale('icon/compass_hover.webp', 100, 100)
            action Jump('hub_choose_label')
        imagebutton:
            idle im.Scale('icon/solar-time.png', 100, 100)
            hover im.Scale('icon/solar-time_hover.webp', 100, 100)
            action Jump('city_wait')


label city_wait:
    menu rest:
        "Вернутья на карту":
            call screen city_hub
        "Вернуться в хаб":
            jump back_to_hub
        "Отдохнуть":
            $ GG_Stamina[0] += (GG_Stamina[1]/2)
            if GG_Stamina[0] > GG_Stamina[1]:
                $ GG_Stamina[0] = GG_Stamina[1]
            "Вы потратили время на отдых"
            call time2
            call screen city_map_2


screen city_map_3:
    imagemap:

        add im.Scale('gui/frame_2.webp', 800, 50) xpos 600 ypos 0
        add im.Scale('gui/frame_2.webp', 335, 100) xpos 1580 ypos 10
        text "{color=#ffffff}[Days] день {/color} " xpos 1600 ypos 10
        text "{color=#ffffff} %s {/color}" % WeekDays[WeekDayNumber] xpos 1600 ypos 44
        text "{color=#ffffff}[Hours]:[MinutesStr]{/color}" xpos 1800 ypos 10

        add im.Scale('icon/opened-food-can.webp', 45, 45) xpos 610 ypos 0
        text "{size=20}{color=#ffffff}: %i {/color}{/size}" %GG_Inventory_Items[0] xpos 660 ypos 10
        add im.Scale('icon/medical-pack-alt.webp', 45, 45) xpos 750 ypos 0
        text "{size=20}{color=#ffffff}: [GG_Inventory_Items[1]] {/color}{/size}" xpos 800 ypos 10
        add im.Scale('icon/half-log.webp', 45, 45) xpos 870 ypos 0
        text "{size=20}{color=#ffffff}: [GG_Inventory_Items[2]] {/color}{/size}" xpos 920 ypos 10

        if Hours >= 6 and Hours < 16:
            idle 'city_1_map_1'
            hover 'city_1_map_1_hover'
            hotspot (655, 167, 294, 368) action Jump('city_wait_shop')
            hotspot (998, 240, 257, 302) action Jump('city_wait_shop')
            hotspot (644, 556, 278, 251) action Jump('city_wait_shop')
            hotspot (997, 553, 318, 253) action Jump('city_wait_shop')
        if Hours >= 16 and Hours < 20:
            idle 'city_1_map_2'
            hover 'city_1_map_2_hover'
            hotspot (655, 167, 294, 368) action Jump('city_wait_shop')
            hotspot (998, 240, 257, 302) action Jump('city_wait_shop')
            hotspot (644, 556, 278, 251) action Jump('city_wait_shop')
            hotspot (997, 553, 318, 253) action Jump('city_wait_shop')
        if Hours >= 20 and Hours < 25:
            idle 'city_1_map_3'
            hover 'city_1_map_3_hover'
            hotspot (655, 167, 294, 368) action Jump('city_wait_shop')
            hotspot (998, 240, 257, 302) action Jump('city_wait_shop')
            hotspot (644, 556, 278, 251) action Jump('city_wait_shop')
            hotspot (997, 553, 318, 253) action Jump('city_wait_shop')

    vbox xalign 0.03 yalign 0.05 spacing 5:
        imagebutton:
            idle im.Scale('icon/compass.png', 100, 100)
            hover im.Scale('icon/compass_hover.webp', 100, 100)
            action Jump('hub_choose_label')
        imagebutton:
            idle im.Scale('icon/solar-time.png', 100, 100)
            hover im.Scale('icon/solar-time_hover.webp', 100, 100)
            action Jump('city_wait')
