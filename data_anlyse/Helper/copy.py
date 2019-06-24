import os
path_s = 'D:\\Work'
path_t = '\\\\10.104.101.104\\Doc\\Work'

def copy_file(paths,patht):
    for filename in os.listdir(paths):
        filename_s = paths+os.sep+filename
        filename_t = patht+os.sep+filename
        if os.path.isdir(filename_s):
            if not os.path.exists(filename_t):
                os.mkdir(filename_t)  
            copy_file(filename_s,filename_t) # 递归
        else:
            if not os.path.exists(filename_t):
                    file=open(filename_t,'w') 
                    file.close()
            #print(filename_s+"  "+str(os.path.getsize(filename_s)))
            #print(filename_t+"  "+str(os.path.getsize(filename_t)))
            if os.path.getsize(filename_s)!=os.path.getsize(filename_t):
                with open(filename_s,'rb') as f_s:
                    with open(filename_t,'wb') as f_t: 
                        print('[*]  Source :'+filename_s+" " +str(os.path.getsize(filename_s)))
                        print('[*]  Target :'+filename_t+" " +str(os.path.getsize(filename_t)))
                        f_t.writelines(f_s.readlines())
                        f_s.close()
                        f_t.close() 

def clear_file(paths,patht):
    for filename in os.listdir(patht):
        filename_s = paths+os.sep+filename
        filename_t = patht+os.sep+filename

        if os.path.isdir(filename_t):
            if  os.path.exists(filename_s): 
                clear_file(filename_s,filename_t) # 递归
        if not os.path.exists(filename_s):
            if  os.path.isfile(filename_t):
                print('[*] DELETE FILE:'+filename_t)
                os.remove(filename_t) 
            else:
                print('[*] DELETE DIR:'+filename_t)
                os.removedirs(filename_t) 
# copy_file(path_s,path_t)
# clear_file(path_s,path_t)