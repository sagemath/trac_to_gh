# Issue 599: sage -valgrind log file is placed in bad location.

archive/issues_000599.json:
```json
{
    "body": "Assignee: malb or mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/599\n\n",
    "created_at": "2007-09-06T17:25:55Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "sage -valgrind log file is placed in bad location.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/599",
    "user": "was"
}
```
Assignee: malb or mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/599





---

archive/issue_comments_003096.json:
```json
{
    "body": "change location of valgrind output",
    "created_at": "2007-09-06T17:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/599#issuecomment-3096",
    "user": "burcin"
}
```

change location of valgrind output



---

archive/issue_comments_003097.json:
```json
{
    "body": "Attachment [sage-valgrind_output_place.patch](tarball://root/attachments/some-uuid/ticket599/sage-valgrind_output_place.patch) by burcin created at 2007-09-06 17:36:02\n\nOn IRC it was suggested the place should be $HOME/.sage/sage-memcheck.$PID\n\nSep 06 19:25:58 <malb>  I vote for $HOME/.sage/sage-memcheck.PID\nSep 06 19:26:23 <wstein>        #599: +1",
    "created_at": "2007-09-06T17:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/599#issuecomment-3097",
    "user": "burcin"
}
```

Attachment [sage-valgrind_output_place.patch](tarball://root/attachments/some-uuid/ticket599/sage-valgrind_output_place.patch) by burcin created at 2007-09-06 17:36:02

On IRC it was suggested the place should be $HOME/.sage/sage-memcheck.$PID

Sep 06 19:25:58 <malb>  I vote for $HOME/.sage/sage-memcheck.PID
Sep 06 19:26:23 <wstein>        #599: +1



---

archive/issue_comments_003098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T18:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/599#issuecomment-3098",
    "user": "mabshoff"
}
```

Resolution: fixed
