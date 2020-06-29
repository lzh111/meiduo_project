from django.core.files.storage import Storage
from django.conf import settings

from fdfs_client.client import Fdfs_client
from rest_framework.exceptions import APIException


class FDFSStorage(Storage):
    """FDFS自定义文件存储类"""
    def __init__(self, client_conf=None, base_url=None):
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF

        # 保存客户端配置文件路径
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_URL

        # 保存的就是FDFS nginx的地址
        self.base_url = base_url

    def _save(self, name, content):
        """
        name: 上传文件的名称
        content: 包含上传文件内容的File对象，content.read()获取上传文件内容
        """
        # 创建FDFS客户端对象
        client = Fdfs_client(self.client_conf)

        # 上传文件到FDFS系统
        res = client.upload_by_buffer(content.read())

        if res.get('Status') != 'Upload successed.':
            raise APIException('上传文件到FDFS系统失败')

        # 获取文件的id
        file_id = res.get('Remote file_id')
        return file_id

    def exists(self, name):
        """
        判断上传文件的名称和文件系统中原有的文件名是否冲突
        name: 上传文件的名称
        """
        return False

    def url(self, name):
        """返回可访问到文件系统中文件的完整的url地址"""
        return self.base_url + name
