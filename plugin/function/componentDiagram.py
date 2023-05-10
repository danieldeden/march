from typing import List

from dollar.plugin.dollarplugin import DollarFunctionPlugin
from dollar.dollarobject import DollarObject
from dollar.format.output.outputformat import OutputFormatText
from dollar.format.output.outputformat import OutputFormatUnorderedList
from dollar.format.output.outputformat import OutputFormatListItem
from dollar.format.output.outputformat import OutputFormatDollarObject
from dollar.format.output.outputformat import OutputFormatParagraph
from dollar.format.output import OutputFormatPluginBlock
from dollar.plugin.pluginarg import PluginArgDollarObject
from dollar.plugin.pluginarg import PluginArg


class ComponentDiagramFunctionPlugin(DollarFunctionPlugin):

    # Namnet som funktionen anropas med
    def get_name(self):
        return "ComponentDiagram"

    # Definierar typerna som tas som argument $$QueueDependency(typ)
    def get_arg_info(self) -> List[PluginArg]:
        return [
            PluginArgDollarObject( # Finns också PluginArg, se github
                    ["component"], # Denna specificerar vilken type som dollar objektet får vara. skulle kunna vara page eller dollar
                    "Component Diagram"),
        ]


    def exec_function(self, dollar_object):
        print("test")
        return [
            OutputFormatParagraph([OutputFormatText("Test")])
        ]
