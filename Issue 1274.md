# Issue 1274: modify singular interface to allow for verbose output

archive/issues_001274.json:
```json
{
    "body": "Assignee: @malb\n\nSimon King:\n Now, another question on the Singular interface:\nIn Singular, doing\n`matrix P,S,IS = invariant_ring(A,1);`\nwould make Singular to additionally print information about the\nprogress of computations (which, in big examples, might be nice to\nhave).\nHowever, when i use the Singular interface, i can not see such\ninformations. Where are they gone?\n\nMartin Albrecht:\nThe information is printed but ignored because pexpect expects\nSingular 'output' and ignores the rest. I am no pexpect expert so I don't\nknow how to fix it. It would very very useful though. Anyone else has any\nidea?\n\nWilliam Stein:\nI think this would be possible to implement, by modifying\ninterfaces/singular.py. It's easiest if we just have it print out\nthe result of all the verbose output, rather than all of it along the way as it is\noutput by singular, though the latter would also be possible.   With pseudo-tty's it is\npossible to do anything you could really imagine doing by hand while physically using\na terminal to interact with singular.  Anything.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1274\n\n",
    "created_at": "2007-11-25T22:21:04Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "modify singular interface to allow for verbose output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1274",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @malb

Simon King:
 Now, another question on the Singular interface:
In Singular, doing
`matrix P,S,IS = invariant_ring(A,1);`
would make Singular to additionally print information about the
progress of computations (which, in big examples, might be nice to
have).
However, when i use the Singular interface, i can not see such
informations. Where are they gone?

Martin Albrecht:
The information is printed but ignored because pexpect expects
Singular 'output' and ignores the rest. I am no pexpect expert so I don't
know how to fix it. It would very very useful though. Anyone else has any
idea?

William Stein:
I think this would be possible to implement, by modifying
interfaces/singular.py. It's easiest if we just have it print out
the result of all the verbose output, rather than all of it along the way as it is
output by singular, though the latter would also be possible.   With pseudo-tty's it is
possible to do anything you could really imagine doing by hand while physically using
a terminal to interact with singular.  Anything.

Issue created by migration from https://trac.sagemath.org/ticket/1274





---

archive/issue_comments_007953.json:
```json
{
    "body": "Attachment [trac_1274.patch](tarball://root/attachments/some-uuid/ticket1274/trac_1274.patch) by @malb created at 2008-01-18 18:21:36",
    "created_at": "2008-01-18T18:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1274#issuecomment-7953",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1274.patch](tarball://root/attachments/some-uuid/ticket1274/trac_1274.patch) by @malb created at 2008-01-18 18:21:36



---

archive/issue_comments_007954.json:
```json
{
    "body": "This works now:\n\n\n```\nsage: r = singular.ring(0,'(x,y,z)','dp')\nsage: i = singular.ideal(['x^2','y^2','z^2'])\nsage: s = i.std()\nsage: singular.eval('hilb(%s)'%(s.name()))\n'// 1 t^0\\n// -3 t^2\\n// 3 t^4\\n// -1 t^6\\n\\n// 1 t^0\\n//\n3 t^1\\n// 3 t^2\\n// 1 t^3\\n// dimension (affine) = 0\\n//\ndegree (affine) = 8'\n\nsage: set_verbose(1)\nsage: singular.eval('hilb(%s)'%(s.name()))\n//         1 t^0\n//        -3 t^2\n//         3 t^4\n//        -1 t^6\n//         1 t^0\n//         3 t^1\n//         3 t^2\n//         1 t^3\n// dimension (affine) = 0\n// degree (affine)  = 8\n''\n\nsage: o = s.hilb()\n//         1 t^0\n//        -3 t^2\n//         3 t^4\n//        -1 t^6\n//         1 t^0\n//         3 t^1\n//         3 t^2\n//         1 t^3\n// dimension (affine) = 0\n// degree (affine)  = 8\n// ** right side is not a datum, assignment ignored\n\nsage: set_verbose(0)\nsage: o = s.hilb()\n```\n",
    "created_at": "2008-01-18T18:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1274#issuecomment-7954",
    "user": "https://github.com/malb"
}
```

This works now:


```
sage: r = singular.ring(0,'(x,y,z)','dp')
sage: i = singular.ideal(['x^2','y^2','z^2'])
sage: s = i.std()
sage: singular.eval('hilb(%s)'%(s.name()))
'// 1 t^0\n// -3 t^2\n// 3 t^4\n// -1 t^6\n\n// 1 t^0\n//
3 t^1\n// 3 t^2\n// 1 t^3\n// dimension (affine) = 0\n//
degree (affine) = 8'

sage: set_verbose(1)
sage: singular.eval('hilb(%s)'%(s.name()))
//         1 t^0
//        -3 t^2
//         3 t^4
//        -1 t^6
//         1 t^0
//         3 t^1
//         3 t^2
//         1 t^3
// dimension (affine) = 0
// degree (affine)  = 8
''

sage: o = s.hilb()
//         1 t^0
//        -3 t^2
//         3 t^4
//        -1 t^6
//         1 t^0
//         3 t^1
//         3 t^2
//         1 t^3
// dimension (affine) = 0
// degree (affine)  = 8
// ** right side is not a datum, assignment ignored

sage: set_verbose(0)
sage: o = s.hilb()
```




---

archive/issue_comments_007955.json:
```json
{
    "body": "Looks fine to me, should be applied.",
    "created_at": "2008-01-20T06:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1274#issuecomment-7955",
    "user": "https://github.com/ncalexan"
}
```

Looks fine to me, should be applied.



---

archive/issue_comments_007956.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T05:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1274#issuecomment-7956",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_events_001418.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-21T05:36:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1274",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1274#event-1418"
}
```



---

archive/issue_comments_007957.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1274#issuecomment-7957",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
