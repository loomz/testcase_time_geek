# http://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index
# appID:wx20d87c72dc1e93bf
# appsecret: deeced62d97f6ec9a53db64dd5dd1bf0

import pytest
from common.common_read_file import CommonReadFile
from common.common_requests import CommonHttp

comm = CommonHttp('https://api.weixin.qq.com/cgi-bin')


def setup():
    print('程序开始了')
    # 实例化自己的common


@pytest.mark.skip
def test_access_toke(grant_type, appid, appsecret):
    print("grant_type=%s ,appid=%s ,appsecret=%s" % (grant_type, appid,appsecret))
    toke_url = '/token?'
    data = {'grant_type': grant_type, 'appid': appid, 'appsecret': appsecret}
    response_login = comm.get(toke_url, params=data)
