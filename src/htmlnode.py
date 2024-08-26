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
            output = output + f' {key}="{self.props[key]}"'
        return output
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self,  tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value required")
        if self.tag == None:
            return f"{self.value}"
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
       
    def to_html(self):           
        if not self.tag:
            raise ValueError("Tag is required")
        if not self.children:
            raise ValueError("Must have children")
        content = []
        parent_open_tag = f"<{self.tag}>"
        parent_close_tag = f"</{self.tag}>"
        
        for child in self.children:
            content.append(child.to_html())
        content = ''.join(content)
        return f'{parent_open_tag}{content}{parent_close_tag}'
    
    



            


        
        


    

    



        