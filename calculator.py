#!/usr/bin/env python3
import sys
if len(sys.argv) >2:
   print("Parameter Error")
else:
   try:
      money=int(sys.argv[1])
      taxmoney=money-3500
      if taxmoney<=1500 :
         tax=taxmoney*0.03
      elif taxmoney>1500 and taxmoney<=4500 :
         tax=taxmoney*0.1-105
      elif taxmoney>4500 and taxmoney<=9000 :
         tax=taxmoney*0.2-555
      elif taxmoney>9000 and taxmoney<=35000 :
         tax=taxmoney*0.25-1005
      elif taxmoney>35000 and taxmoney<=55000 :
         tax=taxmoney*0.3-2755
      elif taxmoney>55000 and taxmoney<=80000 :
         tax=taxmoney*5505
      elif taxmoney>80000 :
         tax=taxmoney*0.45-13505
      print(format(tax,".2f"))
   except:
      print("Parameter Error")
   
