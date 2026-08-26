# test_thrivechain.py
"""
Tests for ThriveChain module.
"""

import unittest
from thrivechain import ThriveChain

class TestThriveChain(unittest.TestCase):
    """Test cases for ThriveChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThriveChain()
        self.assertIsInstance(instance, ThriveChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThriveChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
