# README.md

## 簡介
餐廳訂餐系統，使用HTML, CSS, JavaScript, Python製作網頁，當中技術有Python Flask, PlotyJS, LLM, HTML5 Canvas等。網頁有直接點餐、隨機點餐、 公休時間、上月銷售量及聊天機器人的功能。

## 如何執行
1. 建立並填寫`config.ini`
   - `API_KEY`：Google Gemini API Key，**請注意不要把你的API_KEY上傳到網際網路**
   - `model`: 要使用的 Gemini 模型，老師上課是用 gemini-pro
   - 格式：
     ```ini
     [Gemini]
     API_KEY = your_api_key
     model = gemini-pro
     ```
      
2. 安裝必要套件
    ```bash
    pip install -r requirements.txt
    ```
3. 執行`app.py`
    ```bash
    python app.py
    ```
