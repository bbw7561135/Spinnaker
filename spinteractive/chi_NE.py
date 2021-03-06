#############################################################################
###SCRIPT TO CALCULATE CHI^2 FOR CR TRANSPORT MODELS
###VOLKER HEESEN, FEBRUARY 2016
############################################################################


import math

###NUMBER OF DATA POINTS
N = 12
###NUMBER OF FIT PARAMETERS
n = 0

###READ THE FILES IN
z_read=[]
i20_read=[]
i20_error_read=[]
alpha_read=[]
alpha_error_read=[]
i20_model_read=[]
alpha_model_read=[]


with open('alpha_NE.dat') as inf:
    for line in inf:
        parts= line.split() # split line into parts
        z_read.append(parts[0])   # print column 2
        i20_read.append(parts[1])
        i20_error_read.append(parts[2])
        alpha_read.append(parts[3])
        alpha_error_read.append(parts[4])

with open('int.dat') as inf:
    for line in inf:
        parts= line.split() # split line into parts
        i20_model_read.append(parts[1])
        alpha_model_read.append(parts[5])

###DEFINE NEW VARIABLES        
z=[]
i20=[]
i20_error=[]
alpha=[]
alpha_error=[]
i20_model=[]
alpha_model=[]

for i in range(1,N+1):
    z.append(float(z_read[i]))
    i20.append(float(i20_read[i]))
    i20_error.append(float(i20_error_read[i]))
    alpha.append(float(alpha_read[i]))
    alpha_error.append(float(alpha_error_read[i]))
    i20_model.append(float(i20_model_read[i]))
    alpha_model.append(float(alpha_model_read[i]))


###PRINT VALUES FOR CONTROL
print 'Control values'

print 'z I1, I_error, alpha, alpha_error, I_model, alpha_model'

for i in range(0,N):
    print z[i], i20[i], i20_error[i], alpha[i], alpha_error[i], i20_model[i], alpha_model[i]
print '----------------------------------------------------------------------'

###CALCULATE CHI^2
def res(int,mod,sigma):
    return pow((int-mod)/sigma,2)


i20_chi = 0
print ' z, I1, I1_error, residual^2'

for i in range(0,N):
        print z[i], i20[i], i20_error[i], res(i20[i],i20_model[i],i20_error[i])
        i20_chi = i20_chi + res(i20[i],i20_model[i],i20_error[i])
        
print '===> i20 Chi^2=', i20_chi / (N - n - 1)
print '----------------------------------------------------------------------'

alpha_chi = 0

print ' z, alpha, alpha_eror, residual^2'

for i in range(0,N):
        print z[i], alpha[i], alpha_error[i], res(alpha[i],alpha_model[i],alpha_error[i])
        alpha_chi = alpha_chi + res(alpha[i],alpha_model[i],alpha_error[i])
        

print '===> alpha Chi^2=', alpha_chi / (N - n - 1)


print '----------------------------------------------------------------------'

dof = 2 * N -n - 1
print '===> Total Chi^2=', (i20_chi + alpha_chi) / dof, '(dof=', dof,')'
print '----------------------------------------------------------------------'
