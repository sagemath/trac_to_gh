# Issue 4903: convert sage.calculus.* docstrings to Sphinx

archive/issues_004903.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4903\n\n",
    "created_at": "2009-01-01T22:46:01Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "convert sage.calculus.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4903",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4903





---

archive/issue_comments_037195.json:
```json
{
    "body": "Changing assignee from tba to mhansen.",
    "created_at": "2009-01-02T03:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37195",
    "user": "mhansen"
}
```

Changing assignee from tba to mhansen.



---

archive/issue_comments_037196.json:
```json
{
    "body": "Patch at http://sage.math.washington.edu/home/mhansen/trac_4903.patch",
    "created_at": "2009-01-02T03:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37196",
    "user": "mhansen"
}
```

Patch at http://sage.math.washington.edu/home/mhansen/trac_4903.patch



---

archive/issue_comments_037197.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-02T03:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37197",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037198.json:
```json
{
    "body": "* In minpoly (around line 1659)\n\n\n```\n+        ``self`` and use PARI's algdep to get a candidate\n+        minpoly `f`. If `f(``self``)`,\n+        evaluated to a higher precision, is close enough to 0 then evaluate\n+        `f(``self``)` symbolically, attempting to prove\n+        vanishing. If this fails, and ``epsilon`` is non-zero,\n+        return `f` if and only if\n+        `f(``self``) < ``epsilon```.\n```\n\nis not parsing correctly. See\n\n```\nhttp://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/sage/calculus/calculus.html\n```\n\nI guess sphinx is having trouble with the nested quotes?\n\nAnother problem with the html conversion is that the footer (in ubuntu seamonkey) in that file is\nnot offset as blue. (Eg, the next link at the bottom of the page does not appear as it is overwritten by the white page background, but it is there if you mose over it.) It does render correctly in epiphany however. Does anyone but me even use seamonkey?",
    "created_at": "2009-01-02T12:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37198",
    "user": "wdj"
}
```

* In minpoly (around line 1659)


```
+        ``self`` and use PARI's algdep to get a candidate
+        minpoly `f`. If `f(``self``)`,
+        evaluated to a higher precision, is close enough to 0 then evaluate
+        `f(``self``)` symbolically, attempting to prove
+        vanishing. If this fails, and ``epsilon`` is non-zero,
+        return `f` if and only if
+        `f(``self``) < ``epsilon```.
```

is not parsing correctly. See

```
http://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/sage/calculus/calculus.html
```

I guess sphinx is having trouble with the nested quotes?

Another problem with the html conversion is that the footer (in ubuntu seamonkey) in that file is
not offset as blue. (Eg, the next link at the bottom of the page does not appear as it is overwritten by the white page background, but it is there if you mose over it.) It does render correctly in epiphany however. Does anyone but me even use seamonkey?



---

archive/issue_comments_037199.json:
```json
{
    "body": "Attachment [trac_4903-2.patch](tarball://root/attachments/some-uuid/ticket4903/trac_4903-2.patch) by mhansen created at 2009-01-02 20:32:51\n\nI attached a patch which fixes the problem with the nested quotes.\n\nI'm not seeing the problem that you are in Firefox 3.0.",
    "created_at": "2009-01-02T20:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37199",
    "user": "mhansen"
}
```

Attachment [trac_4903-2.patch](tarball://root/attachments/some-uuid/ticket4903/trac_4903-2.patch) by mhansen created at 2009-01-02 20:32:51

I attached a patch which fixes the problem with the nested quotes.

I'm not seeing the problem that you are in Firefox 3.0.



---

archive/issue_comments_037200.json:
```json
{
    "body": "Attachment [sage.calculus-final.patch](tarball://root/attachments/some-uuid/ticket4903/sage.calculus-final.patch) by cwitty created at 2009-02-22 03:39:58",
    "created_at": "2009-02-22T03:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37200",
    "user": "cwitty"
}
```

Attachment [sage.calculus-final.patch](tarball://root/attachments/some-uuid/ticket4903/sage.calculus-final.patch) by cwitty created at 2009-02-22 03:39:58



---

archive/issue_comments_037201.json:
```json
{
    "body": "Attachment [trac4903-tiny-fix.patch](tarball://root/attachments/some-uuid/ticket4903/trac4903-tiny-fix.patch) by cwitty created at 2009-02-22 03:40:34\n\nI've posted a tiny fix to make doctests pass in sage.calculus.* after sphinxification.",
    "created_at": "2009-02-22T03:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37201",
    "user": "cwitty"
}
```

Attachment [trac4903-tiny-fix.patch](tarball://root/attachments/some-uuid/ticket4903/trac4903-tiny-fix.patch) by cwitty created at 2009-02-22 03:40:34

I've posted a tiny fix to make doctests pass in sage.calculus.* after sphinxification.



---

archive/issue_comments_037202.json:
```json
{
    "body": "I looked through \n\n```\nhttp://sage.math.washington.edu/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/calculus.html\n```\n\nand this looks good to me.",
    "created_at": "2009-02-22T12:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37202",
    "user": "wdj"
}
```

I looked through 

```
http://sage.math.washington.edu/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/calculus.html
```

and this looks good to me.



---

archive/issue_comments_037203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T17:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37203",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037204.json:
```json
{
    "body": "Merged sage.calculus-final.patch in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T17:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37204",
    "user": "mabshoff"
}
```

Merged sage.calculus-final.patch in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_037205.json:
```json
{
    "body": "Merged trac4903-tiny-fix.patch in Sage 3.4.alpha0 to fix a doctest failure not in Mike's patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T20:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4903#issuecomment-37205",
    "user": "mabshoff"
}
```

Merged trac4903-tiny-fix.patch in Sage 3.4.alpha0 to fix a doctest failure not in Mike's patch.

Cheers,

Michael
