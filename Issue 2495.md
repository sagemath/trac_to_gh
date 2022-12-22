# Issue 2495: Updated experimental Mayavi2 spkg (mayavi_2.1.1) linux only

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-03-12 15:14:59

Assignee: was

Updated to the latest release of Mayavi2.

Now uses vtk-5.0.4 with GL2EPS enabled, so picures can be saved as eps, ps and pdf files!

See:
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/mayavi_2.1.1-20080307.spkg

with dependencies:

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/vtk-5.0.4.spkg 

new version of setuptools (will be in sage-2.10.4 standard): http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/setuptools-0.6c8.spkg

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/wxPython-2.8.7.1.spkg (already in experimental)


---

Comment by cwitty created at 2008-03-13 04:53:26

I used these packages to upgrade from earlier versions of Jaap's packages; the installations went perfectly, and my code (which uses wxPython, vtk, and tvtk (from mayavi)) worked fine after the upgrade.

Debian testing 32-bit x86.


---

Comment by wdj created at 2008-03-13 11:04:50

There is a small typo in
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.1/README.txt
The line
ype ./sage -i mayavi_2.1.1.20080307
should read
ype ./sage -i mayavi_2.1.1-20080307


---

Comment by wdj created at 2008-03-13 13:23:54

I tried this and got the following install error:


```
...
Installing mayavi2 script to /home/wdj/wdj/sagefiles/sage-2.10.3/local/bin

Installed /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.mayavi-2.1.1.dev_r18151-py2.5.egg
Processing dependencies for enthought.mayavi==2.1.1.dev-r18151
Searching for enthought.util>=2.0.3.dev,<3.0a
Best match: enthought.util 2.0.3
Processing enthought.util-2.0.3-py2.5.egg
creating /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.util-2.0.3-py2.5.egg
Extracting enthought.util-2.0.3-py2.5.egg to /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages
Adding enthought.util 2.0.3 to easy-install.pth file

Installed /mnt/drive_hda1/sagefiles/sage-2.10.3/local/lib/python2.5/site-packages/enthought.util-2.0.3-py2.5.egg
Searching for enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a

Link to http://code.enthought.com/enstaller/eggs/source ***BLOCKED*** by --allow-hosts


Link to http://pypi.python.org/simple/enthought.tvtk/ ***BLOCKED*** by --allow-hosts

Couldn't find index page for 'enthought.tvtk' (maybe misspelled?)
Scanning index of all packages (this may take a while)

Link to http://pypi.python.org/simple/ ***BLOCKED*** by --allow-hosts

No local packages or download links found for enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a
error: Could not find suitable distribution for Requirement.parse('enthought.tvtk[plugin,wx]>=2.0.2.dev,<3.0a')

real    34m27.361s
user    24m49.633s
sys     3m27.337s
sage: An error occurred while installing mayavi_2.1.1-20080307
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wdj/wdj/sagefiles/sage-2.10.3/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/wdj/wdj/sagefiles/sage-2.10.3/spkg/build/mayavi_2.1.1-20080307 and type 'make'.
Instead type "/home/wdj/wdj/sagefiles/sage-2.10.3/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wdj/wdj/sagefiles/sage-2.10.3/spkg/build/mayavi_2.1.1-20080307
(When you are done debugging, you can type "exit" to leave the
subshell.)
```



---

Comment by jsp created at 2008-03-14 18:01:18

mayvi2 should be built locally, so no need to get external sources!

Dependencies for now:

install vtk-5.0.4.spkg (see http://trac.sagemath.org/sage_trac/ticket/2493 )

Be sure you have installed wxPython-2.8.7.1.spkg (in experimental already!)
 and setuptools-0.6c8.spkg

Or put everything temporarily in spkg/standard, etcetera see the README.txt


---

Comment by jsp created at 2008-03-16 19:30:17

Replying to [comment:4 wdj]:
> I tried this and got the following install error:
> 
>

Could you try once again following the instructions?

And by doing so also comment on trac ticket #2493


---

Comment by mabshoff created at 2008-03-22 05:10:49

A couple remarks:

 * the build directory should be called src
 * please remove the `.svn` directories, that cuts the size of the spkg in half.
 * check in the file to the repo. I did the initial checkin, so in the future you need to check in only the changes

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/mayavi_2.1.1-20080307.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 05:14:06

Changing component from graphics to experimental package.


---

Comment by mabshoff created at 2008-03-22 05:14:06

One thing I forgot: I very much dislike the fact that it forced automated downloads of things like wxPython in case it isn't installed. It is clear from the readme that those ought to be already installed, but we need to find a more elegant way how to solve the "dependency of non-standard spkg" problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 05:14:06

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-03-22 05:19:47

Merged in the experimental spkg repo.


---

Comment by mabshoff created at 2008-03-22 05:19:47

Resolution: fixed


---

Comment by jsp created at 2008-03-22 17:58:01

Replying to [comment:8 mabshoff]:
> One thing I forgot: I very much dislike the fact that it forced automated downloads of things like wxPython in case it isn't installed. It is clear from the readme that those ought to be already installed, but we need to find a more elegant way how to solve the "dependency of non-standard spkg" problem.
> 

Before we have this elegant solution the spkg-install should be consistent with reality!
So reflect that mayavi2 depends on vtk-5.0.4.p0 as you name the package.

The same holds for the vtk spkg, because it depends on cmake.

Jaap




```/bin/sh

sage -i wxPython-2.8.7.1
sage -i vtk-5.0.4.p0


cd src

python egg_builder.py -r -v

easy_install -f dist -H dist enthought.mayavi*


---

Comment by jsp created at 2008-03-27 15:14:27

The mayavi_2.1.1-20080307.p1.spkg does not work for me.



```
MayaVi2 seems to build, but fails to run mlab!

What the difference between mayavi_2.1.1-20080307.p1.spkg
and my original mayavi_2.1.1-20080307.spkg?

1) mv mayavi_build src
2) rm all .svn stuff
3) add .hg and friends

```


My hypothesis for now is that the .svn directories contain
essential information for the build system. I might be wrong, ...

I did a diff -r on both directories, only .svn files missing! See:

http://sage.math.washington.edu/home/jsp/diff_file

I did a fresh install on fresh installed sage-2.10.4,
sage-2.11.alpha0, sage-2.11.alpha1 on two machines. The results are consistent.


---

Comment by jsp created at 2008-03-27 15:14:27

Changing status from closed to reopened.


---

Comment by jsp created at 2008-03-27 15:14:27

Resolution changed from fixed to 


---

Comment by jsp created at 2008-03-31 11:11:59

About time to close this ticket again! A working modified version can be found here:

http://sage.math.washington.edu/home/jsp/mayavi_2.1.1-20080307.p1.spkg

Now the package is announced to be in sage-2.11 I don't think it is wise to have a wrong spkg in the experimental repo.

Jaap


---

Comment by mabshoff created at 2008-03-31 11:27:25

Updated the spkg with Jaap's latest. So I am closing this again since I just mirrored the repo out again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-31 11:27:25

Resolution: fixed
