from database import DB_connect
from database.DB_connect import DBConnect
from database.DTO import retailerDTO
from database.DTO import vendita_ricavo

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def tutti_anni_vendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""SELECT distinct YEAR(date) AS anno
                          FROM go_daily_sales;
                              """)
        lista = cursor.fetchall()

        risultati = []
        for diz in lista:

            risultati.append(diz["anno"])

        cursor.close()
        cnx.close()
        return risultati


    @staticmethod
    def tutti_brand_vendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""SELECT distinct Product_brand as brand
                          FROM go_products;
                              """)
        lista = cursor.fetchall()

        risultati = []
        for diz in lista:

            risultati.append(diz["brand"])

        cursor.close()
        cnx.close()
        return risultati

    @staticmethod
    def tutti_retailer_vendite():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""SELECT Retailer_code as code , retailer_name as name
                              FROM go_retailers;
                                  """)
        lista = cursor.fetchall()

        risultati = []
        for diz in lista:
            risultati.append(retailerDTO(diz["code"],diz["name"]))

        cursor.close()
        cnx.close()
        return risultati

    @staticmethod
    def top_vendite(code, brand, anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""SELECT ds.Retailer_code as code, ds.Unit_sale_price*ds.Quantity as ricavo, p.Product_number as number , ds.date as data
                            FROM go_daily_sales as ds, go_retailers as r, go_products as p
                            WHERE ds.Retailer_code=r.Retailer_code AND ds.Product_number=p.Product_number
                            AND ds.Retailer_code = %s
                            AND p.Product_brand = %s
                            AND YEAR(ds.date) = %s 
                            """, (code, brand, anno))

        lista = cursor.fetchall()

        risultati = []
        for diz in lista:
            risultati.append(vendita_ricavo(diz["code"],int(diz["number"]),int(diz["ricavo"]),diz["data"]))

        cursor.close()
        cnx.close()
        return risultati


