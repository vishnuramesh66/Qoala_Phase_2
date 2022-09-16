import mysql.connector


class Database:
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host="14.143.173.87",
            user="qoala-db-user",
            password="Changem3",
            database="qoala"
        )
        self.__my_cursor = self.__mydb.cursor()

    def insert_order_details(self, order_id, order_detail_id, id_number, registration_number, postal_code, vehicle_sum_insured):
        sql = "INSERT INTO order_details (order_id, order_detail_id, id_number, registration_number, postal_code, " \
              "vehicle_sum_insured) VALUES (%s, %s, %s, %s, %s, %s) "
        val = (order_id, order_detail_id, id_number, registration_number, postal_code, vehicle_sum_insured)
        self.__my_cursor.execute(sql, val)
        self.__mydb.commit()
        print("record inserted with id = ", order_detail_id)

    def insert_quotation_orders(self, order_id, order_count):
        sql = "INSERT INTO quotation_orders (order_id, order_count) VALUES (%s, %s)"
        val = (order_id, order_count)
        self.__my_cursor.execute(sql, val)
        self.__mydb.commit()
        print("record inserted into quotation_orders table with order_id = ", order_id)


