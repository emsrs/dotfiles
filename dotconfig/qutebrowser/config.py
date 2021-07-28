config.load_autoconfig(False)

def privacy():
        # If the web site won't load because of javascript
        # you can enable it on the current host by using the tsh keybinding
        c.content.javascript.enabled = False
        c.content.private_browsing = True
        c.content.canvas_reading = False
        c.content.geolocation = False
        c.content.desktop_capture = False
        c.content.notifications.enabled = False
        c.content.media.audio_video_capture = False
        c.content.mouse_lock = False

def preferences():
        c.zoom.default = 140
        c.fonts.hints = "bold 14pt Iosevka"
        c.fonts.default_size = "14pt"
        c.fonts.default_family = "Iosevka"
        c.colors.hints.bg = "#fff"
        c.colors.hints.fg = "#000"
        c.colors.hints.fg = "#000"
        c.hints.border = "2px solid #000"
        c.downloads.location.directory = "~/down"
        c.tabs.show = "switching"
        c.statusbar.show = "in-mode"

def minimize_finger_printing():
        c.content.headers.user_agent = "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0"
        c.content.headers.accept_language = "en-US,en;q=0.5"
        c.content.headers.custom = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
        c.content.canvas_reading = False
        c.content.webgl = False



privacy()
preferences()
minimize_finger_printing();
