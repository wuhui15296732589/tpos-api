from common import common_public
import  requests,json,os
import logging
import logging.config
import cx_Oracle
from common import commonORBD

CON_LOG='../testFile/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


class Customer_register():
    def __init__(self,mobile,code,password,aginpassword):
        self.mobile = mobile

    def code(self):
        '''
        注册获取验证码
        :return:

        '''

        url= common_public.URL() +'api_002'
        data1 = {"HEAD":common_public.App_head(),
                "BODY":{"type":"1","mobile":self.mobile}}
        logging.info('请求地址：'+url+','+'请求参数：'+data1)
        data = json.dumps(data1)
        respons = requests.post(url = url , data = data)
        result = respons.json()
        assert result['HEAD']['MSG'] =='操作成功'
        logging.info('---------------------end------------验证码获取成功---------------------')



    def register(self):
        '''
        手机号注册商户
        :return:
        '''
        logging.info('---------------------start:手机号注册商户-------------------------')
        url = common_public.URL() + 'api_001'
        data1 = {"HEAD":common_public.App_head(),
                 "BODY":{"code":"6666","password":"123456","mobile":self.mobile,
                         "firPassword":"123456","type":"1","accountType":"1"}}
        logging.info('请求地址：'+url)
        logging.info('请求参数：'+data1)
        data = json.dumps(data1)
        respons = requests.post(url= url,data = data)
        assert respons.status_code ==200
        logging.info('-----------------end:手机号注册成功----------------------------------')
