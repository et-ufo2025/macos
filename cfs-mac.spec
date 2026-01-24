# cfs-mac.spec (示例)
# 说明：根据实际路径调整 pyside6 插件路径与图标路径
from PyInstaller.utils.hooks import collect_all, collect_data_files
import PySide6
import os

hiddenimports = [
    # 根据 PyInstaller 报错补充
    "asyncio", "aiohttp", "ssl", "socket"
]

datas = []
# 收集 PySide6 的数据文件（插件、翻译等）
pyside6_data = collect_data_files('PySide6')
datas += pyside6_data

# 如果你有额外资源（图标等），显式加入
datas += [
    ('cfs.icns', '.'),  # 将图标放到可执行同目录
]

a = Analysis(
    ['cfs-mac.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=['tkinter', 'unittest', 'pytest'],
)

pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='CloudflareScan',
    icon='cfs.icns',
    debug=False,
    strip=False,
    upx=False,
    console=False
)
