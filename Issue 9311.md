# Issue 9311: Add an spkg-check file for ratpoints

archive/issues_009311.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @jhpalmieri @peterjeremy\n\nRatpoints is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to \"yes\", no self-tests of ratpoints will be run. This is silly, as there is a small test suite. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/9311\n\n",
    "created_at": "2010-06-22T15:25:09Z",
    "labels": [
        "component: spkg-check",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add an spkg-check file for ratpoints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9311",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @nexttime @jhpalmieri @peterjeremy

Ratpoints is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of ratpoints will be run. This is silly, as there is a small test suite. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/9311





---

archive/issue_events_022945.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-06-22T15:25:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22945"
}
```



---

archive/issue_comments_087555.json:
```json
{
    "body": "This is not quite as simple as one would like on Solaris, as the test suite makes use of a non-POSIX '-u' option to diff\n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/diff.html\n\nso generates this as an output:\n\n\n```\nSuccessfully installed ratpoints-2.1.3.p2\nRunning the test suite.\nTesting a 64-bit version of ratpoints\ngcc rptest.c -o rptest -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME= -DUSE_SSE -L/export/home/drkirkby/sage-4.4.4.alpha1/local/lib -lgmp -lm -L. -lratpoints -m64 \ntime ./rptest > rptest.out\n\nreal\t0m0.05s\nuser\t0m0.00s\nsys\t0m0.00s\ndiff -q testbase rptest.out\ndiff: illegal option -- q\nusage: diff [-bitw] [-c | -e | -f | -h | -n | -u] file1 file2\n       diff [-bitw] [-C number | -U number] file1 file2\n       diff [-bitw] [-D string] file1 file2\n       diff [-bitw] [-c | -e | -f | -h | -n | -u] [-l] [-r] [-s] [-S name] directory1 directory2\nmake: *** [test] Error 2\nAn error occurred while testing ratpoints\n```\n",
    "created_at": "2010-06-22T15:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9311#issuecomment-87555",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This is not quite as simple as one would like on Solaris, as the test suite makes use of a non-POSIX '-u' option to diff

http://www.opengroup.org/onlinepubs/009695399/utilities/diff.html

so generates this as an output:


```
Successfully installed ratpoints-2.1.3.p2
Running the test suite.
Testing a 64-bit version of ratpoints
gcc rptest.c -o rptest -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME= -DUSE_SSE -L/export/home/drkirkby/sage-4.4.4.alpha1/local/lib -lgmp -lm -L. -lratpoints -m64 
time ./rptest > rptest.out

real	0m0.05s
user	0m0.00s
sys	0m0.00s
diff -q testbase rptest.out
diff: illegal option -- q
usage: diff [-bitw] [-c | -e | -f | -h | -n | -u] file1 file2
       diff [-bitw] [-C number | -U number] file1 file2
       diff [-bitw] [-D string] file1 file2
       diff [-bitw] [-c | -e | -f | -h | -n | -u] [-l] [-r] [-s] [-S name] directory1 directory2
make: *** [test] Error 2
An error occurred while testing ratpoints
```




---

archive/issue_comments_087556.json:
```json
{
    "body": "Sorry, the illegal option is '-q', not '-u' as stated.",
    "created_at": "2010-06-22T15:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9311#issuecomment-87556",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Sorry, the illegal option is '-q', not '-u' as stated.



---

archive/issue_comments_087557.json:
```json
{
    "body": "I emailed this bug report to the developer. I think using 'cmp' rather than 'diff -q' would work fine. Will test it for sure. \n\nDave",
    "created_at": "2010-06-24T10:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9311#issuecomment-87557",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I emailed this bug report to the developer. I think using 'cmp' rather than 'diff -q' would work fine. Will test it for sure. 

Dave



---

archive/issue_events_022946.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22946"
}
```



---

archive/issue_events_022947.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22947"
}
```



---

archive/issue_events_022948.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22948"
}
```



---

archive/issue_events_022949.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22949"
}
```



---

archive/issue_events_022950.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22950"
}
```



---

archive/issue_events_022951.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22951"
}
```



---

archive/issue_events_022952.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22952"
}
```



---

archive/issue_events_022953.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9311",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9311#event-22953"
}
```
