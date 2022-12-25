# Issue 6228: Wrong multiplicities when solving a univariate polynomial equation

archive/issues_006228.json:
```json
{
    "body": "Keywords: multiplicities solve\n\nAt http://groups.google.com/group/sage-support/browse_thread/thread/d8e22deb18d97253 Michael Friedman asked how to get the multiplicities when solving a set of nonlinear equations. \n\nIt turns out that actually even the multiplicities for a single and rather simple equation are wrong:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: z = var('z')\nsage: solve((z^3-1)^3,z,multiplicities=True)\n([z == (sqrt(3)*I - 1)/2, z == (-sqrt(3)*I - 1)/2, z == 1], [1, 1, 3])\n```\n\n| Sage Version 4.0, Release Date: 2009-05-29                         |\n| Type notebook() for the GUI, and license() for information.        |\nI am afraid that symbolics isn't my field of expertise. So, I don't know how to cure it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6228\n\n",
    "created_at": "2009-06-05T19:17:33Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Wrong multiplicities when solving a univariate polynomial equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6228",
    "user": "https://github.com/simon-king-jena"
}
```
Keywords: multiplicities solve

At http://groups.google.com/group/sage-support/browse_thread/thread/d8e22deb18d97253 Michael Friedman asked how to get the multiplicities when solving a set of nonlinear equations. 

It turns out that actually even the multiplicities for a single and rather simple equation are wrong:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: z = var('z')
sage: solve((z^3-1)^3,z,multiplicities=True)
([z == (sqrt(3)*I - 1)/2, z == (-sqrt(3)*I - 1)/2, z == 1], [1, 1, 3])
```

| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
I am afraid that symbolics isn't my field of expertise. So, I don't know how to cure it.

Issue created by migration from https://trac.sagemath.org/ticket/6228





---

archive/issue_comments_049611.json:
```json
{
    "body": "Note that it seems to be a problem in ``maxima``:\n\n```\nsage: maxima.eval('solve((z^3-1)^3,z)')\n'[z=(sqrt(3)*%i-1)/2,z=-(sqrt(3)*%i+1)/2,z=1]'\nsage: maxima.eval('multiplicities')\n'[1,1,3]'\n```\n\n\nSo, I suspect this ticket will get a \"won't fix\"...",
    "created_at": "2009-06-05T19:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6228#issuecomment-49611",
    "user": "https://github.com/simon-king-jena"
}
```

Note that it seems to be a problem in ``maxima``:

```
sage: maxima.eval('solve((z^3-1)^3,z)')
'[z=(sqrt(3)*%i-1)/2,z=-(sqrt(3)*%i+1)/2,z=1]'
sage: maxima.eval('multiplicities')
'[1,1,3]'
```


So, I suspect this ticket will get a "won't fix"...



---

archive/issue_comments_049612.json:
```json
{
    "body": "This is now fixed, presumably in the Maxima upgrade.",
    "created_at": "2009-09-29T14:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6228#issuecomment-49612",
    "user": "https://github.com/kcrisman"
}
```

This is now fixed, presumably in the Maxima upgrade.



---

archive/issue_comments_049613.json:
```json
{
    "body": "Attachment [trac_6228-multiplicity-maxima.patch](tarball://root/attachments/some-uuid/ticket6228/trac_6228-multiplicity-maxima.patch) by @kcrisman created at 2009-09-29 14:49:36\n\nBased on 4.1.2.alpha4",
    "created_at": "2009-09-29T14:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6228#issuecomment-49613",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6228-multiplicity-maxima.patch](tarball://root/attachments/some-uuid/ticket6228/trac_6228-multiplicity-maxima.patch) by @kcrisman created at 2009-09-29 14:49:36

Based on 4.1.2.alpha4



---

archive/issue_comments_049614.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-05T05:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6228#issuecomment-49614",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_014604.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T08:38:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6228",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6228#event-14604"
}
```



---

archive/issue_comments_049615.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T08:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6228#issuecomment-49615",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
