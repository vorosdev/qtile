from libqtile.bar import CALCULATED
from libqtile.lazy import lazy
from libqtile import widget

from core.bar.utils import base, decoration, iconFont, powerline
from extras import Clock, GroupBox, modify, TextBox, Volume, widget
from utils import color

tags = [
  '󰊢', '﬏', '󰆦', '󰈹', '󰈎', '', '󰠮', '',
]

bar = {
  'background': color['bg'],
  'border_color': color['bg'],
  'border_width': 4,
  'margin': [10, 10, 0, 10],
  'opacity': 0.95,
  'size': 18,
}

def sep(fg: str, offset = 0, padding = 8) -> TextBox:
  return TextBox(
    **base(None, fg),
    **iconFont(),
    offset = offset,
    padding = padding,
    text = '',
  )

def logo(bg: str, fg: str) -> TextBox:
  return modify(
    TextBox,
    **base(bg, fg),
    **decoration(),
    **iconFont(),
    mouse_callbacks = { 'Button1': lazy.spawn('rofi -show window')},
    offset = 4,
    padding = 17,
    text = '',
    y = -1,
  )

def groups(bg: str) -> GroupBox:
  return GroupBox(
    **iconFont(),
    background = bg,
    borderwidth = 1,
    colors = [
      color['cyan'], color['magenta'], color['yellow'],
      color['red'], color['blue'], color['green'], color['cherry'],
    ],
    highlight_color = color['bg'],
    highlight_method = 'line',
    inactive = color['black'],
    invert = True,
    padding = 7,
    rainbow = True,
  )

def volume(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      text = '󰖀',
      x = 4,
      y = -1,
    ),
    modify(
      Volume,
      **base(bg, fg),
      **powerline('arrow_right'),
      commands = {
        'decrease': 'pamixer --decrease 5',
        'increase': 'pamixer --increase 5',
        'get': 'pamixer --get-volume-human',
        'mute': 'pamixer --toggle-mute',
      },
      update_interval = 0.1,
    ),
  ]

def updates(bg: str, fg: str) -> list:
  return [
    TextBox(
      **base(bg, fg),
      **iconFont(),
      offset = -1,
      text = '',
      x = -5,
      y = -1,
    ),
    widget.CheckUpdates(
      **base(bg, fg),
      **decoration('right'),
      colour_have_updates = fg,
      colour_no_updates = fg,
      display_format = '{updates} updates  ',
      distro = 'Arch_checkupdates',
      initial_text = 'No updates  ',
      no_update_string = 'No updates  ',
      padding = 0,
      update_interval = 3600,
    ),
  ]
  '''
def window_name(bg: str, fg: str) -> object:
  return widget.WindowName(
    **base(bg, fg),
    format = '{name}',
    max_chars = 20,
    width = CALCULATED,
  )
'''

def pomodoro(bg: str, fg: str) -> list:
  return [
    widget.Pomodoro(
      **base(bg, fg),
      **decoration('left' 'right'),
      padding = 5,
      fontsize = 14,
      prefix_inactive="START",
      color_inactive = "#585b70",
      color_active = "#000000",
      color_break = "#FF0000",
      num_pomodori = 2,
      length_pomodori = 35,
      length_short_break = 5,
      length_long_break = 15,
    ),
  ]

def cpu(bg: str, fg: str) -> list:
  return [
    TextBox(
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      offset = 3,
      padding = 5,
      text = '󰍛',
      x = 5,
      y = -1,
    ),
    widget.CPU(
      **base(bg, fg),
      **powerline('arrow_right'),
      format = '{load_percent:.0f}%',
    )
  ]

def ram(bg: str, fg: str) -> list:
  return [
    TextBox(
      **base(bg, fg),
      **iconFont(),
      offset = -2,
      padding = 5,
      text = '󰘚',
      x = -2,
      y = -1,
    ),
    widget.Memory(
      **base(bg, fg),
      **powerline('arrow_right'),
      format = '{MemUsed: .0f}{mm} ',
      padding = -1,
    ),
  ]

def disk(bg: str, fg: str) -> list:
  return [
    TextBox(
      **base(bg, fg),
      **iconFont(),
      offset = -1,
      text = '',
      x = -5,
      y = -1,
    ),
    widget.DF(
      **base(bg, fg),
      **decoration('right'),
      format = '{f} GB  ',
      padding = 0,
      partition = '/',
      visible_on_warn = False,
      warn_color = fg,
    ),
  ]

def clock(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      offset = 2,
      text = '󰥔',
      x = 1,
      y = -1,
    ),
    modify(
      Clock,
      **base(bg, fg),
      **decoration('right'),
      format = '%A - %I:%M %p ',
      long_format = '%B %-d, %Y ',
      padding = 3,
    ),
  ]

def openweather(bg: str, fg: str) -> list:
  return [
    widget.OpenWeather(
      **base(bg, fg),
      **decoration('left' 'right'),
      location ='Irapuato',
      format = '{temp}°C',
      padding = 5,
    )
  ]


widgets = [
  widget.Spacer(length = 2),
  logo(color['blue'], color['bg']),
  sep(color['black'], offset = -8),
  groups(None),
  sep(color['black'], offset = 4, padding = 4),
  *volume(color['magenta'], color['bg']),
  *updates(color['red'], color['bg']),
  widget.Spacer(),
  # window_name(None, color['fg']),  
  *pomodoro(['#ffffff'], color['bg']),
  widget.Spacer(),
  # *pomodoro(color['black'], color['bg']),
  # *openweather(color['magenta'], color['bg']),
  # sep(color['black']),
  *cpu(color['green'], color['bg']),

  *ram(color['yellow'], color['bg']),
  *disk(color['cyan'], color['bg']),
  sep(color['black']),
  *clock(color['magenta'], color['bg']),
  # widget.Spacer(length = 2),
  sep(color['black']),
  *openweather(color['red'], color['bg']),
  widget.Spacer(length = 2),

]
