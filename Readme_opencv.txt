Step1: Updated the python:
mantejsingh@ubuntu:~$ sudo apt-get install -y python3-pip

Step2: Installing Anaconda
mantejsingh@ubuntu:~$ bash Anaconda3-4.3.1-Linux-x86_64.sh

Step3: setting env path.
mantejsingh@ubuntu:~$ export PATH=~/anaconda3/bin:$PATH
mantejsingh@ubuntu:~$ conda --version

Step4: Installing OPCV3
mantejsingh@ubuntu:~$ conda install opencv

Step5: Installing ffmpeg
mantejsingh@ubuntu:~$ conda install -c menpo ffmpeg=3.1.3

Shantnu, do i need to enable ffmpeg?.
I am not getting any source for enabling it