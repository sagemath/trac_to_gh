# Issue 4334: [with spkg, needs review] Updated experimental Mayavi2 spkg

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-10-21 13:06:04

Assignee: mabshoff

Updated to mayavi_2.2.1


[http://sage.math.washington.edu/home/jsp/mayavi_2.2.1.spkg](http://sage.math.washington.edu/home/jsp/mayavi_2.2.1.spkg)

Depends on on experimental spkgs:
vtk-5.2, cmake-2.4.8 and wxPython-2.8.7.1





---

Comment by jsp created at 2008-10-27 16:55:17

This package works for sage-3.1.2 and earlier, but does not show pictures
for sage-3.1.3 and later!

Any thoughts about what changed between 3.1.2 and 3.1.3 causing this failure?

Jaap


---

Comment by jsp created at 2008-11-20 18:47:05

Yes. It will work when #4381 will be resolved.

Passing the -wthread argument to sage.

Jaap


---

Comment by jsp created at 2008-11-28 13:48:03

Trac #4381 is resolved in sage-3.2.1.alpha2, so
./sage -wthread is working again.

Jaap


---

Comment by was created at 2008-11-29 03:09:02

Just to move this toward being optional (not experimental), some comments.

1. The spkg-install is

```
was`@`sage:~/tmp/mayavi_2.2.1$ more spkg-install 
#!/bin/sh

sage -i wxPython-2.8.7.1
sage -i cmake-2.4.8
sage -i vtk-5.2


cd src

python egg_builder.py -r -v

easy_install -f dist -H dist enthought.mayavi*
```


Each comment, e.g., the "sage -i"'s should have some test that it actually worked before going further.  You could check error codes, or check that the appropriate spkg/installed file exists.

2. The format of the changelog in SPKG.txt is wrong:

```
## Changelog
 * Initial release mayvi2_2.0.20080106 - Jan. 6th, 2008 - Jaap Spies
 * mayavi2_2.0.20080117 - Jan. 17th, 2008 - Jaap Spies
```

Just see any SPKG.txt that is standard for the right format. 

3. spkg-install and SPKG.txt should be in an .hg repo:

```
was`@`sage:~/tmp/mayavi_2.2.1$ ls -a
.  ..  spkg-install  SPKG.txt  src
```

One should do 

```
hg init
hg add spkg-install SPKG.txt
hg ci
```


I didn't actually test this though...


---

Comment by was created at 2008-11-29 03:09:54

Since this spkg is experimental, I think we should drop it in the experimental repo on sagemath.org right now anyways.  I looked in the spkg and it doesn't look like pure evil.  It doesn't matter if it works or not, since it's "experimental".


---

Comment by mabshoff created at 2008-11-29 07:02:25

Merged in the experimental spkg repo and mirrored out.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 07:02:25

Resolution: fixed


---

Comment by was created at 2008-11-29 18:29:57


```
Hi William,

Thanks for your comments.
A problem for moving to optional is lacking a mac version of wxPython and vtk.
This is certainly doable. The enthought people are doing this all the time.


    Do you know anybody besides you who uses mayavi etc. via sage?


In the past Marshal Hampton, Jason Grout, Joshua Kantor and Carl Witty
showed interest. Some of them even installed the package.

I'm now testing a comlete Enthought Tools Suite ETS-3.0.3.
Including a newer version of mayavi_2.
```

