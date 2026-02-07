# CHANGELOG.md — Release History

All notable changes to the OpenClaw Windows Agent.

## [Unreleased]

### Added
- Segoe Fluent Icons throughout UI (replacing emojis)
- App icon (openclaw.ico) for EXE and window
- Windows Update History in HotfixCollector (up to 200 entries)

### Fixed
- Backend extracts updateHistory from nested hotfixes object

---

## [0.2.0] — 2026-02-06

### Added
- **Inventory System** — Full hardware/software/security data collection
  - 7 Collectors: Hardware, Software, Hotfixes, System, Security, Network, Browser
  - `inventory.push` command sends all data to backend API
  - PostgreSQL + TimescaleDB for storage
  - Next.js frontend with Dashboard + Node Detail views
- **Windows Service** — Background service for 24/7 node connection
  - Runs as SYSTEM, persists across reboots
  - GUI controls: Install/Start/Stop/Restart/Uninstall
  - UAC elevation via sc.exe
- **Dashboard View** — Live status cards + log viewer
  - Gateway status, Service status, Sessions, Cron Jobs
  - Auto-refresh every 5 seconds
- **Background mode for system.run** — Start GUI apps without blocking
- Service config stored in `C:\ProgramData\OpenClaw\service-config.json`

### Fixed
- Node invoke result format (id/nodeId/payload structure)
- paramsJSON double-parsing from Gateway
- RefreshServiceStatus runs on background thread
- LogEntry model moved to shared location

---

## [0.1.0] — 2026-02-05

### Added
- Initial WPF application structure
- Gateway connection via WebSocket
- Views: Dashboard, Gateways, Hosts, Commands, Logs
- MVVM architecture with CommunityToolkit.Mvvm
- Credential storage with DPAPI encryption
- Node registration and pairing flow
- `system.run`, `system.which`, `node.ping` commands

---

## Version Numbering

- **Major**: Breaking changes or major feature sets
- **Minor**: New features, backwards compatible
- **Patch**: Bug fixes, small improvements

---
*Format based on [Keep a Changelog](https://keepachangelog.com/)*
