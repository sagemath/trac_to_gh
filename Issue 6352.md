# Issue 6352: gap_packages upgrade

archive/issues_006352.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  awebb\n\nKeywords: gap\n\nThis is an upgrade optional package for gap-4.4.12, as in #6348.\nThis spkg applies fine to 4.0.2.rc1 and all related failures in sage -testall -optional are fixed in the patch in #6348.\n\nThe command \"newest-version gap\" mentioned in the old spkg-install script is broken. I was unable to locate that script, so I slightly modified the spkg-install so it would compile the binaries correctly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6352\n\n",
    "created_at": "2009-06-17T23:06:26Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "gap_packages upgrade",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6352",
    "user": "wdj"
}
```
Assignee: tbd

CC:  awebb

Keywords: gap

This is an upgrade optional package for gap-4.4.12, as in #6348.
This spkg applies fine to 4.0.2.rc1 and all related failures in sage -testall -optional are fixed in the patch in #6348.

The command "newest-version gap" mentioned in the old spkg-install script is broken. I was unable to locate that script, so I slightly modified the spkg-install so it would compile the binaries correctly.

Issue created by migration from https://trac.sagemath.org/ticket/6352





---

archive/issue_comments_050782.json:
```json
{
    "body": "See http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.12_0.spkg.",
    "created_at": "2009-06-17T23:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50782",
    "user": "wdj"
}
```

See http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.12_0.spkg.



---

archive/issue_comments_050783.json:
```json
{
    "body": "Changing component from algebra to optional packages.",
    "created_at": "2009-06-19T18:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50783",
    "user": "boothby"
}
```

Changing component from algebra to optional packages.



---

archive/issue_comments_050784.json:
```json
{
    "body": "I had troubles with: \n\n\n```\nsage -t -long --optional \"devel/sage/sage/groups/perm_gps/permgroup.py\"\n\n... skip 450 lines of traceback\n\n**********************************************************************\n9 items had failures:\n   1 of   4 in __main__.example_31\n   1 of   4 in __main__.example_32\n   4 of   9 in __main__.example_37\n   2 of   6 in __main__.example_38\n   4 of   7 in __main__.example_39\n   2 of  18 in __main__.example_4\n   1 of   4 in __main__.example_40\n   1 of   9 in __main__.example_5\n   2 of   6 in __main__.example_73\n***Test Failed*** 18 failures.\n\n```\n\n\nThey were from both database_gap and gap_packages. I have database_gap-4.4.10 installed and the spkgs here and from #6348 on Sage 4.1. These might be related although I don't get errors from gap-4.4.12. It probably doesn't make sense to worry about this until #6348 is cleared up. The full log is attached.",
    "created_at": "2009-07-17T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50784",
    "user": "awebb"
}
```

I had troubles with: 


```
sage -t -long --optional "devel/sage/sage/groups/perm_gps/permgroup.py"

... skip 450 lines of traceback

**********************************************************************
9 items had failures:
   1 of   4 in __main__.example_31
   1 of   4 in __main__.example_32
   4 of   9 in __main__.example_37
   2 of   6 in __main__.example_38
   4 of   7 in __main__.example_39
   2 of  18 in __main__.example_4
   1 of   4 in __main__.example_40
   1 of   9 in __main__.example_5
   2 of   6 in __main__.example_73
***Test Failed*** 18 failures.

```


They were from both database_gap and gap_packages. I have database_gap-4.4.10 installed and the spkgs here and from #6348 on Sage 4.1. These might be related although I don't get errors from gap-4.4.12. It probably doesn't make sense to worry about this until #6348 is cleared up. The full log is attached.



---

archive/issue_comments_050785.json:
```json
{
    "body": "Attachment [permgroup.log](tarball://root/attachments/some-uuid/ticket6352/permgroup.log) by wdj created at 2009-07-17 12:35:15\n\nReplying to [comment:4 awebb]:\n> I had troubles with: \n> \n> {{{\n> sage -t -long --optional \"devel/sage/sage/groups/perm_gps/permgroup.py\"\n> \n> ... skip 450 lines of traceback\n> \n> **********************************************************************\n> 9 items had failures:\n>    1 of   4 in __main__.example_31\n>    1 of   4 in __main__.example_32\n>    4 of   9 in __main__.example_37\n>    2 of   6 in __main__.example_38\n>    4 of   7 in __main__.example_39\n>    2 of  18 in __main__.example_4\n>    1 of   4 in __main__.example_40\n>    1 of   9 in __main__.example_5\n>    2 of   6 in __main__.example_73\n> ***Test Failed*** 18 failures.\n> \n> }}}\n> \n> They were from both database_gap and gap_packages. I have database_gap-4.4.10 installed and the spkgs \n> here and from #6348 on Sage 4.1. These might be related although I don't get errors from gap-4.4.12. \n> It probably doesn't make sense to worry about this until #6348 is cleared up. The full log is attached.\n\nAll I can say is that they worked fine for me when I posted them. I agree that it is a waste of time\nto work on this until #6348 is cleared up.",
    "created_at": "2009-07-17T12:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50785",
    "user": "wdj"
}
```

Attachment [permgroup.log](tarball://root/attachments/some-uuid/ticket6352/permgroup.log) by wdj created at 2009-07-17 12:35:15

Replying to [comment:4 awebb]:
> I had troubles with: 
> 
> {{{
> sage -t -long --optional "devel/sage/sage/groups/perm_gps/permgroup.py"
> 
> ... skip 450 lines of traceback
> 
> **********************************************************************
> 9 items had failures:
>    1 of   4 in __main__.example_31
>    1 of   4 in __main__.example_32
>    4 of   9 in __main__.example_37
>    2 of   6 in __main__.example_38
>    4 of   7 in __main__.example_39
>    2 of  18 in __main__.example_4
>    1 of   4 in __main__.example_40
>    1 of   9 in __main__.example_5
>    2 of   6 in __main__.example_73
> ***Test Failed*** 18 failures.
> 
> }}}
> 
> They were from both database_gap and gap_packages. I have database_gap-4.4.10 installed and the spkgs 
> here and from #6348 on Sage 4.1. These might be related although I don't get errors from gap-4.4.12. 
> It probably doesn't make sense to worry about this until #6348 is cleared up. The full log is attached.

All I can say is that they worked fine for me when I posted them. I agree that it is a waste of time
to work on this until #6348 is cleared up.



---

archive/issue_comments_050786.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-14T08:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50786",
    "user": "awebb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050787.json:
```json
{
    "body": "As gap_packages has been updated to 4.4.12 this ticket seems to be no longer needed. I think it can be closed.\n\nAdam",
    "created_at": "2010-07-15T17:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50787",
    "user": "awebb"
}
```

As gap_packages has been updated to 4.4.12 this ticket seems to be no longer needed. I think it can be closed.

Adam



---

archive/issue_comments_050788.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-21T10:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50788",
    "user": "awebb"
}
```

Resolution: duplicate



---

archive/issue_comments_050789.json:
```json
{
    "body": "This was closed in #8229.",
    "created_at": "2010-09-21T10:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6352#issuecomment-50789",
    "user": "awebb"
}
```

This was closed in #8229.
