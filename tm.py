import os, sys


_B = {"_B": "DXT1"}
_R = {"_R": "BC5_UNORM"}
_I = {"_I": "DXT5"}
_N = {"_N": "BC5_UNORM"}
_CoatR = {"_CoatR": "BC4_UNORM"}
_DirtMask = {"_DirtMask": "BC4_UNORM"}
_AO = {"_AO": "DXT1"}
suffixes = [_B, _R, _I, _N, _CoatR, _DirtMask, _AO]


def convert_png_to_dds(path):
    for suffix in suffixes:
        files = []
        for _file in os.listdir(path):
            if _file.endswith(list(suffix.keys())[0] + ".png"):
                print("Converting " + _file + " with " + list(suffix.values())[0])
                os.system("texconv.exe -f " + list(suffix.values())[0] + " " + path + "\\" + _file)
                newFile = _file.replace(".png",".dds")
                os.rename(newFile, path + "/" + newFile)


convert_png_to_dds(sys.argv[1])