#!/usr/bin/env/python
# -*-coding:utf-8-*-

import pytest

"""
只对函数用例生效，不在类中
setup_function
teardown_function
"""


def setup_module():
    print("setup_module():在模块最之前执行\n")


def teardown_module():
    print("teardown_module：在模块之后执行")


def setup_function():
    print("setup_function():每个方法之前执行")


def teardown_function():
    print("teardown_function():每个方法之后执行")


def test_01():
    print("正在执行test1")
    x = "this"
    assert 'h' in x


def test_02():
    print("正在执行test2")
    x = "hello"
    assert hasattr(x,"hello")


def add(a,b):
    return a+b


def test_add():
    print("正在执行test_add()")
    assert add(3,4) == 7


if __name__ == "__main__":
    pytest.main(["-s", "test_function.py"])
