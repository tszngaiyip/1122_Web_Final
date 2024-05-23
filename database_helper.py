import json
import random


class DatabaseHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = json.load(open(self.db_name, encoding="utf-8"))

    def rand_pick(self, query_rest_name=None, query_food_type=None, rand_seed=None) -> dict:
        food_dict = self.query(
            None if query_rest_name == '都可' else query_rest_name,
            None if query_food_type == '都可' else query_food_type
        )
        random.seed(rand_seed)
        choice = random.choice(food_dict['rest_menu']['food_type_menu'])
        return {
            'food_type': query_food_type,
            'food_name': choice['food_name'],
            'food_price': choice['food_price'],
        }

    def query(self, query_rest_name=None, query_food_type=None) -> dict:

        # query for both
        if query_rest_name and query_food_type:
            result = []
            for rest in self.db:
                if query_rest_name == rest['rest_name']:
                    for food_type in rest['rest_menu']:
                        if query_food_type == food_type['food_type_name']:
                            return {
                                'rest_name': query_rest_name,
                                'rest_menu': {
                                    'food_type_name': query_food_type,
                                    'food_type_menu': food_type['food_type_menu']
                                }
                            }

        # query for rest name only
        if query_rest_name:
            result = []
            for rest in self.db:
                if query_rest_name == rest['rest_name']:
                    for food_type in rest['rest_menu']:
                        for food in food_type['food_type_menu']:
                            result.append(food)
            return {
                'rest_name': query_rest_name,
                'rest_menu': {
                    'food_type_name': 'all',
                    'food_type_menu': result
                }
            }

        # query for food type only
        if query_food_type:
            result = []
            for rest in self.db:
                for food_type in rest['rest_menu']:
                    if query_food_type == food_type['food_type_name']:
                        for food in food_type['food_type_menu']:
                            result.append(food)
            return {
                'rest_name': 'all',
                'rest_menu': {
                    'food_type_name': query_food_type,
                    'food_type_menu': result
                }
            }

        else:
            ret = {'error': 'No query parameters provided'}

        return ret
