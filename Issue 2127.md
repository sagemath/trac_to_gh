# Issue 2127: Mod n determinant and LinBox/FFPACK

Issue created by migration from https://trac.sagemath.org/ticket/2127

Original creator: cpernet

Original creation time: 2008-02-09 14:43:02

Assignee: cpernet

Improve efficiency of the dense mod n determinant by wrapping directly the LinBox/FFPACK Det.


---

Comment by cpernet created at 2008-02-09 14:59:07

Adds a wrapper to LinBox/FFPACK Det, for dense modular matrices


---

Attachment

Change the wrapper for linbox rank and det to use Modular<double> (fixes a bug) and add appropriate delete.


---

Comment by cpernet created at 2008-02-09 15:05:21

The updated version of linbox spkg is available at [http://sage.math.washington.edu/home/pernet/linbox-20080209.spkg](http://sage.math.washington.edu/home/pernet/linbox-20080209.spkg)


---

Comment by mabshoff created at 2008-02-14 17:49:52

The patches at #2107 and this ticket clash. It is also unclear where linbox-20080209.spkg comes from, i.e. is it an update to the latest linbox svn or just an incremental change over the last linbox.spkg, which should make it linbox-20070915.p4.

Cheers,

Michael


---

Comment by cpernet created at 2008-02-16 23:02:43

Fixed linbox_wrap.cpp.
The new linbox spkg is available at
[http://sage.math.washington.edu/home/pernet/linbox-2007-09-15.p5.spkg](http://sage.math.washington.edu/home/pernet/linbox-2007-09-15.p5.spkg)


---

Comment by cpernet created at 2008-02-16 23:04:40

Fix the wrong url of spkg

[http://sage.math.washington.edu/home/pernet/linbox-20070915.p5.spkg](http://sage.math.washington.edu/home/pernet/linbox-20070915.p5.spkg)


---

Attachment

Updated patch for rank/det wrapping of ffpack


---

Comment by mabshoff created at 2008-02-16 23:59:13

The updated linbox.spkg fixes the issue, but there are two problems:

 * it is not based on linbox-20070915.p4.spkg, but  linbox-20070915.p3.spkg, i.e. missing the Debianization infrastructure
 * there are outstanding changes not committed to the repo.

I am fixing both issues ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 00:30:17

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/linbox-20070915.p5.spkg

resolves all the issues.


---

Comment by mabshoff created at 2008-02-17 01:14:37

With linboxdet.1.patch applied I am seeing doctest failures like

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1$ ./sage -t devel/sage/sage/matrix/matrix_modn_dense.pyx
sage -t  devel/sage-main/sage/matrix/matrix_modn_dense.pyx  dd = 1
**********************************************************************
File "matrix_modn_dense.pyx", line 61:
    sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[16]>", line 1, in <module>
        G = MatrixGroup([M([[Integer(0),Integer(1),Integer(0)],[Integer(0),Integer(0),Integer(1)],[Integer(1),Integer(0),Integer(0)]]), M([[Integer(0),Integer(1),Integer(0)],[Integer(1),Integer(0),Integer(0)],[Integer(0),Integer(0),Integer(1)]])])###line 61:
    sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 146, in MatrixGroup
        return MatrixGroup_gens_finite_field(gens)
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 586, in __init__
        if not x.is_invertible():
      File "matrix0.pyx", line 1414, in sage.matrix.matrix0.Matrix.is_invertible
        return self.is_square() and self.determinant().is_unit()
    AttributeError: 'long' object has no attribute 'is_unit'
**********************************************************************
File "matrix_modn_dense.pyx", line 62:
    sage: G
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        G###line 62:
    sage: G
    NameError: name 'G' is not defined
**********************************************************************
File "matrix_modn_dense.pyx", line 65:
    sage: gap(G)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        gap(G)###line 65:
    sage: gap(G)
    NameError: name 'G' is not defined
**********************************************************************
File "matrix_modn_dense.pyx", line 901:
    sage: m.det()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[0]>", line 1, in <module>
        m.det()###line 901:
    sage: m.det()
    NameError: name 'm' is not defined
**********************************************************************
2 items had failures:
   3 of  24 in __main__.example_0
   1 of   3 in __main__.example_14
***Test Failed*** 4 failures.
For whitespace errors, see the file .doctest_matrix_modn_dense.pyx
         [2.2 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:
```

Ergo: negative review for now until those issues are sorted out.

FYI: My linbox.spkg from #2107 has been merged. The patch linboxdet.3.patch is a non-unified diff, so next to useless :(

Cheers,

Michael


---

Comment by cpernet created at 2008-02-17 01:26:53

Fix the doctest failure due to linboxdet.1.patch


---

Attachment

fix the last doctest failure with det over nonprime modular rings.


---

Attachment


---

Comment by was created at 2008-02-17 05:25:09

Please just apply /home/was/patches/hnf.hg, which includes this plus a little followup to better integrate the functionality into sage.


---

Comment by mabshoff created at 2008-02-17 11:51:45

Merged William's hnf.hg in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-17 11:51:45

Resolution: fixed
