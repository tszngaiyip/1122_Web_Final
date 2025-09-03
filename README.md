# 🍽️ 卡利西里餐廳訂餐系統

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

一個功能完整的餐廳訂餐系統，採用現代化Web技術打造，提供直觀的用戶界面和智能化的點餐體驗。

## 📋 目錄

- [專案簡介](#專案簡介)
- [主要功能](#主要功能)
- [技術架構](#技術架構)
- [專案結構](#專案結構)
- [系統需求](#系統需求)
- [安裝指南](#安裝指南)
- [設定配置](#設定配置)
- [使用說明](#使用說明)
- [API文件](#api文件)
- [功能截圖](#功能截圖)
- [疑難排解](#疑難排解)
- [開發指南](#開發指南)
- [貢獻指南](#貢獻指南)
- [授權條款](#授權條款)

## 🌟 專案簡介

卡利西里餐廳訂餐系統是一個使用 **Python Flask** 框架開發的現代化Web應用程式。系統整合了多項先進技術，包括人工智慧聊天機器人、數據分析視覺化、以及響應式網頁設計，為用戶提供完整的線上點餐體驗。

### 🎯 專案目標
- 提供直觀易用的點餐界面
- 整合AI技術提升用戶體驗
- 提供完整的銷售數據分析
- 實現響應式設計支援多裝置

## ✨ 主要功能

### 🍕 點餐功能
- **直接點餐**: 瀏覽完整菜單，選擇心儀餐點
- **隨機點餐**: 系統智能推薦，為用戶帶來驚喜
- **購物車管理**: 即時管理訂單內容和總價

### 🤖 AI聊天機器人
- 整合 **Google Gemini AI** 技術
- 智能回答用戶關於餐點的問題
- 提供個性化推薦服務
- 自然語言對話體驗

### 📊 數據分析
- **銷售報表**: 視覺化上月銷售數據
- **PlotlyJS圖表**: 互動式圖表展示
- **多維度分析**: 按餐點類型、時間等維度分析

### 🕐 營業管理
- 公休時間設定與顯示
- 即時營業狀態更新
- 營業時間智能提醒

### 🎨 用戶體驗
- **HTML5 Canvas**: 創新的視覺效果
- **響應式設計**: 支援桌面和行動裝置
- **現代化UI**: 美觀的用戶界面設計

## 🔧 技術架構

### 後端技術
- **Python 3.8+**: 主要開發語言
- **Flask 2.0+**: Web應用框架
- **Pandas**: 數據處理和分析
- **LangChain**: AI聊天機器人框架
- **Google Gemini AI**: 自然語言處理

### 前端技術
- **HTML5**: 現代化標記語言
- **CSS3**: 樣式設計和響應式布局
- **JavaScript ES6+**: 動態交互功能
- **PlotlyJS**: 數據視覺化
- **HTML5 Canvas**: 圖形繪製
- **jQuery**: DOM操作和AJAX

### 數據儲存
- **JSON**: 菜單和配置數據
- **CSV**: 銷售數據分析
- **檔案系統**: 靜態資源管理

## 📁 專案結構

```
1122_Web_Final/
├── README.md                 # 專案說明文件
├── app.py                   # Flask主應用程式
├── requirements.txt         # Python依賴套件
├── config.ini              # 配置檔案 (需自行建立)
├── 專題報告.pdf             # 專題報告文件
│
├── 核心模組/
│   ├── database_helper.py   # 數據庫操作輔助類
│   ├── llm.py              # AI聊天機器人模組
│   └── sales_helper.py     # 銷售數據分析模組
│
├── templates/              # HTML模板檔案
│   ├── index.html         # 首頁模板
│   ├── order.html         # 點餐頁面模板
│   ├── ordered.html       # 訂單確認模板
│   └── sales.html         # 銷售分析模板
│
└── static/                # 靜態資源目錄
    ├── css/              # 樣式表檔案
    │   ├── index.css
    │   ├── order.css
    │   ├── ordered.css
    │   └── sales.css
    ├── js/               # JavaScript檔案
    │   ├── index.js
    │   ├── order.js
    │   └── sales.js
    ├── images/           # 圖片資源
    │   └── webcanvas.png
    ├── json/             # JSON數據檔案
    │   └── database.json # 餐廳菜單數據
    ├── BillLastMonth.csv # 上月銷售數據
    └── favicon.ico       # 網站圖標
```

## 💻 系統需求

### 基本需求
- **Python**: 3.8 或更高版本
- **作業系統**: Windows 10+、macOS 10.14+、Ubuntu 18.04+
- **記憶體**: 最少 2GB RAM
- **儲存空間**: 最少 500MB 可用空間

### 必要服務
- **Google Gemini API**: 用於AI聊天機器人功能
- **網路連線**: 用於API調用和外部資源載入

## 🚀 安裝指南

### 1. 複製專案
```bash
git clone https://github.com/tszngaiyip/1122_Web_Final.git
cd 1122_Web_Final
```

### 2. 建立虛擬環境 (建議)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux  
python3 -m venv venv
source venv/bin/activate
```

### 3. 安裝依賴套件
```bash
pip install -r requirements.txt
```

### 4. 設定配置檔案
建立 `config.ini` 檔案 (詳見[設定配置](#設定配置)章節)

### 5. 啟動應用程式
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

# macOS/Linux
export GEMINI_API_KEY=your_api_key_here
export FLASK_ENV=development
```

## 📖 使用說明

### 🏠 首頁功能
1. **歡迎界面**: 展示餐廳資訊和主要功能入口
2. **導航選單**: 快速進入各功能頁面
3. **營業狀態**: 即時顯示餐廳營業狀態

### 🍽️ 點餐流程
1. 點擊「開始點餐」進入點餐頁面
2. 瀏覽不同餐點類別：套餐、麵食、燉飯、漢堡等
3. 選擇心儀餐點加入購物車
4. 查看訂單詳情和總金額
5. 確認訂單並送出

### 🎲 隨機點餐
1. 選擇「隨機點餐」功能
2. 選擇餐點類型或選擇「都可」
3. 系統智能推薦適合的餐點
4. 可重新隨機或直接加入訂單

### 💬 AI聊天機器人
1. 在點餐頁面找到聊天機器人圖示
2. 輸入關於餐點的問題
3. AI會提供智能回答和推薦
4. 支援自然語言對話

### 📈 銷售分析
1. 點擊「銷售報表」查看數據分析
2. 瀏覽互動式圖表
3. 分析不同餐點類型的銷售表現
4. 查看時間趨勢和熱門餐點

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

> 註: 此處可以加入應用程式的實際截圖

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

## 👨‍💻 開發指南

### 開發環境設置

1. **程式碼編輯器**: 推薦使用 VSCode 或 PyCharm
2. **Python 版本管理**: 使用 pyenv 或 conda
3. **版本控制**: Git

### 專案開發流程

1. **分支管理**: 使用 Git Flow 工作流程
2. **程式碼審查**: 提交前進行程式碼檢查
3. **測試**: 確保功能正常運作

### 程式碼風格

- **Python**: 遵循 PEP 8 標準
- **JavaScript**: 使用 ES6+ 語法
- **HTML/CSS**: 保持語義化和響應式設計

### 新增功能

1. 在 `app.py` 中新增路由
2. 建立對應的 HTML 模板
3. 新增必要的 CSS 和 JavaScript
4. 更新 README 文件

## 🤝 貢獻指南

我們歡迎任何形式的貢獻！請遵循以下流程：

### 提交貢獻

1. **Fork** 本專案
2. 建立功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交變更 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 **Pull Request**

### 貢獻類型

- 🐛 錯誤修復
- ✨ 新功能開發
- 📚 文件改善
- 🎨 UI/UX 優化
- ⚡ 效能改善

### 報告問題

如發現問題，請建立 Issue 並包含：
- 問題詳細描述
- 重現步驟
- 預期行為
- 實際行為
- 螢幕截圖 (如適用)

## 📄 授權條款

本專案採用 MIT 授權條款。詳細內容請參考 [LICENSE](LICENSE) 檔案。

```
MIT License

Copyright (c) 2024 卡利西里餐廳訂餐系統

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 聯絡資訊

- **專案維護者**: [您的姓名]
- **電子郵件**: [您的郵箱]
- **專案首頁**: [https://github.com/tszngaiyip/1122_Web_Final](https://github.com/tszngaiyip/1122_Web_Final)

---

<div align="center">

**感謝您使用卡利西里餐廳訂餐系統！** 

如果這個專案對您有幫助，請考慮給我們一個 ⭐

[回到頂部](#-卡利西里餐廳訂餐系統)

</div>