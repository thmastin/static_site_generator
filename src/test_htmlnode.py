import unittest

from htmlnode import HTMLNode


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



if __name__ == "__main__":
    unittest.main()