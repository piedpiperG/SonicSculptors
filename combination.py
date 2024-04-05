from pydub import AudioSegment

# 加载第一个音频文件
audio1 = AudioSegment.from_file("svc_out.wav")

# 加载第二个音频文件
audio2 = AudioSegment.from_file("seperate/output/test/accompaniment.wav")

# 将两个音频文件在同一时间叠加
combined = audio1.overlay(audio2)

# 导出合并后的音频文件
combined.export("./tinker/result/combined.wav", format="wav")
