import pytest
from common.common_requests import  CommonHttp


base_url = "https://api.weixin.qq.com/cgi-bin"
appid = "wx20d87c72dc1e93bf"
appsecret = "deeced62d97f6ec9a53db64dd5dd1bf0"


@pytest.fixture(scope="session", autouse=True)
def get_base_url():
    return base_url


# GET https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
@pytest.fixture(scope="session", autouse=True)
def get_access_token(get_base_url):
    url_params = {"grant_type": "client_credential", "appid": appid, "secret": appsecret}
    response = CommonHttp(get_base_url).get("/token", url_params=url_params)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200 and "access_token" in response.json()
    return response.json()['access_token']
