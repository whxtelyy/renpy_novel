transform character_blink(base, blink):
    base
    choice:
        renpy.random.randint(1, 5)
    choice:
        renpy.random.randint(2, 6)
    choice:
        renpy.random.randint(4, 7)
    choice:
        renpy.random.randint(5, 9)
    choice:
        renpy.random.randint(8, 15)
    blink
    pause 0.2   
    repeat