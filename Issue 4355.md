# Issue 4355: Port latex/asciiArt output for tableaux and all friends from MuPAD-Combinat

archive/issues_004355.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat boussica\n\nThe latex method for tableaux was written in a rush during Sage Days 7\nto get the latex output for crystals. This is a partial quick port of\nthe TeX method we use in MuPAD-Combinat in the general case of\n\"ObjectsWith2DBoxedRepresentation\" which includes everything from\npartitions, tableaux, skew tableaux, ribbons tableaux, to rigged\nconfigurations, or other things that can be drawn with symbols in an\narray, and some horizontal and vertical delimiters, like mazes. \n\nA class which inherits from ObjectsWith2DBoxedRepresentation just has\nto implement a method that fills appropriately an array for the\nsymbols, and another for the delimiters, and it gets for free 2D ascii\nart, latex, ... output.  See:\n\nhttp://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/DOMAINS/CATEGORY/CombinatorialClassWith2DBoxedRepresentation.mu?revision=7455&view=markup\n\nFor a few samples of the produced 2d ascii art, you can have a look\nat:\n\nhttp://mupad-combinat.sourceforge.net/doc/en/output_Combinat/asciiArt.html\n\n(note: the pictures are broken unless you use a fixed font).\n\nIt as proven to be a handy tool, for the zillion of tableaux-like\nclasses, so a good candidate for porting.\n\nFirst straightforward step: LaTeX output\n\nSecond step: ascii art output. This may require a bit more thinking,\nsince there is not yet (?) a general framework for ascii art in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4355\n\n",
    "created_at": "2008-10-24T00:53:04Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Port latex/asciiArt output for tableaux and all friends from MuPAD-Combinat",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4355",
    "user": "nthiery"
}
```
Assignee: mhansen

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

http://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/DOMAINS/CATEGORY/CombinatorialClassWith2DBoxedRepresentation.mu?revision=7455&view=markup

For a few samples of the produced 2d ascii art, you can have a look
at:

http://mupad-combinat.sourceforge.net/doc/en/output_Combinat/asciiArt.html

(note: the pictures are broken unless you use a fixed font).

It as proven to be a handy tool, for the zillion of tableaux-like
classes, so a good candidate for porting.

First straightforward step: LaTeX output

Second step: ascii art output. This may require a bit more thinking,
since there is not yet (?) a general framework for ascii art in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/4355





---

archive/issue_comments_031989.json:
```json
{
    "body": "I have added two patches tableaux_output.patch and tableaux_output1.patch with the aim of fixing the latex output for tableaux. This is particularly important for CrystalOfTableaux tex output which is a main way of viewing crystals. For discussion see this thread:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en#",
    "created_at": "2008-10-24T03:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31989",
    "user": "bump"
}
```

I have added two patches tableaux_output.patch and tableaux_output1.patch with the aim of fixing the latex output for tableaux. This is particularly important for CrystalOfTableaux tex output which is a main way of viewing crystals. For discussion see this thread:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en#



---

archive/issue_comments_031990.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2008-10-24T03:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31990",
    "user": "bump"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_031991.json:
```json
{
    "body": "I changed the type from \"enhancement\" to \"defect\" since the existing code is actually broke. Nicolas envisions an enhancement here but in the meantime perhaps we can at least make the existing code work correctly.",
    "created_at": "2008-10-24T03:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31991",
    "user": "bump"
}
```

I changed the type from "enhancement" to "defect" since the existing code is actually broke. Nicolas envisions an enhancement here but in the meantime perhaps we can at least make the existing code work correctly.



---

archive/issue_comments_031992.json:
```json
{
    "body": "Since what Nicolas is proposing is clearly different from the problems the patches addresses, I created a new ticket at #4362 and changed the type of this one back to enhancement.",
    "created_at": "2008-10-24T11:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31992",
    "user": "bump"
}
```

Since what Nicolas is proposing is clearly different from the problems the patches addresses, I created a new ticket at #4362 and changed the type of this one back to enhancement.



---

archive/issue_comments_031993.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-10-24T11:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31993",
    "user": "bump"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_031994.json:
```json
{
    "body": "I have deleted both of Dan's patches and moved them over to the new ticket so that things are kept simple :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-24T11:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31994",
    "user": "mabshoff"
}
```

I have deleted both of Dan's patches and moved them over to the new ticket so that things are kept simple :)

Cheers,

Michael



---

archive/issue_comments_031995.json:
```json
{
    "body": "I have completed a portion of part 1 in ticket #12314.\n\nTravis",
    "created_at": "2012-01-16T06:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31995",
    "user": "tscrim"
}
```

I have completed a portion of part 1 in ticket #12314.

Travis



---

archive/issue_comments_031996.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-02T09:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4355#issuecomment-31996",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
