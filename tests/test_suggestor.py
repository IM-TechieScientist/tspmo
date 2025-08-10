import unittest
from core.suggestor import get_suggestion

class DummyLLM:
    def get_fix(self, context):
        return "git commit -m 'msg'"

class TestSuggestor(unittest.TestCase):
    def test_get_suggestion(self):
        llm = DummyLLM()
        context = "..."
        suggestion = get_suggestion(llm, context)
        self.assertEqual(suggestion, "git commit -m 'msg'")

if __name__ == "__main__":
    unittest.main()
