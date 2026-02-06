# OpenClaw Windows Agent 🪟

A native Windows agent/node for [OpenClaw](https://openclaw.ai) with GUI, gateway management, and remote deployment capabilities.

![.NET](https://img.shields.io/badge/.NET-8.0-512BD4?style=flat-square&logo=dotnet)
![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=flat-square&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## Screenshots

*Coming soon — build the project to see the UI!*

## Features

- 🔗 **Gateway Connection** — Connect to OpenClaw Gateway with secure token authentication
- 💾 **Credential Storage** — Secure storage using Windows DPAPI/Credential Manager
- 💬 **Command Terminal** — Execute OpenClaw commands with history and output
- 🖥️ **Remote Deployment** — Push agent to other Windows machines via WinRM
- 📊 **Status Dashboard** — Real-time monitoring of agent and gateway status
- 📋 **Log Viewer** — View, filter, and export application logs
- 🔔 **System Tray** — Run minimized with status notifications

## Requirements

- Windows 10 (1903+) or Windows 11
- Windows Server 2019 or later
- .NET 8.0 Runtime (or SDK for building)

## Installation

### From Release (Recommended)

1. Download the latest release from [Releases](https://github.com/BenediktSchackenberg/openclaw-windows-agent/releases)
2. Run `OpenClawAgent-Setup.msi`
3. Launch "OpenClaw Agent" from Start Menu

### Build from Source

```powershell
# Clone repository
git clone https://github.com/BenediktSchackenberg/openclaw-windows-agent.git
cd openclaw-windows-agent

# Restore packages
dotnet restore

# Build
dotnet build -c Release

# Run
dotnet run --project src/OpenClawAgent
```

Or open `OpenClawAgent.sln` in Visual Studio and press F5.

## Quick Start

### 1. Connect to Gateway

1. Open the app
2. Go to **Gateways** in the sidebar
3. Enter Gateway Name, URL, and Token
4. Click **Add Gateway**
5. Select the gateway and click **Connect**

### 2. Run Commands

1. Go to **Commands** in the sidebar
2. Type any OpenClaw command (e.g., `status`, `help`)
3. Press Enter or click **Run**
4. Use ↑/↓ arrows to navigate command history

### 3. Deploy to Remote Hosts

1. Go to **Remote Hosts** in the sidebar
2. Click **Add Host** and enter hostname, username, password
3. Select WinRM connection type
4. Click **Deploy Agent** to push the agent to that machine

## Project Structure

```
src/OpenClawAgent/
├── Converters/          # XAML value converters
│   └── Converters.cs
├── Models/              # Data models
│   ├── GatewayConfig.cs
│   └── RemoteHost.cs
├── Services/            # Business logic
│   ├── GatewayService.cs          # Gateway API communication
│   ├── CredentialService.cs       # Secure credential storage (DPAPI)
│   └── RemoteDeploymentService.cs # WinRM/PowerShell deployment
├── ViewModels/          # MVVM ViewModels
│   ├── MainViewModel.cs
│   ├── DashboardViewModel.cs
│   ├── GatewaysViewModel.cs
│   ├── CommandsViewModel.cs
│   ├── HostsViewModel.cs
│   └── LogsViewModel.cs
├── Views/               # WPF XAML views
│   ├── MainWindow.xaml
│   ├── DashboardView.xaml
│   ├── GatewaysView.xaml
│   ├── CommandsView.xaml
│   ├── HostsView.xaml
│   └── LogsView.xaml
├── Themes/              # OpenClaw dark theme
│   └── OpenClawTheme.xaml
└── Assets/              # Icons, images
```

## Configuration

Config is stored in `%APPDATA%\OpenClaw\Agent\`:

```
%APPDATA%\OpenClaw\Agent\
├── gateways.json      # Encrypted gateway configs (DPAPI)
├── settings.json      # App settings
└── logs/              # Application logs
```

**All credentials are encrypted using Windows DPAPI** (CurrentUser scope) — they cannot be read by other users or on other machines.

## Security

- **DPAPI Encryption** — All sensitive data encrypted with Windows Data Protection API
- **No Admin Required** — Runs with standard user privileges (admin only for remote deployment)
- **TLS Required** — All gateway communication over HTTPS
- **Least Privilege** — Minimal permissions requested
- **No Telemetry** — No data sent anywhere except your configured gateway

## Remote Deployment via WinRM

The agent can deploy itself to other Windows machines using PowerShell Remoting (WinRM).

### Prerequisites on Target Machines

```powershell
# Enable WinRM (run as Admin on target)
Enable-PSRemoting -Force

# If needed, allow connections from your machine
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "your-admin-machine"
```

### Deployment Process

1. Connects via WinRM/PowerShell Remoting
2. Checks for existing OpenClaw installation
3. Copies and installs agent MSI
4. Configures gateway connection
5. Starts agent service or application

## Development

### Tech Stack

- **Framework:** .NET 8.0 + WPF
- **Pattern:** MVVM (CommunityToolkit.Mvvm)
- **UI:** Custom OpenClaw dark theme
- **Tray:** Hardcodet.NotifyIcon.Wpf
- **Remote:** Microsoft.PowerShell.SDK

### Building

```powershell
# Debug build
dotnet build

# Release build
dotnet build -c Release

# Publish self-contained (no .NET runtime required on target)
dotnet publish -c Release -r win-x64 --self-contained -o ./dist
```

### Code Signing

For production releases, sign with Authenticode:

```powershell
signtool sign /f certificate.pfx /p password /tr http://timestamp.digicert.com /td sha256 OpenClawAgent.exe
```

## Roadmap

- [x] v0.1.0 — Project structure, MVVM architecture
- [x] v0.2.0 — All views implemented (Dashboard, Gateways, Commands, Hosts, Logs)
- [ ] v0.3.0 — Full gateway integration, real-time status
- [ ] v0.4.0 — Remote deployment tested and working
- [ ] v0.5.0 — System tray, auto-start, notifications
- [ ] v1.0.0 — MSI installer, code signing, production release

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a Pull Request

## License

MIT — see [LICENSE](LICENSE)

---

*Part of the [OpenClaw](https://openclaw.ai) ecosystem*
