#tests/test_count_words.py
from src.count_words import count_word

def test_demo():
    num = count_word("week01/demo.txt")
    assert num == 6
    print("测试通过")

if __name__ == "__main__":
    test_demo()
