# test_glitchblock.py
"""
Tests for GlitchBlock module.
"""

import unittest
from glitchblock import GlitchBlock

class TestGlitchBlock(unittest.TestCase):
    """Test cases for GlitchBlock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlitchBlock()
        self.assertIsInstance(instance, GlitchBlock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlitchBlock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
