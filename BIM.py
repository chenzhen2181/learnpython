# -*- coding: utf-8 -*-
height=input('身高（m）：')
weight=input('体重（kg）：')
BMI=float(weight)/float(height)**2
BMI_ref = ('偏瘦','正常','偏胖','肥胖','重度肥胖','极重度肥胖')
BMI_data=(18.5,24,27,30,40)
i=0
for n in BMI_ref:
    if BMI<BMI_data[0]:
        print('BMI=%.2f,' % BMI + "您体型（中国标准）"+ str(BMI_ref[0]))
        break
    if BMI_data[i-1]<BMI<BMI_data[i]:
        print('BMI=%.2f,' %BMI + "您体型（中国标准）"+str(BMI_ref[i]) )
        break
    if BMI > BMI_data[4]:
        print('BMI=%.2f,'  % BMI + "您体型（中国标准）"+ str(BMI_ref[5]))
        break
    i=i+1
print('BMI=%.2f' % BMI)


