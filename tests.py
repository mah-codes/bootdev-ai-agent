import unittest
import sys
from functions.get_files_info import get_files_info

class TestGetFileInfo(unittest.TestCase):
    def setUp(self):
        self.output_buffer = []
    
    def capture_output(self, message):
        self.output_buffer.append(message)
    
    def test_current_dir(self):
        result = get_files_info("calculator",".")
        lines = result.strip().split('\n')
        for line in lines:
            self.assertRegex(line, r"- .+: file_size=\d+ bytes, is_dir=(True|False)")
            self.capture_output(line)

    def test_pkg_dir(self):
        result = get_files_info("calculator","pkg")
        lines = result.strip().split('\n')
        for line in lines:
            self.assertRegex(line, r"- .+: file_size=\d+ bytes, is_dir=(True|False)")
            self.capture_output(line)

    def test_bin_projroot(self):
        result = get_files_info("calculator","/bin")
        self.assertIn("Error:", result)
        self.capture_output(result)

    def test_upper_dir(self):
        result = get_files_info("calculator","../")
        self.assertIn("Error:", result)
        self.capture_output(result)
    



if __name__ == "__main__":
    # Collect all output and print at the end
    all_output = []
    
    class OutputCollector:
        def __init__(self):
            self.output = []
        
        def capture(self, message):
            self.output.append(message)
    
    collector = OutputCollector()
    
    # Monkey patch the capture_output method
    # original_capture = TestGetFileInfo.capture_output
    TestGetFileInfo.capture_output = lambda self, message: collector.capture(message)
    
    # Run tests
    unittest.main(exit=False)
    
    # Print all collected output at the end
    print("\n" + "="*60)
    print("ALL TEST OUTPUT:")
    print("="*60)
    for i, output in enumerate(collector.output, 1):
        print(f"{i}. {output}")
    print("="*60)
