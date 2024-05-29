# README.md

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
