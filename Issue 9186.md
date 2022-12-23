# Issue 9186: Update R's spkg-install for building multiple spkgs in parallel

Issue created by migration from https://trac.sagemath.org/ticket/9186

Original creator: mpatel

Original creation time: 2010-06-08 08:42:08

Assignee: tbd

CC:  drkirkby jhpalmieri leif

To build R with `SAGE_PARALLEL_SPKG_BUILD="yes"` on Mac OS X, we need to add, e.g.,

```sh
MAKEFLAGS=
export MAKEFLAGS
```

to the "make install" part of the package's `spkg-install`.

Please see #8306 about building spkgs in parallel.  For `MAKEFLAGS`, see [the GNU Make manual](http://www.gnu.org/software/make/manual/html_node/Options_002fRecursion.html).


---

Comment by mpatel created at 2010-06-09 02:22:24

spkg patch.  Set empty `MAKEFLAGS` for installation.


---

Comment by mpatel created at 2010-06-09 02:25:21

Changing status from new to needs_review.


---

Attachment

I've put a new spkg at

 * http://sage.math.washington.edu/home/mpatel/trac/9186/r-2.10.1.p2.spkg


---

Comment by drkirkby created at 2010-06-24 17:00:40

Positive review. It is extreamly simple, looks good and I've tested it on Solaris 10 on an old Sun Blade 2000 SPARC. 


```
real    21m53.863s
user    17m29.388s
sys     3m22.428s
Successfully installed r-2.10.1.p2
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4/spkg/build/r-2.10.1.p2
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing r-2.10.1.p2.spkg
```


*I really hope your code for building packages in parallel gets into Sage asap. It could make a huge difference to build times. I'll see if I can get some interest in pushing this up the priority list!*


---

Comment by drkirkby created at 2010-06-24 17:00:40

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:47:23

Resolution: fixed
