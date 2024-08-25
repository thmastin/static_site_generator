class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should overwrite this")

    def props_to_html(self):
        output = ""
        if self.props == None:
            raise Exception("No Properties")
        for key in self.props:
            output = output + f" {key} {self.props[key]}"
        return output
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

    



        
