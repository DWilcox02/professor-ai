import torch
from enum import Enum


class Device(Enum):
    CPU = False
    MPS = True


device: Device = Device.MPS if torch.backends.mps.is_available() else Device.CPU
print(f"Using {device} for processing")
