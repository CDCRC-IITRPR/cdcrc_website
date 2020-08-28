from .models import PageVisibilityConfig

def get_default_page_visibility_status():
    PAGE_VISIBILITY_SETTINGS_INIT = {
        'pd_about': True, 
        'pd_activities': False,
        'pd_library': False,
        'pd_videos': False,
        'cr_about': True, 
        'cr_activities': False,
        'cr_hod_message': False,
        'pd_hod_message': False,
        'hod_message': False,
    }
    return PAGE_VISIBILITY_SETTINGS_INIT

def get_page_visibility_status(page):
    try:
        pgv = PageVisibilityConfig.objects.get(page=page)
        return pgv.visible
    except:
        return False