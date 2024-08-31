from htmlnode import *

class TextNode:
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode(text='{self.text}', text_type='{self.text_type}', url={self.url!r})"

def text_node_to_html_node(text_node):
    output = ""
    text_types = {
        "text": LeafNode(tag=None, value=text_node.text),
        "bold": LeafNode(tag="b", value=text_node.text),
        "italic": LeafNode(tag="i", value=text_node.text),
        "code": LeafNode(tag="code", value=text_node.text),
        "link": LeafNode(tag="a", value=text_node.text, props={"href": text_node.url}),
        "image": LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    }

    if text_node.text_type in text_types:
        output = text_types[text_node.text_type]
        return output
    else:
        raise Exception("Text type not found")