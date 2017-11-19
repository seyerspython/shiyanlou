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
##员工数据类
class UserData(object):
    def __init__(self,userdatafile):
        self.userdata={}  ##员工数据字典
        with open(userdatafile) as file:
            for line in file:
                ud_line=line.split(',')
                self.userdata[ud_line[0].strip(' ')]=int(float(ud_line[1]))
            
    ##税后工资计算函数         
    def calculator(self,config_class):
        for ud in self.userdata:
            if self.userdata[ud]<=self.config.get_config('JiShuL'):
                self.
            
        if self.tax_payable<=1500 and self.tax_payable>0:
            self.salary=self.salary-self.social_taxs-self.tax_payable*0.03
        elif self.tax_payable>1500 and self.tax_payable<=4500 :
            self.salary=self.salary-self.social_taxs-(self.tax_payable*0.1-105)
        elif self.tax_payable>4500 and self.tax_payable<=9000 :
            self.salary=self.salary-self.social_taxs-(self.tax_payable*0.2-555)
        elif self.tax_payable>9000 and self.tax_payable<=35000 :
            self.salary=self.salary-self.social_taxs-(self.tax_payable*0.25-1005)
        elif self.tax_payable>35000 and self.tax_payable<=55000 :
            self.salary=self.salary-self.social_taxs-(self.tax_payable*0.3-2755)
        elif self.tax_payable>55000 and self.tax_payable<=80000 :
            self.salary=self.salary-self.social_taxs-(self.tax_payable*0.35-5505)
        elif self.tax_payable>80000 :
            self.salary=self.salary-self.social_taxs-(self.tax_payable*0.45-13505)
        else:
            self.salary=self.salary-self.social_taxs
        

    ##计算社保金额函数
    def cal_social(self):
        
        if 0<self.userdata[ud]<=config.get_config('JiShuL'):
            self.social_taxs=config.get_config('JiShuL')*(0.08+0.02+0.005+0+0+0.06)
        elif config.get_config('JiShuL')<self.salary<config.get_config('JiShuH'):
            self.social_taxs=self.salary*(0.08+0.02+0.005+0+0+0.06)
        elif config.get_config('JiShuH')<=self.salary:
            self.socail_taxs=16446*(0.08+0.02+0.005+0+0+0.06)
        self.ta_payable=self.salary-self.socail_taxs
        
        
    ##计算个税金额
        
    ##计算税后工资
    ##输出文件
    def dumptofile(self,outputfile):
        for ud in self.userdata:
            self.userdata[ud]
            self.calculator()
            with open(outputfile,'a') as file:
                file.write(str(ud)+','+str(self.userdate[ud])+','+'/n')
##主程序
if __name__=='__main__':
    if len(sys.argv)>0 :
        args=sys.argv[1:]
        index=args.index('-c')
        configfile=args[index+1]
        index=args.index('-d')
        userdatefile=args[index+1]
        config=Config(configfile)
        userdata=UserData(userdatefile)
        userdata.cal_social(config)
        
