# Pixel Heroes - NFT Collection Generator

一個基於 Python 的 NFT（非同質化代幣）生成器，用於創建 16 位元像素風格的 RPG 角色，具有各種特徵和屬性。此項目包含生成 NFT 元數據、使用 AI 創建圖像以及將元數據編譯為 CSV 格式的工具。

## 功能特點

- 生成獨特的 NFT 特徵和元數據
- 基於元數據使用 AI 創建圖像
- 將元數據編譯為 CSV 格式以便於分析
- 支持各種角色屬性：
  - 基本角色類型（戰士、法師、公主等）
  - 髮色
  - 眼睛
  - 表情
  - 背景
  - 特殊效果
  - 裝備
  - RPG 屬性（等級、HP、MP、力量、智力、敏捷、幸運）
- 多種像素藝術風格可選

## 項目結構

```
pfp_generator/
├── main.py                      # 原始主腳本
├── simplified_main.py          # 基於配置的簡化主腳本
├── config.py                   # 提示詞和特徵的集中配置
├── nft_traits.py               # 原始 NFT 特徵生成邏輯
├── simplified_trait_generator.py # 基於配置的簡化特徵生成器
├── generate_pfp.py             # 使用 Stability AI 的 AI 圖像生成
├── generate_nft_images.py      # 原始基於元數據的 NFT 圖像生成
├── simplified_image_generator.py # 基於配置的簡化圖像生成器
├── compile_metadata_csv.py     # 元數據 CSV 編譯器
├── metadata/                   # 生成的 NFT 元數據 JSON 文件
├── nft_images/                # 生成的 NFT 圖像
└── metadata_csv/              # 編譯的元數據 CSV 文件
```

## 系統要求

- Python 3.x
- 所需 Python 套件：
  - requests
  - Pillow
  - pandas
  - python-dotenv

## 使用方法

### 設置環境變量

在運行之前，請確保在 `.env` 文件中設置了 Stability AI API 密鑰：
```
STABILITY_API_KEY=your_stability_ai_api_key_here
```

### 原始流程

運行原始流程：
```bash
python3 main.py
```

### 簡化流程（基於配置）

1. 使用默認設置運行簡化流程：
```bash
python3 simplified_main.py
```

2. 使用特定風格和數量運行：
```bash
python3 simplified_main.py --style tiny_sprite --count 5 --start-id 1
```

可用風格：
- `pixel_rpg`：經典 16 位元 RPG 風格角色
- `tiny_sprite`：微小的 16x16 像素精靈
- `chibi`：可愛的 chibi 角色（大頭小身體）

這將：
- 生成 NFT 特徵和元數據
- 創建 NFT 圖像
- 將元數據編譯為 CSV 格式

## 輸出結果

生成器創建三個主要目錄：

1. `metadata/`：包含每個 NFT 的個別 JSON 文件，包含其特徵和屬性
2. `nft_images/`：包含生成的 NFT 圖像
3. `metadata_csv/`：包含編譯的元數據 CSV 格式文件

## 元數據格式

每個 NFT 包括：
- 名稱
- 描述
- 圖像 URL
- 屬性：
  - 基本特徵（角色類型如戰士、法師等）
  - 角色名稱
  - 視覺特徵（髮色、眼睛、表情）
  - 特殊特徵（背景、效果）
  - 特定於角色類型的多件裝備
  - RPG 角色屬性（等級、HP、MP 等）

## 自定義設置

此項目設計為易於自定義：

1. 編輯 `config.py` 以修改：
   - 不同藝術風格的基本提示詞
   - 角色類型及其特徵
   - 適用於所有角色的通用特徵
   - RPG 屬性及其範圍
   - 描述模板

2. 通過更新 `config.py` 中的字典來添加新的角色類型或特徵

3. 通過在 `BASE_PROMPTS` 字典中添加條目來創建新的藝術風格

## 範例配置

```python
# 在 config.py 中添加新的藝術風格
BASE_PROMPTS = {
    "new_style": {
        "prompt": "新風格的基本提示詞...",
        "negative_prompt": "要避免的元素..."
    },
    # 其他現有風格...
}

# 添加新的角色類型
CHARACTER_TYPES["Bard"] = {
    "description": "talented musician with small lute",
    "special_trait": "Sings songs that inspire allies in battle.",
    "outfit": ["Lute", "Colorful Hat", "Fancy Clothes", "Boots"]
}
```

## 授權條款

[MIT License](LICENSE)
