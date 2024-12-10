label door_fix_game_css:
    call screen dfg_menu_scroll({
        "title": "Задайте основные стили для двери (закрытое состояние):",
        "menu": [
            {
                "caption": '.door {{\n  width: 100px;\n  height: 200px;\n  background-image: url("door-closed.png");\n  background-size: cover;\n  transform-origin: left;\n  transition: transform 0.5s ease, background-image 0.5s ease;\n}',
                "action": Return("first")
            },
            {
                "caption": '.door {{\n  width: 100px;\n  height: 200px;\n  background: url("door-closed.png") center/contain;\n  transform-origin: left;\n  transition: none;\n  border: 5px dotted red\n}',
                "action": Return("second")
            },
            {
                "caption": '.door {{\n  width: 100px;\n  height: 200px;\n  background: url("door-closed.png") repeat;\n  transform-origin: center;\n  transition: transform 0.5s ease-in-out;\n  border: none;\n}',
                "action": Return("third")
            },
            {
                "caption": '.door {{\n  width: 100px;\n  height: auto;\n  background: none;\n  transform-origin: top;\n  transition: none;\n  border: 1px solid black;\n}',
                "action": Return("fourth")
            },
        ]
    })

    if result == "first":
        "Вы выбрали правильное решение. Дверь выглядит естественно, и все параметры настроены аккуратно."
        call door_fix_game_css_continue
    elif result == "second":
        "Рабочий вариант, но неаккуратный: рамка выглядит странно, анимации отсутствуют."
        call door_fix_game_html
    elif result == "third":
        "В этом решении фон двери повторяется, а точка трансформации выбрана некорректно."
        call door_fix_game_html
    elif result == "fourth":
        "Ваш выбор привёл к невидимой двери. Без фона и правильной высоты дверь теряет смысл."
        call door_fix_game_html

    return

label door_fix_game_css_continue:
    call screen dfg_menu_scroll({
        "title": "Опишите стили для двери в открытом состоянии (data-status='open'):",
        "menu": [
            {
                "caption": '.door[[data-status="open"] {{\n  transform: rotateY(90deg);\n  background-image: url("door-open.png");\n}}',
                "action": Return("first")
            },
            {
                "caption": '.door[[data-status="open"] {{\n  transform: rotateY(90deg);\n  background: url("door-open.png") center/contain;\n}}',
                "action": Return("second")
            },
            {
                "caption": '.door[[data-status="open"] {{\n  transform: rotateY(180deg);\n  background: none;\n}}',
                "action": Return("third")
            },
            {
                "caption": '.door[[data-status="open"] {{\n  transform: none;\n  background: none;\n}}',
                "action": Return("fourth")
            },
        ]
    })

    if result == "first":
        "Превосходно! Дверь открывается плавно, а изображение меняется. Всё работает корректно."
    elif result == "second":
        "Выбрано рабочее решение, но фон настроен неаккуратно: при увеличении окна могут появиться ошибки."
        call door_fix_game_html
    elif result == "third":
        "Ваш выбор привёл к ошибке: дверь поворачивается на 180°, что нарушает логику, и фон пропадает."
        call door_fix_game_html
    elif result == "fourth":
        "Полностью неверный вариант: дверь не открывается, и никаких изменений не происходит."
        call door_fix_game_html

    return
