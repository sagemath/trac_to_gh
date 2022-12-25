# Issue 9164: cygwin: gap.cputime() does not work

archive/issues_009164.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori @dimpase\n\n```\n\nsage: gap.cputime()\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/home/wstein/sage-4.4.3/<ipython console> in <module>()\n\n/home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in cputime(self, t)\n    429         else:\n    430             self.eval('_r_ := Runtimes();')\n--> 431             r = sum(eval(self.eval('[_r_.user_time, _r_.system_time, _r_.user_time_children, _r_.system_time_children]')))\n    432             return r/1000.0\n    433 \n\n/home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in <module>()\n\nNameError: name 'fail' is not defined\nsage: \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9164\n\n",
    "closed_at": "2013-03-15T13:02:31Z",
    "created_at": "2010-06-07T04:02:22Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: gap.cputime() does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9164",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  jpflori @dimpase

```

sage: gap.cputime()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/wstein/sage-4.4.3/<ipython console> in <module>()

/home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in cputime(self, t)
    429         else:
    430             self.eval('_r_ := Runtimes();')
--> 431             r = sum(eval(self.eval('[_r_.user_time, _r_.system_time, _r_.user_time_children, _r_.system_time_children]')))
    432             return r/1000.0
    433 

/home/wstein/sage-4.4.3/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in <module>()

NameError: name 'fail' is not defined
sage: 
```

Issue created by migration from https://trac.sagemath.org/ticket/9164





---

archive/issue_comments_085420.json:
```json
{
    "body": "Hey, is this related to the mysterious comment\n\n```\nsage: v, t = qsieve(n, time=True)   # uses the sieve    (optional: time doesn't work on cygwin) \n```\nin sage/interfaces/qsieve.py?  And does `time` now work on Cygwin?",
    "created_at": "2013-02-27T03:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85420",
    "user": "https://github.com/kcrisman"
}
```

Hey, is this related to the mysterious comment

```
sage: v, t = qsieve(n, time=True)   # uses the sieve    (optional: time doesn't work on cygwin) 
```
in sage/interfaces/qsieve.py?  And does `time` now work on Cygwin?



---

archive/issue_comments_085421.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-27T21:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85421",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085422.json:
```json
{
    "body": "Dont think so.\n\ngap.cputime() works on both my systems.\nIt is even so nice it reports twice as much on the 32 bits than on the 64 bits...\n\nSo let's close this one.\n\nNonetheless the other qsieve examples do not work, this should be treated elsewhere.",
    "created_at": "2013-02-27T21:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85422",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Dont think so.

gap.cputime() works on both my systems.
It is even so nice it reports twice as much on the 32 bits than on the 64 bits...

So let's close this one.

Nonetheless the other qsieve examples do not work, this should be treated elsewhere.



---

archive/issue_comments_085423.json:
```json
{
    "body": "Replying to [comment:2 jpflori]:\n> Nonetheless the other qsieve examples do not work, this should be treated elsewhere.\n\nOr not:\nhttp://comments.gmane.org/gmane.os.cygwin/106331\nAlthough the time bash builtin works, there is no time command under Cygwin (nor in any package), so either we should modify the qsieve code (what will have to be done anyway after #12173 gets in and we get rid of qsieve which will then be obsoleted), or live with such code being optional.",
    "created_at": "2013-02-27T22:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85423",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Replying to [comment:2 jpflori]:
> Nonetheless the other qsieve examples do not work, this should be treated elsewhere.

Or not:
http://comments.gmane.org/gmane.os.cygwin/106331
Although the time bash builtin works, there is no time command under Cygwin (nor in any package), so either we should modify the qsieve code (what will have to be done anyway after #12173 gets in and we get rid of qsieve which will then be obsoleted), or live with such code being optional.



---

archive/issue_comments_085424.json:
```json
{
    "body": "My bad, I wrongly used cygcheck.\nThere is http://cygwin.com/packages/time/\nSo either we make time a prereq which I would not advocate for, or rather test at runtime if the real time executable is available.\nBut thats for another ticket anyway (unless I get my hand on a Mac, fix #12173 and remove qsieve by that time).",
    "created_at": "2013-02-27T22:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85424",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

My bad, I wrongly used cygcheck.
There is http://cygwin.com/packages/time/
So either we make time a prereq which I would not advocate for, or rather test at runtime if the real time executable is available.
But thats for another ticket anyway (unless I get my hand on a Mac, fix #12173 and remove qsieve by that time).



---

archive/issue_comments_085425.json:
```json
{
    "body": "JP, see #14184.  What do you think?",
    "created_at": "2013-02-27T22:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85425",
    "user": "https://github.com/kcrisman"
}
```

JP, see #14184.  What do you think?



---

archive/issue_comments_085426.json:
```json
{
    "body": "Replying to [comment:3 jpflori]:\n> Although the time bash builtin works, there is no time command under Cygwin (nor in any package)\n\nThis has nothing to do with Cygwin. My Gentoo Linux system doesn't have a `time` command either, it does have the `time` keyword (to be pedantic: it's a keyword, not a builtin) in bash.\n\n> so [...] we should modify the qsieve code\n\nExactly, see #14202.",
    "created_at": "2013-02-28T07:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85426",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:3 jpflori]:
> Although the time bash builtin works, there is no time command under Cygwin (nor in any package)

This has nothing to do with Cygwin. My Gentoo Linux system doesn't have a `time` command either, it does have the `time` keyword (to be pedantic: it's a keyword, not a builtin) in bash.

> so [...] we should modify the qsieve code

Exactly, see #14202.



---

archive/issue_comments_085427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-08T12:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85427",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022547.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2013-03-08T12:43:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9164#event-22547"
}
```



---

archive/issue_comments_085428.json:
```json
{
    "body": "After a rebase, this works!  Awesome.",
    "created_at": "2013-03-08T12:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85428",
    "user": "https://github.com/kcrisman"
}
```

After a rebase, this works!  Awesome.



---

archive/issue_events_022548.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-15T13:02:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9164#event-22548"
}
```



---

archive/issue_comments_085429.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-15T13:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9164#issuecomment-85429",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
