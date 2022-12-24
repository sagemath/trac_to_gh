# Issue 5368: plot3d is broken when variables not given

archive/issues_005368.json:
```json
{
    "body": "Assignee: was\n\nCC:  wcauchois\n\nThis gives an infinite loop in the command line or notebook:\n\n```\nvar('x,y')\nplot3d(x*y^2 - sin(x), (-1,1), (-1,1))\n```\n\n\nPretty bad!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5368\n\n",
    "created_at": "2009-02-25T04:08:50Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plot3d is broken when variables not given",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5368",
    "user": "was"
}
```
Assignee: was

CC:  wcauchois

This gives an infinite loop in the command line or notebook:

```
var('x,y')
plot3d(x*y^2 - sin(x), (-1,1), (-1,1))
```


Pretty bad!!

Issue created by migration from https://trac.sagemath.org/ticket/5368





---

archive/issue_comments_041349.json:
```json
{
    "body": "This is (probably) because fast_float isn't being used for some weird reason:\n\n```\nsage: var('x,y')\n(x, y)\nsage: plot3d(x*y^2 - sin(x), (-1,1), (-1,1))\n^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\nException exceptions.KeyboardInterrupt: KeyboardInterrupt() in  ignored\n^C^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\n^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\n^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\n```\n",
    "created_at": "2009-02-25T23:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5368#issuecomment-41349",
    "user": "was"
}
```

This is (probably) because fast_float isn't being used for some weird reason:

```
sage: var('x,y')
(x, y)
sage: plot3d(x*y^2 - sin(x), (-1,1), (-1,1))
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
Exception exceptions.KeyboardInterrupt: KeyboardInterrupt() in  ignored
^C^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
```




---

archive/issue_comments_041350.json:
```json
{
    "body": "Attachment [trac_5368.patch](tarball://root/attachments/some-uuid/ticket5368/trac_5368.patch) by wcauchois created at 2009-02-26 00:30:45\n\nWilliam's assessment was correct; the function was not being converted into a fast_float form because parametric_plot3d.adapt_to_callable was being invoked incorrectly. I tried to update the documentation of this function according to what I figured out about its workings, so that this mistake might be avoided in the future.",
    "created_at": "2009-02-26T00:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5368#issuecomment-41350",
    "user": "wcauchois"
}
```

Attachment [trac_5368.patch](tarball://root/attachments/some-uuid/ticket5368/trac_5368.patch) by wcauchois created at 2009-02-26 00:30:45

William's assessment was correct; the function was not being converted into a fast_float form because parametric_plot3d.adapt_to_callable was being invoked incorrectly. I tried to update the documentation of this function according to what I figured out about its workings, so that this mistake might be avoided in the future.



---

archive/issue_comments_041351.json:
```json
{
    "body": "No need to add a complete email address, the account name in trac is sufficient.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T05:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5368#issuecomment-41351",
    "user": "mabshoff"
}
```

No need to add a complete email address, the account name in trac is sufficient.

Cheers,

Michael



---

archive/issue_comments_041352.json:
```json
{
    "body": "Attachment [trac_5368-rebased.patch](tarball://root/attachments/some-uuid/ticket5368/trac_5368-rebased.patch) by mabshoff created at 2009-03-05 00:45:59\n\nMerged  trac_5368-rebased.patch in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-05T00:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5368#issuecomment-41352",
    "user": "mabshoff"
}
```

Attachment [trac_5368-rebased.patch](tarball://root/attachments/some-uuid/ticket5368/trac_5368-rebased.patch) by mabshoff created at 2009-03-05 00:45:59

Merged  trac_5368-rebased.patch in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_041353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-05T00:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5368#issuecomment-41353",
    "user": "mabshoff"
}
```

Resolution: fixed
