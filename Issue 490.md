# Issue 490: gcc 4.3: fix gmp.h problem with "using std::FILE"

archive/issues_000490.json:
```json
{
    "body": "Assignee: @williamstein\n\nHello,\n\nnot to be surprised by a new gcc version I have started building gcc 4.3 snapshots (20070824 in this particular case) and compile Sage with them. Here is a problem with gmp.h\n\nGivaro's gmp test fails:\n\n```\ng++ -I ../../../../local/include/ -L ../../../../local/lib/ -l gmp  gcc-test.cpp -o gcc-test\nIn file included from gcc-test.cpp:1:\n../../../../local/include/gmp.h:515: error: \u2018std::FILE\u2019 has not been declared\n```\nUncommenting \"std::FILE\" fixes the problem.\n\n```\n#if defined (__cplusplus)\nextern \"C\" {\n//using std::FILE;\n#endif\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/490\n\n",
    "created_at": "2007-08-25T23:13:13Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "gcc 4.3: fix gmp.h problem with \"using std::FILE\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/490",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Hello,

not to be surprised by a new gcc version I have started building gcc 4.3 snapshots (20070824 in this particular case) and compile Sage with them. Here is a problem with gmp.h

Givaro's gmp test fails:

```
g++ -I ../../../../local/include/ -L ../../../../local/lib/ -l gmp  gcc-test.cpp -o gcc-test
In file included from gcc-test.cpp:1:
../../../../local/include/gmp.h:515: error: ‘std::FILE’ has not been declared
```
Uncommenting "std::FILE" fixes the problem.

```
#if defined (__cplusplus)
extern "C" {
//using std::FILE;
#endif
```

Issue created by migration from https://trac.sagemath.org/ticket/490





---

archive/issue_comments_002437.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-08-25T23:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2437",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_002438.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-25T23:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002439.json:
```json
{
    "body": "Another suggestion for a fix has been made by Patrick Pelissier:\n\n```\n#if defined (__cplusplus)\nextern \"C\" {\n#ifdef _GMP_H_HAVE_FILE\nusing std::FILE;\n#endif\n#endif\n```\nI am waiting up what the gmp gods will decide an report back",
    "created_at": "2007-08-26T12:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2439",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Another suggestion for a fix has been made by Patrick Pelissier:

```
#if defined (__cplusplus)
extern "C" {
#ifdef _GMP_H_HAVE_FILE
using std::FILE;
#endif
#endif
```
I am waiting up what the gmp gods will decide an report back



---

archive/issue_comments_002440.json:
```json
{
    "body": "This fix (in a modified form has been merged in gcc 4.2.2rc3). So rebasing out spkg against the 4.2.2 release will fix the problem.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-06T14:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2440",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This fix (in a modified form has been merged in gcc 4.2.2rc3). So rebasing out spkg against the 4.2.2 release will fix the problem.

Cheers,

Michael



---

archive/issue_comments_002441.json:
```json
{
    "body": "Once #542 is done this ticket can be closed, because gmp 4.2.2. has solved the issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-12T14:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2441",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Once #542 is done this ticket can be closed, because gmp 4.2.2. has solved the issue.

Cheers,

Michael



---

archive/issue_comments_002442.json:
```json
{
    "body": "Well, I fixed this in some other way via #2929.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T10:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2442",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, I fixed this in some other way via #2929.

Cheers,

Michael



---

archive/issue_comments_002443.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T10:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-15T10:53:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/490#event-1253"
}
```



---

archive/issue_comments_002444.json:
```json
{
    "body": "See #12661 for upgrading the optional GMP spkg to a more recent (5.x) version.",
    "created_at": "2012-07-28T13:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/490#issuecomment-2444",
    "user": "https://github.com/nexttime"
}
```

See #12661 for upgrading the optional GMP spkg to a more recent (5.x) version.
