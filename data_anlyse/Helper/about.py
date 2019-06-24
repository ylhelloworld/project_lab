__all__=["info"]

author='Yang Long'
description="some helper tools"
def info():
    print("author:YangLong")
    print("description: some helper tools")

def test(param1,param2='param2',param3='param3'):
    print('param1:%s,param2:%s,param3:%s'%(param1,param2,param3))