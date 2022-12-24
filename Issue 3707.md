# Issue 3707: Make all common Sage classes convertible to SymPy

archive/issues_003707.json:
```json
{
    "body": "Assignee: gfurnish\n\nThe attached patch is here like a request for comments. \n\nWe are about to release a new sympy that contains thorough tests for Sage <-> SymPy conversion:\n\nhttp://hg.sympy.org/sympy/file/16cfc09420ee/sympy/test_external/test_sage.py\n\nWhen sage 3.0.6 gets released, I'll create a new sympy spkg and expand tests in Sage too, so that we are sure things work in Sage environment too.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3707\n\n",
    "created_at": "2008-07-22T11:19:25Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "Make all common Sage classes convertible to SymPy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3707",
    "user": "certik"
}
```
Assignee: gfurnish

The attached patch is here like a request for comments. 

We are about to release a new sympy that contains thorough tests for Sage <-> SymPy conversion:

http://hg.sympy.org/sympy/file/16cfc09420ee/sympy/test_external/test_sage.py

When sage 3.0.6 gets released, I'll create a new sympy spkg and expand tests in Sage too, so that we are sure things work in Sage environment too.

Issue created by migration from https://trac.sagemath.org/ticket/3707





---

archive/issue_comments_026306.json:
```json
{
    "body": "**Review**\n* the patch contains functions without doctests and some without documentation\n* Maybe `import sympy` could be avoided in each method using a `late_import` tricK?",
    "created_at": "2008-08-10T13:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26306",
    "user": "malb"
}
```

**Review**
* the patch contains functions without doctests and some without documentation
* Maybe `import sympy` could be avoided in each method using a `late_import` tricK?



---

archive/issue_comments_026307.json:
```json
{
    "body": "Thanks for the review. I'll write doctests and learn about late_import() to see how I could use it.",
    "created_at": "2008-08-10T15:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26307",
    "user": "certik"
}
```

Thanks for the review. I'll write doctests and learn about late_import() to see how I could use it.



---

archive/issue_comments_026308.json:
```json
{
    "body": "Replying to [comment:3 certik]:\n> Thanks for the review. I'll write doctests and learn about late_import() to see how I could use it.\n\nExamples of this idea (we don't have a framework for that), can be found in:\n\n* `sage.rings.finite_field_givaro`\n* `sage.libs.pari.gen`\n* `sage.rings.integer`\n\nLooking at those should get you started.",
    "created_at": "2008-08-10T16:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26308",
    "user": "malb"
}
```

Replying to [comment:3 certik]:
> Thanks for the review. I'll write doctests and learn about late_import() to see how I could use it.

Examples of this idea (we don't have a framework for that), can be found in:

* `sage.rings.finite_field_givaro`
* `sage.libs.pari.gen`
* `sage.rings.integer`

Looking at those should get you started.



---

archive/issue_comments_026309.json:
```json
{
    "body": "Attachment [sympy0.6.2fix.patch](tarball://root/attachments/some-uuid/ticket3707/sympy0.6.2fix.patch) by certik created at 2008-08-17 20:37:07\n\napply this together with sympy-0.6.2.spkg",
    "created_at": "2008-08-17T20:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26309",
    "user": "certik"
}
```

Attachment [sympy0.6.2fix.patch](tarball://root/attachments/some-uuid/ticket3707/sympy0.6.2fix.patch) by certik created at 2008-08-17 20:37:07

apply this together with sympy-0.6.2.spkg



---

archive/issue_comments_026310.json:
```json
{
    "body": "Attachment [sage_sympy.patch](tarball://root/attachments/some-uuid/ticket3707/sage_sympy.patch) by certik created at 2008-08-17 20:37:32",
    "created_at": "2008-08-17T20:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26310",
    "user": "certik"
}
```

Attachment [sage_sympy.patch](tarball://root/attachments/some-uuid/ticket3707/sage_sympy.patch) by certik created at 2008-08-17 20:37:32



---

archive/issue_comments_026311.json:
```json
{
    "body": "Please update this spkg:\n\nhttp://sage.math.washington.edu/home/ondrej/spkg/sympy-0.6.2.spkg\n\nand apply the above two patches.\n\nmalb: I wrote docstrings and doctests. I didn't use late_import(), as I think in pure python it won't slow things that much and there is a question where I should put this late_import(). But if you think it's necessary, I'll fix that.",
    "created_at": "2008-08-17T20:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26311",
    "user": "certik"
}
```

Please update this spkg:

http://sage.math.washington.edu/home/ondrej/spkg/sympy-0.6.2.spkg

and apply the above two patches.

malb: I wrote docstrings and doctests. I didn't use late_import(), as I think in pure python it won't slow things that much and there is a question where I should put this late_import(). But if you think it's necessary, I'll fix that.



---

archive/issue_comments_026312.json:
```json
{
    "body": "Attachment [trac_3707_fixup.patch](tarball://root/attachments/some-uuid/ticket3707/trac_3707_fixup.patch) by malb created at 2008-08-18 10:07:56\n\napply after the other patches",
    "created_at": "2008-08-18T10:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26312",
    "user": "malb"
}
```

Attachment [trac_3707_fixup.patch](tarball://root/attachments/some-uuid/ticket3707/trac_3707_fixup.patch) by malb created at 2008-08-18 10:07:56

apply after the other patches



---

archive/issue_comments_026313.json:
```json
{
    "body": "**Referee Report**\n* one new function didn't have a doctest (fixed in attached patch)\n* some doctests were failing (fixed in attached patch)\n* `#indirect doctest` directive was missing to make `sage -coverage` happy (fixed in attached patch)\n* One typo (fixed in attached patch)\n\nI'd give the patches a positive review if my fixes are accepted by Ondrej. Ondrej, you now need to check my fixup patch and review it. If you settle for a positive review, then you can change the title to `positive review`.",
    "created_at": "2008-08-18T10:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26313",
    "user": "malb"
}
```

**Referee Report**
* one new function didn't have a doctest (fixed in attached patch)
* some doctests were failing (fixed in attached patch)
* `#indirect doctest` directive was missing to make `sage -coverage` happy (fixed in attached patch)
* One typo (fixed in attached patch)

I'd give the patches a positive review if my fixes are accepted by Ondrej. Ondrej, you now need to check my fixup patch and review it. If you settle for a positive review, then you can change the title to `positive review`.



---

archive/issue_comments_026314.json:
```json
{
    "body": "Oops, thanks you did so much work with it, this is weird, all tests passed for me before posting here. Let me investigate what went wrong, I'll report later.",
    "created_at": "2008-08-18T10:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26314",
    "user": "certik"
}
```

Oops, thanks you did so much work with it, this is weird, all tests passed for me before posting here. Let me investigate what went wrong, I'll report later.



---

archive/issue_comments_026315.json:
```json
{
    "body": "Attachment [trac_3707_fixup.2.patch](tarball://root/attachments/some-uuid/ticket3707/trac_3707_fixup.2.patch) by certik created at 2008-08-19 22:23:31",
    "created_at": "2008-08-19T22:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26315",
    "user": "certik"
}
```

Attachment [trac_3707_fixup.2.patch](tarball://root/attachments/some-uuid/ticket3707/trac_3707_fixup.2.patch) by certik created at 2008-08-19 22:23:31



---

archive/issue_comments_026316.json:
```json
{
    "body": "My review is +1, only please apply this patch:\n\ntrac_3707_fixup.2.patch\n\ninstead of yours. The diff is this:\n\n```\n$ hg di\ndiff -r 25553a0bd339 sage/calculus/calculus.py\n--- a/sage/calculus/calculus.py\tMon Aug 18 11:04:52 2008 +0100\n+++ b/sage/calculus/calculus.py\tTue Aug 19 15:18:50 2008 -0700\n@@ -5099,7 +5099,8 @@\n \n         EXAMPLE:\n             sage: x,y = var('x,y')\n-            sage: sympy(x) # indirect doctest\n+            sage: import sympy\n+            sage: sympy.sympify(x) # indirect doctest\n             x\n         \"\"\"\n```\n\n\n\nyour version didn't pass doctests, but this should fix it. \n\nThanks again for the patch you did, it really helps. I hope all should be fine now. I'll attache the result of sage tests once it finishes.",
    "created_at": "2008-08-19T22:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26316",
    "user": "certik"
}
```

My review is +1, only please apply this patch:

trac_3707_fixup.2.patch

instead of yours. The diff is this:

```
$ hg di
diff -r 25553a0bd339 sage/calculus/calculus.py
--- a/sage/calculus/calculus.py	Mon Aug 18 11:04:52 2008 +0100
+++ b/sage/calculus/calculus.py	Tue Aug 19 15:18:50 2008 -0700
@@ -5099,7 +5099,8 @@
 
         EXAMPLE:
             sage: x,y = var('x,y')
-            sage: sympy(x) # indirect doctest
+            sage: import sympy
+            sage: sympy.sympify(x) # indirect doctest
             x
         """
```



your version didn't pass doctests, but this should fix it. 

Thanks again for the patch you did, it really helps. I hope all should be fine now. I'll attache the result of sage tests once it finishes.



---

archive/issue_comments_026317.json:
```json
{
    "body": "Here is a result of the tests:\n\nhttp://sage.math.washington.edu/home/ondrej/ext/sage/devel/sage/test.log\n\nall tests pass. :)\n\nSo as to me, it's ok to go in.",
    "created_at": "2008-08-19T23:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26317",
    "user": "certik"
}
```

Here is a result of the tests:

http://sage.math.washington.edu/home/ondrej/ext/sage/devel/sage/test.log

all tests pass. :)

So as to me, it's ok to go in.



---

archive/issue_comments_026318.json:
```json
{
    "body": "I give this a positive review. Ondrej could give the release manager (probably mabshoff) a precise list of patches to apply in which order in a comment? I suspect:\n* sympy0.6.2fix.patch\n* sage_sympy.patch\n* trac_3707_fixup.2.patch\nin that order.",
    "created_at": "2008-08-19T23:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26318",
    "user": "malb"
}
```

I give this a positive review. Ondrej could give the release manager (probably mabshoff) a precise list of patches to apply in which order in a comment? I suspect:
* sympy0.6.2fix.patch
* sage_sympy.patch
* trac_3707_fixup.2.patch
in that order.



---

archive/issue_comments_026319.json:
```json
{
    "body": "Yes, apply the new spkg first and then the patches in exactly this order.\n\nThanks for the review!",
    "created_at": "2008-08-20T07:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26319",
    "user": "certik"
}
```

Yes, apply the new spkg first and then the patches in exactly this order.

Thanks for the review!



---

archive/issue_comments_026320.json:
```json
{
    "body": "Ondrej,\n\nI did a number of cleanups to spkg-install and SPKG.txt. SPKG.txt still needs some more work, but I guess this has been a step in the right direction. Please base future sympy.spkgs of this one - I did not change the version number.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T19:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26320",
    "user": "mabshoff"
}
```

Ondrej,

I did a number of cleanups to spkg-install and SPKG.txt. SPKG.txt still needs some more work, but I guess this has been a step in the right direction. Please base future sympy.spkgs of this one - I did not change the version number.

Cheers,

Michael



---

archive/issue_comments_026321.json:
```json
{
    "body": "Merged the patches listed above in Sage 3.1.2.alpha0",
    "created_at": "2008-08-22T19:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26321",
    "user": "mabshoff"
}
```

Merged the patches listed above in Sage 3.1.2.alpha0



---

archive/issue_comments_026322.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-22T19:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3707#issuecomment-26322",
    "user": "mabshoff"
}
```

Resolution: fixed
