from config.models import PageVisibilityConfig
from config.utils import get_default_page_visibility_status
def run():
    PAGE_VISIBILITY_SETTINGS_INIT = get_default_page_visibility_status()
    for page, visible in PAGE_VISIBILITY_SETTINGS_INIT.items():
        try:
            pvc = PageVisibilityConfig(page=page, visible=visible)
            pvc.save()
        except:
            print("{} setting already exists".format(page))
