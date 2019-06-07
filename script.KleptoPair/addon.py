import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser

def menu():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
        function5,
        function6,
        function7,
        function8,
        function9,
        function10,
        function11,
        function12,
        function13,
        function14,
        function15,
        function16
        ) 
    call = dialog.select( "[B][COLOR magenta]Klepto [COLOR cyan]Pairing Tool[/COLOR][/B]" , [ 
    "[B][COLOR magenta]*** [COLOR cyan]Select Site to PAIR:[/COLOR] ***\r\n[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]flashX.tv[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]openload[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]streamango[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]streamcherry[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]VEViO[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]VIDEOSHARE[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]ViduP[/COLOR][/B]" ,
	"[B][COLOR magenta]*** [COLOR cyan]Select Service to AUTHORIZE:[/COLOR] ***[/COLOR][/B]",
    "[B][COLOR cyan]---  [COLOR magenta]RealDebrid [COLOR cyan](ResolveURL)[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]RealDebrid [COLOR cyan](URLResolver)[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]AllDebrid [COLOR cyan](ResolveURL)[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]AllDebrid [COLOR cyan](URLResolver)[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]Premiumize.me [COLOR cyan](ResolveURL)[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]Premiumize.me [COLOR cyan](URLResolver)[/COLOR][/B]" ,
    "[B][COLOR cyan]---  [COLOR magenta]Trakt Addon [COLOR cyan](Install Addon FIRST!)[/COLOR][/B]" ] )
    if call:
        if call < 0:
            return
        func = funcs[call-16]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

check_os = platform()

def function1(): 0

def function2():
    site = 'https://www.flashx.tv/?op=login&magentairect=https://www.flashx.tv/pairing.php'
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function3():
    site = 'https://olpair.com/'
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
        os.system("open " + site)
    else:
        opensite = webbrowser.open(site)
		
def function4():
    site = 'https://streamango.com/pair'
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
        os.system("open " + site)
    else:
        opensite = webbrowser.open(site)
		
def function5():
    site = 'https://streamcherry.com/pair'
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
        os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function6():
    site = 'https://vev.io/pair'
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
        os.system("open " + site)
    else:
        opensite = webbrowser.open(site)
		
def function7():
    site = 'http://vshare.eu/pair'
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
        os.system("open " + site)
    else:
        opensite = webbrowser.open(site)
        
def function8():
    site = 'https://vidup.io/pair'
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function9(): 0

def function10():
    xbmc.executebuiltin("RunPlugin(plugin://script.module.resolveurl/?mode=auth_rd)")
    site = 'https://real-debrid.com/device'
    time.sleep(20)
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function11():
    xbmc.executebuiltin("RunPlugin(plugin://script.module.urlresolver/?mode=auth_rd)")
    site = 'https://real-debrid.com/device'
    time.sleep(20)
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function12():
    xbmc.executebuiltin("RunPlugin(plugin://script.module.resolveurl/?mode=auth_ad)")
    site = 'https://alldebrid.com/pin'
    time.sleep(20)
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function13():
    xbmc.executebuiltin("RunPlugin(plugin://script.module.urlresolver/?mode=auth_ad)")
    site = 'https://alldebrid.com/pin'
    time.sleep(20)
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function14():
    xbmc.executebuiltin("RunPlugin(plugin://script.module.resolveurl/?mode=auth_pm)")
    site = 'https://www.premiumize.me/device'
    time.sleep(20)
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function15():
    xbmc.executebuiltin("RunPlugin(plugin://script.module.urlresolver/?mode=auth_pm)")
    site = 'https://www.premiumize.me/device'
    time.sleep(20)
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)

def function16():
    xbmc.executebuiltin("RunScript(script.trakt, action=auth_info)")
    site = 'https://trakt.tv/activate'
    time.sleep(20)
    if check_os == 'android': 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % (site) )
    elif check_os == 'osx':
       os.system("open " + site)
    else:
        opensite = webbrowser.open(site)
		
menu()