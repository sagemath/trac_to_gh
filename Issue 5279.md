# Issue 5279: Experimental ParaView Package

Issue created by migration from https://trac.sagemath.org/ticket/5279

Original creator: jsp

Original creation time: 2009-02-15 21:25:24

Assignee: was

CC:  mkoeppe

Keywords: 3D, Data Vizualization

Paraview is based on VTK, comes with it's own implementation of vtk.

[http://www.paraview.org/Wiki/ParaView](http://www.paraview.org/Wiki/ParaView)

From the wiki web site:

```
ParaView is an open-source, multi-platform application designed to visualize
data sets of size varying from small to very large. The goals of
the ParaView project include developing an open-source, multi-platform visualization
application that support distributed computational models to process
large data sets.
It has an open, flexible, and intuitive user interface.
Furthermore, ParaView is built on an extensible architecture based on open standards.
ParaView runs on distributed and shared memory parallel as well as single processor
systems and has been succesfully tested on Windows, Linux, Mac OS X, IBM Blue Gene,
Cray XT3 and various Unix workstations and clusters.
Under the hood, ParaView uses the Visualization Toolkit as the data processing
and rendering engine and has a user interface written using the
Qt cross-platform application framework.
```


Dependencies:

OpenGL

Qt4

openmpi for multi processor usage.

Try it! See:

[http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/paraview-3.4.0.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/paraview-3.4.0.spkg)

[http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/Screenshot-257.png](http://sage.math.washington.edu/home/jsp/SPKGS/ParaView/Screenshot-257.png)

Jaap


---

Comment by was created at 2009-03-16 00:10:35

Im working on sage.math.

I tried to install and get:

```
./spkg-install: line 19: cmake: command not found
ls: cannot access /home/wstein/build/sage-3.4/spkg/installed/cmake-2.4.8: No such file or directory
Failed to find cmake-2.4.8  Install cmake-2.4.8 
or install cmake-2.4 or higher

real    0m0.118s
user    0m0.000s
sys     0m0.000s
```


So please list cmake as a dependency.

I then install cmake and...

```
-- Check if system supports 64 bit streams
-- Check if system supports 64 bit streams - yes
-- Cannot determine repository type. Please set UPDATE_TYPE to 'cvs' or 'svn'. CTest update will not work.
-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a
-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a
-- Found PythonLibs: /home/wstein/build/sage-3.4/local/lib/python2.5/config/libpython2.5.a
-- Plugin: Prism enabled
-- Configuring done
Error configuring ParaView

real    0m47.134s
user    0m21.880s
sys     0m12.220s
sage: An error occurred while installing paraview-3.4.0
```


Maybe you could at least get this to build on sage.math?


---

Comment by jsp created at 2009-03-16 13:24:34

The discussion on google groups seems to be relevant here:

http://groups.google.com/group/sage-devel/browse_thread/thread/6094c90ac284edd/b8454dd45de731c4?lnk=gst&q=paraview#b8454dd45de731c4

I think this package as is will not build on sage.math.

A month ago I got the server version running on sage.math. So maybe we will have to make two spkgs: a desktop vesion and a server version.

Jaap


---

Comment by chapoton created at 2022-04-20 19:07:54

maybe we can close this one after 13 years of inactivity ?


---

Comment by chapoton created at 2022-04-20 19:07:54

Changing status from needs_work to needs_review.


---

Comment by dcoudert created at 2022-04-21 12:17:28

Changing status from needs_review to positive_review.


---

Comment by dcoudert created at 2022-04-21 12:17:28

I agree.


---

Comment by chapoton created at 2022-04-21 15:28:35

Resolution: invalid
