#!/usr/bin/env python
# coding=utf-8
import pytest
import allure
import os

@pytest.fixture(scope='function')
def login():
    print("登录")
    yield
    print("登录完成")

@allure.feature('加入购物车')
def test_1(login):
    '''将苹果加入购物车'''
    print("测试用例1")

@allure.feature('加入购物车')
def test_2():
    '''将橘子加入购物车'''
    print("测试用例2")

if __name__ =="__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './temp'])
    # 直接写allure报错了呢
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('/Users/zhaocuixia/Downloads/allure-2.14.0/bin/allure generate ./temp -o ./report --clean')
    os.system('/Users/zhaocuixia/Downloads/allure-2.14.0/bin/allure open ./report')