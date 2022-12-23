# Issue 1726: Experimental package for Enthought Mayavi2 (linux only)

Issue created by migration from https://trac.sagemath.org/ticket/1726

Original creator: jsp

Original creation time: 2008-01-08 22:23:50

Assignee: was

Including a very, very experimental spkg for mayavi2. This may go like this:


```
Ok, I got the sources.
svn co https://svn.enthought.com/svn/enthought/autobuild enthought.autobuild

They are now in a directory mayavi_2.0.20080106/mayavi_build

Copying egg_builder.py into it.

Now I don't run python egg_builder.py :)
Instead I write an spkg_install script.

But first of all we want to remove all directories not needed to build mayavi2.
Any help appreciated!

Mayavi (requires: Traits, TraitsGUI, EnvisageCore, AppTools)

     * enthought.mayavi
     * enthought.tvtk

Let's pretend all unnecessary directories are gone. Now my spkg_install
script looks like:

#!/bin/sh

cd mayavi_build

python egg_builder.py -r -v

easy_install -f dist -H dist enthought.mayavi*

Under the condition that all external dependencies are fullfilled,
this will install mayavi2 in the sage environment.
Is this correct? What are precisely the external dependencies for this build?
wxPython +
setuptools +
vtk +
swig ?
pyrex +
PIL -

Now cd .. and do
sage -pkg mayavi_2.0.20080106

And after some time we have mayavi_2.0.20080106.spkg ready for testing.

[jaap@paix sagefiles]$ ls -l mayavi_2.0.20080106*
-rw-rw-r-- 1 jaap jaap 54051652 2008-01-06 21:43 mayavi_2.0.20080106.spkg

mayavi_2.0.20080106:
total 8
drwxrwxr-x 50 jaap jaap 4096 2008-01-06 21:06 mayavi_build
-rw-rw-r--  1 jaap jaap  106 2008-01-06 21:40 spkg-install

The spkg is *big* also because all the ets source is still in it!

Let's do it now. I'm trying this on my latest installed sage-2.9.2
This may take some time :), mostly in building the dependencies.

Cheers,

Jaap

```


In the near future this will become easier. External dependencies should be resolved by making a "meta"-package.


For some premature results (Fedora 7/8) see:
http://picasaweb.google.nl/j.spies88/Mayavi2FromSage

See also: http://sage.math.washington.edu/home/jsp/spkg/


---

Comment by mabshoff created at 2008-01-09 02:12:58

Resolution: fixed


---

Comment by mabshoff created at 2008-01-09 02:12:58

I put this into the experimental package directory.
