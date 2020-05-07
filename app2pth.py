
import os

lstIgnore = ['.vscode','__pycache__','.svn','apache','app','doc','pth','wsgi','templates','static','rundata','log','tmp','temp','dist','build','exception']
lstIgnore.extend(['AdminLTE','aadmin','ahome','test']) 

def ignorepath(path):
    lst1 = path.split('\\')
    for v1 in lst1:
        if not v1:continue
        if v1 in lstIgnore:return True
    return False

def getRootPath(*args):
    rtn = os.getcwd()
    if args:rtn = os.path.join(rtn, *args)
    rtn = os.path.abspath(rtn)
    return rtn

def save2pth(pathfilename,data):
    try:
        with open(pathfilename,'w', encoding='cp936') as file_:
            file_.write(data)
            file_.close()
    #except :
    except Exception as e:
        print(str(e))
        return False
    return True

if __name__ == "__main__":
    path1 = getRootPath()
    len1 = len(path1)
    lstReturn = []
    for root, dirs, files in os.walk(path1):
        if path1 == root:continue
        root1 = root[len1:]
        if ignorepath(root1):continue
        print("root", root1)  # 当前目录路径
        root1 = root1.lower()
        lstReturn.append(root)

    str1 = '\r\n'.join(lstReturn)

    if not os.path.exists('pth'):os.makedirs('pth')
    save2pth(r'pth\base.pth',str1)
    
    if os.path.exists('app'):
        save2pth(r'app\Lib\site-packages\base.pth',str1)
