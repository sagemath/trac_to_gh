# Issue 9436: zodb3 causes downloads during installation

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2010-07-06 14:21:08

Assignee: tbd

CC:  leif


```
Just for the record:

grep -i downloading $SAGE_ROOT/install.log:

Downloading http://download.zope.org/distribution/zdaemon-2.0.0.tar.gz
Downloading http://download.zope.org/distribution/ZConfig-2.5.tar.gz
Downloading http://download.zope.org/distribution/zope.testing-3.5.0.tar.gz
Downloading http://download.zope.org/distribution/zope.proxy-3.4.0.tar.gz


-Leif
```



---

Attachment

Includes zodb3's requirements in the package.


---

Comment by timdumol created at 2010-07-06 14:24:26

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-07-06 14:24:26

Package up at http://sage.math.washington.edu/home/timdumol/zodb3-3.7.0.p4.spkg


---

Comment by rlm created at 2010-07-06 15:40:52

Changing priority from major to blocker.


---

Comment by leif created at 2010-07-06 17:15:21

Built Sage 4.5.alpha4 from scratch with the new zodb3 spkg (p4), now _another_ file is downloaded from another place:

```
...
zodb3-3.7.0.p4/.hg/store/00manifest.i
Finished extraction
****************************************************
Host system
uname -a:
Linux quadriga 2.6.28-18-generic #60-Ubuntu SMP Fri Mar 12 04:26:47 UTC 2010 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: ../src/configure --prefix=/usr --enable-version-specific-runtime-libs --program-suffix=4.5.0 --with-fpmath=sse --enable-arch=core2
Thread model: posix
gcc version 4.5.0 (GCC)
****************************************************
Processing zope.interface-3.6.1.tar.gz
Running zope.interface-3.6.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-oWJHZn/zope.interface-3.6.1/egg-dist-tmp-O8uYAn
Removing zope.interface 3.5.2 from easy-install.pth file
Adding zope.interface 3.6.1 to easy-install.pth file

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.interface-3.6.1-py2.6-linux-x86_64.egg
Processing dependencies for zope.interface==3.6.1
Finished processing dependencies for zope.interface==3.6.1
Processing zope.proxy-3.6.0.zip
Running zope.proxy-3.6.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-v0n6lX/zope.proxy-3.6.0/egg-dist-tmp-gLPbBv
Adding zope.proxy 3.6.0 to easy-install.pth file

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.proxy-3.6.0-py2.6-linux-x86_64.egg
Processing dependencies for zope.proxy==3.6.0
Finished processing dependencies for zope.proxy==3.6.0
Processing zope.testing-3.9.5.tar.gz
Running zope.testing-3.9.5/setup.py -q bdist_egg --dist-dir /tmp/easy_install-0d62W6/zope.testing-3.9.5/egg-dist-tmp-GdpPl2
warning: no files found matching 'sampletests' under directory 'src'
Adding zope.testing 3.9.5 to easy-install.pth file
Installing zope-testrunner script to /home/leif/sage-4.5.alpha4-zodb3-p4/local/bin

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.testing-3.9.5-py2.6.egg
Processing dependencies for zope.testing==3.9.5
Searching for zope.exceptions
Reading http://pypi.python.org/simple/zope.exceptions/
Reading http://svn.zope.org/zope.exceptions
Best match: zope.exceptions 3.6.0
Downloading http://pypi.python.org/packages/source/z/zope.exceptions/zope.exceptions-3.6.0.tar.gz#md5=491779b577a49f547982ff39b3903b1a
Processing zope.exceptions-3.6.0.tar.gz
Running zope.exceptions-3.6.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-DdGPSF/zope.exceptions-3.6.0/egg-dist-tmp-9J8MOH
Adding zope.exceptions 3.6.0 to easy-install.pth file

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.exceptions-3.6.0-py2.6.egg
Finished processing dependencies for zope.testing==3.9.5
Processing ZConfig-2.8.0.tar.gz
...
```



---

Comment by leif created at 2010-07-06 17:15:34

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-07-07 15:22:20

New version with zope.exceptions now at the same url. I checked the requirements of each package recursively, so there should be no more downloads.


---

Comment by timdumol created at 2010-07-07 15:22:20

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-07-08 13:33:28

Changing keywords from "" to "undesired download, zope, zodb3".


---

Comment by leif created at 2010-07-08 13:33:28

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-07-08 13:33:28

*Works as advertised.*

Ubuntu 9.04, Sage 4.5.alpha4 with SageNB 0.8.1 (#9430) and zodb3 3.7.0.p4 (here) built from scratch.


---

Comment by rlm created at 2010-07-08 19:08:18

Resolution: fixed
