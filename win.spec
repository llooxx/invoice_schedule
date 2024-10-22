# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        (r'C:\Users\linoz\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyzbar\libiconv.dll', '.'),
        (r'C:\Users\linoz\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyzbar\libzbar-64.dll', '.'),
        (r'C:\Users\linoz\AppData\Local\Programs\Python\Python311\Lib\site-packages\pypdfium2_raw\pdfium.dll','.'),
        ],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['img\\invoice.ico'],
)


coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
