#!/usr/bin/evn python3
import sys
import csv
##配置类 
class Config(object):
    def __init__(self,configfile):
        self._config={}
        with open(configfile) as file:
            for line in file:
                cf_line=line.split('=')
                self._config[cf_line[0].strip(' ')]=float(cf_line[1])
    def get_config(self,key_name):
        return self._config[key_name]
    def get_JiShuL(self):
        return self.get_config('JiShuL')
    def get_JiShuH(self):
        return self.get_config('JiShuH')
    def get_taxrate():
        return sum([self.get_config('YangLao'),self.get_config('YiLiao'),self.get_cofnig('ShiYe'),self.get_config('GongShang'),self.get_config('ShengYu'),self.get_config('GongJiJin')])
##员工数据类
class UserData(object):
    def __init__(self,userdatafile):
        self.userdata={}  ##员工数据字典
        with open(userdatafile) as file:
            for line in file:
                ud_line=line.split(',')
                self.userdata[ud_line[0].strip(' ')]=int(float(ud_line[1]))
            
    ##税后工资计算函数         
    def calculator(self):
        salary_list=[]
        for ud in self.userdata:
            if self.userdata[ud]<=config.get_JiShuL():
                
    ##计算个税金额
        
    ##计算税后工资
    ##输出文件
    def dumptofile(self,outputfile):
        for ud in self.userdata:
            self.userdata[ud]
            self.calculator()
            with open(outputfile,'a') as file:
                file.write(str(ud)+','+str(self.userdata[ud])+','+'/n')
##主程序
if __name__=='__main__':
    if len(sys.argv)>0 :
        args=sys.argv[1:]
        index=args.index('-c')
        configfile=args[index+1]
        config=Config(configfile)
        index=args.index('-d')
        userdatefile=args[index+1]
        index=args.index('-o')
        outputfile=args[index+1]
        userdata=UserData(userdatefile)
        userdata.calculator()
        

        userdata.dumptofile(outputfile)
        
