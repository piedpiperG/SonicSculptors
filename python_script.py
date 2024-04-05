import sys


def save_data(option, file_data):
    """
    保存接收到的文件数据到本地文件中。

    :param option: 处理选项
    :param file_data: 要保存的文件数据
    """
    # 根据选项处理数据，这里仅作演示，不做实际处理
    print(f"处理选项：{option}")

    # 将数据写入文件
    with open("output.txt", "w") as file:
        file.write(option)
        file.write(file_data)

    print("文件数据已保存到 output.txt")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("错误：本脚本需要两个参数。")
    else:
        # 获取命令行参数
        option = sys.argv[1]
        file_data = sys.argv[2]

        # 调用函数保存数据
        save_data(option, file_data)
