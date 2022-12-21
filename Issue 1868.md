# Issue 1868: New mayavi2 package

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-01-20 17:57:55

Assignee: was

This spkg needs cmake-2.4.7.spkg (already in experimental), vtk-5.0.3.spkg, setuptools-0.6.spkg
and wxPython-2.8.7.1 (already in experimental as wxPython-linux-2.8.7.1.spk).

```
The following is working on Fedora 7/8 (and Ubuntu?):

 > Dependencies for Sage:
 >

 >   - http://www.wxpython.org wxPython-2.6.x or higher for the UI
 >   - vtk-5.0.3
 >   - setuptools-0.6b

1) Install wxPython-2.8.7.1:
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/wxPython-2.8.7.1.spkg

2) Install vtk-5.0.3:

    install cmake (also an experimental spkg):
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/cmake-2.4.7.spkg
    and
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/vtk-5.0.3.spkg

3) Install setuptools:
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/setuptools-0.6.spkg

4) Install mayavi_2.0.20080117.spkg
    http://sage.math.washington.edu/home/jsp/SPKGS/MayaVi/mayavi_2.0.20080117.spkg

```


This new spkg will install its dependencies automagically.

Eventually


```
./sage -i mayavi_2.0.20080117
```


will do the trick.


---

Comment by jsp created at 2008-01-29 20:46:46

This experimental package could easily be included, I think.

Jaap


---

Comment by was created at 2008-02-28 20:40:17

Once this gets a positive review from some people trying it out, it will be posted to the sage official spkg webpage.


---

Comment by jason created at 2008-02-29 23:38:13

This package seems to work for me.


---

Comment by cwitty created at 2008-03-01 01:46:12

These packages work for me (and have for weeks; I'm sorry, I should have reviewed this ticket a long time ago.)  32-bit x86 debian testing, using the non-free nvidia graphics drivers.


---

Comment by mabshoff created at 2008-03-01 21:49:21

Merged in the experimental package repo


---

Comment by mabshoff created at 2008-03-01 21:49:21

Resolution: fixed
