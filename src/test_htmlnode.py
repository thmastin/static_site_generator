import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props_ex(self):
        node = HTMLNode()  # Assumes props is None by default

        with self.assertRaises(Exception) as context:
            node.props_to_html()

        # Verify that the exception has the correct message
        self.assertEqual(str(context.exception), "No Properties")

    def test_props_to_html_out(self):
        node = HTMLNode("h1", "This is test text", ["h2"], {"href": "<a>"})
        node_text = node.props_to_html()
        print(node_text)
        test_text = f' href="<a>"'
        self.assertEqual(node_text, test_text)
    
    def test_multiple_props(self):
        node = HTMLNode("h1", "This is test text", ["h2"], {"href": "<a>", "<h1>": "heading"})
        node_text = node.props_to_html()
        print(node_text)
        test_text = f' href="<a>" <h1>="heading"'
        self.assertEqual(node_text, test_text)

    def test_LeafNode_no_value(self):
        node = LeafNode(None)
        self.assertRaises(ValueError)

    def test_LeafNode_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        node = node.to_html()
        self.assertEqual(node, expected)
    
    def test_LeafNone_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        node = node.to_html()
        self.assertEqual(node, expected)

    def test_parent_node(self):
        # Basic set of nodes for testing
        parent_node = ParentNode(
            tag="div",
            children=[
                LeafNode(tag="p", value="Paragraph 1"),
                LeafNode(tag="a", value="Link"),
                ParentNode(
                    tag="ul",
                    children=[
                        LeafNode(tag="li", value="Item 1"),
                        LeafNode(tag="li", value="Item 2"),
                    ]
                ),
            ]
        )

        # Attempt to convert the node to HTML and print
        expected_output = "<div><p>Paragraph 1</p><a>Link</a><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), expected_output)

    def test_parent_node_no_children(self):
        parent_node = ParentNode(tag = 'div', children=[])
        with self.assertRaises(ValueError): 
            parent_node.to_html()

    def test_nested_parent_nodes(self):
            inner_node = ParentNode(
                tag="span",
                children=[LeafNode(tag="i", value="Italic text")]
            )
            outer_node = ParentNode(
                tag="div",
                children=[inner_node]
            )
            expected_output = "<div><span><i>Italic text</i></span></div>"
            self.assertEqual(outer_node.to_html(), expected_output)

    def test_nested_empty_parent_node(self):
        inner_node = ParentNode(tag="span", children=[])
        outer_node = ParentNode(tag="div", children=[inner_node])
        
        with self.assertRaises(ValueError) as context:
            outer_node.to_html()
        
        # Optionally assert the specific error message if needed
        self.assertEqual(str(context.exception), "Must have children")


if __name__ == "__main__":
    unittest.main()