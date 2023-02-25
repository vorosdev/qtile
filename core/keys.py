from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils import config

keys, mod, alt = [ ], 'mod4', 'mod1'
terminal = config['terminal'].copy()

if not terminal['main']:
  terminal['main'] = guess_terminal()

for key in [
  # Switch between windows
  ([mod], 'h', lazy.layout.left()),
  ([mod], 'l', lazy.layout.right()),
  ([mod], 'j', lazy.layout.down()),
  ([mod], 'k', lazy.layout.up()),

  # Move windows between columns
  ([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
  ([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
  ([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
  ([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

  # Increase/decrease window size
  ([mod], 'i', lazy.layout.grow()),
  ([mod], 'm', lazy.layout.shrink()),

  # Window management
  ([mod, 'shift'], 'space', lazy.layout.flip()),
  ([mod], 'o', lazy.layout.maximize()),
  ([mod], 'n', lazy.layout.normalize()),
  ([mod], 'a', lazy.window.kill()),
  ([ ], 'F11', lazy.window.toggle_fullscreen()),

  # Floating window management
  ([mod], 'space', lazy.window.toggle_floating()),
  ([mod], 'c', lazy.window.center()),
  ([mod], 'f', lazy.function(float_to_front)),

  # Toggle between layouts
  ([mod], 'Tab', lazy.next_layout()),

  # Qtile management
  ([mod, 'control'], 'b', lazy.hide_show_bar()),
  ([mod, 'control'], 's', lazy.shutdown()),
  ([mod, 'control'], 'r', lazy.reload_config()),
  ([mod, alt], 'r', lazy.restart()),

  # Kill X11 session
  ([mod, alt], 's', lazy.spawn('kill -9 -1')),

  # Terminal
  ([mod], 'Return', lazy.spawn(terminal['main'])),
  ([mod, 'shift'], 'Return', lazy.spawn(terminal['floating'])),

  # Application Launcher
  ([mod, 'shift'], 'z', lazy.spawn('rofi -show window')),
  ([mod], 'z', lazy.spawn('rofi -show drun')),

  # Web Browser
  ([mod], 'b', lazy.spawn('brave')),

  # Screenshot Tool
  ([mod, 'shift'], 's', lazy.spawn('gnome-screenshot -i')),

  # Visual Studio Code
  ([mod], 'v', lazy.spawn('code')),

  # Thunar
  ([mod, 'shift'], 'f', lazy.spawn('thunar')),

  # Redshift
  ([mod], 'r', lazy.spawn("redshift -O 4000")),
  ([mod, 'shift'], 'r', lazy.spawn("redshift -x")),

  # Productivity
  # ([mod], 'p', lazy.spawn("obsidian")),
  ([mod, 'control'], 'p', lazy.spawn("notion-app")),

  # LockScreen 
  ([mod, 'control'], 'l', lazy.spawn("sh /home/vicente/.i3lock/lock.sh")),

  # Messenger 
  ([mod, 'control'], 'm', lazy.spawn("caprine"))
  # # Backlight
  # ([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
  # ([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

  # # Volume
  # ([ ], 'XF86AudioMute', lazy.spawn('pamixer --toggle-mute')),
  # ([ ], 'XF86AudioLowerVolume', lazy.spawn('pamixer --decrease 5')),
  # ([ ], 'XF86AudioRaiseVolume', lazy.spawn('pamixer --increase 5')),

  # # Player
  # ([ ], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
  # ([ ], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
  # ([ ], 'XF86AudioNext', lazy.spawn('playerctl next')),
]: keys.append(Key(*key)) # type: ignore
