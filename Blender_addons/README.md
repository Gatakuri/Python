# by coelho DEV

Auto Save addon for Blender inspired by VS Code behavior.

## Features

- Automatic `.blend` saving
- Detects scene modifications
- Saves after inactivity
- Lightweight and simple
- Works globally after enabling

---

## Installation

1. Download the addon `.py`
2. Open Blender
3. Go to:

Edit → Preferences → Add-ons

4. Click:

Install from Disk

5. Select the addon file
6. Enable the addon checkbox

---

## How It Works

1. Save your project at least once:

Ctrl + S

2. Modify anything in the scene
3. Stop interacting for a few seconds
4. The addon automatically saves the project

---

## Console Messages

Open Blender console:

Window → Toggle System Console

You should see messages like:

```text
Addon iniciado
Auto saved
```

---

## Custom Save Delay

You can change the delay here:

```python
SAVE_DELAY = 5
```

Example:

```python
SAVE_DELAY = 10
```

This would save after 10 seconds without activity.

---

## Important Notes

- The project must already be saved at least once
- Blender cannot auto-save unnamed projects
- Works best for active workflow sessions

---

## Author

by coelho DEV