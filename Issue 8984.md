# Issue 8984: Implementation of the Lenart--Postnikov alcove path crystal

archive/issues_008984.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat brant@math.ucdavis.edu @rlmill\n\nThis is an implementation of the Lenart--Postnikov alcove path model as described in:\n\nA combinatorial model for crystals of Kac-Moody algebras. Trans. Amer. Math. Soc.  360  (2008).\n\nIt also implements to_coroot_lattice_morphism() and associated_coroot() in root_lattice_realization.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8984\n\n",
    "created_at": "2010-05-18T00:26:22Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Implementation of the Lenart--Postnikov alcove path crystal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8984",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```
Assignee: sage-combinat

CC:  sage-combinat brant@math.ucdavis.edu @rlmill

This is an implementation of the Lenart--Postnikov alcove path model as described in:

A combinatorial model for crystals of Kac-Moody algebras. Trans. Amer. Math. Soc.  360  (2008).

It also implements to_coroot_lattice_morphism() and associated_coroot() in root_lattice_realization.py.

Issue created by migration from https://trac.sagemath.org/ticket/8984





---

archive/issue_comments_082756.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-18T00:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82756",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082757.json:
```json
{
    "body": "Test whether Brant gets this message.",
    "created_at": "2010-05-18T00:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82757",
    "user": "https://github.com/anneschilling"
}
```

Test whether Brant gets this message.



---

archive/issue_comments_082758.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-06T16:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82758",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082759.json:
```json
{
    "body": "Changing keywords from \"\" to \"combinat, crystals\".",
    "created_at": "2010-06-06T16:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82759",
    "user": "https://github.com/anneschilling"
}
```

Changing keywords from "" to "combinat, crystals".



---

archive/issue_comments_082760.json:
```json
{
    "body": "Thank you for implementing the alcove path model by Lenart and Postnikov.\nThis will be a useful addition to sage.\n\nIt might be useful to add a few more words about the model you implemented\nin the documentation of ClassicalCrystalOfAlcovePaths. For example, you could\nadd that these are highest weight crystals for classical types\n`A_n`, `B_n`, `C_n`, `D_n` and the exceptional types `F_4`, `G_2`, `E_6`,\n`E_7`, `E_8`.\n\nAlso, for the user it would be helpful to say how precisely one should\nenter the input data. For example, you could say\n\nINPUT:\n  \n- ``cartan_type`` is the Cartan type of a classical Dynkin diagram \n- ``highest_weight`` is a dominant weight as a list of coefficients of \n   the fundamental weights `Lambda_i`\n\nIt might also be good to briefly describe how the crystal elements\nare represented so that the user can interpret the output.\n\nSome technical comments:\n\n(1) In combinat/crystals/alcove_path.py, it might be safer to only \nimport the methods/classes that you really need for:\n\nfrom sage.rings.integer import * (which appears twice, so please remove one!)\nfrom sage.misc.misc import *\nfrom sage.calculus.calculus import *\n\n(2) All methods need EXAMPLES or TESTS. Please add them to the following\nmethods in combinat/crystals/alcove_path.py for\n\n__classcall__\nget_initial_chain\nfold\ncompare_graphs\n\n(3) Perhaps remove the commented out lines by # in\n\n__init__\nlist\n\n(4) Add extra line after EXAMPLES:: get_chain_from_subset\n\n(5) Remove the commented out `weight` function\n\n(6) You need TESTS or EXAMPLES to_coroot_lattice_morphism in \nsage/combinat/root_system/root_lattice_realization.py",
    "created_at": "2010-06-06T16:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82760",
    "user": "https://github.com/anneschilling"
}
```

Thank you for implementing the alcove path model by Lenart and Postnikov.
This will be a useful addition to sage.

It might be useful to add a few more words about the model you implemented
in the documentation of ClassicalCrystalOfAlcovePaths. For example, you could
add that these are highest weight crystals for classical types
`A_n`, `B_n`, `C_n`, `D_n` and the exceptional types `F_4`, `G_2`, `E_6`,
`E_7`, `E_8`.

Also, for the user it would be helpful to say how precisely one should
enter the input data. For example, you could say

INPUT:
  
- ``cartan_type`` is the Cartan type of a classical Dynkin diagram 
- ``highest_weight`` is a dominant weight as a list of coefficients of 
   the fundamental weights `Lambda_i`

It might also be good to briefly describe how the crystal elements
are represented so that the user can interpret the output.

Some technical comments:

(1) In combinat/crystals/alcove_path.py, it might be safer to only 
import the methods/classes that you really need for:

from sage.rings.integer import * (which appears twice, so please remove one!)
from sage.misc.misc import *
from sage.calculus.calculus import *

(2) All methods need EXAMPLES or TESTS. Please add them to the following
methods in combinat/crystals/alcove_path.py for

__classcall__
get_initial_chain
fold
compare_graphs

(3) Perhaps remove the commented out lines by # in

__init__
list

(4) Add extra line after EXAMPLES:: get_chain_from_subset

(5) Remove the commented out `weight` function

(6) You need TESTS or EXAMPLES to_coroot_lattice_morphism in 
sage/combinat/root_system/root_lattice_realization.py



---

archive/issue_comments_082761.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-08T00:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82761",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082762.json:
```json
{
    "body": "Attachment [trac_8984_crystals_alcove_path_model_bj.patch](tarball://root/attachments/some-uuid/ticket8984/trac_8984_crystals_alcove_path_model_bj.patch) by brant.c.jones created at 2010-06-08 00:23:53\n\nI have implemented all of the suggestions given by the reviewer above.\n\nPlease review the new version.",
    "created_at": "2010-06-08T00:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82762",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```

Attachment [trac_8984_crystals_alcove_path_model_bj.patch](tarball://root/attachments/some-uuid/ticket8984/trac_8984_crystals_alcove_path_model_bj.patch) by brant.c.jones created at 2010-06-08 00:23:53

I have implemented all of the suggestions given by the reviewer above.

Please review the new version.



---

archive/issue_comments_082763.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-09T03:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82763",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082764.json:
```json
{
    "body": "This patch implements the Lenart-Postnikov model for highest weight crystals for finite-dimensional Lie algebras. There are extensive tests to test that this gives the same crystal graph as other models.\n\nAll tests pass with sage-4.4.2 and the sage-combinat queue applied to this patch.",
    "created_at": "2010-06-09T03:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82764",
    "user": "https://github.com/anneschilling"
}
```

This patch implements the Lenart-Postnikov model for highest weight crystals for finite-dimensional Lie algebras. There are extensive tests to test that this gives the same crystal graph as other models.

All tests pass with sage-4.4.2 and the sage-combinat queue applied to this patch.



---

archive/issue_comments_082765.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T03:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82765",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021981.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-09T03:58:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8984#event-21981"
}
```



---

archive/issue_events_021982.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-06-09T04:37:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "milestone": "sage-4.4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8984#event-21982"
}
```



---

archive/issue_comments_082766.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-06-09T19:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82766",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_082767.json:
```json
{
    "body": "I had to backout this change from 4.4.4 for now.  I was getting weird failures with random_element in matrix_group.py.  I'm trying to figure out why this patch was causing it.",
    "created_at": "2010-06-09T19:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82767",
    "user": "https://github.com/mwhansen"
}
```

I had to backout this change from 4.4.4 for now.  I was getting weird failures with random_element in matrix_group.py.  I'm trying to figure out why this patch was causing it.



---

archive/issue_comments_082768.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-06-09T19:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82768",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to new.



---

archive/issue_events_021983.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-09T19:18:37Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8984#event-21983"
}
```



---

archive/issue_comments_082769.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-09T19:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82769",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082770.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-09T19:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82770",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082771.json:
```json
{
    "body": "Replying to [comment:12 mhansen]:\n\nHi Mike,\n\nWhat is the status on this now? Do you know why there were the strange failures in random_element in matrix_group.py?\n\nAnne",
    "created_at": "2010-06-13T22:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82771",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:12 mhansen]:

Hi Mike,

What is the status on this now? Do you know why there were the strange failures in random_element in matrix_group.py?

Anne



---

archive/issue_comments_082772.json:
```json
{
    "body": "See #9310",
    "created_at": "2010-06-22T22:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82772",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

See #9310



---

archive/issue_comments_082773.json:
```json
{
    "body": "Replying to [comment:14 drkirkby]:\n> See #9310\n\nIs this patch the cause of the failure in #9310 though? It was not\nmerged into sage-4.4.4 and still the error is there.",
    "created_at": "2010-06-25T02:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82773",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:14 drkirkby]:
> See #9310

Is this patch the cause of the failure in #9310 though? It was not
merged into sage-4.4.4 and still the error is there.



---

archive/issue_comments_082774.json:
```json
{
    "body": "Hi Robert!\n\nAny chances to merge this patch, since it does not seem any more related to the failures than any other?\n\nThanks!",
    "created_at": "2010-07-10T01:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82774",
    "user": "https://github.com/nthiery"
}
```

Hi Robert!

Any chances to merge this patch, since it does not seem any more related to the failures than any other?

Thanks!



---

archive/issue_comments_082775.json:
```json
{
    "body": "sage-4.5 is in feature freeze mode. Nothing but essential fixes will be merged until final release. I am strongly suggesting that the next release be patches to the sage library only (other than essential spkg fixes), and tickets like these deserve to go in then. (I would have had an alpha for such tickets in the 4.5 series, but the spkg issues are already holding things up long enough.)",
    "created_at": "2010-07-11T21:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82775",
    "user": "https://github.com/rlmill"
}
```

sage-4.5 is in feature freeze mode. Nothing but essential fixes will be merged until final release. I am strongly suggesting that the next release be patches to the sage library only (other than essential spkg fixes), and tickets like these deserve to go in then. (I would have had an alpha for such tickets in the 4.5 series, but the spkg issues are already holding things up long enough.)



---

archive/issue_events_021984.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T01:55:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8984#event-21984"
}
```



---

archive/issue_comments_082776.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8984",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8984#issuecomment-82776",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
