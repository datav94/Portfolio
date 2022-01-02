from django.contrib import admin
from app_portfolio_landing.data_models.portfolio import Portfolio
# Register your models here.

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['field_block', 'text_data', 'file_path' ,'url_link', 'date_uploaded', 'active']