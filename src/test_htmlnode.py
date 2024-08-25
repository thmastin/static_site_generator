import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props_ex(self):
        node = HTMLNode()
        node.props_to_html
        self.assertRaises(NotImplementedError)

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



if __name__ == "__main__":
    unittest.main()