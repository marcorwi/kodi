import xbmc
import xbmcgui
import xbmcaddon

addon = xbmcaddon.Addon()
STREAM_URL = "https://a8.asurahosting.com:7230/radio.mp3"
LOCAL_LOGO = addon.getAddonInfo('icon')

def run_radiovision():
    try:
        list_item = xbmcgui.ListItem(label="Radio Web Italia")
        list_item.setInfo('music', {
            'title': 'Radio Web Italia - In Diretta', 
            'plot': 'Radiovisione - Radio Web Italia', 
            'genre': 'Radio'
        })
        
        list_item.setArt({
            'thumb': LOCAL_LOGO,
            'icon': LOCAL_LOGO,
            'poster': LOCAL_LOGO,
            'fanart': LOCAL_LOGO
        })
        
        player = xbmc.Player()
        if not player.isPlaying():
            player.play(STREAM_URL, list_item)
            
    except Exception as e:
        xbmc.log(f"--- ERRORE SCRIPT RADIO WEB ITALIA: {str(e)} ---", xbmc.LOGERROR)

if __name__ == '__main__':
    run_radiovision()
