# Issue 4972: matrix setitem should deal with slicing

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-14 08:33:23

Assignee: was

The following should work:


```
a=matrix(QQ,3,[1,3,4,3,2,3,6,4,5])
a[1,:]=a[0,:]
```


Instead, I get an error:


```
          	

Traceback (click to the left for traceback)
...
TypeError: 'slice' object cannot be interpreted as an index

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/grout/.sage/sage_notebook/worksheets/admin/143/code/10.py", line 7, in <module>
    a[_sage_const_1 ,:]=a[_sage_const_0 ,:]
  File "/home/grout/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "matrix0.pyx", line 798, in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:4517)
TypeError: 'slice' object cannot be interpreted as an index

```



---

Comment by jason created at 2009-01-14 08:46:42

To clarify, I think we should support setting a submatrix (and not just getting a submatrix) using slicing.  This will be consistent with numpy, matlab, octave, etc.


---

Comment by jason created at 2009-01-16 02:29:25

Now that #4973 is pretty much done, what we really should do is factor out the bulk of the setup code in getitem and use it for both setitem and getitem.


---

Comment by jason created at 2009-02-03 21:41:50

See #2396, which should probably be closed when this is fixed.


---

Comment by jason created at 2009-02-04 21:42:54

I'm making some changes.  I'll post an updated patch soon.


---

Comment by jason created at 2009-02-05 06:52:22

ignore the .2.patch file.  I've refreshed the original .patch file.


---

Attachment

Refreshed patch to fix some doctests.


---

Comment by cwitty created at 2009-02-06 02:50:18

That's a lot of doctests; cool!  (Maybe some of them should be marked
as TESTS:, in case we ever get around to having that mean something...)


```
            key -- any legal indexing (i.e., self[key] works)
```

feels a little awkward... I had to read it twice to figure out what it
meant.  Maybe

```
            key -- any legal indexing (i.e., such that self[key] works)
```

would be better?

I think it's wrong that this works:

```
sage: M = matrix(3, 2, srange(6)); M[1] = 15; M
```

but this raises an exception:

```
sage: M = matrix(3, 1, srange(3)); M[1] = 15; M
```


A lot of your variables should have type Py_ssize_t rather than int;
your current code will give very wrong results on matrices with more
than 2<sup>31</sup> rows or columns (which could happen on a 64-bit machine).

Other than that, looks very nice!


---

Comment by jason created at 2009-02-06 06:21:10

the fixups.patch addresses cwitty's concerns.  It should be applied on top of trac_4972-matrix-setitem.patch


---

Attachment

grr, forgot to check the "replace" checkbox again.

So apply the following:

trac_4972-matrix-setitem.patch, then trac_4972-matrix-setitem-fixups.patch

Ignore both .2.patch files.

This second refresh corrects some "int" cdefs in misc_c.pyx


---

Comment by cwitty created at 2009-02-06 06:38:58

Code looks good, all doctests pass.

Thanks for making the requested changes!

Positive review; apply both patches.


---

Comment by mabshoff created at 2009-02-06 22:27:49

Resolution: fixed


---

Comment by mabshoff created at 2009-02-06 22:27:49

Merged both patches in Sage 3.3.alpha6.

Cheers,

Michael
