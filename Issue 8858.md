# Issue 8858: 4.4.1 accessing internet during compilation

Issue created by migration from https://trac.sagemath.org/ticket/8858

Original creator: was

Original creation time: 2010-05-03 15:01:14

Assignee: jason, was


```
[sage-devel] 4.4.1 accessing internet during compilation 						Inbox		X						 
Reply to all
Harald Schilly to sage-devel
show details 7:39 AM (20 minutes ago)
Hi, while watching the compilation of 4.4.1 I saw that it stopped
compiling and waited for a package to download. I'm curious if this is
intended or just a strange glitch. At least my idea of a self
containing source package is that it doesn't need to download software
from the internet!

...
creating 'dist/Sphinx-0.6.3-py2.6.egg' and adding 'build/bdist.linux-
i686/egg' to it
removing 'build/bdist.linux-i686/egg' (and everything under it)
Processing Sphinx-0.6.3-py2.6.egg
creating /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/
site-packages/Sphinx-0.6.3-py2.6.egg
Extracting Sphinx-0.6.3-py2.6.egg to /scratch/scratch/schilly/sage/
sage-4.4.1/local/lib/python2.6/site-packages
Adding Sphinx 0.6.3 to easy-install.pth file
Installing sphinx-build script to /scratch/scratch/schilly/sage/
sage-4.4.1/local/bin
Installing sphinx-quickstart script to /scratch/scratch/schilly/sage/
sage-4.4.1/local/bin
Installing sphinx-autogen script to /scratch/scratch/schilly/sage/
sage-4.4.1/local/bin

Installed /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/
site-packages/Sphinx-0.6.3-py2.6.egg
Processing dependencies for Sphinx==0.6.3
Searching for docutils==0.5
Best match: docutils 0.5
Adding docutils 0.5 to easy-install.pth file

Using /scratch/scratch/schilly/sage/sage-4.4.1/local/lib/python2.6/
site-packages
Searching for Jinja2==2.3.1
Reading http://pypi.python.org/simple/Jinja2/
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/
Download error: [Errno 110] Connection timed out -- Some packages may
not be found!
Reading http://jinja.pocoo.org/

And well, it waits the usual 2 minutes socket timeout in each line and
the pocoo website is really down.

H
```



---

Comment by schilly created at 2010-05-03 15:15:47

I think that's not the notebook component, because it affects the sphinx package. john cremona had another problem with the notebook spkg. So, there are at least two issues like that and probably even more?


---

Comment by was created at 2010-05-03 15:59:25

From Tim, who also points out that I was wrong:


```
This isn't related to my new package includes. Jinja2 wasn't one of those new packages. 
The problem is that SageNB is installed before Jinja2 is installed, so it's more of
a problem in the dependency script.
```



---

Comment by mvngu created at 2010-05-05 11:30:37

Resolution: duplicate


---

Comment by mvngu created at 2010-05-05 11:30:37

Closing this as a duplicate of #8861.
