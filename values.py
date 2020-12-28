screen_dimensions = None
screen_width = None
screen_height = None
hud_side = None
hud_scale = None
hud_margin_v = None
hud_geometry = None
tmp = "/tmp/fner_tmp"

brightness_up = 'brightnessctl s +10'
brightness_down = 'brightnessctl s 10-'
brightness_get_level = 'brightnessctl get > /tmp/fner_tmp'

volume_up = 'amixer set Master 10%+ unmute -q'
volume_down = 'amixer set Master 10%- -q'
volume_toggle = 'amixer set Master toggle -q'
volume_get_level = 'amixer sget Master | grep \'Right:\' | awk -F\'[][]\' \'{ print $2 }\' > /tmp/fner_tmp'
volume_get_status = 'amixer sget Master | grep \'Right:\' | awk -F\'[][]\' \'{ print $4 }\' > /tmp/fner_tmp'

