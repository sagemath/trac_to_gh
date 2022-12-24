# Issue 3786: [with patch, needs review] Refactor binary code isom code.

archive/issues_003786.json:
```json
{
    "body": "Assignee: rlm\n\nThis is *not* a full replacement of `binary_code`, only the half of it that computes automorphism groups and canonical labels. The other half will be refactored later in the summer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3786\n\n",
    "created_at": "2008-08-07T01:13:10Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] Refactor binary code isom code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3786",
    "user": "rlm"
}
```
Assignee: rlm

This is *not* a full replacement of `binary_code`, only the half of it that computes automorphism groups and canonical labels. The other half will be refactored later in the summer.

Issue created by migration from https://trac.sagemath.org/ticket/3786





---

archive/issue_comments_026918.json:
```json
{
    "body": "Is this based on 3.1.alpha0?\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: coding\nsage: hg_sage.apply(\"/home/wdj/sagefiles/trac3786-linear_binary_codes.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage\" && hg import   \"/home/wdj/sagefiles/trac3786-linear_binary_codes.patch\"\napplying /home/wdj/sagefiles/trac3786-linear_binary_codes.patch\npatching file setup.py\nHunk #1 FAILED at 680\n1 out of 1 hunk FAILED -- saving rejects to file setup.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-08-07T10:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26918",
    "user": "wdj"
}
```

Is this based on 3.1.alpha0?


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: coding
sage: hg_sage.apply("/home/wdj/sagefiles/trac3786-linear_binary_codes.patch")
cd "/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage" && hg import   "/home/wdj/sagefiles/trac3786-linear_binary_codes.patch"
applying /home/wdj/sagefiles/trac3786-linear_binary_codes.patch
patching file setup.py
Hunk #1 FAILED at 680
1 out of 1 hunk FAILED -- saving rejects to file setup.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_026919.json:
```json
{
    "body": "Depends on the patches at #3676.",
    "created_at": "2008-08-07T18:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26919",
    "user": "rlm"
}
```

Depends on the patches at #3676.



---

archive/issue_comments_026920.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-08-09T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26920",
    "user": "rlm"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_026921.json:
```json
{
    "body": "I applied the patches at #3676 and then this patch to sage-3.1.alpha0. They applied cleanly and passes sage -testall on a amd64 hardy heron machine.\n\nThough I think this is a very important contribution, there is a lot of code here and I didn't understand most of it. However, I did notice that some of the key functions (for me anyway) had only fairly trivial examples attached to them. For example, automorphism_group. There were *lots* of good examples in run (which automorphism_group seems to require), so I don't think it is necessary to redo the docstrings but people who type \"sage: B.automorphism_group?\" won't find any interesting examples, though people who type \"sage: B.run?\" will. However, if the real referee makes suggested changes, I don't think it will hurt to add to the docstring of automorphism_group either (a) something like \"See the docstring for run for more examples\" or (b) simply copy some of the examples from run (or make some simply modifications) into the docstring of automorphism_group.\n\nAs a general question, I'd like to know will this code will make it easier to create a fast matrix_automorphism function?",
    "created_at": "2008-08-10T13:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26921",
    "user": "wdj"
}
```

I applied the patches at #3676 and then this patch to sage-3.1.alpha0. They applied cleanly and passes sage -testall on a amd64 hardy heron machine.

Though I think this is a very important contribution, there is a lot of code here and I didn't understand most of it. However, I did notice that some of the key functions (for me anyway) had only fairly trivial examples attached to them. For example, automorphism_group. There were *lots* of good examples in run (which automorphism_group seems to require), so I don't think it is necessary to redo the docstrings but people who type "sage: B.automorphism_group?" won't find any interesting examples, though people who type "sage: B.run?" will. However, if the real referee makes suggested changes, I don't think it will hurt to add to the docstring of automorphism_group either (a) something like "See the docstring for run for more examples" or (b) simply copy some of the examples from run (or make some simply modifications) into the docstring of automorphism_group.

As a general question, I'd like to know will this code will make it easier to create a fast matrix_automorphism function?



---

archive/issue_comments_026922.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> some of the key functions (for me anyway) had only fairly trivial examples attached to them...\n> people who type \"sage: B.automorphism_group?\" won't find any interesting examples, though people who type \"sage: B.run?\" will.\n\nThis is meant to be a developer-level file, not a user-level file. Much like `binary_code.pyx`, it is supposed to be doing the work behind the scenes, when someone does something like B.permutation_automorphism_group() where B is a normal LinearCode over GF(2). The docstring for B.run() contains a large number of doctests to ensure that the file is working properly, but the idea is that since the objects in this file are never exported, only minimal examples are necessary for each function in order to see the syntax, in order for developers to plug into it.\n\n> As a general question, I'd like to know will this code will make it easier to create a fast matrix_automorphism function? \n\nThe objects and methods of this file bring us about half way from #3676 to having a matrix automorphism group function. They also bring us about half way to linear codes in general, and all of these are on my list, probably for when I get back from SD9, I'm not sure. Expect them soon, however (as well as hypergraphs!).",
    "created_at": "2008-08-10T17:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26922",
    "user": "rlm"
}
```

Replying to [comment:4 wdj]:
> some of the key functions (for me anyway) had only fairly trivial examples attached to them...
> people who type "sage: B.automorphism_group?" won't find any interesting examples, though people who type "sage: B.run?" will.

This is meant to be a developer-level file, not a user-level file. Much like `binary_code.pyx`, it is supposed to be doing the work behind the scenes, when someone does something like B.permutation_automorphism_group() where B is a normal LinearCode over GF(2). The docstring for B.run() contains a large number of doctests to ensure that the file is working properly, but the idea is that since the objects in this file are never exported, only minimal examples are necessary for each function in order to see the syntax, in order for developers to plug into it.

> As a general question, I'd like to know will this code will make it easier to create a fast matrix_automorphism function? 

The objects and methods of this file bring us about half way from #3676 to having a matrix automorphism group function. They also bring us about half way to linear codes in general, and all of these are on my list, probably for when I get back from SD9, I'm not sure. Expect them soon, however (as well as hypergraphs!).



---

archive/issue_comments_026923.json:
```json
{
    "body": "This all looks good to me.\n\nAfter discussion with rlmiller, he is going to address some small documentation concerns concurrently with #3676, mostly to use this as the example for his general framework.\n\nI cannot vouch to the correctness of the code but I'm happy with the documentation, code cleanliness, and testing regimen.\n\nSoon to be applied!",
    "created_at": "2008-08-11T19:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26923",
    "user": "ncalexan"
}
```

This all looks good to me.

After discussion with rlmiller, he is going to address some small documentation concerns concurrently with #3676, mostly to use this as the example for his general framework.

I cannot vouch to the correctness of the code but I'm happy with the documentation, code cleanliness, and testing regimen.

Soon to be applied!



---

archive/issue_comments_026924.json:
```json
{
    "body": "After discussion with rlm, I think this looks good.",
    "created_at": "2008-08-12T02:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26924",
    "user": "ncalexan"
}
```

After discussion with rlm, I think this looks good.



---

archive/issue_comments_026925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-12T06:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26925",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026926.json:
```json
{
    "body": "Attachment [trac_3786-linear_binary_codes.patch](tarball://root/attachments/some-uuid/ticket3786/trac_3786-linear_binary_codes.patch) by mabshoff created at 2008-08-12 06:01:05\n\nMerged in Sage 3.1.alpha2",
    "created_at": "2008-08-12T06:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3786#issuecomment-26926",
    "user": "mabshoff"
}
```

Attachment [trac_3786-linear_binary_codes.patch](tarball://root/attachments/some-uuid/ticket3786/trac_3786-linear_binary_codes.patch) by mabshoff created at 2008-08-12 06:01:05

Merged in Sage 3.1.alpha2
