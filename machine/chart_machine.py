from db.mongodb.mongodb_handler import MongoDBHandler
from db.mysql.mysql_handler import MySqlHandler

class ChartMachine:

    def get_analysis_chart(self):
        """
        1. actual_data 가지고 오기 - 14개
        2. predicted_data 가지고 오기 - 15개
        """
        mySqlHandler = MySqlHandler(mode="local", db_name="flowbit")
        actual_data = mySqlHandler.find_all_items_from_actual_data(limit=14)
        #print(actual_data)
        predicted_data = mySqlHandler.find_all_items_from_predicted_data(limit=15)
        #db = MongoDBHandler(mode="local", db_name="AI", collection_name="actual_data")
        #actual_data = db.find_items_for_chart( db_name="AI", collection_name="actual_data", limit=14)
        #predicted_data = db.find_items_for_chart(db_name="AI", collection_name="predicted_data", limit=15)

        actual_data_list = []
        predicted_data_list = []

        actual_data_str = ''
        predicted_data_str = ''

        for i in actual_data:
            i["_id"] = str(i["_id"])
            actual_data_str += str(i)

        for i in predicted_data:
            i["_id"] = str(i["_id"])
            predicted_data_str += str(i)
        
        return actual_data_str, predicted_data_str

    def get_basic_chart(self):

        mySqlHandler = MySqlHandler(mode="local", db_name="flowbit")
        actual_data = mySqlHandler.find_all_items_from_actual_data(limit=14)
        predicted_data = mySqlHandler.find_all_items_from_predicted_data(limit=15)
        #db = MongoDBHandler(db_name="AI", collection_name="actual_data")
        #actual_data = db.find_items_for_chart( db_name="AI", collection_name="actual_data", limit=14)
        #predicted_data = db.find_items_for_chart(db_name="AI", collection_name="predicted_data", limit=15)

        actual_data_list = []
        predicted_data_list = []
        lables = []

        for i in actual_data:
            actual_data_list.append(i["close_price"])

        for i in predicted_data:
            lables.append(i["timestamp"])
            predicted_data_list.append(i["predicted_price"])

        chart_data = {}
        actual_data_list.reverse()
        predicted_data_list.reverse()
        lables.reverse()

        max_value = max(actual_data_list + predicted_data_list)
        min_value = min(actual_data_list + predicted_data_list)

        blank = (min_value + max_value) / 10
        chart_data["max"] = max_value + blank
        chart_data["min"] = min_value + blank
        chart_data["label"] = lables
        chart_data["datas"] = [
            {"label" : "actual_data", "datas" : actual_data_list}, 
            {"label" : "predicted_data", "datas" : predicted_data_list}]

        return chart_data