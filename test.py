import sys
print("Python executable:", sys.executable)
print("Python path:", sys.path)

try:
    import matplotlib
    print("matplotlib version:", matplotlib.__version__)
except ImportError:
    print("matplotlib is not installed")