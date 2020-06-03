# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data,new_record),axis=0)

#print(census)
age = census[:,0]
#print(age)

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

race_0,race_1,race_2,race_3,race_4 = [],[],[],[],[]
for i in census:
    k = i[2]
    if k==0:
        race_0.append(i)
    elif k==1:
        race_1.append(i)
    elif k==2:
        race_2.append(i)
    elif k==3:
        race_3.append(i)
    else:
        race_4.append(i)

race_0 = np.asarray(race_0)
race_1 = np.asarray(race_1)
race_2 = np.asarray(race_2)
race_3 = np.asarray(race_3)
race_4 = np.asarray(race_4)


len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = min(len_0,len_1,len_2,len_3,len_4)
#print(minority_race)

senior_citizens = census[census[:,0]>60]

working_hours_sum = sum(senior_citizens[:,6])

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum/senior_citizens_len

print(avg_working_hours)

high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high,avg_pay_low)


