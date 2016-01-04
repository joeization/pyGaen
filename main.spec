# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\joe\\Desktop\\pyGaen'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          Tree('src', prefix='src'),
          Tree('img', prefix='img'),
          Tree('sfx', prefix='sfx'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=None,
          upx=True,
          console=True )
