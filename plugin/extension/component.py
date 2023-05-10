from dollar.plugin import DollarExtensionPlugin
from dollar.plugin import PluginHandler


class ComponentExtensionPlugin(DollarExtensionPlugin):

    def extends(self):
        return "dollar"

    def get_name(self):
        return "component"

    def get_secondaries(self):
        return ["components"]

    def get_primaries(self):
        return []

    def validate_primary(self, dollar_object):
        return None

    def exec_primary(self, dollar_object):
        dollar_object.get_header()['componenet'] = {}


    def exec_secondary(self, dollar_object):
        return None