import unittest
from core.analyzer import analyze_failure

class TestAnalyzer(unittest.TestCase):
    def test_analyze_failure(self):
        cmd = "git cmomit -m 'msg'"
        err = "git: 'cmomit' is not a git command."
        prompt = analyze_failure(cmd, err)
        self.assertIn(cmd, prompt)
        self.assertIn(err, prompt)
        self.assertIn("Suggest the corrected command", prompt)

if __name__ == "__main__":
    unittest.main()
