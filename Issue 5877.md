# Issue 5877: calling a group character is broken

archive/issues_005877.json:
```json
{
    "body": "Assignee: saliola\n\nCC:  wdj\n\n\n```\nsage: G = SymmetricGroup(3)\nsage: h = G((2,3))\nsage: triv = G.trivial_character()\nsage: triv(h)\nTraceback ...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5877\n\n",
    "created_at": "2009-04-23T16:38:58Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "calling a group character is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5877",
    "user": "saliola"
}
```
Assignee: saliola

CC:  wdj


```
sage: G = SymmetricGroup(3)
sage: h = G((2,3))
sage: triv = G.trivial_character()
sage: triv(h)
Traceback ...
```


Issue created by migration from https://trac.sagemath.org/ticket/5877





---

archive/issue_comments_046428.json:
```json
{
    "body": "It's a small problem, with a small patch.",
    "created_at": "2009-04-23T16:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46428",
    "user": "saliola"
}
```

It's a small problem, with a small patch.



---

archive/issue_comments_046429.json:
```json
{
    "body": "Just to confirm: This is still a problem with the downgraded GAP in Sage 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T23:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46429",
    "user": "mabshoff"
}
```

Just to confirm: This is still a problem with the downgraded GAP in Sage 3.4.1.

Cheers,

Michael



---

archive/issue_comments_046430.json:
```json
{
    "body": "I know very little about GAP and the implementation of groups in Sage, but is this really the most efficient way to do this? It looks like the code has to enumerate the conjugacy classes of the group on every call, is that for real?",
    "created_at": "2009-04-25T00:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46430",
    "user": "dmharvey"
}
```

I know very little about GAP and the implementation of groups in Sage, but is this really the most efficient way to do this? It looks like the code has to enumerate the conjugacy classes of the group on every call, is that for real?



---

archive/issue_comments_046431.json:
```json
{
    "body": "Hello David, thanks for your comments.\n\nReplying to [comment:3 dmharvey]:\n> I know very little about GAP and the implementation of groups in Sage, but is this really the most efficient way to do this? It looks like the code has to enumerate the conjugacy classes of the group on every call, is that for real?\n\nI know very little about GAP as well. I just followed the method described below, which I found at\n[GAP-Forum](http://www.gap-system.org/ForumArchive/Hulpke.1/Alexande.1/Re__Char.11/2.html):\n\n```\nYou will (if you like it or not) have to identify the class of the element g.\nYou can do this in general, by a specific test with \\in (but see below):\n\ngap> cl:=ConjugacyClasses(G);;\ngap> First([1..Length(cl)],i->g in cl[i]);\n4\n\nSo you know the class is class number 4, with the name:\n\n    gap> ClassNames(CharacterTable(G))[4];\n    \"9a\"\n\nSo the character value is:\n\ngap> Irr(G)[3][4];\nE(9)^2+E(9)^4+E(9)^5+E(9)^7\n```\n\n\nI did a bit more research, and I found a direct method to evaluate the class function via GAP. Of course, the computation still needs to determine the class to which the element belongs, but at least there won't be the extra interface overhead of going back and forth between Sage and GAP for each test. Moreover, GAP must have speedups for particular types of groups (the above method is for the generic case).\n\nI'll replace the patch right-away with the better version.",
    "created_at": "2009-04-25T11:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46431",
    "user": "saliola"
}
```

Hello David, thanks for your comments.

Replying to [comment:3 dmharvey]:
> I know very little about GAP and the implementation of groups in Sage, but is this really the most efficient way to do this? It looks like the code has to enumerate the conjugacy classes of the group on every call, is that for real?

I know very little about GAP as well. I just followed the method described below, which I found at
[GAP-Forum](http://www.gap-system.org/ForumArchive/Hulpke.1/Alexande.1/Re__Char.11/2.html):

```
You will (if you like it or not) have to identify the class of the element g.
You can do this in general, by a specific test with \in (but see below):

gap> cl:=ConjugacyClasses(G);;
gap> First([1..Length(cl)],i->g in cl[i]);
4

So you know the class is class number 4, with the name:

    gap> ClassNames(CharacterTable(G))[4];
    "9a"

So the character value is:

gap> Irr(G)[3][4];
E(9)^2+E(9)^4+E(9)^5+E(9)^7
```


I did a bit more research, and I found a direct method to evaluate the class function via GAP. Of course, the computation still needs to determine the class to which the element belongs, but at least there won't be the extra interface overhead of going back and forth between Sage and GAP for each test. Moreover, GAP must have speedups for particular types of groups (the above method is for the generic case).

I'll replace the patch right-away with the better version.



---

archive/issue_comments_046432.json:
```json
{
    "body": "Attachment [trac_5877.patch](tarball://root/attachments/some-uuid/ticket5877/trac_5877.patch) by dmharvey created at 2009-04-25 12:24:11\n\nOK, can I just clarify that the problem with the original code is that the GAP Representative function doesn't return a canonical representative? i.e. if you start with two different group elements in the same class, convert them to classes and then ask for their Representative, you might get different answers?",
    "created_at": "2009-04-25T12:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46432",
    "user": "dmharvey"
}
```

Attachment [trac_5877.patch](tarball://root/attachments/some-uuid/ticket5877/trac_5877.patch) by dmharvey created at 2009-04-25 12:24:11

OK, can I just clarify that the problem with the original code is that the GAP Representative function doesn't return a canonical representative? i.e. if you start with two different group elements in the same class, convert them to classes and then ask for their Representative, you might get different answers?



---

archive/issue_comments_046433.json:
```json
{
    "body": "Replying to [comment:5 dmharvey]:\n> OK, can I just clarify that the problem with the original code is that the GAP Representative function doesn't return a canonical representative? i.e. if you start with two different group elements in the same class, convert them to classes and then ask for their Representative, you might get different answers?\n\nThat is correct, here's an illustration.\n\n```\nsage: G = SymmetricGroup(3)\nsage: g = G((1,2))\nsage: h = G((2,3))\nsage: gap(G).ConjugacyClass(h).Representative()\n(2,3)\nsage: gap(G).ConjugacyClass(g).Representative()\n(1,2)\nsage: gap(G).ConjugacyClass(g) == gap(G).ConjugacyClass(h)\nTrue\n```\n\n\nFranco",
    "created_at": "2009-04-25T12:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46433",
    "user": "saliola"
}
```

Replying to [comment:5 dmharvey]:
> OK, can I just clarify that the problem with the original code is that the GAP Representative function doesn't return a canonical representative? i.e. if you start with two different group elements in the same class, convert them to classes and then ask for their Representative, you might get different answers?

That is correct, here's an illustration.

```
sage: G = SymmetricGroup(3)
sage: g = G((1,2))
sage: h = G((2,3))
sage: gap(G).ConjugacyClass(h).Representative()
(2,3)
sage: gap(G).ConjugacyClass(g).Representative()
(1,2)
sage: gap(G).ConjugacyClass(g) == gap(G).ConjugacyClass(h)
True
```


Franco



---

archive/issue_comments_046434.json:
```json
{
    "body": "Ok, looks good to me.",
    "created_at": "2009-04-25T20:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46434",
    "user": "dmharvey"
}
```

Ok, looks good to me.



---

archive/issue_comments_046435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T02:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46435",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046436.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T02:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5877#issuecomment-46436",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael
