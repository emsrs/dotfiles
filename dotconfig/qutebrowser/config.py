config.load_autoconfig(False)

def privacy():
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

privacy()
preferences()
