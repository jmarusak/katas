## GPU Driver Setup

### install ubuntu utility to check drivers/devices
```bash
sudo apt install ubuntu-drivers-common
```

### check devices installed
```bash
ubuntu-drivers devices
```

### install recommended driver
```bash
sudo apt install nvidia-driver-535
```

### check GPU driver and CUDA version
```bash
nvidia-smi
```
