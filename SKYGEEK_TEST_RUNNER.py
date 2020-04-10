import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

test_modules = [
    'Tests.test_SimpleSearch',
    'Tests.test_AdvancedSearch',
    'Tests.test_BulkItemUpdate',

]

suite = unittest.TestSuite()

for test in test_modules:
    try:
        mod = __import__(test, globals(), locals(), ['suite'])
        suite_fn = getattr(mod, 'suite')
        suite.addTest(suite_fn())
    except (ImportError, AttributeError):

        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

unittest.TextTestRunner().run(suite)