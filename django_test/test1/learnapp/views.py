from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView, CreateView
from django.http import HttpResponse

from learnapp.models import Article, Reporter

# Create your views here.

class Test(View):
    '''
    测试正向查询,反向查询,链式查询,在查询中进行字符串的操作,
    '''
    def get(self,request):
        #正向查询  获取到莫言之无言的作者名字
        # headline = '莫言之无言'
        # a = Article.objects.get(headline=headline)
        # full_name = a.reporter
        # return HttpResponse(full_name)   # 莫言

        # 反向查询  获取到莫言的所有书籍
        # full_name = '莫言'
        # r = Reporter.objects.get(full_name = full_name)
        # rlist = r.article_set.all()
        # return HttpResponse(rlist)   # 莫言之无言莫言之言而无信莫言之诺贝尔文学奖获得者

        # 链式查询和在查询中进行字符串的操作   查询出作者名字开头为鲁字的所有书籍
        # a = Article.objects.filter(reporter__full_name__startswith = '鲁')
        # return HttpResponse(a)   # 鲁迅之狂人日记鲁迅之百草园鲁迅之闰土
        pass