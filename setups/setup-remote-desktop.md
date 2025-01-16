## Setup Chrome Remote Desktop

```bash
sudo passwd $(whoami)
sudo chage -l $(whoami)
```

```bash
curl https://dl.google.com/linux/linux_signing_key.pub \
    | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/chrome-remote-desktop.gpg
echo "deb [arch=amd64] https://dl.google.com/linux/chrome-remote-desktop/deb stable main" \
    | sudo tee /etc/apt/sources.list.d/chrome-remote-desktop.list
```

```
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive \
    apt-get install --assume-yes chrome-remote-desktop
```

### Ubuntu Desktop
```bash
sudo apt install ubuntu-desktop-minimal
```

### set remote desktop session to GNOME
```bash
sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/gnome-session" > /etc/chrome-remote-desktop-session'
```

### Disable the Gnome display manager service on your instance, because it conflicts with the Chrome Remote Desktop service
```bash
sudo systemctl disable gdm3.service
```

### reboot

### check RD status
```bash
sudo systemctl status chrome-remote-desktop@$USER
```

### change user setting by
```bash
sudo gnome-control-center
```

### remove game apps
```bash
sudo apt remove gnome-games
sudo apt autoremove
```
