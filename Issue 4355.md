# Issue 4355: Port latex/asciiArt output for tableaux and all friends from MuPAD-Combinat

archive/issues_004355.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat boussica\n\nThe latex method for tableaux was written in a rush during Sage Days 7\nto get the latex output for crystals. This is a partial quick port of\nthe TeX method we use in MuPAD-Combinat in the general case of\n\"ObjectsWith2DBoxedRepresentation\" which includes everything from\npartitions, tableaux, skew tableaux, ribbons tableaux, to rigged\nconfigurations, or other things that can be drawn with symbols in an\narray, and some horizontal and vertical delimiters, like mazes. \n\nA class which inherits from ObjectsWith2DBoxedRepresentation just has\nto implement a method that fills appropriately an array for the\nsymbols, and another for the delimiters, and it gets for free 2D ascii\nart, latex, ... output.  See:\n\nhttp://mupad-combinat.sourceforge.net/doc/en/Cat_Combinat/CombinatorialClassWith2DBoxedRepresentation.html\n\nhttp://sourceforge.net/p/mupad-combinat/code/HEAD/tree/trunk/MuPAD-Combinat/lib/DOMAINS/CATEGORY/CombinatorialClassWith2DBoxedRepresentation.mu\n\nFor a few samples of the produced 2d ascii art, you can have a look\nat:\n\nhttp://mupad-combinat.sourceforge.net/doc/en/output_Combinat/asciiArt.html\n\n(note: the pictures are broken unless you use a fixed font).\n\nIt as proven to be a handy tool, for the zillion of tableaux-like\nclasses, so a good candidate for porting.\n\nFirst straightforward step: LaTeX output (partitions and cores in ticket #12314)\n\nSecond step: same as above, but making sure the produced LaTeX is compatible with jsmath/mathjax, for display in the notebook.\n\nThird step: ascii art output. This may require a bit more thinking,\nsince there is not yet (?) a general framework for ascii art in Sage.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4355\n\n",
    "created_at": "2008-10-24T00:53:04Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Port latex/asciiArt output for tableaux and all friends from MuPAD-Combinat",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4355",
    "user": "https://github.com/nthiery"
}
```
Assignee: @mwhansen

CC:  sage-combinat boussica

The latex method for tableaux was written in a rush during Sage Days 7
to get the latex output for crystals. This is a partial quick port of
the TeX method we use in MuPAD-Combinat in the general case of
"ObjectsWith2DBoxedRepresentation" which includes everything from
partitions, tableaux, skew tableaux, ribbons tableaux, to rigged
configurations, or other things that can be drawn with symbols in an
array, and some horizontal and vertical delimiters, like mazes. 

A class which inherits from ObjectsWith2DBoxedRepresentation just has
to implement a method that fills appropriately an array for the
symbols, and another for the delimiters, and it gets for free 2D ascii
art, latex, ... output.  See:

http://mupad-combinat.sourceforge.net/doc/en/Cat_Combinat/CombinatorialClassWith2DBoxedRepresentation.html

http://sourceforge.net/p/mupad-combinat/code/HEAD/tree/trunk/MuPAD-Combinat/lib/DOMAINS/CATEGORY/CombinatorialClassWith2DBoxedRepresentation.mu

For a few samples of the produced 2d ascii art, you can have a look
at:

http://mupad-combinat.sourceforge.net/doc/en/output_Combinat/asciiArt.html

(note: the pictures are broken unless you use a fixed font).

It as proven to be a handy tool, for the zillion of tableaux-like
classes, so a good candidate for porting.

First straightforward step: LaTeX output (partitions and cores in ticket #12314)

Second step: same as above, but making sure the produced LaTeX is compatible with jsmath/mathjax, for display in the notebook.

Third step: ascii art output. This may require a bit more thinking,
since there is not yet (?) a general framework for ascii art in Sage.


Issue created by migration from https://trac.sagemath.org/ticket/4355





---

archive/issue_comments_031927.json:
```json
{
    "body": "I have added two patches tableaux_output.patch and tableaux_output1.patch with the aim of fixing the latex output for tableaux. This is particularly important for CrystalOfTableaux tex output which is a main way of viewing crystals. For discussion see this thread:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en#",
    "created_at": "2008-10-24T03:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31927",
    "user": "https://github.com/dwbump"
}
```

I have added two patches tableaux_output.patch and tableaux_output1.patch with the aim of fixing the latex output for tableaux. This is particularly important for CrystalOfTableaux tex output which is a main way of viewing crystals. For discussion see this thread:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en#



---

archive/issue_comments_031928.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2008-10-24T03:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31928",
    "user": "https://github.com/dwbump"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_031929.json:
```json
{
    "body": "I changed the type from \"enhancement\" to \"defect\" since the existing code is actually broke. Nicolas envisions an enhancement here but in the meantime perhaps we can at least make the existing code work correctly.",
    "created_at": "2008-10-24T03:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31929",
    "user": "https://github.com/dwbump"
}
```

I changed the type from "enhancement" to "defect" since the existing code is actually broke. Nicolas envisions an enhancement here but in the meantime perhaps we can at least make the existing code work correctly.



---

archive/issue_comments_031930.json:
```json
{
    "body": "Since what Nicolas is proposing is clearly different from the problems the patches addresses, I created a new ticket at #4362 and changed the type of this one back to enhancement.",
    "created_at": "2008-10-24T11:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31930",
    "user": "https://github.com/dwbump"
}
```

Since what Nicolas is proposing is clearly different from the problems the patches addresses, I created a new ticket at #4362 and changed the type of this one back to enhancement.



---

archive/issue_comments_031931.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-10-24T11:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31931",
    "user": "https://github.com/dwbump"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_031932.json:
```json
{
    "body": "I have deleted both of Dan's patches and moved them over to the new ticket so that things are kept simple :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-24T11:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have deleted both of Dan's patches and moved them over to the new ticket so that things are kept simple :)

Cheers,

Michael



---

archive/issue_comments_031933.json:
```json
{
    "body": "I have completed a portion of part 1 in ticket #12314.\n\nTravis",
    "created_at": "2012-01-16T06:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31933",
    "user": "https://github.com/tscrim"
}
```

I have completed a portion of part 1 in ticket #12314.

Travis



---

archive/issue_events_009848.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4355#event-9848"
}
```



---

archive/issue_events_009849.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4355#event-9849"
}
```



---

archive/issue_events_009850.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4355#event-9850"
}
```



---

archive/issue_comments_031934.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-02T09:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31934",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_009851.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4355#event-9851"
}
```



---

archive/issue_events_009852.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4355#event-9852"
}
```



---

archive/issue_events_009853.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4355#event-9853"
}
```



---

archive/issue_events_009854.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4355#event-9854"
}
```
