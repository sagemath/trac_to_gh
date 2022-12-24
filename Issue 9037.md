# Issue 9037: pynac fails to build on 64-bit OpenSolaris x64.

archive/issues_009037.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies\n\nThe spkg-install of 'pynac' has:\n\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n    echo \"64 bit MacIntel\"\n    CXXFLAGS=\"-m64 -O2 -g\"; export CXXFLAGS\n    LDFLAGS=\"-m64\"; export LDFLAGS\nfi\n```\n\n\nso obviously does not attempt to build 64-bit when SAGE64=\"yes\", unless the operating systems is OS X. \n\nThe build actually fails on a 64-bit OpenSolaris system, as pynac tries to link to 64-bit objects, which obviously fails. \n\n\n```\nsage: An error occurred while installing pynac-0.1.12\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9037\n\n",
    "created_at": "2010-05-24T17:04:56Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "pynac fails to build on 64-bit OpenSolaris x64.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9037",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies

The spkg-install of 'pynac' has:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel"
    CXXFLAGS="-m64 -O2 -g"; export CXXFLAGS
    LDFLAGS="-m64"; export LDFLAGS
fi
```


so obviously does not attempt to build 64-bit when SAGE64="yes", unless the operating systems is OS X. 

The build actually fails on a 64-bit OpenSolaris system, as pynac tries to link to 64-bit objects, which obviously fails. 


```
sage: An error occurred while installing pynac-0.1.12
```


Issue created by migration from https://trac.sagemath.org/ticket/9037





---

archive/issue_comments_083660.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83660",
    "user": "drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083661.json:
```json
{
    "body": "This should be coordinated with #8903.  I can make a new spkg for this issue.",
    "created_at": "2010-05-25T19:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83661",
    "user": "@mwhansen"
}
```

This should be coordinated with #8903.  I can make a new spkg for this issue.



---

archive/issue_comments_083662.json:
```json
{
    "body": "There is a new spkg at #8903 which fixes this issue.",
    "created_at": "2010-05-25T22:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83662",
    "user": "@mwhansen"
}
```

There is a new spkg at #8903 which fixes this issue.



---

archive/issue_comments_083663.json:
```json
{
    "body": "#8903 does **not** fix the issue, as it still has:\n\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n    echo \"64 bit MacIntel\"\n    CXXFLAGS=\"-m64 -O2 -g\"; export CXXFLAGS\n    LDFLAGS=\"-m64\"; export LDFLAGS\nfi\n```\n\n\nI'll have to create a new package based on that at #8031. \n\nDave",
    "created_at": "2010-05-30T12:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83663",
    "user": "drkirkby"
}
```

#8903 does **not** fix the issue, as it still has:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel"
    CXXFLAGS="-m64 -O2 -g"; export CXXFLAGS
    LDFLAGS="-m64"; export LDFLAGS
fi
```


I'll have to create a new package based on that at #8031. 

Dave



---

archive/issue_comments_083664.json:
```json
{
    "body": "Oops, I mean I'll have to create a new package based on that at #8903.",
    "created_at": "2010-05-30T12:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83664",
    "user": "drkirkby"
}
```

Oops, I mean I'll have to create a new package based on that at #8903.



---

archive/issue_comments_083665.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T04:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83665",
    "user": "@mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083666.json:
```json
{
    "body": "This change looks good to me and is what is done in lots of other spkgs.",
    "created_at": "2010-06-03T04:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83666",
    "user": "@mwhansen"
}
```

This change looks good to me and is what is done in lots of other spkgs.



---

archive/issue_comments_083667.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T04:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83667",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T15:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9037#issuecomment-83668",
    "user": "@williamstein"
}
```

Resolution: fixed
