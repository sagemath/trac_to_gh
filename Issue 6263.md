# Issue 6263: Add __cmp__ method to ClassFunctions (group characters)

archive/issues_006263.json:
```json
{
    "body": "Assignee: joyner\n\nThe loads/dumps test for ClassFunction fails because `__cmp__` is not defined.\n\n```\nsage: chi = ClassFunction(CyclicPermutationGroup(4), [1,-1,1,-1])\nsage: loads(dumps(chi)) == chi\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6263\n\n",
    "created_at": "2009-06-11T20:28:36Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Add __cmp__ method to ClassFunctions (group characters)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6263",
    "user": "saliola"
}
```
Assignee: joyner

The loads/dumps test for ClassFunction fails because `__cmp__` is not defined.

```
sage: chi = ClassFunction(CyclicPermutationGroup(4), [1,-1,1,-1])
sage: loads(dumps(chi)) == chi
False
```


Issue created by migration from https://trac.sagemath.org/ticket/6263





---

archive/issue_comments_050006.json:
```json
{
    "body": "Attachment [trac_6263.patch](tarball://root/attachments/some-uuid/ticket6263/trac_6263.patch) by saliola created at 2009-06-11 21:20:10",
    "created_at": "2009-06-11T21:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50006",
    "user": "saliola"
}
```

Attachment [trac_6263.patch](tarball://root/attachments/some-uuid/ticket6263/trac_6263.patch) by saliola created at 2009-06-11 21:20:10



---

archive/issue_comments_050007.json:
```json
{
    "body": "I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?",
    "created_at": "2009-06-11T21:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50007",
    "user": "wdj"
}
```

I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?



---

archive/issue_comments_050008.json:
```json
{
    "body": "Aside from wdj comments, the patch fixes the problem I was having with the characters of finite groups.\nDoes the  <  a shortcut for \"does this character of G restrict to this character of H, where H is a subgroup of G\"?",
    "created_at": "2009-06-11T22:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50008",
    "user": "jlefebvre"
}
```

Aside from wdj comments, the patch fixes the problem I was having with the characters of finite groups.
Does the  <  a shortcut for "does this character of G restrict to this character of H, where H is a subgroup of G"?



---

archive/issue_comments_050009.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?\n\nThe GAP manual contains a section called [Comparison of Class Functions](http://www.gap-system.org/~gap/Manuals/doc/htm/ref/CHAP070.htm#SECT003), which reads:\n\n```\nSo two class functions are equal if and only if their lists of values are equal, no matter whether they are class functions of the same character table, of the same group but w.r.t. different class ordering, or of different groups. \n```\n\nSo this is partly replicated here, except that the patch actually tests the groups as well as the values.\n\nIf you think it would be better, we can just ask GAP and return the answer it gives.",
    "created_at": "2009-06-11T22:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50009",
    "user": "saliola"
}
```

Replying to [comment:2 wdj]:
> I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?

The GAP manual contains a section called [Comparison of Class Functions](http://www.gap-system.org/~gap/Manuals/doc/htm/ref/CHAP070.htm#SECT003), which reads:

```
So two class functions are equal if and only if their lists of values are equal, no matter whether they are class functions of the same character table, of the same group but w.r.t. different class ordering, or of different groups. 
```

So this is partly replicated here, except that the patch actually tests the groups as well as the values.

If you think it would be better, we can just ask GAP and return the answer it gives.



---

archive/issue_comments_050010.json:
```json
{
    "body": "Replying to [comment:3 jlefebvre]:\n> Does the  <  a shortcut for \"does this character of G restrict to this character of H, where H is a subgroup of G\"?\n\nNo, it just does a comparison of the list of values. This is what GAP does (see my previous method for more information).",
    "created_at": "2009-06-11T22:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50010",
    "user": "saliola"
}
```

Replying to [comment:3 jlefebvre]:
> Does the  <  a shortcut for "does this character of G restrict to this character of H, where H is a subgroup of G"?

No, it just does a comparison of the list of values. This is what GAP does (see my previous method for more information).



---

archive/issue_comments_050011.json:
```json
{
    "body": "Replying to [comment:4 saliola]:\n> Replying to [comment:2 wdj]:\n> > I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?\n> \n> The GAP manual contains a section called [Comparison of Class Functions](http://www.gap-system.org/~gap/Manuals/doc/htm/ref/CHAP070.htm#SECT003), which reads:\n> {{{\n> So two class functions are equal if and only if their lists of values are equal, no matter whether they are class functions of the same character table, of the same group but w.r.t. different class ordering, or of different groups. \n> }}}\n\nOkay, it seems as though at least you are improving the situation over what GAP has!\n\n\n\n> So this is partly replicated here, except that the patch actually tests the groups as well as the values.\n> \n> If you think it would be better, we can just ask GAP and return the answer it gives.",
    "created_at": "2009-06-11T22:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50011",
    "user": "wdj"
}
```

Replying to [comment:4 saliola]:
> Replying to [comment:2 wdj]:
> > I thought GAP's characters were returned in randomish order, at least for more complicated groups that have lots of conjugacy classes of a given order. Does this patch handle that situation?
> 
> The GAP manual contains a section called [Comparison of Class Functions](http://www.gap-system.org/~gap/Manuals/doc/htm/ref/CHAP070.htm#SECT003), which reads:
> {{{
> So two class functions are equal if and only if their lists of values are equal, no matter whether they are class functions of the same character table, of the same group but w.r.t. different class ordering, or of different groups. 
> }}}

Okay, it seems as though at least you are improving the situation over what GAP has!



> So this is partly replicated here, except that the patch actually tests the groups as well as the values.
> 
> If you think it would be better, we can just ask GAP and return the answer it gives.



---

archive/issue_comments_050012.json:
```json
{
    "body": "It looks good to me, I'm not quite sure of gaps justification of having less than comparison, but seems there's nothing wrong in following it. So, marking it with positive review.",
    "created_at": "2009-06-12T05:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50012",
    "user": "jlefebvre"
}
```

It looks good to me, I'm not quite sure of gaps justification of having less than comparison, but seems there's nothing wrong in following it. So, marking it with positive review.



---

archive/issue_comments_050013.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6263#issuecomment-50013",
    "user": "ncalexan"
}
```

Resolution: fixed
