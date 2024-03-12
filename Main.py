import subprocess

# 定义你的命令
cmd1 = 'python seperate.py'

cmd2 = 'python svc_inference.py --config configs/base.yaml --model sovits5.0.pth --spk ./data_svc/singer/speaker0.spk.npy --wave ./seperate/output/test/vocals.wav --shift 0'

cmd3 = 'python combination.py'

# 执行第一个命令
subprocess.run(cmd1, shell=True)

# 执行第二个命令
subprocess.run(cmd2, shell=True)

# 执行第三个命令
subprocess.run(cmd3, shell=True)

