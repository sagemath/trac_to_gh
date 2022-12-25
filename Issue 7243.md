# Issue 7243: bashisms in extcode-4.1.2/pari/dokchitser/testall

archive/issues_007243.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.net @mwhansen\n\nIn the extcode spkg, pari/dokchitser/testall uses bashisms but has a /bin/sh #! line:\n\n#!/bin/sh\necho \"\\\\r ex-bsw\" | sage -gp\necho \"\\\\r ex-chgen\" | sage -gp\n\nWe should change the #! line to\n\n#!/bin/bash\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7243\n\n",
    "created_at": "2009-10-19T00:09:55Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "bashisms in extcode-4.1.2/pari/dokchitser/testall",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7243",
    "user": "https://github.com/timabbott"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.net @mwhansen

In the extcode spkg, pari/dokchitser/testall uses bashisms but has a /bin/sh #! line:

#!/bin/sh
echo "\\r ex-bsw" | sage -gp
echo "\\r ex-chgen" | sage -gp

We should change the #! line to

#!/bin/bash


Issue created by migration from https://trac.sagemath.org/ticket/7243





---

archive/issue_comments_060022.json:
```json
{
    "body": "Attachment [trac_7243.patch](tarball://root/attachments/some-uuid/ticket7243/trac_7243.patch) by @mwhansen created at 2009-10-19 04:06:57",
    "created_at": "2009-10-19T04:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60022",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7243.patch](tarball://root/attachments/some-uuid/ticket7243/trac_7243.patch) by @mwhansen created at 2009-10-19 04:06:57



---

archive/issue_comments_060023.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-19T04:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60023",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060024.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-03T05:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60024",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060025.json:
```json
{
    "body": "I think the\n\n\n```\n\n#!/usr/bin/env bash\n```\n\n\n(from memory, so might not be right)\n\nis better, as bash is not always installed in /bin\n\n\n```\nbash-2.04$ uname -a\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\nbash-2.04$ ls /bin/bash\n/bin/bash not found\nbash-2.04$ which bash\n/opt/OpenSource/bin/bash\nbash-2.04$ which env\n/usr/bin/env\nbash-2.04$\n```\n",
    "created_at": "2009-12-03T05:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60025",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I think the


```

#!/usr/bin/env bash
```


(from memory, so might not be right)

is better, as bash is not always installed in /bin


```
bash-2.04$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
bash-2.04$ ls /bin/bash
/bin/bash not found
bash-2.04$ which bash
/opt/OpenSource/bin/bash
bash-2.04$ which env
/usr/bin/env
bash-2.04$
```




---

archive/issue_comments_060026.json:
```json
{
    "body": "Yeah, using '#!/usr/bin/env bash' should be correct.",
    "created_at": "2009-12-16T21:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60026",
    "user": "https://github.com/timabbott"
}
```

Yeah, using '#!/usr/bin/env bash' should be correct.



---

archive/issue_comments_060027.json:
```json
{
    "body": "Attachment [trac_7243.patch.v2](tarball://root/attachments/some-uuid/ticket7243/trac_7243.patch.v2) by @timabbott created at 2009-12-17 19:34:25",
    "created_at": "2009-12-17T19:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60027",
    "user": "https://github.com/timabbott"
}
```

Attachment [trac_7243.patch.v2](tarball://root/attachments/some-uuid/ticket7243/trac_7243.patch.v2) by @timabbott created at 2009-12-17 19:34:25



---

archive/issue_comments_060028.json:
```json
{
    "body": "I posted a new patch reflecting that change.",
    "created_at": "2009-12-18T02:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60028",
    "user": "https://github.com/timabbott"
}
```

I posted a new patch reflecting that change.



---

archive/issue_comments_060029.json:
```json
{
    "body": "That looks safe and reliable to me, so I'll set this to 'needs review' then set it to 'positive'. \n\nDave",
    "created_at": "2009-12-18T07:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60029",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That looks safe and reliable to me, so I'll set this to 'needs review' then set it to 'positive'. 

Dave



---

archive/issue_comments_060030.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-18T07:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60030",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060031.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-18T07:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60031",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007462.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-19T23:45:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7243#event-7462"
}
```



---

archive/issue_comments_060032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T23:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7243#issuecomment-60032",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
