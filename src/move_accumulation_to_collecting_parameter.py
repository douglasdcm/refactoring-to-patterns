# Original code
# It is necessary to build the content of an ML file. The parameter "result"
# is used to accumlate the string


class TagNode:
    def to_string(self):
        tag_name = "any-tag"
        attributes = "any-attributes"
        result = ""
        result += "<" + tag_name + " " + attributes + ">"
        for _ in range(3):
            result += "<child>"
        result += "any-value"
        result += "</" + tag_name + ">"
        return result


# Refctored code
# Some functions were created to build the string and "result" is passed
# hand by hand to accumulate the string. 'result' is a list that is converted
# to a string at to_string()
class TagNodeRefac:
    def __init__(self):
        self._result = []

    def append_contents_to(self):
        self.write_open_tag_to("any-tag", "any-attributes")
        self.write_children_to()
        self.write_value_to("any-value")
        self.writ_end_tag_to("any-tag")

    def write_children_to(self):
        for _ in range(3):
            self._result.append("<child>")

    def writ_end_tag_to(self, tag_name):
        self._result.append("</")
        self._result.append(tag_name)
        self._result.append(">")

    def write_open_tag_to(self, tag_name, attributes):
        self._result.append("<")
        self._result.append(tag_name)
        self._result.append(" ")
        self._result.append(attributes)
        self._result.append(">")

    def write_value_to(self, value):
        self._result.append(value)

    def to_string(self):
        self.append_contents_to()
        return "".join(self._result)


def run_refac():
    result1 = TagNode().to_string()
    result2 = TagNodeRefac().to_string()
    return result1, result2
