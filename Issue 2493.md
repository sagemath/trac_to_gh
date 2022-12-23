# Issue 2493: Updated experimental vtk spkg (vtk-5.0.4.spkg)

Issue created by migration from https://trac.sagemath.org/ticket/2493

Original creator: jsp

Original creation time: 2008-03-12 14:44:00

Assignee: was

Updated to vtk-5.0.4

Now compiles with GL2EPS enabled. So it is possible to save pictures as eps, ps and pdf files.

Depency cmake updated to cmake-2.4.8

Files see:

```
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/cmake-2.4.8.spkg
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/vtk-5.0.4.spkg
```




---

Comment by jsp created at 2008-03-12 14:45:50

Files:

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/cmake-2.4.8.spkg

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/vtk-5.0.4.spkg


---

Comment by jsp created at 2008-03-15 19:55:31

I think reviewing this is easy. In experimental there are already cmake-2.4.7 and vtk-5.0.3

This are only minor updates to the latest versions.

With one exception: vtk-5.0.4 comes now with GL3EPS enabled! Making it possible to save
figures as eps, ps and pdf files.

This update is needed for the mayavi_2.1.1 package!


---

Comment by cwitty created at 2008-03-20 20:51:58

I used these packages to upgrade from earlier versions of Jaap's packages; the installations went perfectly, and my code (which uses wxPython, vtk, and tvtk (from mayavi)) worked fine after the upgrade.

Debian testing 32-bit x86.


---

Comment by mabshoff created at 2008-03-22 05:20:51

Hi, 

I checked in the changes into the repo. The result is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/vtk-5.0.4.p0.spkg

I didn't look at SPKG.txt yet

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 05:23:05

Resolution: fixed


---

Comment by mabshoff created at 2008-03-22 05:23:05

Merged both spkgs into the experimental spkg repo.


---

Comment by jsp created at 2008-03-22 17:46:16

Replying to [comment:5 mabshoff]:
> Hi, 
> 
> I checked in the changes into the repo. The result is at 
> 
> http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/vtk-5.0.4.p0.spkg
> 
> I didn't look at SPKG.txt yet
> 

This spkg depends on cmake-2.4.8 (see spkg-install). Probably it will work also with cmake-2.4.7,
which is already in experimental. But this should be reflected in the spkg-install file.

Jaap
