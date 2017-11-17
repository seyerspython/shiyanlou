#!/usr/bin/env python3
import sys
##计算社保函数
def social_taxs(salary):
    social_taxs=salary*(8/100+2/100+0.5/100+6/100)
    return social_taxs

##计算应纳税额
def tax_payable(salary,social_taxs):
    tax_payable=salary-social_taxs-3500
    return tax_payable

##计算税后工资
def taxed_salary(salary,social_taxs,tax_payable):
      if tax_payable<=1500 and tax_payable>0:
         salary=salary-social_taxs-tax_payable*0.03
      elif tax_payable>1500 and tax_payable<=4500 :
         salary=salary-social_taxs-(tax_payable*0.1-105)
      elif tax_payable>4500 and tax_payable<=9000 :
         salary=salary-social_taxs-(tax_payable*0.2-555)
      elif tax_payable>9000 and tax_payable<=35000 :
         salary=salary-social_taxs-(tax_payable*0.25-1005)
      elif tax_payable>35000 and tax_payable<=55000 :
         salary=salary-social_taxs-(tax_payable*0.3-2755)
      elif tax_payable>55000 and tax_payable<=80000 :
         salary=salary-social_taxs-(tax_payable*0.35-5505)
      elif tax_payable>80000 :
         salary=salary-social_taxs-(tax_payable*0.45-13505)
      return salary

      
if __name__=="__main__":
   hr_dict={}
   if len(sys.argv)==1:
      print("parameter Error")
   else:
      for arg in sys.argv[1:]:
      
         try:
            id_salist=arg.split(':')         
            if len(id_salist)==2:
              salary=int(id_salist[1])
              social_tax=social_taxs(salary)
              tax_pay=tax_payable(salary,social_tax)           
              ta_salary=taxed_salary(salary,social_tax,tax_pay)
              hr_dict[id_salist[0]]=ta_salary           
            else:
              print("Parameter Error")
         except:
            print("Parameter Error")
      if hr_dict!=None:
        for h in hr_dict:
           print(h+":%.2f"%hr_dict[h]) 
   
