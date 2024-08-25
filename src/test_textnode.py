import unittest

from textnode import TextNode


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

    

    


if __name__ == "__main__":
    unittest.main()