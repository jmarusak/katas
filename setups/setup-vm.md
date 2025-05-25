### Google Cloud VM config
- region: northamerica-northeast2-a
- machine type: n2-standard-8 (8 vCPUs, 32 GB Memory)
- Disk: 128GB
- HTTP/HTTPS trafic: On
- SSH Keys: martinviewanalytics

### VM Desktop2 software inventory
- flutter
- cursor
- neovim
- xclip
- tree

### VM network rule
```
"IPProtocol": "tcp",
"ports": "3000"
"destinationRanges": "0.0.0.0/0"
"direction": "EGRESS",
"targetTags": "http-server"
```

### Firefox enable Clipboard API
```
about:config

dom.events.testing.asyncClipboard
```
