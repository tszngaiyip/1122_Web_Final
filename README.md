# README.md

## 如何執行
系統安裝python及flask後，執行`app.py`即可

## 檔案說明

### app.py
- 跑flask的地方

### database_helper.py
- 讀取`static/json/db.json`
- 接受查詢要求並回傳餐點資料，沒有符合條件的餐點時
- 參數接受亂數及指定的條件，當使用亂數時忽略指定條件`meal_type_menu`為空陣列
- 回傳格式為`json`，例如：
    ```json
    {
      "rest_name": "仙桃總鋪",
      "rest_menu": {
        "meal_type_name": "飯",
        "meal_type_menu": [
          {
            "meal_name": "蛋炒飯",
            "meal_price": 60
          },
          {
            "meal_name": "肉絲炒飯",
            "meal_price": 70
          }
        ] 
      }
    }
    ```
  其中，`{}`是字典`dictionary`，`[]`是陣列`list`，用法不太一樣，須注意


### 其餘應該不用解釋
- 有問題再問
