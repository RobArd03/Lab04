
import flet as ft



class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.on_check_click = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page




    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title ],
                   alignment=ft.MainAxisAlignment.START)
        )





        # Dati che do al utente

        self._language = ft.Dropdown(label = "Seleziona la lingua",
                           expand = True,
                           options=[
                               ft.dropdown.Option("Italian"),
                               ft.dropdown.Option("English"),
                               ft.dropdown.Option("Spanish") ]
                           )

        self._modIn = ft.Dropdown(label = "Modalità",
                          width = 200,
                          options=[
                              ft.dropdown.Option("Default"),
                              ft.dropdown.Option("Linear"),
                              ft.dropdown.Option("Dichotomic") ]
                          )

        # dati che mi da l'utente
        self._txtIn = ft.TextField(label = "Inserisci la frase",
                             expand = True)

        self._btn_check = ft.ElevatedButton(text="Controlla",
                                      on_click = self.__controller.check,
                                      width = 150)

        # Lista di stringhe sottostante
        self._lv = ft.ListView( expand = True )

        # Definizione dei row
        row1 = ft.Row( controls = [ self._language ] )
        row2 = ft.Row( controls = [ self._modIn, self._txtIn, self._btn_check ] )

        self.page.add( row1, row2, self._lv )

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
