import pytest
import random


def add(x):
    return x + 2


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # 失败重试，需安装pytest-rerunfailures
def test_addnew(self):
    print('3')
    assert add(2) == 5


#  有输出报告形式
if __name__ == "__main__":
    # pytest.main(["-s", "--html=report.html", "test_param.py"])
    pytest.main(["-s", "test_html.py"])
