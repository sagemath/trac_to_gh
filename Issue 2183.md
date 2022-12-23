# Issue 2183: scipy and special functions

archive/issues_002183.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexan\n\nIn the thread \"[sage-support] Bessel argument order\"\nhttp://blog.gmane.org/gmane.comp.mathematics.sage.support/page=20\nMicheal suggested replacing all \"#random's\" by \"...\" and\nWilliam seconded this. Then William suggested adding the scip option to\nthe functions implemented. This has been done as well.\nThe patch passes \"sage -t\" has some examples added and some\ndocstring typos fixed. The patch is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2183\n\n",
    "created_at": "2008-02-16T23:14:55Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "title": "scipy and special functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2183",
    "user": "wdj"
}
```
Assignee: was

CC:  ncalexan

In the thread "[sage-support] Bessel argument order"
http://blog.gmane.org/gmane.comp.mathematics.sage.support/page=20
Micheal suggested replacing all "#random's" by "..." and
William seconded this. Then William suggested adding the scip option to
the functions implemented. This has been done as well.
The patch passes "sage -t" has some examples added and some
docstring typos fixed. The patch is attached.

Issue created by migration from https://trac.sagemath.org/ticket/2183





---

archive/issue_comments_014339.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-16T23:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14339",
    "user": "wdj"
}
```

Attachment



---

archive/issue_comments_014340.json:
```json
{
    "body": "David,\n\nplease export a single patch next time since this is a single commit only. It makes review on the command line easier and in case of rejects makes it possible to edit the patch by hand.\n\nYou should also add an indicator like \"[with patch|bundle, needs review]\" so that people are aware that there is a patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T23:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14340",
    "user": "mabshoff"
}
```

David,

please export a single patch next time since this is a single commit only. It makes review on the command line easier and in case of rejects makes it possible to edit the patch by hand.

You should also add an indicator like "[with patch|bundle, needs review]" so that people are aware that there is a patch.

Cheers,

Michael



---

archive/issue_comments_014341.json:
```json
{
    "body": "There is also no reason not to still try to get this into 2.10.2, so for something as simple as this it is always recommended to assign against the current milestone.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T23:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14341",
    "user": "mabshoff"
}
```

There is also no reason not to still try to get this into 2.10.2, so for something as simple as this it is always recommended to assign against the current milestone.

Cheers,

Michael



---

archive/issue_comments_014342.json:
```json
{
    "body": "There are some typos in the opening docstring.\n\nThe tests don't always make it clear that scipy agrees with the previous implementations, which is what I was looking for.\n\nI say apply.",
    "created_at": "2008-02-18T19:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14342",
    "user": "ncalexan"
}
```

There are some typos in the opening docstring.

The tests don't always make it clear that scipy agrees with the previous implementations, which is what I was looking for.

I say apply.



---

archive/issue_comments_014343.json:
```json
{
    "body": "I see two typos in the initial docstring and will fix those after I apply the bundle.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T20:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14343",
    "user": "mabshoff"
}
```

I see two typos in the initial docstring and will fix those after I apply the bundle.

Cheers,

Michael



---

archive/issue_comments_014344.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14344",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014345.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T20:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2183#issuecomment-14345",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
