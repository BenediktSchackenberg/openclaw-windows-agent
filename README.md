# OpenClaw Windows Agent 🪟🐉

> **Production Ready (v0.3.2)** — Zero-touch installation, hardware/software inventory, remote command execution. Manage your Windows fleet from anywhere.

A native Windows Service + GUI for [OpenClaw](https://openclaw.ai) that turns your Windows PCs into remotely manageable nodes. Talk to your machines via Discord, Telegram, or any AI interface.

[![.NET](https://img.shields.io/badge/.NET-8.0-512BD4?style=flat-square&logo=dotnet)](https://dotnet.microsoft.com/)
[![Windows](https://img.shields.io/badge/Windows-10%2F11%2FServer-0078D6?style=flat-square&logo=windows)](https://www.microsoft.com/windows)
[![Release](https://img.shields.io/github/v/release/BenediktSchackenberg/openclaw-windows-agent?style=flat-square)](https://github.com/BenediktSchackenberg/openclaw-windows-agent/releases)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 🚀 Zero-Touch Installation

**One PowerShell command. 30 seconds. Done.**

```powershell
# Run as Administrator
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/BenediktSchackenberg/openclaw-windows-agent/main/installer/Install-OpenClawAgent.ps1" -OutFile "Install.ps1"
.\Install.ps1 -GatewayUrl "http://YOUR-GATEWAY-IP:18789" -GatewayToken "YOUR-TOKEN"
```

The script automatically:
1. ✅ Downloads agent from GitHub Releases
2. ✅ Verifies SHA256 hash
3. ✅ Installs to `C:\Program Files\OpenClaw\Agent`
4. ✅ Registers Windows Service (auto-start)
5. ✅ Connects to Gateway

**No manual steps. No reboots. No touching keyboards.**

---

## ✨ Features

### 📊 Hardware & Software Inventory
Automatically collects and reports:
- **Hardware** — CPU, RAM, GPU, Disks, Mainboard, BIOS/UEFI, TPM
- **Software** — All installed applications with versions & MSI codes
- **Windows Updates** — Hotfixes + full Windows Update history
- **Security** — Firewall status, BitLocker, UAC settings
- **Network** — Active connections, adapters, IP addresses
- **Browser Extensions** — Chrome, Edge, Firefox

### 🖥️ Remote Command Execution
Run any command on your Windows machines:
```
You: "What's the hostname of CONTROLLER?"
AI: *runs command* → "CONTROLLER"

You: "Open Notepad on my desktop"
AI: *starts Notepad* → "Started with PID 1234"

You: "Get the top 5 processes by memory"
AI: *runs Get-Process | Sort WS -Desc | Select -First 5*
```

### 🔗 Persistent Connection
- Windows Service runs 24/7 in background
- Auto-reconnects if connection drops
- Survives reboots
- Unique node ID per machine (`win-{hostname}`)

### 🌐 Web Dashboard
Beautiful Next.js dashboard showing:
- All connected nodes with status
- Hardware/Software details per node
- Groups and tags for organization
- Windows Update history

---

## 📋 Prerequisites

Before installing the agent, you need:

1. **OpenClaw Gateway** running on Linux (Raspberry Pi, Server, WSL, etc.)
   ```bash
   npm install -g openclaw
   openclaw gateway start
   ```

2. **Gateway accessible from network**
   - Set `bind: "lan"` in `~/.openclaw/openclaw.json`
   - Default port: `18789`

3. **Gateway Token**
   ```bash
   grep token ~/.openclaw/openclaw.json
   ```

📚 Full docs: [docs.openclaw.ai](https://docs.openclaw.ai)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           YOUR NETWORK                                   │
│                                                                          │
│  ┌──────────────────┐                        ┌───────────────────────┐  │
│  │   Linux Server   │      WebSocket         │   Windows Machines    │  │
│  │                  │ ◄────────────────────► │                       │  │
│  │  ┌────────────┐  │                        │  ┌─────────────────┐  │  │
│  │  │  OpenClaw  │  │   Commands/Events      │  │  Agent Service  │  │  │
│  │  │  Gateway   │  │ ─────────────────────► │  │  (runs 24/7)    │  │  │
│  │  └────────────┘  │                        │  └─────────────────┘  │  │
│  │        │         │                        │           │           │  │
│  │  ┌────────────┐  │                        │  ┌─────────────────┐  │  │
│  │  │ Inventory  │  │   Inventory Push       │  │   WMI/CIM       │  │  │
│  │  │ Backend    │ ◄───────────────────────  │  │   Collectors    │  │  │
│  │  │ (FastAPI)  │  │                        │  └─────────────────┘  │  │
│  │  └────────────┘  │                        │                       │  │
│  │        │         │                        │  DESKTOP-PC           │  │
│  │  ┌────────────┐  │                        │  LAPTOP-01            │  │
│  │  │ Dashboard  │  │                        │  SERVER-2022          │  │
│  │  │ (Next.js)  │  │                        │  ...                  │  │
│  │  └────────────┘  │                        └───────────────────────┘  │
│  └──────────────────┘                                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Supported Commands

| Command | Description | Example |
|---------|-------------|---------|
| `system.run` | Execute command | `{"command": ["hostname"]}` |
| `system.run` (background) | Start GUI app | `{"command": ["notepad.exe"], "background": true}` |
| `system.which` | Find executable | `{"name": "python"}` |
| `inventory.hardware` | Get hardware info | — |
| `inventory.software` | Get installed apps | — |
| `inventory.hotfixes` | Get Windows updates | — |
| `inventory.security` | Get security status | — |
| `inventory.network` | Get network info | — |
| `inventory.browser` | Get browser extensions | — |
| `inventory.full` | Get everything | — |
| `inventory.push` | Push to backend | — |

---

## 📦 Project Structure

```
├── src/
│   ├── OpenClawAgent/              # WPF GUI Application
│   │   ├── ViewModels/             # MVVM ViewModels
│   │   ├── Views/                  # WPF XAML views
│   │   └── Services/               # Gateway, Node, Credentials
│   │
│   └── OpenClawAgent.Service/      # Windows Service
│       ├── NodeWorker.cs           # WebSocket client
│       └── Inventory/              # WMI Collectors
│           ├── HardwareCollector.cs
│           ├── SoftwareCollector.cs
│           ├── SecurityCollector.cs
│           └── ...
│
├── backend/                        # FastAPI Inventory Backend
│   └── main.py                     # REST API for inventory storage
│
├── frontend/                       # Next.js Dashboard
│   └── src/app/                    # React components
│
├── installer/
│   ├── Install-OpenClawAgent.ps1   # Zero-touch installer
│   ├── Build-Release.ps1           # Release packaging
│   └── Package.wxs                 # MSI installer (WiX)
│
└── docs/
    └── E10-ZERO-TOUCH-INSTALL.md   # Deployment documentation
```

---

## 🔐 Security

- **Tokens stored with DPAPI** — Windows-native encryption
- **SHA256 hash verification** — Installer validates downloads
- **Service runs as SYSTEM** — Full local access (intentional)
- **Enrollment Tokens** — Coming in v0.4.0 for large deployments

⚠️ **Important:** Only connect to Gateways you control. The token grants full access.

---

## 📈 Roadmap

- [x] **v0.1** — Basic GUI + Gateway connection
- [x] **v0.2** — Windows Service + remote commands
- [x] **v0.3** — Inventory collection + Zero-touch install
- [ ] **v0.4** — Enrollment tokens + Job system
- [ ] **v0.5** — Package management + Software deployment
- [ ] **v1.0** — Production-ready with RBAC

See full roadmap: [ROADMAP.md](ROADMAP.md)

---

## 🤝 Contributing

Contributions welcome!

```bash
# Clone
git clone https://github.com/BenediktSchackenberg/openclaw-windows-agent.git

# Build
dotnet build

# Run GUI
dotnet run --project src/OpenClawAgent
```

Or open `OpenClawAgent.sln` in Visual Studio.

---

## 📄 License

MIT — see [LICENSE](LICENSE)

---

## 🔗 Links

- **OpenClaw**: [openclaw.ai](https://openclaw.ai) | [GitHub](https://github.com/openclaw/openclaw)
- **Docs**: [docs.openclaw.ai](https://docs.openclaw.ai)
- **Blog Post**: [schackenberg.com/posts/openclaw-windows-agent](https://schackenberg.com/posts/openclaw-windows-agent/)
- **Discord**: [OpenClaw Community](https://discord.com/invite/clawd)

---

*Built with 🐉 energy by [Benedikt Schackenberg](https://schackenberg.com)*
