### gpg
```bash
sudo apt-get install gnupg
```

### mongodb
```
docker pull mongodb/mongodb-community-server:latest
```

```
docker run --name mongodb -p 27017:27017 mongodb/mongodb-community-server:latest
```

### mongosh
```
wget -qO- https://www.mongodb.org/static/pgp/server-7.0.asc | sudo tee /etc/apt/trusted.gpg.d/server-7.0.asc
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update
sudo apt-get install -y mongodb-mongosh
```

```
mongosh --version
```
