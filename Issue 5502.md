# Issue 5502: implement ascii art output for Dynkin diagrams

archive/issues_005502.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: dynkin diagram ascii art lie\n\nDan Bump requested this in his Sage Days 14 talk: have ascii art output a la LiE for Dynkin diagrams (see interfaces/lie.py for some examples of usage).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5502\n\n",
    "created_at": "2009-03-12T19:26:49Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "implement ascii art output for Dynkin diagrams",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5502",
    "user": "https://github.com/aghitza"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: dynkin diagram ascii art lie

Dan Bump requested this in his Sage Days 14 talk: have ascii art output a la LiE for Dynkin diagrams (see interfaces/lie.py for some examples of usage).


Issue created by migration from https://trac.sagemath.org/ticket/5502





---

archive/issue_comments_042654.json:
```json
{
    "body": "I uploaded trac_5502.patch for this. It applies to sage-3.4.1.rc2 and there are no errors in `sage/combinat/rootsystems/*.py.`.\n\nI have not tested it against the combinat patchseries because at the moment hg qpush -a fails in sage-combinat.\n\nAfter the patch, the `__repr__` method of `class DynkinDiagram` returns ascii art for the classical Cartan Types.\n\nA natural extension would be to give the extended Dynkin diagram for the untwisted affine types.",
    "created_at": "2009-04-15T13:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42654",
    "user": "https://github.com/dwbump"
}
```

I uploaded trac_5502.patch for this. It applies to sage-3.4.1.rc2 and there are no errors in `sage/combinat/rootsystems/*.py.`.

I have not tested it against the combinat patchseries because at the moment hg qpush -a fails in sage-combinat.

After the patch, the `__repr__` method of `class DynkinDiagram` returns ascii art for the classical Cartan Types.

A natural extension would be to give the extended Dynkin diagram for the untwisted affine types.



---

archive/issue_comments_042655.json:
```json
{
    "body": "Is this related to http://trac.sagemath.org/sage_trac/ticket/2023 ?",
    "created_at": "2009-04-15T15:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42655",
    "user": "https://github.com/wdjoyner"
}
```

Is this related to http://trac.sagemath.org/sage_trac/ticket/2023 ?



---

archive/issue_comments_042656.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> Is this related to http://trac.sagemath.org/sage_trac/ticket/2023 ?\n\nThat's indeed the ascii art version of 2023. Thanks for the pointer.",
    "created_at": "2009-04-15T16:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42656",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 wdj]:
> Is this related to http://trac.sagemath.org/sage_trac/ticket/2023 ?

That's indeed the ascii art version of 2023. Thanks for the pointer.



---

archive/issue_comments_042657.json:
```json
{
    "body": "I think the spirit of this patch is the same as #2023.\n\nThe idea of this patch is just that if the Cartan type is that\nof a classical Lie algebra, you should be able to *somehow*\naccess it's Dynkin diagram. The solution here is making it part of the string\nreturned by the `__repr__` method of the class.\n\nWe follow the Bourbaki conventions, which is the same as the\nprogrammed-in Cartan types. These diagrams are identical to\nthose produced by LiE, so you can have them already if you\ninstall that optional package.\n\n\n```\nsage: CartanType(\"E6\").dynkin_diagram()\n\n        O 2\n        |\n        |\nO---O---O---O---O\n1   3   4   5   6   \nE6\n```\n\n\nYou want this if you need to be reminded of what labeling\nconvention is used. If the Cartan type is not recognized, we get the\nold behavior. Thus:\n\n\n```\nsage: CartanType(['E',6,1]).dynkin_diagram()\nDynkin diagram of type ['E', 6, 1]\n```\n\n\nIt might be more convenient if untwisted affine types gave the\nextended Dynkin diagram, thus:\n\n\n```\nsage: CartanType(['E',6,1]).dynkin_diagram()\n        O 0 \n        |\n        |\n        O 2\n        |\n        |\nO---O---O---O---O\n1   3   4   5   6\nE6~\n```\n\n\nBeyond that, one might implement Dynkin diagrams for twisted\naffine types, but that seems less urgent.",
    "created_at": "2009-04-15T20:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42657",
    "user": "https://github.com/dwbump"
}
```

I think the spirit of this patch is the same as #2023.

The idea of this patch is just that if the Cartan type is that
of a classical Lie algebra, you should be able to *somehow*
access it's Dynkin diagram. The solution here is making it part of the string
returned by the `__repr__` method of the class.

We follow the Bourbaki conventions, which is the same as the
programmed-in Cartan types. These diagrams are identical to
those produced by LiE, so you can have them already if you
install that optional package.


```
sage: CartanType("E6").dynkin_diagram()

        O 2
        |
        |
O---O---O---O---O
1   3   4   5   6   
E6
```


You want this if you need to be reminded of what labeling
convention is used. If the Cartan type is not recognized, we get the
old behavior. Thus:


```
sage: CartanType(['E',6,1]).dynkin_diagram()
Dynkin diagram of type ['E', 6, 1]
```


It might be more convenient if untwisted affine types gave the
extended Dynkin diagram, thus:


```
sage: CartanType(['E',6,1]).dynkin_diagram()
        O 0 
        |
        |
        O 2
        |
        |
O---O---O---O---O
1   3   4   5   6
E6~
```


Beyond that, one might implement Dynkin diagrams for twisted
affine types, but that seems less urgent.



---

archive/issue_comments_042658.json:
```json
{
    "body": "The file trac_5502.2.patch add extended Dynkin diagrams as Dynkin diagrams of untwisted affine Cartan types.\n\nAnne Schilling requests twisted affine types, but this is not done.",
    "created_at": "2009-04-23T15:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42658",
    "user": "https://github.com/dwbump"
}
```

The file trac_5502.2.patch add extended Dynkin diagrams as Dynkin diagrams of untwisted affine Cartan types.

Anne Schilling requests twisted affine types, but this is not done.



---

archive/issue_comments_042659.json:
```json
{
    "body": "Attachment [trac_5502-revised.patch](tarball://root/attachments/some-uuid/ticket5502/trac_5502-revised.patch) by @dwbump created at 2009-04-30 14:48:45\n\nThe patch `trac_5502-revised.patch` corrects some problems and supercedes\nthe previous patches.",
    "created_at": "2009-04-30T14:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42659",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5502-revised.patch](tarball://root/attachments/some-uuid/ticket5502/trac_5502-revised.patch) by @dwbump created at 2009-04-30 14:48:45

The patch `trac_5502-revised.patch` corrects some problems and supercedes
the previous patches.



---

archive/issue_comments_042660.json:
```json
{
    "body": "I changed the milestone to 4.0 in hopes this can be merged.",
    "created_at": "2009-05-06T22:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42660",
    "user": "https://github.com/dwbump"
}
```

I changed the milestone to 4.0 in hopes this can be merged.



---

archive/issue_comments_042661.json:
```json
{
    "body": "The patch implements ascii art for all finite and untwisted Cartan types,\nwhich is very useful for visual clues about the numbering of the Dynkin nodes.\n\nAll doctests pass.",
    "created_at": "2009-05-08T01:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42661",
    "user": "https://github.com/anneschilling"
}
```

The patch implements ascii art for all finite and untwisted Cartan types,
which is very useful for visual clues about the numbering of the Dynkin nodes.

All doctests pass.



---

archive/issue_comments_042662.json:
```json
{
    "body": "There are two new functions without doctests:\n\n* extended_dynkin_diagram_ascii_art\n* dynkin_diagram_ascii_art\n\nI know they are tested elsewhere, but the 100% rule still applies. Once the doctests have been added the positive review can be reinstated assuming the doctests in the file modified actually pass ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T09:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42662",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are two new functions without doctests:

* extended_dynkin_diagram_ascii_art
* dynkin_diagram_ascii_art

I know they are tested elsewhere, but the 100% rule still applies. Once the doctests have been added the positive review can be reinstated assuming the doctests in the file modified actually pass ;)

Cheers,

Michael



---

archive/issue_comments_042663.json:
```json
{
    "body": "Attachment [trac_5502-doc.patch](tarball://root/attachments/some-uuid/ticket5502/trac_5502-doc.patch) by @dwbump created at 2009-05-12 04:09:56\n\nThe patch trac_5502-doc.patch goes on top of trac_5502-revised.patch.\n\nIt adds doctests to the two ascii art functions.",
    "created_at": "2009-05-12T04:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42663",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5502-doc.patch](tarball://root/attachments/some-uuid/ticket5502/trac_5502-doc.patch) by @dwbump created at 2009-05-12 04:09:56

The patch trac_5502-doc.patch goes on top of trac_5502-revised.patch.

It adds doctests to the two ascii art functions.



---

archive/issue_comments_042664.json:
```json
{
    "body": "Positive review overall.\n\nDan: Please remember to change the summary back once you updated the patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T05:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review overall.

Dan: Please remember to change the summary back once you updated the patch.

Cheers,

Michael



---

archive/issue_events_005755.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-12T06:04:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5502#event-5755"
}
```



---

archive/issue_comments_042665.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T06:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42665",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042666.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T06:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5502#issuecomment-42666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
