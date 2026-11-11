###写Python工具代码--简单统计文本单词数
# src/count_words.py
import sys

def count_word(file_path):
    """统计文件单词数量"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    return len(words)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python src/count_words.py 文本文件路径")
        sys.exit(1)
    path = sys.argv[1]
    res = count_word(path)
    print(f"单词总数：{res}")