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


class ComponentOverviewFunctionPlugin(DollarFunctionPlugin):

    # Namnet som funktionen anropas med
    def get_name(self):
        return "ComponentOverview"

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

            inputComponents = component.get_header()['inputs']['components']
            inputFormats = component.get_header()['inputs']['formats']
            inputProtocols = component.get_header()['inputs']['protocols']

            i = 0
            for inputComponent in inputComponents:

                componentName = component.get_header()['id'].replace("-", "_")
                umlHeader.append("component" + " \"" + componentName + "\" as " + componentName)

                #Handle inputs to component
                if isinstance(inputComponent, DollarObject):
                     
                    inputComponentName = inputComponent.get_header()['id'].replace("-", "_")   
                    umlHeader.append("component" + " \"" + inputComponentName + "\" as " + inputComponentName)
                    umlContent += inputComponentName + "  -->  " + componentName + "  :" + inputFormats[i] +"\n"

                else:
                    if inputComponent in predefinedComponents:
                        umlHeader.append(inputComponent + " \"" + inputComponent + "\" as " + inputComponent + str(i))
                        umlContent += inputComponent + str(i) + "  ->  " + componentName + "  :" + inputProtocols[i] +"\n"
                    else:
                        print("component: ", inputComponent, " not supported")

            #Handle outputs from component
            outputComponents = component.get_header()['outputs']['components']
            outputFormats = component.get_header()['outputs']['formats']
            outputProtocols = component.get_header()['outputs']['protocols']

            for outputComponent in outputComponents:
                if isinstance(outputComponent, DollarObject):
                    
                    outputComponentName = outputComponent.get_header()['id'].replace("-", "_")   
                    umlHeader.append("component" + " \"" + outputComponentName + "\" as " + outputComponentName)
                    umlContent += outputComponentName + "  <--  " + componentName + "  :" + outputFormats[i] +"\n"

                else:
                    if outputComponent in predefinedComponents:
                        umlHeader.append(outputComponent + " \"" + outputComponent + "\" as " + outputComponent + str(i))
                        umlContent += outputComponent + str(i) + "  <-  " + componentName + "  :" + outputProtocols[i] +"\n"
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
            OutputFormatParagraph([OutputFormatText("System components")]),
            OutputFormatUnorderedList(components),
            OutputFormatPluginBlock("plantuml", umlResult)
        ]
