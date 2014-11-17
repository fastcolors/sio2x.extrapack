import xbmcgui

def notify(header="", message="", icon=xbmcgui.NOTIFICATION_INFO, time=5000, sound=True):
    dialog = xbmcgui.Dialog()
    dialog.notification(heading="SiO2X-tra packs", message="Thanks for your preference.", icon=icon, time=time, sound=sound)

notify()
