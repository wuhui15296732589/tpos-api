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
        ע���ȡ��֤��
        :return:

        '''

        url= common_public.URL() +'api_002'
        data1 = {"HEAD":common_public.App_head(),
                "BODY":{"type":"1","mobile":self.mobile}}
        logging.info('�����ַ��'+url+','+'���������'+data1)
        data = json.dumps(data1)
        respons = requests.post(url = url , data = data)
        result = respons.json()
        assert result['HEAD']['MSG'] =='�����ɹ�'
        logging.info('---------------------end------------��֤���ȡ�ɹ�---------------------')



    def register(self):
        '''
        �ֻ���ע���̻�
        :return:
        '''
        logging.info('---------------------start:�ֻ���ע���̻�-------------------------')
        url = common_public.URL() + 'api_001'
        data1 = {"HEAD":common_public.App_head(),
                 "BODY":{"code":"6666","password":"123456","mobile":self.mobile,
                         "firPassword":"123456","type":"1","accountType":"1"}}
        logging.info('�����ַ��'+url)
        logging.info('���������'+data1)
        data = json.dumps(data1)
        respons = requests.post(url= url,data = data)
        assert respons.status_code ==200
        logging.info('-----------------end:�ֻ���ע��ɹ�----------------------------------')
