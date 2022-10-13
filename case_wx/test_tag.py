import pytest
from common.common_requests import CommonHttp


# http://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index
# appID:wx20d87c72dc1e93bf
# appsecret: deeced62d97f6ec9a53db64dd5dd1bf0


# GET https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token=ACCESS_TOKEN
def test_get_ip(get_base_url, get_access_token):
    url_params = {"access_token": get_access_token}
    response = CommonHttp(get_base_url).get("/get_api_domain_ip", url_params=url_params)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200 and "errcode" not in response.json()


# POST（请使用 https 协议） https://api.weixin.qq.com/cgi-bin/tags/create?access_token=ACCESS_TOKEN
def test_add_tag(get_base_url, get_access_token):
    tag = {"tag": {"name": "湖南"}}
    url_params = {"access_token": get_access_token}
    response = CommonHttp(get_base_url).post("/tags/create", url_params=url_params, body=tag)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200 and "errcode" not in response.json()

    test_get_tag_list(get_base_url, get_access_token)

    return response.json()['tag']['id']


# POST（请使用 https 协议） https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=ACCESS_TOKEN
def test_del_tag(get_base_url, get_access_token):
    tag_id = {"tag": {"id": 101}}
    url_params = {"access_token": get_access_token}
    response = CommonHttp(get_base_url).post("/tags/delete", url_params=url_params, body=tag_id)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200 and response.json()["errcode"] == 0


# GET（请使用 https 协议） https://api.weixin.qq.com/cgi-bin/tags/get?access_token=ACCESS_TOKEN
def test_get_tag_list(get_base_url, get_access_token):
    url_params = {"access_token": get_access_token}
    response = CommonHttp(get_base_url).get("/tags/get", url_params=url_params)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200 and "errcode" not in response.json()
