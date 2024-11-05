# ---
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: init_project.py
# @Author: sunbcy
# @Institution: SYLG University, ShenZhen, China
# @E-mail: saintbcy@163.com
# @Time: 11月 05, 2024 17:45
# ---
import os
from api.utils import get_os_type
from api.utils import get_local_ip


if __name__ == "__main__":
    os_type = get_os_type()
    print(f"当前系统是 {os_type}")

    current_local_ip = get_local_ip()  # 获取当前局域网IP
    print(current_local_ip)

    # 项目指定路径下创建初始文件夹供功能使用
    # if 'logs' not in os.listdir(os.path.abspath('api')):  # 直接写IP
    #     os.mkdir(os.path.join(os.path.abspath('api/logs')))
    #
    # if 'CodeRepo' not in os.listdir(os.path.abspath('api')):  # 直接写IP
    #     os.mkdir(os.path.join(os.path.abspath('api/CodeRepo')))

    # 全局配置保存在项目根目录. backend_config.yaml  <-- os_type/current_local_ip