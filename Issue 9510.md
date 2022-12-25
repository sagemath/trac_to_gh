# Issue 9510: gfan fails to build on skynet machines eno, taurus

archive/issues_009510.json:
```json
{
    "body": "Assignee: tbd\n\nToward the end of the gfan log file, it says\n\n```\nmake[2]: Leaving directory `/home/palmieri/eno/sage-4.5.alpha4/spkg/build/gfan-0.4plus.p1\\\n/src'\nrm: cannot remove `gfan_*': No such file or directory\n./gfan: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.14' not found (required by ./gfan\\\n)\ngfan links not created correctly\n```\nThe full log file is here:\n\n[http://sage.math.washington.edu/home/palmieri/misc/gfan-0.4plus.p1.log](http://sage.math.washington.edu/home/palmieri/misc/gfan-0.4plus.p1.log)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9510\n\n",
    "created_at": "2010-07-15T15:49:25Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gfan fails to build on skynet machines eno, taurus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9510",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

Toward the end of the gfan log file, it says

```
make[2]: Leaving directory `/home/palmieri/eno/sage-4.5.alpha4/spkg/build/gfan-0.4plus.p1\
/src'
rm: cannot remove `gfan_*': No such file or directory
./gfan: /usr/lib64/libstdc++.so.6: version `GLIBCXX_3.4.14' not found (required by ./gfan\
)
gfan links not created correctly
```
The full log file is here:

[http://sage.math.washington.edu/home/palmieri/misc/gfan-0.4plus.p1.log](http://sage.math.washington.edu/home/palmieri/misc/gfan-0.4plus.p1.log)


Issue created by migration from https://trac.sagemath.org/ticket/9510





---

archive/issue_comments_091233.json:
```json
{
    "body": "I've now built this successfully.  I'm pretty sure that the reason is because of a bad  LD_LIBRARY_PATH, as in #8769.  I was building on eno using \"screen\", and when I use screen on eno, it doesn't set LD_LIBRARY_PATH at all.  On taurus, LD_LIBRARY_PATH was misconfigured.  On taurus, for example, if I set it correctly, then gfan (and everything else) builds fine.  If I then set it to the previous wrong value and delete spkg/installed/gfan..., then I get the same error that I reported here.\n\nSo I'm going to close this ticket.",
    "created_at": "2010-07-15T20:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9510#issuecomment-91233",
    "user": "https://github.com/jhpalmieri"
}
```

I've now built this successfully.  I'm pretty sure that the reason is because of a bad  LD_LIBRARY_PATH, as in #8769.  I was building on eno using "screen", and when I use screen on eno, it doesn't set LD_LIBRARY_PATH at all.  On taurus, LD_LIBRARY_PATH was misconfigured.  On taurus, for example, if I set it correctly, then gfan (and everything else) builds fine.  If I then set it to the previous wrong value and delete spkg/installed/gfan..., then I get the same error that I reported here.

So I'm going to close this ticket.



---

archive/issue_events_023603.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-07-15T20:11:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9510",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9510#event-23603"
}
```



---

archive/issue_events_023604.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-07-15T20:11:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9510",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9510#event-23604"
}
```



---

archive/issue_comments_091234.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-07-15T20:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9510#issuecomment-91234",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: worksforme



---

archive/issue_comments_091235.json:
```json
{
    "body": "Changing priority from blocker to trivial.",
    "created_at": "2010-07-15T20:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9510#issuecomment-91235",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from blocker to trivial.
