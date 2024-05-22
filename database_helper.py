import json
import random


class DatabaseHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = json.load(open(self.db_name, encoding="utf-8"))

    def query(self, query_rest_name=None, query_meal_type=None, rand_seed=None) -> dict:
        ret: dict = {}

        # query for both
        if query_rest_name and query_food_type:
            result = []
            for rest in self.db:
                if query_rest_name == rest['rest_name']:
                    for meal_type in rest['rest_menu']:
                        if query_meal_type == meal_type['meal_type_name']:
                            for meal in meal_type['meal_type_menu']:
                                result.append(meal)
            ret = {
                'rest_name': query_rest_name,
                'rest_menu': {
                    'meal_type_name': 'all',
                    'meal_type_menu': result
                }
            }


        else:
            ret = {'error': 'No query parameters provided'}

        if rand_seed:
            random.seed(rand_seed)
            print(ret)
            ret['rest_menu']['meal_type_menu'] = [random.choice(ret['rest_menu']['meal_type_menu'])]

        return ret
