import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_noteq(self):
        node = TextNode("THIS IS A TEXT NODE", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_with_url_eq(self):
        node = TextNode("This is a text node", "bold", "https://google.com")
        node2 = TextNode("This is a text node", "bold", "https://google.com")
        self.assertEqual(node, node2)

    def test_text_type_noteq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_with_url_default_eq(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_noteq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic", "https://google.com")
        self.assertNotEqual(node, node2)

    def test_text_node_conversion(self):
        # Set up a TextNode as input
        node = TextNode("This is a text node", "text")
        
        # Convert to LeafNode
        leaf_node = text_node_to_html_node(node)
        
        # Verify the expected LeafNode properties
        expected_tag = None
        expected_text = "This is a text node"
        
        # Check if `leaf_node` properties match expectations
        self.assertEqual(leaf_node.tag, expected_tag)
        self.assertEqual(leaf_node.value, expected_text)

    def test_text_node_bold(self):
        # Set up a TextNode as input
        node = TextNode("This is a bold node", "bold")
        
        # Convert to LeafNode
        leaf_node = text_node_to_html_node(node)
        
        # Verify the expected LeafNode properties
        expected_tag = "b"
        expected_text = "This is a bold node"
        
        # Check if `leaf_node` properties match expectations
        self.assertEqual(leaf_node.tag, expected_tag)
        self.assertEqual(leaf_node.value, expected_text)

    def test_text_node_italic(self):
        # Set up a TextNode as input
        node = TextNode("This is a italic node", "italic")
        
        # Convert to LeafNode
        leaf_node = text_node_to_html_node(node)
        
        # Verify the expected LeafNode properties
        expected_tag = "i"
        expected_text = "This is a italic node"
        
        # Check if `leaf_node` properties match expectations
        self.assertEqual(leaf_node.tag, expected_tag)
        self.assertEqual(leaf_node.value, expected_text)
    
    def test_text_node_code(self):
        # Set up a TextNode as input
        node = TextNode("This is a code node", "code")
        
        # Convert to LeafNode
        leaf_node = text_node_to_html_node(node)
        
        # Verify the expected LeafNode properties
        expected_tag = "code"
        expected_text = "This is a code node"
        
        # Check if `leaf_node` properties match expectations
        self.assertEqual(leaf_node.tag, expected_tag)
        self.assertEqual(leaf_node.value, expected_text)

    def test_text_node_link(self):
        # Set up a TextNode as input
        node = TextNode("This is a link node", "link")
        
        # Convert to LeafNode
        leaf_node = text_node_to_html_node(node)
        
        # Verify the expected LeafNode properties
        expected_tag = "a"
        expected_text = "This is a link node"
        expected_props = {"href": node.url}
        
        # Check if `leaf_node` properties match expectations
        self.assertEqual(leaf_node.tag, expected_tag)
        self.assertEqual(leaf_node.value, expected_text)
        self.assertEqual(leaf_node.props, expected_props)

    def test_text_node_image(self):
        # Set up a TextNode as input
        node = TextNode("This is a image node", "image")
        
        # Convert to LeafNode
        leaf_node = text_node_to_html_node(node)
        
        # Verify the expected LeafNode properties
        expected_tag = "img"
        expected_text = ""
        expected_props = {"src": node.url, "alt": node.text}
        
        # Check if `leaf_node` properties match expectations
        self.assertEqual(leaf_node.tag, expected_tag)
        self.assertEqual(leaf_node.value, expected_text)
        self.assertEqual(leaf_node.props, expected_props)

    def test_text_node_not_found(self):
        # Set up a TextNode with an invalid type
        node = TextNode("Unknown", "unknown_type")

        # Verify that the conversion raises an exception
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        
        # Optionally, check the exception message
        self.assertTrue('Text type not found' in str(context.exception))

if __name__ == "__main__":
    unittest.main()