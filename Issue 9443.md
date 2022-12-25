# Issue 9443: infinite polynomial ring is_integral_domain and is_field omit optional argument 'proof'

archive/issues_009443.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: infinite polynomial ring\n\nOther implementations of is_integral_domain allow an argument 'proof' whose default value is False.  Infinite polynomial ring omits this argument in its definition of is_integral_domain:\n\n```\nsage: W = PolynomialRing(InfinitePolynomialRing(QQ,'a'),2,'x,y')\nsage: W.is_integral_domain()\n-------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: is_integral_domain() takes exactly 1 argument (2 given)\n```\n\nsame goes for is_field:\n\n```\nsage: W = PowerSeriesRing(InfinitePolynomialRing(QQ,'a'),'x')\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: is_field() got an unexpected keyword argument 'proof'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9443\n\n",
    "closed_at": "2010-09-15T11:14:08Z",
    "created_at": "2010-07-07T02:52:26Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "infinite polynomial ring is_integral_domain and is_field omit optional argument 'proof'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9443",
    "user": "https://github.com/nilesjohnson"
}
```
Assignee: @aghitza

Keywords: infinite polynomial ring

Other implementations of is_integral_domain allow an argument 'proof' whose default value is False.  Infinite polynomial ring omits this argument in its definition of is_integral_domain:

```
sage: W = PolynomialRing(InfinitePolynomialRing(QQ,'a'),2,'x,y')
sage: W.is_integral_domain()
-------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: is_integral_domain() takes exactly 1 argument (2 given)
```

same goes for is_field:

```
sage: W = PowerSeriesRing(InfinitePolynomialRing(QQ,'a'),'x')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: is_field() got an unexpected keyword argument 'proof'
```

Issue created by migration from https://trac.sagemath.org/ticket/9443





---

archive/issue_comments_090326.json:
```json
{
    "body": "Attachment [trac_9943_default_arguments.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9943_default_arguments.patch) by @nilesjohnson created at 2010-07-07 02:58:33\n\nadd argument 'proof' with default value False to is_field and is_integral_domain",
    "created_at": "2010-07-07T02:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90326",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_9943_default_arguments.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9943_default_arguments.patch) by @nilesjohnson created at 2010-07-07 02:58:33

add argument 'proof' with default value False to is_field and is_integral_domain



---

archive/issue_comments_090327.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-07T03:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90327",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090328.json:
```json
{
    "body": "apply after previous patch; includes doctests, and updates a few functions to accept positional and keyword arguments; removes duplicate definition of is_field",
    "created_at": "2010-07-12T15:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90328",
    "user": "https://github.com/nilesjohnson"
}
```

apply after previous patch; includes doctests, and updates a few functions to accept positional and keyword arguments; removes duplicate definition of is_field



---

archive/issue_comments_090329.json:
```json
{
    "body": "Attachment [trac_9943_default_arguments_doctests.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9943_default_arguments_doctests.patch) by @simon-king-jena created at 2010-07-30 16:53:56\n\nThank you for working on Infinite Polynomial Rings! Why didn't you add me (as original author) to Cc? I think I am a natural candidate for being reviewer...\n\nFirst of all, the patches apply cleanly, and `sage -b` does not complain.\n\nSecond, I think the patches provide a clean solution. I am sorry that I didn't use `*args` and `**kwds` in the first place.\n\nThird, it is a formal requirement that the commit message of each patch must point to the relevant ticket. So, could you please add \"#9443: \" or so to the commit messages? Moreover, the attachments name a wrong ticket number (9943 rather than 9443).\n\nFourth, I am now running `make ptestlong` and report back whether it has worked.\n\nFifth, since you fix a bug, I believe the priority is certainly not \"trivial\". I am promoting it to \"major\".",
    "created_at": "2010-07-30T16:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90329",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_9943_default_arguments_doctests.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9943_default_arguments_doctests.patch) by @simon-king-jena created at 2010-07-30 16:53:56

Thank you for working on Infinite Polynomial Rings! Why didn't you add me (as original author) to Cc? I think I am a natural candidate for being reviewer...

First of all, the patches apply cleanly, and `sage -b` does not complain.

Second, I think the patches provide a clean solution. I am sorry that I didn't use `*args` and `**kwds` in the first place.

Third, it is a formal requirement that the commit message of each patch must point to the relevant ticket. So, could you please add "#9443: " or so to the commit messages? Moreover, the attachments name a wrong ticket number (9943 rather than 9443).

Fourth, I am now running `make ptestlong` and report back whether it has worked.

Fifth, since you fix a bug, I believe the priority is certainly not "trivial". I am promoting it to "major".



---

archive/issue_comments_090330.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-30T16:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90330",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090331.json:
```json
{
    "body": "`make ptestlong` is not done yet. But at least I can confirm that the original problem is fixed:\n\n```\nsage: W = PolynomialRing(InfinitePolynomialRing(QQ,'a'),2,'x,y')\nsage: W.is_integral_domain()\nTrue\nsage: W = PowerSeriesRing(InfinitePolynomialRing(QQ,'a'),'x')\nsage: W\nPower Series Ring in x over Infinite polynomial ring in a over Rational Field\n```",
    "created_at": "2010-07-30T17:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90331",
    "user": "https://github.com/simon-king-jena"
}
```

`make ptestlong` is not done yet. But at least I can confirm that the original problem is fixed:

```
sage: W = PolynomialRing(InfinitePolynomialRing(QQ,'a'),2,'x,y')
sage: W.is_integral_domain()
True
sage: W = PowerSeriesRing(InfinitePolynomialRing(QQ,'a'),'x')
sage: W
Power Series Ring in x over Infinite polynomial ring in a over Rational Field
```



---

archive/issue_comments_090332.json:
```json
{
    "body": "All tests pass. \n\nSo, I can give this a positive review - modulo the minor nitpicking about the commit message. This is easy to change.\n\nI hope it is, in this case, correct to mark this ticket as \"positive review\" but keep the \"work issues\" field.",
    "created_at": "2010-07-30T20:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90332",
    "user": "https://github.com/simon-king-jena"
}
```

All tests pass. 

So, I can give this a positive review - modulo the minor nitpicking about the commit message. This is easy to change.

I hope it is, in this case, correct to mark this ticket as "positive review" but keep the "work issues" field.



---

archive/issue_comments_090333.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-30T20:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90333",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_090334.json:
```json
{
    "body": "Attachment [trac_9443_default_arguments_combined.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9443_default_arguments_combined.patch) by @nilesjohnson created at 2010-08-01 15:09:47\n\ncompined patch replacing the previous two; patch name and commit message fixed",
    "created_at": "2010-08-01T15:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90334",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_9443_default_arguments_combined.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9443_default_arguments_combined.patch) by @nilesjohnson created at 2010-08-01 15:09:47

compined patch replacing the previous two; patch name and commit message fixed



---

archive/issue_comments_090335.json:
```json
{
    "body": "Thanks!  The combined patch should now be complete.",
    "created_at": "2010-08-01T15:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90335",
    "user": "https://github.com/nilesjohnson"
}
```

Thanks!  The combined patch should now be complete.



---

archive/issue_comments_090336.json:
```json
{
    "body": "Applying [attachment:trac_9443_default_arguments_combined.patch] to the forthcoming Sage 4.5.2, which is just 4.5.2.rc1 + #9226, I see\n\n```\nHunk #1 FAILED at 1036\n1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/infinite_polynomial_ring.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_9443_default_arguments_combined.patch\n```\nThe reject file's contents:\n\n```diff\n--- infinite_polynomial_ring.py\n+++ infinite_polynomial_ring.py\n@@ -1037,10 +1037,17 @@\n         \"\"\"\n         return False\n \n-    def is_field(self,**kwds):\n+    def is_field(self, *args, **kwds):\n         \"\"\"\n-        Since Infinite Polynomial Rings must have at least one generator, they\n-        have infinitely many variables and thus never are fields.\n+        Return ``False``, since an infinite polynomial ring has at least one\n+        generator and hence infinitely many variables.\n+\n+        EXAMPLES::\n+\n+            sage: R.<x, y> = InfinitePolynomialRing(QQ)\n+            sage: R.is_field()\n+            False\n+\n \n         TESTS::\n \n```\n\nCan someone rebase the patch when it's convenient?  It might be sufficient to work from #9114.",
    "created_at": "2010-08-07T06:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90336",
    "user": "https://github.com/qed777"
}
```

Applying [attachment:trac_9443_default_arguments_combined.patch] to the forthcoming Sage 4.5.2, which is just 4.5.2.rc1 + #9226, I see

```
Hunk #1 FAILED at 1036
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/infinite_polynomial_ring.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_9443_default_arguments_combined.patch
```
The reject file's contents:

```diff
--- infinite_polynomial_ring.py
+++ infinite_polynomial_ring.py
@@ -1037,10 +1037,17 @@
         """
         return False
 
-    def is_field(self,**kwds):
+    def is_field(self, *args, **kwds):
         """
-        Since Infinite Polynomial Rings must have at least one generator, they
-        have infinitely many variables and thus never are fields.
+        Return ``False``, since an infinite polynomial ring has at least one
+        generator and hence infinitely many variables.
+
+        EXAMPLES::
+
+            sage: R.<x, y> = InfinitePolynomialRing(QQ)
+            sage: R.is_field()
+            False
+
 
         TESTS::
 
```

Can someone rebase the patch when it's convenient?  It might be sufficient to work from #9114.



---

archive/issue_comments_090337.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-07T06:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90337",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090338.json:
```json
{
    "body": "Attachment [trac_9443_default_arguments_combined_rebased.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9443_default_arguments_combined_rebased.patch) by @nilesjohnson created at 2010-08-10 20:54:24\n\nrebased against #9114 (for 4.5.2); apply only this patch.",
    "created_at": "2010-08-10T20:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90338",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_9443_default_arguments_combined_rebased.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9443_default_arguments_combined_rebased.patch) by @nilesjohnson created at 2010-08-10 20:54:24

rebased against #9114 (for 4.5.2); apply only this patch.



---

archive/issue_comments_090339.json:
```json
{
    "body": "should now apply cleanly, although I admit I haven't had time to test it thoroughly.",
    "created_at": "2010-08-10T20:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90339",
    "user": "https://github.com/nilesjohnson"
}
```

should now apply cleanly, although I admit I haven't had time to test it thoroughly.



---

archive/issue_comments_090340.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-10T20:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90340",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090341.json:
```json
{
    "body": "Attachment [trac_9443_default_arguments_combined_rebased.2.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9443_default_arguments_combined_rebased.2.patch) by @qed777 created at 2010-08-10 22:39:15\n\nRestore commit string.  Apply only this patch.",
    "created_at": "2010-08-10T22:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90341",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9443_default_arguments_combined_rebased.2.patch](tarball://root/attachments/some-uuid/ticket9443/trac_9443_default_arguments_combined_rebased.2.patch) by @qed777 created at 2010-08-10 22:39:15

Restore commit string.  Apply only this patch.



---

archive/issue_comments_090342.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-10T22:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90342",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090343.json:
```json
{
    "body": "Thanks!  The new patch applies cleanly to 4.5.3.alpha0.  I've attached V2, which simply restores the earlier fixed commit message.",
    "created_at": "2010-08-10T22:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90343",
    "user": "https://github.com/qed777"
}
```

Thanks!  The new patch applies cleanly to 4.5.3.alpha0.  I've attached V2, which simply restores the earlier fixed commit message.



---

archive/issue_events_023352.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T11:14:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9443#event-23352"
}
```



---

archive/issue_comments_090344.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9443#issuecomment-90344",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
