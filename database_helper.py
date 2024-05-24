import json
import random


class DatabaseHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = json.load(open(self.db_name, encoding="utf-8"))

    def rand_pick_in_rest(self, query_rest_name, query_food_type, rand_seed) -> dict:
        ret = {
            'food_type': None,
            'food_name': None,
            'food_price': None,
        }
        if query_food_type == '都可':
            query_result: dict = self.query(query_rest_name, None)
            random.seed(rand_seed)
            choice = random.choice(query_result['rest_menu'])
            ret['food_type'] = choice['food_type_name']
            choice = random.choice(choice['food_type_menu'])
            ret['food_name'] = choice['food_name']
            ret['food_price'] = choice['food_price']

            return ret

        query_result: dict = self.query(query_rest_name, query_food_type)
        print(query_result)
        random.seed(rand_seed)
        choice = random.choice(query_result['rest_menu']['food_type_menu'])
        ret['food_type'] = query_food_type
        ret['food_name'] = choice['food_name']
        ret['food_price'] = choice['food_price']

        return ret

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
            # result = []
            for rest in self.db:
                if query_rest_name == rest['rest_name']:
                    return {
                        'rest_name': query_rest_name,
                        'rest_menu': rest['rest_menu']
                    }
            #         for food_type in rest['rest_menu']:
            #             for food in food_type['food_type_menu']:
            #                 result.append(food)
            # return {
            #     'rest_name': query_rest_name,
            #     'rest_menu': {
            #         'food_type_name': 'all',
            #         'food_type_menu': result
            #     }
            # }

        # query for food type only
        if query_food_type:
            ret = self.db
            for rest in self.db:
                for menu in rest['rest_menu']:
                    if query_food_type != menu['food_type_name']:
                        rest['rest_menu'].remove(menu)
            return ret

            # result = []
            # for rest in self.db:
            #     for food_type in rest['rest_menu']:
            #         if query_food_type == food_type['food_type_name']:
            #             for food in food_type['food_type_menu']:
            #                 result.append(food)
            # return {
            #     'rest_name': 'all',
            #     'rest_menu': {
            #         'food_type_name': query_food_type,
            #         'food_type_menu': result
            #     }
            # }

        else:
            ret = {'error': 'No query parameters provided'}

        return ret
