# Issue 6156: gap packages don't load anymore on itanium, even with gap-4.4.10.p11 (!)

archive/issues_006156.json:
```json
{
    "body": "Assignee: tbd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6156\n\n",
    "created_at": "2009-05-30T04:06:32Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "gap packages don't load anymore on itanium, even with gap-4.4.10.p11 (!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6156",
    "user": "was"
}
```
Assignee: tbd



Issue created by migration from https://trac.sagemath.org/ticket/6156





---

archive/issue_comments_049117.json:
```json
{
    "body": "mabshoff: \"gcc-4.4.0 is the reason GAP doesn't work on itanium skynet.\"\n\nmabshoff: \"the correct thing to do is to not compile gcc with arch or march settings. I have fixed 95% of #2999-3001 in all spkgs which would all to inject flags like march into each spkg.\"",
    "created_at": "2009-05-30T23:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6156#issuecomment-49117",
    "user": "was"
}
```

mabshoff: "gcc-4.4.0 is the reason GAP doesn't work on itanium skynet."

mabshoff: "the correct thing to do is to not compile gcc with arch or march settings. I have fixed 95% of #2999-3001 in all spkgs which would all to inject flags like march into each spkg."



---

archive/issue_comments_049118.json:
```json
{
    "body": "A fix for this problem is to build GAP with -O0. That's what we'll do.  \n\nI do wonder if gap-4.4.12 would work fine with -O0?\n\nAn spkg is up here, ready for review:   \n\n       http://sage.math.washington.edu/home/wstein/patches/gap-4.4.10.p12.spkg",
    "created_at": "2009-06-03T06:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6156#issuecomment-49118",
    "user": "was"
}
```

A fix for this problem is to build GAP with -O0. That's what we'll do.  

I do wonder if gap-4.4.12 would work fine with -O0?

An spkg is up here, ready for review:   

       http://sage.math.washington.edu/home/wstein/patches/gap-4.4.10.p12.spkg



---

archive/issue_comments_049119.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T05:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6156#issuecomment-49119",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049120.json:
```json
{
    "body": "Looks good to me.\n\nMerged in 4.0.1.rc0.",
    "created_at": "2009-06-04T05:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6156#issuecomment-49120",
    "user": "mhansen"
}
```

Looks good to me.

Merged in 4.0.1.rc0.
