#!/usr/bin/python3

from src.framework.src.apifuncs import CompanyManageFuncs
from src.framework.src.helper import CompanyManageCaseHelper

"""
公司管理测试用例
"""


def test_create_company():
    """
    创建公司测试用例
    :return:
    """

    # 获取地址id
    address_id = CompanyManageCaseHelper.get_address_id("苏州")
    # 测试创建公司的数据
    data = {
        "code": "0004",
        "name": "公司0004",
        "address_id": address_id
    }
    # 调用接口
    result = CompanyManageFuncs.create_company(data)
    # 断言
    assert result == 10004
    # todo 不知道数据库在什么场景用，这里就可以用呀, 可以查一下数据库，看数据有没有正确的存储进去


def test_company_detail():
    """
    修改公司测试用例
    :return:
    """

    # 调用接口
    result = CompanyManageFuncs.company_detail(10003)
    # 断言
    assert result["name"] == "公司0003"
