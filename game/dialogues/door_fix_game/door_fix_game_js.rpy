label door_fix_game_js:
    call screen dfg_menu_scroll({
        "title": "Выберите способ назначения события на дверь:",
        "menu": [
            {
                "caption": 'document.querySelector(".door").addEventListener("click", function () {{\n  const isClosed = this.getAttribute("data-status") = = = "closed";\n  this.setAttribute("data-status", isClosed ? "open" : "closed");\n});',
                "action": Return("first")
            },
            {
                "caption": 'var door = document.querySelector(".door");\ndoor.onclick = function () {{\n  var isClosed = door.getAttribute("data-status") = = = "closed";\n  door.setAttribute("data-status", isClosed ? "open" : "closed");\n};',
                "action": Return("second")
            },
            {
                "caption": 'document.querySelector(".door").addEventListener("click", () => {{\n  const isClosed = this.getAttribute("data-status") = = = "closed";\n  this.setAttribute("data-status", isClosed ? "open" : "closed");\n});',
                "action": Return("third")
            },
            {
                "caption": 'document.querySelector(".door").onclick = function () {{\n  const isClosed = document.getAttribute("data-status") = = = "closed";\n  document.setAttribute("data-status", isClosed ? "open" : "closed");\n};',
                "action": Return("fourth")
            },
        ]
    })

    if result == "first":
        "Этот вариант идеально подходит. Используется современный способ назначения событий через addEventListener, который позволяет гибко управлять обработчиками. class задаёт стиль двери, а data-status переключается при каждом клике."
    elif result == "second":
        "Этот вариант работает, но он устарел. Использование onclick ограничивает возможность добавления нескольких обработчиков на один элемент. Это может быть проблемой, если нам потребуется добавить новые функции, связанные с кликом."
        call door_fix_game_js
    elif result == "third":
        "Вместо обычной функции используется стрелочная. Проблема в том, что стрелочная функция не имеет собственного контекста this. В данном случае this не будет ссылаться на .door, что приведёт к ошибке. Это частая ошибка новичков, так как синтаксис стрелочной функции выглядит компактно, но работает по-другому."
        call door_fix_game_js
    elif result == "fourth":
        "Вместо изменения атрибута у элемента .door, здесь используется document. Это приводит к тому, что код пытается менять атрибуты у всего документа, а не у конкретной двери. Такой подход полностью некорректен и вызовет ошибку."
        call door_fix_game_js

    return
