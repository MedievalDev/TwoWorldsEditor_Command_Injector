
## TW Editor Command Injector

A tool for automating the Two Worlds editor. Detects a running editor instance and executes commands via clipboard injection — single commands or batch execution from TXT command lists.

### Features

- **Auto-detection** — Finds the Two Worlds editor automatically, no setup needed
- **Single & batch execution** — Run individual commands or load entire TXT command lists
- **Searchable command browser** — All available commands sorted by category, executable directly from the interface
- **Editable commands** — Right-click any command to view details, modify values, and execute instantly
- **Defaults system** — Read default values, send commands without parameters, or reset with the D:wert button
- **Safety features** — STOP button, auto-stop on focus loss, and mouse-to-corner emergency abort
- **Configurable** — Language setting and editor path in `tw_injector_config.json`

### Usage

Double-click `START.bat` or run directly:

```
python tw_editor_cmd_injector.py
```

The BAT launcher auto-detects Python installations even if Python is not in PATH.

### Requirements

- Python 3.8+
- `pyautogui` and `pygetwindow` (auto-installed by BAT launcher)
- Two Worlds 1 Editor running

### How It Works

The injector uses clipboard injection to send commands to the editor's console. It copies the command text to clipboard, brings the editor window to focus, simulates Ctrl+V paste and Enter, then returns focus. Batch mode processes command lists with configurable delay between commands.

## Related Repositories

Related Repositories

- Twor-Worlds-Dialog-Viewer-Editor — LAN Viewer and Quest/Dialog Editor for .lan, .idx, .qtx, and .shf files https://github.com/MedievalDev/Twor-Worlds-Dialog-Viewer-Editor
- Twor-Worlds-LND-Viewer — LND map format viewer with heightmap, textures, objects, and world viewer https://github.com/MedievalDev/Twor-Worlds-LND-Viewer
- Two-Worlds-Modding-Guid — Interactive modding guide with step-by-step tutorials                         https://github.com/MedievalDev/Two-Worlds-Modding-Guid

## License

MIT
