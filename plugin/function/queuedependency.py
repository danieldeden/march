from typing import List

from dollar.plugin.dollarplugin import DollarFunctionPlugin
from dollar.dollarobject import DollarObject
from dollar.format.output.outputformat import OutputFormatText
from dollar.format.output.outputformat import OutputFormatUnorderedList
from dollar.format.output.outputformat import OutputFormatListItem
from dollar.format.output.outputformat import OutputFormatDollarObject
from dollar.format.output.outputformat import OutputFormatParagraph
from dollar.plugin.pluginarg import PluginArgDollarObject
from dollar.plugin.pluginarg import PluginArg


class QueueDependencyFunctionPlugin(DollarFunctionPlugin):

    # Namnet som funktionen anropas med
    def get_name(self):
        return "QueueDependency"

    # Definierar typerna som tas som argument $$QueueDependency(typ)
    def get_arg_info(self) -> List[PluginArg]:
        return [
            PluginArgDollarObject( # Finns också PluginArg, se github
                    "queue", # Denna specificerar vilken type som dollar objektet får vara. skulle kunna vara page eller dollar
                    "Queue for which dependency will be printend"),
        ]

    # När funktionen anropas körs denna funktionen, med argumenten specade i get_arg_info
    def exec_function(self, dollar_object):
        output_subscribers = []
        output_publishers = []
        #print(dollar_object)
        for item in dollar_object.get_header()['queue']['subscribers']:
            if isinstance(item, DollarObject):
                output_subscribers.append(
                        OutputFormatListItem([
                            OutputFormatDollarObject(item)
                        ]))
        for item in dollar_object.get_header()['queue']['publishers']:
            if isinstance(item, DollarObject):
                output_publishers.append(
                        OutputFormatListItem([
                            OutputFormatDollarObject(item)
                        ]))
        # output är av typen dollar.format.output.OutputFormat, se github
        return [
            OutputFormatParagraph([OutputFormatText("Subscribers")]),
            OutputFormatUnorderedList(output_subscribers),
            OutputFormatParagraph([OutputFormatText("Publishers")]),
            OutputFormatUnorderedList(output_publishers),
        ]
