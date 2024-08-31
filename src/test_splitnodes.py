import unittest
from textnode import TextNode
from splitnodes import split_nodes_delimiter  # Replace 'your_module' with the actual module name

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_split(self):
        node = TextNode("This is **bold** text", "text")
        result = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[0].text_type, "text")
        self.assertEqual(result[1].text_type, "bold")
        self.assertEqual(result[2].text_type, "text")

    def test_no_split(self):
        node = TextNode("This is just text", "text")
        result = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is just text")
        self.assertEqual(result[0].text_type, "text")

    def test_multiple_splits(self):
        node = TextNode("This **is** a **test** string", "text")
        result = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(result), 5)
        self.assertEqual(result[1].text, "is")
        self.assertEqual(result[1].text_type, "bold")
        self.assertEqual(result[3].text, "test")
        self.assertEqual(result[3].text_type, "bold")

    def test_invalid_markdown(self):
        node = TextNode("This is **invalid markdown", "text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", "")