# Issue 3522: [with spkgs, needs review] New experimental mayavi2 spkg based on vtk_5.2 for linux

Issue created by migration from https://trac.sagemath.org/ticket/3522

Original creator: jsp

Original creation time: 2008-06-27 14:26:11

Assignee: mabshoff



```
There were problems building mayavi2 experimental spkg on Fedora 9 and other
new Linuxes:
1) vtk-5.0.4 does not build with tcl/tk-8.5.1
2) vtk-5.0.4 will not build with gcc-4.3

Both problems are solved with vtk-5.2 from svn.

I checked out mayavi_2.2.0 and it worked for me on Fedora 8 and Fedora 9:
```


http://sage.math.washington.edu/home/jsp/mayavi_2.2.0.spkg


```
Depends on:
```

http://sage.math.washington.edu/home/jsp/vtk-5.2.spkg

```
(and experimental spkgs cmake-2.4.8 and wxPython-2.8.7.1)
```




---

Comment by mabshoff created at 2008-07-02 20:06:02

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-08-11 06:57:30

Jaap,

both spkgs looks good to me. I checked in the relevant files into the repos. One thing I noticed was that both archives contain the full svn history, but after the disaster last time around I left them there. Sorry that it took so long.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-11 06:58:44

Merged into the experimental package repo in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 06:58:44

Resolution: fixed
