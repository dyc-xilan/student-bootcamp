# week01/check_environment.py
import platform
import sys

print("python:", sys.version)
print("platform:", platform.platform())
try:
    import torch
    print("torch:", torch.__version__)
    print("cuda_available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("gpu:", torch.cuda.get_device_name(0))
except ImportError:
    print("torch: not installed (acceptable for Week 1 CPU task)")