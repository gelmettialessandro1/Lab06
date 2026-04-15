import flet as ft
from database.DAO import DAO
from database.DTO import*

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def riempiTendina_anno(self):
        self._view.tendina_anno.options.append(ft.dropdown.Option("nessun filtro"))
        for anno in DAO.tutti_anni_vendite():
            self._view.tendina_anno.options.append(ft.dropdown.Option(key=anno,text=f"{anno}"))
        self._view.update_page()




    def riempiTendina_brand(self):
        self._view.tendina_brand.options.append(ft.dropdown.Option("nessun filtro"))
        for brand in DAO.tutti_brand_vendite():
            self._view.tendina_brand.options.append(ft.dropdown.Option(key=brand, text=f"{brand}"))
        self._view.update_page()

    def riempiTendina_retailer(self):
        self._view.tendina_retailer.options.append(ft.dropdown.Option("nessun filtro"))
        for retailer in DAO.tutti_retailer_vendite():
            self._view.tendina_retailer.options.append(ft.dropdown.Option(key=retailer.code, text=f"{retailer.code}-{retailer.name}", data=retailerDTO))
        self._view.update_page()

    def topVendite(self,e):

        codeRetailer = int(self._view.tendina_retailer.value)
        anno = int(self._view.tendina_anno.value)
        brand = self._view.tendina_brand.value
        if(codeRetailer=="nessun filtro"):
            codeRetailer=None
        if(anno=="nessun filtro"):
            anno=None
        if(brand=="nessun filtro"):
            brand=None

        for vr in DAO.top_vendite(codeRetailer,brand,anno):
            self._view.txt_result.controls.append(ft.Text(f"fornitore con codice:  {vr.codeRetailer} ricavo di:  {vr.ricavo} in data:  {vr.data}"))

        self._view.update_page()







    def analizzaVendite(self,e):
        pass

