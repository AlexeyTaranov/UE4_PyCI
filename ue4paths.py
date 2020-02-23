from os import path

# Absolute path to Microsoft Compiler
MSVC = r'C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin\MSBuild.exe'

# Absolute path to Unreal Engine folder
_UE_Path = r'D:\UE_4.24'

# Relative paths to engine parts
_UBT_relative = r'Engine\Binaries\DotNET\UnrealBuildTool.exe'
_UAT_relative = r'Engine\Build\BatchFiles\RunUAT.bat'
_UEditor_relative = r'Engine\Binaries\Win64\UE4Editor.exe'


def ubt():
    return path.join(_UE_Path, _UBT_relative)


def uat():
    return path.join(_UE_Path, _UAT_relative)


def editor():
    return path.join(_UE_Path, _UEditor_relative)
