# Issue 3051: Weyl Characters

archive/issues_003051.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: Weyl characters, branching rules\n\nThis was announced here:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/74ed91d5153e6022?hl=en\n\nSee also:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/f713ed4bf3df8c22?hl=en\n\nAt Mike Hansen and Nicolas Thiery's suggestions the default separator is now \",\" and the separator is configurable. \n\nI believe all branching rules to maximal subgroups of compact Lie groups are implemented with two (large) exceptions: reducible subgroups like A1 x A1, and branching rules involving the exceptional groups. Mike requested that the branching be made a method, and the new syntax is something like\nchi.branch(B3,rule=\"symmetric\"). However I left Branch as a standalone program and the\nmain docstring is Branch? This of course can be changed. \n\nAn issue is that the caching is a substantial speedup but at a potentially large cost in memory. I hesitated to make it the default so cache=False is the default. But the user will be happier with cache=True.\n\nIt is possible to cache more aggressively. I have not implemented but know how to implement caching the results of multiplications instead of just the characters themselves.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3051\n\n",
    "created_at": "2008-04-28T22:52:26Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Weyl Characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3051",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: Weyl characters, branching rules

This was announced here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/74ed91d5153e6022?hl=en

See also:

http://groups.google.com/group/sage-devel/browse_thread/thread/f713ed4bf3df8c22?hl=en

At Mike Hansen and Nicolas Thiery's suggestions the default separator is now "," and the separator is configurable. 

I believe all branching rules to maximal subgroups of compact Lie groups are implemented with two (large) exceptions: reducible subgroups like A1 x A1, and branching rules involving the exceptional groups. Mike requested that the branching be made a method, and the new syntax is something like
chi.branch(B3,rule="symmetric"). However I left Branch as a standalone program and the
main docstring is Branch? This of course can be changed. 

An issue is that the caching is a substantial speedup but at a potentially large cost in memory. I hesitated to make it the default so cache=False is the default. But the user will be happier with cache=True.

It is possible to cache more aggressively. I have not implemented but know how to implement caching the results of multiplications instead of just the characters themselves.



Issue created by migration from https://trac.sagemath.org/ticket/3051





---

archive/issue_comments_020980.json:
```json
{
    "body": "Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3051/9607.patch) by @dwbump created at 2008-04-28 22:52:48",
    "created_at": "2008-04-28T22:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20980",
    "user": "https://github.com/dwbump"
}
```

Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3051/9607.patch) by @dwbump created at 2008-04-28 22:52:48



---

archive/issue_comments_020981.json:
```json
{
    "body": "Is this based on 3.0? I got:\n\n\n```\n\napplying /Users/wdj/sagefiles/9607.patch\nabort: unable to find sage/combinat/crystals/crystals.py or sage/combinat/crystals/crystals.py for patching\n```\n",
    "created_at": "2008-04-29T00:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20981",
    "user": "https://github.com/wdjoyner"
}
```

Is this based on 3.0? I got:


```

applying /Users/wdj/sagefiles/9607.patch
abort: unable to find sage/combinat/crystals/crystals.py or sage/combinat/crystals/crystals.py for patching
```




---

archive/issue_comments_020982.json:
```json
{
    "body": "Things work perfectly to me:\n\n```\nsage$ patch -p1 --dry-run < 9607.patch\\?format\\=raw\npatching file sage/combinat/crystals/crystals.py\npatching file sage/combinat/root_system/all.py\npatching file sage/combinat/root_system/cartan_type.py\npatching file sage/combinat/root_system/weyl_characters.py\n```\n\nThis is against 3.0.1.alpha1.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-29T00:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Things work perfectly to me:

```
sage$ patch -p1 --dry-run < 9607.patch\?format\=raw
patching file sage/combinat/crystals/crystals.py
patching file sage/combinat/root_system/all.py
patching file sage/combinat/root_system/cartan_type.py
patching file sage/combinat/root_system/weyl_characters.py
```

This is against 3.0.1.alpha1.

Cheers,

Michael



---

archive/issue_comments_020983.json:
```json
{
    "body": "It's a patch against 3.0.\n\nDan",
    "created_at": "2008-04-29T02:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20983",
    "user": "https://github.com/dwbump"
}
```

It's a patch against 3.0.

Dan



---

archive/issue_comments_020984.json:
```json
{
    "body": "Thanks. It's working now. I'm running sage -testall now but want to point out that the standard format for Python functions is all_lower_underscore. The function \"Branch\" is definitely non-standard naming.",
    "created_at": "2008-04-29T03:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20984",
    "user": "https://github.com/wdjoyner"
}
```

Thanks. It's working now. I'm running sage -testall now but want to point out that the standard format for Python functions is all_lower_underscore. The function "Branch" is definitely non-standard naming.



---

archive/issue_comments_020985.json:
```json
{
    "body": "Applies cleanly to a 3.0 base and passes sage -testall on an ubuntu 7.10amd64 machine. (It did not apply cleanly on a macbook but possibly I made a mistake somewhere.) \n\n(1) This character theory stuff is a *great* contribution and I think that SAGE is lucky to have someone of Dan's abilities contributing code like this. However, I have some unfavorable comments.\n\n(2) There is this capitalization issue. I think capitalizing the functions IrreducibleCharacterFreudenthal and Branch is confusing. (There may be other examples I am missing as well.) Classes are capitalized, not functions. Possibly you could drop \n\n```\nirreducible_character_freudenthal = IrreducibleCharacterFreudenthal\nbranch = Branch\n```\n\nat the bottom of the file but even that I think is not enough. \n\n(3) Actually, I think branch is too generic to use and would prefer something like branch_character or something. (Who knows, maybe someone will write a Tableau class for characters of the symmetric group and friends and wants to use it in their module too. Who wins?)\n\n(4) I think the documentation is great on one hand and lacking references on the other. I really hope the author will consider adding somewhere a REFERENCES: section to his docstrings (possibly to books or papers of his own) and specific (I mean page or Theorem or Definition numbers) citations thoughout his code. That way people will learn from it and be able to maintain it better, since with proper citations everyone will be one the same page.\n \nI realize these are a little excessive and am happy to be over-ruled. But I don't yet give this a positive review.",
    "created_at": "2008-04-29T11:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20985",
    "user": "https://github.com/wdjoyner"
}
```

Applies cleanly to a 3.0 base and passes sage -testall on an ubuntu 7.10amd64 machine. (It did not apply cleanly on a macbook but possibly I made a mistake somewhere.) 

(1) This character theory stuff is a *great* contribution and I think that SAGE is lucky to have someone of Dan's abilities contributing code like this. However, I have some unfavorable comments.

(2) There is this capitalization issue. I think capitalizing the functions IrreducibleCharacterFreudenthal and Branch is confusing. (There may be other examples I am missing as well.) Classes are capitalized, not functions. Possibly you could drop 

```
irreducible_character_freudenthal = IrreducibleCharacterFreudenthal
branch = Branch
```

at the bottom of the file but even that I think is not enough. 

(3) Actually, I think branch is too generic to use and would prefer something like branch_character or something. (Who knows, maybe someone will write a Tableau class for characters of the symmetric group and friends and wants to use it in their module too. Who wins?)

(4) I think the documentation is great on one hand and lacking references on the other. I really hope the author will consider adding somewhere a REFERENCES: section to his docstrings (possibly to books or papers of his own) and specific (I mean page or Theorem or Definition numbers) citations thoughout his code. That way people will learn from it and be able to maintain it better, since with proper citations everyone will be one the same page.
 
I realize these are a little excessive and am happy to be over-ruled. But I don't yet give this a positive review.



---

archive/issue_comments_020986.json:
```json
{
    "body": "I definitely agree that Branch -> branch_character should be done and the capitalization of the other function can be changed too. BTW Branch is globally exposed by IrreducibleCharacterFreudenthal is not (cf. all.py).\n\nThere is a question of whether Branch should be left globally exposed. Maybe this is not needed. The code in it could be moved to the branch method of Weyl character but since it's long and its docstring is long I left it alone.\n\nAbout (4), I'm less eager to start expanding the docstring further.\n\nI won't put up another patch yet since Mike Hansen may comment or revise it, and there could be further comments from others.\n\nIn view of Michael Abshoff's comments the caching should be left off by default and before considering turning it on by default it should be reimplemented  using weak references.",
    "created_at": "2008-04-29T12:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20986",
    "user": "https://github.com/dwbump"
}
```

I definitely agree that Branch -> branch_character should be done and the capitalization of the other function can be changed too. BTW Branch is globally exposed by IrreducibleCharacterFreudenthal is not (cf. all.py).

There is a question of whether Branch should be left globally exposed. Maybe this is not needed. The code in it could be moved to the branch method of Weyl character but since it's long and its docstring is long I left it alone.

About (4), I'm less eager to start expanding the docstring further.

I won't put up another patch yet since Mike Hansen may comment or revise it, and there could be further comments from others.

In view of Michael Abshoff's comments the caching should be left off by default and before considering turning it on by default it should be reimplemented  using weak references.



---

archive/issue_comments_020987.json:
```json
{
    "body": "Attachment [9608.patch](tarball://root/attachments/some-uuid/ticket3051/9608.patch) by @dwbump created at 2008-04-29 16:09:22\n\nname change: Branch -> branch_weyl_character",
    "created_at": "2008-04-29T16:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20987",
    "user": "https://github.com/dwbump"
}
```

Attachment [9608.patch](tarball://root/attachments/some-uuid/ticket3051/9608.patch) by @dwbump created at 2008-04-29 16:09:22

name change: Branch -> branch_weyl_character



---

archive/issue_comments_020988.json:
```json
{
    "body": "I added a second small patch that makes the name changes Branch -> branch_weyl_character and IrreducibleCharacterFreudenthal -> irreducible_character_freudenthal, addressing points (2) and (3) of David's review.",
    "created_at": "2008-04-29T16:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20988",
    "user": "https://github.com/dwbump"
}
```

I added a second small patch that makes the name changes Branch -> branch_weyl_character and IrreducibleCharacterFreudenthal -> irreducible_character_freudenthal, addressing points (2) and (3) of David's review.



---

archive/issue_comments_020989.json:
```json
{
    "body": "I'll go through and get it 100% doctested so it can go in.",
    "created_at": "2008-04-29T19:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20989",
    "user": "https://github.com/mwhansen"
}
```

I'll go through and get it 100% doctested so it can go in.



---

archive/issue_comments_020990.json:
```json
{
    "body": "Attachment [9609.patch](tarball://root/attachments/some-uuid/ticket3051/9609.patch) by @dwbump created at 2008-05-02 14:53:51",
    "created_at": "2008-05-02T14:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20990",
    "user": "https://github.com/dwbump"
}
```

Attachment [9609.patch](tarball://root/attachments/some-uuid/ticket3051/9609.patch) by @dwbump created at 2008-05-02 14:53:51



---

archive/issue_comments_020991.json:
```json
{
    "body": "I added 9609.patch.\n\nThis gives doctests for most methods.\n\nRemoves an unimplemented method that was accidentally left.\n\nCorrects a minor bug (`__repr__` misspelled somewhere).",
    "created_at": "2008-05-02T14:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20991",
    "user": "https://github.com/dwbump"
}
```

I added 9609.patch.

This gives doctests for most methods.

Removes an unimplemented method that was accidentally left.

Corrects a minor bug (`__repr__` misspelled somewhere).



---

archive/issue_comments_020992.json:
```json
{
    "body": "Attachment [9610.patch](tarball://root/attachments/some-uuid/ticket3051/9610.patch) by @dwbump created at 2008-05-02 21:53:11\n\nThe patch 9610.patch completes the doctesting to 100%.\n\nI found 2 bugs which are fixed. In _add_ some code had the wrong\nindent level and this has been fixed. and `_neg_` was misspelled\nsomewhere.\n\nDan",
    "created_at": "2008-05-02T21:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20992",
    "user": "https://github.com/dwbump"
}
```

Attachment [9610.patch](tarball://root/attachments/some-uuid/ticket3051/9610.patch) by @dwbump created at 2008-05-02 21:53:11

The patch 9610.patch completes the doctesting to 100%.

I found 2 bugs which are fixed. In _add_ some code had the wrong
indent level and this has been fixed. and `_neg_` was misspelled
somewhere.

Dan



---

archive/issue_comments_020993.json:
```json
{
    "body": "Attachment [9611.patch](tarball://root/attachments/some-uuid/ticket3051/9611.patch) by @dwbump created at 2008-05-04 17:17:43\n\nAdded 9611.patch.\n\nMinor bugfixes and improvements.\n\nThe bugfixes are in WeylCharacterRing's `__call__` method, which worked reasonably well over ZZ but not over a polynomial ring. After the patch, we first intercept integers, then try to coerce elements into the base ring, but we check the parent first since it is possible to coerce a list of integers into a polynomial ring.  In other words, we don't want to break calls like `R([2,1,0])`.\n\nI found that changing the way `repr_lincomb` is called resulted in nicer output.\n\nA parent method is added to elements.\n\nMore doctests are added in response to the problems I found in __call__ and there are revisions to old doctests in response to the revised lincomb call.",
    "created_at": "2008-05-04T17:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20993",
    "user": "https://github.com/dwbump"
}
```

Attachment [9611.patch](tarball://root/attachments/some-uuid/ticket3051/9611.patch) by @dwbump created at 2008-05-04 17:17:43

Added 9611.patch.

Minor bugfixes and improvements.

The bugfixes are in WeylCharacterRing's `__call__` method, which worked reasonably well over ZZ but not over a polynomial ring. After the patch, we first intercept integers, then try to coerce elements into the base ring, but we check the parent first since it is possible to coerce a list of integers into a polynomial ring.  In other words, we don't want to break calls like `R([2,1,0])`.

I found that changing the way `repr_lincomb` is called resulted in nicer output.

A parent method is added to elements.

More doctests are added in response to the problems I found in __call__ and there are revisions to old doctests in response to the revised lincomb call.



---

archive/issue_comments_020994.json:
```json
{
    "body": "Attachment [9673.patch](tarball://root/attachments/some-uuid/ticket3051/9673.patch) by @dwbump created at 2008-05-06 18:56:07",
    "created_at": "2008-05-06T18:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20994",
    "user": "https://github.com/dwbump"
}
```

Attachment [9673.patch](tarball://root/attachments/some-uuid/ticket3051/9673.patch) by @dwbump created at 2008-05-06 18:56:07



---

archive/issue_comments_020995.json:
```json
{
    "body": "I added a patch called 9673.patch.\n\nThis reimplements the Freudenthal multiplicity formula. \n\nFormerly, weight multiplicities are calculated in a region containing the positive Weyl chamber, then copied around using the action of the Weyl group. In the reimplementation, all weights are calculated using the recursion relations, without using the Weyl group action. This turns out to be much faster, as well as simpler.\n\nOne test result was changed because the weights of B3(spin) are calculated in a different order.",
    "created_at": "2008-05-06T19:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20995",
    "user": "https://github.com/dwbump"
}
```

I added a patch called 9673.patch.

This reimplements the Freudenthal multiplicity formula. 

Formerly, weight multiplicities are calculated in a region containing the positive Weyl chamber, then copied around using the action of the Weyl group. In the reimplementation, all weights are calculated using the recursion relations, without using the Weyl group action. This turns out to be much faster, as well as simpler.

One test result was changed because the weights of B3(spin) are calculated in a different order.



---

archive/issue_comments_020996.json:
```json
{
    "body": "Attachment [9674.patch](tarball://root/attachments/some-uuid/ticket3051/9674.patch) by @dwbump created at 2008-05-07 21:54:17",
    "created_at": "2008-05-07T21:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20996",
    "user": "https://github.com/dwbump"
}
```

Attachment [9674.patch](tarball://root/attachments/some-uuid/ticket3051/9674.patch) by @dwbump created at 2008-05-07 21:54:17



---

archive/issue_comments_020997.json:
```json
{
    "body": "Attachment [3051-unified.patch](tarball://root/attachments/some-uuid/ticket3051/3051-unified.patch) by @dwbump created at 2008-05-07 21:55:37",
    "created_at": "2008-05-07T21:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20997",
    "user": "https://github.com/dwbump"
}
```

Attachment [3051-unified.patch](tarball://root/attachments/some-uuid/ticket3051/3051-unified.patch) by @dwbump created at 2008-05-07 21:55:37



---

archive/issue_comments_020998.json:
```json
{
    "body": "The last patch, 9674.patch is explained here:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/82dd8255caa108cf\n\nThere are a lot of patches so I posted a single patch 3051-unified.patch\nthat is the union of the other patches.\n\nI have changed the patch summary from [with patch, positive review pending changes]\nto [with patch, needs review (again)] and hope that David Joyner and Mike Hansen\ncan look at it again.",
    "created_at": "2008-05-07T22:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20998",
    "user": "https://github.com/dwbump"
}
```

The last patch, 9674.patch is explained here:

http://groups.google.com/group/sage-combinat-devel/msg/82dd8255caa108cf

There are a lot of patches so I posted a single patch 3051-unified.patch
that is the union of the other patches.

I have changed the patch summary from [with patch, positive review pending changes]
to [with patch, needs review (again)] and hope that David Joyner and Mike Hansen
can look at it again.



---

archive/issue_comments_020999.json:
```json
{
    "body": "This passes sage -testall and applies cleanly. I'll look at it some more later this morning but wanted to post that info since it might save some time for anyone else looking at it.",
    "created_at": "2008-05-08T11:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-20999",
    "user": "https://github.com/wdjoyner"
}
```

This passes sage -testall and applies cleanly. I'll look at it some more later this morning but wanted to post that info since it might save some time for anyone else looking at it.



---

archive/issue_comments_021000.json:
```json
{
    "body": "I see I inadvertently omitted the changes to crystals.py from 9607.patch when I made the unified patch. I think it best if I leave those out for now since David has already run testall. If this patch can be reviewed as it is I can make another ticket later for the changes to crystals.py.",
    "created_at": "2008-05-08T12:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21000",
    "user": "https://github.com/dwbump"
}
```

I see I inadvertently omitted the changes to crystals.py from 9607.patch when I made the unified patch. I think it best if I leave those out for now since David has already run testall. If this patch can be reviewed as it is I can make another ticket later for the changes to crystals.py.



---

archive/issue_comments_021001.json:
```json
{
    "body": "Don't worry about that. If you want to make a new unified patch, do so and let me know. I'll re-run sage -testall.",
    "created_at": "2008-05-08T13:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21001",
    "user": "https://github.com/wdjoyner"
}
```

Don't worry about that. If you want to make a new unified patch, do so and let me know. I'll re-run sage -testall.



---

archive/issue_comments_021002.json:
```json
{
    "body": "Attachment [3051-1.patch](tarball://root/attachments/some-uuid/ticket3051/3051-1.patch) by @dwbump created at 2008-05-08 14:41:24\n\n> Don't worry about that. If you want to make a new unified patch, do so and let me know. I'll re-run sage -testall.\n\nThanks.\n\nI made a separate patch called 3051-1.patch containing just the changes to\ncrystals.py. This goes on top of 3051-1.unified.",
    "created_at": "2008-05-08T14:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21002",
    "user": "https://github.com/dwbump"
}
```

Attachment [3051-1.patch](tarball://root/attachments/some-uuid/ticket3051/3051-1.patch) by @dwbump created at 2008-05-08 14:41:24

> Don't worry about that. If you want to make a new unified patch, do so and let me know. I'll re-run sage -testall.

Thanks.

I made a separate patch called 3051-1.patch containing just the changes to
crystals.py. This goes on top of 3051-1.unified.



---

archive/issue_comments_021003.json:
```json
{
    "body": "This patch 3051-1, applied on top of the 3051-unified patch, applies cleanly to 3.0.1. sage -testall \nfailed on one module but then testing that module separately passes. \n\n\n```\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx\nTotal time for all tests: 5283.6 seconds\nPlease see /home/wdj/wdj/sagefiles/sage-3.0.1/tmp/test.log for the complete log from this test.\nwdj@wooster:~/wdj/sagefiles/sage-3.0.1$ ./sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx\nsage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx\n         [4.8 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.8 seconds\n```\n\nI'm guessing that this failure is spurious. (It was done on an older machine, which has had\nlots of such failures before.) I'll keep looking at this patch, but wanted to report this issue ASAP.",
    "created_at": "2008-05-08T17:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21003",
    "user": "https://github.com/wdjoyner"
}
```

This patch 3051-1, applied on top of the 3051-unified patch, applies cleanly to 3.0.1. sage -testall 
failed on one module but then testing that module separately passes. 


```
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx
Total time for all tests: 5283.6 seconds
Please see /home/wdj/wdj/sagefiles/sage-3.0.1/tmp/test.log for the complete log from this test.
wdj@wooster:~/wdj/sagefiles/sage-3.0.1$ ./sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx
sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx
         [4.8 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.8 seconds
```

I'm guessing that this failure is spurious. (It was done on an older machine, which has had
lots of such failures before.) I'll keep looking at this patch, but wanted to report this issue ASAP.



---

archive/issue_comments_021004.json:
```json
{
    "body": "More comments.\n\n1. The class name Weight is IMHO too generic and is not consistent with SAGE's naming \"standard\". Better would be WeightRingElement (or WeightAlgebraElement?).\n\n2. Perhaps this is a very minor point since this appears common with lots of other modules, but I think that legally when you simply license code under the GPL, the default is the latest version (which of course is GPLv3). Better is to specify \"GPLv2 or later (at your preference)\".\n\n3. IMHO, this is a fantastic contribution by a leader in the field. Not to look a gift horse in the mouth, but I repeat that references to the literature would add value. I don't want to make a big deal of it though. If no one else does, I will add them myself later when I can get near my repn theory books (due to some home construction, those books are behind mounds of furniture at the moment).\n\nSo, modulo (1) above, I give this a positive review, but would like to hear what Mike Hansen has to say as well before renaming the Summary.",
    "created_at": "2008-05-08T18:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21004",
    "user": "https://github.com/wdjoyner"
}
```

More comments.

1. The class name Weight is IMHO too generic and is not consistent with SAGE's naming "standard". Better would be WeightRingElement (or WeightAlgebraElement?).

2. Perhaps this is a very minor point since this appears common with lots of other modules, but I think that legally when you simply license code under the GPL, the default is the latest version (which of course is GPLv3). Better is to specify "GPLv2 or later (at your preference)".

3. IMHO, this is a fantastic contribution by a leader in the field. Not to look a gift horse in the mouth, but I repeat that references to the literature would add value. I don't want to make a big deal of it though. If no one else does, I will add them myself later when I can get near my repn theory books (due to some home construction, those books are behind mounds of furniture at the moment).

So, modulo (1) above, I give this a positive review, but would like to hear what Mike Hansen has to say as well before renaming the Summary.



---

archive/issue_comments_021005.json:
```json
{
    "body": "> 1. The class name Weight is IMHO too generic and is not consistent with SAGE's naming \"standard\". Better would be WeightRingElement? (or WeightAlgebraElement??).\n\nI agree and will change it to WeightRingElement.\n\n> 2. Perhaps this is a very minor point since this appears common with lots of other modules, but I think that legally when you simply license code under the GPL, the default is the latest version (which of course is GPLv3). Better is to specify \"GPLv2 or later (at your preference)\".\n\nThe copyright header is the same as the other files in the combinat directory.\n\n> 3. IMHO, this is a fantastic contribution by a leader in the field. Not to look a gift horse in the mouth, but I repeat that references to the literature would add value. I don't want to make a big deal of it though. If no one else does, I will add them myself later when I can get near my repn theory books (due to some home construction, those books are behind mounds of furniture at the moment).\n\nDynkin's paper is already cited, where maximal subgroups of Lie groups are classified. Also Humpfrey's book on Lie algebras is already cited. However I will add some references. I can add references to books of Goodman and Wallach and Bump and a further citation of Humpfrey's book(for highest weight theory) and (for branching rules) papers of Howe, Chye and Willenbring and of R.C. King.\n\nCan you (or anyone) think of anything else that would be good to cite?\n\nI'll put up another patch (I hope by 5PM PDT) addressing (1) and (3) but not (2) since the comment applies systematically in combinat/.",
    "created_at": "2008-05-08T20:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21005",
    "user": "https://github.com/dwbump"
}
```

> 1. The class name Weight is IMHO too generic and is not consistent with SAGE's naming "standard". Better would be WeightRingElement? (or WeightAlgebraElement??).

I agree and will change it to WeightRingElement.

> 2. Perhaps this is a very minor point since this appears common with lots of other modules, but I think that legally when you simply license code under the GPL, the default is the latest version (which of course is GPLv3). Better is to specify "GPLv2 or later (at your preference)".

The copyright header is the same as the other files in the combinat directory.

> 3. IMHO, this is a fantastic contribution by a leader in the field. Not to look a gift horse in the mouth, but I repeat that references to the literature would add value. I don't want to make a big deal of it though. If no one else does, I will add them myself later when I can get near my repn theory books (due to some home construction, those books are behind mounds of furniture at the moment).

Dynkin's paper is already cited, where maximal subgroups of Lie groups are classified. Also Humpfrey's book on Lie algebras is already cited. However I will add some references. I can add references to books of Goodman and Wallach and Bump and a further citation of Humpfrey's book(for highest weight theory) and (for branching rules) papers of Howe, Chye and Willenbring and of R.C. King.

Can you (or anyone) think of anything else that would be good to cite?

I'll put up another patch (I hope by 5PM PDT) addressing (1) and (3) but not (2) since the comment applies systematically in combinat/.



---

archive/issue_comments_021006.json:
```json
{
    "body": "Attachment [3051-2.patch](tarball://root/attachments/some-uuid/ticket3051/3051-2.patch) by @dwbump created at 2008-05-09 00:10:57",
    "created_at": "2008-05-09T00:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21006",
    "user": "https://github.com/dwbump"
}
```

Attachment [3051-2.patch](tarball://root/attachments/some-uuid/ticket3051/3051-2.patch) by @dwbump created at 2008-05-09 00:10:57



---

archive/issue_comments_021007.json:
```json
{
    "body": "Attachment [3051-unified-1.patch](tarball://root/attachments/some-uuid/ticket3051/3051-unified-1.patch) by @dwbump created at 2008-05-09 00:11:53",
    "created_at": "2008-05-09T00:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21007",
    "user": "https://github.com/dwbump"
}
```

Attachment [3051-unified-1.patch](tarball://root/attachments/some-uuid/ticket3051/3051-unified-1.patch) by @dwbump created at 2008-05-09 00:11:53



---

archive/issue_comments_021008.json:
```json
{
    "body": "The patch 3051-2.patch is in response to items (1) and (2) of David's report.  I changed Weight -> WeightRingElement, and added some more references. \n\nThe patch 3051-2.patch goes on top of 3051-unifed.patch and 3041-1.patch.\n\nThe patch 3051-unified-1.patch is a single unified patch containing all changes. It thus supercedes 3051-unified.patch.",
    "created_at": "2008-05-09T00:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21008",
    "user": "https://github.com/dwbump"
}
```

The patch 3051-2.patch is in response to items (1) and (2) of David's report.  I changed Weight -> WeightRingElement, and added some more references. 

The patch 3051-2.patch goes on top of 3051-unifed.patch and 3041-1.patch.

The patch 3051-unified-1.patch is a single unified patch containing all changes. It thus supercedes 3051-unified.patch.



---

archive/issue_comments_021009.json:
```json
{
    "body": "This patch 3051-unified-1.patch applied cleanly to 3.0.1 and passes sage -testall. I give this a very positive review. Very nice work. I think Mike Hansen should look at it since it is based on some work he has done or at least knows better than I. However, since it is around the end of the semester, I 'm not sure if he will have time to do that before 3.0.2 is released. So, I changed the summary to \"one positive review\".",
    "created_at": "2008-05-09T10:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21009",
    "user": "https://github.com/wdjoyner"
}
```

This patch 3051-unified-1.patch applied cleanly to 3.0.1 and passes sage -testall. I give this a very positive review. Very nice work. I think Mike Hansen should look at it since it is based on some work he has done or at least knows better than I. However, since it is around the end of the semester, I 'm not sure if he will have time to do that before 3.0.2 is released. So, I changed the summary to "one positive review".



---

archive/issue_comments_021010.json:
```json
{
    "body": "Attachment [3051-3.patch](tarball://root/attachments/some-uuid/ticket3051/3051-3.patch) by @dwbump created at 2008-05-17 04:56:21\n\nGoes on top of 3051-unified-1.patch. Revises the __repr to avoid string notation and adds _coerce_impl methods",
    "created_at": "2008-05-17T04:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21010",
    "user": "https://github.com/dwbump"
}
```

Attachment [3051-3.patch](tarball://root/attachments/some-uuid/ticket3051/3051-3.patch) by @dwbump created at 2008-05-17 04:56:21

Goes on top of 3051-unified-1.patch. Revises the __repr to avoid string notation and adds _coerce_impl methods



---

archive/issue_comments_021011.json:
```json
{
    "body": "Both David Joyner and Mike Hansen disliked the string notation followed in earlier versions of the patch. This has been removed and replaced by Mike's suggestion, `A2(1,1,0)` for example.\n\nAlso, _coerce_impl methods were added to WeylCharacterRing and WeightRing, so that now the two rings can *always* parse their own output.",
    "created_at": "2008-05-17T05:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21011",
    "user": "https://github.com/dwbump"
}
```

Both David Joyner and Mike Hansen disliked the string notation followed in earlier versions of the patch. This has been removed and replaced by Mike's suggestion, `A2(1,1,0)` for example.

Also, _coerce_impl methods were added to WeylCharacterRing and WeightRing, so that now the two rings can *always* parse their own output.



---

archive/issue_comments_021012.json:
```json
{
    "body": "Attachment [3051-unified-2.patch](tarball://root/attachments/some-uuid/ticket3051/3051-unified-2.patch) by @dwbump created at 2008-05-17 14:26:06\n\nUnified patch equivalent to 3051-unified-1.patch plus 3051-3.patch plus 3051-4.patch",
    "created_at": "2008-05-17T14:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21012",
    "user": "https://github.com/dwbump"
}
```

Attachment [3051-unified-2.patch](tarball://root/attachments/some-uuid/ticket3051/3051-unified-2.patch) by @dwbump created at 2008-05-17 14:26:06

Unified patch equivalent to 3051-unified-1.patch plus 3051-3.patch plus 3051-4.patch



---

archive/issue_comments_021013.json:
```json
{
    "body": "I realized that I'd forgotten to revise the doctest in crystals.py after the notational change. The patch 3051-4.patch fixes the doctest. I revised and reposted 3051-unified-2.patch accordingly.",
    "created_at": "2008-05-17T14:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21013",
    "user": "https://github.com/dwbump"
}
```

I realized that I'd forgotten to revise the doctest in crystals.py after the notational change. The patch 3051-4.patch fixes the doctest. I revised and reposted 3051-unified-2.patch accordingly.



---

archive/issue_comments_021014.json:
```json
{
    "body": "Really, or someone should look at this instead of me but to help out a little, I thought I'd at least do some testing. Oddly enough, I had trouble applying it to a newly made clone:\n\n\n```\nwdj@wooster:/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.2.alpha1, Release Date: 2008-05-11                |\n| Type notebook() for the GUI, and license() for information.        |\nLoading SAGE library. Current Mercurial branch is: weyl2\nsage: hg_sage.apply(\"/home/wdj/wdj/sagefiles/3051-unified-2.patch\")\ncd \"/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage\" && hg status\ncd \"/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage\" && hg status\ncd \"/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage\" && hg import   \"/home/wdj/wdj/sagefiles/3051-unified-2.patch\"\napplying /home/wdj/wdj/sagefiles/3051-unified-2.patch\npatching file sage/combinat/crystals/crystals.py\nHunk #1 FAILED at 103\nHunk #2 succeeded at 231 with fuzz 2 (offset 1 line).\n1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/crystals/crystals.py.rej\nfile sage/combinat/root_system/weyl_characters.py already exists\n1 out of 1 hunk FAILED -- saving rejects to file sage/combinat/root_system/weyl_characters.py.rej\nabort: patch failed to apply\nsage:                               \n```\n\n\nThe previous version of this patch applied and  passed sage -testall except for crystal, as you already pointed out.",
    "created_at": "2008-05-17T14:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21014",
    "user": "https://github.com/wdjoyner"
}
```

Really, or someone should look at this instead of me but to help out a little, I thought I'd at least do some testing. Oddly enough, I had trouble applying it to a newly made clone:


```
wdj@wooster:/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.2.alpha1, Release Date: 2008-05-11                |
| Type notebook() for the GUI, and license() for information.        |
Loading SAGE library. Current Mercurial branch is: weyl2
sage: hg_sage.apply("/home/wdj/wdj/sagefiles/3051-unified-2.patch")
cd "/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage" && hg status
cd "/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage" && hg status
cd "/mnt/drive_hda1/sagefiles/sage-3.0.2.alpha0/devel/sage" && hg import   "/home/wdj/wdj/sagefiles/3051-unified-2.patch"
applying /home/wdj/wdj/sagefiles/3051-unified-2.patch
patching file sage/combinat/crystals/crystals.py
Hunk #1 FAILED at 103
Hunk #2 succeeded at 231 with fuzz 2 (offset 1 line).
1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/crystals/crystals.py.rej
file sage/combinat/root_system/weyl_characters.py already exists
1 out of 1 hunk FAILED -- saving rejects to file sage/combinat/root_system/weyl_characters.py.rej
abort: patch failed to apply
sage:                               
```


The previous version of this patch applied and  passed sage -testall except for crystal, as you already pointed out.



---

archive/issue_comments_021015.json:
```json
{
    "body": "You must have had a leftover weyl_characters.py in your directory since I don't think this file is in\nthe repository. At least it's not in sage-3.0.2.alpha0. The patch creates this file.\n\n\n```\n1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/crystals/crystals.py.rej\nfile sage/combinat/root_system/weyl_characters.py already exists\n```\n",
    "created_at": "2008-05-17T18:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21015",
    "user": "https://github.com/dwbump"
}
```

You must have had a leftover weyl_characters.py in your directory since I don't think this file is in
the repository. At least it's not in sage-3.0.2.alpha0. The patch creates this file.


```
1 out of 2 hunks FAILED -- saving rejects to file sage/combinat/crystals/crystals.py.rej
file sage/combinat/root_system/weyl_characters.py already exists
```




---

archive/issue_comments_021016.json:
```json
{
    "body": "Attachment [3051-doctest.patch](tarball://root/attachments/some-uuid/ticket3051/3051-doctest.patch) by @mwhansen created at 2008-05-18 00:05:24",
    "created_at": "2008-05-18T00:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21016",
    "user": "https://github.com/mwhansen"
}
```

Attachment [3051-doctest.patch](tarball://root/attachments/some-uuid/ticket3051/3051-doctest.patch) by @mwhansen created at 2008-05-18 00:05:24



---

archive/issue_comments_021017.json:
```json
{
    "body": "Sorry it's taken so long -- I've been awfully busy this week. I've attached a patch which makes a few minor changes to docstrings / doctests.\n\nApply only the last two patches.",
    "created_at": "2008-05-18T00:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21017",
    "user": "https://github.com/mwhansen"
}
```

Sorry it's taken so long -- I've been awfully busy this week. I've attached a patch which makes a few minor changes to docstrings / doctests.

Apply only the last two patches.



---

archive/issue_comments_021018.json:
```json
{
    "body": "Merged 3051-unified-2.patch and 3051-doctest.patch in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T00:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3051-unified-2.patch and 3051-doctest.patch in Sage 3.0.2.alpha1



---

archive/issue_comments_021019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T00:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3051#issuecomment-21019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
