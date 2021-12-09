# ROPSlap
Automatic Return Oriented Programming exploit generator

Takes a vulnerable program, calculates buffer overflow offset and produces an input file containing ROPChain to call execve

## Vagrant VM

Although ROPSlap has been tested to work outside of a virtual machine, we cannot guarantee it will work on every platform and setup. For this reason we have included a vagrantfile that can be used to setup a virtual machine to run ROPSlap on. With vagrant installed, run the following commands inside of the root of the repository

```bash
vagrant up
vagrant ssh
cd /vagrant
```
The /vagrant directory will hold all files included in the repository.

## Setup

In order to get started with this tool we will first need to install some dependencies required for ROPGadget. 

```bash
sudo apt update
sudo apt install -y python3-pip gdb gcc-multilib
pip3 install capstone
```

## Usage

To generate the rop chain for a given vulnerable file run the following command from the root of the repository

```bash
./ropslap.sh <VULNERABLE_FILE> <EXECVE_CALL> <ENVIRONMENT_VARS>
```

Where <VULNERABLE_FILE> is replaced with the path to the vulnerable file that we are trying execute and <EXECVE_CALL> is replaced with the program that the exploit is going to run. <ENVIRONMENT_VARS> is an optional argument that is used to specify any necessary environment variables.

Running this command will generate a file called execveChain, in order to exploit vulnerable file that the exploit was generated for we now simply run

```bash
./<VULNERABLE_FILE> execveChain
```

## Vulnfiles

For demonstration purposes a number of files with exploitable buffer overflow vulnerabilities have been included in the vulnfiles directory. These vulnerable files have been compiled using gcc under specific conditions that allows ROPSlap to work. When compiling new vulnerable files for ROPSlap to generate exploits the following command should be used

```bash
gcc -fno-stack-protector -m32 -static vulnfile.c -o vulnfile
```
