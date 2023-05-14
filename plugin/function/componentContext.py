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


class ComponentContextFunctionPlugin(DollarFunctionPlugin):

    # Namnet som funktionen anropas med
    def get_name(self):
        return "ComponentContext"

    # Definierar typerna som tas som argument $$QueueDependency(typ)
    def get_arg_info(self) -> List[PluginArg]:
        return [
            PluginArgDollarObject( # Finns också PluginArg, se github
                    "component", # Denna specificerar vilken type som dollar objektet får vara. skulle kunna vara page eller dollar
                    "Component context"),
        ]
    
    def exec_function(self, dollar_object):
        component = dollar_object

        predefinedComponents = ["database", "queue"]
        umlHeader = []
        umlContent = ""


        componentName = component.get_header()['id'].replace("-", "_")
        umlHeader.append("component" + " \"" + componentName + "\" as " + componentName)

        inputComponents = component.get_header()['inputs']['components']
        inputFormats = component.get_header()['inputs']['formats']
        inputProtocols = component.get_header()['inputs']['protocols']

        i = 0
        for inputComponent in inputComponents:

            #Handle inputs to component
            if isinstance(inputComponent, DollarObject):
                    
                inputComponentName = inputComponent.get_header()['id'].replace("-", "_")   
                umlHeader.append("component" + " \"" + inputComponentName + "\" as " + inputComponentName)
                umlContent += inputComponentName + "  -->  " + componentName + "  :" + inputFormats[i] +"\n"

            else:
                if inputComponent in predefinedComponents:
                    umlHeader.append(inputComponent + " \"" + inputComponent + "\" as " + inputComponent + str(i))
                    umlContent += inputComponent + str(i) + "  ->  " + componentName + "  :" + inputProtocols[i] +"\n"
            i+=1


        #Handle outputs from component
        outputComponents = component.get_header()['outputs']['components']
        outputFormats = component.get_header()['outputs']['formats']
        outputProtocols = component.get_header()['outputs']['protocols']

        i = 0
        for outputComponent in outputComponents:
            if isinstance(outputComponent, DollarObject):
                
                outputComponentName = outputComponent.get_header()['id'].replace("-", "_")   
                umlHeader.append("component" + " \"" + outputComponentName + "\" as " + outputComponentName)
                umlContent +=  componentName + "  -->  " + outputComponentName + "  :" + outputFormats[i] +"\n"

            else:
                if outputComponent in predefinedComponents:
                    umlHeader.append(outputComponent + " \"" + outputComponent + "\" as " + outputComponent + str(i))
                    umlContent +=  componentName + "  ->  " + outputComponent + str(i) + "  :" + outputProtocols[i] +"\n"
            i+=1


            umlResult = "\n".join(umlHeader)
            umlResult = umlResult + "\n" + umlContent

        inputs = []
        outputs = []

        i = 0
        for inputComponent in inputComponents:
            if isinstance(inputComponent, DollarObject):
                inputs.append(
                        OutputFormatListItem([
                            OutputFormatText(component.get_header()['id'] + " inputs " + inputFormats[i] + " from: "),
                            OutputFormatDollarObject(inputComponent),
                            OutputFormatText(" via "+ inputProtocols[i])
                        ]))
            i+=1

        i = 0
        for outputComponent in outputComponents:
            if isinstance(outputComponent, DollarObject):
                outputs.append(
                        OutputFormatListItem([
                            OutputFormatText(component.get_header()['id'] + " outputs " + outputFormats[i] + " to: "),
                            OutputFormatDollarObject(outputComponent),
                            OutputFormatText(" via "+ outputProtocols[i])
                        ]))
            i+=1

        return [
            OutputFormatParagraph([OutputFormatText("## Component context")]),
            OutputFormatUnorderedList(inputs),
            OutputFormatUnorderedList(outputs),
            OutputFormatPluginBlock("plantuml", umlResult)
        ]
