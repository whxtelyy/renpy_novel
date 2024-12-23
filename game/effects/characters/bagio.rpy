transform bagio(base, blink):
    parallel:
        character_blink(base, blink)
# animation
transform bagio_fly:
    easeout 1.25:
        offset(-30, 82.5)
        rotate 0
    parallel:
        ease 4:
            xoffset 0
            rotate 2
        ease 4:
            xoffset -60
            rotate -2
        repeat
    parallel:
        ease 3.5 yoffset 90
        ease 3.5 yoffset 75
        repeat
# at
transform bagio_show:
    offset(-650, -750)
    zoom 0.0
    rotate -100
    easeout 1.5:
        offset(125, 250)
        zoom 1.0
        rotate -10
    pause 1
    bagio_fly

