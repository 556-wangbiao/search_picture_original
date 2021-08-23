# coding:utf-8
from setuptools import setup
setup(
    name='vic',  # 包名字
    version='1.0',  # 包版本
    description='学习打包',  # 简单描述
    author='vic',  # 作者
    author_email='vic@163.com',  # 作者邮箱
    url='https://www.vic.com',  # 包的主页
    packages=['vic_pkg','tests'],  # 包
    package_data={'vic_pkg': ['*.ini']} # 打包的数据文件
)

from  distutils.core import setup
setup(name='小楼的计算器',  # 程序名称
      version='1.0',  # 程序版本号
      description='一个萌萌的计算器。',  # 程序描述
      author='小楼一夜听春语',  # 程序作者
      py_modules=['calculator'],  # 包含的模块列表
      packages=['other_module'] , # 包含的包列表
      )