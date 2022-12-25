# Issue 5521: fix serious bug in pickling the rational numbers and the magma interface

archive/issues_005521.json:
```json
{
    "body": "Assignee: @malb\n\nAfter converting QQ to Magma it suddenly stops pickling!\n\n\n```\nwstein@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: loads(dumps(QQ))\nRational Field\nsage: magma(QQ)\nRational Field\nsage: loads(dumps(QQ))\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n| Sage Version 3.4, Release Date: 2009-03-11                         |\n| Type notebook() for the GUI, and license() for information.        |\n/scratch/wstein/sage/temp/sage.math.washington.edu/13063/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:6159)()\n\nRuntimeError: (TypeError(RuntimeError('Error evaluating Magma code.\\nIN:_sage_[3]:=Rational Field;\\nOUT:\\n>> _sage_[3]:=Rational Field;\\n                       ^\\nUser error: bad syntax',),), <function reduce_load at 0x11318c0>, (Magma, 'Rational Field'))\ninvalid data stream\ninvalid load key, 'x'.\nUnable to load pickled data.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5521\n\n",
    "created_at": "2009-03-14T22:39:00Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "fix serious bug in pickling the rational numbers and the magma interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5521",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

After converting QQ to Magma it suddenly stops pickling!


```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: loads(dumps(QQ))
Rational Field
sage: magma(QQ)
Rational Field
sage: loads(dumps(QQ))
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
/scratch/wstein/sage/temp/sage.math.washington.edu/13063/_scratch_wstein_sage_init_sage_0.py in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:6159)()

RuntimeError: (TypeError(RuntimeError('Error evaluating Magma code.\nIN:_sage_[3]:=Rational Field;\nOUT:\n>> _sage_[3]:=Rational Field;\n                       ^\nUser error: bad syntax',),), <function reduce_load at 0x11318c0>, (Magma, 'Rational Field'))
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.
```


Issue created by migration from https://trac.sagemath.org/ticket/5521





---

archive/issue_comments_042859.json:
```json
{
    "body": "Attachment [trac_5521.patch](tarball://root/attachments/some-uuid/ticket5521/trac_5521.patch) by mabshoff created at 2009-03-23 19:19:42\n\nThis patch causes 20 doctests to fail in extended_rational_field.py starting with:\n\n```\nsage -t -long \"devel/sage/sage/rings/extended_rational_field.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/extended_rational_field.py\", line 51:\n    sage: loads(dumps(f))\nExpected:\n    Natural morphism:\n      From: Rational Field\n      To:   Extended Rational Field\nGot:\n    Natural endomorphism of Rational Field\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/extended_rational_field.py\", line 110:\n    sage: E == loads(dumps(E))\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n<SNIP>\n```\n",
    "created_at": "2009-03-23T19:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5521#issuecomment-42859",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5521.patch](tarball://root/attachments/some-uuid/ticket5521/trac_5521.patch) by mabshoff created at 2009-03-23 19:19:42

This patch causes 20 doctests to fail in extended_rational_field.py starting with:

```
sage -t -long "devel/sage/sage/rings/extended_rational_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/extended_rational_field.py", line 51:
    sage: loads(dumps(f))
Expected:
    Natural morphism:
      From: Rational Field
      To:   Extended Rational Field
Got:
    Natural endomorphism of Rational Field
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/extended_rational_field.py", line 110:
    sage: E == loads(dumps(E))
Expected:
    True
Got:
    False
**********************************************************************
<SNIP>
```




---

archive/issue_comments_042860.json:
```json
{
    "body": "This has been fixed via the patch at #5520.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T08:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5521#issuecomment-42860",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed via the patch at #5520.

Cheers,

Michael



---

archive/issue_events_005771.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-31T08:45:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5521",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5521#event-5771"
}
```



---

archive/issue_comments_042861.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T08:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5521#issuecomment-42861",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
