import librosa
import soundfile as sf
import numpy as np
from pypesq import pesq

# 目标采样率
target_rate = 16000

# 读取音频文件
ref_path = '../test.wav'
deg_path = '../combined.wav'
ref, fs_ref = librosa.load(ref_path, sr=None)  # 使用librosa读取原始采样率
deg, fs_deg = librosa.load(deg_path, sr=None)

# print(f'fs_ref: {fs_ref}')
# print(f'fs_deg: {fs_deg}')

# 确认采样率不一致，需要转换
if fs_ref != target_rate:
    ref = librosa.resample(ref, orig_sr=fs_ref, target_sr=target_rate)
if fs_deg != target_rate:
    deg = librosa.resample(deg, orig_sr=fs_deg, target_sr=target_rate)

# 多声道转单声道（如果需要）
if ref.ndim > 1:
    ref = np.mean(ref, axis=1)
if deg.ndim > 1:
    deg = np.mean(deg, axis=1)

# 截取音频长度使音频等长
min_len = min(len(ref), len(deg))
ref, deg = ref[:min_len], deg[:min_len]

# 确保ref和deg都是一维数组
if ref.ndim > 1:
    ref = ref.flatten()  # 或者使用 ref = np.mean(ref, axis=1) 如果是多声道需要转单声道
if deg.ndim > 1:
    deg = deg.flatten()  # 或者使用 deg = np.mean(deg, axis=1) 如果是多声道需要转单声道

# print(ref)
# print(deg)
# 使用PESQ进行评估，确保使用正确的模式（'nb'：窄带）
pesq_score = pesq(ref, deg, normalize=True)
print("PESQ Score:", pesq_score)
