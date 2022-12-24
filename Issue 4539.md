# Issue 4539: [with patch, needs work] plural wrapper

archive/issues_004539.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  saliola mhansen alexanderdreyer oleksandrmotsak polybori malb simonking\n\nDuring SD10 in Nancy, Michael Brickenstein and I worked on making Plural (the non-commutative extension of Singular) accessible from Sage.\n\nThe patches that resulted from this work are attached. They still need to be polished to be included in Sage.\n\nPossible topics that need work are:\n* coercion\n* flag to check degeneracy conditions on init\n* put the files in sage/algebra/ ???\n* make sure element does not export functions it doesn't support (e.g. gcd)\n\nFor a full featured wrapper we also need the following (they should be separated into different bugs once this one is done):\n* groebner basis\n* predefined structures from the library\n\nIssue created by migration from https://trac.sagemath.org/ticket/4539\n\n",
    "created_at": "2008-11-17T15:27:31Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "[with patch, needs work] plural wrapper",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4539",
    "user": "burcin"
}
```
Assignee: tbd

CC:  saliola mhansen alexanderdreyer oleksandrmotsak polybori malb simonking

During SD10 in Nancy, Michael Brickenstein and I worked on making Plural (the non-commutative extension of Singular) accessible from Sage.

The patches that resulted from this work are attached. They still need to be polished to be included in Sage.

Possible topics that need work are:
* coercion
* flag to check degeneracy conditions on init
* put the files in sage/algebra/ ???
* make sure element does not export functions it doesn't support (e.g. gcd)

For a full featured wrapper we also need the following (they should be separated into different bugs once this one is done):
* groebner basis
* predefined structures from the library

Issue created by migration from https://trac.sagemath.org/ticket/4539





---

archive/issue_comments_033830.json:
```json
{
    "body": "initial wrapper for plural",
    "created_at": "2008-11-17T15:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33830",
    "user": "burcin"
}
```

initial wrapper for plural



---

archive/issue_comments_033831.json:
```json
{
    "body": "Attachment [plural_1.patch](tarball://root/attachments/some-uuid/ticket4539/plural_1.patch) by burcin created at 2008-11-17 15:29:20\n\nbetter user interface for plural rings",
    "created_at": "2008-11-17T15:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33831",
    "user": "burcin"
}
```

Attachment [plural_1.patch](tarball://root/attachments/some-uuid/ticket4539/plural_1.patch) by burcin created at 2008-11-17 15:29:20

better user interface for plural rings



---

archive/issue_comments_033832.json:
```json
{
    "body": "Attachment [plural_2.patch](tarball://root/attachments/some-uuid/ticket4539/plural_2.patch) by PolyBoRi created at 2009-10-15 11:20:31",
    "created_at": "2009-10-15T11:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33832",
    "user": "PolyBoRi"
}
```

Attachment [plural_2.patch](tarball://root/attachments/some-uuid/ticket4539/plural_2.patch) by PolyBoRi created at 2009-10-15 11:20:31



---

archive/issue_comments_033833.json:
```json
{
    "body": "Attachment [letterplace.py](tarball://root/attachments/some-uuid/ticket4539/letterplace.py) by AlexGhitza created at 2009-11-15 13:22:40",
    "created_at": "2009-11-15T13:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33833",
    "user": "AlexGhitza"
}
```

Attachment [letterplace.py](tarball://root/attachments/some-uuid/ticket4539/letterplace.py) by AlexGhitza created at 2009-11-15 13:22:40



---

archive/issue_comments_033834.json:
```json
{
    "body": "Changing assignee from tbd to burcin.",
    "created_at": "2009-12-30T21:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33834",
    "user": "burcin"
}
```

Changing assignee from tbd to burcin.



---

archive/issue_comments_033835.json:
```json
{
    "body": "The letterplace interface in attachment:letterplace.py is now at #7797.",
    "created_at": "2009-12-30T21:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33835",
    "user": "burcin"
}
```

The letterplace interface in attachment:letterplace.py is now at #7797.



---

archive/issue_comments_033836.json:
```json
{
    "body": "Attachment [plural_1.sage-4.4.4.patch](tarball://root/attachments/some-uuid/ticket4539/plural_1.sage-4.4.4.patch) by burcin created at 2010-07-14 16:46:24\n\nrebased to 4.4.4",
    "created_at": "2010-07-14T16:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33836",
    "user": "burcin"
}
```

Attachment [plural_1.sage-4.4.4.patch](tarball://root/attachments/some-uuid/ticket4539/plural_1.sage-4.4.4.patch) by burcin created at 2010-07-14 16:46:24

rebased to 4.4.4



---

archive/issue_comments_033837.json:
```json
{
    "body": "rebased to 4.4.4",
    "created_at": "2010-07-14T16:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33837",
    "user": "burcin"
}
```

rebased to 4.4.4



---

archive/issue_comments_033838.json:
```json
{
    "body": "Attachment [plural_3.patch](tarball://root/attachments/some-uuid/ticket4539/plural_3.patch) by burcin created at 2010-07-15 09:40:15\n\nappy on top of 1 and 2, new classes for plural objects which don't inherit from the commutative ones",
    "created_at": "2010-07-15T09:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33838",
    "user": "burcin"
}
```

Attachment [plural_3.patch](tarball://root/attachments/some-uuid/ticket4539/plural_3.patch) by burcin created at 2010-07-15 09:40:15

appy on top of 1 and 2, new classes for plural objects which don't inherit from the commutative ones



---

archive/issue_comments_033839.json:
```json
{
    "body": "Attachment [plural_functions.2.patch](tarball://root/attachments/some-uuid/ticket4539/plural_functions.2.patch) by PolyBoRi created at 2010-07-15 21:03:31",
    "created_at": "2010-07-15T21:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33839",
    "user": "PolyBoRi"
}
```

Attachment [plural_functions.2.patch](tarball://root/attachments/some-uuid/ticket4539/plural_functions.2.patch) by PolyBoRi created at 2010-07-15 21:03:31



---

archive/issue_comments_033840.json:
```json
{
    "body": "sorry, for multiple files. Apply patches in this order:\n\nplural_1.sage-4.4.4.patch \n         \nplural_2.sage-4.4.4.patch\n                         \nplural_3.patch Download \n                         \nplural_functions.patch",
    "created_at": "2010-07-15T21:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33840",
    "user": "PolyBoRi"
}
```

sorry, for multiple files. Apply patches in this order:

plural_1.sage-4.4.4.patch 
         
plural_2.sage-4.4.4.patch
                         
plural_3.patch Download 
                         
plural_functions.patch



---

archive/issue_comments_033841.json:
```json
{
    "body": "Attachment [plural_functions.patch](tarball://root/attachments/some-uuid/ticket4539/plural_functions.patch) by mhansen created at 2010-07-20 00:14:47",
    "created_at": "2010-07-20T00:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33841",
    "user": "mhansen"
}
```

Attachment [plural_functions.patch](tarball://root/attachments/some-uuid/ticket4539/plural_functions.patch) by mhansen created at 2010-07-20 00:14:47



---

archive/issue_comments_033842.json:
```json
{
    "body": "i have just folded all the previous patches by Michael & Burcin into plural_folded-4.4.4.patch (should be applied before anything else)",
    "created_at": "2010-07-20T14:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33842",
    "user": "OleksandrMotsak"
}
```

i have just folded all the previous patches by Michael & Burcin into plural_folded-4.4.4.patch (should be applied before anything else)



---

archive/issue_comments_033843.json:
```json
{
    "body": "Attachment [plural_folded-4.4.4.patch](tarball://root/attachments/some-uuid/ticket4539/plural_folded-4.4.4.patch) by AlexanderDreyer created at 2010-07-20 14:28:54\n\nPart one Olekandr's work in Linz",
    "created_at": "2010-07-20T14:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33843",
    "user": "AlexanderDreyer"
}
```

Attachment [plural_folded-4.4.4.patch](tarball://root/attachments/some-uuid/ticket4539/plural_folded-4.4.4.patch) by AlexanderDreyer created at 2010-07-20 14:28:54

Part one Olekandr's work in Linz



---

archive/issue_comments_033844.json:
```json
{
    "body": "Attachment [extplural-more](tarball://root/attachments/some-uuid/ticket4539/extplural-more) by AlexanderDreyer created at 2010-07-20 14:29:15\n\nDoctest fixes by Alexander",
    "created_at": "2010-07-20T14:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33844",
    "user": "AlexanderDreyer"
}
```

Attachment [extplural-more](tarball://root/attachments/some-uuid/ticket4539/extplural-more) by AlexanderDreyer created at 2010-07-20 14:29:15

Doctest fixes by Alexander



---

archive/issue_comments_033845.json:
```json
{
    "body": "Attachment [extplural-more.patch](tarball://root/attachments/some-uuid/ticket4539/extplural-more.patch) by AlexanderDreyer created at 2010-07-20 14:30:35\n\nDoctest fixes by Alexander",
    "created_at": "2010-07-20T14:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33845",
    "user": "AlexanderDreyer"
}
```

Attachment [extplural-more.patch](tarball://root/attachments/some-uuid/ticket4539/extplural-more.patch) by AlexanderDreyer created at 2010-07-20 14:30:35

Doctest fixes by Alexander



---

archive/issue_comments_033846.json:
```json
{
    "body": "Attachment [extplural-more2.patch](tarball://root/attachments/some-uuid/ticket4539/extplural-more2.patch) by AlexanderDreyer created at 2010-07-21 10:23:52\n\nnoncommunative ring functionality",
    "created_at": "2010-07-21T10:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33846",
    "user": "AlexanderDreyer"
}
```

Attachment [extplural-more2.patch](tarball://root/attachments/some-uuid/ticket4539/extplural-more2.patch) by AlexanderDreyer created at 2010-07-21 10:23:52

noncommunative ring functionality



---

archive/issue_comments_033847.json:
```json
{
    "body": "Attachment [extplural-more3.patch](tarball://root/attachments/some-uuid/ticket4539/extplural-more3.patch) by AlexanderDreyer created at 2010-07-21 15:47:26",
    "created_at": "2010-07-21T15:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33847",
    "user": "AlexanderDreyer"
}
```

Attachment [extplural-more3.patch](tarball://root/attachments/some-uuid/ticket4539/extplural-more3.patch) by AlexanderDreyer created at 2010-07-21 15:47:26



---

archive/issue_comments_033848.json:
```json
{
    "body": "Changing assignee from burcin to OleksandrMotsak,AlexanderDreyer.",
    "created_at": "2010-07-22T12:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33848",
    "user": "AlexanderDreyer"
}
```

Changing assignee from burcin to OleksandrMotsak,AlexanderDreyer.



---

archive/issue_comments_033849.json:
```json
{
    "body": "Attachment [plural-wrapper-2010-07-22.patch](tarball://root/attachments/some-uuid/ticket4539/plural-wrapper-2010-07-22.patch) by AlexanderDreyer created at 2010-07-22 12:33:11\n\nThis folds of the following patches, a crucial subset of the noncommutation fucntionality as well as extensive documentation and  doctests",
    "created_at": "2010-07-22T12:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33849",
    "user": "AlexanderDreyer"
}
```

Attachment [plural-wrapper-2010-07-22.patch](tarball://root/attachments/some-uuid/ticket4539/plural-wrapper-2010-07-22.patch) by AlexanderDreyer created at 2010-07-22 12:33:11

This folds of the following patches, a crucial subset of the noncommutation fucntionality as well as extensive documentation and  doctests



---

archive/issue_comments_033850.json:
```json
{
    "body": "We have an first release ready for reviewing! \n\nRegards, Oleksandr and Alexander",
    "created_at": "2010-07-22T12:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33850",
    "user": "AlexanderDreyer"
}
```

We have an first release ready for reviewing! 

Regards, Oleksandr and Alexander



---

archive/issue_comments_033851.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-22T12:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33851",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033852.json:
```json
{
    "body": "wow, that sounds awesome.\nYou make me really happy.\nCan you outline in the ticket description, what the patch actually implements and what not.",
    "created_at": "2010-07-22T12:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33852",
    "user": "PolyBoRi"
}
```

wow, that sounds awesome.
You make me really happy.
Can you outline in the ticket description, what the patch actually implements and what not.



---

archive/issue_comments_033853.json:
```json
{
    "body": "what is meant in \"predefined structures from the library\"?\n\nNeed input: what structures / what library?",
    "created_at": "2010-07-22T13:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33853",
    "user": "OleksandrMotsak"
}
```

what is meant in "predefined structures from the library"?

Need input: what structures / what library?



---

archive/issue_comments_033854.json:
```json
{
    "body": "Attachment [plural-missing-docu.patch](tarball://root/attachments/some-uuid/ticket4539/plural-missing-docu.patch) by AlexanderDreyer created at 2010-07-23 06:02:31\n\nFixed some broken doctests",
    "created_at": "2010-07-23T06:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33854",
    "user": "AlexanderDreyer"
}
```

Attachment [plural-missing-docu.patch](tarball://root/attachments/some-uuid/ticket4539/plural-missing-docu.patch) by AlexanderDreyer created at 2010-07-23 06:02:31

Fixed some broken doctests



---

archive/issue_comments_033855.json:
```json
{
    "body": "Attachment [plural-missing-docu.2.patch](tarball://root/attachments/some-uuid/ticket4539/plural-missing-docu.2.patch) by AlexanderDreyer created at 2010-07-24 07:22:41",
    "created_at": "2010-07-24T07:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33855",
    "user": "AlexanderDreyer"
}
```

Attachment [plural-missing-docu.2.patch](tarball://root/attachments/some-uuid/ticket4539/plural-missing-docu.2.patch) by AlexanderDreyer created at 2010-07-24 07:22:41



---

archive/issue_comments_033856.json:
```json
{
    "body": "coverage to 100%",
    "created_at": "2010-07-24T07:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33856",
    "user": "AlexanderDreyer"
}
```

coverage to 100%



---

archive/issue_comments_033857.json:
```json
{
    "body": "How to apply the patches? *All* and in the given order? Or is one of them a \"master patch\" that replaces several other patches",
    "created_at": "2010-07-24T14:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33857",
    "user": "SimonKing"
}
```

How to apply the patches? *All* and in the given order? Or is one of them a "master patch" that replaces several other patches



---

archive/issue_comments_033858.json:
```json
{
    "body": "Just the following:\nplural-wrapper-2010-07-22.patch \nplural-missing-docu.2.patch \n\nRegards,\n  Alexander",
    "created_at": "2010-07-25T19:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33858",
    "user": "AlexanderDreyer"
}
```

Just the following:
plural-wrapper-2010-07-22.patch 
plural-missing-docu.2.patch 

Regards,
  Alexander



---

archive/issue_comments_033859.json:
```json
{
    "body": "Accumulated patch for all patches above for Singular/Plural",
    "created_at": "2010-07-27T13:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33859",
    "user": "AlexanderDreyer"
}
```

Accumulated patch for all patches above for Singular/Plural



---

archive/issue_comments_033860.json:
```json
{
    "body": "Attachment [plural-wrapper-2010-07-27.patch](tarball://root/attachments/some-uuid/ticket4539/plural-wrapper-2010-07-27.patch) by AlexanderDreyer created at 2010-07-27 13:52:17",
    "created_at": "2010-07-27T13:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33860",
    "user": "AlexanderDreyer"
}
```

Attachment [plural-wrapper-2010-07-27.patch](tarball://root/attachments/some-uuid/ticket4539/plural-wrapper-2010-07-27.patch) by AlexanderDreyer created at 2010-07-27 13:52:17



---

archive/issue_comments_033861.json:
```json
{
    "body": "Changing assignee from OleksandrMotsak,AlexanderDreyer to OleksandrMotsak, AlexanderDreyer.",
    "created_at": "2010-07-27T13:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33861",
    "user": "AlexanderDreyer"
}
```

Changing assignee from OleksandrMotsak,AlexanderDreyer to OleksandrMotsak, AlexanderDreyer.



---

archive/issue_comments_033862.json:
```json
{
    "body": "Hi!\n\nI have some computations to do with Weyl algebras, and would love to have this cool piece of work at my fingertips! Please keep it up!\n\nFor the record: I tried to apply those patches to Sage 4.5.2, and got the following rejects:\n\n```\nzephyr-/opt/sage/devel/sage>hg qimport ~/plural-wrapper-2010-07-27.patch\nadding plural-wrapper-2010-07-27.patch to series file\nzephyr-/opt/sage/devel/sage>hg qpush\napplying plural-wrapper-2010-07-27.patch\npatching file sage/libs/singular/function.pyx\nHunk #3 succeeded at 96 with fuzz 2 (offset 0 lines).\nHunk #36 FAILED at 1378\n1 out of 38 hunks FAILED -- saving rejects to file sage/libs/singular/function.pyx.rej\npatching file sage/libs/singular/singular-cdefs.pxi\nHunk #3 succeeded at 218 with fuzz 2 (offset -1 lines).\npatching file sage/rings/ideal_monoid.py\nHunk #1 FAILED at 12\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/ideal_monoid.py.rej\npatching file sage/rings/polynomial/term_order.py\nHunk #1 FAILED at 419\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/term_order.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh plural-wrapper-2010-07-27.patch\n```\n\n\nCheers,",
    "created_at": "2010-10-01T07:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33862",
    "user": "nthiery"
}
```

Hi!

I have some computations to do with Weyl algebras, and would love to have this cool piece of work at my fingertips! Please keep it up!

For the record: I tried to apply those patches to Sage 4.5.2, and got the following rejects:

```
zephyr-/opt/sage/devel/sage>hg qimport ~/plural-wrapper-2010-07-27.patch
adding plural-wrapper-2010-07-27.patch to series file
zephyr-/opt/sage/devel/sage>hg qpush
applying plural-wrapper-2010-07-27.patch
patching file sage/libs/singular/function.pyx
Hunk #3 succeeded at 96 with fuzz 2 (offset 0 lines).
Hunk #36 FAILED at 1378
1 out of 38 hunks FAILED -- saving rejects to file sage/libs/singular/function.pyx.rej
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #3 succeeded at 218 with fuzz 2 (offset -1 lines).
patching file sage/rings/ideal_monoid.py
Hunk #1 FAILED at 12
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/ideal_monoid.py.rej
patching file sage/rings/polynomial/term_order.py
Hunk #1 FAILED at 419
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/term_order.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh plural-wrapper-2010-07-27.patch
```


Cheers,



---

archive/issue_comments_033863.json:
```json
{
    "body": "Hi nthiery,\nMeanwhile, Burcin did a rebase?  Does it help you?\n\nRegards,\n  Alexander",
    "created_at": "2010-10-01T12:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33863",
    "user": "AlexanderDreyer"
}
```

Hi nthiery,
Meanwhile, Burcin did a rebase?  Does it help you?

Regards,
  Alexander



---

archive/issue_comments_033864.json:
```json
{
    "body": "Yes, it now applies smoothly on 4.5.2, and compiles. Thanks!\n\n\n```\nzephyr-~sage-main>sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: F.<x,dx> = FreeAlgebra(QQ,2)    \nsage: F.g_algebra({dx*x: x*dx+1})\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\n| Sage Version 4.5.2, Release Date: 2010-08-05                       |\n| Type notebook() for the GUI, and license() for information.        |\nSame problem with the example taken from the documentation:\n\n\n```\nzephyr-~sage-main>sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: A.<x,y,z>=FreeAlgebra(QQ,3)\nsage: G=A.g_algebra({y*x:-x*y})\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\n| Sage Version 4.5.2, Release Date: 2010-08-05                       |\n| Type notebook() for the GUI, and license() for information.        |\nShould I be using 4.5.3 (being downloaded)?",
    "created_at": "2010-10-01T12:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33864",
    "user": "nthiery"
}
```

Yes, it now applies smoothly on 4.5.2, and compiles. Thanks!


```
zephyr-~sage-main>sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<x,dx> = FreeAlgebra(QQ,2)    
sage: F.g_algebra({dx*x: x*dx+1})
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

| Sage Version 4.5.2, Release Date: 2010-08-05                       |
| Type notebook() for the GUI, and license() for information.        |
Same problem with the example taken from the documentation:


```
zephyr-~sage-main>sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A.<x,y,z>=FreeAlgebra(QQ,3)
sage: G=A.g_algebra({y*x:-x*y})
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

| Sage Version 4.5.2, Release Date: 2010-08-05                       |
| Type notebook() for the GUI, and license() for information.        |
Should I be using 4.5.3 (being downloaded)?



---

archive/issue_comments_033865.json:
```json
{
    "body": "Did you rebuild? (`sage -br`)",
    "created_at": "2010-10-01T12:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33865",
    "user": "AlexanderDreyer"
}
```

Did you rebuild? (`sage -br`)



---

archive/issue_comments_033866.json:
```json
{
    "body": "Replying to [comment:24 AlexanderDreyer]:\n> Did you rebuild? (`sage -br`)\n\nYup.",
    "created_at": "2010-10-01T12:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33866",
    "user": "nthiery"
}
```

Replying to [comment:24 AlexanderDreyer]:
> Did you rebuild? (`sage -br`)

Yup.



---

archive/issue_comments_033867.json:
```json
{
    "body": "I could reproduce the issue: `sage -gdb` vields the following;\n\n```\nsage: A.<x,y,z>=FreeAlgebra(QQ,3)\nsage: G=A.g_algebra({y*x:-x*y})\n\nProgram received signal SIGSEGV, Segmentation fault.\n0x00007fffdec7c488 in __pyx_f_4sage_4libs_8singular_8function_call_function (__pyx_v_self=0x459f910, __pyx_v_args=0x4538ab8, __pyx_v_R=0x4676480,\n    __pyx_optional_args=<value optimized out>) at sage/libs/singular/function.cpp:11969\n11969       currRingHdl->data.uring->ref += 1;\n```\n",
    "created_at": "2010-10-01T14:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33867",
    "user": "AlexanderDreyer"
}
```

I could reproduce the issue: `sage -gdb` vields the following;

```
sage: A.<x,y,z>=FreeAlgebra(QQ,3)
sage: G=A.g_algebra({y*x:-x*y})

Program received signal SIGSEGV, Segmentation fault.
0x00007fffdec7c488 in __pyx_f_4sage_4libs_8singular_8function_call_function (__pyx_v_self=0x459f910, __pyx_v_args=0x4538ab8, __pyx_v_R=0x4676480,
    __pyx_optional_args=<value optimized out>) at sage/libs/singular/function.cpp:11969
11969       currRingHdl->data.uring->ref += 1;
```




---

archive/issue_comments_033868.json:
```json
{
    "body": "I didn't have a chance to test the rebased patch, I had to leave right after I finished merging the rejected parts. I just wanted to get it out there in case it worked.\n\nI can also reproduce the crash. I'll take a look at it now and try to upload a patch that works.",
    "created_at": "2010-10-01T14:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33868",
    "user": "burcin"
}
```

I didn't have a chance to test the rebased patch, I had to leave right after I finished merging the rejected parts. I just wanted to get it out there in case it worked.

I can also reproduce the crash. I'll take a look at it now and try to upload a patch that works.



---

archive/issue_comments_033869.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-01T14:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33869",
    "user": "burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033870.json:
```json
{
    "body": "rebased to 4.5.3",
    "created_at": "2010-10-01T14:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33870",
    "user": "burcin"
}
```

rebased to 4.5.3



---

archive/issue_comments_033871.json:
```json
{
    "body": "Attachment [plural-wrapper-2010-10-01.patch](tarball://root/attachments/some-uuid/ticket4539/plural-wrapper-2010-10-01.patch) by burcin created at 2010-10-01 14:44:23\n\nIt was indeed careless rebasing. attachment:plural-wrapper-2010-10-01.patch (patch with same name as before, to hide my shame :) ) seems to work.\n\nNicolas, it would be great if you could help with the review. We are pretty confident with the interface to Singular and low-level code, since, as you can also see from the comments on the ticket, many Singular and Sage developers were involved in writing the code. However, we added many of the noncommutative structures on the spot (in a late night coding sprint) as we needed them. Another pair of eyes checking the mathematical structures and design would be really useful.\n\nThough I think we should try to get this patch in as soon as possible. I'm sure quite a few people would be interested in the functionality of Plural. We can always work on providing a better interface later, as the number of users/developers increases.",
    "created_at": "2010-10-01T14:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33871",
    "user": "burcin"
}
```

Attachment [plural-wrapper-2010-10-01.patch](tarball://root/attachments/some-uuid/ticket4539/plural-wrapper-2010-10-01.patch) by burcin created at 2010-10-01 14:44:23

It was indeed careless rebasing. attachment:plural-wrapper-2010-10-01.patch (patch with same name as before, to hide my shame :) ) seems to work.

Nicolas, it would be great if you could help with the review. We are pretty confident with the interface to Singular and low-level code, since, as you can also see from the comments on the ticket, many Singular and Sage developers were involved in writing the code. However, we added many of the noncommutative structures on the spot (in a late night coding sprint) as we needed them. Another pair of eyes checking the mathematical structures and design would be really useful.

Though I think we should try to get this patch in as soon as possible. I'm sure quite a few people would be interested in the functionality of Plural. We can always work on providing a better interface later, as the number of users/developers increases.



---

archive/issue_comments_033872.json:
```json
{
    "body": "Replying to [comment:28 burcin]:\n> It was indeed careless rebasing. attachment:plural-wrapper-2010-10-01.patch (patch with same name as before, to hide my shame :) ) seems to work.\n\nIt also does for me so far! Thanks a lot for the quick rebase!\n\n> Nicolas, it would be great if you could help with the review. We are pretty confident with the interface to Singular and low-level code, since, as you can also see from the comments on the ticket, many Singular and Sage developers were involved in writing the code. However, we added many of the noncommutative structures on the spot (in a late night coding sprint) as we needed them. Another pair of eyes checking the mathematical structures and design would be really useful.\n\nI don't want to promise much at this time because I am already (very) late with a couple other reviews. But since the code is going to very useful for my research right now, I can promise to provide feedback for how it feels in practice!\n\n> Though I think we should try to get this patch in as soon as possible. I'm sure quite a few people would be interested in the functionality of Plural. We can always work on providing a better interface later, as the number of users/developers increases. \n\nSounds good to me!",
    "created_at": "2010-10-03T21:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33872",
    "user": "nthiery"
}
```

Replying to [comment:28 burcin]:
> It was indeed careless rebasing. attachment:plural-wrapper-2010-10-01.patch (patch with same name as before, to hide my shame :) ) seems to work.

It also does for me so far! Thanks a lot for the quick rebase!

> Nicolas, it would be great if you could help with the review. We are pretty confident with the interface to Singular and low-level code, since, as you can also see from the comments on the ticket, many Singular and Sage developers were involved in writing the code. However, we added many of the noncommutative structures on the spot (in a late night coding sprint) as we needed them. Another pair of eyes checking the mathematical structures and design would be really useful.

I don't want to promise much at this time because I am already (very) late with a couple other reviews. But since the code is going to very useful for my research right now, I can promise to provide feedback for how it feels in practice!

> Though I think we should try to get this patch in as soon as possible. I'm sure quite a few people would be interested in the functionality of Plural. We can always work on providing a better interface later, as the number of users/developers increases. 

Sounds good to me!



---

archive/issue_comments_033873.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-03T21:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33873",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033874.json:
```json
{
    "body": "Is it possible at this stage to define non commutative polynomial rings over QQ['q'].fraction_field()?\nI got an error with what I tried:\n\n\n```\nsage: K = QQ['q'].fraction_field()\nq = K.gen()\nF.<x,y,ex,ey> = FreeAlgebra(K,4)\nW =  F.g_algebra({ex*x: x*(1+ex),ey*y:y*(1+ey)})\n\nsage: ------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/algebras/free_algebra.py\", line 547, in g_algebra\n    return NCPolynomialRing_plural(base_ring, n, \",\".join([str(g) for g in self.gens()]), c=cmat, d=dmat, order=order, check=check)\n  File \"plural.pyx\", line 223, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__init__ (sage/rings/polynomial/plural.cpp:3772)\n  File \"matrix0.pyx\", line 1520, in sage.matrix.matrix0.Matrix.change_ring (sage/matrix/matrix0.c:7670)\n  File \"/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py\", line 405, in __call__\n    return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)\n  File \"/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py\", line 1136, in matrix\n    return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)\n  File \"matrix_generic_dense.pyx\", line 93, in sage.matrix.matrix_generic_dense.Matrix_generic_dense.__init__ (sage/matrix/matrix_generic_dense.c:2321)\n  File \"/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ring.py\", line 468, in __call__\n    c = self.base_ring()(x)\n  File \"parent.pyx\", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)\n  File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)\n  File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)\n  File \"/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/fraction_field.py\", line 467, in _element_constructor_\n    coerce=coerce, reduce = self.is_exact())\n  File \"fraction_field_element.pyx\", line 120, in sage.rings.fraction_field_element.FractionFieldElement.__init__ (sage/rings/fraction_field_element.c:1934)\n  File \"parent.pyx\", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)\n  File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)\n  File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)\n  File \"/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 313, in _element_constructor_\n    return C(self, x, check, is_gen, construct=construct, **kwds)\n  File \"/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element_generic.py\", line 656, in __init__\n    x = [QQ(z) for z in x]\n  File \"parent.pyx\", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)\n  File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)\n  File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)\n  File \"rational.pyx\", line 367, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)\n  File \"rational.pyx\", line 521, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7052)\nTypeError: Unable to coerce 0 (<class 'sage.algebras.free_algebra_element.FreeAlgebraElement'>) to Rational\n```\n\n\nThanks!",
    "created_at": "2010-10-03T21:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33874",
    "user": "nthiery"
}
```

Is it possible at this stage to define non commutative polynomial rings over QQ['q'].fraction_field()?
I got an error with what I tried:


```
sage: K = QQ['q'].fraction_field()
q = K.gen()
F.<x,y,ex,ey> = FreeAlgebra(K,4)
W =  F.g_algebra({ex*x: x*(1+ex),ey*y:y*(1+ey)})

sage: ------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/algebras/free_algebra.py", line 547, in g_algebra
    return NCPolynomialRing_plural(base_ring, n, ",".join([str(g) for g in self.gens()]), c=cmat, d=dmat, order=order, check=check)
  File "plural.pyx", line 223, in sage.rings.polynomial.plural.NCPolynomialRing_plural.__init__ (sage/rings/polynomial/plural.cpp:3772)
  File "matrix0.pyx", line 1520, in sage.matrix.matrix0.Matrix.change_ring (sage/matrix/matrix0.c:7670)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 405, in __call__
    return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 1136, in matrix
    return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)
  File "matrix_generic_dense.pyx", line 93, in sage.matrix.matrix_generic_dense.Matrix_generic_dense.__init__ (sage/matrix/matrix_generic_dense.c:2321)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ring.py", line 468, in __call__
    c = self.base_ring()(x)
  File "parent.pyx", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/fraction_field.py", line 467, in _element_constructor_
    coerce=coerce, reduce = self.is_exact())
  File "fraction_field_element.pyx", line 120, in sage.rings.fraction_field_element.FractionFieldElement.__init__ (sage/rings/fraction_field_element.c:1934)
  File "parent.pyx", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.py", line 313, in _element_constructor_
    return C(self, x, check, is_gen, construct=construct, **kwds)
  File "/opt/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element_generic.py", line 656, in __init__
    x = [QQ(z) for z in x]
  File "parent.pyx", line 859, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "rational.pyx", line 367, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)
  File "rational.pyx", line 521, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7052)
TypeError: Unable to coerce 0 (<class 'sage.algebras.free_algebra_element.FreeAlgebraElement'>) to Rational
```


Thanks!



---

archive/issue_comments_033875.json:
```json
{
    "body": "I started playing with ideals. Currently, one creates an ideal I, and\nthen when one calls I.std() or I.twostd() to create a new left or\ntwosided ideal, and actually compute the Groebner basis. What about\nthe following variants:\n\n(A) Take the side decision at the time the ideal is created:\n\n```\n    sage: I = W.ideal([...], side=...)\n```\n\n(to be documented in ``W.ideal?``).\n\nWith that, ``I`` would be well defined as an ideal; otherwise it is\nmore a ``collection of polynomials'' and the name is misleading.\n\n(B) About computing the Grobner basis:\n\n```\n    sage: I.groebner_basis()\n```\n\n\nor:\n\n```\n    sage: I.std() \n```\n\nwould compute the groebner basis, store it for later calculations, and\nreturn it as a list of polynomials rather than a new ideal.\n\nI haven't actually played with ideals in Sage; so maybe point (B) is\njust how things are with commutative ideals in Sage, and consistency\nshould take precedence.\n\nCheers,\n                    Nicolas",
    "created_at": "2010-10-03T21:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33875",
    "user": "nthiery"
}
```

I started playing with ideals. Currently, one creates an ideal I, and
then when one calls I.std() or I.twostd() to create a new left or
twosided ideal, and actually compute the Groebner basis. What about
the following variants:

(A) Take the side decision at the time the ideal is created:

```
    sage: I = W.ideal([...], side=...)
```

(to be documented in ``W.ideal?``).

With that, ``I`` would be well defined as an ideal; otherwise it is
more a ``collection of polynomials'' and the name is misleading.

(B) About computing the Grobner basis:

```
    sage: I.groebner_basis()
```


or:

```
    sage: I.std() 
```

would compute the groebner basis, store it for later calculations, and
return it as a list of polynomials rather than a new ideal.

I haven't actually played with ideals in Sage; so maybe point (B) is
just how things are with commutative ideals in Sage, and consistency
should take precedence.

Cheers,
                    Nicolas



---

archive/issue_comments_033876.json:
```json
{
    "body": "Replying to [comment:32 nthiery]:\n> I started playing with ideals. Currently, one creates an ideal I, and\n> then when one calls I.std() or I.twostd() to create a new left or\n> twosided ideal, and actually compute the Groebner basis. What about\n> the following variants:\n\nCurrently, if R is a commutative ring and L is a list of elements of R, one may use the shorthand notation `I = R*L` or `I = L*R` to create an ideal. It seems natural to me to extend this to the non-commutative case: `R*L` for left ideal,  `L*R` for right ideal, and `R*L*R` for two-sided ideal.\n\nHow to implement it? Well, on could have a base class for ideals over non-commutative rings (let's call it `NCIdeal`), and derive from it `NCIdeal_left`, `NCIdeal_right`, `NCIdeal_twodsided`.\n\nThen, one has to modify the multiplication method for rings so that sidedness is taken care of (there is a method ideal_class(), that probably needs to accept an optional argument \"side\"). And of course, the one-sided ideal classes need a multiplication method as well.\n\nAnd then, `NCIdeal_twodsided.groebner_basis()` would yield a two-sided Gr\u00f6bner basis, while `NCIdeal_left/right.groebner_basis()` would only yield a one-sided Gr\u00f6bner basis, of course unless a two-sided Gr\u00f6bner basis is requested by using an optional argument.",
    "created_at": "2010-10-03T21:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33876",
    "user": "SimonKing"
}
```

Replying to [comment:32 nthiery]:
> I started playing with ideals. Currently, one creates an ideal I, and
> then when one calls I.std() or I.twostd() to create a new left or
> twosided ideal, and actually compute the Groebner basis. What about
> the following variants:

Currently, if R is a commutative ring and L is a list of elements of R, one may use the shorthand notation `I = R*L` or `I = L*R` to create an ideal. It seems natural to me to extend this to the non-commutative case: `R*L` for left ideal,  `L*R` for right ideal, and `R*L*R` for two-sided ideal.

How to implement it? Well, on could have a base class for ideals over non-commutative rings (let's call it `NCIdeal`), and derive from it `NCIdeal_left`, `NCIdeal_right`, `NCIdeal_twodsided`.

Then, one has to modify the multiplication method for rings so that sidedness is taken care of (there is a method ideal_class(), that probably needs to accept an optional argument "side"). And of course, the one-sided ideal classes need a multiplication method as well.

And then, `NCIdeal_twodsided.groebner_basis()` would yield a two-sided Gröbner basis, while `NCIdeal_left/right.groebner_basis()` would only yield a one-sided Gröbner basis, of course unless a two-sided Gröbner basis is requested by using an optional argument.



---

archive/issue_comments_033877.json:
```json
{
    "body": "Replying to [comment:32 nthiery]:\n> I started playing with ideals. Currently, one creates an ideal I, and\n> then when one calls I.std() or I.twostd() to create a new left or\n> twosided ideal, and actually compute the Groebner basis. \n\nBy the way: right ideals are not yet handled yet, right? Would it be a lot of work? It's just that the ideals I am currently playing with are right ideals, and I keep mixing myself up when playing with the \"dualized\" version I had to write in Sage.",
    "created_at": "2010-10-12T15:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33877",
    "user": "nthiery"
}
```

Replying to [comment:32 nthiery]:
> I started playing with ideals. Currently, one creates an ideal I, and
> then when one calls I.std() or I.twostd() to create a new left or
> twosided ideal, and actually compute the Groebner basis. 

By the way: right ideals are not yet handled yet, right? Would it be a lot of work? It's just that the ideals I am currently playing with are right ideals, and I keep mixing myself up when playing with the "dualized" version I had to write in Sage.



---

archive/issue_comments_033878.json:
```json
{
    "body": "Hi Simon!\n\nReplying to [comment:33 SimonKing]:\n> Replying to [comment:32 nthiery]:\n> > I started playing with ideals. Currently, one creates an ideal I, and\n> > then when one calls I.std() or I.twostd() to create a new left or\n> > twosided ideal, and actually compute the Groebner basis. What about\n> > the following variants:\n> \n> Currently, if R is a commutative ring and L is a list of elements of R, one may use the shorthand notation `I = R*L` or `I = L*R` to create an ideal. It seems natural to me to extend this to the non-commutative case: `R*L` for left ideal,  `L*R` for right ideal, and `R*L*R` for two-sided ideal.\n\n+1 for the implementation proposal!\n\nI also like that shorthand syntax for interactive usage. However, in\ncode, I prefer using something more explicit like R.ideal(L,side=...).\nBesides, having an R.ideal method also provides with:\n\n- a good place for advertising (it appears in R.<tab>), documenting,\n  testing the feature and its shorthand\n- an easy way for subclasses of (the class of) R to override this\n  method without having to worry about overloading/coercion/...\n\nCheers,\n\t\t\tNicolas",
    "created_at": "2010-10-12T15:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33878",
    "user": "nthiery"
}
```

Hi Simon!

Replying to [comment:33 SimonKing]:
> Replying to [comment:32 nthiery]:
> > I started playing with ideals. Currently, one creates an ideal I, and
> > then when one calls I.std() or I.twostd() to create a new left or
> > twosided ideal, and actually compute the Groebner basis. What about
> > the following variants:
> 
> Currently, if R is a commutative ring and L is a list of elements of R, one may use the shorthand notation `I = R*L` or `I = L*R` to create an ideal. It seems natural to me to extend this to the non-commutative case: `R*L` for left ideal,  `L*R` for right ideal, and `R*L*R` for two-sided ideal.

+1 for the implementation proposal!

I also like that shorthand syntax for interactive usage. However, in
code, I prefer using something more explicit like R.ideal(L,side=...).
Besides, having an R.ideal method also provides with:

- a good place for advertising (it appears in R.<tab>), documenting,
  testing the feature and its shorthand
- an easy way for subclasses of (the class of) R to override this
  method without having to worry about overloading/coercion/...

Cheers,
			Nicolas



---

archive/issue_comments_033879.json:
```json
{
    "body": "Apply plural-wrapper-2010-10-01.patch\n\n(to the patchbot)\n\nIf I understand correctly, this patch is the only one, right? So, it would be a good thing to try whether it needs to be rebased again.\n\nCurrently, I have a high motivation to have the noncommutative stuff (including letterplace!) in libsingular. So, I hope the work on this ticket and on #7797 can be resumed.",
    "created_at": "2011-03-13T10:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33879",
    "user": "SimonKing"
}
```

Apply plural-wrapper-2010-10-01.patch

(to the patchbot)

If I understand correctly, this patch is the only one, right? So, it would be a good thing to try whether it needs to be rebased again.

Currently, I have a high motivation to have the noncommutative stuff (including letterplace!) in libsingular. So, I hope the work on this ticket and on #7797 can be resumed.



---

archive/issue_comments_033880.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-13T14:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33880",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033881.json:
```json
{
    "body": "Apply trac4539_libplural.patch\n\nIt turned out that the old patch did not apply, since meanwhile the libsingular options are dealt with in a different way. I have rebased the patch, and also adopted the new option syntax.\n\nHowever, not all is good. Here is one error that I just found:\n\n```\nsage: A.<x,y,z> = FreeAlgebra(QQ, 3) \nsage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y}) \nsage: H.inject_variables() \nDefining x, y, z\nsage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False) \nsage: G = vector(I.gens()); G  \n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n...\n/mnt/local/king/SAGE/sage-4.6.2/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:6035)()\n\nNotImplementedError: \n```\n\n\nSo, there remains work to do!",
    "created_at": "2011-03-13T14:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33881",
    "user": "SimonKing"
}
```

Apply trac4539_libplural.patch

It turned out that the old patch did not apply, since meanwhile the libsingular options are dealt with in a different way. I have rebased the patch, and also adopted the new option syntax.

However, not all is good. Here is one error that I just found:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3) 
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y}) 
sage: H.inject_variables() 
Defining x, y, z
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False) 
sage: G = vector(I.gens()); G  
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
...
/mnt/local/king/SAGE/sage-4.6.2/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:6035)()

NotImplementedError: 
```


So, there remains work to do!



---

archive/issue_comments_033882.json:
```json
{
    "body": "Changing keywords from \"\" to \"libsingular plural wrapper\".",
    "created_at": "2011-03-13T14:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33882",
    "user": "SimonKing"
}
```

Changing keywords from "" to "libsingular plural wrapper".



---

archive/issue_comments_033883.json:
```json
{
    "body": "The reason of the error was that `FreeModule` tries (among other things) the method `is_integral_domain()`. By default, it raises a `NotImplementedError`, and this is the error we get above.\n\nProposed solution: Catch that `NotImplementedError` and do as if `is_integral_domain()` had returned `False`.\n\nI don't know if there will be further problems, but I'll put it back to \"needs review\".",
    "created_at": "2011-03-13T14:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33883",
    "user": "SimonKing"
}
```

The reason of the error was that `FreeModule` tries (among other things) the method `is_integral_domain()`. By default, it raises a `NotImplementedError`, and this is the error we get above.

Proposed solution: Catch that `NotImplementedError` and do as if `is_integral_domain()` had returned `False`.

I don't know if there will be further problems, but I'll put it back to "needs review".



---

archive/issue_comments_033884.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-13T14:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33884",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033885.json:
```json
{
    "body": "Apply trac4539_libplural.patch",
    "created_at": "2011-03-13T18:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33885",
    "user": "SimonKing"
}
```

Apply trac4539_libplural.patch



---

archive/issue_comments_033886.json:
```json
{
    "body": "1. I don't know why the patchbot is trying *two* patches. It is supposed to use only one of them.\n\n2. I get numerous doctest failures. Some of them look like severe errors. So, it needs work.",
    "created_at": "2011-03-13T18:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33886",
    "user": "SimonKing"
}
```

1. I don't know why the patchbot is trying *two* patches. It is supposed to use only one of them.

2. I get numerous doctest failures. Some of them look like severe errors. So, it needs work.



---

archive/issue_comments_033887.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-13T18:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33887",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033888.json:
```json
{
    "body": "It would be great to have this in Sage!\n\nI'm seeing some problems with the patch.  First, it doesn't apply cleanly to Sage 4.7.alpha1.  I haven't tried applying to 4.6.2.  I rebased it by hand.\n\nSecond, the change\n\n```diff\n-                    block_name, block_length, _ = re.split(length_pattern,block)\n+                    block_name, block_length, _ = re.split(pattern, block.strip())\n```\n\nin term_order.py is problematic, because \"pattern\" is not defined anywhere.  Replacing it by \"length_pattern\" seems to work.\n\nThird, in multipolynomial_ideal.py, `_groebner_basis_libsingular` is being called with keywords \"deg_bound\" and \"mult_bound\", but it doesn't accept those keywords as valid arguments.  Should we add `*args, **kwds` to the argument list?    Or should those keywords be dealt with explicitly?  I tried adding generic `*args` and `**kwds`, but doctesting on that file segfaults.\n\nWhen I doctest the whole Sage library after making these changes, I get the following failures:\n\n```\nThe following tests failed:\n\n        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # Killed/crashed\n        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/libs/singular/polynomial.pyx # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/plural.pyx # 6 doctests failed\n```\n\nOn one machine, I also had this failure:\n\n```\n\tsage -t -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial.pyx # Killed/crashed\n```\n",
    "created_at": "2011-03-23T22:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33888",
    "user": "jhpalmieri"
}
```

It would be great to have this in Sage!

I'm seeing some problems with the patch.  First, it doesn't apply cleanly to Sage 4.7.alpha1.  I haven't tried applying to 4.6.2.  I rebased it by hand.

Second, the change

```diff
-                    block_name, block_length, _ = re.split(length_pattern,block)
+                    block_name, block_length, _ = re.split(pattern, block.strip())
```

in term_order.py is problematic, because "pattern" is not defined anywhere.  Replacing it by "length_pattern" seems to work.

Third, in multipolynomial_ideal.py, `_groebner_basis_libsingular` is being called with keywords "deg_bound" and "mult_bound", but it doesn't accept those keywords as valid arguments.  Should we add `*args, **kwds` to the argument list?    Or should those keywords be dealt with explicitly?  I tried adding generic `*args` and `**kwds`, but doctesting on that file segfaults.

When I doctest the whole Sage library after making these changes, I get the following failures:

```
The following tests failed:

        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # Killed/crashed
        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/libs/singular/polynomial.pyx # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/polynomial/plural.pyx # 6 doctests failed
```

On one machine, I also had this failure:

```
	sage -t -long -force_lib devel/sage/sage/rings/polynomial/multi_polynomial.pyx # Killed/crashed
```




---

archive/issue_comments_033889.json:
```json
{
    "body": "I've rebased the patch to Sage 4.7.  I'm not sure it's worth cluttering up this ticket with more patches, especially ones this big, so I've posted it to [http://sage.math.washington.edu/home/palmieri/misc/trac_4539_libplural-rebased.patch](http://sage.math.washington.edu/home/palmieri/misc/trac_4539_libplural-rebased.patch).  This patch also fixes a few docstrings, and it makes the changes that I described above, although I'm not sure they're the right thing to do.",
    "created_at": "2011-03-30T22:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33889",
    "user": "jhpalmieri"
}
```

I've rebased the patch to Sage 4.7.  I'm not sure it's worth cluttering up this ticket with more patches, especially ones this big, so I've posted it to [http://sage.math.washington.edu/home/palmieri/misc/trac_4539_libplural-rebased.patch](http://sage.math.washington.edu/home/palmieri/misc/trac_4539_libplural-rebased.patch).  This patch also fixes a few docstrings, and it makes the changes that I described above, although I'm not sure they're the right thing to do.



---

archive/issue_comments_033890.json:
```json
{
    "body": "Changing keywords from \"libsingular plural wrapper\" to \"libsingular plural wrapper sd34\".",
    "created_at": "2011-09-26T17:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33890",
    "user": "SimonKing"
}
```

Changing keywords from "libsingular plural wrapper" to "libsingular plural wrapper sd34".



---

archive/issue_comments_033891.json:
```json
{
    "body": "At sage days 34, we try to rebase the old patch. Burcin and I agree that we should rebase it with respect to #7797 (which, among other things, modernises coercion for free algebras). It also means that we can use one- and two-sided ideals in non-commutative rings, by #11068.\n\nSome hunks of the latest patch fail due to other tickets that meanwhile are merged, such as #11316.\n\nIt seems to me that, out of the 5 hunks that fail, only 2 are non-trivial to fix.",
    "created_at": "2011-09-26T17:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33891",
    "user": "SimonKing"
}
```

At sage days 34, we try to rebase the old patch. Burcin and I agree that we should rebase it with respect to #7797 (which, among other things, modernises coercion for free algebras). It also means that we can use one- and two-sided ideals in non-commutative rings, by #11068.

Some hunks of the latest patch fail due to other tickets that meanwhile are merged, such as #11316.

It seems to me that, out of the 5 hunks that fail, only 2 are non-trivial to fix.



---

archive/issue_comments_033892.json:
```json
{
    "body": "experimental rebasement to 4.7.2alpha3-prerelease",
    "created_at": "2011-09-26T22:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33892",
    "user": "AlexanderDreyer"
}
```

experimental rebasement to 4.7.2alpha3-prerelease



---

archive/issue_comments_033893.json:
```json
{
    "body": "Attachment [trac4539_libplural-2011-09-27-untested.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural-2011-09-27-untested.patch) by AlexanderDreyer created at 2011-09-26 22:32:30\n\nCan you test, whether Attach:trac4539_libplural-2011-09-27-untested.patch does the job?",
    "created_at": "2011-09-26T22:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33893",
    "user": "AlexanderDreyer"
}
```

Attachment [trac4539_libplural-2011-09-27-untested.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural-2011-09-27-untested.patch) by AlexanderDreyer created at 2011-09-26 22:32:30

Can you test, whether Attach:trac4539_libplural-2011-09-27-untested.patch does the job?



---

archive/issue_comments_033894.json:
```json
{
    "body": "Replying to [comment:44 AlexanderDreyer]:\n> Can you test, whether Attach:trac4539_libplural-2011-09-27-untested.patch does the job?\n\nWe were just dubling the work, it seems. I had rebased my old patch and was running tests (don't know the outcome).\n\nBut is your patch relative to #11068 (and perhaps to #7797 as well)? #11068 already has a positive review, and since it adds one- and twosided ideals of non-commutative rings, it seems like a natural dependency for a plural wrapper.",
    "created_at": "2011-09-26T23:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33894",
    "user": "SimonKing"
}
```

Replying to [comment:44 AlexanderDreyer]:
> Can you test, whether Attach:trac4539_libplural-2011-09-27-untested.patch does the job?

We were just dubling the work, it seems. I had rebased my old patch and was running tests (don't know the outcome).

But is your patch relative to #11068 (and perhaps to #7797 as well)? #11068 already has a positive review, and since it adds one- and twosided ideals of non-commutative rings, it seems like a natural dependency for a plural wrapper.



---

archive/issue_comments_033895.json:
```json
{
    "body": "Replying to [comment:45 SimonKing]:\n\n> We were just dubling the work, it seems. I had rebased my old patch and was running tests (don't know the outcome). But is your patch relative to #11068 (and perhaps to #7797 as well)? #11068 already has a positive review, and since it adds one- and twosided ideals of non-commutative rings, it seems like a natural dependency for a plural wrapper.\n\nSorry, I thought rebasing couldn't be finished. But it seems, that something is wrong with my rebased patch. So you should post yours.",
    "created_at": "2011-09-26T23:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33895",
    "user": "AlexanderDreyer"
}
```

Replying to [comment:45 SimonKing]:

> We were just dubling the work, it seems. I had rebased my old patch and was running tests (don't know the outcome). But is your patch relative to #11068 (and perhaps to #7797 as well)? #11068 already has a positive review, and since it adds one- and twosided ideals of non-commutative rings, it seems like a natural dependency for a plural wrapper.

Sorry, I thought rebasing couldn't be finished. But it seems, that something is wrong with my rebased patch. So you should post yours.



---

archive/issue_comments_033896.json:
```json
{
    "body": "Replying to [comment:46 AlexanderDreyer]:\n> Sorry, I thought rebasing couldn't be finished. But it seems, that something is wrong with my rebased patch. So you should post yours.\nJust foudn out, the patch was fine (so far), but my sage/devel directory was corrupted. (Luckily I cloned.)",
    "created_at": "2011-09-26T23:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33896",
    "user": "AlexanderDreyer"
}
```

Replying to [comment:46 AlexanderDreyer]:
> Sorry, I thought rebasing couldn't be finished. But it seems, that something is wrong with my rebased patch. So you should post yours.
Just foudn out, the patch was fine (so far), but my sage/devel directory was corrupted. (Luckily I cloned.)



---

archive/issue_comments_033897.json:
```json
{
    "body": "I have attached my experimental rebasement (relative to #7797 on top of sage-4.7.2.alpha3), but not all is good.\n\nThere are quite a lot of doctest failures, including some very wrong arithmetical results in plural.pyx.\n\nLess dramatic: There are some zero division errors (for example in doctests of mul\nti_polynomial_libsingular.pyx) where the expected error message was \"rational division by zero\", but now there is *no* error message (but there is a `ZeroDivisionError`, at least).\n\nThere is a segment fault in the tests of multi_polynomial_ideal.py. I guess it is the same segfault that also occurs in some elliptic curves tests.\n\nAlexander, when you said that your broken Sage installation was to blame: Do you mean that the tests are mostly passing with your patch?",
    "created_at": "2011-09-27T06:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33897",
    "user": "SimonKing"
}
```

I have attached my experimental rebasement (relative to #7797 on top of sage-4.7.2.alpha3), but not all is good.

There are quite a lot of doctest failures, including some very wrong arithmetical results in plural.pyx.

Less dramatic: There are some zero division errors (for example in doctests of mul
ti_polynomial_libsingular.pyx) where the expected error message was "rational division by zero", but now there is *no* error message (but there is a `ZeroDivisionError`, at least).

There is a segment fault in the tests of multi_polynomial_ideal.py. I guess it is the same segfault that also occurs in some elliptic curves tests.

Alexander, when you said that your broken Sage installation was to blame: Do you mean that the tests are mostly passing with your patch?



---

archive/issue_comments_033898.json:
```json
{
    "body": "I am now testing Alexander's patch. First good news: It applies without fuzz, even when #7797 is applied. Let's see how the doc tests work!",
    "created_at": "2011-09-27T08:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33898",
    "user": "SimonKing"
}
```

I am now testing Alexander's patch. First good news: It applies without fuzz, even when #7797 is applied. Let's see how the doc tests work!



---

archive/issue_comments_033899.json:
```json
{
    "body": "I started with \"manually\" testing against three of the doc test errors that I got with my patch. Two of them fail with Alexander's patch as well:\n\n```\nsage: P.<x,y,z> = QQ[]\nsage: x/0\nTraceback (most recent call last):\n...\nZeroDivisionError:\n```\n\n --> The old error message \"rational division by zero\" has gone.\n\n\n```\nsage: (x*y).is_monomial()\nTrue\nsage: (2*y).is_monomial()\nFalse\n```\n\n --> That's better than my patch, where these return 1 and 0.\n\n\n```\nsage: (x+y^2^30)^10\nx^10\n```\n\n --> That should result in an overflow error.\n\nI didn't analyse the segmentation faults.",
    "created_at": "2011-09-27T08:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33899",
    "user": "SimonKing"
}
```

I started with "manually" testing against three of the doc test errors that I got with my patch. Two of them fail with Alexander's patch as well:

```
sage: P.<x,y,z> = QQ[]
sage: x/0
Traceback (most recent call last):
...
ZeroDivisionError:
```

 --> The old error message "rational division by zero" has gone.


```
sage: (x*y).is_monomial()
True
sage: (2*y).is_monomial()
False
```

 --> That's better than my patch, where these return 1 and 0.


```
sage: (x+y^2^30)^10
x^10
```

 --> That should result in an overflow error.

I didn't analyse the segmentation faults.



---

archive/issue_comments_033900.json:
```json
{
    "body": "PS: Note that all these problems concern *commutative* polynomials.",
    "created_at": "2011-09-27T08:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33900",
    "user": "SimonKing"
}
```

PS: Note that all these problems concern *commutative* polynomials.



---

archive/issue_comments_033901.json:
```json
{
    "body": "Replying to [comment:50 SimonKing]:\n> sage: P.<x,y,z> = QQ[]\n> sage: x/0\n> Traceback (most recent call last):\n> ...\n> ZeroDivisionError:\n\nHere is the explanation:\n\nLet `P = QQ[x,y,z]`. Since coercion is now done properly, x/0 is first converting 0 into P and tries to invert it there. The result is a naked `ZeroDivisionError` in\nsage.libs.singular.polynomial.singular_polynomial_div_coeff.\nBefore, it used to invert 0 as a rational number, resulting in a `ZeroDivisionError` with some error message.\n\nBurcin and I agree that it is ok to have the `ZeroDivisionError` without a message: What else could it state but \"don't divide by zero\"?\n\nSo, it is not an issue.\n\n> {{{\n> sage: (x*y).is_monomial()\n> True\n> sage: (2*y).is_monomial()\n> False\n\nI don't know why it has occured in the first place, but now it seems alright, even with my patch.\n\n> {{{\n> sage: (x+y<sup>2</sup>30)^10\n> x^10\n> }}}\n>  --> That should result in an overflow error.\n\nIt turns out that one gets the *same* stupid result with an unpatched sage-4.7.2.alpha2. Burcin told me that this patch is supposed to fix it. Apparently it fails, and we need to understand why it fails.\n\n> I didn't analyse the segmentation faults.\n\nThat will be next...",
    "created_at": "2011-09-27T14:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33901",
    "user": "SimonKing"
}
```

Replying to [comment:50 SimonKing]:
> sage: P.<x,y,z> = QQ[]
> sage: x/0
> Traceback (most recent call last):
> ...
> ZeroDivisionError:

Here is the explanation:

Let `P = QQ[x,y,z]`. Since coercion is now done properly, x/0 is first converting 0 into P and tries to invert it there. The result is a naked `ZeroDivisionError` in
sage.libs.singular.polynomial.singular_polynomial_div_coeff.
Before, it used to invert 0 as a rational number, resulting in a `ZeroDivisionError` with some error message.

Burcin and I agree that it is ok to have the `ZeroDivisionError` without a message: What else could it state but "don't divide by zero"?

So, it is not an issue.

> {{{
> sage: (x*y).is_monomial()
> True
> sage: (2*y).is_monomial()
> False

I don't know why it has occured in the first place, but now it seems alright, even with my patch.

> {{{
> sage: (x+y<sup>2</sup>30)^10
> x^10
> }}}
>  --> That should result in an overflow error.

It turns out that one gets the *same* stupid result with an unpatched sage-4.7.2.alpha2. Burcin told me that this patch is supposed to fix it. Apparently it fails, and we need to understand why it fails.

> I didn't analyse the segmentation faults.

That will be next...



---

archive/issue_comments_033902.json:
```json
{
    "body": "I created a new ticket #11856 for the (missing) overflow error.",
    "created_at": "2011-09-27T14:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33902",
    "user": "SimonKing"
}
```

I created a new ticket #11856 for the (missing) overflow error.



---

archive/issue_comments_033903.json:
```json
{
    "body": "Replying to [comment:53 SimonKing]:\n> I created a new ticket #11856 for the (missing) overflow error.\n\nSorry, I forgot: It should be a dependency.",
    "created_at": "2011-09-27T14:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33903",
    "user": "SimonKing"
}
```

Replying to [comment:53 SimonKing]:
> I created a new ticket #11856 for the (missing) overflow error.

Sorry, I forgot: It should be a dependency.



---

archive/issue_comments_033904.json:
```json
{
    "body": "Attachment [trac4539_libplural_todo.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural_todo.patch) by SimonKing created at 2011-09-27 16:10:14\n\nExperimental rebasement wrt sage-4.7.2.alpha3 plus #7797 plus #11856",
    "created_at": "2011-09-27T16:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33904",
    "user": "SimonKing"
}
```

Attachment [trac4539_libplural_todo.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural_todo.patch) by SimonKing created at 2011-09-27 16:10:14

Experimental rebasement wrt sage-4.7.2.alpha3 plus #7797 plus #11856



---

archive/issue_comments_033905.json:
```json
{
    "body": "It seems that I was able to get the missing overflow error in #11856, which I added as a dependency. I had to update my patch (and Alexander will need to update his as well), because the function overflow_check is now expecting two arguments (a long and a ring), not one.\n\nTests are still missing, of course, and I have still no idea about the segfault.",
    "created_at": "2011-09-27T16:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33905",
    "user": "SimonKing"
}
```

It seems that I was able to get the missing overflow error in #11856, which I added as a dependency. I had to update my patch (and Alexander will need to update his as well), because the function overflow_check is now expecting two arguments (a long and a ring), not one.

Tests are still missing, of course, and I have still no idea about the segfault.



---

archive/issue_comments_033906.json:
```json
{
    "body": "fixes at least some segfault (updated patch) - needs main patch applied before",
    "created_at": "2011-09-27T22:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33906",
    "user": "AlexanderDreyer"
}
```

fixes at least some segfault (updated patch) - needs main patch applied before



---

archive/issue_comments_033907.json:
```json
{
    "body": "Attachment [trac4539_lmul.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_lmul.patch) by AlexanderDreyer created at 2011-09-27 22:11:45\n\nI found out that the intended lmul implementation, namely using rmul *and* reverting left and right hand side, is an illegal for some right hand side objects. Up to now, this is only verified for schemes/elliptic_curves/ell_curve_isogeny.py More extensive tests follow.",
    "created_at": "2011-09-27T22:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33907",
    "user": "AlexanderDreyer"
}
```

Attachment [trac4539_lmul.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_lmul.patch) by AlexanderDreyer created at 2011-09-27 22:11:45

I found out that the intended lmul implementation, namely using rmul *and* reverting left and right hand side, is an illegal for some right hand side objects. Up to now, this is only verified for schemes/elliptic_curves/ell_curve_isogeny.py More extensive tests follow.



---

archive/issue_comments_033908.json:
```json
{
    "body": "Hi Alexander, the description of your lmul patch says \"needs main patch applied before\". Which of the two main patches are you referring to?",
    "created_at": "2011-09-28T06:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33908",
    "user": "SimonKing"
}
```

Hi Alexander, the description of your lmul patch says "needs main patch applied before". Which of the two main patches are you referring to?



---

archive/issue_comments_033909.json:
```json
{
    "body": "Attachment [trac4539_kwds.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_kwds.patch) by AlexanderDreyer created at 2011-09-28 08:59:07\n\nfixes \"keyword not found\" issue (revert unnecessary path of the big patch)",
    "created_at": "2011-09-28T08:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33909",
    "user": "AlexanderDreyer"
}
```

Attachment [trac4539_kwds.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_kwds.patch) by AlexanderDreyer created at 2011-09-28 08:59:07

fixes "keyword not found" issue (revert unnecessary path of the big patch)



---

archive/issue_comments_033910.json:
```json
{
    "body": "Here another small patch reverts an unnecessary part of the big patch. It fixes the keyword argument not found issue.",
    "created_at": "2011-09-28T09:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33910",
    "user": "AlexanderDreyer"
}
```

Here another small patch reverts an unnecessary part of the big patch. It fixes the keyword argument not found issue.



---

archive/issue_comments_033911.json:
```json
{
    "body": "Attachment [trac4539_is_monomial.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_is_monomial.patch) by AlexanderDreyer created at 2011-09-28 10:33:49\n\nPatch for using trac4539_libplural-2011-09-27-untested.patch together with #11856 (not needed for trac4539_libplural_todo.patch)",
    "created_at": "2011-09-28T10:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33911",
    "user": "AlexanderDreyer"
}
```

Attachment [trac4539_is_monomial.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_is_monomial.patch) by AlexanderDreyer created at 2011-09-28 10:33:49

Patch for using trac4539_libplural-2011-09-27-untested.patch together with #11856 (not needed for trac4539_libplural_todo.patch)



---

archive/issue_comments_033912.json:
```json
{
    "body": "Attachment [trac4539_overflow.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_overflow.patch) by AlexanderDreyer created at 2011-09-28 10:54:41\n\nmonomial_quotient should throw instead of return nonsense",
    "created_at": "2011-09-28T10:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33912",
    "user": "AlexanderDreyer"
}
```

Attachment [trac4539_overflow.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_overflow.patch) by AlexanderDreyer created at 2011-09-28 10:54:41

monomial_quotient should throw instead of return nonsense



---

archive/issue_comments_033913.json:
```json
{
    "body": "Attachment [trac4539_monomial_quotient.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_monomial_quotient.patch) by SimonKing created at 2011-09-28 13:18:13\n\nConcerning [attachment:trac4539_monomial_quotient.patch]: I am not sure if it is the right thing to do. I think that monomial_quotient is a method that should be as fast as possible, since in some situations it is used very frequently. In these situations, it is always the case that one monomial *does* divide the other. Hence, for the application, it is a bad idea to have a redundant sanity test in monomial_quotient. I'd rather have it return a wrong result when using it in a wrong way.\n\nNote that [attachment:trac4539_kwds.patch] is not needed for my patch - I already have *args in it.\n\nWe have already briefly discussed why I think that [attachment:trac4539_lmul.patch] probably is not a good approach: x._rmul_(c) and x._lmul_(c) (by specification of the coercion model) can assume that the argument c belongs to x.parent().base_ring(). In particular, I don't believe that c can actually be a non-commutative polynomial.\n\nCan you please provide an example that was segfaulting without the lmul-patch?",
    "created_at": "2011-09-28T13:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33913",
    "user": "SimonKing"
}
```

Attachment [trac4539_monomial_quotient.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_monomial_quotient.patch) by SimonKing created at 2011-09-28 13:18:13

Concerning [attachment:trac4539_monomial_quotient.patch]: I am not sure if it is the right thing to do. I think that monomial_quotient is a method that should be as fast as possible, since in some situations it is used very frequently. In these situations, it is always the case that one monomial *does* divide the other. Hence, for the application, it is a bad idea to have a redundant sanity test in monomial_quotient. I'd rather have it return a wrong result when using it in a wrong way.

Note that [attachment:trac4539_kwds.patch] is not needed for my patch - I already have *args in it.

We have already briefly discussed why I think that [attachment:trac4539_lmul.patch] probably is not a good approach: x._rmul_(c) and x._lmul_(c) (by specification of the coercion model) can assume that the argument c belongs to x.parent().base_ring(). In particular, I don't believe that c can actually be a non-commutative polynomial.

Can you please provide an example that was segfaulting without the lmul-patch?



---

archive/issue_comments_033914.json:
```json
{
    "body": "At least, when I use [attachment:trac4539_libplural_todo.patch] plus [attachment:trac4539_lmul.patch] on top of sage-4.7.3.alpha3-prerelease, then all tests in sage/rings/polynomial pass (except those that fail in the unpatched version as well).\n\nSince I believe that the monomial quotient patch does not do the right thing, I'd prefer to work on top of [attachment:trac4539_libplural_todo.patch] and [attachment:trac4539_lmul.patch], and concentrate on getting the lmul business right.",
    "created_at": "2011-09-28T13:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33914",
    "user": "SimonKing"
}
```

At least, when I use [attachment:trac4539_libplural_todo.patch] plus [attachment:trac4539_lmul.patch] on top of sage-4.7.3.alpha3-prerelease, then all tests in sage/rings/polynomial pass (except those that fail in the unpatched version as well).

Since I believe that the monomial quotient patch does not do the right thing, I'd prefer to work on top of [attachment:trac4539_libplural_todo.patch] and [attachment:trac4539_lmul.patch], and concentrate on getting the lmul business right.



---

archive/issue_comments_033915.json:
```json
{
    "body": "I can already confirm that ther *is* a segfault without the lmul patch. So, I'll try to analyse what arguments are passed to _rmul_ / _lmul_. If I remember correctly, polynomial rings do not use the current coercion model. Hence, it is perhaps no surprise that _rmul_ and _lmul_ do not do what we expect.",
    "created_at": "2011-09-28T13:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33915",
    "user": "SimonKing"
}
```

I can already confirm that ther *is* a segfault without the lmul patch. So, I'll try to analyse what arguments are passed to _rmul_ / _lmul_. If I remember correctly, polynomial rings do not use the current coercion model. Hence, it is perhaps no surprise that _rmul_ and _lmul_ do not do what we expect.



---

archive/issue_comments_033916.json:
```json
{
    "body": "It is very strange: Apparently, a different lmul method fixes the segfault. However, when I insert a print statement in the unpatched lmul method, then I find that it is actually not executed directly before segfaulting.\n\nAlexander, how did you found that a change in lmul could fix it?",
    "created_at": "2011-09-28T13:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33916",
    "user": "SimonKing"
}
```

It is very strange: Apparently, a different lmul method fixes the segfault. However, when I insert a print statement in the unpatched lmul method, then I find that it is actually not executed directly before segfaulting.

Alexander, how did you found that a change in lmul could fix it?



---

archive/issue_comments_033917.json:
```json
{
    "body": "Alexander has just explained the lmul problem to me. It was an oversight in the original patch, where self._lmul_(right) was calling right._rmul_(self), which is of course wrong, since the argument to _rmul_ must be an element of the base ring. It should correctly be self._rmul_(right).\n\nAlexander just told me that he agrees in dropping the (redundant) test in monomial_quotient.",
    "created_at": "2011-09-28T14:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33917",
    "user": "SimonKing"
}
```

Alexander has just explained the lmul problem to me. It was an oversight in the original patch, where self._lmul_(right) was calling right._rmul_(self), which is of course wrong, since the argument to _rmul_ must be an element of the base ring. It should correctly be self._rmul_(right).

Alexander just told me that he agrees in dropping the (redundant) test in monomial_quotient.



---

archive/issue_comments_033918.json:
```json
{
    "body": "Attachment [trac4539_libplural.2.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural.2.patch) by SimonKing created at 2011-09-28 14:10:45\n\nCombined patch relative to sage-4.7.2.alpha3 plus #7797 plus #11856",
    "created_at": "2011-09-28T14:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33918",
    "user": "SimonKing"
}
```

Attachment [trac4539_libplural.2.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural.2.patch) by SimonKing created at 2011-09-28 14:10:45

Combined patch relative to sage-4.7.2.alpha3 plus #7797 plus #11856



---

archive/issue_comments_033919.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-28T14:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33919",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033920.json:
```json
{
    "body": "The new [attachment:trac4539_libplural.2.patch] is stand-alone and is supposed to summarise the discussion we had here. I think it is ready to be reviewed (but as usual I didn't run the tests yet...).\n\nApply trac4539_libplural.2.patch",
    "created_at": "2011-09-28T14:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33920",
    "user": "SimonKing"
}
```

The new [attachment:trac4539_libplural.2.patch] is stand-alone and is supposed to summarise the discussion we had here. I think it is ready to be reviewed (but as usual I didn't run the tests yet...).

Apply trac4539_libplural.2.patch



---

archive/issue_comments_033921.json:
```json
{
    "body": "I get a doctest failure in sage/rings/polynomial/multi_polynomial_ideal.py. There, a protocol of a Gr\u00f6bner basis computation is printed where we do not expect it.\n\nThe problem: If one runs the test separately, it works fine:\n\n```\nsage: A.<x,y,z> = FreeAlgebra(QQ, 3)\nsage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})\nsage: H.inject_variables()\nDefining x, y, z\nsage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)\nsage: G = vector(I.gens()); G\n/mnt/local/king/SAGE/debug/sage-4.7.2.alpha3-prerelease/local/lib/python2.6/site-packages/sage/modules/free_module.py:366: UserWarning: You are constructing a free module   over a noncommutative ring. Sage does\n             not have a concept of left/right and both sided modules, so be careful. It's also\n             not guaranteed that all multiplications are done from the right side.\n  not guaranteed that all multiplications are done from the right side.\"\"\")\n/mnt/local/king/SAGE/debug/sage-4.7.2.alpha3-prerelease/local/lib/python2.6/site-packages/sage/modules/free_module.py:584: UserWarning: You are constructing a free module over a noncommutative ring. Sage does not have a concept of left/right and both sided modules be careful. It's also not guarantied that all multiplications are done from the right side.\n  warn(\"\"\"You are constructing a free module over a noncommutative ring. Sage does not have a concept of left/right and both sided modules be careful. It's also not guarantied that all multiplications are done from the right side.\"\"\")\n(y^2, x^2, z^2 - 1)\n```\n\n\nBut the same doctest executed as part of the doctest suite has a \n\n```\nstd in (0),(x,y),(dp(2),C)\n[4294967295:2]3ss4s6\n(S:2)--\nproduct criterion:1 chain criterion:0\n```\n\nprinted after (!!) the result.\n\nSo, apparently another test has a side effect. I tried to identify it (e.g., a test that sets verbosity and forgets to reset it), but I did not succeed.  Also I wonder why one first sees the result and only later sees the protocol.",
    "created_at": "2011-09-28T15:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33921",
    "user": "SimonKing"
}
```

I get a doctest failure in sage/rings/polynomial/multi_polynomial_ideal.py. There, a protocol of a Gröbner basis computation is printed where we do not expect it.

The problem: If one runs the test separately, it works fine:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H.inject_variables()
Defining x, y, z
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)
sage: G = vector(I.gens()); G
/mnt/local/king/SAGE/debug/sage-4.7.2.alpha3-prerelease/local/lib/python2.6/site-packages/sage/modules/free_module.py:366: UserWarning: You are constructing a free module   over a noncommutative ring. Sage does
             not have a concept of left/right and both sided modules, so be careful. It's also
             not guaranteed that all multiplications are done from the right side.
  not guaranteed that all multiplications are done from the right side.""")
/mnt/local/king/SAGE/debug/sage-4.7.2.alpha3-prerelease/local/lib/python2.6/site-packages/sage/modules/free_module.py:584: UserWarning: You are constructing a free module over a noncommutative ring. Sage does not have a concept of left/right and both sided modules be careful. It's also not guarantied that all multiplications are done from the right side.
  warn("""You are constructing a free module over a noncommutative ring. Sage does not have a concept of left/right and both sided modules be careful. It's also not guarantied that all multiplications are done from the right side.""")
(y^2, x^2, z^2 - 1)
```


But the same doctest executed as part of the doctest suite has a 

```
std in (0),(x,y),(dp(2),C)
[4294967295:2]3ss4s6
(S:2)--
product criterion:1 chain criterion:0
```

printed after (!!) the result.

So, apparently another test has a side effect. I tried to identify it (e.g., a test that sets verbosity and forgets to reset it), but I did not succeed.  Also I wonder why one first sees the result and only later sees the protocol.



---

archive/issue_comments_033922.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-09-28T15:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33922",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033923.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-28T17:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33923",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033924.json:
```json
{
    "body": "It turned out that I misinterpreted the error: The actual error was wrong line breaks in the expected warning message. The protocol from Singular is printed to stdout, and apparently it was just by accident (though reproducible) that I saw it in the test log.\n\nNote that the warning message misspells the word \"guaranteed\" (namely \"guarantied\"). I fixed that misspelling as well, and I also introduced nicer (I think) line breaks for the warning.\n\nGlad that this is fixed. I hope the tests pass by now.\n\nApply trac4539_libplural.patch",
    "created_at": "2011-09-28T17:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33924",
    "user": "SimonKing"
}
```

It turned out that I misinterpreted the error: The actual error was wrong line breaks in the expected warning message. The protocol from Singular is printed to stdout, and apparently it was just by accident (though reproducible) that I saw it in the test log.

Note that the warning message misspells the word "guaranteed" (namely "guarantied"). I fixed that misspelling as well, and I also introduced nicer (I think) line breaks for the warning.

Glad that this is fixed. I hope the tests pass by now.

Apply trac4539_libplural.patch



---

archive/issue_comments_033925.json:
```json
{
    "body": "Changing keywords from \"libsingular plural wrapper sd34\" to \"libsingular plural wrapper sd10 sd23.5 sd24 sd34\".",
    "created_at": "2011-09-28T17:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33925",
    "user": "SimonKing"
}
```

Changing keywords from "libsingular plural wrapper sd34" to "libsingular plural wrapper sd10 sd23.5 sd24 sd34".



---

archive/issue_comments_033926.json:
```json
{
    "body": "FWIW, all doctests pass for me, except those that fail with unpatched sage-4.7.2.alpha3-prerelease.\n\nBy the way: How should reviewing be done in this case? I have no overview who wrote what (i.e., who can *review* what), and I think many people contributed to it.\n\nIn [attachment:trac4539_libplural.patch], I added an author list. But is it exhaustive?",
    "created_at": "2011-09-28T17:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33926",
    "user": "SimonKing"
}
```

FWIW, all doctests pass for me, except those that fail with unpatched sage-4.7.2.alpha3-prerelease.

By the way: How should reviewing be done in this case? I have no overview who wrote what (i.e., who can *review* what), and I think many people contributed to it.

In [attachment:trac4539_libplural.patch], I added an author list. But is it exhaustive?



---

archive/issue_comments_033927.json:
```json
{
    "body": "Concerning reviewing: Would it be OK that we all comment whether we are happy with the current patch, and that it constitutes a positive review if all are happy with it and nobody has a veto? Martin seems to agree.",
    "created_at": "2011-09-28T18:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33927",
    "user": "SimonKing"
}
```

Concerning reviewing: Would it be OK that we all comment whether we are happy with the current patch, and that it constitutes a positive review if all are happy with it and nobody has a veto? Martin seems to agree.



---

archive/issue_comments_033928.json:
```json
{
    "body": "I am writing a reviewer patch, since several doc strings needs reformatting.\n\nQuestion:\n\nIn sage/algebras/free_algebra.py in the method g_algebra, I find the statement:\n\"By default is assumed, that two variables commute.\" I don't understand that statement. Is it meant \"If there are only two variables then they commute\"? Or \"Any two variables commute\" (hopefully not)? Or \"There are two variables that commute\" (but which)? Can you provide an example for that default, and also show how (if possible) the default can be overridden?",
    "created_at": "2011-09-28T18:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33928",
    "user": "SimonKing"
}
```

I am writing a reviewer patch, since several doc strings needs reformatting.

Question:

In sage/algebras/free_algebra.py in the method g_algebra, I find the statement:
"By default is assumed, that two variables commute." I don't understand that statement. Is it meant "If there are only two variables then they commute"? Or "Any two variables commute" (hopefully not)? Or "There are two variables that commute" (but which)? Can you provide an example for that default, and also show how (if possible) the default can be overridden?



---

archive/issue_comments_033929.json:
```json
{
    "body": "PS: The other statements\n\n```\n        - Coercion doesn't work yet, there is some cheating about assumptions\n        - The optional argument ``check`` controls checking the degeneracy conditions.\n          Furthermore, the default values interfere with non-degeneracy conditions.\n```\n\naren't clear to  me either. \n\n* What does \"cheating about assumptions\" mean (what are the assumptions)?\n* What exactly does not work in coercion (perhaps I can fix it?)?\n* What are \"the default values\" (the only default is `order=\"degrevlex\"`)?\n* How do they interfere with non-degeneracy conditions? What are these conditions?",
    "created_at": "2011-09-28T18:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33929",
    "user": "SimonKing"
}
```

PS: The other statements

```
        - Coercion doesn't work yet, there is some cheating about assumptions
        - The optional argument ``check`` controls checking the degeneracy conditions.
          Furthermore, the default values interfere with non-degeneracy conditions.
```

aren't clear to  me either. 

* What does "cheating about assumptions" mean (what are the assumptions)?
* What exactly does not work in coercion (perhaps I can fix it?)?
* What are "the default values" (the only default is `order="degrevlex"`)?
* How do they interfere with non-degeneracy conditions? What are these conditions?



---

archive/issue_comments_033930.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-09-28T18:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33930",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_033931.json:
```json
{
    "body": "Too bad. I forgot to apply my \"combined\" patch relative to #7797 (or at least to #11068). Needs work.",
    "created_at": "2011-09-28T18:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33931",
    "user": "SimonKing"
}
```

Too bad. I forgot to apply my "combined" patch relative to #7797 (or at least to #11068). Needs work.



---

archive/issue_comments_033932.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-28T19:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33932",
    "user": "SimonKing"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_033933.json:
```json
{
    "body": "I think that it would be better to just have #11068 as a dependency: We should use it (because it implements one- and twosided ideals), and in contrast to #7797 it has a positive review.",
    "created_at": "2011-09-28T19:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33933",
    "user": "SimonKing"
}
```

I think that it would be better to just have #11068 as a dependency: We should use it (because it implements one- and twosided ideals), and in contrast to #7797 it has a positive review.



---

archive/issue_comments_033934.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-09-28T19:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33934",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033935.json:
```json
{
    "body": "Here's a report on features that I implemented today (not posted yet), missing features, and I also have some questions for you:\n\n__Sidedness of ideals__\n\nBy #11068, we can have one- and two-sided ideals. Oleksander told me that Singular can only compute left or twosided Gr\u00f6bner bases. Therefore, I think non-commutative polynomial ideals should refuse to be right-sided. The default should be left ideal. If the ideal is defined as a two-sided ideal, then std should return the same as twostd. Here is an example:\n\n```\nsage: A.<x,y,z> = FreeAlgebra(QQ, 3)\nsage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})\nsage: H.inject_variables()\nDefining x, y, z\nsage: JL = H.ideal([x^3, y^3, z^3 - 4*z])\nsage: JL\nLeft Ideal (x^3, y^3, z^3 - 4*z) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: JL.std()\nLeft Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, 2*x*y*z - z^2 - 2*z, y^3, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: JT = H.ideal([x^3, y^3, z^3 - 4*z], side='twosided')\nsage: JT\nTwosided Ideal (x^3, y^3, z^3 - 4*z) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: JT.std()\nTwosided Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, y^2*z - 2*y^2, 2*x*y*z - z^2 - 2*z, x^2*z + 2*x^2, y^3, x*y^2 - y*z, x^2*y - x*z - 2*x, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: JT.std() == JL.twostd()\nTrue\n```\n\n\nI think that's a good solution.\n\n__Cache__\n\nI added a cached_method decorator to std and twostd - I guess it is obvious that the result of a GB computation should be cached.\n\n**Question:** Should g-algebras be unique parents? If you agree that they should be, then I can try to implement it.\n\n__Category__\n\nA proper initialisation of non-commutative polynomial rings in the category of algebras was missing and is now added:\n\n```\nsage: H._is_category_initialized()\nTrue\nsage: H.category()\nCategory of algebras over Rational Field\n```\n\n\n__Pickling__\n\nThe test suite does not pass. Among other things, pickling of g-algebras has simply been forgotten. This certainly must be fixed:\n\n```\nsage: dumps(H)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: expected string or Unicode object, NoneType found\n```\n\nIt could be that, by using a `UniqueFactory` or `UniqueRepresentation`, the pickling problem automatically vanishes. Otherwise, a `__reduce__` method must be implemented.\n\n__Generator names for g-algebras__\n\nIt should be possible to choose names in the `g_algebra()` method.\n\n__Quotients__\n\nThere is a custom `quotient()` method for g-algebras (not using #11068). The question is: Is that really a quotient? It isn't printed as such, and the quotient relations are not used in arithmetic nor in comparison:\n\n```\nsage: A.<x,y,z> = FreeAlgebra(QQ, 3)\nsage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})\nsage: H.inject_variables()\nDefining x, y, z\nsage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)\nsage: Q = H.quotient(I); Q\nNoncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: Q.relations()\n{y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: I.twostd()\nTwosided Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: Q.2^2\nz^2\nsage: Q.2^2 == Q.one_element()\nFalse\n```\n\n**Question:** Did I misinterprete it? Hence, is there a way to make Q show that `Q.2^2` is equal to one?\n\nOtherwise, the custom `quotient()` should be dropped. #11068 provides the framework for nc-quotient rings; one just needs to add a `I.reduce(p)` method to our ideals (which is missing anyway).\n\n__Doc strings__\n\nI fixed various wrong doc string formats. Of course, after the changes mentioned above, some doc tests need to be modified.",
    "created_at": "2011-09-29T00:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33935",
    "user": "SimonKing"
}
```

Here's a report on features that I implemented today (not posted yet), missing features, and I also have some questions for you:

__Sidedness of ideals__

By #11068, we can have one- and two-sided ideals. Oleksander told me that Singular can only compute left or twosided Gröbner bases. Therefore, I think non-commutative polynomial ideals should refuse to be right-sided. The default should be left ideal. If the ideal is defined as a two-sided ideal, then std should return the same as twostd. Here is an example:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H.inject_variables()
Defining x, y, z
sage: JL = H.ideal([x^3, y^3, z^3 - 4*z])
sage: JL
Left Ideal (x^3, y^3, z^3 - 4*z) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JL.std()
Left Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, 2*x*y*z - z^2 - 2*z, y^3, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT = H.ideal([x^3, y^3, z^3 - 4*z], side='twosided')
sage: JT
Twosided Ideal (x^3, y^3, z^3 - 4*z) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT.std()
Twosided Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, y^2*z - 2*y^2, 2*x*y*z - z^2 - 2*z, x^2*z + 2*x^2, y^3, x*y^2 - y*z, x^2*y - x*z - 2*x, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT.std() == JL.twostd()
True
```


I think that's a good solution.

__Cache__

I added a cached_method decorator to std and twostd - I guess it is obvious that the result of a GB computation should be cached.

**Question:** Should g-algebras be unique parents? If you agree that they should be, then I can try to implement it.

__Category__

A proper initialisation of non-commutative polynomial rings in the category of algebras was missing and is now added:

```
sage: H._is_category_initialized()
True
sage: H.category()
Category of algebras over Rational Field
```


__Pickling__

The test suite does not pass. Among other things, pickling of g-algebras has simply been forgotten. This certainly must be fixed:

```
sage: dumps(H)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: expected string or Unicode object, NoneType found
```

It could be that, by using a `UniqueFactory` or `UniqueRepresentation`, the pickling problem automatically vanishes. Otherwise, a `__reduce__` method must be implemented.

__Generator names for g-algebras__

It should be possible to choose names in the `g_algebra()` method.

__Quotients__

There is a custom `quotient()` method for g-algebras (not using #11068). The question is: Is that really a quotient? It isn't printed as such, and the quotient relations are not used in arithmetic nor in comparison:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H.inject_variables()
Defining x, y, z
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)
sage: Q = H.quotient(I); Q
Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: Q.relations()
{y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: I.twostd()
Twosided Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: Q.2^2
z^2
sage: Q.2^2 == Q.one_element()
False
```

**Question:** Did I misinterprete it? Hence, is there a way to make Q show that `Q.2^2` is equal to one?

Otherwise, the custom `quotient()` should be dropped. #11068 provides the framework for nc-quotient rings; one just needs to add a `I.reduce(p)` method to our ideals (which is missing anyway).

__Doc strings__

I fixed various wrong doc string formats. Of course, after the changes mentioned above, some doc tests need to be modified.



---

archive/issue_comments_033936.json:
```json
{
    "body": "Attachment [trac4539_libplural.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural.patch) by SimonKing created at 2011-09-29 08:10:33\n\nCombined patch relative to sage-4.7.2.alpha3 plus #11068 plus #11856",
    "created_at": "2011-09-29T08:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33936",
    "user": "SimonKing"
}
```

Attachment [trac4539_libplural.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural.patch) by SimonKing created at 2011-09-29 08:10:33

Combined patch relative to sage-4.7.2.alpha3 plus #11068 plus #11856



---

archive/issue_comments_033937.json:
```json
{
    "body": "New patch posted! It does what I have announced above. I suggest that the next step should be to provide pickling, possibly by using `UniqueRepresentation`.",
    "created_at": "2011-09-29T08:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33937",
    "user": "SimonKing"
}
```

New patch posted! It does what I have announced above. I suggest that the next step should be to provide pickling, possibly by using `UniqueRepresentation`.



---

archive/issue_comments_033938.json:
```json
{
    "body": "The patch that I have just attached provides uniqueness of the parent (using a `UniqueFactory`) and pickling for nc rings and polynomials.\n\nIn short:\n\n```\nsage: A.<x,y,z> = FreeAlgebra(QQ, 3)\nsage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})\nsage: H is loads(dumps(H))\nTrue\nsage: TestSuite(H).run()\n```\n\n\nDoc tests still need to be updated, though. I also think that normal form computation should be easy to implement.\n\nApply trac4539_libplural.patch trac4539_pickling.patch",
    "created_at": "2011-09-29T10:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33938",
    "user": "SimonKing"
}
```

The patch that I have just attached provides uniqueness of the parent (using a `UniqueFactory`) and pickling for nc rings and polynomials.

In short:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: H is loads(dumps(H))
True
sage: TestSuite(H).run()
```


Doc tests still need to be updated, though. I also think that normal form computation should be easy to implement.

Apply trac4539_libplural.patch trac4539_pickling.patch



---

archive/issue_comments_033939.json:
```json
{
    "body": "Attachment [trac4539_pickling.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_pickling.patch) by SimonKing created at 2011-09-29 12:28:22\n\nPickling of nc rings and polynomials",
    "created_at": "2011-09-29T12:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33939",
    "user": "SimonKing"
}
```

Attachment [trac4539_pickling.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_pickling.patch) by SimonKing created at 2011-09-29 12:28:22

Pickling of nc rings and polynomials



---

archive/issue_comments_033940.json:
```json
{
    "body": "I have updated the second patch (adding a commit message), and I added a third patch. It provides a non-commutative \"Gr\u00f6bner strategy\", normal form computation, and thus quotient rings of g-algebras.\n\nNote that the quotients use the general framework from #11068. They *should* simply be g-algebras as well. But I suggest that this will be done on a different ticket.\n\nWith the new patch, one can do:\n\n```\nsage: A.<x,y,z> = FreeAlgebra(QQ, 3)\nsage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})\nsage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False, side='twosided')\nsage: Q = H.quotient(I); Q\nQuotient of Noncommutative Multivariate Polynomial Ring in x, y, z\nover Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y,\nz*x: x*z + 2*x} by the ideal (y^2, x^2, z^2 - 1)\nsage: Q.2^2 == Q.one_element()   # indirect doctest\nTrue\n```\n\nHere, we see that the relation that we just found in the quotient is actually a consequence of the given relations:\n\n```\nsage: I.twostd()\nTwosided Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2)\nof Noncommutative Multivariate Polynomial Ring in x, y, z over\nRational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\n```\n\n\nNote that reduction of polynomials by a list of polynomials is, in general, not a normal form. However, reduction of a polynomial by an ideal uses a two-sided Gr\u00f6bner basis and is thus a normal form.\n\nI just thought that it would better be reduction by a left Gr\u00f6bner basis, if the ideal is just a left ideal. OK, doing it soon...\n\nApply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch",
    "created_at": "2011-09-29T12:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33940",
    "user": "SimonKing"
}
```

I have updated the second patch (adding a commit message), and I added a third patch. It provides a non-commutative "Gröbner strategy", normal form computation, and thus quotient rings of g-algebras.

Note that the quotients use the general framework from #11068. They *should* simply be g-algebras as well. But I suggest that this will be done on a different ticket.

With the new patch, one can do:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False, side='twosided')
sage: Q = H.quotient(I); Q
Quotient of Noncommutative Multivariate Polynomial Ring in x, y, z
over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y,
z*x: x*z + 2*x} by the ideal (y^2, x^2, z^2 - 1)
sage: Q.2^2 == Q.one_element()   # indirect doctest
True
```

Here, we see that the relation that we just found in the quotient is actually a consequence of the given relations:

```
sage: I.twostd()
Twosided Ideal (z^2 - 1, y*z - y, x*z + x, y^2, 2*x*y - z - 1, x^2)
of Noncommutative Multivariate Polynomial Ring in x, y, z over
Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
```


Note that reduction of polynomials by a list of polynomials is, in general, not a normal form. However, reduction of a polynomial by an ideal uses a two-sided Gröbner basis and is thus a normal form.

I just thought that it would better be reduction by a left Gröbner basis, if the ideal is just a left ideal. OK, doing it soon...

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch



---

archive/issue_comments_033941.json:
```json
{
    "body": "The third patch is now modified, so that reduction wrt a left ideal is computed with a left (not a two-sided) Gr\u00f6bner basis.\n\nIt needs work, since the documentation is not complete and since certainly several doc tests need to be modified. But feel free to test the new patches...",
    "created_at": "2011-09-29T12:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33941",
    "user": "SimonKing"
}
```

The third patch is now modified, so that reduction wrt a left ideal is computed with a left (not a two-sided) Gröbner basis.

It needs work, since the documentation is not complete and since certainly several doc tests need to be modified. But feel free to test the new patches...



---

archive/issue_comments_033942.json:
```json
{
    "body": "Normal forms, quotient rings, and ideal containment",
    "created_at": "2011-09-29T12:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33942",
    "user": "SimonKing"
}
```

Normal forms, quotient rings, and ideal containment



---

archive/issue_comments_033943.json:
```json
{
    "body": "Attachment [trac4539_normal_forms.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_normal_forms.patch) by SimonKing created at 2011-09-29 12:56:09\n\nSorry, I couldn't resist to add one more feature: Ideal containment, which is a direct application of normal form computation.\n\nWith the new version of the third patch, we have:\n\n```\nsage: A.<x,y,z> = FreeAlgebra(QQ, 3)\nsage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})\nsage: JL = H.ideal([x^3, y^3, z^3 - 4*z])\nsage: JL.std()\nLeft Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, 2*x*y*z - z^2 - 2*z, y^3, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\nsage: JT = H.ideal([x^3, y^3, z^3 - 4*z], side='twosided')\nsage: JT.std()\nTwosided Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, y^2*z - 2*y^2, 2*x*y*z - z^2 - 2*z, x^2*z + 2*x^2, y^3, x*y^2 - y*z, x^2*y - x*z - 2*x, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}\n```\n\nApparently, ``x*y^2-y*z`` should be in the two-sided, but not in the left ideal. And that is indeed what we get:\n\n```\nsage: x*y^2-y*z in JL\nFalse\nsage: x*y^2-y*z in JT\nTrue\n```\n\n\nDocs are still to fix. And I promise to focus on it - no new features...\n\nApply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch",
    "created_at": "2011-09-29T12:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33943",
    "user": "SimonKing"
}
```

Attachment [trac4539_normal_forms.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_normal_forms.patch) by SimonKing created at 2011-09-29 12:56:09

Sorry, I couldn't resist to add one more feature: Ideal containment, which is a direct application of normal form computation.

With the new version of the third patch, we have:

```
sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
sage: H.<x,y,z> = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
sage: JL = H.ideal([x^3, y^3, z^3 - 4*z])
sage: JL.std()
Left Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, 2*x*y*z - z^2 - 2*z, y^3, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
sage: JT = H.ideal([x^3, y^3, z^3 - 4*z], side='twosided')
sage: JT.std()
Twosided Ideal (z^3 - 4*z, y*z^2 - 2*y*z, x*z^2 + 2*x*z, y^2*z - 2*y^2, 2*x*y*z - z^2 - 2*z, x^2*z + 2*x^2, y^3, x*y^2 - y*z, x^2*y - x*z - 2*x, x^3) of Noncommutative Multivariate Polynomial Ring in x, y, z over Rational Field, nc-relations: {y*x: x*y - z, z*y: y*z - 2*y, z*x: x*z + 2*x}
```

Apparently, ``x*y^2-y*z`` should be in the two-sided, but not in the left ideal. And that is indeed what we get:

```
sage: x*y^2-y*z in JL
False
sage: x*y^2-y*z in JT
True
```


Docs are still to fix. And I promise to focus on it - no new features...

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch



---

archive/issue_comments_033944.json:
```json
{
    "body": "The fourth patch does not provide a new feature, but only fixes of bugs, of the doc string formatting, and of the doc tests.\n\nSince I do not have Sage locally, I'd appreciate if one of you could build the documentation and see if it looks nice.\n\nNot a feature, but a fix concerns the hash: If one constructs a g-algebra as one is supposed to (`g_algeba` method resp. unique factory) then the g-algebra is a unique parent. Hence, `id(self)` is a good hash for it, and `__cmp__` can be removed.\n\nNote that the hash in Sage is allowed to change from session to session, so, `id(self)` is fine - see `UniqueRepresentation.__hash__`. Of course, one can destroy the uniqueness on purpose, but that's  not our problem.\n\nTests in sage/libs/singular, multi_polynomial_ideal.py and plural.pyx pass. I am now running all doc tests, but I think it is OK to put it as \"needs review\".\n\nConcerning review: I think we should review each other's code. So, in particular, one of you should please review my last three patches.\n\nPlease verify if I got the credits (author list) right.\n\nApply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch trac4539_fix_docs.patch",
    "created_at": "2011-09-29T15:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33944",
    "user": "SimonKing"
}
```

The fourth patch does not provide a new feature, but only fixes of bugs, of the doc string formatting, and of the doc tests.

Since I do not have Sage locally, I'd appreciate if one of you could build the documentation and see if it looks nice.

Not a feature, but a fix concerns the hash: If one constructs a g-algebra as one is supposed to (`g_algeba` method resp. unique factory) then the g-algebra is a unique parent. Hence, `id(self)` is a good hash for it, and `__cmp__` can be removed.

Note that the hash in Sage is allowed to change from session to session, so, `id(self)` is fine - see `UniqueRepresentation.__hash__`. Of course, one can destroy the uniqueness on purpose, but that's  not our problem.

Tests in sage/libs/singular, multi_polynomial_ideal.py and plural.pyx pass. I am now running all doc tests, but I think it is OK to put it as "needs review".

Concerning review: I think we should review each other's code. So, in particular, one of you should please review my last three patches.

Please verify if I got the credits (author list) right.

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch trac4539_fix_docs.patch



---

archive/issue_comments_033945.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-29T15:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33945",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033946.json:
```json
{
    "body": "Hoorray, only three errors, in sage/rings/noncommutative_ideal.pyx! That should be doable before dinner.",
    "created_at": "2011-09-29T15:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33946",
    "user": "SimonKing"
}
```

Hoorray, only three errors, in sage/rings/noncommutative_ideal.pyx! That should be doable before dinner.



---

archive/issue_comments_033947.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-09-29T15:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33947",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033948.json:
```json
{
    "body": "Fixing doc strings and doc tests",
    "created_at": "2011-09-29T16:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33948",
    "user": "SimonKing"
}
```

Fixing doc strings and doc tests



---

archive/issue_comments_033949.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-29T16:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33949",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033950.json:
```json
{
    "body": "Attachment [trac4539_fix_docs.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs.patch) by SimonKing created at 2011-09-29 16:32:53\n\nIt turned out that the element constructor of ideal monoids changed a left ideal into a twosided ideal, which (together with the missing uniqueness of ideal monoids) led to errors in a `loads(dumps(...)==...` test.\n\nI hope all tests will pass by now!\n\nApply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch trac4539_fix_docs.patch",
    "created_at": "2011-09-29T16:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33950",
    "user": "SimonKing"
}
```

Attachment [trac4539_fix_docs.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs.patch) by SimonKing created at 2011-09-29 16:32:53

It turned out that the element constructor of ideal monoids changed a left ideal into a twosided ideal, which (together with the missing uniqueness of ideal monoids) led to errors in a `loads(dumps(...)==...` test.

I hope all tests will pass by now!

Apply trac4539_libplural.patch trac4539_pickling.patch trac4539_normal_forms.patch trac4539_fix_docs.patch



---

archive/issue_comments_033951.json:
```json
{
    "body": "Replying to [comment:83 SimonKing]:\n> I hope all tests will pass by now!\n\nThey do!",
    "created_at": "2011-09-29T20:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33951",
    "user": "SimonKing"
}
```

Replying to [comment:83 SimonKing]:
> I hope all tests will pass by now!

They do!



---

archive/issue_comments_033952.json:
```json
{
    "body": "I checked the patches, the look good indeed. So a positive review for the mathematical part. I'm starting doc tests now.",
    "created_at": "2011-09-29T21:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33952",
    "user": "AlexanderDreyer"
}
```

I checked the patches, the look good indeed. So a positive review for the mathematical part. I'm starting doc tests now.



---

archive/issue_comments_033953.json:
```json
{
    "body": "Hm, trac4539_fix_docs.patch doesn't apply cleanly, maybe i used the  wrong order. What does the following tell you?\n`hg qseries`",
    "created_at": "2011-09-29T22:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33953",
    "user": "AlexanderDreyer"
}
```

Hm, trac4539_fix_docs.patch doesn't apply cleanly, maybe i used the  wrong order. What does the following tell you?
`hg qseries`



---

archive/issue_comments_033954.json:
```json
{
    "body": "Replying to [comment:86 AlexanderDreyer]:\n> Hm, trac4539_fix_docs.patch doesn't apply cleanly, maybe i used the  wrong order. What does the following tell you?\n\n```\nhg qseries\ntrac11815_format_must_preserve_embedding.patch\ntrac11817_question_mark_using_sage_getdoc.patch\ntrac11768_source_of_dynamic_class.patch\ntrac11115-cached_cython.patch\ntrac11115_element_with_cache.patch\ntrac11115_cached_function_pickling.patch\ntrac11791_dynamic_metaclass_introspection.patch\ntrac11780_unique_auxiliar_polyring.patch\ntrac11856_exponent_overflow.patch\ntrac11068_nc_ideals_and_quotients.patch\ntrac11068_quotient_ring_without_names.patch\ntrac11068_lifting_map.patch\ntrac4539_libplural.patch\ntrac4539_pickling.patch\ntrac4539_normal_forms.patch\ntrac4539_fix_docs.patch\n```\n\n\nSo, as you can see, I indeed have more stuff applied in front of the plural patches. I will try to see what went wrong.",
    "created_at": "2011-09-30T06:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33954",
    "user": "SimonKing"
}
```

Replying to [comment:86 AlexanderDreyer]:
> Hm, trac4539_fix_docs.patch doesn't apply cleanly, maybe i used the  wrong order. What does the following tell you?

```
hg qseries
trac11815_format_must_preserve_embedding.patch
trac11817_question_mark_using_sage_getdoc.patch
trac11768_source_of_dynamic_class.patch
trac11115-cached_cython.patch
trac11115_element_with_cache.patch
trac11115_cached_function_pickling.patch
trac11791_dynamic_metaclass_introspection.patch
trac11780_unique_auxiliar_polyring.patch
trac11856_exponent_overflow.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac4539_libplural.patch
trac4539_pickling.patch
trac4539_normal_forms.patch
trac4539_fix_docs.patch
```


So, as you can see, I indeed have more stuff applied in front of the plural patches. I will try to see what went wrong.



---

archive/issue_comments_033955.json:
```json
{
    "body": "I can not confirm Alexander's statement that some patch does not apply.\n\nI cleaned my patch queue, so that I only use the patches that are dependencies. Now, I have\n\n```\n$ hg qapplied\ntrac11815_format_must_preserve_embedding.patch\ntrac11115-cached_cython.patch\ntrac11115_element_with_cache.patch\ntrac11115_cached_function_pickling.patch\ntrac11068_nc_ideals_and_quotients.patch\ntrac11068_quotient_ring_without_names.patch\ntrac11068_lifting_map.patch\ntrac11856_exponent_overflow.patch\ntrac4539_libplural.patch\ntrac4539_pickling.patch\ntrac4539_normal_forms.patch\ntrac4539_fix_docs.patch\n```\n\non top of sage-4.7.2.alpha3-prerelease.\n\nOne remark: It happened to me recently that I tried to qimport a patch from trac, but my university had a proxy, and for some reason it thought that the patch is cached. I therefore switched the cache off, for the computer in my office. That is where I test the patches.\n\nBut Burcin just told me that they have a proxy here as well. So, could it be that you tried to download the latest patch version, but your proxy only provided you with a cached but outdated version of the patches?\n\nThe other possibility is that I thought I have posted the patch version that I have on my computer in my office, but in fact posted an outdated version that I have on my netbook here. Testing it now.",
    "created_at": "2011-09-30T08:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33955",
    "user": "SimonKing"
}
```

I can not confirm Alexander's statement that some patch does not apply.

I cleaned my patch queue, so that I only use the patches that are dependencies. Now, I have

```
$ hg qapplied
trac11815_format_must_preserve_embedding.patch
trac11115-cached_cython.patch
trac11115_element_with_cache.patch
trac11115_cached_function_pickling.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac11856_exponent_overflow.patch
trac4539_libplural.patch
trac4539_pickling.patch
trac4539_normal_forms.patch
trac4539_fix_docs.patch
```

on top of sage-4.7.2.alpha3-prerelease.

One remark: It happened to me recently that I tried to qimport a patch from trac, but my university had a proxy, and for some reason it thought that the patch is cached. I therefore switched the cache off, for the computer in my office. That is where I test the patches.

But Burcin just told me that they have a proxy here as well. So, could it be that you tried to download the latest patch version, but your proxy only provided you with a cached but outdated version of the patches?

The other possibility is that I thought I have posted the patch version that I have on my computer in my office, but in fact posted an outdated version that I have on my netbook here. Testing it now.



---

archive/issue_comments_033956.json:
```json
{
    "body": "See #11878 for quotients of g-algebras.",
    "created_at": "2011-09-30T09:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33956",
    "user": "SimonKing"
}
```

See #11878 for quotients of g-algebras.



---

archive/issue_comments_033957.json:
```json
{
    "body": "Replying to [comment:88 SimonKing]:\n> I can not confirm Alexander's statement that some patch does not apply.\nYeah, I just mixed up the order of the following patches:\n> trac4539_pickling.patch\n> trac4539_normal_forms.patch\nAlready the first didn't apply cleanly, but I overlooked. It built fine and the tests are running.",
    "created_at": "2011-09-30T10:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33957",
    "user": "AlexanderDreyer"
}
```

Replying to [comment:88 SimonKing]:
> I can not confirm Alexander's statement that some patch does not apply.
Yeah, I just mixed up the order of the following patches:
> trac4539_pickling.patch
> trac4539_normal_forms.patch
Already the first didn't apply cleanly, but I overlooked. It built fine and the tests are running.



---

archive/issue_comments_033958.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-09-30T12:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33958",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_033959.json:
```json
{
    "body": "I found that the function `new_NRing`, that is supposed to return a valid `NCPolynomialRing_plural` out of a ring wrap, is broken. Important data, namely the matrices c and d, are left as `None`. Hence, for a ring produced with `new_NRing`, pickling won't work at all.\n\nThe question is whether we can leave it broken for now, and fix it separately, or leave this ticket open and \"needs work\". How shall we proceed?",
    "created_at": "2011-09-30T12:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33959",
    "user": "SimonKing"
}
```

I found that the function `new_NRing`, that is supposed to return a valid `NCPolynomialRing_plural` out of a ring wrap, is broken. Important data, namely the matrices c and d, are left as `None`. Hence, for a ring produced with `new_NRing`, pickling won't work at all.

The question is whether we can leave it broken for now, and fix it separately, or leave this ticket open and "needs work". How shall we proceed?



---

archive/issue_comments_033960.json:
```json
{
    "body": "PS: Even *if* it returns a valid picklable ring, uniqueness of parents would break. So, we should analyse whether `new_NRing` is used in a critical (uniqueness-breaking) way in the current patch.",
    "created_at": "2011-09-30T12:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33960",
    "user": "SimonKing"
}
```

PS: Even *if* it returns a valid picklable ring, uniqueness of parents would break. So, we should analyse whether `new_NRing` is used in a critical (uniqueness-breaking) way in the current patch.



---

archive/issue_comments_033961.json:
```json
{
    "body": "Replying to [comment:92 SimonKing]:\n> PS: Even *if* it returns a valid picklable ring, uniqueness of parents would break. So, we should analyse whether `new_NRing` is used in a critical (uniqueness-breaking) way in the current patch.\n\nIt concerncs the `SCA` function and the original approach towards quotients.",
    "created_at": "2011-09-30T12:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33961",
    "user": "SimonKing"
}
```

Replying to [comment:92 SimonKing]:
> PS: Even *if* it returns a valid picklable ring, uniqueness of parents would break. So, we should analyse whether `new_NRing` is used in a critical (uniqueness-breaking) way in the current patch.

It concerncs the `SCA` function and the original approach towards quotients.



---

archive/issue_comments_033962.json:
```json
{
    "body": "I suggest that we leave stuff as it is now, so that it can be merged and we can build on top of it. Therefore, I revert it to \"needs review\".\n\nIf I am not mistaken, `SCA` is a special case in Singular anyway, and it is a huge difference whether one works in an `SCA` or in an isomorphic general g-algebra quotient (Oleksandr, could you tell how the ring should be created in this case? I guess the function `SCA` in the patch does not do the right thing).\n\nI believe that there should be a sub-class of `NCPolynomialRing_plural` for general quotients of g-algebras, and then a sub-sub-class for SCA that uses the specialised implementation from Singular. But that should be on #11878.",
    "created_at": "2011-09-30T14:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33962",
    "user": "SimonKing"
}
```

I suggest that we leave stuff as it is now, so that it can be merged and we can build on top of it. Therefore, I revert it to "needs review".

If I am not mistaken, `SCA` is a special case in Singular anyway, and it is a huge difference whether one works in an `SCA` or in an isomorphic general g-algebra quotient (Oleksandr, could you tell how the ring should be created in this case? I guess the function `SCA` in the patch does not do the right thing).

I believe that there should be a sub-class of `NCPolynomialRing_plural` for general quotients of g-algebras, and then a sub-sub-class for SCA that uses the specialised implementation from Singular. But that should be on #11878.



---

archive/issue_comments_033963.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-09-30T14:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33963",
    "user": "SimonKing"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_033964.json:
```json
{
    "body": "Replying to [comment:94 SimonKing]:\n> If I am not mistaken, `SCA` is a special case in Singular anyway, and it is a huge difference whether one works in an `SCA` or in an isomorphic general g-algebra quotient (Oleksandr, could you tell how the ring should be created in this case? I guess the function `SCA` in the patch does not do the right thing).\n\nSCA structure is _autodetected_ upon creation of a GR-algebra (`qring`) in runtime. Therefore one should not use an extra method for this: just create a GRing and its quotient by correct twosided ideal there.\n\nTest: if SCA implementation is used then `y*y == 0;` for each non-commutative (odd degree) variable `y`.",
    "created_at": "2011-09-30T15:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33964",
    "user": "OleksandrMotsak"
}
```

Replying to [comment:94 SimonKing]:
> If I am not mistaken, `SCA` is a special case in Singular anyway, and it is a huge difference whether one works in an `SCA` or in an isomorphic general g-algebra quotient (Oleksandr, could you tell how the ring should be created in this case? I guess the function `SCA` in the patch does not do the right thing).

SCA structure is _autodetected_ upon creation of a GR-algebra (`qring`) in runtime. Therefore one should not use an extra method for this: just create a GRing and its quotient by correct twosided ideal there.

Test: if SCA implementation is used then `y*y == 0;` for each non-commutative (odd degree) variable `y`.



---

archive/issue_comments_033965.json:
```json
{
    "body": "Attachment [trac4539_fix_docs_32bit.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs_32bit.patch) by AlexanderDreyer created at 2011-09-30 21:50:51\n\nFixed one doc test which faild in 32 bit",
    "created_at": "2011-09-30T21:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33965",
    "user": "AlexanderDreyer"
}
```

Attachment [trac4539_fix_docs_32bit.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs_32bit.patch) by AlexanderDreyer created at 2011-09-30 21:50:51

Fixed one doc test which faild in 32 bit



---

archive/issue_comments_033966.json:
```json
{
    "body": "One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch. Since we postponed the quotient issue, I think I can give a positive review for Simon's work as well as for Michael's, Burcin's and Oleksandr's part , which I reviewed on SD24.\n\n`@`Simon: If you accept my part we would have a positive review now.",
    "created_at": "2011-09-30T21:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33966",
    "user": "AlexanderDreyer"
}
```

One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch. Since we postponed the quotient issue, I think I can give a positive review for Simon's work as well as for Michael's, Burcin's and Oleksandr's part , which I reviewed on SD24.

`@`Simon: If you accept my part we would have a positive review now.



---

archive/issue_comments_033967.json:
```json
{
    "body": "Replying to [comment:96 AlexanderDreyer]:\n> One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch.\n\nIt looks like this error already occurs #11856 - can you verify whether the error occurs on 32-bit with #11856? Then it might be better to post your patch there.\n\n> `@`Simon: If you accept my part we would have a positive review now.\n\nThe \"big\" patch merely combines work of y'all, and I certainly give the stuff there a positive review. However, the question on #11856 should first be answered.",
    "created_at": "2011-10-01T09:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33967",
    "user": "SimonKing"
}
```

Replying to [comment:96 AlexanderDreyer]:
> One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch.

It looks like this error already occurs #11856 - can you verify whether the error occurs on 32-bit with #11856? Then it might be better to post your patch there.

> `@`Simon: If you accept my part we would have a positive review now.

The "big" patch merely combines work of y'all, and I certainly give the stuff there a positive review. However, the question on #11856 should first be answered.



---

archive/issue_comments_033968.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-10-01T09:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33968",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_033969.json:
```json
{
    "body": "Replying to [comment:97 SimonKing]:\n> Replying to [comment:96 AlexanderDreyer]:\n> > One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch.\n> \n> It looks like this error already occurs #11856 - can you verify whether the error occurs on 32-bit with #11856? Then it might be better to post your patch there.\nIndeed, I already had to apply http://trac.sagemath.org/sage_trac/attachment/ticket/4539/trac4539_fix_docs_32bit.patch to #11856 on 32-bit systems.",
    "created_at": "2011-10-01T22:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33969",
    "user": "AlexanderDreyer"
}
```

Replying to [comment:97 SimonKing]:
> Replying to [comment:96 AlexanderDreyer]:
> > One doctest failed on OSX 10.5 PPC. This is fixed in the attached patch.
> 
> It looks like this error already occurs #11856 - can you verify whether the error occurs on 32-bit with #11856? Then it might be better to post your patch there.
Indeed, I already had to apply http://trac.sagemath.org/sage_trac/attachment/ticket/4539/trac4539_fix_docs_32bit.patch to #11856 on 32-bit systems.



---

archive/issue_comments_033970.json:
```json
{
    "body": "Replying to [comment:98 AlexanderDreyer]:\n> Indeed, I already had to apply http://trac.sagemath.org/sage_trac/attachment/ticket/4539/trac4539_fix_docs_32bit.patch to #11856 on 32-bit systems.\n\nOK, then [attachment:trac4539_fix_docs_32bit.patch] should better be moved to #11856 - since it only concerns doctests in the obvious way, but does not change the code, I think that your patch can be a reviewer patch for #11856, thus, preserving the positive review that Martin gave (but then add your name in the \"Reviewer\" field of #11856).\n\nIf that's done, then I'll try the stuff from here again, and then hopefully it can be turned into a positive review.",
    "created_at": "2011-10-02T06:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33970",
    "user": "SimonKing"
}
```

Replying to [comment:98 AlexanderDreyer]:
> Indeed, I already had to apply http://trac.sagemath.org/sage_trac/attachment/ticket/4539/trac4539_fix_docs_32bit.patch to #11856 on 32-bit systems.

OK, then [attachment:trac4539_fix_docs_32bit.patch] should better be moved to #11856 - since it only concerns doctests in the obvious way, but does not change the code, I think that your patch can be a reviewer patch for #11856, thus, preserving the positive review that Martin gave (but then add your name in the "Reviewer" field of #11856).

If that's done, then I'll try the stuff from here again, and then hopefully it can be turned into a positive review.



---

archive/issue_comments_033971.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-10-02T21:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33971",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_033972.json:
```json
{
    "body": "Now 32 bit issue was solved in #11856 (and has positive review again).",
    "created_at": "2011-10-02T21:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33972",
    "user": "AlexanderDreyer"
}
```

Now 32 bit issue was solved in #11856 (and has positive review again).



---

archive/issue_comments_033973.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-02T21:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33973",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033974.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-10-04T17:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33974",
    "user": "SimonKing"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_033975.json:
```json
{
    "body": "Too bad. I was asked to rebase #11586 and #11068 with respect  to #11339/#10903. By consequence, the patches from here need to be rebase as well. Needs work...",
    "created_at": "2011-10-04T17:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33975",
    "user": "SimonKing"
}
```

Too bad. I was asked to rebase #11586 and #11068 with respect  to #11339/#10903. By consequence, the patches from here need to be rebase as well. Needs work...



---

archive/issue_comments_033976.json:
```json
{
    "body": "It is not going to be easy. #11339 and #10903 have removed some functions (eg., `n_IsOne`) that are needed here. So, I need to find out where it was imported from.",
    "created_at": "2011-10-04T18:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33976",
    "user": "SimonKing"
}
```

It is not going to be easy. #11339 and #10903 have removed some functions (eg., `n_IsOne`) that are needed here. So, I need to find out where it was imported from.



---

archive/issue_comments_033977.json:
```json
{
    "body": "`n_IsOne` was replaced by `ring.cf.nIsOne(foo)`. We didn't remove any functionality, only replaced it by calls which are more explicit about the ring. If in doubt just ask :)",
    "created_at": "2011-10-04T18:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33977",
    "user": "malb"
}
```

`n_IsOne` was replaced by `ring.cf.nIsOne(foo)`. We didn't remove any functionality, only replaced it by calls which are more explicit about the ring. If in doubt just ask :)



---

archive/issue_comments_033978.json:
```json
{
    "body": "Replying to [comment:105 malb]:\n> `n_IsOne` was replaced by `ring.cf.nIsOne(foo)`. We didn't remove any functionality, only replaced it by calls which are more explicit about the ring. If in doubt just ask :)\n\nYep, I already found the replacement (by doing a grep for `n_IsOne` in my `.hg/patches`, when I wanted to find out where that function came from).",
    "created_at": "2011-10-04T18:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33978",
    "user": "SimonKing"
}
```

Replying to [comment:105 malb]:
> `n_IsOne` was replaced by `ring.cf.nIsOne(foo)`. We didn't remove any functionality, only replaced it by calls which are more explicit about the ring. If in doubt just ask :)

Yep, I already found the replacement (by doing a grep for `n_IsOne` in my `.hg/patches`, when I wanted to find out where that function came from).



---

archive/issue_comments_033979.json:
```json
{
    "body": "I didn't post my rebased patches yet, since I need to fix a few doctest errors.\n\nActually, the first error is a clear improvement. We have the following doctest:\n\n```\n            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)\n            sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})\n            sage: H.inject_variables()\n            Defining x, y, z\n            sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)\n            sage: G = vector(I.gens()); G\n            d...: UserWarning: You are constructing a free module\n            over a noncommutative ring. Sage does not have a concept\n            of left/right and both sided modules, so be careful.\n            It's also not guaranteed that all multiplications are\n            done from the right side.\n            d...: UserWarning: You are constructing a free module\n            over a noncommutative ring. Sage does not have a concept\n            of left/right and both sided modules, so be careful.\n            It's also not guaranteed that all multiplications are\n            done from the right side.\n            (y^2, x^2, z^2 - 1)\n            sage: M = I.syzygy_module()\n```\n\n\nWith #10903 applied, one gets 9 Syzygies:\n\n```\nsage: M[0]\n(-z^2 - 8*z - 15, 0, y^2)\nsage: M[1]\n(0, -z^2 + 8*z - 15, x^2)\nsage: M[2]\n(x^2*z^2 + 8*x^2*z + 15*x^2, -y^2*z^2 + 8*y^2*z - 15*y^2, -4*x*y*z + 2*z^2 + 2*z)\nsage: M[3]\n(x^2*y*z^2 + 9*x^2*y*z - 6*x*z^3 + 20*x^2*y - 72*x*z^2 - 282*x*z - 360*x, -y^3*z^2 + 7*y^3*z - 12*y^3, 6*y*z^2)\nsage: M[4]\n(x^3*z^2 + 7*x^3*z + 12*x^3, -x*y^2*z^2 + 9*x*y^2*z - 4*y*z^3 - 20*x*y^2 + 52*y*z^2 - 224*y*z + 320*y, -6*x*z^2)\nsage: M[5]\n(x^2*y^2*z + 4*x^2*y^2 - 8*x*y*z^2 - 48*x*y*z + 12*z^3 - 64*x*y + 108*z^2 + 312*z + 288, -y^4*z + 4*y^4, 0)\nsage: M[6]\n(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)\nsage: M[7]\n(x^4*z + 4*x^4, -x^2*y^2*z + 4*x^2*y^2 - 4*x*y*z^2 + 32*x*y*z - 6*z^3 - 64*x*y + 66*z^2 - 240*z + 288, 0)\nsage: M[8]\n(x^3*y^2*z + 4*x^3*y^2 + 18*x^2*y*z - 36*x*z^3 + 66*x^2*y - 432*x*z^2 - 1656*x*z - 2052*x, -x*y^4*z + 4*x*y^4 - 8*y^3*z^2 + 62*y^3*z - 114*y^3, 48*y*z^2 - 36*y*z)\nsage: M[9]\nTraceback (most recent call last):\n...\nIndexError: matrix index out of range\n```\n\n\nHowever, without #10903 (and with the original patches applied), one gets what is expected in the doc tests, namely 10 Syzygies -- but two of them are identical:\n\n```\nsage: M[0]\n(-z^2 - 8*z - 15, 0, y^2)\nsage: M[1]\n(0, -z^2 + 8*z - 15, x^2)\nsage: M[2]\n(x^2*z^2 + 8*x^2*z + 15*x^2, -y^2*z^2 + 8*y^2*z - 15*y^2, -4*x*y*z + 2*z^2 + 2*z)\nsage: M[3]\n(x^2*y*z^2 + 9*x^2*y*z - 6*x*z^3 + 20*x^2*y - 72*x*z^2 - 282*x*z - 360*x, -y^3*z^2 + 7*y^3*z - 12*y^3, 6*y*z^2)\nsage: M[4]\n(x^3*z^2 + 7*x^3*z + 12*x^3, -x*y^2*z^2 + 9*x*y^2*z - 4*y*z^3 - 20*x*y^2 + 52*y*z^2 - 224*y*z + 320*y, -6*x*z^2)\nsage: M[5]\n(x^2*y^2*z + 4*x^2*y^2 - 8*x*y*z^2 - 48*x*y*z + 12*z^3 - 64*x*y + 108*z^2 + 312*z + 288, -y^4*z + 4*y^4, 0)\nsage: M[6]\n(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)\nsage: M[7]\n(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)\nsage: M[8]\n(x^4*z + 4*x^4, -x^2*y^2*z + 4*x^2*y^2 - 4*x*y*z^2 + 32*x*y*z - 6*z^3 - 64*x*y + 66*z^2 - 240*z + 288, 0)\nsage: M[9]\n(x^3*y^2*z + 4*x^3*y^2 + 18*x^2*y*z - 36*x*z^3 + 66*x^2*y - 432*x*z^2 - 1656*x*z - 2052*x, -x*y^4*z + 4*x*y^4 - 8*y^3*z^2 + 62*y^3*z - 114*y^3, 48*y*z^2 - 36*y*z)\nsage: M[7]==M[6]\nTrue\n```\n\n\nSo, the old Singular version forgot to remove a redundant Syzygy.",
    "created_at": "2011-10-05T08:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33979",
    "user": "SimonKing"
}
```

I didn't post my rebased patches yet, since I need to fix a few doctest errors.

Actually, the first error is a clear improvement. We have the following doctest:

```
            sage: A.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: H = A.g_algebra({y*x:x*y-z, z*x:x*z+2*x, z*y:y*z-2*y})
            sage: H.inject_variables()
            Defining x, y, z
            sage: I = H.ideal([y^2, x^2, z^2-H.one_element()],coerce=False)
            sage: G = vector(I.gens()); G
            d...: UserWarning: You are constructing a free module
            over a noncommutative ring. Sage does not have a concept
            of left/right and both sided modules, so be careful.
            It's also not guaranteed that all multiplications are
            done from the right side.
            d...: UserWarning: You are constructing a free module
            over a noncommutative ring. Sage does not have a concept
            of left/right and both sided modules, so be careful.
            It's also not guaranteed that all multiplications are
            done from the right side.
            (y^2, x^2, z^2 - 1)
            sage: M = I.syzygy_module()
```


With #10903 applied, one gets 9 Syzygies:

```
sage: M[0]
(-z^2 - 8*z - 15, 0, y^2)
sage: M[1]
(0, -z^2 + 8*z - 15, x^2)
sage: M[2]
(x^2*z^2 + 8*x^2*z + 15*x^2, -y^2*z^2 + 8*y^2*z - 15*y^2, -4*x*y*z + 2*z^2 + 2*z)
sage: M[3]
(x^2*y*z^2 + 9*x^2*y*z - 6*x*z^3 + 20*x^2*y - 72*x*z^2 - 282*x*z - 360*x, -y^3*z^2 + 7*y^3*z - 12*y^3, 6*y*z^2)
sage: M[4]
(x^3*z^2 + 7*x^3*z + 12*x^3, -x*y^2*z^2 + 9*x*y^2*z - 4*y*z^3 - 20*x*y^2 + 52*y*z^2 - 224*y*z + 320*y, -6*x*z^2)
sage: M[5]
(x^2*y^2*z + 4*x^2*y^2 - 8*x*y*z^2 - 48*x*y*z + 12*z^3 - 64*x*y + 108*z^2 + 312*z + 288, -y^4*z + 4*y^4, 0)
sage: M[6]
(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)
sage: M[7]
(x^4*z + 4*x^4, -x^2*y^2*z + 4*x^2*y^2 - 4*x*y*z^2 + 32*x*y*z - 6*z^3 - 64*x*y + 66*z^2 - 240*z + 288, 0)
sage: M[8]
(x^3*y^2*z + 4*x^3*y^2 + 18*x^2*y*z - 36*x*z^3 + 66*x^2*y - 432*x*z^2 - 1656*x*z - 2052*x, -x*y^4*z + 4*x*y^4 - 8*y^3*z^2 + 62*y^3*z - 114*y^3, 48*y*z^2 - 36*y*z)
sage: M[9]
Traceback (most recent call last):
...
IndexError: matrix index out of range
```


However, without #10903 (and with the original patches applied), one gets what is expected in the doc tests, namely 10 Syzygies -- but two of them are identical:

```
sage: M[0]
(-z^2 - 8*z - 15, 0, y^2)
sage: M[1]
(0, -z^2 + 8*z - 15, x^2)
sage: M[2]
(x^2*z^2 + 8*x^2*z + 15*x^2, -y^2*z^2 + 8*y^2*z - 15*y^2, -4*x*y*z + 2*z^2 + 2*z)
sage: M[3]
(x^2*y*z^2 + 9*x^2*y*z - 6*x*z^3 + 20*x^2*y - 72*x*z^2 - 282*x*z - 360*x, -y^3*z^2 + 7*y^3*z - 12*y^3, 6*y*z^2)
sage: M[4]
(x^3*z^2 + 7*x^3*z + 12*x^3, -x*y^2*z^2 + 9*x*y^2*z - 4*y*z^3 - 20*x*y^2 + 52*y*z^2 - 224*y*z + 320*y, -6*x*z^2)
sage: M[5]
(x^2*y^2*z + 4*x^2*y^2 - 8*x*y*z^2 - 48*x*y*z + 12*z^3 - 64*x*y + 108*z^2 + 312*z + 288, -y^4*z + 4*y^4, 0)
sage: M[6]
(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)
sage: M[7]
(2*x^3*y*z + 8*x^3*y + 9*x^2*z + 27*x^2, -2*x*y^3*z + 8*x*y^3 - 12*y^2*z^2 + 99*y^2*z - 195*y^2, -36*x*y*z + 24*z^2 + 18*z)
sage: M[8]
(x^4*z + 4*x^4, -x^2*y^2*z + 4*x^2*y^2 - 4*x*y*z^2 + 32*x*y*z - 6*z^3 - 64*x*y + 66*z^2 - 240*z + 288, 0)
sage: M[9]
(x^3*y^2*z + 4*x^3*y^2 + 18*x^2*y*z - 36*x*z^3 + 66*x^2*y - 432*x*z^2 - 1656*x*z - 2052*x, -x*y^4*z + 4*x*y^4 - 8*y^3*z^2 + 62*y^3*z - 114*y^3, 48*y*z^2 - 36*y*z)
sage: M[7]==M[6]
True
```


So, the old Singular version forgot to remove a redundant Syzygy.



---

archive/issue_comments_033980.json:
```json
{
    "body": "Attachment [trac4539_libplural_rel10903.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural_rel10903.patch) by SimonKing created at 2011-10-05 08:12:32\n\nCombined patch relative to sage-4.7.2.alpha3 plus #11068, #11856 and #10903",
    "created_at": "2011-10-05T08:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33980",
    "user": "SimonKing"
}
```

Attachment [trac4539_libplural_rel10903.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural_rel10903.patch) by SimonKing created at 2011-10-05 08:12:32

Combined patch relative to sage-4.7.2.alpha3 plus #11068, #11856 and #10903



---

archive/issue_comments_033981.json:
```json
{
    "body": "Pickling of nc rings and polynomials, rel #10903",
    "created_at": "2011-10-05T08:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33981",
    "user": "SimonKing"
}
```

Pickling of nc rings and polynomials, rel #10903



---

archive/issue_comments_033982.json:
```json
{
    "body": "Attachment [trac4539_normal_forms_rel10903.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_normal_forms_rel10903.patch) by SimonKing created at 2011-10-05 08:13:40\n\nNormal forms, quotient rings, and ideal containment, rel #10903",
    "created_at": "2011-10-05T08:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33982",
    "user": "SimonKing"
}
```

Attachment [trac4539_normal_forms_rel10903.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_normal_forms_rel10903.patch) by SimonKing created at 2011-10-05 08:13:40

Normal forms, quotient rings, and ideal containment, rel #10903



---

archive/issue_comments_033983.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-05T08:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33983",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033984.json:
```json
{
    "body": "Hoorray! The other doctest error was even easier to fix: It has been a new test, and I simply had a typo in it.\n\nBecause of #11339 and #10903, I had to change some lines in the code. In order to make the changes more easily visible, I attached the new patches under a new name, so that you can compare them with the old patches.\n\nCould you please have a look whether we can return to the positive review?\n\nApply trac4539_libplural_rel10903.patch trac4539_pickling_rel10903.patch trac4539_normal_forms_rel10903.patch trac4539_fix_docs_rel10903.patch",
    "created_at": "2011-10-05T08:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33984",
    "user": "SimonKing"
}
```

Hoorray! The other doctest error was even easier to fix: It has been a new test, and I simply had a typo in it.

Because of #11339 and #10903, I had to change some lines in the code. In order to make the changes more easily visible, I attached the new patches under a new name, so that you can compare them with the old patches.

Could you please have a look whether we can return to the positive review?

Apply trac4539_libplural_rel10903.patch trac4539_pickling_rel10903.patch trac4539_normal_forms_rel10903.patch trac4539_fix_docs_rel10903.patch



---

archive/issue_comments_033985.json:
```json
{
    "body": "The patches look sane. I'll test them now (setting up 4.7.2alph3 will last some time).",
    "created_at": "2011-10-05T09:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33985",
    "user": "AlexanderDreyer"
}
```

The patches look sane. I'll test them now (setting up 4.7.2alph3 will last some time).



---

archive/issue_comments_033986.json:
```json
{
    "body": "FWIW, all tests pass for me (starting with the \"official version\" of sage-4.7.3.alpha3).",
    "created_at": "2011-10-05T09:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33986",
    "user": "SimonKing"
}
```

FWIW, all tests pass for me (starting with the "official version" of sage-4.7.3.alpha3).



---

archive/issue_comments_033987.json:
```json
{
    "body": "Can you just post the output of `hg qapplied`? this would simplify things for me.",
    "created_at": "2011-10-05T09:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33987",
    "user": "AlexanderDreyer"
}
```

Can you just post the output of `hg qapplied`? this would simplify things for me.



---

archive/issue_comments_033988.json:
```json
{
    "body": "Replying to [comment:111 AlexanderDreyer]:\n> Can you just post the output of `hg qapplied`? this would simplify things for me. \n\nStarting with sage-4.7.2.alpha3 (no prerelease this time):\n\n```\n$ hg qapplied\ntrac_11339_refcount_singular_rings.patch\ntrac_11339_refcount_singular_polynomials.patch\ntrac_10903_singular-3-1-3-3.patch\ntrac_10903_singular-fixes.patch\ntrac11856_exponent_overflow.patch\ntrac11856_fix_docs_32bit.patch\ntrac11115-cached_cython.patch\ntrac11115_element_with_cache.patch\ntrac11115_cached_function_pickling.patch\ntrac_11115_reviewer.patch\ntrac11068_nc_ideals_and_quotients.patch\ntrac11068_quotient_ring_without_names.patch\ntrac11068_lifting_map.patch\ntrac4539_libplural_rel10903.patch\ntrac4539_pickling_rel10903.patch\ntrac4539_normal_forms_rel10903.patch\ntrac4539_fix_docs_rel10903.patch\n```\n",
    "created_at": "2011-10-05T09:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33988",
    "user": "SimonKing"
}
```

Replying to [comment:111 AlexanderDreyer]:
> Can you just post the output of `hg qapplied`? this would simplify things for me. 

Starting with sage-4.7.2.alpha3 (no prerelease this time):

```
$ hg qapplied
trac_11339_refcount_singular_rings.patch
trac_11339_refcount_singular_polynomials.patch
trac_10903_singular-3-1-3-3.patch
trac_10903_singular-fixes.patch
trac11856_exponent_overflow.patch
trac11856_fix_docs_32bit.patch
trac11115-cached_cython.patch
trac11115_element_with_cache.patch
trac11115_cached_function_pickling.patch
trac_11115_reviewer.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac4539_libplural_rel10903.patch
trac4539_pickling_rel10903.patch
trac4539_normal_forms_rel10903.patch
trac4539_fix_docs_rel10903.patch
```




---

archive/issue_comments_033989.json:
```json
{
    "body": "Sorry, I had to produce a new version of the last patch: The first patch has introduced a wrong instance of the `..todo::` markup. The docbuilder complained about it. Since [attachment:trac4539_fix_docs_rel10903.patch] is responsible for fixing the doc strings, I fixed it there.\n\nSo, please replace the last patch with the new version, and also try to build the documentation (`sage -docbuild reference html`).",
    "created_at": "2011-10-05T10:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33989",
    "user": "SimonKing"
}
```

Sorry, I had to produce a new version of the last patch: The first patch has introduced a wrong instance of the `..todo::` markup. The docbuilder complained about it. Since [attachment:trac4539_fix_docs_rel10903.patch] is responsible for fixing the doc strings, I fixed it there.

So, please replace the last patch with the new version, and also try to build the documentation (`sage -docbuild reference html`).



---

archive/issue_comments_033990.json:
```json
{
    "body": "OMG. It seems that I managed to destroy the patch that I have just attached by a patch that I had prepared for #10903. Needs work, for now.",
    "created_at": "2011-10-05T10:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33990",
    "user": "SimonKing"
}
```

OMG. It seems that I managed to destroy the patch that I have just attached by a patch that I had prepared for #10903. Needs work, for now.



---

archive/issue_comments_033991.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-05T10:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33991",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033992.json:
```json
{
    "body": "Attachment [8800_functor_pushout_doc_and_fixes.patch](tarball://root/attachments/some-uuid/ticket4539/8800_functor_pushout_doc_and_fixes.patch) by SimonKing created at 2011-10-05 10:53:00\n\nFixing doc strings and doc tests , rel #10903",
    "created_at": "2011-10-05T10:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33992",
    "user": "SimonKing"
}
```

Attachment [8800_functor_pushout_doc_and_fixes.patch](tarball://root/attachments/some-uuid/ticket4539/8800_functor_pushout_doc_and_fixes.patch) by SimonKing created at 2011-10-05 10:53:00

Fixing doc strings and doc tests , rel #10903



---

archive/issue_comments_033993.json:
```json
{
    "body": "Attachment [trac4539_fix_docs_rel10903.2.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs_rel10903.2.patch) by SimonKing created at 2011-10-05 10:53:53\n\nFixing doc strings and doc tests , rel #10903",
    "created_at": "2011-10-05T10:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33993",
    "user": "SimonKing"
}
```

Attachment [trac4539_fix_docs_rel10903.2.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs_rel10903.2.patch) by SimonKing created at 2011-10-05 10:53:53

Fixing doc strings and doc tests , rel #10903



---

archive/issue_comments_033994.json:
```json
{
    "body": "Attachment [trac4539_fix_docs_rel10903.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs_rel10903.patch) by SimonKing created at 2011-10-05 10:54:11\n\nFixing doc strings and doc tests , rel #10903",
    "created_at": "2011-10-05T10:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33994",
    "user": "SimonKing"
}
```

Attachment [trac4539_fix_docs_rel10903.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_fix_docs_rel10903.patch) by SimonKing created at 2011-10-05 10:54:11

Fixing doc strings and doc tests , rel #10903



---

archive/issue_comments_033995.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-05T10:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33995",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033996.json:
```json
{
    "body": "I urgently need a break. It is unbelievable how many errors I made in the past 30 minutes.\n\nAnyway.\n\nI have now updated the patch (after first attaching a wrong file, followed by the correct file under a wrong name, and those things).\n\nNote that there is now a new patch at #10903 - without that patch, building the documentation would fail.\n\nThe new version of [attachment:trac4539_fix_docs_rel10903.patch] fixes one wrongly formatted `.. todo::` directive.\n\nPlease test whether the documentation builds fine for you.\n\nApply trac4539_libplural_rel10903.patch trac4539_pickling_rel10903.patch trac4539_normal_forms_rel10903.patch trac4539_fix_docs_rel10903.patch",
    "created_at": "2011-10-05T10:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33996",
    "user": "SimonKing"
}
```

I urgently need a break. It is unbelievable how many errors I made in the past 30 minutes.

Anyway.

I have now updated the patch (after first attaching a wrong file, followed by the correct file under a wrong name, and those things).

Note that there is now a new patch at #10903 - without that patch, building the documentation would fail.

The new version of [attachment:trac4539_fix_docs_rel10903.patch] fixes one wrongly formatted `.. todo::` directive.

Please test whether the documentation builds fine for you.

Apply trac4539_libplural_rel10903.patch trac4539_pickling_rel10903.patch trac4539_normal_forms_rel10903.patch trac4539_fix_docs_rel10903.patch



---

archive/issue_comments_033997.json:
```json
{
    "body": "Everything is fine, but one issue: Unfortunately the docbuild contains one uncaught exception (on SuSE 11):\n\n\n```\nsphinx-build -b html -d /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/doctrees/en/reference    /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/en/reference /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/html/en/reference\nRunning Sphinx v1.0.4\nloading pickled environment... done\nbuilding [html]: targets for 152 source files that are out of date\nupdating environment: 1 added, 152 changed, 0 removed\nreading sources... [ 99%] sage/symbolic/expression\nException occurred:\n  File \"/p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/common/conf.py\", line 378, in skip_member\n    if (hasattr(obj, '__name__') and obj.__name__.find('.') != -1 and\nAttributeError: 'NoneType' object has no attribute 'find'\nThe full traceback has been saved in /tmp/sphinx-err-RJnoHz.log, if you want to report the issue to the developers.\nPlease also report this if it was a user error, so that a better error message can be provided next time.\nEither send bugs to the mailing list at <http://groups.google.com/group/sphinx-dev/>,\nor report them in the tracker at <http://bitbucket.org/birkenfeld/sphinx/issues/>. Thanks!\nBuild finished.  The built documents can be found in /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/html/en/reference\n```\n\n\nI suggested the reviewer patch: [attachment:trac4539_docbuild_reviewer.patch]\n\nWith that patch we are close to a positive review: I'm also running tests on OS X.",
    "created_at": "2011-10-05T18:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33997",
    "user": "AlexanderDreyer"
}
```

Everything is fine, but one issue: Unfortunately the docbuild contains one uncaught exception (on SuSE 11):


```
sphinx-build -b html -d /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/doctrees/en/reference    /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/en/reference /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/html/en/reference
Running Sphinx v1.0.4
loading pickled environment... done
building [html]: targets for 152 source files that are out of date
updating environment: 1 added, 152 changed, 0 removed
reading sources... [ 99%] sage/symbolic/expression
Exception occurred:
  File "/p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/common/conf.py", line 378, in skip_member
    if (hasattr(obj, '__name__') and obj.__name__.find('.') != -1 and
AttributeError: 'NoneType' object has no attribute 'find'
The full traceback has been saved in /tmp/sphinx-err-RJnoHz.log, if you want to report the issue to the developers.
Please also report this if it was a user error, so that a better error message can be provided next time.
Either send bugs to the mailing list at <http://groups.google.com/group/sphinx-dev/>,
or report them in the tracker at <http://bitbucket.org/birkenfeld/sphinx/issues/>. Thanks!
Build finished.  The built documents can be found in /p/sys/Sage/share/versions/sage-4.7.2.alpha3/devel/sage/doc/output/html/en/reference
```


I suggested the reviewer patch: [attachment:trac4539_docbuild_reviewer.patch]

With that patch we are close to a positive review: I'm also running tests on OS X.



---

archive/issue_comments_033998.json:
```json
{
    "body": "Attachment [trac4539_docbuild_reviewer.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_docbuild_reviewer.patch) by SimonKing created at 2011-10-05 18:43:04\n\nHi Alexander,\n\nNote that there is a new patch at #10903 (where the docbuild crash was introduced), and it fixes the problem in a more satisfying way. The problem was that under certain circumstances the name of a deprecated Cython method could not be determined - but with the new patch from #10903 (actually there are TWO new patches) the problem is fixed.\n\nSo, the docbuild reviewer patch is not needed.",
    "created_at": "2011-10-05T18:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33998",
    "user": "SimonKing"
}
```

Attachment [trac4539_docbuild_reviewer.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_docbuild_reviewer.patch) by SimonKing created at 2011-10-05 18:43:04

Hi Alexander,

Note that there is a new patch at #10903 (where the docbuild crash was introduced), and it fixes the problem in a more satisfying way. The problem was that under certain circumstances the name of a deprecated Cython method could not be determined - but with the new patch from #10903 (actually there are TWO new patches) the problem is fixed.

So, the docbuild reviewer patch is not needed.



---

archive/issue_comments_033999.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-06T07:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-33999",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034000.json:
```json
{
    "body": "Building, installing and testing succeeded on SuSE 11 Enterprise amd64 and OS X 10.5 ppc. So we can switch back to positive review.",
    "created_at": "2011-10-06T07:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34000",
    "user": "AlexanderDreyer"
}
```

Building, installing and testing succeeded on SuSE 11 Enterprise amd64 and OS X 10.5 ppc. So we can switch back to positive review.



---

archive/issue_comments_034001.json:
```json
{
    "body": "Attachment [trac4539_libplural_rel11761.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural_rel11761.patch) by jdemeyer created at 2011-11-05 14:05:43",
    "created_at": "2011-11-05T14:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34001",
    "user": "jdemeyer"
}
```

Attachment [trac4539_libplural_rel11761.patch](tarball://root/attachments/some-uuid/ticket4539/trac4539_libplural_rel11761.patch) by jdemeyer created at 2011-11-05 14:05:43



---

archive/issue_comments_034002.json:
```json
{
    "body": "It could be that we need some work here. The first patch does not apply when we start with sage-4.8.alpha0. Namely, in sage/libs/singular/function.pyx, it expects the line\n\n```\n       ring2 = None\n```\n\nbut this line has been removed. I don't know in which ticket that has happened. By consequence, a rather complicated chunk of the patch does not apply.\n\nWhat shall we do? In order to avoid premature work, it would be an option to wait until finally all the dependencies got a positive review.",
    "created_at": "2011-11-08T15:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34002",
    "user": "SimonKing"
}
```

It could be that we need some work here. The first patch does not apply when we start with sage-4.8.alpha0. Namely, in sage/libs/singular/function.pyx, it expects the line

```
       ring2 = None
```

but this line has been removed. I don't know in which ticket that has happened. By consequence, a rather complicated chunk of the patch does not apply.

What shall we do? In order to avoid premature work, it would be an option to wait until finally all the dependencies got a positive review.



---

archive/issue_comments_034003.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-11-08T15:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34003",
    "user": "SimonKing"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_034004.json:
```json
{
    "body": "That line comes from http://trac.sagemath.org/sage_trac/attachment/ticket/11761/11761-cython-0.15.patch (Cython is more strict here.) That patch was not merged in alpha0.",
    "created_at": "2011-11-08T22:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34004",
    "user": "AlexanderDreyer"
}
```

That line comes from http://trac.sagemath.org/sage_trac/attachment/ticket/11761/11761-cython-0.15.patch (Cython is more strict here.) That patch was not merged in alpha0.



---

archive/issue_comments_034005.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-11-08T23:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34005",
    "user": "SimonKing"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_034006.json:
```json
{
    "body": "Replying to [comment:123 AlexanderDreyer]:\n> That line comes from http://trac.sagemath.org/sage_trac/attachment/ticket/11761/11761-cython-0.15.patch (Cython is more strict here.)\n\nYes, now I see it: #11761 is a dependency! So, sorry for the noise, and back to a positive review - which needs two steps. One...",
    "created_at": "2011-11-08T23:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34006",
    "user": "SimonKing"
}
```

Replying to [comment:123 AlexanderDreyer]:
> That line comes from http://trac.sagemath.org/sage_trac/attachment/ticket/11761/11761-cython-0.15.patch (Cython is more strict here.)

Yes, now I see it: #11761 is a dependency! So, sorry for the noise, and back to a positive review - which needs two steps. One...



---

archive/issue_comments_034007.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-08T23:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34007",
    "user": "SimonKing"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034008.json:
```json
{
    "body": "... and two.",
    "created_at": "2011-11-08T23:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34008",
    "user": "SimonKing"
}
```

... and two.



---

archive/issue_comments_034009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-21T23:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4539#issuecomment-34009",
    "user": "jdemeyer"
}
```

Resolution: fixed
