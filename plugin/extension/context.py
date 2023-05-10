from dollar.plugin import DollarExtensionPlugin
from dollar.plugin import PluginHandler


class ContextExtensionPlugin(DollarExtensionPlugin):

    def extends(self):
        return "page"

    # Namnet på typen eg type: queue
    def get_name(self):
        return "context"

    def get_secondaries(self):
        return ["contexts"]

    def get_primaries(self):
        return []

    def validate_primary(self, dollar_object):
        return None

    # Denna exekveras för den aktuella typen, här type: queue
    def exec_primary(self, dollar_object):
        dollar_object.get_header()['context'] = {}
        dollar_object.get_header()['context']['components'] = []

    # Denna exekveras för alla typer som har fältet "queues", se get_secondaries()
    def exec_secondary(self, dollar_object):
        if "contexts" in dollar_object.get_header():
            context = dollar_object.get_header().get("contexts")
            if 'components' in context:
                for subscribed_dollar_object in context['components']:
                    subscribed_dollar_object.get_header()['context']['components'].append(dollar_object)
           