# Issue 5002: CrystalOfTableaux call method breaks on legitimate data

archive/issues_005002.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n```\nsage: C = CrystalOfTableaux(['B',2],shape=[3]) \nsage: C(rows=[[1,1,0]])\n```\n\nraises an exception though this is a legitimate B2 tableaux. This was\nanalyzed by Anne Schilling and others in this thread:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/cb02f961c41947e2?hl=en\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5002\n\n",
    "created_at": "2009-01-17T17:03:36Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "CrystalOfTableaux call method breaks on legitimate data",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5002",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

```
sage: C = CrystalOfTableaux(['B',2],shape=[3]) 
sage: C(rows=[[1,1,0]])
```

raises an exception though this is a legitimate B2 tableaux. This was
analyzed by Anne Schilling and others in this thread:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/cb02f961c41947e2?hl=en


Issue created by migration from https://trac.sagemath.org/ticket/5002





---

archive/issue_events_011562.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-17T17:06:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5002#event-11562"
}
```



---

archive/issue_comments_038073.json:
```json
{
    "body": "Changing assignee from @mwhansen to @anneschilling.",
    "created_at": "2009-04-02T22:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38073",
    "user": "https://github.com/anneschilling"
}
```

Changing assignee from @mwhansen to @anneschilling.



---

archive/issue_comments_038074.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-02T22:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38074",
    "user": "https://github.com/anneschilling"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038075.json:
```json
{
    "body": "Attachment [ticket-5002.patch](tarball://root/attachments/some-uuid/ticket5002/ticket-5002.patch) by @anneschilling created at 2009-04-05 03:28:01",
    "created_at": "2009-04-05T03:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38075",
    "user": "https://github.com/anneschilling"
}
```

Attachment [ticket-5002.patch](tarball://root/attachments/some-uuid/ticket5002/ticket-5002.patch) by @anneschilling created at 2009-04-05 03:28:01



---

archive/issue_comments_038076.json:
```json
{
    "body": "The patch depends on 4549 and 5308.",
    "created_at": "2009-04-06T20:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38076",
    "user": "https://github.com/anneschilling"
}
```

The patch depends on 4549 and 5308.



---

archive/issue_comments_038077.json:
```json
{
    "body": "* fixes the bug when legitimate tableau of type B is entered\n* allows to enter several shapes for tableaux (which will be\nessential for the Kirillov-Reshetikhin crystals later)\n* fixes a small bug in partitions when adding a box to the\nempty partition \n* fixes errors in comparison of the elements in crystal of letters",
    "created_at": "2009-04-07T19:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38077",
    "user": "https://github.com/anneschilling"
}
```

* fixes the bug when legitimate tableau of type B is entered
* allows to enter several shapes for tableaux (which will be
essential for the Kirillov-Reshetikhin crystals later)
* fixes a small bug in partitions when adding a box to the
empty partition 
* fixes errors in comparison of the elements in crystal of letters



---

archive/issue_comments_038078.json:
```json
{
    "body": "This patch fixes three bugs.\n\nFirst, there is the bug originally reported in this ticket.\nSecond, there is the bug described at\nhttp://groups.google.com/group/sage-combinat-devel/msg/bce932c675b8b04a?hl=en\nThird, it fixes an exception on \n`Partition([]).outside_corners()`.\n\nIn addition there are a lot of documentation improvements.\n\nThe new class CrystalOfWords needs a docstring. Otherwise I found no problems.\n\nThe patch does not change the effect of `sage --testall`.\n\nThe patch applies cleanly on sage-3.4.1.rc1.\n\nPatch summary:\n\n```\nAdds index_set as a lazy_attribute method in class Crystal.\nRemoves class AffineCrystal which was prematurely implemented\nReplaces the cmp_elements method => lt_elements in ClassicalCrystalOfLetters.\nImplements __ne__, __lt__, __ge__ methods in class Letter.\nProperly indents docstrings for TensorProductOfCrystals.\nNew class CrystalOfWords.\nFullTensorProductOfCrystals inherits from CrystalOfWords.\ncall method of FullTensorProductOfCrystals is taken down.\nCrystalOfTableaux inherits from CrystalOfWords.\nDocstring revision for CrystalOfTableaux.\nCrystalOfTableaux __init__ method allows multiple shapes.\nCrystalOfTableaux gets new methods cartan_type and module_generator\nCrystalOfTableauxElement __init__ revisions\n```",
    "created_at": "2009-04-08T15:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38078",
    "user": "https://github.com/dwbump"
}
```

This patch fixes three bugs.

First, there is the bug originally reported in this ticket.
Second, there is the bug described at
http://groups.google.com/group/sage-combinat-devel/msg/bce932c675b8b04a?hl=en
Third, it fixes an exception on 
`Partition([]).outside_corners()`.

In addition there are a lot of documentation improvements.

The new class CrystalOfWords needs a docstring. Otherwise I found no problems.

The patch does not change the effect of `sage --testall`.

The patch applies cleanly on sage-3.4.1.rc1.

Patch summary:

```
Adds index_set as a lazy_attribute method in class Crystal.
Removes class AffineCrystal which was prematurely implemented
Replaces the cmp_elements method => lt_elements in ClassicalCrystalOfLetters.
Implements __ne__, __lt__, __ge__ methods in class Letter.
Properly indents docstrings for TensorProductOfCrystals.
New class CrystalOfWords.
FullTensorProductOfCrystals inherits from CrystalOfWords.
call method of FullTensorProductOfCrystals is taken down.
CrystalOfTableaux inherits from CrystalOfWords.
Docstring revision for CrystalOfTableaux.
CrystalOfTableaux __init__ method allows multiple shapes.
CrystalOfTableaux gets new methods cartan_type and module_generator
CrystalOfTableauxElement __init__ revisions
```



---

archive/issue_events_011563.json:
```json
{
    "actor": "https://github.com/dwbump",
    "created_at": "2009-04-08T15:15:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5002#event-11563"
}
```



---

archive/issue_events_011564.json:
```json
{
    "actor": "https://github.com/dwbump",
    "created_at": "2009-04-08T15:15:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5002#event-11564"
}
```



---

archive/issue_comments_038079.json:
```json
{
    "body": "Added docstring to CrystalOfWords as requested by Dan Bump.",
    "created_at": "2009-04-08T17:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38079",
    "user": "https://github.com/anneschilling"
}
```

Added docstring to CrystalOfWords as requested by Dan Bump.



---

archive/issue_comments_038080.json:
```json
{
    "body": "Hi, \n\nafter some discussion about lazy attributed at SD 14 with Nicolas the consensus at least from the non-combinat developers was that lazy attributes should be avoided for public API data structures. If you want to access the index_set of a crystal we see no reason for the inconsistency **A.data_set** while everywhere else in Sage it would be **A.data_set()**. Caching can be done in some other ways.\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-08T19:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi, 

after some discussion about lazy attributed at SD 14 with Nicolas the consensus at least from the non-combinat developers was that lazy attributes should be avoided for public API data structures. If you want to access the index_set of a crystal we see no reason for the inconsistency **A.data_set** while everywhere else in Sage it would be **A.data_set()**. Caching can be done in some other ways.


Cheers,

Michael



---

archive/issue_comments_038081.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> Hi, \n> \n> after some discussion about lazy attributed at SD 14 with \n> Nicolas the consensus at least from the non-combinat \n> developers was that lazy attributes should be avoided for \n> public API data structures. If you want to access the \n> index_set of a crystal we see no reason for the \n> inconsistency **A.data_set** while everywhere else \n> in Sage it would be **A.data_set()**. Caching can be done \n> in some other ways.\n\n\n+10   I very strongly agree with this.  The point isn't to argue about whether lazy attributes are good or bad, but that using them is inconsistent with hundreds of thousands of lines of existing Sage code, and we're definitely not going to change all that code.  For consistency, do not use them in the Sage library for \"user facing\" code.",
    "created_at": "2009-04-08T19:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38081",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:8 mabshoff]:
> Hi, 
> 
> after some discussion about lazy attributed at SD 14 with 
> Nicolas the consensus at least from the non-combinat 
> developers was that lazy attributes should be avoided for 
> public API data structures. If you want to access the 
> index_set of a crystal we see no reason for the 
> inconsistency **A.data_set** while everywhere else 
> in Sage it would be **A.data_set()**. Caching can be done 
> in some other ways.


+10   I very strongly agree with this.  The point isn't to argue about whether lazy attributes are good or bad, but that using them is inconsistent with hundreds of thousands of lines of existing Sage code, and we're definitely not going to change all that code.  For consistency, do not use them in the Sage library for "user facing" code.



---

archive/issue_comments_038082.json:
```json
{
    "body": "Peace. The lazy_attribute here is just a temporary workaround. Anne precisely did send an e-mail\nto the mailing list 2 days ago asking for confirmation for changing it systematically to a method\nin all the crystal library. This will come as a subsequent patch.\n\nRefactoring all the crap in the combinatorics code will take a while. No need to jump on every occasion to repeat the same arguments. We have heard them, and fully taken points for them.\n\nThat being said, I still think that lazy attributes have their role to play in some well localized places in the user interface. I will run a complete discussion about this when time is ready for it. And the final code will follow whatever consensus emerges.",
    "created_at": "2009-04-08T19:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38082",
    "user": "https://github.com/nthiery"
}
```

Peace. The lazy_attribute here is just a temporary workaround. Anne precisely did send an e-mail
to the mailing list 2 days ago asking for confirmation for changing it systematically to a method
in all the crystal library. This will come as a subsequent patch.

Refactoring all the crap in the combinatorics code will take a while. No need to jump on every occasion to repeat the same arguments. We have heard them, and fully taken points for them.

That being said, I still think that lazy attributes have their role to play in some well localized places in the user interface. I will run a complete discussion about this when time is ready for it. And the final code will follow whatever consensus emerges.



---

archive/issue_comments_038083.json:
```json
{
    "body": "Can the patch be merged (and this issue sorted out later) or does it need to be revised to avoid lazy_attributes?\n\nI suppose this is Michael's call, so this question is addressed mainly to him.",
    "created_at": "2009-04-08T23:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38083",
    "user": "https://github.com/dwbump"
}
```

Can the patch be merged (and this issue sorted out later) or does it need to be revised to avoid lazy_attributes?

I suppose this is Michael's call, so this question is addressed mainly to him.



---

archive/issue_comments_038084.json:
```json
{
    "body": "Replying to [comment:11 bump]:\n> Can the patch be merged (and this issue sorted out later) or does it need to be revised to avoid lazy_attributes?\n> \n> I suppose this is Michael's call, so this question is addressed mainly to him.\n\n\nI am reluctant to merge any large patch that is not on my blocker list at this point in general, but I would greatly prefer if the lazy_attribute issue in this patch was fixed. The main reason is that otherwise some of the API in crystals will be different in 3.4.1 until the fix is merged and there is no clean way to handle this. I think since this is a combinat patch, i.e. no Cython, it is relatively low risk. But we are at the moment sitting around trying to get all blockers resolved and put out 3.4.1.rc2, so if the fix appears it should appear quickly. \n\n`@`Nicolas: I did not see the patch by Anne, but I will look it up.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T01:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:11 bump]:
> Can the patch be merged (and this issue sorted out later) or does it need to be revised to avoid lazy_attributes?
> 
> I suppose this is Michael's call, so this question is addressed mainly to him.


I am reluctant to merge any large patch that is not on my blocker list at this point in general, but I would greatly prefer if the lazy_attribute issue in this patch was fixed. The main reason is that otherwise some of the API in crystals will be different in 3.4.1 until the fix is merged and there is no clean way to handle this. I think since this is a combinat patch, i.e. no Cython, it is relatively low risk. But we are at the moment sitting around trying to get all blockers resolved and put out 3.4.1.rc2, so if the fix appears it should appear quickly. 

`@`Nicolas: I did not see the patch by Anne, but I will look it up.

Cheers,

Michael



---

archive/issue_comments_038085.json:
```json
{
    "body": "removed reference to lazy attribute",
    "created_at": "2009-04-09T07:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38085",
    "user": "https://github.com/anneschilling"
}
```

removed reference to lazy attribute



---

archive/issue_comments_038086.json:
```json
{
    "body": "Attachment [crystal-5002-track.patch](tarball://root/attachments/some-uuid/ticket5002/crystal-5002-track.patch) by @anneschilling created at 2009-04-09 07:04:39\n\nI removed the reference to lazy attribute. I hope it is now ok to be integrated.\nIn the process I also had to touch fast_crystals.py and spins.py.",
    "created_at": "2009-04-09T07:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38086",
    "user": "https://github.com/anneschilling"
}
```

Attachment [crystal-5002-track.patch](tarball://root/attachments/some-uuid/ticket5002/crystal-5002-track.patch) by @anneschilling created at 2009-04-09 07:04:39

I removed the reference to lazy attribute. I hope it is now ok to be integrated.
In the process I also had to touch fast_crystals.py and spins.py.



---

archive/issue_comments_038087.json:
```json
{
    "body": "Merged crystal-5002-track.patch only in Sage 3.4.1.rc2. \n\nI did reread the changes Anne made and they look good to me. Doctests do pass, too.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T07:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged crystal-5002-track.patch only in Sage 3.4.1.rc2. 

I did reread the changes Anne made and they look good to me. Doctests do pass, too.

Cheers,

Michael



---

archive/issue_comments_038088.json:
```json
{
    "body": "Merged crystal-5002-track.patch only in Sage 3.4.1.rc2.\n\nI did reread the changes Anne made and they look good to me. Doctests do pass, too. And this time I closed the ticket, too :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T07:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38088",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged crystal-5002-track.patch only in Sage 3.4.1.rc2.

I did reread the changes Anne made and they look good to me. Doctests do pass, too. And this time I closed the ticket, too :)

Cheers,

Michael



---

archive/issue_comments_038089.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T07:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5002#issuecomment-38089",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011565.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-09T07:22:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5002",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5002#event-11565"
}
```
