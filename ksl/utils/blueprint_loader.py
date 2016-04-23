import pkgutil
import re
import importlib
import sys
from traceback import print_tb
from flask import Blueprint


class BlueprintLoader(object):
    """
    Simple automatic conventions blueprint loader.
    """
    def __init__(self, app_package, blueprint_module_name='blueprints'):
        """
        :param package app_package: Python package which blueprint modules
            will be recursively searched within.
        :param str blueprint_module_name: String name of the blueprints modules
            that we're searching for (without the .py extension)
        """
        self.app_package = app_package
        self.blueprint_module_name = blueprint_module_name

    def discover_blueprint_modules(self, skip_modules=[], import_error_callback=None):

        regex = re.compile(r'{0}$'.format(self.blueprint_module_name))

        # walk packages returns a tuple.. so just so I remember which indexes
        (module_loader, name, ispkg) = 0, 1, 2

        packages = pkgutil.walk_packages(
            self.app_package.__path__,
            "{0}.".format(self.app_package.__name__),
            onerror=import_error_callback or self.handle_import_error)

        module_names = [pkg[name] for pkg
                        in packages
                        if regex.search(pkg[name])
                            and pkg[name] not in skip_modules]

        return module_names

    def load_blueprint_module(self, module_name):
        return importlib.import_module(module_name)


    def discover_blueprint_attributes(self, module):
        # iterate our blueprint modules, and find attributes matching the
        # provided pattern.
        return [attr for attr in vars(module).values() if isinstance(attr, Blueprint)]


    def handle_import_error(self, name):
        """
        Callback function for :py:meth:`pkgutil.walk_packages`, when an import
        error is encountered.

        :param str name: Name of the module that raised an import error.
        """
        (_type, _value_, _traceback) = sys.exc_info()
        print_tb(_traceback)
        raise ImportError("Error importing module {0}".format(name))
