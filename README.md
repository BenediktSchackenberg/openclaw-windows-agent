# OpenClaw Windows Agent 🪟

> ⚠️ **TESTING / ALPHA** — This project is in early development. Expect bugs, breaking changes, and missing features. Use at your own risk!

A native Windows GUI + Background Service for [OpenClaw](https://openclaw.ai) that registers your Windows PC as a Node, allowing remote command execution from the OpenClaw Gateway.

![.NET](https://img.shields.io/badge/.NET-8.0-512BD4?style=flat-square&logo=dotnet)
![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=flat-square&logo=windows)
![Status](https://img.shields.io/badge/Status-Alpha%20Testing-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## What It Does

The OpenClaw Windows Agent connects your Windows PC to an OpenClaw Gateway, enabling:

- 🖥️ **Remote Command Execution** — Run PowerShell/CMD commands from the Gateway
- 📁 **File Operations** — Create, read, write files remotely
- 🚀 **App Launching** — Start applications on your Windows PC
- 🔗 **Persistent Connection** — Windows Service keeps connection alive 24/7
- 📊 **Live Monitoring** — Dashboard shows real-time Gateway events and logs

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     YOUR NETWORK                                 │
│                                                                  │
│  ┌──────────────┐         WebSocket          ┌───────────────┐  │
│  │   Linux PC   │ ◄──────────────────────► │  Windows PC   │  │
│  │              │                            │               │  │
│  │  OpenClaw    │    "Run notepad.exe"       │  Agent GUI    │  │
│  │  Gateway     │ ─────────────────────────► │      +        │  │
│  │              │                            │  Background   │  │
│  │  (Port 18789)│ ◄───────────────────────── │  Service      │  │
│  │              │     { "pid": 1234 }        │               │  │
│  └──────────────┘                            └───────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Two Components:**
1. **OpenClawAgent.exe** — WPF GUI for configuration, monitoring, and service control
2. **OpenClawAgent.Service.exe** — Windows Service that maintains the Gateway connection 24/7

## Features

### ✅ Working Now

- 🔗 **Gateway Connection** — WebSocket connection with token auth
- ⚙️ **Windows Service** — Runs in background, survives reboots
- 💻 **Remote Commands** — `system.run` and `system.which` 
- 📊 **Live Dashboard** — Real-time Gateway events with emoji indicators
- 🔐 **Secure Credentials** — DPAPI encryption for tokens
- 🎨 **Dark Theme** — Slick OpenClaw-branded UI
- 🔄 **Auto-Reconnect** — Service reconnects if connection drops

### 🚧 In Progress / Planned

- 📸 Screenshot capture
- 📂 File browser/transfer
- 🖱️ GUI automation (mouse/keyboard)
- 🔔 System tray notifications
- 📦 MSI Installer
- 🔏 Code signing

## Supported Commands

| Command | Description | Example |
|---------|-------------|---------|
| `system.run` | Execute command, capture output | `{"command": ["powershell", "-Command", "Get-Date"]}` |
| `system.run` (background) | Start GUI app without waiting | `{"command": ["notepad.exe"], "background": true}` |
| `system.which` | Find executable in PATH | `{"name": "python"}` |

## Requirements

- Windows 10 (1903+) or Windows 11
- .NET 8.0 Runtime
- OpenClaw Gateway running somewhere on your network

## Installation

### Build from Source

```powershell
# Clone repository
git clone https://github.com/BenediktSchackenberg/openclaw-windows-agent.git
cd openclaw-windows-agent

# Build everything
dotnet build

# Run the GUI
dotnet run --project src/OpenClawAgent
```

Or open `OpenClawAgent.sln` in Visual Studio and press F5.

### Install the Service

1. Open the GUI
2. Go to **Connector** tab
3. Add your Gateway (URL + Token)
4. Click **Connect** to test
5. Click **Install Service**
6. Service starts automatically and survives reboots!

## Quick Start

### 1. Configure Gateway Connection

1. Open OpenClawAgent.exe
2. Go to **Connector** → Add Gateway
3. Enter:
   - **Name:** My Gateway
   - **URL:** `http://192.168.0.5:18789` (your Gateway IP)
   - **Token:** Your gateway token
4. Click **Add Gateway** → **Connect**

### 2. Install Background Service

1. Still in **Connector** tab
2. Click **📥 Install Service**
3. Accept UAC prompt
4. Service starts automatically!

### 3. Test from Gateway

From your OpenClaw session, try:
```
# Check the node is connected
nodes status

# Run a command
nodes invoke --node node-host --command system.which --params '{"name": "powershell"}'

# Create a file
nodes invoke --node node-host --command system.run --params '{"command": ["powershell", "-Command", "Set-Content -Path C:\\temp\\test.txt -Value Hello"]}'
```

## Project Structure

```
src/
├── OpenClawAgent/              # WPF GUI Application
│   ├── Models/                 # Data models (GatewayConfig, LogEntry, etc.)
│   ├── Services/               # Business logic
│   │   ├── GatewayService.cs   # WebSocket communication
│   │   ├── GatewayManager.cs   # Connection state management
│   │   ├── CredentialService.cs # DPAPI encrypted storage
│   │   ├── NodeService.cs      # Node registration
│   │   └── ServiceController.cs # Windows Service control
│   ├── ViewModels/             # MVVM ViewModels
│   ├── Views/                  # WPF XAML views
│   └── Themes/                 # OpenClaw dark theme
│
└── OpenClawAgent.Service/      # Windows Service
    ├── NodeWorker.cs           # Main service logic
    ├── ServiceConfig.cs        # Configuration handling
    └── Program.cs              # Service entry point
```

## Configuration

### GUI Settings
Stored in `%APPDATA%\OpenClaw\`:
- `gateways.json` — Saved gateways (tokens encrypted with DPAPI)

### Service Settings
Stored in `%PROGRAMDATA%\OpenClaw\`:
- `service-config.json` — Gateway URL, token, display name

## Security Notes

⚠️ **The Service runs as SYSTEM** — This means:
- Commands execute with SYSTEM privileges
- GUI apps won't be visible (Session 0 isolation)
- Full access to the local machine

**Recommendations:**
- Only connect to Gateways you control
- Use strong, unique tokens
- Consider firewall rules for the Gateway port
- For production: implement proper authentication

## Known Limitations

1. **GUI Apps Not Visible** — Service runs as SYSTEM, can't show windows on user desktop
2. **No Interactive Sessions** — Can't capture user input
3. **Single Node ID** — Currently hardcoded as `node-host`
4. **Limited Commands** — Only `system.run` and `system.which` for now

## Troubleshooting

### Service won't start
```powershell
# Check service status
Get-Service OpenClawNodeAgent

# Check Windows Event Log
Get-EventLog -LogName Application -Source "OpenClawNodeAgent" -Newest 10
```

### Connection issues
1. Check Gateway is reachable: `Test-NetConnection 192.168.0.5 -Port 18789`
2. Verify token is correct
3. Check Gateway config has `bind: "lan"` (not loopback)

### Commands timeout
- Check Dashboard for incoming events
- Restart service: `Restart-Service OpenClawNodeAgent`

## Development

### Tech Stack

- **Framework:** .NET 8.0
- **GUI:** WPF with MVVM (CommunityToolkit.Mvvm)
- **Service:** Worker Service template
- **Protocol:** OpenClaw Gateway Protocol v3 (WebSocket + JSON)

### Building

```powershell
# Debug build
dotnet build

# Release build
dotnet build -c Release

# Publish self-contained
dotnet publish -c Release -r win-x64 --self-contained -o ./dist
```

## Contributing

This is an alpha project — contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a Pull Request

## License

MIT — see [LICENSE](LICENSE)

---

*Part of the [OpenClaw](https://openclaw.ai) ecosystem* 🦀
