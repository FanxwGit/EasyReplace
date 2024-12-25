import os
import argparse

#把所有后缀为suffix的文件中文本的old替换为new，并且备份新文件
def Change(suffix, oldText, newText, dir):
    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(suffix):
                fName = os.path.join(root, file)
                
                # 备份源文件
                backupName = fName + '.back'
                cmd = 'cp "%s" "%s"' % (fName, backupName)
                os.system(cmd)
                
                # 读取原文件内容并替换
                F = open(fName, 'r').read()
                new = F.replace(oldText, newText)
                
                # 写入替换后的内容
                open(fName, 'w').write(new)

#删除所有.back文件，应用改动，无法撤回
def DeleteBack(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.back'):
                fName = os.path.join(root, file)
                os.remove(fName)

#把.back文件都回复成原文件，撤回改动
def RestoreBack(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.back'):
                backFile = os.path.join(root, file)
                newFile = backFile[:-5]
                cmd = 'mv "%s" "%s"' % (backFile, newFile)
                os.system(cmd)




    
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='e.g. python %s -dir "/Users/fxw/OneDrive/note"  -old "https://cdn.jsdelivr.net" -new "http://fastly.jsdelivr.net"' % (os.path.basename(__file__)))
    parser.add_argument('-dir', help='The directory to change', required=True)
    parser.add_argument('-old', help='The old text to change', required=True)
    parser.add_argument('-new', help='The new text to change', required=True)
    parser.add_argument('-clear', help='Clear all .back files', action='store_true')
    parser.add_argument('-drawback', help='Restore all .back files', action='store_true')
    
    args = parser.parse_args()
    dir = args.dir
    oldText = args.old
    newText = args.new

    Change('.md', oldText, newText, dir)

    if args.clear and args.drawback:
        print("ERROR: -clear and -drawback can't be used together")
        exit(1)

    if args.clear:
        DeleteBack(dir)

    if args.drawback:
        RestoreBack(dir)
