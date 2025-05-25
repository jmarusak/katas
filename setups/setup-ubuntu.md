## Ubuntu VM Desktop software inventory
- chrome
- neovim
- xclip
- tree
- curl


## Docker

### install Docker
```
sudo apt install docker.io
```

### add to group
```
sudo usermod -aG docker $USER
```

### or set permissions
```
sudo chmod 777 /var/run/docker.sock
```


## Nodejs 22.x

```
# download and install nvm (nodejs version manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm install 22
```

```
# verify nodejs and npm version
node -v
nvm current
npm -v
```

## Java 17
```
sudo apt-get install openjdk-17-jdk
```

## file watcher tools for "go run"
```
apt install inotify-tools
```

## Vim

### vim plugin folder
```
~/.vim/pack/github/start
```

## Neovim
### nvim plugin folder
```
~/.config/nvim/pack/github/start
```

## git config
```
git config --global user.email "jmarusak@users.noreply.github.com"
git config --global user.name "jmarusak"
```
```
git config --local user.email "pepinoloco@users.noreply.github.com"
git config --local user.name "pepinoloco"
```

## Google VM ssh RSA keys
```
ssh-keygen -t rsa -f ~/.ssh/id_rsa_google -C martinviewanalytics -b 2048
```

## how to use in desktop2.sh
```
gcloud compute ssh martinviewanalytics@desktop2 --zone "northamerica-northeast2-a" --project "martinview4" --ssh-key-file=~/.ssh/id_rsa_google
```

# Github Copilot CLI
```
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
```

```
gh extension install github/gh-copilot
```

```
alias suggest='gh copilot suggest'
alias explain='gh copilot explain'
```

### Chrome Brower Extensions
- Jupyter Notebook Viewer
- Markdown Viewer
- 1Password – Password Manager v8.10.55.2

  
### change desktop color scheme
```
gsettings set org.gnome.desktop.background picture-uri ''
gsettings set org.gnome.desktop.background picture-uri-dark ''
```
```
gsettings set org.gnome.desktop.background primary-color 'rgb(50, 50, 50)'
```

