# Issue 8008: Implement an rref() function which works over the fraction field of the base ring of a matrix

archive/issues_008008.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @rbeezer\n\nThis is a resolution to the issues at #3211.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8008\n\n",
    "created_at": "2010-01-20T05:01:34Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Implement an rref() function which works over the fraction field of the base ring of a matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8008",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @williamstein @rbeezer

This is a resolution to the issues at #3211.

Issue created by migration from https://trac.sagemath.org/ticket/8008





---

archive/issue_comments_069860.json:
```json
{
    "body": "Attachment [trac-8008-rref.patch](tarball://root/attachments/some-uuid/ticket8008/trac-8008-rref.patch) by @jasongrout created at 2010-01-20 05:04:42",
    "created_at": "2010-01-20T05:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69860",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8008-rref.patch](tarball://root/attachments/some-uuid/ticket8008/trac-8008-rref.patch) by @jasongrout created at 2010-01-20 05:04:42



---

archive/issue_comments_069861.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T06:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69861",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069862.json:
```json
{
    "body": "- Perhaps a very short statement about what the row echelon form of matrices over fields look like would be nice.\n\n- line 4035: instead of echelon_form, I think this should be ``echelon_form`` or :meth:`echelon_form`\n\n- line 4085: I'd prefer if this was done in two lines \n    {{{\n        F = R.fraction_field()\n        return self.change_ring(F).echelon_form()\n    }}}\n   so that if an error occurs when creating the fraction field, the line number corresponds to the obvious problem.  (Of course, this would be clear from the traceback anyway...)\n\nSebastian",
    "created_at": "2010-01-20T09:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69862",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

- Perhaps a very short statement about what the row echelon form of matrices over fields look like would be nice.

- line 4035: instead of echelon_form, I think this should be ``echelon_form`` or :meth:`echelon_form`

- line 4085: I'd prefer if this was done in two lines 
    {{{
        F = R.fraction_field()
        return self.change_ring(F).echelon_form()
    }}}
   so that if an error occurs when creating the fraction field, the line number corresponds to the obvious problem.  (Of course, this would be clear from the traceback anyway...)

Sebastian



---

archive/issue_comments_069863.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T09:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69863",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069864.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-01-20T10:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69864",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_069865.json:
```json
{
    "body": "Attachment [trac-8008-fixes.patch](tarball://root/attachments/some-uuid/ticket8008/trac-8008-fixes.patch) by @jasongrout created at 2010-01-20 10:02:48",
    "created_at": "2010-01-20T10:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69865",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8008-fixes.patch](tarball://root/attachments/some-uuid/ticket8008/trac-8008-fixes.patch) by @jasongrout created at 2010-01-20 10:02:48



---

archive/issue_comments_069866.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T10:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69866",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069867.json:
```json
{
    "body": "The second patch fixes the issues Sebastian brought up.",
    "created_at": "2010-01-20T10:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69867",
    "user": "https://github.com/jasongrout"
}
```

The second patch fixes the issues Sebastian brought up.



---

archive/issue_comments_069868.json:
```json
{
    "body": "I think this looks good now.",
    "created_at": "2010-01-20T10:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69868",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

I think this looks good now.



---

archive/issue_comments_069869.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T10:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69869",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069870.json:
```json
{
    "body": "I got a hunk failure after applying [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch), then [trac-8008-fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-fixes.patch):\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8008/trac-8008-rref.patch && hg qpush\nadding trac-8008-rref.patch to series file\napplying trac-8008-rref.patch\nnow at: trac-8008-rref.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8008/trac-8008-fixes.patch && hg qpush\nadding trac-8008-fixes.patch to series file\napplying trac-8008-fixes.patch\npatching file sage/matrix/matrix2.pyx\nHunk #3 FAILED at 4273\n1 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac-8008-fixes.patch\n[mvngu@sage sage-main]$ cat sage/matrix/matrix2.pyx.rej\n--- matrix2.pyx\n+++ matrix2.pyx\n@@ -4267,12 +4274,14 @@\n         \"\"\"\n         Return the echelon form of self.\n \n-        .. note:: This row reduction does not use division if the\n-        matrix is not over a field (e.g., if the matrix is over the\n-        integers).  If you want to calculate the echelon form using\n-        division, then use :meth:`rref`, which assumes that the matrix\n-        entries are in a field (specifically, the field of fractions\n-        of the base ring of the matrix).\n+        .. note:: \n+\n+            This row reduction does not use division if the\n+            matrix is not over a field (e.g., if the matrix is over\n+            the integers).  If you want to calculate the echelon form\n+            using division, then use :meth:`rref`, which assumes that\n+            the matrix entries are in a field (specifically, the field\n+            of fractions of the base ring of the matrix).\n         \n         INPUT:\n```\nPerhaps this ticket needs a rebase?",
    "created_at": "2010-01-22T14:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I got a hunk failure after applying [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch), then [trac-8008-fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-fixes.patch):

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8008/trac-8008-rref.patch && hg qpush
adding trac-8008-rref.patch to series file
applying trac-8008-rref.patch
now at: trac-8008-rref.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8008/trac-8008-fixes.patch && hg qpush
adding trac-8008-fixes.patch to series file
applying trac-8008-fixes.patch
patching file sage/matrix/matrix2.pyx
Hunk #3 FAILED at 4273
1 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-8008-fixes.patch
[mvngu@sage sage-main]$ cat sage/matrix/matrix2.pyx.rej
--- matrix2.pyx
+++ matrix2.pyx
@@ -4267,12 +4274,14 @@
         """
         Return the echelon form of self.
 
-        .. note:: This row reduction does not use division if the
-        matrix is not over a field (e.g., if the matrix is over the
-        integers).  If you want to calculate the echelon form using
-        division, then use :meth:`rref`, which assumes that the matrix
-        entries are in a field (specifically, the field of fractions
-        of the base ring of the matrix).
+        .. note:: 
+
+            This row reduction does not use division if the
+            matrix is not over a field (e.g., if the matrix is over
+            the integers).  If you want to calculate the echelon form
+            using division, then use :meth:`rref`, which assumes that
+            the matrix entries are in a field (specifically, the field
+            of fractions of the base ring of the matrix).
         
         INPUT:
```
Perhaps this ticket needs a rebase?



---

archive/issue_comments_069871.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-22T14:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_events_019187.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-22T14:58:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8008#event-19187"
}
```



---

archive/issue_comments_069872.json:
```json
{
    "body": "rebase of trac-8008-fixes.patch against Sage 4.3.1",
    "created_at": "2010-01-24T12:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

rebase of trac-8008-fixes.patch against Sage 4.3.1



---

archive/issue_comments_069873.json:
```json
{
    "body": "Attachment [trac_8008-fixes-rebase.patch](tarball://root/attachments/some-uuid/ticket8008/trac_8008-fixes-rebase.patch) by mvngu created at 2010-01-24 12:20:31\n\nThe attachment [trac_8008-fixes-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-fixes-rebase.patch) is a rebase of [trac-8008-fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-fixes.patch) against Sage 4.3.1. So my rebase needs some review to ensure I didn't mess up anything. Only apply [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch) and [trac_8008-fixes-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-fixes-rebase.patch).",
    "created_at": "2010-01-24T12:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8008-fixes-rebase.patch](tarball://root/attachments/some-uuid/ticket8008/trac_8008-fixes-rebase.patch) by mvngu created at 2010-01-24 12:20:31

The attachment [trac_8008-fixes-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-fixes-rebase.patch) is a rebase of [trac-8008-fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-fixes.patch) against Sage 4.3.1. So my rebase needs some review to ensure I didn't mess up anything. Only apply [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch) and [trac_8008-fixes-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-fixes-rebase.patch).



---

archive/issue_comments_069874.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-24T12:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69874",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069875.json:
```json
{
    "body": "I think the rebase is fine.  But I wanted to add some doctests for more complicated rings, since sometimes echelon_form is not implemented but rref does work.  Anyone can review that review and then all is well.  Apply only rref.patch and rebase-plus-more.",
    "created_at": "2010-02-04T04:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69875",
    "user": "https://github.com/kcrisman"
}
```

I think the rebase is fine.  But I wanted to add some doctests for more complicated rings, since sometimes echelon_form is not implemented but rref does work.  Anyone can review that review and then all is well.  Apply only rref.patch and rebase-plus-more.



---

archive/issue_comments_069876.json:
```json
{
    "body": "Attachment [trac_8008-rebase-plus-more.patch](tarball://root/attachments/some-uuid/ticket8008/trac_8008-rebase-plus-more.patch) by @kcrisman created at 2010-02-04 04:33:21",
    "created_at": "2010-02-04T04:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69876",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_8008-rebase-plus-more.patch](tarball://root/attachments/some-uuid/ticket8008/trac_8008-rebase-plus-more.patch) by @kcrisman created at 2010-02-04 04:33:21



---

archive/issue_comments_069877.json:
```json
{
    "body": "ping to whoever has time: this is an easy ticket to finish reviewing...",
    "created_at": "2010-02-27T10:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69877",
    "user": "https://github.com/jasongrout"
}
```

ping to whoever has time: this is an easy ticket to finish reviewing...



---

archive/issue_comments_069878.json:
```json
{
    "body": "Patches install fine, sage builds and runs, docs build without warnings and look fine, passes all tests.\n\nPositive review.  Thanks for everybody's work on this one, my students will appreciate it.  6 lines of code, 4 reviewers.  Hmmm.\n\nRelease manager - two patches only, original \"rref\" and then \"rebase-plus-more.\"  Should be able to kill #3211 also.",
    "created_at": "2010-02-27T22:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69878",
    "user": "https://github.com/rbeezer"
}
```

Patches install fine, sage builds and runs, docs build without warnings and look fine, passes all tests.

Positive review.  Thanks for everybody's work on this one, my students will appreciate it.  6 lines of code, 4 reviewers.  Hmmm.

Release manager - two patches only, original "rref" and then "rebase-plus-more."  Should be able to kill #3211 also.



---

archive/issue_comments_069879.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-27T22:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69879",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069880.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019188.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T21:52:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8008#event-19188"
}
```



---

archive/issue_comments_069881.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch)\n2. [trac_8008-rebase-plus-more.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-rebase-plus-more.patch)\n\nJason: You should put a sensible commit message in your patch, together with the ticket number.",
    "created_at": "2010-03-02T21:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch)
2. [trac_8008-rebase-plus-more.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-rebase-plus-more.patch)

Jason: You should put a sensible commit message in your patch, together with the ticket number.



---

archive/issue_comments_069882.json:
```json
{
    "body": "Replying to [comment:12 mvngu]:\n\n> Jason: You should put a sensible commit message in your patch, together with the ticket number.\n\n\nYou'll notice that my recent patches do that :).\n\nI still think the trac ticket number should be automatically prepended to the commit message by the merge script to prevent mistakes and make it easier for patch authors.",
    "created_at": "2010-03-02T22:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8008#issuecomment-69882",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:12 mvngu]:

> Jason: You should put a sensible commit message in your patch, together with the ticket number.


You'll notice that my recent patches do that :).

I still think the trac ticket number should be automatically prepended to the commit message by the merge script to prevent mistakes and make it easier for patch authors.
