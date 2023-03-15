import os

# 定义存储文件的路径
file_path = 'ip_addresses.txt'

# 判断文件是否存在，如果不存在则创建
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write('')

# 读取已经存在的IP地址信息
with open(file_path, 'r') as f:
    ip_addresses = f.read().splitlines()

# 获取用户输入的IP地址信息
ip_address_a = input('请输入IP地址a：')
ip_address_b = input('请输入IP地址b：')

# 判断IP地址a是否存在
if ip_address_a in ip_addresses:
    # 如果存在，则判断IP地址b是否和已存在的记录相同
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith(ip_address_a):
                if line.rstrip().split(',')[1] == ip_address_b:
                    print('已有相同记录，可以通过')
                else:
                    print('已有不同的用户使用该IP，请驳回！')
                break
else:
    # 如果不存在，则添加新的记录到文件中
    with open(file_path, 'a') as f:
        f.write(f'{ip_address_a},{ip_address_b}\n')
    print('该IP为首次使用，请放心审核。')
