# 设置Django运行所依赖的环境变量
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meiduo_mall.settings.dev')

# 让Django进行一次初始化
import django
django.setup()

from goods.models import SKUImage
from django.core.files import File

if __name__ == "__main__":
    file = open('/Users/smart/Desktop/images/1.jpg', 'rb')
    image = File(file)

    # SKUImage.objects.create(sku_id=1, image=image)

    sku_image = SKUImage.objects.get(id=44)
    sku_image.image = image
    sku_image.save()