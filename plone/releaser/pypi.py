# -*- coding: utf-8 -*-

try:
    from xmlrpclib import ServerProxy
except ImportError:
    from xmlrpc.client import ServerProxy


def get_users_with_release_rights(package_name):
    client = ServerProxy('https://pypi.python.org/pypi')
    existing_admins = set([
        user for role, user in client.package_roles(package_name)])
    return existing_admins


def can_user_release_package_to_pypi(user, package_name):
    return user in get_users_with_release_rights(package_name)
