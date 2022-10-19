from maya import mel
import maya.cmds as cmds
import sys, json

class gr_license:
    is_py3 = str(sys.version[0]) == '3'

    if is_py3:
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
'''*10

    @staticmethod
    def show_ui():
        win_id = 'BRSACTIVATOR'
        current_key = 'D094DF54-217B4C1F-AB006260-0AC1BDCA1'
        win_width = 600

        if cmds.window(win_id, exists=True):
            cmds.deleteUI(win_id)
        cmds.window(win_id, t='Burased x Gumroad license activate',
            w=win_width, sizeable=1, h=10,
            retain=0, bgc=(.2, .2, .2))

        cmds.columnLayout(adj=0, w=win_width)

        cmds.text(l='', fn='boldLabelFont', h=30, w=win_width)

        ct_w_percentile = win_width*.88
        bd_w_percentile = (win_width-ct_w_percentile)*.5
        cmds.rowLayout(numberOfColumns=3,
                       columnWidth3=(bd_w_percentile, ct_w_percentile,bd_w_percentile),
                       columnAlign3=['center', 'center', 'center'], adj=2)
        cmds.columnLayout(adj=0);cmds.setParent('..')

        cmds.columnLayout(adj=0, w=ct_w_percentile)

        cmds.scrollField(h=150, w=ct_w_percentile, editable=0, wordWrap=1, text=gr_license.eula_message)
        cmds.text(l='', h=30, w=ct_w_percentile)

        cmds.rowLayout(numberOfColumns=2, columnWidth2=(ct_w_percentile * .2, ct_w_percentile * .8),
                       columnAlign2=['right', 'left'], adj=1, h=30)
        cmds.text(al='right', l='Product Name : ')
        cmds.textField(tx='BRS Library', ed=0, w=ct_w_percentile * .7)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2, columnWidth2=(ct_w_percentile*.2, ct_w_percentile*.8),
                       columnAlign2=['right', 'left'], adj=1, h=30)
        cmds.text(al='right', l='Product Code : ')
        cmds.textField(tx='hZBQC', ed=0, w=ct_w_percentile * .7)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2, columnWidth2=(ct_w_percentile * .2, ct_w_percentile * .8),
                       columnAlign2=['right', 'left'], adj=1, h=30)
        cmds.text(al='right', l='Email Address : ')
        cmds.textField(tx='burasedborvon@gmail.com', w=ct_w_percentile * .7)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2, columnWidth2=(ct_w_percentile * .2, ct_w_percentile * .8),
                       columnAlign2=['right', 'left'], adj=1, h=30)
        cmds.text(al='right', l='License Key : ')
        cmds.textField(tx='D094DF54-217B4C1F-AB006260-0AC1BDCA1', w=ct_w_percentile * .7)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2, columnWidth2=(ct_w_percentile * .2, ct_w_percentile * .8),
                       columnAlign2=['right', 'left'], adj=1, h=30)
        cmds.text(al='right', l='')
        cmds.button(l='Verify', al='center', w=100)
        cmds.setParent('..')

        cmds.setParent('..') #columnLayout

        cmds.columnLayout(adj=0);cmds.setParent('..')
        cmds.setParent('..') #rowLayout2

        cmds.text(l='', h=30, w=ct_w_percentile)

        cmds.showWindow(win_id)

print(sys.version[0])
#print(gr_license.is_py3)
#print(gr_license.uLib)

#print(gr_license.get_license_verify('D094DF54-217B4C1F-AB006260-0AC1BDCA1'))
gr_license.show_ui()