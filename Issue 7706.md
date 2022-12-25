# Issue 7706: palp (lattice polytopes): replace the pickle-based database of lattice polytopes by a non-pickle database format

archive/issues_007706.json:
```json
{
    "body": "Assignee: mhampton\n\nThe Sage source distribution must ship with a bare minimum of opaque potentially dangerous binary files.   Pickles (i.e. sobjs) are opaque binary files that can invoke arbitrary code when being unpickled.  Also, sobj's have the drawback that they can someday break, and can be very hard to update and extend later.  They are also hard to scan for virus.     There are currently three places in the Sage source code that includes pickles:  \n* the pickle jar,\n* the database of lattice polytopes\n* the world map graph\n\nFor this ticket, please find a way to replace the lattice polytopes database spkg with something that contains no pickles.  One solution would be to put plain text files in polytopes_db-*.spkg that described the 2d and 3d lattice polytopes. Then make the sobj's only when the spkg is installed.   This would require making the spkg depend on the sage library (which is very reasonable). \n\nAnother possibility would be to change your code so that the first time the lattice polytope table is needed, a plain text file is parsed (so there is never an sobj).  \n\nIssue created by migration from https://trac.sagemath.org/ticket/7706\n\n",
    "created_at": "2009-12-16T08:53:07Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "palp (lattice polytopes): replace the pickle-based database of lattice polytopes by a non-pickle database format",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7706",
    "user": "https://github.com/williamstein"
}
```
Assignee: mhampton

The Sage source distribution must ship with a bare minimum of opaque potentially dangerous binary files.   Pickles (i.e. sobjs) are opaque binary files that can invoke arbitrary code when being unpickled.  Also, sobj's have the drawback that they can someday break, and can be very hard to update and extend later.  They are also hard to scan for virus.     There are currently three places in the Sage source code that includes pickles:  
* the pickle jar,
* the database of lattice polytopes
* the world map graph

For this ticket, please find a way to replace the lattice polytopes database spkg with something that contains no pickles.  One solution would be to put plain text files in polytopes_db-*.spkg that described the 2d and 3d lattice polytopes. Then make the sobj's only when the spkg is installed.   This would require making the spkg depend on the sage library (which is very reasonable). 

Another possibility would be to change your code so that the first time the lattice polytope table is needed, a plain text file is parsed (so there is never an sobj).  

Issue created by migration from https://trac.sagemath.org/ticket/7706





---

archive/issue_comments_066017.json:
```json
{
    "body": "See also #7705.",
    "created_at": "2009-12-16T08:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66017",
    "user": "https://github.com/williamstein"
}
```

See also #7705.



---

archive/issue_comments_066018.json:
```json
{
    "body": "Changing assignee from mhampton to @novoselt.",
    "created_at": "2009-12-16T15:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66018",
    "user": "https://github.com/novoselt"
}
```

Changing assignee from mhampton to @novoselt.



---

archive/issue_comments_066019.json:
```json
{
    "body": "Attachment [trac_7706_change_format_of_reflexive_polytope_databases.patch](tarball://root/attachments/some-uuid/ticket7706/trac_7706_change_format_of_reflexive_polytope_databases.patch) by @novoselt created at 2009-12-17 06:38:57\n\nBased on 4.3.rc0",
    "created_at": "2009-12-17T06:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66019",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_7706_change_format_of_reflexive_polytope_databases.patch](tarball://root/attachments/some-uuid/ticket7706/trac_7706_change_format_of_reflexive_polytope_databases.patch) by @novoselt created at 2009-12-17 06:38:57

Based on 4.3.rc0



---

archive/issue_comments_066020.json:
```json
{
    "body": "Must be placed in DB_HOME/reflexive_polytopes",
    "created_at": "2009-12-17T06:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66020",
    "user": "https://github.com/novoselt"
}
```

Must be placed in DB_HOME/reflexive_polytopes



---

archive/issue_comments_066021.json:
```json
{
    "body": "Attachment [reflexive_polytopes_3d](tarball://root/attachments/some-uuid/ticket7706/reflexive_polytopes_3d) by @novoselt created at 2009-12-17 06:42:26\n\nMust be placed in DB_HOME/reflexive_polytopes",
    "created_at": "2009-12-17T06:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66021",
    "user": "https://github.com/novoselt"
}
```

Attachment [reflexive_polytopes_3d](tarball://root/attachments/some-uuid/ticket7706/reflexive_polytopes_3d) by @novoselt created at 2009-12-17 06:42:26

Must be placed in DB_HOME/reflexive_polytopes



---

archive/issue_comments_066022.json:
```json
{
    "body": "4 sobj files should be removed and replaced with two attached text files.\n\nAfter some thinking and adjusting internal functions it turned out to be possible to reduce computing time for databases from 15 minutes to about 5 seconds (by avoiding extra checks and using initial polytopes in normal form), which is about 10 times longer than it was taking to load pickled files, but still seems quite reasonable to me as a once-per-session computation. It also now has the advantage of cached points (which are dropped during pickling for faster unpickling).\n\nTiming (on sage.math):\n\nBefore (with sobj's):\n\n```\nsage: time len(ReflexivePolytopes(3))\nCPU times: user 0.51 s, sys: 0.02 s, total: 0.53 s\nWall time: 0.54 s\n4319\nsage: time len(ReflexivePolytopes(3))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n4319\n\n```\n\nAfter (with text data files):\n\n```\nsage: time len(ReflexivePolytopes(3))\nCPU times: user 5.04 s, sys: 0.25 s, total: 5.29 s\nWall time: 5.90 s\n4319\nsage: time len(ReflexivePolytopes(3))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n4319\n```",
    "created_at": "2009-12-17T07:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66022",
    "user": "https://github.com/novoselt"
}
```

4 sobj files should be removed and replaced with two attached text files.

After some thinking and adjusting internal functions it turned out to be possible to reduce computing time for databases from 15 minutes to about 5 seconds (by avoiding extra checks and using initial polytopes in normal form), which is about 10 times longer than it was taking to load pickled files, but still seems quite reasonable to me as a once-per-session computation. It also now has the advantage of cached points (which are dropped during pickling for faster unpickling).

Timing (on sage.math):

Before (with sobj's):

```
sage: time len(ReflexivePolytopes(3))
CPU times: user 0.51 s, sys: 0.02 s, total: 0.53 s
Wall time: 0.54 s
4319
sage: time len(ReflexivePolytopes(3))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4319

```

After (with text data files):

```
sage: time len(ReflexivePolytopes(3))
CPU times: user 5.04 s, sys: 0.25 s, total: 5.29 s
Wall time: 5.90 s
4319
sage: time len(ReflexivePolytopes(3))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4319
```



---

archive/issue_comments_066023.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-17T07:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66023",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066024.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T00:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66024",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066025.json:
```json
{
    "body": "Is there a new `polytopes_db-*.spkg`?",
    "created_at": "2010-02-10T17:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66025",
    "user": "https://github.com/qed777"
}
```

Is there a new `polytopes_db-*.spkg`?



---

archive/issue_comments_066026.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-10T17:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66026",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066027.json:
```json
{
    "body": "Should be used instead of two data files attached earlier",
    "created_at": "2010-02-11T04:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66027",
    "user": "https://github.com/novoselt"
}
```

Should be used instead of two data files attached earlier



---

archive/issue_comments_066028.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-11T04:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66028",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066029.json:
```json
{
    "body": "Attachment [polytopes_db-20100210.spkg](tarball://root/attachments/some-uuid/ticket7706/polytopes_db-20100210.spkg) by @novoselt created at 2010-02-11 04:19:45",
    "created_at": "2010-02-11T04:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66029",
    "user": "https://github.com/novoselt"
}
```

Attachment [polytopes_db-20100210.spkg](tarball://root/attachments/some-uuid/ticket7706/polytopes_db-20100210.spkg) by @novoselt created at 2010-02-11 04:19:45



---

archive/issue_comments_066030.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T13:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66030",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066031.json:
```json
{
    "body": "```\n Please remember to update the relevant ticket fields --- the release\n managers use an automated script to generate lists of merged tickets.\n\n```",
    "created_at": "2010-02-11T13:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66031",
    "user": "https://github.com/qed777"
}
```

```
 Please remember to update the relevant ticket fields --- the release
 managers use an automated script to generate lists of merged tickets.

```



---

archive/issue_comments_066032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7706#issuecomment-66032",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_018405.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T15:04:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7706",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7706#event-18405"
}
```
