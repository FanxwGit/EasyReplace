## README
[中文](Readme_zh.md), [English](Readme_en.md)

---

# EasyReplace

EasyReplace是个图床换源工具，用于批量更换博客中图片链接的CDN源。当你使用的CDN服务不可用时，只需运行该工具，快速替换指定文件夹下所有.md文件中图片链接的CDN源，并支持备份和撤回改动。通过这个工具，你可以轻松地切换CDN加速服务，确保博客内容在不同网络环境下都能正常访问。

---

博客的图床经常会出现需要更换cdn，这样国内网络才能正常打开，这个时候就需要替换图片链接，这个脚本就是为了解决这个问题。

比如常用的'https://cdn.jsdelivr.net'这个cdn加速，有时候会挂掉，需要替换'http://fastly.jsdelivr.net' 或者其他的cdn加速。

脚本枚举所有.md文件，更换图片链接的前缀的CDN


## 使用方法

1. 查看手册

```
python Replace.py -h
usage: Replace.py [-h] -dir DIR -old OLD -new NEW [-clear] [-drawback]

e.g. python Replace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastly.jsdelivr.net"

options:
  -h, --help  show this help message and exit
  -dir DIR    The directory to change
  -old OLD    The old text to change
  -new NEW    The new text to change
  -clear      Clear all .back files
  -drawback   Restore all .back files
```

2. 替换图片链接，程序会枚举所有.md文件，更换图片链接的前缀的CDN，并且生成备份文件`.back`

例如

```
python Replace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastlyjsdelivr.net"
```


3. (可选)撤回改动, 把`.back`文件替换回去

```
python Replace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastlyjsdelivr.net" -drawback
```

4. (可选)删除备份文件`.back`
```
python Replace.py -dir "/Users/fxw/OneDrive/note" -old "https://cdn.jsdelivr.net" -new "http://fastlyjsdelivr.net" -clear
```

