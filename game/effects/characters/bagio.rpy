# show
transform bagio(base, blink):
    parallel:
        character_blink(base, blink)
# at
transform bagio_show:
    align(0.0, 0.35)
    offset (-400, -900)
    zoom 0.0
    rotate -100
    parallel:
        easeout 1.5:
            offset (0, 0)
            zoom 1.0
            rotate -10
    pause 0.0
    bagio_fly
# animation
transform bagio_fly:
    parallel:
        ease 4:
            xoffset -30
            rotate -2
        ease 4:
            xoffset 30
            rotate 2
        repeat
    parallel:
        ease 3.5 yoffset 7.5
        ease 3.5 yoffset -7.5
        repeat
