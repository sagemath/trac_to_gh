# Issue 5761: Bring doctests of sage/misc/latex.py to 100%

archive/issues_005761.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5761\n\n",
    "created_at": "2009-04-11T19:56:35Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "Bring doctests of sage/misc/latex.py to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5761",
    "user": "https://github.com/rbeezer"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/5761





---

archive/issue_comments_044940.json:
```json
{
    "body": "I'm partway through this, but still need to do much more, and will be away from it for a few days.",
    "created_at": "2009-04-12T01:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44940",
    "user": "https://github.com/rbeezer"
}
```

I'm partway through this, but still need to do much more, and will be away from it for a few days.



---

archive/issue_comments_044941.json:
```json
{
    "body": "Changing assignee from mabshoff to @rbeezer.",
    "created_at": "2009-04-12T01:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44941",
    "user": "https://github.com/rbeezer"
}
```

Changing assignee from mabshoff to @rbeezer.



---

archive/issue_comments_044942.json:
```json
{
    "body": "Bouncing to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bouncing to 3.4.2.

Cheers,

Michael



---

archive/issue_events_013505.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-13T03:40:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5761#event-13505"
}
```



---

archive/issue_comments_044943.json:
```json
{
    "body": "I've gone through an brought the documentation for `latex.py` to full coverage and up to current standards. I've also removed the ~2 year old deprecated method `pdflatex()`.",
    "created_at": "2013-02-01T16:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44943",
    "user": "https://github.com/tscrim"
}
```

I've gone through an brought the documentation for `latex.py` to full coverage and up to current standards. I've also removed the ~2 year old deprecated method `pdflatex()`.



---

archive/issue_comments_044944.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-01T16:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44944",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044945.json:
```json
{
    "body": "Changing keywords from \"\" to \"documentation, coverage, latex\".",
    "created_at": "2013-02-01T16:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44945",
    "user": "https://github.com/tscrim"
}
```

Changing keywords from "" to "documentation, coverage, latex".



---

archive/issue_comments_044946.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-02-02T16:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44946",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_044947.json:
```json
{
    "body": "There are some `True, False` and `None` not surrounded by ````.\n\nAfter\n\n```\n\"\\\\ZZ[x]\n```\n\nin\n\n```\nEXAMPLES::\n\n    # sage: latex.eval(\"\\\\ZZ[x], locals(), filename=\"test\") # This would generate a file named \"test.png\"\n    # ''\n    # sage: latex.eval(\"\\\\ZZ[x], locals(), filename=\"/path/to/test\") # This would generate a file named \"/path/to/test.png\"\n    # ''\n```\n\na \" is missing, otherwise the command will fail. You can use *# not tested* at the end of the line instead of commenting out the examples.\n\nEverything else looks good to me.",
    "created_at": "2013-02-02T16:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44947",
    "user": "https://github.com/a-andre"
}
```

There are some `True, False` and `None` not surrounded by ````.

After

```
"\\ZZ[x]
```

in

```
EXAMPLES::

    # sage: latex.eval("\\ZZ[x], locals(), filename="test") # This would generate a file named "test.png"
    # ''
    # sage: latex.eval("\\ZZ[x], locals(), filename="/path/to/test") # This would generate a file named "/path/to/test.png"
    # ''
```

a " is missing, otherwise the command will fail. You can use *# not tested* at the end of the line instead of commenting out the examples.

Everything else looks good to me.



---

archive/issue_comments_044948.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-05T02:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44948",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_044949.json:
```json
{
    "body": "I believe I caught them all; let me know where if I missed any others.\n\nThanks for the review,\n\nTravis",
    "created_at": "2013-02-05T02:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44949",
    "user": "https://github.com/tscrim"
}
```

I believe I caught them all; let me know where if I missed any others.

Thanks for the review,

Travis



---

archive/issue_comments_044950.json:
```json
{
    "body": "Could you add an additional patch to fix the trac reference in `repr_lincomb()`:\n\n```\nVerify that a certain corner case works (see trac 5707 and 5766)::\n```\n\nand in `latex_varify()`:\n\n```\nif \"is_fname\" flag is True or False.\n```\n",
    "created_at": "2013-02-05T22:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44950",
    "user": "https://github.com/a-andre"
}
```

Could you add an additional patch to fix the trac reference in `repr_lincomb()`:

```
Verify that a certain corner case works (see trac 5707 and 5766)::
```

and in `latex_varify()`:

```
if "is_fname" flag is True or False.
```




---

archive/issue_comments_044951.json:
```json
{
    "body": "Fixed. I've also made the patchbot offending test optional.\n\n-----\n\nFor patchbot:\n\nApply only: trac_5791-latex_docstrings-ts.patch",
    "created_at": "2013-02-05T23:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44951",
    "user": "https://github.com/tscrim"
}
```

Fixed. I've also made the patchbot offending test optional.

-----

For patchbot:

Apply only: trac_5791-latex_docstrings-ts.patch



---

archive/issue_comments_044952.json:
```json
{
    "body": "You added one trailing whitespace after \"An error\"\n\n```\nsage: latex.eval(\"\\ThisIsAnInvalidCommand\", {}) # optional - requires 'convert'\nAn error\n```\n\nBut I think it's no problem. So I'm giving this a positive review. Let's hope the release manager does not complain about the wrong number in the filename. ;)",
    "created_at": "2013-02-06T18:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44952",
    "user": "https://github.com/a-andre"
}
```

You added one trailing whitespace after "An error"

```
sage: latex.eval("\ThisIsAnInvalidCommand", {}) # optional - requires 'convert'
An error
```

But I think it's no problem. So I'm giving this a positive review. Let's hope the release manager does not complain about the wrong number in the filename. ;)



---

archive/issue_comments_044953.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-06T18:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44953",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044954.json:
```json
{
    "body": "Attachment [trac_5761-latex_docstrings-ts.patch](tarball://root/attachments/some-uuid/ticket5761/trac_5761-latex_docstrings-ts.patch) by @tscrim created at 2013-02-06 18:30:53\n\nFixed trailing whitespace and matched ticket number",
    "created_at": "2013-02-06T18:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44954",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_5761-latex_docstrings-ts.patch](tarball://root/attachments/some-uuid/ticket5761/trac_5761-latex_docstrings-ts.patch) by @tscrim created at 2013-02-06 18:30:53

Fixed trailing whitespace and matched ticket number



---

archive/issue_comments_044955.json:
```json
{
    "body": "Fixed. Thank you.\n\nFor patchbot:\n\nApply only: trac_5761-latex_docstrings-ts.patch",
    "created_at": "2013-02-06T18:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44955",
    "user": "https://github.com/tscrim"
}
```

Fixed. Thank you.

For patchbot:

Apply only: trac_5761-latex_docstrings-ts.patch



---

archive/issue_events_013506.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-02-09T12:13:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5761#event-13506"
}
```



---

archive/issue_comments_044956.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-09T12:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5761#issuecomment-44956",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
