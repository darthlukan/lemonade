## Lemonade

Nothing to see yet don't look here.

Python script with the intent of being an easy to use and configurable [lemonbar](https://github.com/LemonBoy/bar), targeting bspwm.

~wip~

- Considering psutils for system info(ram, HDD)
- Probably just going to parse mpc calls for mpd.
- Needs to be able to grab config from shell variables/some other flexible medium(maybe just launch flags)
- data structure(s) for Monitor, workspace, windows
- will assume xrandr setup for calculating dimensions.

consideration for the far future: run as server in background so can kill and bring up with no problems adjusting dimensions a little bit at a time.

Considering a yaml style config file. mockup(dual monitors):

``` yaml
location:
	monitor: all
	dock: top

dimensions:
	monitor: all
	width: 1080	# or auto
	height: 32
	padding_horizontal: 20
	padding_vertical: 10
	x_offset: -10
	y_offset: -2

colors:
	foreground: #00000000
	background: #00000000
	alt1: #00000000
	alt2: #00000000
	workspace_focused: #00000000
	workspace_unfocused: #00000000
	workspace_urgent: #00000000
	icon: #00000000

# dropdown workspace mail yaourtUpdates
# mpd battery network volume weather clock windowTitle
# global
widgets:
	panel: all
	left: "dropdown workspace"
	center: "windowTitle"
	left: "mpd clock"
	# style of the contained items
	# considering: none powerline block
	style: block

# override second panel widgets
widgets:
	panel: 2
	left: "dropdown workspace"
	center: "windowTitle"
	left: "mpd clock"
	style: none

# workspace
workspace_display:
	icon_free: '-'
	icon_occupied: '+'
	workspace_display: name # name | icon
	show_free: true
	together: true
	mode_toggle: false


```

### Misc
- [spoonm](http://github.com/skewerr) came up with the name when we brainstormed.
