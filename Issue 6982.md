# Issue 6982: cygwin port: atlas and linbox

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-22 05:01:18

Assignee: tbd

* atlas --  require systemwide lapack installed

  * linbox -- use systemwide lapack


---

Comment by was created at 2009-09-22 05:21:37

Here are the spkgs:

   * http://sage.math.washington.edu/home/wstein/patches/atlas-3.8.3.p8.spkg

   * http://sage.math.washington.edu/home/wstein/patches/linbox-1.1.6.p1.spkg


---

Comment by certik created at 2009-09-22 05:48:24

The packages seem ok to me, both provide good error messages if cygwin atlas is not installed.


---

Comment by mvngu created at 2009-09-27 01:08:34

New ATLAS package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/atlas-3.8.3.p9.spkg

The changes from .p8 are:

 * Remove the junk files `spkg-install~` and `SPKG.txt~`.
 * Add the following line to `.hgignore`
 {{{
patches
 }}}
 so that everything under the directory `patches/` would be ignored.


---

Comment by mvngu created at 2009-09-27 01:12:39

New LinBox package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/linbox-1.1.6.p2.spkg

The only change from .p1 is:

 * Remove the junk file `spkg-install~`.


---

Comment by mvngu created at 2009-09-27 03:26:27

See my report at #6849.


---

Comment by mvngu created at 2009-09-27 03:26:27

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 11:02:14

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
