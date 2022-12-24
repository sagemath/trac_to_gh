# Issue 6594: doctest issue in "r.py" (follow-up to #6379)

archive/issues_006594.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  mvngu\n\nIf the file \"r_commandlist.sobj\" under $DOT_SAGE is missing, the first time you run a doctest over \"r.py\", you'll get:\n\n```\nsage -t  \"devel/sage/sage/interfaces/r.py\"                  \n**********************************************************************\nFile \"/Users/Shared/sage/sage-4.1.1.alpha0/devel/sage/sage/interfaces/r.py\", line 838:\n    sage: r.completions('tes')\nExpected:\n    ['testPlatformEquivalence', 'testVirtual']\nGot:\n    <BLANKLINE>\n    Building R command completion list (this takes\n    a few seconds only the first time you do it).\n    To force rebuild later, delete /Users/georgweber/.sage//r_commandlist.sobj.\n    ['testPlatformEquivalence', 'testVirtual']\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_34\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/Shared/sage/sage-4.1.1.alpha0/tmp/.doctest_r.py\n```\n\nor some error message closely related. If you run the doctest a second time, the failure vanishes, since the file in $DOT_SAGE had been built. But that is not something one wants to happen during doctesting.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6594\n\n",
    "created_at": "2009-07-22T18:43:24Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "doctest issue in \"r.py\" (follow-up to #6379)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6594",
    "user": "GeorgSWeber"
}
```
Assignee: GeorgSWeber

CC:  mvngu

If the file "r_commandlist.sobj" under $DOT_SAGE is missing, the first time you run a doctest over "r.py", you'll get:

```
sage -t  "devel/sage/sage/interfaces/r.py"                  
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.alpha0/devel/sage/sage/interfaces/r.py", line 838:
    sage: r.completions('tes')
Expected:
    ['testPlatformEquivalence', 'testVirtual']
Got:
    <BLANKLINE>
    Building R command completion list (this takes
    a few seconds only the first time you do it).
    To force rebuild later, delete /Users/georgweber/.sage//r_commandlist.sobj.
    ['testPlatformEquivalence', 'testVirtual']
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_34
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/Shared/sage/sage-4.1.1.alpha0/tmp/.doctest_r.py
```

or some error message closely related. If you run the doctest a second time, the failure vanishes, since the file in $DOT_SAGE had been built. But that is not something one wants to happen during doctesting.

Issue created by migration from https://trac.sagemath.org/ticket/6594





---

archive/issue_comments_053961.json:
```json
{
    "body": "tested against 4.1.1.alpha0",
    "created_at": "2009-07-22T18:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6594#issuecomment-53961",
    "user": "GeorgSWeber"
}
```

tested against 4.1.1.alpha0



---

archive/issue_comments_053962.json:
```json
{
    "body": "Attachment [trac_6594-R_doctest.patch](tarball://root/attachments/some-uuid/ticket6594/trac_6594-R_doctest.patch) by GeorgSWeber created at 2009-07-22 18:48:29\n\nMinh, could please review this one-liner?\n(Cough, cough ...)",
    "created_at": "2009-07-22T18:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6594#issuecomment-53962",
    "user": "GeorgSWeber"
}
```

Attachment [trac_6594-R_doctest.patch](tarball://root/attachments/some-uuid/ticket6594/trac_6594-R_doctest.patch) by GeorgSWeber created at 2009-07-22 18:48:29

Minh, could please review this one-liner?
(Cough, cough ...)



---

archive/issue_comments_053963.json:
```json
{
    "body": "Doctesting r.py after (if it there at all) deleting the file $HOME/.sage/r_commandlist.sobj will always fail --- unless one has this patch applied. So I hope it is a very easy review.",
    "created_at": "2009-07-22T18:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6594#issuecomment-53963",
    "user": "GeorgSWeber"
}
```

Doctesting r.py after (if it there at all) deleting the file $HOME/.sage/r_commandlist.sobj will always fail --- unless one has this patch applied. So I hope it is a very easy review.



---

archive/issue_comments_053964.json:
```json
{
    "body": "With \n\n```\n~/.sage/r_commandlist.sobj\n```\n\ndoctests passed. Without it, doctests failed. With patch and with `~/.sage/r_commandlist.sobj`: doctests passed. Doctests also passed with the patch and without `~/.sage/r_commandlist.sobj`. So this is a\n\n```\n***************\nPOSITIVE REVIEW\n***************\n```\n\nLet's make R statistically significant :-)",
    "created_at": "2009-07-23T00:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6594#issuecomment-53964",
    "user": "mvngu"
}
```

With 

```
~/.sage/r_commandlist.sobj
```

doctests passed. Without it, doctests failed. With patch and with `~/.sage/r_commandlist.sobj`: doctests passed. Doctests also passed with the patch and without `~/.sage/r_commandlist.sobj`. So this is a

```
***************
POSITIVE REVIEW
***************
```

Let's make R statistically significant :-)



---

archive/issue_comments_053965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T02:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6594#issuecomment-53965",
    "user": "mvngu"
}
```

Resolution: fixed
