# Issue 9662: gp(string) always returns a value, even when it should not

archive/issues_009662.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen executing a GP command using the Sage interface, a value of 0 is returned when None would be expected.  For example, in a gp shell (started with sage -gp for example):\n\n```\ngp> kill(x)   /* No output */\n```\n\nBut in Sage:\n\n```\nsage: gp('kill(x)')\n0\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9662\n\n",
    "created_at": "2010-08-01T17:37:29Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gp(string) always returns a value, even when it should not",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9662",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @williamstein

When executing a GP command using the Sage interface, a value of 0 is returned when None would be expected.  For example, in a gp shell (started with sage -gp for example):

```
gp> kill(x)   /* No output */
```

But in Sage:

```
sage: gp('kill(x)')
0
```

Issue created by migration from https://trac.sagemath.org/ticket/9662





---

archive/issue_comments_093624.json:
```json
{
    "body": "This is not easily fixed, it is due to the way how Expect assigns variables.  In fact, one could argue that the observed behaviour is as expected, because in gp, we get\n\n```\ngp> a = kill(x)\n0\n```\nSo, assigning a nil value makes it into a zero.",
    "created_at": "2010-08-01T17:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9662#issuecomment-93624",
    "user": "https://github.com/jdemeyer"
}
```

This is not easily fixed, it is due to the way how Expect assigns variables.  In fact, one could argue that the observed behaviour is as expected, because in gp, we get

```
gp> a = kill(x)
0
```
So, assigning a nil value makes it into a zero.



---

archive/issue_comments_093625.json:
```json
{
    "body": "Changing keywords from \"\" to \"pari\".",
    "created_at": "2010-08-03T07:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9662#issuecomment-93625",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "" to "pari".



---

archive/issue_comments_093626.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-24T12:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9662#issuecomment-93626",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_093627.json:
```json
{
    "body": "I agree that this is invalid.  Doing `gp('kill(x)')` means to create an object \"kill(x)\" in gp, assign it to a variable, and return a object pointing to that variable.\n\n```\nsage: type(gp('kill(x)'))\n<class 'sage.interfaces.gp.GpElement'>\n```\n\nThis is how it works for all the interfaces.  If you just want to evaluate a command, then you can do\n\n```\nsage: gp.eval('kill(x)')\n''\n```\n\nwhich appropriately returns an empty string.",
    "created_at": "2013-07-24T12:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9662#issuecomment-93627",
    "user": "https://github.com/mwhansen"
}
```

I agree that this is invalid.  Doing `gp('kill(x)')` means to create an object "kill(x)" in gp, assign it to a variable, and return a object pointing to that variable.

```
sage: type(gp('kill(x)'))
<class 'sage.interfaces.gp.GpElement'>
```

This is how it works for all the interfaces.  If you just want to evaluate a command, then you can do

```
sage: gp.eval('kill(x)')
''
```

which appropriately returns an empty string.



---

archive/issue_events_024101.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-24T12:23:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9662",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9662#event-24101"
}
```



---

archive/issue_events_024102.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-24T12:23:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9662",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9662#event-24102"
}
```
