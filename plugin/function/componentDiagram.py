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
                    "context", # Denna specificerar vilken type som dollar objektet får vara. skulle kunna vara page eller dollar
                    "Component Overview"),
        ]
    
    def exec_function(self, dollar_object):

        predefinedComponents = ["database", "queue"]

        components = []
        umlHeader = []
        umlContent = ""


        for component in dollar_object.get_header()['context']['components']:

            componentName = component.get_header()['id'].replace("-", "_")
            umlHeader.append("component" + " \"" + componentName + "\" as " + componentName)

            #Handle outputs from component
            outputComponents = component.get_header()['outputs']['components']
            outputFormats = component.get_header()['outputs']['formats']
            outputProtocols = component.get_header()['outputs']['protocols']
            i = 0
            for outputComponent in outputComponents:
                if isinstance(outputComponent, DollarObject):

                    ic = outputComponent.get_header()['inputs']['components']
                    j = 0
                    for c in ic:
                        if c == component:
                            break
                        j+=1
                    
                    format = outputComponent.get_header()['inputs']['formats']
                    
                    outputComponentName = outputComponent.get_header()['id'].replace("-", "_")   
                    umlHeader.append("component" + " \"" + outputComponentName + "\" as " + outputComponentName)
                    umlContent +=  componentName + "  -->  " + outputComponentName + "  :" + format[j] +"\n"

                else:
                    if outputComponent in predefinedComponents:
                        umlHeader.append(outputComponent + " \"" + outputComponent + "\" as " + outputComponent + str(i))
                        umlContent += componentName + "  ->  " + outputComponent + str(i) + "  :" + outputProtocols[i] +"\n"
                    else:
                        print("component: ", outputComponent, " not supported")

            i+=1

                    

            umlResult = "\n".join(umlHeader)
            umlResult = umlResult + "\n" + umlContent

            if isinstance(component, DollarObject):
                components.append(
                        OutputFormatListItem([
                            OutputFormatDollarObject(component),
                            OutputFormatText(":  "+ component.get_header()['description'])
                        ]))

        return [
            OutputFormatParagraph([OutputFormatText("## System components")]),
            OutputFormatUnorderedList(components),
            OutputFormatPluginBlock("plantuml", umlResult)
        ]
