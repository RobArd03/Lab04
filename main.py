import flet as ft
import controller as c
import view as v

# setup model view control according to MVC pattern
def main(page: ft.Page):
    view = v.View(page)
    controller = c.SpellChecker(view)
    view.setController(controller)
    view.add_content()
    view.update()

ft.app(target=main)
