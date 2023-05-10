from dollar.plugin import DollarExtensionPlugin
from dollar.plugin import PluginHandler


class QueueExtensionPlugin(DollarExtensionPlugin):

    def extends(self):
        return "page"

    # Namnet på typen eg type: queue
    def get_name(self):
        return "queue"

    def get_secondaries(self):
        return ["queues"]

    def get_primaries(self):
        return []

    def validate_primary(self, dollar_object):
        return None

    # Denna exekveras för den aktuella typen, här type: queue
    def exec_primary(self, dollar_object):
        dollar_object.get_header()['queue'] = {}
        dollar_object.get_header()['queue']['subscribers'] = []
        dollar_object.get_header()['queue']['publishers'] = []

    # Denna exekveras för alla typer som har fältet "queues", se get_secondaries()
    def exec_secondary(self, dollar_object):
        if "queues" in dollar_object.get_header():
            queue = dollar_object.get_header().get("queues")
            if 'subscriber' in queue:
                for subscribed_dollar_object in queue['subscriber']:
                    #print(subscribed_dollar_object)
                    #print(subscribed_dollar_object.get_header())
                    subscribed_dollar_object.get_header()['queue']['subscribers'].append(dollar_object)
            if 'publisher' in queue:
                for subscribed_dollar_object in queue['publisher']:
                    #print(subscribed_dollar_object)
                    #print(subscribed_dollar_object.get_header())
                    subscribed_dollar_object.get_header()['queue']['publishers'].append(dollar_object)
