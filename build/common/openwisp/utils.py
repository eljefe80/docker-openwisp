# Utility functions for django modules
# that are used in multiple openwisp modules
import logging
import socket
import os


class HostFilter(logging.Filter):
    # Used in logging for printing hostname
    # of the container with log details
    def filter(self, record):
        record.host = socket.gethostname()
        return True


def env_bool(env):
    return env in ["True", "true", "TRUE"]


def request_scheme():
    if os.environ['SSL_CERT_MODE'] in ["No", "no", "NO"]:
        return 'http'
    return 'https'


def openwisp_controller_urls():
    # Setting correct urlpatterns for the
    # modules -- used in urls.py
    from openwisp_controller.urls import urlpatterns as controller_urls

    exclude = ["openwisp_users.accounts.urls"]
    for url in controller_urls[:]:
        if url.urlconf_module.__name__ in exclude:
            controller_urls.remove(url)
    return controller_urls
