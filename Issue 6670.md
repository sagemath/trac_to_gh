# Issue 6670: [with patch, needs work] Port group algebras to the current coercion system

archive/issues_006670.json:
```json
{
    "body": "Assignee: mraum\n\nThis upgrades the group algebras to the current coercion system and fixes some issues of multiplication of group algebras A and B, satisfying A == B but not admitting coercion of elements.\nThis depends on #6669, which concerns homomorphisms from matrix group to other objects.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6670\n\n",
    "created_at": "2009-08-03T20:41:36Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "[with patch, needs work] Port group algebras to the current coercion system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6670",
    "user": "mraum"
}
```
Assignee: mraum

This upgrades the group algebras to the current coercion system and fixes some issues of multiplication of group algebras A and B, satisfying A == B but not admitting coercion of elements.
This depends on #6669, which concerns homomorphisms from matrix group to other objects.

Issue created by migration from https://trac.sagemath.org/ticket/6670





---

archive/issue_comments_054764.json:
```json
{
    "body": "Attachment [trac-6670-group_algebra.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra.patch) by mraum created at 2009-08-03 20:42:52",
    "created_at": "2009-08-03T20:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54764",
    "user": "mraum"
}
```

Attachment [trac-6670-group_algebra.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra.patch) by mraum created at 2009-08-03 20:42:52



---

archive/issue_comments_054765.json:
```json
{
    "body": "Attachment [trac-6670-group_algebra-2.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-2.patch) by mraum created at 2009-10-22 16:46:17\n\nThis is a rebase to 4.1.2",
    "created_at": "2009-10-22T16:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54765",
    "user": "mraum"
}
```

Attachment [trac-6670-group_algebra-2.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-2.patch) by mraum created at 2009-10-22 16:46:17

This is a rebase to 4.1.2



---

archive/issue_comments_054766.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-22T16:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54766",
    "user": "mraum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054767.json:
```json
{
    "body": "A patch for #6669 has been uploaded. This patch depends on it.",
    "created_at": "2009-10-22T16:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54767",
    "user": "mraum"
}
```

A patch for #6669 has been uploaded. This patch depends on it.



---

archive/issue_comments_054768.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-20T05:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54768",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054769.json:
```json
{
    "body": "There's a lot of new code here, but it all looks good, and the doctests are fine too. \n\nGiven the amount of category code that went into 4.3, we should make sure all tests pass when applied against that as well. (I tested against 4.2.)",
    "created_at": "2009-11-20T05:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54769",
    "user": "@robertwb"
}
```

There's a lot of new code here, but it all looks good, and the doctests are fine too. 

Given the amount of category code that went into 4.3, we should make sure all tests pass when applied against that as well. (I tested against 4.2.)



---

archive/issue_comments_054770.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-29T07:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54770",
    "user": "@mwhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_054771.json:
```json
{
    "body": "Needs some work/rebasing for 4.3",
    "created_at": "2009-11-29T07:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54771",
    "user": "@mwhansen"
}
```

Needs some work/rebasing for 4.3



---

archive/issue_comments_054772.json:
```json
{
    "body": "Attachment [trac-6670-group_algebra-3.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-3.patch) by mraum created at 2009-12-01 16:46:12\n\nThis is a rebase to 4.3alpha0 .",
    "created_at": "2009-12-01T16:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54772",
    "user": "mraum"
}
```

Attachment [trac-6670-group_algebra-3.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-3.patch) by mraum created at 2009-12-01 16:46:12

This is a rebase to 4.3alpha0 .



---

archive/issue_comments_054773.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-01T16:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54773",
    "user": "mraum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054774.json:
```json
{
    "body": "\n```\n\tsage -t  devel/sage-main/sage/modular/modsym/space.py # Segfault\n\tsage -t  devel/sage-main/sage/algebras/group_algebra.py # 5 doctests failed\n\tsage -t  devel/sage-main/sage/interfaces/sage0.py # 1 doctests failed\n```\n",
    "created_at": "2010-01-20T09:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54774",
    "user": "@robertwb"
}
```


```
	sage -t  devel/sage-main/sage/modular/modsym/space.py # Segfault
	sage -t  devel/sage-main/sage/algebras/group_algebra.py # 5 doctests failed
	sage -t  devel/sage-main/sage/interfaces/sage0.py # 1 doctests failed
```




---

archive/issue_comments_054775.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T09:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54775",
    "user": "@robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054776.json:
```json
{
    "body": "Attachment [trac-6670-group_algebra-4.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-4.patch) by mraum created at 2010-01-21 10:25:42\n\nThis applies cleanly to a fresh 4.3.1",
    "created_at": "2010-01-21T10:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54776",
    "user": "mraum"
}
```

Attachment [trac-6670-group_algebra-4.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-4.patch) by mraum created at 2010-01-21 10:25:42

This applies cleanly to a fresh 4.3.1



---

archive/issue_comments_054777.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-21T10:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54777",
    "user": "mraum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054778.json:
```json
{
    "body": "I'm hoping to take a look at this, but if someone else has time soon and wants to beat me to it, go for it.",
    "created_at": "2010-02-15T19:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54778",
    "user": "@roed314"
}
```

I'm hoping to take a look at this, but if someone else has time soon and wants to beat me to it, go for it.



---

archive/issue_comments_054779.json:
```json
{
    "body": "-- This patch does not apply on sage 4.3.3. Mercurial error message :\n\napplying trac-6670-group_algebra-4.patch\npatching file sage/algebras/group_algebra.py\nHunk #1 FAILED at 27\nHunk #7 succeeded at 358 with fuzz 2 (offset 9 lines).\nHunk #8 FAILED at 361\n2 out of 10 hunks FAILED -- saving rejects to file sage/algebras/group_algebra.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac-6670-group_algebra-4.patch\n\n-- You may want to have a look at the following related bug :\n\nsage: G= SymmetricGroup(5); x, y= G.gens()\nsage: A= GroupAlgebra(G)\nsage: A( A(x) )\n\n...fails. This bug may or may not be automatically fixed by your patch.\n\n-- The docstring on line 367 of group_algebra.py mentions GroupAlgebra.__call__(), even though this method has been suppressed.",
    "created_at": "2010-02-26T17:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54779",
    "user": "pierre"
}
```

-- This patch does not apply on sage 4.3.3. Mercurial error message :

applying trac-6670-group_algebra-4.patch
patching file sage/algebras/group_algebra.py
Hunk #1 FAILED at 27
Hunk #7 succeeded at 358 with fuzz 2 (offset 9 lines).
Hunk #8 FAILED at 361
2 out of 10 hunks FAILED -- saving rejects to file sage/algebras/group_algebra.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-6670-group_algebra-4.patch

-- You may want to have a look at the following related bug :

sage: G= SymmetricGroup(5); x, y= G.gens()
sage: A= GroupAlgebra(G)
sage: A( A(x) )

...fails. This bug may or may not be automatically fixed by your patch.

-- The docstring on line 367 of group_algebra.py mentions GroupAlgebra.__call__(), even though this method has been suppressed.



---

archive/issue_comments_054780.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-26T17:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54780",
    "user": "pierre"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054781.json:
```json
{
    "body": "I spent quite a while rebasing this to 4.5.alpha1. I will upload the rebased patch; but I was disappointed to find that there is still a serious issue that needs to be addressed.\n\nThe problem is that unpickling elements of group algebras created using the old code fails; you can't replace a class name with a function name and expect it to unpickle seamlessly. It ends up expecting `sage.algebras.group_algebra.GroupAlgebraElement` to be a class which can just be filled in with the pickled `__dict__` values, not a callable. This is what I get if I pickle a group algebra element without the patch, apply the patch and try to unpickle:\n\n```\nsage: load(\"/home/masiao/gpalg.sobj\")\n---------------------------------------------------------------------------\nUnpicklingError                           Traceback (most recent call last)\n\n/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/algebras/<ipython console> in <module>()\n\n/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7577)()\n\n/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)()\n\nUnpicklingError: NEWOBJ class argument isn't a type object\n```\n",
    "created_at": "2010-07-03T09:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54781",
    "user": "@loefflerd"
}
```

I spent quite a while rebasing this to 4.5.alpha1. I will upload the rebased patch; but I was disappointed to find that there is still a serious issue that needs to be addressed.

The problem is that unpickling elements of group algebras created using the old code fails; you can't replace a class name with a function name and expect it to unpickle seamlessly. It ends up expecting `sage.algebras.group_algebra.GroupAlgebraElement` to be a class which can just be filled in with the pickled `__dict__` values, not a callable. This is what I get if I pickle a group algebra element without the patch, apply the patch and try to unpickle:

```
sage: load("/home/masiao/gpalg.sobj")
---------------------------------------------------------------------------
UnpicklingError                           Traceback (most recent call last)

/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/algebras/<ipython console> in <module>()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7577)()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)()

UnpicklingError: NEWOBJ class argument isn't a type object
```




---

archive/issue_comments_054782.json:
```json
{
    "body": "Attachment [trac-6670-group_algebra-5.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-5.patch) by @loefflerd created at 2010-07-03 09:53:00\n\nApply only this -- rebased against 4.5.alpha1 and docstrings ReSTified",
    "created_at": "2010-07-03T09:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54782",
    "user": "@loefflerd"
}
```

Attachment [trac-6670-group_algebra-5.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-5.patch) by @loefflerd created at 2010-07-03 09:53:00

Apply only this -- rebased against 4.5.alpha1 and docstrings ReSTified



---

archive/issue_comments_054783.json:
```json
{
    "body": "Attachment [trac-6670-group_algebra-6.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-6.patch) by mraum created at 2011-03-23 01:33:50",
    "created_at": "2011-03-23T01:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54783",
    "user": "mraum"
}
```

Attachment [trac-6670-group_algebra-6.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-6.patch) by mraum created at 2011-03-23 01:33:50



---

archive/issue_comments_054784.json:
```json
{
    "body": "Attachment [trac-6670-group_algebra-7.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-7.patch) by mraum created at 2011-03-23 01:34:04",
    "created_at": "2011-03-23T01:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54784",
    "user": "mraum"
}
```

Attachment [trac-6670-group_algebra-7.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-group_algebra-7.patch) by mraum created at 2011-03-23 01:34:04



---

archive/issue_comments_054785.json:
```json
{
    "body": "I added a completely new file containing the new implementation. The old one is deprecated now, but it still exists and pickling works. William suggested to remove the old implementation in 5.0, which I will open a ticket for as soon as this ticket is merged.",
    "created_at": "2011-03-23T01:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54785",
    "user": "mraum"
}
```

I added a completely new file containing the new implementation. The old one is deprecated now, but it still exists and pickling works. William suggested to remove the old implementation in 5.0, which I will open a ticket for as soon as this ticket is merged.



---

archive/issue_comments_054786.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-23T01:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54786",
    "user": "mraum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054787.json:
```json
{
    "body": "For the bot:\n\nApply trac-6670-group_algebra-6.patch, trac-6670-group_algebra-7.patch",
    "created_at": "2011-06-25T08:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54787",
    "user": "@fchapoton"
}
```

For the bot:

Apply trac-6670-group_algebra-6.patch, trac-6670-group_algebra-7.patch



---

archive/issue_comments_054788.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-07-22T20:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54788",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054789.json:
```json
{
    "body": "Some minor comments:\n\n- The first line of the new file is redundant: \"Group algebra of a group\".  Maybe it should just be \"Group algebras\"?\n- The new file should be added to the reference manual, by adding an appropriate line to `sage/doc/en/reference/algebras.rst`.\n\nMore interesting:\n\n- Can you implement coercion from R[H] to R[G] if H is a subgroup of G, or more generally from R[H] to S[G] if there is a coercion from H to G and from R to S?  Then coercing from the base ring R to R[G] would just be the special case where R=S and H is the trivial group.\n\nA more important issue: I'm not sure that I agree with the implementation.  I would have it inherit from `CombinatorialFreeModule`, and then unique representation is built in nicely so you don't have to cache the results as you do now.  You can also implement the Hopf algebra structure on the group algebra pretty easily.  For reference, you should look at the files\n\n- `sage/categories/examples/hopf_algebras_with_basis.py` for a simple (not very full-featured) implementation of group algebras.\n\n- `sage/algebras/steenrod/steenrod_algebra.py` for the implementation of the Steenrod algebra, including all of its Hopf algebra structure, inheriting from `CombinatorialFreeModule`.  This has a lot of things you don't need, but if you want to base the implementation on the first file, or if you want to modify the print representation of elements (which I recommend), you might be able to use this one to help fill in some details.",
    "created_at": "2011-07-22T20:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54789",
    "user": "@jhpalmieri"
}
```

Some minor comments:

- The first line of the new file is redundant: "Group algebra of a group".  Maybe it should just be "Group algebras"?
- The new file should be added to the reference manual, by adding an appropriate line to `sage/doc/en/reference/algebras.rst`.

More interesting:

- Can you implement coercion from R[H] to R[G] if H is a subgroup of G, or more generally from R[H] to S[G] if there is a coercion from H to G and from R to S?  Then coercing from the base ring R to R[G] would just be the special case where R=S and H is the trivial group.

A more important issue: I'm not sure that I agree with the implementation.  I would have it inherit from `CombinatorialFreeModule`, and then unique representation is built in nicely so you don't have to cache the results as you do now.  You can also implement the Hopf algebra structure on the group algebra pretty easily.  For reference, you should look at the files

- `sage/categories/examples/hopf_algebras_with_basis.py` for a simple (not very full-featured) implementation of group algebras.

- `sage/algebras/steenrod/steenrod_algebra.py` for the implementation of the Steenrod algebra, including all of its Hopf algebra structure, inheriting from `CombinatorialFreeModule`.  This has a lot of things you don't need, but if you want to base the implementation on the first file, or if you want to modify the print representation of elements (which I recommend), you might be able to use this one to help fill in some details.



---

archive/issue_comments_054790.json:
```json
{
    "body": "Here's a new version, which makes the changes I suggested, and also adds some documentation at the top of the file.  I think I preserved all of the tests from the previous version, so we're not losing any functionality.  There are some new things, like an antipode and a comultiplication for elements.",
    "created_at": "2011-07-28T22:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54790",
    "user": "@jhpalmieri"
}
```

Here's a new version, which makes the changes I suggested, and also adds some documentation at the top of the file.  I think I preserved all of the tests from the previous version, so we're not losing any functionality.  There are some new things, like an antipode and a comultiplication for elements.



---

archive/issue_comments_054791.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-07-28T22:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54791",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054792.json:
```json
{
    "body": "Attachment [trac_6670-jhp.patch](tarball://root/attachments/some-uuid/ticket6670/trac_6670-jhp.patch) by @jhpalmieri created at 2011-07-28 22:46:49",
    "created_at": "2011-07-28T22:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54792",
    "user": "@jhpalmieri"
}
```

Attachment [trac_6670-jhp.patch](tarball://root/attachments/some-uuid/ticket6670/trac_6670-jhp.patch) by @jhpalmieri created at 2011-07-28 22:46:49



---

archive/issue_comments_054793.json:
```json
{
    "body": "I'm afraid the new version is quite similar to the original (though much better), so that I wouldn't be a legitimate reviewer. On the other hand, since the changes that you introduced are located in some function that you added I could review this part, as soon as I am back from holidays and you could review the other part. Do you think this is a legitimate solution?\n\nOne thing: The functor needs to be modified, using the new apply methods, that are available thanks to Simon's work. I will do this, if you don't do it first.",
    "created_at": "2011-07-29T16:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54793",
    "user": "mraum"
}
```

I'm afraid the new version is quite similar to the original (though much better), so that I wouldn't be a legitimate reviewer. On the other hand, since the changes that you introduced are located in some function that you added I could review this part, as soon as I am back from holidays and you could review the other part. Do you think this is a legitimate solution?

One thing: The functor needs to be modified, using the new apply methods, that are available thanks to Simon's work. I will do this, if you don't do it first.



---

archive/issue_comments_054794.json:
```json
{
    "body": "I think it is important to note that on #11318 it is suggested unifying GroupAlgebra(G, A) and G.algebra(A). But I think we should still get this patch into Sage to have at least some more modern construction until we finally have the implementation anticipated in #11318.",
    "created_at": "2011-07-31T19:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54794",
    "user": "mraum"
}
```

I think it is important to note that on #11318 it is suggested unifying GroupAlgebra(G, A) and G.algebra(A). But I think we should still get this patch into Sage to have at least some more modern construction until we finally have the implementation anticipated in #11318.



---

archive/issue_comments_054795.json:
```json
{
    "body": "Attachment [trac-6670-functors.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-functors.patch) by mraum created at 2011-07-31 21:59:44\n\nI attached a patch that changes the way functors are called.\n\nAlso I reviewed the parts that you implemented. That is, the transition to CombinatorialFreeModule. I would give this a positive review. So if you agree with the procedure that I described above and are fine with the rest of the code you can give this a positive review as a whole.",
    "created_at": "2011-07-31T21:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54795",
    "user": "mraum"
}
```

Attachment [trac-6670-functors.patch](tarball://root/attachments/some-uuid/ticket6670/trac-6670-functors.patch) by mraum created at 2011-07-31 21:59:44

I attached a patch that changes the way functors are called.

Also I reviewed the parts that you implemented. That is, the transition to CombinatorialFreeModule. I would give this a positive review. So if you agree with the procedure that I described above and are fine with the rest of the code you can give this a positive review as a whole.



---

archive/issue_comments_054796.json:
```json
{
    "body": "Looks good to me.  The point about #11318 is a good one, although I don't like the way elements of `G.algebra(R)` are printed, compared to elements of `GroupAlgebra(G,R)`.",
    "created_at": "2011-08-02T16:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54796",
    "user": "@jhpalmieri"
}
```

Looks good to me.  The point about #11318 is a good one, although I don't like the way elements of `G.algebra(R)` are printed, compared to elements of `GroupAlgebra(G,R)`.



---

archive/issue_comments_054797.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-02T16:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54797",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054798.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-08-18T22:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6670#issuecomment-54798",
    "user": "@jdemeyer"
}
```

Resolution: fixed
