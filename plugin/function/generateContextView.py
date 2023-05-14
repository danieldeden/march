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


class GenerateContextViewFunctionPlugin(DollarFunctionPlugin):

    # Namnet som funktionen anropas med
    def get_name(self):
        return "GenerateContextView"

    # Definierar typerna som tas som argument $$QueueDependency(typ)
    def get_arg_info(self) -> List[PluginArg]:
        return [
            PluginArgDollarObject( # Finns också PluginArg, se github
                    "context", # Denna specificerar vilken type som dollar objektet får vara. skulle kunna vara page eller dollar
                    "Component Overview"),
        ]
    
    def exec_function(self, dollar_object):

        componentsDescriptionList = []
        umlHeader = []
        umlContent = ""

        umlComponents = []


        #Get all compoenets for cotnext
        for component in dollar_object.get_header()['context']['components']:          
            if isinstance(component, DollarObject):
                umlComponents.append(component)
                componentsDescriptionList.append(
                        OutputFormatListItem([
                            OutputFormatDollarObject(component),
                            OutputFormatText(":  "+ component.get_header()['description'])
                        ]))



        umlComponentsOutputComponents = [[] for _ in range(len(umlComponents))]
        umlComponentsOutputFormats = [[] for _ in range(len(umlComponents))]
        umlComponentsOutputProtocols = [[] for _ in range(len(umlComponents))]

        specialOutputComponents = [[] for _ in range(len(umlComponents))]
        specialOutputComponentsFormats = [[] for _ in range(len(umlComponents))]
        specialOutputComponentsProtocols = [[] for _ in range(len(umlComponents))]

        specialInputComponents = [[] for _ in range(len(umlComponents))]
        specialInputComponentsFormats = [[] for _ in range(len(umlComponents))]
        specialInputComponentsProtocols = [[] for _ in range(len(umlComponents))]

        #Sort all components outputs in 2D-array
        i = 0
        for component in umlComponents:
            
            outputComponents = component.get_header()['outputs']['components']
            outputFormats = component.get_header()['outputs']['formats']
            outputProtocols = component.get_header()['outputs']['protocols']

            inputComponents = component.get_header()['inputs']['components']
            inputFormats = component.get_header()['inputs']['formats']
            inputProtocols = component.get_header()['inputs']['protocols']
            
            j = 0
            for outputComponent in outputComponents:
                
                if isinstance(outputComponent, DollarObject):
                    umlComponentsOutputComponents[i].append(outputComponent.get_header()['id'].replace("-", "_"))

                    #Get input format and protocol for outputComponent where id = component
                    ic = outputComponent.get_header()['inputs']['components']
                    format = outputComponent.get_header()['inputs']['formats']
                    protocol = outputComponent.get_header()['inputs']['protocols']

                    k = 0
                    for c in ic:
                        if c == component:
                            #Append the right format and protocol to the list
                            umlComponentsOutputFormats[i].append(format[k])
                            umlComponentsOutputProtocols[i].append(protocol[k])
                            break
                        k+=1

                #Special output components (that's not a dollar-object)
                else:
                    if not outputComponent == "none":
                        specialOutputComponents[i].append(outputComponent)
                        specialOutputComponentsFormats[i].append(outputFormats[j])
                        specialOutputComponentsProtocols[i].append(outputProtocols[j])

                j += 1
            
            j = 0
            for specialInput in inputComponents:
                if not isinstance(specialInput, DollarObject):
                    if not specialInput == "none":
                        specialInputComponents[i].append(specialInput)
                        specialInputComponentsFormats[i].append(inputFormats[j])
                        specialInputComponentsProtocols[i].append(inputProtocols[j])
                j += 1

            i += 1




        #Generate UML-text for all regular components (dollar-objects)
        i = 0
        for component in umlComponents:
            componentName = component.get_header()['id'].replace("-", "_")
            umlHeader.append("component" + " \"" + componentName + "\" as " + componentName)

            j = 0
            for _ in umlComponentsOutputComponents[i]:      
                outputName = umlComponentsOutputComponents[i][j]
                format = umlComponentsOutputFormats[i][j]
                protocol = umlComponentsOutputProtocols[i][j]

                umlContent +=  componentName + "  -->  " + outputName + "  :" + format + " : " + protocol + "\n"
                j += 1

            i += 1



        appendedSpecialComponent = []

        #Generate UML-text for all special components (NONE dollar-objects)
        i = 0
        for component in umlComponents:
            componentName = component.get_header()['id'].replace("-", "_")

            j = 0
            for _ in specialOutputComponents[i]: 
                name = specialOutputComponents[i][j]
                format = specialOutputComponentsFormats[i][j]
                protocol = specialOutputComponentsProtocols[i][j]

                #Check if special component is already added to UML header
                if not (name in appendedSpecialComponent):
                    #Check component type (ie, queue/database)
                    componentType = "interface"
                    if "queue" in name.lower():
                        componentType = "queue"
                    elif "database" in name.lower():
                        componentType = "database"
                    umlHeader.append(componentType + " \"" + name + "\" as " + name)
                    appendedSpecialComponent.append(name)

                umlContent +=  componentName + "  -->  " + name + "  :" + format + " : " + protocol + "\n"

                j += 1

                
            j = 0
            for _ in specialInputComponents[i]: 
                name = specialInputComponents[i][j]
                format = specialInputComponentsFormats[i][j]
                protocol = specialInputComponentsProtocols[i][j]

                #Check if special component is already added to UML header
                if not (name in appendedSpecialComponent):
                    #Check component type (ie, queue/database)
                    componentType = "interface"
                    if "queue" in name.lower():
                        componentType = "queue"
                    elif "database" in name.lower():
                        componentType = "database"
                    umlHeader.append(componentType + " \"" + name + "\" as " + name)
                    appendedSpecialComponent.append(name)

                umlContent +=  name + "  -->  " + componentName + "  :" + format + " : " + protocol + "\n"

                j += 1


            i += 1


        umlResult = "\n".join(umlHeader)
        umlResult = umlResult + "\n" + umlContent

        return [
            OutputFormatParagraph([OutputFormatText("## System components")]),
            OutputFormatUnorderedList(componentsDescriptionList),
            OutputFormatPluginBlock("plantuml", umlResult)
        ]
