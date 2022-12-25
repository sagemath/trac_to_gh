# Issue 6412: [with patch, needs review] Getting Singular's cputime does not work with negative argument

archive/issues_006412.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nCC:  @malb\n\nKeywords: cputime Singular\n\nIn some application, I accidentally had a negative argument `t` to `singular.cputime(t)`. Actually I don't know how this came, but anyway: This lead to a Traceback, since `t` is inserted into a string: 'timer-%d'%t\n\nOf coure, if t has a minus sign, Singular complains.\nEasy solution: Put brackets aroung %d.\n\nWithout the patch:\n\n```\nsage: singular.cputime(-7)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/SimonKing/.sage/temp/sage.math.washington.edu/18981/_home_SimonKing__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in cputime(self, t)\n    677         \"\"\"\n    678         if t:\n--> 679             return float(self.eval('timer-%d'%(int(1000*t))))/1000.0\n    680         else:\n    681             return float(self.eval('timer'))/1000.0\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in eval(self, x, allow_semicolon, strip, **kwds)\n    547\n    548         if s.find(\"error\") != -1 or s.find(\"Segment fault\") != -1:\n--> 549             raise RuntimeError, 'Singular error:\\n%s'%s\n    550\n    551         if get_verbose() > 0:\n\nRuntimeError: Singular error:\n   ? --(`int`) failed\n   ? expected --(`identifier`)\n   ? error occurred in STDIN line 19: `timer--7000;`\n```\n\n\nWith the patch:\n\n```\nsage: singular.cputime(-70)\n70.060000000000002\n```\n\n\nIt will certainly hardly ever occur that people call the cputime with a negative starting point, but why not fix a corner case?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6412\n\n",
    "created_at": "2009-06-25T17:53:48Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] Getting Singular's cputime does not work with negative argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6412",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @simon-king-jena

CC:  @malb

Keywords: cputime Singular

In some application, I accidentally had a negative argument `t` to `singular.cputime(t)`. Actually I don't know how this came, but anyway: This lead to a Traceback, since `t` is inserted into a string: 'timer-%d'%t

Of coure, if t has a minus sign, Singular complains.
Easy solution: Put brackets aroung %d.

Without the patch:

```
sage: singular.cputime(-7)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/18981/_home_SimonKing__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in cputime(self, t)
    677         """
    678         if t:
--> 679             return float(self.eval('timer-%d'%(int(1000*t))))/1000.0
    680         else:
    681             return float(self.eval('timer'))/1000.0

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in eval(self, x, allow_semicolon, strip, **kwds)
    547
    548         if s.find("error") != -1 or s.find("Segment fault") != -1:
--> 549             raise RuntimeError, 'Singular error:\n%s'%s
    550
    551         if get_verbose() > 0:

RuntimeError: Singular error:
   ? --(`int`) failed
   ? expected --(`identifier`)
   ? error occurred in STDIN line 19: `timer--7000;`
```


With the patch:

```
sage: singular.cputime(-70)
70.060000000000002
```


It will certainly hardly ever occur that people call the cputime with a negative starting point, but why not fix a corner case?


Issue created by migration from https://trac.sagemath.org/ticket/6412





---

archive/issue_comments_051394.json:
```json
{
    "body": "Allow negative arguments for singular.cputime()",
    "created_at": "2009-06-25T17:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6412#issuecomment-51394",
    "user": "https://github.com/simon-king-jena"
}
```

Allow negative arguments for singular.cputime()



---

archive/issue_comments_051395.json:
```json
{
    "body": "Attachment [cputime.patch](tarball://root/attachments/some-uuid/ticket6412/cputime.patch) by @malb created at 2009-06-25 17:55:58\n\nLooks good.",
    "created_at": "2009-06-25T17:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6412#issuecomment-51395",
    "user": "https://github.com/malb"
}
```

Attachment [cputime.patch](tarball://root/attachments/some-uuid/ticket6412/cputime.patch) by @malb created at 2009-06-25 17:55:58

Looks good.



---

archive/issue_comments_051396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6412#issuecomment-51396",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed



---

archive/issue_events_015106.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-06-26T17:43:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6412",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6412#event-15106"
}
```
