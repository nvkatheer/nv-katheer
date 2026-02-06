from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),       # root → login
    path("login/", views.login_view, name="login"), # login page
    path("logout/", views.logout_view, name="logout"), # logout
    path("dashboard/", views.dashboard, name="dashboard"), # dashboard page
    path("report/", views.report, name="report"), # report page
    path("feed/", views.feed, name="feed"), # feed page
    path("katheer/", views.katheer, name="katheer"), # katheer page (katheer)
    path("fetch-record-katheer/", views.fetch_record_katheer, name="fetch_record_katheer"),
    path("dashboard-data/", views.dashboard_data, name="dashboard_data"),
    path("report-data/", views.report_data, name="report_data"), # report data endpoint
    path("download-excel/", views.download_excel, name="download_excel"), # excel download endpoint
    path("add-user/", views.add_user, name="add_user"),
    path("get-user/<int:user_id>/", views.get_user, name="get_user"),
    path("females/", views.females, name="females"),  # Make sure the name matches exactly
    path("males/", views.males, name="males"),
    path("eggout/", views.eggout, name="eggout"),
    # Feed Stock URLs
    path("feed-stock-save/", views.feed_stock_save, name="feed_stock_save"),
    path("feed-stock-list/", views.feed_stock_list, name="feed_stock_list"),
    path("feed-stock-get/<int:feed_stock_id>/", views.feed_stock_get, name="feed_stock_get"),
    path("feed-stock-delete/<int:feed_stock_id>/", views.feed_stock_delete, name="feed_stock_delete"),
    path("feed-stock-dashboard/", views.feed_stock_dashboard, name="feed_stock_dashboard"),
    path("feed-stock-report-data/", views.feed_stock_report_data, name="feed_stock_report_data"),
    path("feed-stock-download-excel/", views.feed_stock_download_excel, name="feed_stock_download_excel"),
    # Male Birds Stock URLs
    path("male-birds-stock-save/", views.male_birds_stock_save, name="male_birds_stock_save"),
    path("male-birds-stock-list/", views.male_birds_stock_list, name="male_birds_stock_list"),
    path("male-birds-stock-get/<int:stock_id>/", views.male_birds_stock_get, name="male_birds_stock_get"),
    path("male-birds-stock-delete/<int:stock_id>/", views.male_birds_stock_delete, name="male_birds_stock_delete"),
    # Male Birds Mortality URLs
    path("male-birds-mortality-save/", views.male_birds_mortality_save, name="male_birds_mortality_save"),
    path("male-birds-mortality-list/", views.male_birds_mortality_list, name="male_birds_mortality_list"),
    path("male-birds-mortality-get/<int:mortality_id>/", views.male_birds_mortality_get, name="male_birds_mortality_get"),
    path("male-birds-mortality-delete/<int:mortality_id>/", views.male_birds_mortality_delete, name="male_birds_mortality_delete"),
    # Male Birds Dashboard & Report URLs
    path("male-birds-dashboard/", views.male_birds_dashboard, name="male_birds_dashboard"),
    path("male-birds-report-data/", views.male_birds_report_data, name="male_birds_report_data"),
    path("male-birds-download-excel/", views.male_birds_download_excel, name="male_birds_download_excel"),

    # Female Birds Stock URLs
    path("female-birds-stock-save/", views.female_birds_stock_save, name="female_birds_stock_save"),
    path("female-birds-stock-list/", views.female_birds_stock_list, name="female_birds_stock_list"),
    path("female-birds-stock-get/<int:stock_id>/", views.female_birds_stock_get, name="female_birds_stock_get"),
    path("female-birds-stock-delete/<int:stock_id>/", views.female_birds_stock_delete, name="female_birds_stock_delete"),
    # Female Birds Mortality URLs
    path("female-birds-mortality-save/", views.female_birds_mortality_save, name="female_birds_mortality_save"),
    path("female-birds-mortality-list/", views.female_birds_mortality_list, name="female_birds_mortality_list"),
    path("female-birds-mortality-get/<int:mortality_id>/", views.female_birds_mortality_get, name="female_birds_mortality_get"),
    path("female-birds-mortality-delete/<int:mortality_id>/", views.female_birds_mortality_delete, name="female_birds_mortality_delete"),
    # Female Birds Dashboard & Report URLs
    path("female-birds-dashboard/", views.female_birds_dashboard, name="female_birds_dashboard"),
    path("female-birds-report-data/", views.female_birds_report_data, name="female_birds_report_data"),
    path("female-birds-download-excel/", views.female_birds_download_excel, name="female_birds_download_excel"),
    
    # Egg Out URLs
    path("eggout-save/", views.eggout_save, name="eggout_save"),
    path("eggout-list/", views.eggout_list, name="eggout_list"),
    path("eggout-get/<int:eggout_id>/", views.eggout_get, name="eggout_get"),
    path("eggout-delete/<int:eggout_id>/", views.eggout_delete, name="eggout_delete"),
    path("eggout-dashboard/", views.eggout_dashboard, name="eggout_dashboard"),
    path("eggout-download-excel/", views.eggout_download_excel, name="eggout_download_excel"),

    # Backup & Restore URLs
    path("export-backup/", views.export_backup, name="export_backup"),
    path("import-backup/", views.import_backup, name="import_backup"),

    path("backup/", views.backup, name="backup"),
]
