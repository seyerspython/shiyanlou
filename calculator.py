#!/usr/bin/env python3
import sys
import csv
import os
##配置类 
class Config(object):
    def __init__(self,configfile):
        self._config={}
        try:
            with open(configfile) as file:
                for line in file:
                    try:
                        cf_line=line.split('=')
                        self._config[cf_line[0].strip(' ')]=float(cf_line[1])
                    except:
                        print("Config Error")
        except IOError:
             print("Config File not found or not accessiable")
    def get_config(self,key_name):
        try:
            return self._config[key_name]
        except:
           print("Config Error")
    def get_JiShuL(self):
        try:
            return self.get_config('JiShuL')
        except:
            print("Config Error")
    def get_JiShuH(self):
        try:
            return self.get_config('JiShuH')
        except:
            print("Config Error")
    def get_s_taxrate(self):
        try:
            return sum([self.get_config('YangLao'),self.get_config('YiLiao'),self.get_config('ShiYe'),self.get_config('GongShang'),self.get_config('ShengYu'),self.get_config('GongJiJin')])
        except:
            print("Config Error")
##员工数据类
class UserData(object):
    def __init__(self,userdatafile):
        self.userdata={}  ##员工数据字典
        self.salary_list=[]
        ##打开CSV文件
        try:
            with open(userdatafile) as csvfile:
                reader=csv.reader(csvfile) 
                for line in reader:
                    try:
                        self.userdata[line[0].strip(' ')]=int(float(line[1]))
                    except:
                        print("Userdata Error")
                        exit()
        except IOError:
            print("User salary File not found or not accessiable")
            
    ##税后工资计算函数         
    def calculator(self):
        for ud in self.userdata:
            try:
                salary=self.userdata[ud]
                scial=self.scial_tax(salary)
                tax_pay_able=self.tax_payable(salary,scial)
                tax=self.tax_rate(tax_pay_able)
                taxed_salary=salary-scial-tax
                single_salary=[ud,salary,'{:.2f}'.format(scial),'{:.2f}'.format(tax),'{:.2f}'.format(taxed_salary)]
                self.salary_list.append(single_salary)
            except:
                print("Userdate Error")
           
            
            
    ##计算社保
    def scial_tax(self,salary):
        if salary<=config.get_JiShuL():
            base_social=config.get_JiShuL()*config.get_s_taxrate()
        elif salary>=config.get_JiShuH():
            base_social=config.get_JiShuH()*config.get_s_taxrate()
        elif config.get_JiShuL()<salary<config.get_JiShuH():
            base_social=salary*config.get_s_taxrate()
        return base_social
    ##计算应纳税金额
    def tax_payable(self,salary,scial):
        return salary-scial-3500
    ##计算税额
    def tax_rate(self,tax_pay):
        if 0<tax_pay<=1500:
            tax_pay=tax_pay*0.03
        elif 1500<tax_pay<=4500:
            tax_pay=tax_pay*0.1-105
        elif 4500<tax_pay<=9000:
            tax_pay=tax_pay*0.2-555
        elif 9000<tax_pay<=35000:
            tax_pay=tax_pay*0.25-1005
        elif 35000<tax_pay<=55000:
            tax_pay=tax_pay*0.3-2755
        elif 55000<tax_pay<=80000:
            tax_pay=tax_pay*0.35-5505
        elif 80000<tax_pay:
            tax_pay=tax_pay*0.45-13505
        else:
            tax_pay=0
        return tax_pay
            
           
                
                
        ##计算税后工资
    ##输出文件
    def dumptofile(self,outputfile):
        for row in self.salary_list:
            try:            
                with open(outputfile,'a') as csvfile:
                    try:                
                        writer=csv.writer(csvfile)
                        writer.writerow(row)
                    except:
                        print("Writer Error") 
            except IOError:
                print("Gongzi File is not found or not accessiable")
            
##主程序
if __name__=='__main__':
    if len(sys.argv)>0 :
        
            args=sys.argv[1:]
            configfile=args[args.index('-c')+1]
            userdatefile=args[args.index('-d')+1]
            outputfile=args[args.index('-o')+1]
            config=Config(configfile)             
            userdata=UserData(userdatefile)
            userdata.calculator()
                
            userdata.dumptofile(outputfile)
                    
