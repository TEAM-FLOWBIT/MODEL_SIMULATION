import pymysql
import configparser
from sqlalchemy import create_engine, text


class MySqlHandler():

    def __init__(self, mode="remote", db_name=None, charset=None):
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        self.host = config["MYSQL"]['remote_host']
        self.user = config["MYSQL"]['user']
        self.password = config["MYSQL"]['password']
        #self.db = config["MYSQL"]['db']

        if mode == "remote":
            self._client = pymysql.connect(host=self.host, user=self.user, password=self.password, db=db_name, charset=charset)
        elif mode == "local":
            self._client = pymysql.connect(host='127.0.0.1', user='root', password='1248', db='flowbit', charset='utf8')
        self.cursor = self._client.cursor()

    def insert_items_to_actual_data(self, datas):
        #print(datas)
        for data in datas:
            #print(type(data))
            query = """
            INSERT INTO actual_data(timestamp, open_price, close_price,high_price, low_price, volume) 
            VALUES('{timestamp}', '{open_price}', '{close_price}', '{high_price}', '{low_price}', '{volume}');
            """.format(**data)
            #print(query)
            self.cursor.execute(query)
        
        self._client.commit()
        
    def insert_item_to_actual_data(self, data):
        query = """
        INSERT INTO actual_data(timestamp, open_price, close_price,high_price, low_price, volume) 
        VALUES('{timestamp}', '{open_price}', '{close_price}', '{high_price}', '{low_price}', '{volume}');
        """.format(**data)
        #print(query)
        self.cursor.execute(query)
        self._client.commit()

    def find_close_price_from_actual_data(self, limit=0):
        query = """SELECT close_price FROM actual_data ORDER BY aid DESC LIMIT """ + str(limit) + """;"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        #print(result)
        return result
    
    def find_all_items_from_actual_data(self, limit=0):
        query = """SELECT * FROM actual_data ORDER BY aid DESC LIMIT """ + str(limit) + """;"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        ret_list = []
        for result in results:
            item = {}
            item["_id"] = result[0]
            item["timestamp"] = result[1].strftime('%Y-%m-%d')
            item["open_price"] = result[2]
            item["close_price"] = result[3]
            item["high_price"] = result[4]
            item["low_price"] = result[5]
            item["volume"] = result[6]
            ret_list.append(item)
            #print(item)
        
        return ret_list
    
    def find_all_items_from_predicted_data(self, limit=0):
        query = """SELECT * FROM predicted_data ORDER BY pid DESC LIMIT """ + str(limit) + """;"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        ret_list = []
        for result in results:
            item = {}
            item["_id"] = result[0]
            item["timestamp"] = result[1].strftime('%Y-%m-%d')
            item["predicted_price"] = result[2]
            ret_list.append(item)
        
        return ret_list
    
    def find_all_data_from_actual_data(self):
        query = """SELECT * FROM actual_data;"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        ret_list = []
        for result in results:
            item = {}
            item["_id"] = result[0]
            item["timestamp"] = result[1].strftime('%Y-%m-%d')
            item["open_price"] = result[2]
            item["close_price"] = result[3]
            item["high_price"] = result[4]
            item["low_price"] = result[5]
            item["volume"] = result[6]
            ret_list.append(item)
            #print(item)
        
        return ret_list
    
    def find_all_data_from_predicted_data(self):
        query = """SELECT * FROM predicted_data;"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        ret_list = []
        for result in results:
            item = {}
            item["_id"] = result[0]
            item["timestamp"] = result[1].strftime('%Y-%m-%d')
            item["predicted_price"] = result[2]
            ret_list.append(item)
        
        return ret_list

    def find_all_items_from_analysis_data(self, limit=0):
        query = """SELECT * FROM analysis_data ORDER BY aid DESC LIMIT """ + str(limit) + """;"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        ret_list = []
        for result in results:
            item = {}
            item["_id"] = result[0]
            item["timestamp"] = result[1].strftime('%Y-%m-%d')
            item["gpt_response"] = result[2]
            ret_list.append(item)
        
        return ret_list

    def insert_item_to_analysis_data(self, data):
        query = """
        INSERT INTO analysis_data(timestamp, gpt_response) 
        VALUES('{timestamp}', "{gpt_response}");
        """.format(**data)
        #print(query)
        self.cursor.execute(query)
        self._client.commit()
    
    def insert_item_to_predicted_data(self, data):
        #print(type(data))
        query = """
        INSERT INTO predicted_data(timestamp, predicted_price) 
        VALUES('{timestamp}', '{predicted_price}');
        """.format(**data)
        #print(query)
        self.cursor.execute(query)
        
        self._client.commit()
    def find_items_from_predicted_data(self, limit=0):
        query = """SELECT close_price FROM actual_data ORDER BY aid DESC LIMIT """ + str(limit) + """;"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        #print(result)
        return result

    def insert_items(self):
        pass


    def find_items(self):
        pass

    def find_item(self):
        pass

    def delete_items(self):
        pass

    def update_items(self):
        pass

    def aggregate(self):
        pass