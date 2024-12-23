transform spaghettinio(base, blink, jump):
    parallel:
        character_blink(base, blink)
    parallel:
        spagetinio_jump(base, jump)
    parallel:
        spagetinio_xzoom
# at
transform spagetinio_show():
    align (0.99, 0.95)
    offset (1000, 0)
    easeout 1.5:
        offset (0, 0)
    pause 0.1
# animations
transform spagetinio_jump(base, jump):
    renpy.random.randint(8, 20)
    jump
    easein 0.30 yoffset -300
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