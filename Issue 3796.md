# Issue 3796: Do something about empty directories for pexpect interfaces

archive/issues_003796.json:
```json
{
    "body": "Assignee: mabshoff\n\nI almost forgot to open a ticket on this one.  I'm not sure what solution we should use, but here's the discussion from sage-devel:\n\ntabbott:\n>> - The sage expect wrapper script (sage/interfaces/expect.py) works if its\n>> __path field (normally SAGE_ROOT/data/extcode/genus2reduction or whatever)\n>> is a directory that it can't write to, but if the (empty) directory is\n>> deleted, it breaks.  I'm not sure what gets put in these directories --\n>> there's a function user_dir that outputs that location, but it doesn't\n>> seem to be called.  Anyway, either these directories are useless and\n>> shouldn't exist, or there should be a way to relocate them to ~/.sage for\n>> users who don't have write access to their sage installation (I have a\n>> feeling I may regret not having fixed this yet).\nmabshoff:\n> It sounds like a sensible idea to do so. The reason those directories\n> exist is that when we send a large amount of data to a pexpect\n> interface we write the input to a temp file and then use the program  \n> to read the input from disk. This is a hackish solution, but is cause\n> be pexpect using quadratic time copying buffers. That issue should\n> obviously be fixed.\nwstein:\nThat's not right.  We use a user-writable temp directory for data interchange\nwith subprocesses.  Those directories were part of the early design   \nof the pexpect interface, when I imagined individual users putting code\nin there that would get loaded.  The interfaces can and should be redesigned\nto not use/require those interfaces.  Sorry this is vague.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3796\n\n",
    "created_at": "2008-08-09T18:27:40Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Do something about empty directories for pexpect interfaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3796",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

I almost forgot to open a ticket on this one.  I'm not sure what solution we should use, but here's the discussion from sage-devel:

tabbott:
>> - The sage expect wrapper script (sage/interfaces/expect.py) works if its
>> __path field (normally SAGE_ROOT/data/extcode/genus2reduction or whatever)
>> is a directory that it can't write to, but if the (empty) directory is
>> deleted, it breaks.  I'm not sure what gets put in these directories --
>> there's a function user_dir that outputs that location, but it doesn't
>> seem to be called.  Anyway, either these directories are useless and
>> shouldn't exist, or there should be a way to relocate them to ~/.sage for
>> users who don't have write access to their sage installation (I have a
>> feeling I may regret not having fixed this yet).
mabshoff:
> It sounds like a sensible idea to do so. The reason those directories
> exist is that when we send a large amount of data to a pexpect
> interface we write the input to a temp file and then use the program  
> to read the input from disk. This is a hackish solution, but is cause
> be pexpect using quadratic time copying buffers. That issue should
> obviously be fixed.
wstein:
That's not right.  We use a user-writable temp directory for data interchange
with subprocesses.  Those directories were part of the early design   
of the pexpect interface, when I imagined individual users putting code
in there that would get loaded.  The interfaces can and should be redesigned
to not use/require those interfaces.  Sorry this is vague.


Issue created by migration from https://trac.sagemath.org/ticket/3796





---

archive/issue_events_008717.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8717"
}
```



---

archive/issue_events_008718.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8718"
}
```



---

archive/issue_events_008719.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8719"
}
```



---

archive/issue_events_008720.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8720"
}
```



---

archive/issue_events_008721.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8721"
}
```



---

archive/issue_events_008722.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8722"
}
```



---

archive/issue_events_008723.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8723"
}
```



---

archive/issue_comments_026937.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-11-06T15:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3796#issuecomment-26937",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_008724.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-11-06T15:47:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8724"
}
```



---

archive/issue_events_008725.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-11-06T15:47:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8725"
}
```



---

archive/issue_comments_026938.json:
```json
{
    "body": "Fixed by #17044.",
    "created_at": "2014-11-06T15:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3796#issuecomment-26938",
    "user": "https://github.com/jdemeyer"
}
```

Fixed by #17044.



---

archive/issue_comments_026939.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-06T15:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3796#issuecomment-26939",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008726.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-11-07T16:49:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3796#event-8726"
}
```



---

archive/issue_comments_026940.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-11-07T16:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3796#issuecomment-26940",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
