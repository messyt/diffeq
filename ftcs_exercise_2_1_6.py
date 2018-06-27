# Victor Zhang, June 26, 2018
# FTCS algorithm for solving linear wave equation
# Python

### Imports

import numpy as np
#from mpmath import mp ## says no module named mpmath; need if want pi to high precision

#mp.dps = 16

### Constants

jx = 100 ## This should be constant.

### Arrays

# Initializing Numpy arrays of size 100 with entries as 0's
x = np.zeros(jx)
u = np.zeros(jx)
f = np.zeros(jx)

### Variables

## Time control parameters
nstop = 100
nskip = 50

## Counters
time = 0.0
ns = 0
nx = nstop/nskip + 1

## Velocity
cs = 1.0

### Setting Initial Conditions

#pi = mp.pi ## if mpmath exists, then can use this for high precision in pi
pi = np.pi

####### Checking if numpy arrays work as intended; they do
#x = np.append(x,2)
#u = np.append(u,3.2)
#print pi
#######

## grid
dx = 1.0
x[0] = dx
for i in range(0,jx-1):
    x[i+1] = x[i] + dx

## variable
for i in range(0,jx/2):
    u[i] = 1.0

for i in range(jx/2, jx):
    u[i] = 0.0

### Output initial condition ###

print " " + ' write    step=' + "{:8}".format(ns) + ' time=' + "{:10.3e}".format(time)

file = open("out.dat","w")

# print "Writing " +"{:5}".format(jx) + "," + "{:5}".format(nx) + " to file out.dat"
file.write("{:5}".format(jx) + "," + "{:5}".format(nx) + "\n")

# print "Writing " + "{:5}".format(ns) + ", " + "{:6.2f}".format(time) + " to file out.dat"
file.write("{:5}".format(ns) + "," + "{:6.2f}".format(time) + "\n")

for i in range(0,jx):
	#print "Writing " + "{:5.1f}".format(x[i]) + "," + "{:10.7f}".format(u[i]) + " to file out.dat"
	file.write("{:5.1f}".format(x[i]) + "," + "{:10.7f}".format(u[i]) + "\n")


### Time integration
while ns < nstop:
	ns += 1
	# print 'This is ns: ', ns

	# time spacing
	safety = 0.25
	dt = safety*dx/cs
	time = time + dt

	# solve equation using ftcs
	#
	# start >>>
	for i in range(0,jx-1):
		f[i] = 0.5*cs*(u[i+1]+u[i])

	f[jx-1] = f[jx-2]

	for i in range(1,jx-1):
		u[i] = u[i] - dt/dx*(f[i]-f[i-1])

	u[1] = u[2]
	u[jx-1] = u[jx-2]
	#end >>>

	## data output
	if ns % nskip == 0:
		print " " + ' write    step=' + "{:8}".format(ns) + ' time=' + "{:10.3e}".format(time)
		file.write("{:5}".format(ns) + "," + "{:6.2f}".format(time) + "\n")
		for i in range(0,jx):
			# print "Writing " + "{:5.1f}".format(x[i]) + "," + "{:10.7f}".format(u[i]) + " to file out.dat"
			file.write("{:5.1f}".format(x[i]) + "," + "{:10.7f}".format(u[i]) + "\n")

file.close()

print '### normal stop ###'


"""
print x
print u
print len(x)
print len(u)
"""
