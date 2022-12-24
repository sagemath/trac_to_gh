# Issue 6788: 1 doctest timed out in devel/sage/sage/symbolic/assumptions.py

archive/issues_006788.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t  \"devel/sage/sage/symbolic/assumptions.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [360.3 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6788\n\n",
    "created_at": "2009-08-20T22:14:12Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "1 doctest timed out in devel/sage/sage/symbolic/assumptions.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6788",
    "user": "drkirkby"
}
```
Assignee: tbd


```
sage -t  "devel/sage/sage/symbolic/assumptions.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [360.3 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6788





---

archive/issue_comments_055941.json:
```json
{
    "body": "Changing keywords from \"\" to \"maxima\".",
    "created_at": "2009-08-20T23:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55941",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "maxima".



---

archive/issue_comments_055942.json:
```json
{
    "body": "On the various machines I tried (no Solaris though!) I don't get a timeout but rather a doctest failure.  I'm attaching a patch fixing it.  David, is the timeout you get reproducible, or does it only happen sporadically?",
    "created_at": "2009-08-21T01:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55942",
    "user": "AlexGhitza"
}
```

On the various machines I tried (no Solaris though!) I don't get a timeout but rather a doctest failure.  I'm attaching a patch fixing it.  David, is the timeout you get reproducible, or does it only happen sporadically?



---

archive/issue_comments_055943.json:
```json
{
    "body": "Attachment [trac_6788.patch](tarball://root/attachments/some-uuid/ticket6788/trac_6788.patch) by AlexGhitza created at 2009-08-21 01:38:28\n\napply after spkg's at #6564 and #6699",
    "created_at": "2009-08-21T01:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55943",
    "user": "AlexGhitza"
}
```

Attachment [trac_6788.patch](tarball://root/attachments/some-uuid/ticket6788/trac_6788.patch) by AlexGhitza created at 2009-08-21 01:38:28

apply after spkg's at #6564 and #6699



---

archive/issue_comments_055944.json:
```json
{
    "body": "To release manager: Was this fixed elsewhere?",
    "created_at": "2009-09-28T20:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55944",
    "user": "kcrisman"
}
```

To release manager: Was this fixed elsewhere?



---

archive/issue_comments_055945.json:
```json
{
    "body": "This still fails for me, but what is worrying is how the CPU usage keeps climbing after the test failure. \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/f5502f8489cc2b31\n\nThis is nothing to do with this particular test, but this test is an example of which shows that doctest failures are handled badly. \n\nDave",
    "created_at": "2009-10-08T09:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55945",
    "user": "drkirkby"
}
```

This still fails for me, but what is worrying is how the CPU usage keeps climbing after the test failure. 

http://groups.google.com/group/sage-devel/browse_thread/thread/f5502f8489cc2b31

This is nothing to do with this particular test, but this test is an example of which shows that doctest failures are handled badly. 

Dave



---

archive/issue_comments_055946.json:
```json
{
    "body": "Changing component from algebra to packages.",
    "created_at": "2009-10-19T06:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55946",
    "user": "AlexGhitza"
}
```

Changing component from algebra to packages.



---

archive/issue_comments_055947.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-10-19T06:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55947",
    "user": "AlexGhitza"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_055948.json:
```json
{
    "body": "To drkirkby - can you try this with the spkg for 5.20.1 in #7745?",
    "created_at": "2009-12-24T03:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55948",
    "user": "kcrisman"
}
```

To drkirkby - can you try this with the spkg for 5.20.1 in #7745?



---

archive/issue_comments_055949.json:
```json
{
    "body": "Hi, \nsorry for not replying earlier, but I did not see the request. The .spkg for Maxima 5.20.1 does fix this:\n\n\n```\nThis does fix the problem. \n\n\nkirkby@t2:[~/sage-4.3] $ ./sage -t  \"devel/sage/sage/symbolic/assumptions.py\"\nsage -t  \"devel/sage/sage/symbolic/assumptions.py\"          \n         [60.8 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 60.8 seconds\n```\n",
    "created_at": "2009-12-28T21:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55949",
    "user": "drkirkby"
}
```

Hi, 
sorry for not replying earlier, but I did not see the request. The .spkg for Maxima 5.20.1 does fix this:


```
This does fix the problem. 


kirkby@t2:[~/sage-4.3] $ ./sage -t  "devel/sage/sage/symbolic/assumptions.py"
sage -t  "devel/sage/sage/symbolic/assumptions.py"          
         [60.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 60.8 seconds
```




---

archive/issue_comments_055950.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-03-19T23:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6788#issuecomment-55950",
    "user": "mhansen"
}
```

Resolution: invalid
