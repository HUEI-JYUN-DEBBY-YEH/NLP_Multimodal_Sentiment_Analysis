import pandas as pd

# 讀入人工標註模板
df = pd.read_csv("D:\\NLP_Multimodal_Sentiment_Analysis\\visual_emotion_output\\annotation_template.csv", encoding="utf-8-sig")

# 清理欄位（避免空白值錯誤）
df.fillna("none", inplace=True)

# 一致性判斷
df["text_match"] = df["text_emotion"] == df["true_text_emotion"]
df["basic_match"] = df["basic_emotion"] == df["true_basic_emotion"]
df["visual_match"] = df["visual_emotion"] == df["true_basic_emotion"]  # 視覺 vs 人類情緒類型比對（也可比對 text）

# 統計分析
total = len(df)
text_acc = df["text_match"].mean()
basic_acc = df["basic_match"].mean()
visual_acc = df["visual_match"].mean()

# 輸出比對結果表格
df.to_csv("D:\\NLP_Multimodal_Sentiment_Analysis\\visual_emotion_output\\evaluation_result.csv", index=False, encoding="utf-8-sig")
print("✅ 已產出逐句評估表：evaluation_result.csv")

# 顯示總結統計
print("\n📊 標註 vs 預測一致性統計：")
print(f"🗣️ 語音情緒一致率：{text_acc:.2%}")
print(f"💬 語意類型一致率：{basic_acc:.2%}")
print(f"🧍‍♀️ 視覺表情一致率：{visual_acc:.2%}")
