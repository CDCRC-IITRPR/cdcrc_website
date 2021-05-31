import os


def get_current_site_from_env():
    # fetching the url from env variables
    url=os.environ.get('CURRENT_SITE').replace('"', '')
    # checking if the end is having slash
    if url[-1]=='/':
        return url[0:-1]

    return url

    