# Issue 2813: Add keycodes to split / join cells.

archive/issues_002813.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nFrom: Andrey Novoseltsev\nSubject: [sage-devel] Cell splitting/merging in notebook\n\n\nIs it possible to realize some convenient and fast (in the sense of\nkeyboard use) cell splitting/merging? It seems to me that now it\ninvolves manual copying of a part of code and creating/removing a\ncell, or editing the text representation. I really liked the ability\nto do it in Maple (back when I was using it ;-) by pressing some hot\nkeys since it allows you to group cells for executing in one step and\nnicer visual presentation or break them back when you want to interact\nwith intermediate values.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2813\n\n",
    "created_at": "2008-04-05T19:30:19Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Add keycodes to split / join cells.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2813",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby


```
From: Andrey Novoseltsev
Subject: [sage-devel] Cell splitting/merging in notebook


Is it possible to realize some convenient and fast (in the sense of
keyboard use) cell splitting/merging? It seems to me that now it
involves manual copying of a part of code and creating/removing a
cell, or editing the text representation. I really liked the ability
to do it in Maple (back when I was using it ;-) by pressing some hot
keys since it allows you to group cells for executing in one step and
nicer visual presentation or break them back when you want to interact
with intermediate values.
```


Issue created by migration from https://trac.sagemath.org/ticket/2813





---

archive/issue_comments_019266.json:
```json
{
    "body": "Attachment [2813-splitcell.patch](tarball://root/attachments/some-uuid/ticket2813/2813-splitcell.patch) by boothby created at 2008-04-05 19:33:18",
    "created_at": "2008-04-05T19:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19266",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [2813-splitcell.patch](tarball://root/attachments/some-uuid/ticket2813/2813-splitcell.patch) by boothby created at 2008-04-05 19:33:18



---

archive/issue_comments_019267.json:
```json
{
    "body": "Hi Tom,\n\nIn OS X firefox I tried this patch and it is really broken.  Splitting cells does absolutely nothing.  Joining works, but puts the active focus in the wrong cell. \n\nI'll see if I can fix it.",
    "created_at": "2008-04-05T20:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19267",
    "user": "https://github.com/williamstein"
}
```

Hi Tom,

In OS X firefox I tried this patch and it is really broken.  Splitting cells does absolutely nothing.  Joining works, but puts the active focus in the wrong cell. 

I'll see if I can fix it.



---

archive/issue_comments_019268.json:
```json
{
    "body": "On OS X with safari split does work.  Join has the same problem as described above.",
    "created_at": "2008-04-05T20:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19268",
    "user": "https://github.com/williamstein"
}
```

On OS X with safari split does work.  Join has the same problem as described above.



---

archive/issue_comments_019269.json:
```json
{
    "body": "Another REFEREE COMMENT:\n\nAbsolutely none of the functions you added in this patch have any documentation. \nThat has to be fixed before this patch gets accepted.  Even javascript functions have to have docs.   Again, I'm trying to work out what they do -- contact me before working on this.",
    "created_at": "2008-04-05T21:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19269",
    "user": "https://github.com/williamstein"
}
```

Another REFEREE COMMENT:

Absolutely none of the functions you added in this patch have any documentation. 
That has to be fixed before this patch gets accepted.  Even javascript functions have to have docs.   Again, I'm trying to work out what they do -- contact me before working on this.



---

archive/issue_comments_019270.json:
```json
{
    "body": "Attachment [sage-2813.patch](tarball://root/attachments/some-uuid/ticket2813/sage-2813.patch) by @williamstein created at 2008-04-06 02:29:09\n\nthis should be applied after tom's first patch",
    "created_at": "2008-04-06T02:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19270",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2813.patch](tarball://root/attachments/some-uuid/ticket2813/sage-2813.patch) by @williamstein created at 2008-04-06 02:29:09

this should be applied after tom's first patch



---

archive/issue_comments_019271.json:
```json
{
    "body": "Attachment [sage-2813_part3.patch](tarball://root/attachments/some-uuid/ticket2813/sage-2813_part3.patch) by @williamstein created at 2008-04-06 03:58:23\n\nthis adds opera support, at least under os x.",
    "created_at": "2008-04-06T03:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19271",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2813_part3.patch](tarball://root/attachments/some-uuid/ticket2813/sage-2813_part3.patch) by @williamstein created at 2008-04-06 03:58:23

this adds opera support, at least under os x.



---

archive/issue_comments_019272.json:
```json
{
    "body": "Attachment [2813_4.patch](tarball://root/attachments/some-uuid/ticket2813/2813_4.patch) by boothby created at 2008-04-06 05:31:23",
    "created_at": "2008-04-06T05:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19272",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [2813_4.patch](tarball://root/attachments/some-uuid/ticket2813/2813_4.patch) by boothby created at 2008-04-06 05:31:23



---

archive/issue_comments_019273.json:
```json
{
    "body": "Works great in Camino, but it has issues joining cells in Safari 3.1 on OS X 10.4.11.",
    "created_at": "2008-04-06T06:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19273",
    "user": "https://github.com/robertwb"
}
```

Works great in Camino, but it has issues joining cells in Safari 3.1 on OS X 10.4.11.



---

archive/issue_comments_019274.json:
```json
{
    "body": "Safari 3.1 isn't supported by Sage yet. Works great elsewhere.",
    "created_at": "2008-04-06T06:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19274",
    "user": "https://github.com/robertwb"
}
```

Safari 3.1 isn't supported by Sage yet. Works great elsewhere.



---

archive/issue_comments_019275.json:
```json
{
    "body": "Merged all four patches in Sage 3.0.alpha2",
    "created_at": "2008-04-06T06:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all four patches in Sage 3.0.alpha2



---

archive/issue_comments_019276.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T06:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2813#issuecomment-19276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
