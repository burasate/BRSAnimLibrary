from maya import mel
import maya.cmds as cmds
import sys, json

class gr_license:
    is_py3 = str(sys.version[0]) == '3'

    if gr_license.is_py3:
        import urllib.request as uLib
    else:
        import urllib as uLib

    @staticmethod
    def get_license_verify(key, product_code='hZBQC'):
        license_key, license_email = ['','']

        if not cmds.about(cnt=1):
            return None

        url_verify = 'https://api.gumroad.com/v2/licenses/verify'
        data = {
            'product_permalink': product_code,
            'license_key': key,
            'increment_uses_count': 'false'
        }

        if gr_license.is_py3:
            import urllib.parse
            verify_params = urllib.parse.urlencode(data)
        else:
            verify_params = gr_license.uLib.urlencode(data)
        verify_params = verify_params.encode('ascii')
        #print(verify_params)
        response = gr_license.uLib.urlopen(url_verify, verify_params)
        license = json.loads(response.read())
        #print(license)
        if license['success']:
            #print(license['message'] + '\n')
            license_key = license['purchase']['license_key']
            license_email = license['purchase']['email']
        return (license_key, license_email)

    eula_message = '''
End-user license agreement
    '''

    @staticmethod
    def show_ui():
        win_id = 'BRSACTIVATOR'
        current_key = 'D094DF54-217B4C1F-AB006260-0AC1BDCA1'
        win_width = 700

        if cmds.window(win_id, exists=True):
            cmds.deleteUI(win_id)
        cmds.window(win_id, t='Burased x Gumroad license activate',
            w=win_width, sizeable=1,
            retain=0, bgc=(.2, .2, .2))

        cmds.columnLayout(adj=0, w=win_width)

        cmds.text(l='End-user license agreement', fn='boldLabelFont', h=20, w=win_width)

        cmds.rowLayout(numberOfColumns=3,
                       columnWidth3=(win_width*.1, win_width*.8, win_width*.1),
                       columnAlign3=['center', 'center', 'center'], adj=2)
        cmds.columnLayout(adj=0);cmds.setParent('..')
        cmds.scrollField(h=150,editable=0, wordWrap=1, text=gr_license.eula_message)
        cmds.columnLayout(adj=0);cmds.setParent('..')
        cmds.setParent('..')

        cmds.showWindow(win_id)



print(sys.version[0])
print(gr_license.is_py3)
#print(gr_license.uLib)

#print(gr_license.get_license_verify('D094DF54-217B4C1F-AB006260-0AC1BDCA1'))
gr_license.show_ui()