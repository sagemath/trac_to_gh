# Issue 2110: Cython annotation should be available more easily

archive/issues_002110.json:
```json
{
    "body": "Assignee: @williamstein\n\ncython -a creates an annotated html file that helps with profiling code.  It would be nice if this functionality were available on:\n1. .spyx files\n2. .pyx files in the sage library, more easily.\n\nI propose that there should be a new flag to sage (eg sage -n) that fulfills these goals.\n\nsage -n file.spyx would proprocess file.spyx and then call cython -a then start a web-browser to view the file.\nsage -bn would build sage and call cython -a on the cython files that are being built.\nsage -ban would run sage -ba with cython -a.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2110\n\n",
    "created_at": "2008-02-08T11:37:09Z",
    "labels": [
        "component: user interface"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Cython annotation should be available more easily",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2110",
    "user": "https://github.com/roed314"
}
```
Assignee: @williamstein

cython -a creates an annotated html file that helps with profiling code.  It would be nice if this functionality were available on:
1. .spyx files
2. .pyx files in the sage library, more easily.

I propose that there should be a new flag to sage (eg sage -n) that fulfills these goals.

sage -n file.spyx would proprocess file.spyx and then call cython -a then start a web-browser to view the file.
sage -bn would build sage and call cython -a on the cython files that are being built.
sage -ban would run sage -ba with cython -a.


Issue created by migration from https://trac.sagemath.org/ticket/2110





---

archive/issue_events_005058.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2011-09-19T19:14:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2110",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2110#event-5058"
}
```



---

archive/issue_comments_013730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-19T19:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2110#issuecomment-13730",
    "user": "https://github.com/robertwb"
}
```

Resolution: fixed



---

archive/issue_comments_013731.json:
```json
{
    "body": "As of http://hg.sagemath.org/scripts-main/annotate/b1badfb26e13/sage-cython#1\n\nYou can do \n\n\n```\nsage -cython -a /path/to/file.spyx\n```\n\n\nor \n\n\n```\nsage -cython -a /sage/library/file.pyx\n```\n\n\nor even \n\n\n```\nsage -cython -a -sage /path/to/non/library/file.pyx\n```\n\n\nTo do this.  \n\nAlso, as of Cython 0.15 , existing .html files will automatically get updated even if the -a flag is not used to ensure they stay in sync.",
    "created_at": "2011-09-19T19:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2110#issuecomment-13731",
    "user": "https://github.com/robertwb"
}
```

As of http://hg.sagemath.org/scripts-main/annotate/b1badfb26e13/sage-cython#1

You can do 


```
sage -cython -a /path/to/file.spyx
```


or 


```
sage -cython -a /sage/library/file.pyx
```


or even 


```
sage -cython -a -sage /path/to/non/library/file.pyx
```


To do this.  

Also, as of Cython 0.15 , existing .html files will automatically get updated even if the -a flag is not used to ensure they stay in sync.



---

archive/issue_events_005059.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-04T10:13:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2110",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2110#event-5059"
}
```
