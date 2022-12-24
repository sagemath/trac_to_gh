# Issue 2294: RealDoubleElement _interface_init_ is very poor

archive/issues_002294.json:
```json
{
    "body": "Assignee: was\n\nWe see here that _interface_init_() on RDF loses the last few digits of its value, by truncation.\n\n\n```\nsage: RR(RDF(sin(1)))\n0.841470984807897\nsage: RR(RDF(sin(1))._interface_init_())\n0.841470984808000\n```\n\n\nI should have a patch for this very soon.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2294\n\n",
    "created_at": "2008-02-24T19:18:35Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "RealDoubleElement _interface_init_ is very poor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2294",
    "user": "cwitty"
}
```
Assignee: was

We see here that _interface_init_() on RDF loses the last few digits of its value, by truncation.


```
sage: RR(RDF(sin(1)))
0.841470984807897
sage: RR(RDF(sin(1))._interface_init_())
0.841470984808000
```


I should have a patch for this very soon.


Issue created by migration from https://trac.sagemath.org/ticket/2294





---

archive/issue_comments_015217.json:
```json
{
    "body": "Changing assignee from was to cwitty.",
    "created_at": "2008-02-24T21:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2294#issuecomment-15217",
    "user": "cwitty"
}
```

Changing assignee from was to cwitty.



---

archive/issue_comments_015218.json:
```json
{
    "body": "Attachment [fp-interface-init.patch](tarball://root/attachments/some-uuid/ticket2294/fp-interface-init.patch) by cwitty created at 2008-02-24 21:09:54",
    "created_at": "2008-02-24T21:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2294#issuecomment-15218",
    "user": "cwitty"
}
```

Attachment [fp-interface-init.patch](tarball://root/attachments/some-uuid/ticket2294/fp-interface-init.patch) by cwitty created at 2008-02-24 21:09:54



---

archive/issue_comments_015219.json:
```json
{
    "body": "REFEREE REPORT\n\n\nWow, this is a really important patch to apply ASAP.  \n\nThere is an English typo in a parenthetical remark:\n\n\n```\n \t105\t        computer algebra system.  (This the default function used for\n```\n",
    "created_at": "2008-02-24T21:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2294#issuecomment-15219",
    "user": "was"
}
```

REFEREE REPORT


Wow, this is a really important patch to apply ASAP.  

There is an English typo in a parenthetical remark:


```
 	105	        computer algebra system.  (This the default function used for
```




---

archive/issue_comments_015220.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-24T21:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2294#issuecomment-15220",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015221.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-24T21:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2294#issuecomment-15221",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.alpha0



---

archive/issue_comments_015222.json:
```json
{
    "body": "Attachment [trac_2294_fix_small_grammatical_issues.patch](tarball://root/attachments/some-uuid/ticket2294/trac_2294_fix_small_grammatical_issues.patch) by mabshoff created at 2008-02-24 22:34:49\n\nThe patch corrects some small issue and has already been merged.",
    "created_at": "2008-02-24T22:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2294#issuecomment-15222",
    "user": "mabshoff"
}
```

Attachment [trac_2294_fix_small_grammatical_issues.patch](tarball://root/attachments/some-uuid/ticket2294/trac_2294_fix_small_grammatical_issues.patch) by mabshoff created at 2008-02-24 22:34:49

The patch corrects some small issue and has already been merged.
