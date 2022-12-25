# Issue 6936: [with patch, needs review] Implement generic testing from #6343 for matrices

archive/issues_006936.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman @nthiery @hivert @rbeezer\n\nThe patch calls TestSuite().run() every time load(dumps()) is called in the matrix directory.  I also added a _test_minpoly() function, and fixed an existing _test_pickle() function.\n\nRunning doctests in matrix/*.pyx now fails for a number of files.  In other words, this testing infrastructure works and is uncovering bugs!\n\nThe bugs should be dealt with on other tickets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6936\n\n",
    "created_at": "2009-09-15T18:20:03Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "[with patch, needs review] Implement generic testing from #6343 for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6936",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman @nthiery @hivert @rbeezer

The patch calls TestSuite().run() every time load(dumps()) is called in the matrix directory.  I also added a _test_minpoly() function, and fixed an existing _test_pickle() function.

Running doctests in matrix/*.pyx now fails for a number of files.  In other words, this testing infrastructure works and is uncovering bugs!

The bugs should be dealt with on other tickets.

Issue created by migration from https://trac.sagemath.org/ticket/6936





---

archive/issue_comments_057215.json:
```json
{
    "body": "This, of course, depends on the patches at #6343.",
    "created_at": "2009-09-15T18:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57215",
    "user": "https://github.com/jasongrout"
}
```

This, of course, depends on the patches at #6343.



---

archive/issue_comments_057216.json:
```json
{
    "body": "Ticket #6934 is related, of course.",
    "created_at": "2009-09-15T18:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57216",
    "user": "https://github.com/kcrisman"
}
```

Ticket #6934 is related, of course.



---

archive/issue_comments_057217.json:
```json
{
    "body": "Changing keywords from \"\" to \"TestSuite\".",
    "created_at": "2009-09-16T07:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57217",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "TestSuite".



---

archive/issue_comments_057218.json:
```json
{
    "body": "Hi Jason,\n\nI am glad to hear that TestSuite is useful, even before the category\ncode gets in :-)\n\nSome suggestions:\n\n- remove the loads(dumps(a)) == a tests, since anyway they are\n  done by TestSuite\n\n- Maybe rename _test_matrix_pickle by _test_reduce?\n\n  In fact, it would be nice to have this test whenever __reduce__ is\n  implemented (even though it's tested by test_pickle anyway).  An\n  option would be to lift _test_reduce to SageObject, and add a\n  conditional in _test_reduce to do nothing if _reduce_ is not\n  defined. The downside is that, if someone inadvertently remove\n  __reduce__, then this won't be detected. Any better idea?\n\n- About _test_minpoly (and in general _test methods for elements):\n  One thing which is not yet clear to me is whether the _test method\n  should be on the elements or the parent. The former sounds more\n  natural; however, with the later, one can use the information from\n  the parent to build a good set of elements on which to run the\n  test.\n\n  One option would be to add to each parent a method _test_elements\n  that would run TestSuite on some_elements(). However, there\n  typically might be very expensive test methods that one will want\n  to run on just a couple small elements, and other test methods that\n  one will want to test with many large ones.\n\n  But that's just food for thoughts for the long run\n\nOther than that, I will be very happy being a reviewer for this patch,\nand put a positive review.\n\nI haven't run the tests yet. But from the comments above, I gather\nthat some tests are broken, not because this patch is wrong, but\nbecause it uncovers bugs elsewhere. Should those be fixed before\nsetting a positive review on this one?",
    "created_at": "2009-09-16T07:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57218",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_057219.json:
```json
{
    "body": "Replying to [comment:5 nthiery]:\n> Hi Jason,\n> \n> I am glad to hear that TestSuite is useful, even before the category\n> code gets in :-)\n> \n> Some suggestions:\n> \n>  - remove the loads(dumps(a)) == a tests, since anyway they are\n>    done by TestSuite\n\n\nThe -review.patch patch does this.\n\n\n> \n>  - Maybe rename _test_matrix_pickle by _test_reduce?\n\n\nThe -review.patch patch does this.\n\n\n> \n>    In fact, it would be nice to have this test whenever __reduce__ is\n>    implemented (even though it's tested by test_pickle anyway).  An\n>    option would be to lift _test_reduce to SageObject, and add a\n>    conditional in _test_reduce to do nothing if _reduce_ is not\n>    defined. The downside is that, if someone inadvertently remove\n>    __reduce__, then this won't be detected. Any better idea?\n> \n>  - About _test_minpoly (and in general _test methods for elements):\n>    One thing which is not yet clear to me is whether the _test method\n>    should be on the elements or the parent. The former sounds more\n>    natural; however, with the later, one can use the information from\n>    the parent to build a good set of elements on which to run the\n>    test.\n> \n>    One option would be to add to each parent a method _test_elements\n>    that would run TestSuite on some_elements(). However, there\n>    typically might be very expensive test methods that one will want\n>    to run on just a couple small elements, and other test methods that\n>    one will want to test with many large ones.\n> \n>    But that's just food for thoughts for the long run\n\nThe rest of these items sound controversial enough that they should be brought up on sage-devel.\n\n\n\n> \n> Other than that, I will be very happy being a reviewer for this patch,\n> and put a positive review.\n\n\nIf you're happy with the changes, can you mark this positive review?\n\n\n\n> \n> I haven't run the tests yet. But from the comments above, I gather\n> that some tests are broken, not because this patch is wrong, but\n> because it uncovers bugs elsewhere. Should those be fixed before\n> setting a positive review on this one?\n\n\nI'd say merge this, since it uncovers existing bugs, but doesn't introduce any.  With this merged, those bugs will get fixed before the next release.",
    "created_at": "2009-09-17T08:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57219",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_comments_057220.json:
```json
{
    "body": "> The -review.patch patch does this.\n\nThanks!\n\n> The rest of these items sound controversial enough that they should be brought up on sage-devel.\n\nDo you mind doing it?\n\n> If you're happy with the changes, can you mark this positive review?\n\nDone! However, please someone run the tests. I don't have a sage devel under hand.\n\n> I'd say merge this, since it uncovers existing bugs, but doesn't introduce any.  With this merged, those bugs will get fixed before the next release.\n\nSounds good to me.",
    "created_at": "2009-09-17T19:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57220",
    "user": "https://github.com/nthiery"
}
```

> The -review.patch patch does this.

Thanks!

> The rest of these items sound controversial enough that they should be brought up on sage-devel.

Do you mind doing it?

> If you're happy with the changes, can you mark this positive review?

Done! However, please someone run the tests. I don't have a sage devel under hand.

> I'd say merge this, since it uncovers existing bugs, but doesn't introduce any.  With this merged, those bugs will get fixed before the next release.

Sounds good to me.



---

archive/issue_comments_057221.json:
```json
{
    "body": "With `trac-6936-matrix-generic-doctesting-minpoly.patch`, I got a hunk failure:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6936/trac-6936-matrix-generic-doctesting-minpoly.patch && hg qpush\nadding trac-6936-matrix-generic-doctesting-minpoly.patch to series file\napplying trac-6936-matrix-generic-doctesting-minpoly.patch\npatching file sage/matrix/matrix2.pyx\nHunk #2 FAILED at 1190\n1 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac-6936-matrix-generic-doctesting-minpoly.patch\n```\n\nThe hunk in question is\n\n```\n[mvngu@sage sage-main]$ cat sage/matrix/matrix2.pyx.rej\n--- matrix2.pyx\n+++ matrix2.pyx\n@@ -1190,6 +1191,22 @@\n         return mp\n     \n \n+    def _test_minpoly(self, **options):\n+        \"\"\"\n+        Checks that :meth:`minpoly` works.\n+\n+        EXAMPLES::\n+\n+            sage: a=matrix([[1,2],[3,4]])\n+            sage: a._test_minpoly()\n+\n+        \"\"\"\n+        if self.nrows()==self.ncols():\n+            tester = self._tester(**options)\n+            # At least we'll check that the minimal polynomial kills the\n+            # matrix.\n+            tester.assert_(self.minpoly().subs(x=self).is_zero())\n+\n     def charpoly(self, var='x', algorithm=\"hessenberg\"):\n         r\"\"\"\n         Return the characteristic polynomial of self, as a polynomial over\n```\n",
    "created_at": "2009-09-26T07:50:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57221",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_057222.json:
```json
{
    "body": "Okay, it's rebased; the problem was that \"charpoly\" changed its default algorithm to \"None\".  Since that doesn't affect anything in this patch, I'll set it back to positive review.",
    "created_at": "2009-10-01T05:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57222",
    "user": "https://github.com/jasongrout"
}
```

Okay, it's rebased; the problem was that "charpoly" changed its default algorithm to "None".  Since that doesn't affect anything in this patch, I'll set it back to positive review.



---

archive/issue_comments_057223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T10:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57223",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_057224.json:
```json
{
    "body": "I get failures in these files:\n\n\n```\n        sage -t  devel/sage-main/sage/matrix/matrix_generic_dense.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_integer_2x2.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_dense.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix1.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx # 1 doctests failed\n\n```\n\n\nOne of them is definitely #5639.",
    "created_at": "2009-10-16T07:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57224",
    "user": "https://github.com/mwhansen"
}
```

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

archive/issue_comments_057225.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2009-10-16T07:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57225",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_057226.json:
```json
{
    "body": "Aren't these bugs that are exposed by this patch, rather than bugs caused by this patch?  If so, then new tickets should be opened, rather than changing this to needs work.",
    "created_at": "2009-10-16T08:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57226",
    "user": "https://github.com/jasongrout"
}
```

Aren't these bugs that are exposed by this patch, rather than bugs caused by this patch?  If so, then new tickets should be opened, rather than changing this to needs work.



---

archive/issue_comments_057227.json:
```json
{
    "body": "Hi there,\n\nWhen creating #5274 it was my intend to implement this generic testing. So one probably wan't to close #5274 as a duplicate. However, It should be a good idea to include `test_trivial_matrices_inverse` from `matrix_space.py` in this generic testing infrastruture, since it currently test the different space by hand. \n\nCheers,\n\nFlorent",
    "created_at": "2009-10-19T17:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57227",
    "user": "https://github.com/hivert"
}
```

Hi there,

When creating #5274 it was my intend to implement this generic testing. So one probably wan't to close #5274 as a duplicate. However, It should be a good idea to include `test_trivial_matrices_inverse` from `matrix_space.py` in this generic testing infrastruture, since it currently test the different space by hand. 

Cheers,

Florent



---

archive/issue_comments_057228.json:
```json
{
    "body": "Attachment [trac-6936-matrix-generic-doctesting.patch](tarball://root/attachments/some-uuid/ticket6936/trac-6936-matrix-generic-doctesting.patch) by @jasongrout created at 2010-01-19 02:35:31",
    "created_at": "2010-01-19T02:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57228",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-6936-matrix-generic-doctesting.patch](tarball://root/attachments/some-uuid/ticket6936/trac-6936-matrix-generic-doctesting.patch) by @jasongrout created at 2010-01-19 02:35:31



---

archive/issue_comments_057229.json:
```json
{
    "body": "Okay, I took out the minpoly test, so this patch just implements the generic testing infrastructure.  The minpoly test will go on another ticket so the doctest failures can be dealt with there.",
    "created_at": "2010-01-19T02:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57229",
    "user": "https://github.com/jasongrout"
}
```

Okay, I took out the minpoly test, so this patch just implements the generic testing infrastructure.  The minpoly test will go on another ticket so the doctest failures can be dealt with there.



---

archive/issue_comments_057230.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T02:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57230",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057231.json:
```json
{
    "body": "This looks good to me.  Please put the new ticket number for minpoly here.",
    "created_at": "2010-01-19T02:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57231",
    "user": "https://github.com/mwhansen"
}
```

This looks good to me.  Please put the new ticket number for minpoly here.



---

archive/issue_comments_057232.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T02:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57232",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057233.json:
```json
{
    "body": "The minpoly ticket is #7989.",
    "created_at": "2010-01-19T02:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6936#issuecomment-57233",
    "user": "https://github.com/jasongrout"
}
```

The minpoly ticket is #7989.
