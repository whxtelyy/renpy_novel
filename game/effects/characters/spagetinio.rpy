transform spaghettinio(base, blink, jump):
    base
    align (0.99, 0.95)
    parallel:
        spagetinio_jump(base, jump)
    parallel:
        spagetinio_xzoom
    parallel:
        character_blink(base, blink)
# animations
transform spagetinio_jump(base, jump):
    renpy.random.randint(8, 20)
    jump
    easein 0.30 yoffset -200
    easeout 0.30 yoffset 0
    base
    repeat
transform spagetinio_xzoom():
    renpy.random.randint(8, 20)
    choice:
        linear 0.001 xzoom 1
    choice:
        linear 0.001 xzoom -1
    repeat
# at
transform spagetinio_show():
    align (1.25, 1.5)
    easeout 1.0:
        align (0.99, 0.95)
    pause 0.1
    