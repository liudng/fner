# fner

Forked from [obhud](https://github.com/nwg-piotr/obhud).

## Installation

Clone the repo to local:

```bash
git clone git@github.com:liudng/fner.git ~/src/fner
```

Create a new bash script file `~/.local/bin/fner`:

```bash
#!/bin/bash
cd ~/src/fner
python3 fner.py $@
```

## Configs for Openbox

```xml
<?xml version="1.0" encoding="UTF-8"?>
<openbox_config xmlns="http://openbox.org/3.4/rc" xmlns:xi="http://www.w3.org/2001/XInclude">
  <keyboard>
    <keybind key="XF86AudioRaiseVolume">
      <action name="Execute">
        <command>fner --volume up</command>
      </action>
    </keybind>
    <keybind key="XF86AudioLowerVolume">
      <action name="Execute">
        <command>fner --volume down</command>
      </action>
    </keybind>
    <keybind key="XF86AudioMute">
      <action name="Execute">
        <command>fner --volume toggle</command>
      </action>
    </keybind>
    <keybind key="XF86MonBrightnessUp">
      <action name="Execute">
        <command>fner --brightness up</command>
      </action>
    </keybind>
    <keybind key="XF86MonBrightnessDown">
      <action name="Execute">
        <command>fner --brightness down</command>
      </action>
    </keybind>
  </keyboard>
</openbox_config>
```

## References

* https://github.com/nwg-piotr/obhud

