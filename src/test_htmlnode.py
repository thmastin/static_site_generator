import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props_ex(self):
        node = HTMLNode()
        node.props_to_html
        self.assertRaises(NotImplementedError)



if __name__ == "__main__":
    unittest.main()