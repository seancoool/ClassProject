import xadmin
from apps.organizations.models import City, Teacher, Organization


class TeacherAdmin(object):
    list_display = ['organization', 'name', 'work_year', 'work_company']
    search_fields = ['organization__name', 'name', 'work_year', 'work_company']
    list_filter = ['organization__name', 'name', 'work_year', 'work_company']


class OrganizationAdmin(object):
    list_display = ['name', 'description', 'click_num', 'fav_num']
    search_fields = ['name', 'description', 'click_num', 'fav_num']
    list_filter = ['name', 'description', 'click_num', 'fav_num']


class CityAdmin(object):
    list_display = ["id", "name", 'description']
    search_fields = ["name", "description"]
    list_filter = ["name", "description", "create_time"]
    list_editable = ["name", "description"]


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(Organization, OrganizationAdmin)
xadmin.site.register(City, CityAdmin)