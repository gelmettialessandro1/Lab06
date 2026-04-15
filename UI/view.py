import flet as ft



class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.tendina_anno= ft.Dropdown(label="anno")
        self._controller.riempiTendina_anno()

        self.tendina_brand = ft.Dropdown(label="brand")
        self._controller.riempiTendina_brand()

        self.tendina_retailer = ft.Dropdown(label="retailer")
        self._controller.riempiTendina_retailer()

        self.row1=ft.Row(controls=[self.tendina_anno,self.tendina_brand,self.tendina_retailer])
        self._page.add(self.row1)

        self.top_vendite = ft.ElevatedButton(text="top vendite", on_click=self._controller.topVendite)

        self.analizza_vendite = ft.ElevatedButton(text="analizza vendite", on_click=self._controller.analizzaVendite)

        self.row2 = ft.Row(controls=[self.top_vendite, self.analizza_vendite])
        self._page.add(self.row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()











    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
