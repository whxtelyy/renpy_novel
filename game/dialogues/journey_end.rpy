label journey_end:
    scene radik
    show bagio at bagio_dynamic
    show spaghettinio at spagetinio_dynamic
    with Fade(0.5, 0.4, 0.75)

    em "Фух, наконец-то! Дверь есть, она работает и выглядит как надо."
    show bagio happy with dissolve
    ba "Ну что, хорошо поработали."
    sp "И не просто справился. Дверь теперь не только работает, но и выглядит так, как должна. Молодец."

    em "Спасибо, но... что дальше? Сколько там ещё таких багов осталось?"

    ba "Хм... Никаких багов. Нигде. Всё чисто. Это даже... странно."
    sp "Ты хочешь сказать, что мы всё это время гонялись всего за одной маленькой недоработкой?"

    ba "Выходит так. Искал три дня, перевернул всё вверх дном, а исправил за пару минут. Ну, классика."

    em "Точно. Столько всего проверили, перебрали, а в итоге всё упиралось в одну мелочь."

    sp "Зачастую именно так и бывает. Самое сложное — понять, в чём проблема. А исправить её — это уже дело техники."

    show bagio happy with dissolve
    ba "Но главное, ты справился. Багов больше нет, проект завершён. Ты можешь возвращаться."
    show bagio with dissolve

    em "Значит, теперь мы прощаемся?"

    ba "Ну, как сказать... Мы останемся тут, а ты вернёшься в свой мир. Но ведь ты уже понял: мы всегда были с тобой — и в прошлых проектах, и будем в будущих."

    sp "Когда ты будешь искать ошибки или доводить код до совершенства, нас будет не видно, но мы всё равно будем рядом."

    em "Спасибо вам. Я уж думал, что не справлюсь. А теперь... теперь даже немного горжусь собой."

    ba "Удачи, Эмрах. Мы увидимся, даже если ты этого не заметишь."
    play sound "audio/baggio_flying.mp3" volume 0.09
    hide bagio with moveouttop

    sp "И помни, в любом проекте главное — думать. Всё остальное приложится."
    hide spaghettinio with moveoutright
    stop sound fadeout 0.5
    pause 0.5

    scene office with Pixellate(1.5, 8)
    play music "audio/office_music.mp3" volume 0.1 fadein 0.5
    show emrach with dissolve
    em "И вот я снова здесь. Всё готово. Проект завершён."

    play sound "door_knock_open.mp3" volume 0.3
    pause 2

    show sergey happy at left with moveinleft
    sg "Эмрах! Тестировщики прогнали проект перед релизом, всё работает безупречно. Отличная работа! Клиенты будут довольны."

    show emrach happy with dissolve
    em "Спасибо, Сергей Геннадьевич. Были сложности, но мы разобрались."
    show emrach with dissolve

    sg "И это главное. Хороший разработчик не тот, кто не ошибается, а тот, кто умеет находить проблемы и исправлять их. Продолжай в том же духе."
    hide sergey happy with moveoutleft

    play sound "door_open.mp3" volume 0.3
    pause 1

    show emrach surprised with dissolve
    em "Искал ошибку три дня, исправил за три минуты. Да, программирование часто так работает. Самая простая ошибка может отнять кучу времени."
    em "Но это не страшно. Программирование — это не про идеальный код с первого раза. Это про то, как ты справляешься с неидеальным. Главное — всегда доводить до конца."
    show emrach happy with dissolve
    $ good_ending.grant()
    em "Ну что, поехали дальше. Пойду возьму новый таск."
    hide emrach with moveoutleft
    show full_black with irisin
    pause 2.5
    return
