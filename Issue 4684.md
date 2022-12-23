# Issue 4684: should be easier to change how many threads used for "make ptest" and friends

archive/issues_004684.json:
```json
{
    "body": "Assignee: mabshoff\n\nI just ran a `make ptest` and was surprised to see my 4-core machine overwhelmed. Of course, that's because the makefile in $SAGE_ROOT defaults to \"`-tp 12`\" for all the parallel testing.\n\nI added a variable at the top of the makefile so that the, uh, tiny minority of Sage users with fewer than 16 cores can easily edit the makefile so that parallel testing doesn't kill their machines. :)\n\nSince $SAGE_ROOT isn't under version control, I'm just uploading the entire new makefile. The changes are really simple.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4684\n\n",
    "created_at": "2008-12-03T05:53:28Z",
    "labels": [
        "build",
        "major",
        "enhancement"
    ],
    "title": "should be easier to change how many threads used for \"make ptest\" and friends",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4684",
    "user": "ddrake"
}
```
Assignee: mabshoff

I just ran a `make ptest` and was surprised to see my 4-core machine overwhelmed. Of course, that's because the makefile in $SAGE_ROOT defaults to "`-tp 12`" for all the parallel testing.

I added a variable at the top of the makefile so that the, uh, tiny minority of Sage users with fewer than 16 cores can easily edit the makefile so that parallel testing doesn't kill their machines. :)

Since $SAGE_ROOT isn't under version control, I'm just uploading the entire new makefile. The changes are really simple.

Issue created by migration from https://trac.sagemath.org/ticket/4684





---

archive/issue_comments_035306.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-03T05:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35306",
    "user": "ddrake"
}
```

Attachment



---

archive/issue_comments_035307.json:
```json
{
    "body": "Hi,\n\nplease post a diff to the original version of the makefile.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T05:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35307",
    "user": "mabshoff"
}
```

Hi,

please post a diff to the original version of the makefile.

Cheers,

Michael



---

archive/issue_comments_035308.json:
```json
{
    "body": "Attachment\n\nLooks good to me. I posted a diff between the current and the patched version for the record.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T06:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35308",
    "user": "mabshoff"
}
```

Attachment

Looks good to me. I posted a diff between the current and the patched version for the record.

Cheers,

Michael



---

archive/issue_comments_035309.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-03T06:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35309",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035310.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-03T06:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35310",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_comments_035311.json:
```json
{
    "body": "Hi,\n\nThis is already closed, but I want to comment that I would vastly prefer if \"make ptest\" were to by default just parse the MAKE environment variable, and if it is \"make -j6\", say, then use 6 threads.  This is what \"sage -t\" does now.   This way, I just set MAKE in my .bash_profile, and everything works right.",
    "created_at": "2008-12-04T20:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35311",
    "user": "was"
}
```

Hi,

This is already closed, but I want to comment that I would vastly prefer if "make ptest" were to by default just parse the MAKE environment variable, and if it is "make -j6", say, then use 6 threads.  This is what "sage -t" does now.   This way, I just set MAKE in my .bash_profile, and everything works right.



---

archive/issue_comments_035312.json:
```json
{
    "body": "I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T23:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35312",
    "user": "mabshoff"
}
```

I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.

Cheers,

Michael



---

archive/issue_comments_035313.json:
```json
{
    "body": "Oops, I was busy opening #4699 while mabshoff was commenting!",
    "created_at": "2008-12-04T23:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4684#issuecomment-35313",
    "user": "ddrake"
}
```

Oops, I was busy opening #4699 while mabshoff was commenting!
