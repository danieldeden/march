from dollar.plugin import DollarBlockPlugin
from dollar.format.input import InputFormatType
from dollar.format.output import OutputFormatPluginBlock
from dollar import ConfigMap

dollar_uml_type_map = {
    "queue": "queue",
    "page": "component",
}
#print("BLOCK")
class UmlBlockPlugin(DollarBlockPlugin):

    def __init__(self, config: ConfigMap):
        self.type_map = config.get_plugin_config(self.get_name())
        if self.type_map is None:
            self.type_map = dollar_uml_type_map # Går att overridea med config, detta kan vi titta på senare

    # Namnet för blocket, $$$ UML
    def get_name(self):
        return "UML"

    # Bara för den själv
    def get_type_map(self):
        return self.type_map

    # Denna funktionen skapar ett plantuml block. content är av typen dollar.format.input.InputFormat, se github
    def exec_block(self, content):
        result_def = []
        result_content = ""
        #print(content)
        for item in content.get_children():
            if item.get_format_type() == InputFormatType.TEXT:
                result_content = result_content + item.get_text()
            elif item.get_format_type() == InputFormatType.DOLLAR_OBJECT:
                dollar_object = item.get_dollar_object()
                id = dollar_object.get_id()
                alias = id.replace("-", "_")
                if alias == id:
                    item_def = self.get_type_map().get(dollar_object.get_type()) + " " + id
                else:
                    item_def = self.get_type_map().get(dollar_object.get_type()) + " \"" + id + "\" as " + alias
                if (item_def not in result_def):
                    result_def.append(item_def)
                result_content = result_content + dollar_object.get_id().replace("-", "_")
        result = "\n".join(result_def)
        result = result + "\n" + result_content

        # output är av typen dollar.format.output.OutputFormat, se github
        return [
            OutputFormatPluginBlock("plantuml", result)
        ]
