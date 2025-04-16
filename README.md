This project explores multimodal sentiment analysis by combining textual and visual data. It employs natural language processing techniques alongside image processing to assess sentiment, demonstrating the integration of multiple data modalities for comprehensive sentiment evaluation.​

# 🎭 Multimodal Emotion Analyzer for Mandarin Workplace Videos

本專案建立一套結合語音語意與視覺模態的情緒分析系統，針對台灣職場語境影片進行逐秒級情緒預測與人工對照。專案涵蓋 WhisperX 語音對齊、RoBERTa 語意情緒分析、DeepFace 視覺辨識，以及時間軸融合、人工標註與精華片段整理。

---

## 🔖 Why this project matters：

This project integrates speech, text, and facial emotion data to analyze workplace sentiment over time.
It showcases how multimodal AI can interpret nuanced human expression and support more empathetic, insight-driven environments—especially in organizational settings.

---

## 🚀 專案亮點

- 🎥 使用 YouTube 職場講座影片作為真實資料來源
- 🔊 WhisperX 實現語音逐字時間對齊
- 🧠 中文 RoBERTa 模型進行情緒詞判斷
- 🧍 DeepFace 擷取畫面中人臉表情情緒
- 🧩 多模態融合成 per-second `merged_timegrid.csv` 統一結構
- 📈 可視化時間軸折線圖、標註對照與高變化片段摘要

---

## 🧠 系統架構圖

![Multimodal Pipeline](./multimodal_emotion_pipeline_clean.png)

![Architecture Diagram](./multimodal_sentiment_analysis.png)

---

## 📘 Modalities & Tools

- Text: WhisperX for speech-to-text → RoBERTa sentiment classifier (Hugging Face)
- Visual: DeepFace + YOLO-Face for expression recognition
- Labeling: Manual 6-class sentiment annotation per video segment
- Visualization: Matplotlib + Timeline Sync
  
---

## 📊 模型輸出對照分析（Multimodal Emotion Evaluation）

本專案最終階段進行了語音、語意、視覺三模態的機器判讀結果與人工標註的比對分析，涵蓋以下兩個層次：

### 🎯 模型輸出對照（人工 vs 機器）

| 模型欄位 | 說明 |
|----------|------|
| `text_emotion` | 語音模態預測的情緒傾向（正面／中性／負面） |
| `basic_emotion` | 語意中出現的情緒詞所映射的基本情緒（如 joy, anger） |
| `visual_emotion` | DeepFace 對畫面中人臉的表情判定（如 sad, happy） |

| 標註欄位 | 說明 |
|----------|------|
| `true_text_emotion` | 人工主觀判定的語氣傾向 |
| `true_basic_emotion` | 人工判定之語意表情類型 |
| `remark` | 額外補充說明，如模態不一致、情緒轉折段落等 |

📌 以下為代表性片段對照：

| second | text_emotion | basic_emotion | visual_emotion | true_text_emotion | true_basic_emotion |
|--------|--------------|----------------|----------------|-------------------|--------------------|
| 7      | 未知         | none           | error          | 中性              | none               |
| 23     | 正面         | joy            | neutral        | 負面              | sadness            |
| 42     | 中性         | none           | happy          | 正面              | joy                |

---

### 📈 模型一致率統計

| 項目 | 一致率 |
|------|--------|
| 🗣️ 語音情緒一致率（text_emotion） | **0.00%** |
| 💬 語意類型一致率（basic_emotion） | **35.00%** |
| 🧍‍♀️ 視覺表情一致率（visual_emotion） | **0.00%** |

---

### 🧠 標註樣本概況與 Joy 類分析

- 標註樣本總數：40 句
- 其中明確標註為 `joy`（快樂情緒）：26 句
- 其他標記為 `none`（無明顯情緒）

| 標註為 joy 的句數 | 模型預測為 joy | 預測錯誤 |
|------------------|----------------|------------|
| 26               | 18             | 8          |

🎯 `joy` 類別預測準確率：**69.2%**

---

### 🔍 小結與觀察

- 多數職場片段為中性敘事語氣，模態間一致性偏低
- 模型在 `joy` 上有較佳表現，預測準確率近七成
- 視覺模態易受畫面品質與臉部角度影響
- 可延伸為多模態強化學習與人機互動應用基礎

---

## 🎬 精華片段與情緒高變區段摘要

📄 [點我查看情緒高變段摘要](./emotion_highlight_summary.md)

---

## 📁 專案結構與輸出檔案說明

- `cut_xxx/merged_timegrid.csv`：每部影片的多模態時間軸資料
- `*_emotion_timeline_zh.png`：每秒基本情緒變化圖
- `evaluation_result.csv`：人工標註對照表格
- `analysis_report.md`：模型與人工一致性分析報告

---

## 📌 授權與延伸應用

- 本專案資料來源為公開 YouTube 職場演講影片（具教育、分析用途）
- 模型皆採自 Hugging Face 預訓練模型（MIT / Open License）
- 適用於教育影片情緒回饋、人機互動情緒辨識、職場演講訓練輔助等應用場景

---

## 🔗 Related Links
- 📝 [Medium post: A Multimodal Approach to Workplace Emotion](https://medium.com/@debby.yeh1994)
- 📂 [Project portfolio summary](https://mango-mapusaurus-5df.notion.site/Debby-Yeh-NLP-Application-Engineer-Portfolio-1ca5118474d2801caa58de564fb53e38?pvs=4)
