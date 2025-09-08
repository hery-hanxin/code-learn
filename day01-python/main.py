# -*- coding: utf-8 -*-
# 试试给文本贴"标签"
import sys

# 在部分 Windows 终端上，打印中文可能因编码为 GBK 报 UnicodeEncodeError
# 这里强制将 stdout/stderr 切换为 UTF-8，保证中文正常输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
sample_text = "Hello world! How are you? I'm fine."
print("原始文本：", sample_text)

# 试试统计基本信息
text_length = len(sample_text)

print("文本总长度：", text_length)

# 把文本分割成单词列表，去除标点符号
import string
clean_text = sample_text.translate(str.maketrans('', '', string.punctuation))
words = clean_text.split()
print("单词列表：", words)
print("单词个数：", len(words))

# 创建空的计数字典
word_count = {}

# 处理每个单词
for word in words:
    word_lower = word.lower()
    if word_lower in word_count:
        word_count[word_lower] = word_count[word_lower] + 1
    else:
        word_count[word_lower] = 1

print("词频统计结果：", word_count)



