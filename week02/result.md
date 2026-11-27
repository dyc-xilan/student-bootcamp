## Flan-T5-small 实验结果总结
# 选择该模型的原因：
flan-t5-small是经过指令微调的轻量文本生成模型，支持CPU本地运行，适配问答、翻译、摘要等多种文本到文本任务，适合本次实验。

# 受控对照实验说明
固定条件：model_id=google/flan-t5-small，revision固定，seed=42，输入prompt不变，max_new_tokens=64不变
唯一变量：do_sample
A（基准）：do_sample=False，贪心解码，输出稳定可复现
B（对照）：do_sample=True，开启采样，引入随机性，相同输入多次运行结果可能不一样

# 三组正常样例
1. 输入1：What is machine learning?
【基准 do_sample=False】输出： machine learning
【对照 do_sample=True】输出： machine learning () is a technique used in machine science to identify and formulate patterns of behaviour. This concept is also recognized as a subject of attention to detail and knowledge.

2. 输入2：Explain what is AI in one sentence.
【基准 do_sample=False】输出： AI (human) is a cellular phone used to communicate with other humans.
【对照 do_sample=True】输出： AI is a computer model used to compute data and calculate the size of a frame, thus measuring the size of an AI.

3. 输入3：Summarize: Apples are red and grow on trees.
【基准 do_sample=False】输出： Leave the apple in the tree for a few days.
【对照 do_sample=True】输出： Place an apple in the pear grate and lay it on the tree.

# 失败样例
输入4（失败样例）： aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...
【基准 do_sample=False】输出： Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
【对照 do_sample=True】输出： Ana aamaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa asaaaaa

# 失败分析：
当输入是没有语义的重复乱码时，flan-t5-small无法有效识别任务意图，对于基准组（do_sample=False），模型直接复述输入的乱码；对于对照组（do_sample=True），模型没有识别出输入无效，强行生成了无依据的文本，属于模型幻觉。

# 模型不适用场景
不适合要高精度数学推导、严谨公式计算、强事实校验的科研计算场景，容易产生错误的幻觉内容。

## 可追溯信息
model_id: google/flan-t5-small
revision: 0fc9ddf78a1e988dac52e2dac162b0ede4fd74ab
seed: 42
device: CPU
transformers版本：5.23.0
torch版本：2.15.0+cpu
