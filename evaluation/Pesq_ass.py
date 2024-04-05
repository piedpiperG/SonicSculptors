from pesq import pesq
import soundfile as sf

# 读取参考语音和被评估语音
rate, ref_data = sf.read('../test.wav')  # 这里rate应该是一个整数，ref_data应该是一个NumPy数组
_, deg_data = sf.read('../combine.wav')  # 这里只关心音频数据

# 如果音频是立体声的，只取第一个通道
if ref_data.ndim > 1:
    ref_data = ref_data[:, 0]
if deg_data.ndim > 1:
    deg_data = deg_data[:, 0]

# 计算并打印PESQ分数
score = pesq(rate, ref_data, deg_data, 'wb')
print(f'PESQ score: {score}')
