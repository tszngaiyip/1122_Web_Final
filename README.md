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

### 6. 瀏覽應用程式
在瀏覽器中開啟 `http://localhost:5000`

## ⚙️ 設定配置

### config.ini 配置檔案

在專案根目錄建立 `config.ini` 檔案：

```ini
[Gemini]
API_KEY = your_google_gemini_api_key_here
model = gemini-pro
```

### 取得 Google Gemini API Key

1. 前往 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 登入您的 Google 帳戶
3. 建立新的 API Key
4. 複製 API Key 到 `config.ini` 檔案

> ⚠️ **安全提醒**: 請勿將 API Key 上傳到公開的版本控制系統

### 環境變數設定 (可選)

```bash
# Windows
set GEMINI_API_KEY=your_api_key_here
set FLASK_ENV=development
```

## 📖 使用說明

### 🏠 首頁功能展示
1. **歡迎界面**: 展示餐廳資訊和主要功能入口
2. **導航選單**: 快速進入各功能頁面
3. **營業狀態**: 即時顯示模擬營業狀態

### 🍽️ 點餐流程展示
1. 點擊「開始點餐」進入點餐頁面
2. 瀏覽不同餐點類別：套餐、麵食、燉飯、漢堡等
3. 選擇餐點加入購物車（模擬功能）
4. 查看訂單詳情和總金額計算
5. 確認訂單並送出（展示完整流程）

### 🎲 隨機點餐功能
1. 選擇「隨機點餐」功能展示
2. 選擇餐點類型或選擇「都可」
3. 系統智能推薦演算法展示
4. 可重新隨機或直接加入訂單

### 💬 AI聊天機器人展示
1. 在點餐頁面找到聊天機器人圖示
2. 輸入關於餐點的問題
3. AI會提供智能回答和推薦（需配置API）
4. 支援自然語言對話技術展示

### 📈 銷售分析功能
1. 點擊「銷售報表」查看數據分析展示
2. 瀏覽互動式圖表技術實作
3. 分析不同餐點類型的銷售模擬數據
4. 查看時間趨勢和熱門餐點分析

## 🔌 API文件

### 餐點相關API

#### 取得隨機餐點
```http
POST /random_pick
Content-Type: application/json

{
    "food_type": "套餐",
    "rand_seed": 12345
}
```

#### 聊天機器人對話
```http
POST /chat
Content-Type: application/json

{
    "message": "推薦一些素食餐點"
}
```

#### 取得銷售數據
```http
GET /sales_data
```

### 回應格式

所有API回應均使用JSON格式：

```json
{
    "success": true,
    "data": {
        // 具體數據內容
    },
    "message": "操作成功"
}
```

## 🖼️ 功能截圖

> 註: 這是學術專題的功能展示截圖

- **首頁界面**: 清晰的導航和營業狀態顯示
- **點餐介面**: 直觀的餐點選擇和購物車功能
- **AI聊天**: 智能對話和推薦介面
- **銷售分析**: 豐富的數據視覺化圖表

## 🛠️ 疑難排解

### 常見問題

#### Q: 無法啟動應用程式，顯示模組找不到錯誤
**A**: 
```bash
# 確認已啟動虛擬環境
pip list  # 檢查已安裝的套件
pip install -r requirements.txt  # 重新安裝依賴
```

#### Q: AI聊天機器人無法回應
**A**: 
1. 檢查 `config.ini` 檔案是否正確設定
2. 確認 API Key 有效且有足夠配額
3. 檢查網路連線狀態

#### Q: 銷售數據無法載入
**A**: 
1. 確認 `static/BillLastMonth.csv` 檔案存在
2. 檢查 CSV 檔案格式是否正確
3. 確認檔案編碼為 UTF-8

#### Q: 靜態檔案無法載入
**A**: 
```bash
# 檢查檔案路徑
ls -la static/css/
ls -la static/js/
ls -la static/images/
```

### 錯誤代碼說明

| 錯誤代碼 | 說明 | 解決方案 |
|---------|------|----------|
| 500 | 伺服器內部錯誤 | 檢查應用程式日誌 |
| 404 | 檔案或路由不存在 | 確認URL路徑正確 |
| 400 | 請求格式錯誤 | 檢查API請求格式 |

### 日誌查看

應用程式日誌會顯示在終端機中，如需詳細除錯：

```bash
# 啟用除錯模式
export FLASK_DEBUG=1
python app.py
```

### 新增功能

1. 在 `app.py` 中新增路由
2. 建立對應的 HTML 模板
3. 新增必要的 CSS 和 JavaScript
4. 更新 README 文件

## 📄 授權

此專案為學術期末專題作品，僅供教育和學習用途。

### 📝 特別聲明
- 本專案非商業用途，純屬學術展示
- 菜單內容參考自卡利西里餐廳，僅供技術實作學習
- 如有侵權請聯繫，將立即移除相關內容
- 感謝卡利西里餐廳提供優質菜單內容作為學習參考

此專案僅供學習和教育用途。

<div align="center">


[回到頂部](#-卡利西里餐廳訂餐系統)

</div>