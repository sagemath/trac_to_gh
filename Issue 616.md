# Issue 616: sage -coverage improvements

archive/issues_000616.json:
```json
{
    "body": "Assignee: craigcitro\n\nsage -coverage is currently easy to trick: just add a doctest that doesn't actually test your function. This can also happen by accident: if you copy-paste a function, and then don't look at the docstring, you end up with a function that has fake doctests. (This occurs in various places in the sage source code.) \n\nThis patch makes sage -coverage a little smarter: it looks every time to make sure that the function name occurs in the doctests, and if not, adds the function to a list of \"possibly wrong\" functions that it spits out at the end. If the function begins and ends with __, we don't bother looking for the name in the docstring. Also, if the string 'indirect doctest' occurs anywhere, we don't look. \n\nThis patch also sneaks in a change so that scons is replaced by scons -Q, making it quieter whenever it's called. Time for the first line-item veto in a sage patch? :)\n\nIssue created by migration from https://trac.sagemath.org/ticket/616\n\n",
    "created_at": "2007-09-07T06:23:11Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "title": "sage -coverage improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/616",
    "user": "craigcitro"
}
```
Assignee: craigcitro

sage -coverage is currently easy to trick: just add a doctest that doesn't actually test your function. This can also happen by accident: if you copy-paste a function, and then don't look at the docstring, you end up with a function that has fake doctests. (This occurs in various places in the sage source code.) 

This patch makes sage -coverage a little smarter: it looks every time to make sure that the function name occurs in the doctests, and if not, adds the function to a list of "possibly wrong" functions that it spits out at the end. If the function begins and ends with __, we don't bother looking for the name in the docstring. Also, if the string 'indirect doctest' occurs anywhere, we don't look. 

This patch also sneaks in a change so that scons is replaced by scons -Q, making it quieter whenever it's called. Time for the first line-item veto in a sage patch? :)

Issue created by migration from https://trac.sagemath.org/ticket/616





---

archive/issue_comments_003158.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-07T06:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3158",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_003159.json:
```json
{
    "body": "Yeah, I just got bit by trac formatting. In the above, it says that if the function name begins and ends with a double underscore (such as add, etc).",
    "created_at": "2007-09-07T06:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3159",
    "user": "craigcitro"
}
```

Yeah, I just got bit by trac formatting. In the above, it says that if the function name begins and ends with a double underscore (such as add, etc).



---

archive/issue_comments_003160.json:
```json
{
    "body": "Attachment\n\ntrac_616_pt2.hg makes sage -coverage just a bit smarter.",
    "created_at": "2007-09-07T08:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3160",
    "user": "craigcitro"
}
```

Attachment

trac_616_pt2.hg makes sage -coverage just a bit smarter.



---

archive/issue_comments_003161.json:
```json
{
    "body": "Didn't make it, retagged for 2.9\n\nCheers,\n\nMichael",
    "created_at": "2007-09-07T19:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3161",
    "user": "mabshoff"
}
```

Didn't make it, retagged for 2.9

Cheers,

Michael



---

archive/issue_comments_003162.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-07T22:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3162",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003163.json:
```json
{
    "body": "Actually, I'm adding one more patch, that's a combination of the previous two. I don't know how to remove a file I've added, sadly.",
    "created_at": "2007-10-12T21:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3163",
    "user": "craigcitro"
}
```

Actually, I'm adding one more patch, that's a combination of the previous two. I don't know how to remove a file I've added, sadly.



---

archive/issue_comments_003164.json:
```json
{
    "body": "Attachment\n\nI should have mentioned that in addition, the previous two patches made some modifications to the scons/c_lib stuff that no longer applies, so definitely use sage-coverage.hg. This is a patch against $SAGE_ROOT/local/bin.",
    "created_at": "2007-10-12T21:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3164",
    "user": "craigcitro"
}
```

Attachment

I should have mentioned that in addition, the previous two patches made some modifications to the scons/c_lib stuff that no longer applies, so definitely use sage-coverage.hg. This is a patch against $SAGE_ROOT/local/bin.



---

archive/issue_comments_003165.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T06:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/616#issuecomment-3165",
    "user": "was"
}
```

Resolution: fixed
