from django.contrib import admin

# Register your models here.
from django.contrib import admin
from account.models import User

admin.site.register(User)









































# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('id','email', 'name', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         ('User Credentials', {'fields': ('email', 'password',)}),
#         ('Personal info', {'fields': ('name','like',' save_retaturant',)}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password', 'like',' save_retaturant',),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


# Now register the new UserAdmin...
