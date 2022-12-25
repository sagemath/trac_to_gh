# Issue 6105: [with patch, need review] Additions and changes in Group Algebras

archive/issues_006105.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: Group Algebra\n\nAdded helper functions to better exchange character information between gap and Sage and then use those to build a system of idempotent for any group algebra defined over a finite group. Also, made small fixes in the group algebra.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6105\n\n",
    "created_at": "2009-05-21T05:08:16Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "[with patch, need review] Additions and changes in Group Algebras",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6105",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```
Assignee: tbd

Keywords: Group Algebra

Added helper functions to better exchange character information between gap and Sage and then use those to build a system of idempotent for any group algebra defined over a finite group. Also, made small fixes in the group algebra.

Issue created by migration from https://trac.sagemath.org/ticket/6105





---

archive/issue_comments_048670.json:
```json
{
    "body": "Attachment [6105groupAlgebraPT2.patch](tarball://root/attachments/some-uuid/ticket6105/6105groupAlgebraPT2.patch) by jlefebvre created at 2009-05-21 05:33:35\n\nPart 2",
    "created_at": "2009-05-21T05:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48670",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```

Attachment [6105groupAlgebraPT2.patch](tarball://root/attachments/some-uuid/ticket6105/6105groupAlgebraPT2.patch) by jlefebvre created at 2009-05-21 05:33:35

Part 2



---

archive/issue_comments_048671.json:
```json
{
    "body": "Hi Jerome. Are there any special reasons why you use camel case for the following functions?\n* `goodFor`\n* `inCon`\n* `complexGtoS`\n* `charValue`\n* `systemOfIdempotent`\n* `Augmentation`\nI'm just asking, since I'm not at Sage Days 15 so I have no idea why you did so. But I trust that you've read the coding conventions at\n\n\n\nhttp://www.sagemath.org/doc/developer/conventions.html",
    "created_at": "2009-05-21T06:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Hi Jerome. Are there any special reasons why you use camel case for the following functions?
* `goodFor`
* `inCon`
* `complexGtoS`
* `charValue`
* `systemOfIdempotent`
* `Augmentation`
I'm just asking, since I'm not at Sage Days 15 so I have no idea why you did so. But I trust that you've read the coding conventions at



http://www.sagemath.org/doc/developer/conventions.html



---

archive/issue_comments_048672.json:
```json
{
    "body": "Attachment [6105groupAlgebraPT3.patch](tarball://root/attachments/some-uuid/ticket6105/6105groupAlgebraPT3.patch) by jlefebvre created at 2009-05-21 06:28:04\n\nFixed to follow coding convention",
    "created_at": "2009-05-21T06:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48672",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```

Attachment [6105groupAlgebraPT3.patch](tarball://root/attachments/some-uuid/ticket6105/6105groupAlgebraPT3.patch) by jlefebvre created at 2009-05-21 06:28:04

Fixed to follow coding convention



---

archive/issue_comments_048673.json:
```json
{
    "body": "Hi Minh, there was no particular reason. Thanks for pointing out the coding convention to me.",
    "created_at": "2009-05-21T06:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48673",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```

Hi Minh, there was no particular reason. Thanks for pointing out the coding convention to me.



---

archive/issue_comments_048674.json:
```json
{
    "body": "Hey again, I noticed some bugs in my conversion from gap to Sage. I'm going to try to fix it as soon as  I can.",
    "created_at": "2009-05-21T07:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48674",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```

Hey again, I noticed some bugs in my conversion from gap to Sage. I'm going to try to fix it as soon as  I can.



---

archive/issue_comments_048675.json:
```json
{
    "body": "Attachment [6105groupAlgebraPT4.patch](tarball://root/attachments/some-uuid/ticket6105/6105groupAlgebraPT4.patch) by jlefebvre created at 2009-05-21 19:23:12\n\nFix to gap to complex conversion",
    "created_at": "2009-05-21T19:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48675",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```

Attachment [6105groupAlgebraPT4.patch](tarball://root/attachments/some-uuid/ticket6105/6105groupAlgebraPT4.patch) by jlefebvre created at 2009-05-21 19:23:12

Fix to gap to complex conversion



---

archive/issue_comments_048676.json:
```json
{
    "body": "Attachment [6105GroupAlgebraPT5.patch](tarball://root/attachments/some-uuid/ticket6105/6105GroupAlgebraPT5.patch) by jlefebvre created at 2009-06-10 03:17:58\n\nA new patch against sage 4.0.1",
    "created_at": "2009-06-10T03:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48676",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```

Attachment [6105GroupAlgebraPT5.patch](tarball://root/attachments/some-uuid/ticket6105/6105GroupAlgebraPT5.patch) by jlefebvre created at 2009-06-10 03:17:58

A new patch against sage 4.0.1



---

archive/issue_comments_048677.json:
```json
{
    "body": "Here's a silly thing: this patch has never appeared in the list of patches needing review, because that list does a text search in the summary field for \"needs review\", and \"need review\" doesn't show up.",
    "created_at": "2009-06-10T10:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48677",
    "user": "https://github.com/loefflerd"
}
```

Here's a silly thing: this patch has never appeared in the list of patches needing review, because that list does a text search in the summary field for "needs review", and "need review" doesn't show up.



---

archive/issue_comments_048678.json:
```json
{
    "body": "I haven't tried installing this, but here are some comments based on browsing the code. \n\nIt looks like this is excellent functionality, but there are some things I'm not very happy with. \n\n(1) Brutally converting all finite groups into permutation groups will mean we can't generally create an element of the group algebra from an element of the group, which means that most of the basic arithmetic operations that I originally wrote the class for won't work any more. Please don't do this; rather, add more functionality to the basic Group class, or (if absolutely necessary) make GroupAlgebra store both the original group and its permutation form (and the mapping between them).\n\n(2) Many of these docstrings are somewhat confusing; I can't for the life of me work out what the docstring for \"good_for\" is trying to say -- some of it seems to be about the function at hand, some about another unnamed function, and nowhere is it defined what the function actually does.\n\n(3) Lots of these functions need more testing. There are some obvious typos, e.g. in is_noetherian:  \n\n```\nif self.group().is_polycyclic and self.base_ring().is_field():\n```\n\nshould read\n\n```\nif self.group().is_polycyclic() and self.base_ring().is_field():\n```\n\n\nWhen there are lots of different cases handled in a function, it's good to have a test for each case -- the aim is that \"sage -testall\" should test every single line of code in the Sage library, and much of this code simply won't get hit. Then typos like this come out in the wash.\n\n(4) It would be good if the GroupAlgebra class could be incorporated into the reference manual (by adding a line to `sage/doc/en/reference/algebras.rst`). To do this will require lots of formatting changes to the docstrings (e.g. example blocks must look like\n\n```\nEXAMPLE::\n\n    sage: some code\n```\n\nwith two colons and a blank line). This is somewhat orthogonal to your patch and is actually my fault -- when I wrote the group algebra class, I forgot to add it to the reference manual, so it never got updated when we changed to a new and better reference manual compilation system -- but it seems a shame to make the problem worse by adding many new functions with new docstrings that are not ReSTified.\n\nMuch of this is cosmetic, but (1) is a big issue -- I don't think we can consider merging this into Sage if it's going to break creating elements of group algebras for most of our finite group classes. So I'm changing this back to \"needs work\"; sorry.",
    "created_at": "2009-06-14T11:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48678",
    "user": "https://github.com/loefflerd"
}
```

I haven't tried installing this, but here are some comments based on browsing the code. 

It looks like this is excellent functionality, but there are some things I'm not very happy with. 

(1) Brutally converting all finite groups into permutation groups will mean we can't generally create an element of the group algebra from an element of the group, which means that most of the basic arithmetic operations that I originally wrote the class for won't work any more. Please don't do this; rather, add more functionality to the basic Group class, or (if absolutely necessary) make GroupAlgebra store both the original group and its permutation form (and the mapping between them).

(2) Many of these docstrings are somewhat confusing; I can't for the life of me work out what the docstring for "good_for" is trying to say -- some of it seems to be about the function at hand, some about another unnamed function, and nowhere is it defined what the function actually does.

(3) Lots of these functions need more testing. There are some obvious typos, e.g. in is_noetherian:  

```
if self.group().is_polycyclic and self.base_ring().is_field():
```

should read

```
if self.group().is_polycyclic() and self.base_ring().is_field():
```


When there are lots of different cases handled in a function, it's good to have a test for each case -- the aim is that "sage -testall" should test every single line of code in the Sage library, and much of this code simply won't get hit. Then typos like this come out in the wash.

(4) It would be good if the GroupAlgebra class could be incorporated into the reference manual (by adding a line to `sage/doc/en/reference/algebras.rst`). To do this will require lots of formatting changes to the docstrings (e.g. example blocks must look like

```
EXAMPLE::

    sage: some code
```

with two colons and a blank line). This is somewhat orthogonal to your patch and is actually my fault -- when I wrote the group algebra class, I forgot to add it to the reference manual, so it never got updated when we changed to a new and better reference manual compilation system -- but it seems a shame to make the problem worse by adding many new functions with new docstrings that are not ReSTified.

Much of this is cosmetic, but (1) is a big issue -- I don't think we can consider merging this into Sage if it's going to break creating elements of group algebras for most of our finite group classes. So I'm changing this back to "needs work"; sorry.



---

archive/issue_comments_048679.json:
```json
{
    "body": "Thanks for the feed back!\nI've started to attack (1), it looks like I needed to convert group to their permutation group representation to deal with AbelianGroup class. I couldn't fix some of the issues I ran into, so created tracs about them; 6291, 6292, 6293.",
    "created_at": "2009-06-15T04:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48679",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```

Thanks for the feed back!
I've started to attack (1), it looks like I needed to convert group to their permutation group representation to deal with AbelianGroup class. I couldn't fix some of the issues I ran into, so created tracs about them; 6291, 6292, 6293.



---

archive/issue_comments_048680.json:
```json
{
    "body": "Replying to [comment:6 jlefebvre]:\n> it looks like I needed to convert group to their permutation group representation to deal with AbelianGroup class.\n\nI would be *extremely* surprised if this were the best way of doing it. \n\nBy the way, there are some major changes pending to the abelian group implementation -- the plan is to implement them directly in Sage via the machinery we already have for linear algebra over ZZ, using William Stein's work at ticket #5882, rather than relying on Gap. (This is for several reasons, one of which being the speed penalty of communicating with Gap via the pexpect interface.)\n\nDavid",
    "created_at": "2009-06-15T09:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48680",
    "user": "https://github.com/loefflerd"
}
```

Replying to [comment:6 jlefebvre]:
> it looks like I needed to convert group to their permutation group representation to deal with AbelianGroup class.

I would be *extremely* surprised if this were the best way of doing it. 

By the way, there are some major changes pending to the abelian group implementation -- the plan is to implement them directly in Sage via the machinery we already have for linear algebra over ZZ, using William Stein's work at ticket #5882, rather than relying on Gap. (This is for several reasons, one of which being the speed penalty of communicating with Gap via the pexpect interface.)

David



---

archive/issue_comments_048681.json:
```json
{
    "body": "> By the way, there are some major changes pending to the abelian group implementation --\n>  the plan is to implement them directly in Sage via the machinery we already have for \n> linear algebra over ZZ, using William Stein's work at ticket #5882, \n\nAnd amazingly, I will have time to work on this soon! (I claim.)",
    "created_at": "2009-06-15T12:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6105#issuecomment-48681",
    "user": "https://github.com/williamstein"
}
```

> By the way, there are some major changes pending to the abelian group implementation --
>  the plan is to implement them directly in Sage via the machinery we already have for 
> linear algebra over ZZ, using William Stein's work at ticket #5882, 

And amazingly, I will have time to work on this soon! (I claim.)



---

archive/issue_events_014357.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6105#event-14357"
}
```



---

archive/issue_events_014358.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6105#event-14358"
}
```



---

archive/issue_events_014359.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6105#event-14359"
}
```



---

archive/issue_events_014360.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6105#event-14360"
}
```



---

archive/issue_events_014361.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6105#event-14361"
}
```



---

archive/issue_events_014362.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6105#event-14362"
}
```



---

archive/issue_events_014363.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6105",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6105#event-14363"
}
```
