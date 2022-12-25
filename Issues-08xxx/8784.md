# Issue 8784: remove quit_sage() command from all.py top level

archive/issues_008784.json:
```json
{
    "body": "Assignee: @jasongrout\n\nIt is stupid that it is this easy to accidentally destabilize and segfault Sage.    Also, having a function \"quit_sage()\" available at the sage: prompt by default that does not quit sage, is dumb. \n\n```\nwstein@boxen:~/build/sage-4.4$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: quit_sage()\nExiting Sage (CPU time 0m0.04s, Wall time 0m3.16s).\nsage: quit\nExiting Sage (CPU time 0m0.07s, Wall time 0m4.80s).\n/virtual/scratch/wstein/build/sage-4.4/local/bin/sage-sage: line 206: 11559 Segmentation fault      sage-ipython \"$@\" -i\nwstein@boxen:~/build/sage-4.4$            \n```\n| Sage Version 4.4, Release Date: 2010-04-24                         |\n| Type notebook() for the GUI, and license() for information.        |\nThe fix is to rename quit_sage() somehow and change *all* code that calls it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8784\n\n",
    "closed_at": "2022-04-02T10:53:24Z",
    "created_at": "2010-04-27T20:47:41Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.6",
    "title": "remove quit_sage() command from all.py top level",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8784",
    "user": "https://github.com/williamstein"
}
```
Assignee: @jasongrout

It is stupid that it is this easy to accidentally destabilize and segfault Sage.    Also, having a function "quit_sage()" available at the sage: prompt by default that does not quit sage, is dumb. 

```
wstein@boxen:~/build/sage-4.4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: quit_sage()
Exiting Sage (CPU time 0m0.04s, Wall time 0m3.16s).
sage: quit
Exiting Sage (CPU time 0m0.07s, Wall time 0m4.80s).
/virtual/scratch/wstein/build/sage-4.4/local/bin/sage-sage: line 206: 11559 Segmentation fault      sage-ipython "$@" -i
wstein@boxen:~/build/sage-4.4$            
```
| Sage Version 4.4, Release Date: 2010-04-24                         |
| Type notebook() for the GUI, and license() for information.        |
The fix is to rename quit_sage() somehow and change *all* code that calls it. 

Issue created by migration from https://trac.sagemath.org/ticket/8784





---

archive/issue_comments_080290.json:
```json
{
    "body": "Maybe rename it to \"sage_library_cleanup\"?",
    "created_at": "2010-04-28T02:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80290",
    "user": "https://github.com/jasongrout"
}
```

Maybe rename it to "sage_library_cleanup"?



---

archive/issue_events_021409.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21409"
}
```



---

archive/issue_events_021410.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21410"
}
```



---

archive/issue_events_021411.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21411"
}
```



---

archive/issue_events_021412.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21412"
}
```



---

archive/issue_events_021413.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21413"
}
```



---

archive/issue_events_021414.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21414"
}
```



---

archive/issue_events_021415.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21415"
}
```



---

archive/issue_comments_080291.json:
```json
{
    "body": "Now all of the cleanup happens automatically and `quit_sage()` is a no-op:\n\n```\nsage: quit_sage()\n<ipython-input-1-ce1781e96a1f>:1: DeprecationWarning: quit_sage is deprecated and now does nothing; please simply delete it\nSee http://trac.sagemath.org/8784 for details.\n  quit_sage()\nsage:\n```\n\n---\nNew commits:",
    "created_at": "2022-01-25T22:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80291",
    "user": "https://github.com/orlitzky"
}
```

Now all of the cleanup happens automatically and `quit_sage()` is a no-op:

```
sage: quit_sage()
<ipython-input-1-ce1781e96a1f>:1: DeprecationWarning: quit_sage is deprecated and now does nothing; please simply delete it
See http://trac.sagemath.org/8784 for details.
  quit_sage()
sage:
```

---
New commits:



---

archive/issue_comments_080292.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2022-01-25T22:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80292",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_events_021416.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-01-25T22:54:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21416"
}
```



---

archive/issue_events_021417.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-01-25T22:54:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21417"
}
```



---

archive/issue_comments_080293.json:
```json
{
    "body": "Does this mean that `sage-cleaner` may go, too?",
    "created_at": "2022-01-31T13:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80293",
    "user": "https://github.com/dimpase"
}
```

Does this mean that `sage-cleaner` may go, too?



---

archive/issue_comments_080294.json:
```json
{
    "body": "Replying to [comment:8 dimpase]:\n> Does this mean that `sage-cleaner` may go, too?\n\n\nNot yet, although that's another long-term goal of mine. sage-cleaner also cleans up \"temporary\" files, which it wouldn't have to do if we used the OS's built-in tempfile functions instead of our home-grown `SAGE_TMP`. The first and easiest part of that cleanup is #33213.",
    "created_at": "2022-01-31T14:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80294",
    "user": "https://github.com/orlitzky"
}
```

Replying to [comment:8 dimpase]:
> Does this mean that `sage-cleaner` may go, too?


Not yet, although that's another long-term goal of mine. sage-cleaner also cleans up "temporary" files, which it wouldn't have to do if we used the OS's built-in tempfile functions instead of our home-grown `SAGE_TMP`. The first and easiest part of that cleanup is #33213.



---

archive/issue_comments_080295.json:
```json
{
    "body": "Replying to [comment:8 dimpase]:\n> Does this mean that `sage-cleaner` may go, too?\n\n\nOk, I actually did this in #33213, which now depends on this ticket.",
    "created_at": "2022-02-18T00:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80295",
    "user": "https://github.com/orlitzky"
}
```

Replying to [comment:8 dimpase]:
> Does this mean that `sage-cleaner` may go, too?


Ok, I actually did this in #33213, which now depends on this ticket.



---

archive/issue_comments_080296.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-03-11T12:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80296",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080297.json:
```json
{
    "body": "OK, looks and tests good.",
    "created_at": "2022-03-11T12:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80297",
    "user": "https://github.com/dimpase"
}
```

OK, looks and tests good.



---

archive/issue_comments_080298.json:
```json
{
    "body": "perhaps you want to rebase on the latest beta",
    "created_at": "2022-03-11T12:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80298",
    "user": "https://github.com/dimpase"
}
```

perhaps you want to rebase on the latest beta



---

archive/issue_comments_080299.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. This was a forced push. New commits:",
    "created_at": "2022-03-11T13:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80299",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. This was a forced push. New commits:



---

archive/issue_comments_080300.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2022-03-11T13:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80300",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_080301.json:
```json
{
    "body": "oops, overlooked this, sorry. Looks good.",
    "created_at": "2022-03-29T10:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80301",
    "user": "https://github.com/dimpase"
}
```

oops, overlooked this, sorry. Looks good.



---

archive/issue_comments_080302.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-03-29T10:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80302",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021418.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2022-04-02T10:53:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8784#event-21418"
}
```



---

archive/issue_comments_080303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2022-04-02T10:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80303",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_080304.json:
```json
{
    "body": "Follow up in #33706.",
    "created_at": "2022-04-17T19:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80304",
    "user": "https://github.com/mkoeppe"
}
```

Follow up in #33706.



---

archive/issue_comments_080305.json:
```json
{
    "body": "We have a complaint about ipython processes staying alive in a patchbot.\nhttps://groups.google.com/d/msgid/sage-devel/20220717160807.GA13671%40metelu.net\n\nCould it be due to this ticket, perhaps the change for `src/sage/repl/ipython_extension.py`\nwas an overkill?",
    "created_at": "2022-07-17T16:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80305",
    "user": "https://github.com/dimpase"
}
```

We have a complaint about ipython processes staying alive in a patchbot.
https://groups.google.com/d/msgid/sage-devel/20220717160807.GA13671%40metelu.net

Could it be due to this ticket, perhaps the change for `src/sage/repl/ipython_extension.py`
was an overkill?
