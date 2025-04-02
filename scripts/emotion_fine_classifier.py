import os
import pandas as pd
import jieba

# ✅ 建立六類情緒對應詞彙庫
emotion_dict = {
    "joy": ["開心", "快樂", "喜歡", "感動", "幸福", "讚", "棒", "興奮", "感激"],
    "anger": ["生氣", "火大", "憤怒", "氣死", "暴怒", "不爽", "惱火"],
    "sadness": ["難過", "悲傷", "失落", "心碎", "絕望", "想哭"],
    "fear": ["害怕", "恐懼", "擔心", "緊張", "不安", "慌張"],
    "disgust": ["噁心", "反感", "厭惡", "無言", "嘔", "煩"],
    "surprise": ["驚訝", "沒想到", "居然", "天啊", "哇", "意外"]
}

# ✅ 分析句子中情緒詞
def detect_emotion(text):
    word_list = jieba.lcut(text)
    scores = {emo: 0 for emo in emotion_dict}

    for emo, keywords in emotion_dict.items():
        for word in word_list:
            if word in keywords:
                scores[emo] += 1

    # 若無情緒詞，回傳空
    if max(scores.values()) == 0:
        return "none"

    # 回傳出現次數最多的情緒類別
    return max(scores, key=scores.get)

# ✅ 處理所有情緒CSV檔案
folder = "D:\\NLP_Multimodal_Sentiment_Analysis"
csv_files = [f for f in os.listdir(folder) if f.startswith("emotion_cut_") and f.endswith("_roberta3.csv")]

for file in csv_files:
    path = os.path.join(folder, file)
    df = pd.read_csv(path, encoding="utf-8-sig")

    # ✅ 加入細分類欄位
    df["basic_emotion"] = df["text"].apply(detect_emotion)

    # ✅ 輸出新檔
    out_path = path.replace("_roberta3.csv", "_roberta3_fine.csv")
    df.to_csv(out_path, index=False, encoding="utf-8-sig")
    print(f"✅ 完成細分類標註：{out_path}")
