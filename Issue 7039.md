# Issue 7039: zn_poly-0.9 uses gcc, irrespective of setting of CC

archive/issues_007039.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.net\n\nKeywords: GNUism\n\nSome time ago I sorted out the fact that znpoly failed to build if the linker used was the Sun linker, as znpoly used GNU specific flags. \n\nWell it seems there was another defect too, as the setting of CC is ignored too. \n\n\n```\nzn_poly-0.9.p1/src/src/ks_support.c\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/zn_poly-0.9.p1/src'\ngcc -fPIC -O3 -L. -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7039\n\n",
    "created_at": "2009-09-27T16:01:04Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "zn_poly-0.9 uses gcc, irrespective of setting of CC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7039",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.net

Keywords: GNUism

Some time ago I sorted out the fact that znpoly failed to build if the linker used was the Sun linker, as znpoly used GNU specific flags. 

Well it seems there was another defect too, as the setting of CC is ignored too. 


```
zn_poly-0.9.p1/src/src/ks_support.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c

```


Issue created by migration from https://trac.sagemath.org/ticket/7039





---

archive/issue_comments_058165.json:
```json
{
    "body": "At ticket #12433, I ask about writing an autotools build system for zn_poly and push it upstream. Wouldn't that fix that report too?",
    "created_at": "2012-06-16T20:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58165",
    "user": "https://trac.sagemath.org/admin/accounts/users/Snark"
}
```

At ticket #12433, I ask about writing an autotools build system for zn_poly and push it upstream. Wouldn't that fix that report too?



---

archive/issue_comments_058166.json:
```json
{
    "body": "Changing component from build to packages: standard.",
    "created_at": "2015-09-08T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58166",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to packages: standard.



---

archive/issue_comments_058167.json:
```json
{
    "body": "Duplicate of #12433.",
    "created_at": "2015-09-08T13:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58167",
    "user": "https://github.com/jdemeyer"
}
```

Duplicate of #12433.



---

archive/issue_comments_058168.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-08T13:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58168",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058169.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-08T13:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58169",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007260.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-09-12T13:58:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7039#event-7260"
}
```



---

archive/issue_comments_058170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T13:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58170",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_058171.json:
```json
{
    "body": "Should this not be \"wont fix\"? \n\nThis almost automatic setting \n\nnew -> needs_review\nneed_review to positive review\npositive_review to closed. \n\nis in my opinion a bad thing.",
    "created_at": "2015-09-12T15:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58171",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Should this not be "wont fix"? 

This almost automatic setting 

new -> needs_review
need_review to positive review
positive_review to closed. 

is in my opinion a bad thing.



---

archive/issue_comments_058172.json:
```json
{
    "body": "It looks like it is \"won't fix\": look at the ticket's \"milestone\".",
    "created_at": "2015-09-12T15:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7039#issuecomment-58172",
    "user": "https://github.com/jhpalmieri"
}
```

It looks like it is "won't fix": look at the ticket's "milestone".
