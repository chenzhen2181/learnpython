# -*- coding: utf-8 -*-
height = input('身高（m）：')
weight = input('体重（kg）：')
BMI = float(weight) / float(height) ** 2
BMI_ref = ('偏瘦', '正常', '偏胖', '肥胖', '重度肥胖', '极重度肥胖')
BMI_data = (18.5, 24, 27, 30, 40)
strr ="您体型（中国标准）属于"
for i in range(0, len(BMI_ref) - 1):
	if BMI < BMI_data[0]:
		print('BMI=%.2f,' % BMI + strr + str(BMI_ref[0]))
		break
	if BMI_data[i - 1] < BMI < BMI_data[i]:
		print('BMI=%.2f,' % BMI + strr  + str(BMI_ref[i]))
		break
	if BMI > BMI_data[4]:
		print('BMI=%.2f,' % BMI + strr  + str(BMI_ref[5]))
		break
print('BMI=%.2f' % BMI)
