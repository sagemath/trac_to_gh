# Issue 5923: Handling of magma and pari input in ModularForms

archive/issues_005923.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe ModularForms command has some slightly counter-intuitive behaviour on some types of input:\n\n\n```\nsage: ModularForms(gp(1),12)\n---------------------------------------------------------------------------\nTypeError     \n\n[much snipped error message]\n\nTypeError: Error executing code in GP/PARI:\nCODE:\n        sage[4]=level(sage[3]);\nGP/PARI ERROR:\n  ***   expected character: ',' instead of: sage[4]=level(sage[3]);\n                                                              ^-----\n```\n\n\nI realize that this is because the first element is supposed to be a group, although a (Sage) integer is allowed.\n\nWould there be any support for having an if statement in the function to catch magma or pari elements and transform them into their Sage equivalents?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5923\n\n",
    "created_at": "2009-04-28T22:41:04Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Handling of magma and pari input in ModularForms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5923",
    "user": "ljpk"
}
```
Assignee: @craigcitro

The ModularForms command has some slightly counter-intuitive behaviour on some types of input:


```
sage: ModularForms(gp(1),12)
---------------------------------------------------------------------------
TypeError     

[much snipped error message]

TypeError: Error executing code in GP/PARI:
CODE:
        sage[4]=level(sage[3]);
GP/PARI ERROR:
  ***   expected character: ',' instead of: sage[4]=level(sage[3]);
                                                              ^-----
```


I realize that this is because the first element is supposed to be a group, although a (Sage) integer is allowed.

Would there be any support for having an if statement in the function to catch magma or pari elements and transform them into their Sage equivalents?

Issue created by migration from https://trac.sagemath.org/ticket/5923





---

archive/issue_comments_046826.json:
```json
{
    "body": "Changing assignee from @craigcitro to @loefflerd.",
    "created_at": "2009-05-01T08:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46826",
    "user": "@loefflerd"
}
```

Changing assignee from @craigcitro to @loefflerd.



---

archive/issue_comments_046827.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-01T08:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46827",
    "user": "@loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046828.json:
```json
{
    "body": "Certainly this is a bug, but a very easy one to fix; I'll fix it lat",
    "created_at": "2009-05-01T08:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46828",
    "user": "@loefflerd"
}
```

Certainly this is a bug, but a very easy one to fix; I'll fix it lat



---

archive/issue_comments_046829.json:
```json
{
    "body": ".. er. \n\nIt turns out that the problem is that if x is a gp object, then \"x.level\" always *exists*: it is a microscopic function wrapper which on being called, executes \"level(x)\" in gp. Which of course doesn't work. Anyway, I've fixed it by rearranging the ModularForms constructor function a bit, and added a doctest to check that it's fixed.",
    "created_at": "2009-05-01T11:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46829",
    "user": "@loefflerd"
}
```

.. er. 

It turns out that the problem is that if x is a gp object, then "x.level" always *exists*: it is a microscopic function wrapper which on being called, executes "level(x)" in gp. Which of course doesn't work. Anyway, I've fixed it by rearranging the ModularForms constructor function a bit, and added a doctest to check that it's fixed.



---

archive/issue_comments_046830.json:
```json
{
    "body": "patch against 3.4.2.rc0",
    "created_at": "2009-05-01T11:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46830",
    "user": "@loefflerd"
}
```

patch against 3.4.2.rc0



---

archive/issue_comments_046831.json:
```json
{
    "body": "Attachment [trac_5923.patch](tarball://root/attachments/some-uuid/ticket5923/trac_5923.patch) by @craigcitro created at 2009-05-07 08:45:22",
    "created_at": "2009-05-07T08:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46831",
    "user": "@craigcitro"
}
```

Attachment [trac_5923.patch](tarball://root/attachments/some-uuid/ticket5923/trac_5923.patch) by @craigcitro created at 2009-05-07 08:45:22



---

archive/issue_comments_046832.json:
```json
{
    "body": "Attachment [trac_5923_pt2.patch](tarball://root/attachments/some-uuid/ticket5923/trac_5923_pt2.patch) by @craigcitro created at 2009-05-07 09:11:32\n\nLooks good -- I added one small patch that just slightly moved things around. (Mostly just removed cases where tests would end up getting run several times, even though this code isn't anywhere near performance-critical.)",
    "created_at": "2009-05-07T09:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46832",
    "user": "@craigcitro"
}
```

Attachment [trac_5923_pt2.patch](tarball://root/attachments/some-uuid/ticket5923/trac_5923_pt2.patch) by @craigcitro created at 2009-05-07 09:11:32

Looks good -- I added one small patch that just slightly moved things around. (Mostly just removed cases where tests would end up getting run several times, even though this code isn't anywhere near performance-critical.)



---

archive/issue_comments_046833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T09:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46833",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046834.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T09:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5923#issuecomment-46834",
    "user": "mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
