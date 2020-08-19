"""
Before running this script, make sure that
You have ssh-key. If you are not, generate ssh-key
by commanding '$ ssh-keygen' command.
For example, if you want to allow ssh-nopasswd-login to
user John, Cathy and Kail, the first thing you have to do
before executing this script is,

John@yboot:~$ ssh-keygen
Cathy@yboot:~$ ssh-keygen
Kail@yboot:~$ ssh-keygen

Then these users will get publickey and private key in
~/.ssh/id_rsa
~/.ssh/id_rsa.pub

The following code is distributing public keys of these uses to node y101.
"""

import subprocess as sp
import sys, os

nodes=[]
homes = []
homename = 'yhome%01d'
nodename = 'y%03d'

#for number in xrange(1, 4):
#	homes.append(homename % number)
#	nodes.append(homename % number)

#for number in xrange(101,200):
#	nodes.append(nodename % number)

for number in range(101,121):
    nodes.append(nodename % number)

#nodes.append("cpunode")
#nodes.append("gpunode")
#nodes.append("gpunode.no.ana")
#nodes.append("gpunode.ana")
#nodes.append("gpunode.ana.cuda")
#nodes.append("gpunode.ana.cuda.ompi-dev")
#nodes.append("gpunode.ana.cuda.ompi-dev.mpi4py")

def ext_exec_wait(cmd):
    out, err = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE).communicate()
    if err != '': print(err)
    return out

passwd = sys.argv[1]

users = ['lsy','intro15']

for user in users:
    command = 'sshpass -p "{0}" ssh-copy-id {1}@y101'.format(passwd,user)
    print(command)
    ext_exec_wait(command)
