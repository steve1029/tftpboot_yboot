import subprocess as sp

nodes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	nodes.append(homename % number)

#for number in xrange(101,109):
#	nodes.append(nodename % number)

for number in xrange(205,213):
	nodes.append(nodename % number)


def ext_exec_wait(cmd):
	out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
	if err != '': print err
	return out

for node in nodes:
	print '%s: sending rebooting signal using ssh' % node
	command = 'rsh %s /sbin/reboot' % node
	print ext_exec_wait(command)
