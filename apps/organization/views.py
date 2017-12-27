from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render
from django.views.generic import View
from organization.models import CourseOrg, CityDict


class OrgView(View):
    # 课程机构列表功能
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_cities = CityDict.objects.all()

        # 对课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # int 数值为具体每页显示数量
        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_cities': all_cities,
            'org_nums': org_nums
        })
