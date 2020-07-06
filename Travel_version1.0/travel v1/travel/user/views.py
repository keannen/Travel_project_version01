from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from strategy.models import Picture,PictureType

# 测试
def test(request):
    return HttpResponse('hahah')

# 测试注册
def test_register(request):
    if request.method == 'GET':
        return render(request,'user/test_register.html')
    elif request.method == 'POST':
        return HttpResponse('post')

# 测试上传
def test_uploadpic(request):

    if request.method == 'GET':
        return render(request,'user/test_uplodepic.html')

    elif request.method == 'POST':
        pic = request.FILES['pic']
        save_path = '%s/startegyImg/%s' %(settings.MEDIA_ROOT,pic.name)
        with open(save_path, 'wb') as f:
            for content in pic.chunks():
                f.write(content)
        p = PictureType.objects.get(id=1)
        Picture.objects.create(picturetype=p,picture_path='startegyImg/%s'%pic.name)

        return render(request,'user/test_uplodepic.html',{'s':pic.name})