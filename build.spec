# -*- mode: python ; coding: utf-8 -*-
import os


block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/heath/Code/qt-calculator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name="Heath's Calculator",
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name="Heath's Calculator")
app = BUNDLE(coll,
             name="Heath's Calculator.app",
             info_plist={'NSHighResolutionCapable': 'True'},
             icon=os.path.join('images', 'program_icon.icns'),
             bundle_identifier=None)