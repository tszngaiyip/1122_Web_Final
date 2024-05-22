import json
import random


class DatabaseHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = json.load(open(self.db_name, encoding="utf-8"))

    def query(self, query_rest_name=None, query_meal_type=None, rand_seed=None) -> dict:
        ret: dict = {}

        # query for both
        if query_rest_name and query_meal_type:
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
                    'meal_type_name': query_meal_type,
                    'meal_type_menu': result
                }
            }

        # query for rest name only
        # if query_rest_name:
        #     for rest in self.db:
        #         if query_rest_name == rest['rest_name']:
        #             ret = rest
        #             break
        #
        # # query for meal type only
        # if query_meal_type:
        #     result = []
        #     for rest in self.db:
        #         for meal_type in rest['rest_menu']:
        #             if query_meal_type == meal_type['meal_type_name']:
        #                 result.append(meal_type['meal_type_menu'])
        #     ret = {
        #         'rest_name': '全部',
        #         'rest_menu': {
        #             'meal_type_name': query_meal_type,
        #             'meal_type_menu': result
        #         }
        #     }

        else:
            ret = {'error': 'No query parameters provided'}

        if rand_seed:
            random.seed(rand_seed)
            print(ret)
            ret['rest_menu']['meal_type_menu'] = [random.choice(ret['rest_menu']['meal_type_menu'])]

            # random_rest = random.choice(ret['rest_menu']['meal_type_menu'])  # 随机选择一个餐馆
            # random_meal_type = random.choice(random_rest['rest_menu'])  # 随机选择一个餐类型
            # random_meal = random.choice(random_meal_type['meal_type_menu'])  # 随机选择一个餐点
            # ret = {
            #     'rest_name': random_rest['rest_name'],
            #     'rest_menu': {
            #         'meal_type_name': random_meal_type['meal_type_name'],
            #         'meal_type_menu': [
            #             random_meal
            #         ]
            #     }
            # }

        return ret
