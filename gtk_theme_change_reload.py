import shutil
import subprocess
import os
import tempfile

"""Runs xsettingsd for a short time to reload gtk3 theme"""
if shutil.which("xsettingsd"):
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, "w+") as tmp:
            tmp.write(
                """Net/DndDragThreshold 8
Net/CursorBlinkTime 1200
Net/ThemeName "Layan-dark"
Net/DoubleClickTime 400
Net/CursorBlink 1
Net/FallbackIconTheme "gnome"
Net/EnableEventSounds 1
Net/IconThemeName "Tela-blue-dark"
Net/SoundThemeName "freedesktop"
Net/EnableInputFeedbackSounds 0
"""
            )
            tmp.close()
            subprocess.Popen.wait(
                subprocess.Popen(["timeout", "1s", "xsettingsd", "-c", path])
            )
    finally:
        os.remove(path)
