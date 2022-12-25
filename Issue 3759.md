# Issue 3759: make testlong leaves all kinds of crap in SAGE_ROOT

archive/issues_003759.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nbsd:sage-3.1.alpha0 was$ ls\n0.png                   devel                   sage.png\n1.png                   doc                     sage0.png\n2.png                   docs-0.html             sage1.png\n3.png                   examples                sage2.png\n4.png                   install.log             sage3.png\n5.png                   ipython                 sage4.png\n6.png                   isogeny_graph.png       sage5.png\n7.png                   local                   sage6.png\n8.png                   makefile                search_tree.png\n9.png                   matplotlibrc            simon.db\nCOPYING.txt             sage                    spkg\nHISTORY.txt             sage-README-osx.txt     test.sobj\nREADME.txt              sage-python             testlong.log\na.png                   sage.db                 tmp\ndata                    sage.eps                tmp.sws\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3759\n\n",
    "created_at": "2008-08-02T19:01:19Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "make testlong leaves all kinds of crap in SAGE_ROOT",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3759",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure


```
bsd:sage-3.1.alpha0 was$ ls
0.png                   devel                   sage.png
1.png                   doc                     sage0.png
2.png                   docs-0.html             sage1.png
3.png                   examples                sage2.png
4.png                   install.log             sage3.png
5.png                   ipython                 sage4.png
6.png                   isogeny_graph.png       sage5.png
7.png                   local                   sage6.png
8.png                   makefile                search_tree.png
9.png                   matplotlibrc            simon.db
COPYING.txt             sage                    spkg
HISTORY.txt             sage-README-osx.txt     test.sobj
README.txt              sage-python             testlong.log
a.png                   sage.db                 tmp
data                    sage.eps                tmp.sws
```


Issue created by migration from https://trac.sagemath.org/ticket/3759





---

archive/issue_comments_026641.json:
```json
{
    "body": "This should remove one of the files...",
    "created_at": "2008-08-13T07:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26641",
    "user": "https://github.com/rlmill"
}
```

This should remove one of the files...



---

archive/issue_comments_026642.json:
```json
{
    "body": "Attachment [trac_3759-no_more_isogeny_graph.png.patch](tarball://root/attachments/some-uuid/ticket3759/trac_3759-no_more_isogeny_graph.png.patch) by @rlmill created at 2008-08-13 07:59:52",
    "created_at": "2008-08-13T07:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26642",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_3759-no_more_isogeny_graph.png.patch](tarball://root/attachments/some-uuid/ticket3759/trac_3759-no_more_isogeny_graph.png.patch) by @rlmill created at 2008-08-13 07:59:52



---

archive/issue_comments_026643.json:
```json
{
    "body": "Attachment [trac_3759-no_more_a.png.patch](tarball://root/attachments/some-uuid/ticket3759/trac_3759-no_more_a.png.patch) by @rlmill created at 2008-08-13 08:32:39",
    "created_at": "2008-08-13T08:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26643",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_3759-no_more_a.png.patch](tarball://root/attachments/some-uuid/ticket3759/trac_3759-no_more_a.png.patch) by @rlmill created at 2008-08-13 08:32:39



---

archive/issue_comments_026644.json:
```json
{
    "body": "Attachment [trac_3759-no_more_sage.eps.patch](tarball://root/attachments/some-uuid/ticket3759/trac_3759-no_more_sage.eps.patch) by @rlmill created at 2008-08-13 08:32:56",
    "created_at": "2008-08-13T08:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26644",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_3759-no_more_sage.eps.patch](tarball://root/attachments/some-uuid/ticket3759/trac_3759-no_more_sage.eps.patch) by @rlmill created at 2008-08-13 08:32:56



---

archive/issue_comments_026645.json:
```json
{
    "body": "0.png through 9.png and all the .db files are generated by graph_database.py, which Emily is working on right now.",
    "created_at": "2008-08-13T08:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26645",
    "user": "https://github.com/rlmill"
}
```

0.png through 9.png and all the .db files are generated by graph_database.py, which Emily is working on right now.



---

archive/issue_comments_026646.json:
```json
{
    "body": "This just leaves `sage.png`, `sage0.png`, `sage1.png`, `sage2.png`, `sage3.png`, `sage4.png`, `sage5.png` and `sage6.png`.",
    "created_at": "2008-08-13T08:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26646",
    "user": "https://github.com/rlmill"
}
```

This just leaves `sage.png`, `sage0.png`, `sage1.png`, `sage2.png`, `sage3.png`, `sage4.png`, `sage5.png` and `sage6.png`.



---

archive/issue_comments_026647.json:
```json
{
    "body": "This does not completely resolve issue.  We need to open a new ticket.   See #3871",
    "created_at": "2008-08-15T10:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26647",
    "user": "https://github.com/williamstein"
}
```

This does not completely resolve issue.  We need to open a new ticket.   See #3871



---

archive/issue_comments_026648.json:
```json
{
    "body": "Merged all four patches in Sage 3.1.rc0",
    "created_at": "2008-08-15T10:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26648",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all four patches in Sage 3.1.rc0



---

archive/issue_comments_026649.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T10:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3759#issuecomment-26649",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003981.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-15T10:10:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3759",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3759#event-3981"
}
```
