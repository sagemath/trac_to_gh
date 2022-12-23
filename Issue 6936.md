# Issue 6936: [with patch, needs review] Implement generic testing from #6343 for matrices

Issue created by migration from https://trac.sagemath.org/ticket/6936

Original creator: jason

Original creation time: 2009-09-15 18:20:03

Assignee: was

CC:  kcrisman nthiery hivert rbeezer

The patch calls TestSuite().run() every time load(dumps()) is called in the matrix directory.  I also added a _test_minpoly() function, and fixed an existing _test_pickle() function.

Running doctests in matrix/*.pyx now fails for a number of files.  In other words, this testing infrastructure works and is uncovering bugs!

The bugs should be dealt with on other tickets.


---

Comment by jason created at 2009-09-15 18:23:15

This, of course, depends on the patches at #6343.


---

Comment by kcrisman created at 2009-09-15 18:30:22

Ticket #6934 is related, of course.


---

Comment by nthiery created at 2009-09-16 07:52:10

Changing keywords from "" to "TestSuite".


---

Comment by nthiery created at 2009-09-16 07:52:10

Hi Jason,

I am glad to hear that TestSuite is useful, even before the category
code gets in :-)

Some suggestions:

 - remove the loads(dumps(a)) == a tests, since anyway they are
   done by TestSuite

 - Maybe rename _test_matrix_pickle by _test_reduce?

   In fact, it would be nice to have this test whenever __reduce__ is
   implemented (even though it's tested by test_pickle anyway).  An
   option would be to lift _test_reduce to SageObject, and add a
   conditional in _test_reduce to do nothing if _reduce_ is not
   defined. The downside is that, if someone inadvertently remove
   __reduce__, then this won't be detected. Any better idea?

 - About _test_minpoly (and in general _test methods for elements):
   One thing which is not yet clear to me is whether the _test method
   should be on the elements or the parent. The former sounds more
   natural; however, with the later, one can use the information from
   the parent to build a good set of elements on which to run the
   test.

   One option would be to add to each parent a method _test_elements
   that would run TestSuite on some_elements(). However, there
   typically might be very expensive test methods that one will want
   to run on just a couple small elements, and other test methods that
   one will want to test with many large ones.

   But that's just food for thoughts for the long run

Other than that, I will be very happy being a reviewer for this patch,
and put a positive review.

I haven't run the tests yet. But from the comments above, I gather
that some tests are broken, not because this patch is wrong, but
because it uncovers bugs elsewhere. Should those be fixed before
setting a positive review on this one?


---

Comment by jason created at 2009-09-17 08:29:13

Replying to [comment:5 nthiery]:
> Hi Jason,
> 
> I am glad to hear that TestSuite is useful, even before the category
> code gets in :-)
> 
> Some suggestions:
> 
>  - remove the loads(dumps(a)) == a tests, since anyway they are
>    done by TestSuite


The -review.patch patch does this.


> 
>  - Maybe rename _test_matrix_pickle by _test_reduce?


The -review.patch patch does this.


> 
>    In fact, it would be nice to have this test whenever __reduce__ is
>    implemented (even though it's tested by test_pickle anyway).  An
>    option would be to lift _test_reduce to SageObject, and add a
>    conditional in _test_reduce to do nothing if _reduce_ is not
>    defined. The downside is that, if someone inadvertently remove
>    __reduce__, then this won't be detected. Any better idea?
> 
>  - About _test_minpoly (and in general _test methods for elements):
>    One thing which is not yet clear to me is whether the _test method
>    should be on the elements or the parent. The former sounds more
>    natural; however, with the later, one can use the information from
>    the parent to build a good set of elements on which to run the
>    test.
> 
>    One option would be to add to each parent a method _test_elements
>    that would run TestSuite on some_elements(). However, there
>    typically might be very expensive test methods that one will want
>    to run on just a couple small elements, and other test methods that
>    one will want to test with many large ones.
> 
>    But that's just food for thoughts for the long run

The rest of these items sound controversial enough that they should be brought up on sage-devel.



> 
> Other than that, I will be very happy being a reviewer for this patch,
> and put a positive review.


If you're happy with the changes, can you mark this positive review?



> 
> I haven't run the tests yet. But from the comments above, I gather
> that some tests are broken, not because this patch is wrong, but
> because it uncovers bugs elsewhere. Should those be fixed before
> setting a positive review on this one?


I'd say merge this, since it uncovers existing bugs, but doesn't introduce any.  With this merged, those bugs will get fixed before the next release.


---

Comment by nthiery created at 2009-09-17 19:53:41

> The -review.patch patch does this.

Thanks!

> The rest of these items sound controversial enough that they should be brought up on sage-devel.

Do you mind doing it?

> If you're happy with the changes, can you mark this positive review?

Done! However, please someone run the tests. I don't have a sage devel under hand.

> I'd say merge this, since it uncovers existing bugs, but doesn't introduce any.  With this merged, those bugs will get fixed before the next release.

Sounds good to me.


---

Comment by mvngu created at 2009-09-26 07:50:26

With `trac-6936-matrix-generic-doctesting-minpoly.patch`, I got a hunk failure:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6936/trac-6936-matrix-generic-doctesting-minpoly.patch && hg qpush
adding trac-6936-matrix-generic-doctesting-minpoly.patch to series file
applying trac-6936-matrix-generic-doctesting-minpoly.patch
patching file sage/matrix/matrix2.pyx
Hunk #2 FAILED at 1190
1 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac-6936-matrix-generic-doctesting-minpoly.patch
```

The hunk in question is

```
[mvngu@sage sage-main]$ cat sage/matrix/matrix2.pyx.rej
--- matrix2.pyx
+++ matrix2.pyx
@@ -1190,6 +1191,22 @@
         return mp
     
 
+    def _test_minpoly(self, **options):
+        """
+        Checks that :meth:`minpoly` works.
+
+        EXAMPLES::
+
+            sage: a=matrix([[1,2],[3,4]])
+            sage: a._test_minpoly()
+
+        """
+        if self.nrows()==self.ncols():
+            tester = self._tester(**options)
+            # At least we'll check that the minimal polynomial kills the
+            # matrix.
+            tester.assert_(self.minpoly().subs(x=self).is_zero())
+
     def charpoly(self, var='x', algorithm="hessenberg"):
         r"""
         Return the characteristic polynomial of self, as a polynomial over
```



---

Comment by jason created at 2009-10-01 05:56:25

Okay, it's rebased; the problem was that "charpoly" changed its default algorithm to "None".  Since that doesn't affect anything in this patch, I'll set it back to positive review.


---

Comment by mhansen created at 2009-10-15 10:06:45

Resolution: fixed


---

Comment by mhansen created at 2009-10-16 07:15:27

I get failures in these files:


```
        sage -t  devel/sage-main/sage/matrix/matrix_generic_dense.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_integer_2x2.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_dense.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix1.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx # 1 doctests failed

```


One of them is definitely #5639.


---

Comment by mhansen created at 2009-10-16 07:15:27

Changing status from closed to needs_work.


---

Comment by jason created at 2009-10-16 08:23:02

Aren't these bugs that are exposed by this patch, rather than bugs caused by this patch?  If so, then new tickets should be opened, rather than changing this to needs work.


---

Comment by hivert created at 2009-10-19 17:19:34

Hi there,

When creating #5274 it was my intend to implement this generic testing. So one probably wan't to close #5274 as a duplicate. However, It should be a good idea to include `test_trivial_matrices_inverse` from `matrix_space.py` in this generic testing infrastruture, since it currently test the different space by hand. 

Cheers,

Florent


---

Attachment


---

Comment by jason created at 2010-01-19 02:37:57

Okay, I took out the minpoly test, so this patch just implements the generic testing infrastructure.  The minpoly test will go on another ticket so the doctest failures can be dealt with there.


---

Comment by jason created at 2010-01-19 02:37:57

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-01-19 02:41:37

This looks good to me.  Please put the new ticket number for minpoly here.


---

Comment by mhansen created at 2010-01-19 02:41:37

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-01-19 02:51:31

The minpoly ticket is #7989.
