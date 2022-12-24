# Issue 9805: Constellations

archive/issues_009805.json:
```json
{
    "body": "Assignee: vdelecroix\n\nCC:  vdelecroix slelievre\n\nKeywords: constellation, permutation, surfaces, graphs\n\nA constellation is a combinatorial description (via elements of the symmetric group) of graphs embedded in surfaces (also called G-map). This ticket aims to implement a basic class for it with:\n* fast data type\n* normal form and isomorphism test\n* enumeration/generation with constraints\n\nIssue created by migration from https://trac.sagemath.org/ticket/9806\n\n",
    "created_at": "2010-08-26T14:18:20Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "Constellations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9805",
    "user": "vdelecroix"
}
```
Assignee: vdelecroix

CC:  vdelecroix slelievre

Keywords: constellation, permutation, surfaces, graphs

A constellation is a combinatorial description (via elements of the symmetric group) of graphs embedded in surfaces (also called G-map). This ticket aims to implement a basic class for it with:
* fast data type
* normal form and isomorphism test
* enumeration/generation with constraints

Issue created by migration from https://trac.sagemath.org/ticket/9806





---

archive/issue_comments_096338.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2011-01-23T11:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96338",
    "user": "davidloeffler"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_096339.json:
```json
{
    "body": "I just had a quick look at the code. There are many procedures without documentation and tests. This should be corrected. \n\nMoreover, near the beginning of the patch, an example is given\n\n```\nsage: c = Constellation(['(0,1)', '(0,2)', None])\n```\n\nand the syntax is rather unclear. What is the meaning of none ? Why do we need quotes around permutations ?",
    "created_at": "2012-05-18T12:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96339",
    "user": "chapoton"
}
```

I just had a quick look at the code. There are many procedures without documentation and tests. This should be corrected. 

Moreover, near the beginning of the patch, an example is given

```
sage: c = Constellation(['(0,1)', '(0,2)', None])
```

and the syntax is rather unclear. What is the meaning of none ? Why do we need quotes around permutations ?



---

archive/issue_comments_096340.json:
```json
{
    "body": "Hello,\n\nThe following line appears twice at the beginning:\n\n\n```\nfrom sage.combinat.partition import Partition \n```\n",
    "created_at": "2012-06-07T09:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96340",
    "user": "chapoton"
}
```

Hello,

The following line appears twice at the beginning:


```
from sage.combinat.partition import Partition 
```




---

archive/issue_comments_096341.json:
```json
{
    "body": "Using the latest sage-combinat queue, the doctest coverage is clearly bad :\n\n\n```\nSCORE constellation.py: 25% (18 of 70)\n```\n\n\nAnd some tests are failing :\n\n\n```\n2 items had failures:\n   1 of   5 in __main__.example_0\n   2 of   5 in __main__.example_14\n***Test Failed*** 3 failures.\n```\n",
    "created_at": "2012-06-08T19:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96341",
    "user": "chapoton"
}
```

Using the latest sage-combinat queue, the doctest coverage is clearly bad :


```
SCORE constellation.py: 25% (18 of 70)
```


And some tests are failing :


```
2 items had failures:
   1 of   5 in __main__.example_0
   2 of   5 in __main__.example_14
***Test Failed*** 3 failures.
```




---

archive/issue_comments_096342.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-08T19:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96342",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096343.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-08T19:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96343",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096344.json:
```json
{
    "body": "Here is a patch with more documentation, but there is still lacking a lot of tests.\n\nI have also corrected the previously failing tests, but now some of the new tests are failing, because the procedures last() and first() do not work !",
    "created_at": "2012-06-28T09:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96344",
    "user": "chapoton"
}
```

Here is a patch with more documentation, but there is still lacking a lot of tests.

I have also corrected the previously failing tests, but now some of the new tests are failing, because the procedures last() and first() do not work !



---

archive/issue_comments_096345.json:
```json
{
    "body": "Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..",
    "created_at": "2012-07-23T19:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96345",
    "user": "chapoton"
}
```

Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..



---

archive/issue_comments_096346.json:
```json
{
    "body": "Attachment [trac_9806-constellations-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-vd.patch) by vdelecroix created at 2012-07-23 20:48:36\n\nReplying to [comment:7 chapoton]:\n> Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..\n\nDone.",
    "created_at": "2012-07-23T20:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96346",
    "user": "vdelecroix"
}
```

Attachment [trac_9806-constellations-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-vd.patch) by vdelecroix created at 2012-07-23 20:48:36

Replying to [comment:7 chapoton]:
> Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..

Done.



---

archive/issue_comments_096347.json:
```json
{
    "body": "Apply:\n\n* [attachment:trac_9806-constellations-vd.patch]\n* [attachment:trac_9806-constellations-doc-patch-fc.patch]",
    "created_at": "2012-08-28T19:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96347",
    "user": "chapoton"
}
```

Apply:

* [attachment:trac_9806-constellations-vd.patch]
* [attachment:trac_9806-constellations-doc-patch-fc.patch]



---

archive/issue_comments_096348.json:
```json
{
    "body": "Attachment [trac_9806-constellations-doc-patch-fc.2.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.2.patch) by chapoton created at 2012-09-22 12:29:49",
    "created_at": "2012-09-22T12:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96348",
    "user": "chapoton"
}
```

Attachment [trac_9806-constellations-doc-patch-fc.2.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.2.patch) by chapoton created at 2012-09-22 12:29:49



---

archive/issue_comments_096349.json:
```json
{
    "body": "Apply:\n\ntrac_9806-constellations-vd.patch \ntrac_9806-constellations-doc-patch-fc.patch",
    "created_at": "2012-09-22T12:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96349",
    "user": "chapoton"
}
```

Apply:

trac_9806-constellations-vd.patch 
trac_9806-constellations-doc-patch-fc.patch



---

archive/issue_comments_096350.json:
```json
{
    "body": "Apply trac_9806-constellations-vd.patch trac_9806-constellations-doc-patch-fc.patch",
    "created_at": "2012-11-09T16:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96350",
    "user": "chapoton"
}
```

Apply trac_9806-constellations-vd.patch trac_9806-constellations-doc-patch-fc.patch



---

archive/issue_comments_096351.json:
```json
{
    "body": "more clean up\n\nstill one failing doctest that I am not able to correct\n\nand of course, coverage is only 60% !",
    "created_at": "2013-05-20T09:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96351",
    "user": "chapoton"
}
```

more clean up

still one failing doctest that I am not able to correct

and of course, coverage is only 60% !



---

archive/issue_comments_096352.json:
```json
{
    "body": "coverage 70%",
    "created_at": "2013-05-20T20:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96352",
    "user": "chapoton"
}
```

coverage 70%



---

archive/issue_comments_096353.json:
```json
{
    "body": "coverage 80%",
    "created_at": "2013-05-23T18:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96353",
    "user": "chapoton"
}
```

coverage 80%



---

archive/issue_comments_096354.json:
```json
{
    "body": "Attachment [trac_9806-constellations-doc-patch-fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.patch) by chapoton created at 2013-05-24 18:59:21",
    "created_at": "2013-05-24T18:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96354",
    "user": "chapoton"
}
```

Attachment [trac_9806-constellations-doc-patch-fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.patch) by chapoton created at 2013-05-24 18:59:21



---

archive/issue_comments_096355.json:
```json
{
    "body": "coverage 92 %",
    "created_at": "2013-05-24T18:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96355",
    "user": "chapoton"
}
```

coverage 92 %



---

archive/issue_comments_096356.json:
```json
{
    "body": "Replying to [comment:16 chapoton]:\n> coverage 92 %\n\nThanks working on doctests !\n\nI would like to split the file in two parts. More precisely, I intend to move the first part (the little functions on permutations) in a file like sage.misc.permutations. What do you think ? Do I have the green light to fold your patch with mine and do the splitting ?\n\nBest,\nVincent",
    "created_at": "2013-05-25T12:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96356",
    "user": "vdelecroix"
}
```

Replying to [comment:16 chapoton]:
> coverage 92 %

Thanks working on doctests !

I would like to split the file in two parts. More precisely, I intend to move the first part (the little functions on permutations) in a file like sage.misc.permutations. What do you think ? Do I have the green light to fold your patch with mine and do the splitting ?

Best,
Vincent



---

archive/issue_comments_096357.json:
```json
{
    "body": "Yes, you can fold and split if you want.\n\nAnd what about removing the Test class ?",
    "created_at": "2013-05-25T12:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96357",
    "user": "chapoton"
}
```

Yes, you can fold and split if you want.

And what about removing the Test class ?



---

archive/issue_comments_096358.json:
```json
{
    "body": "By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..",
    "created_at": "2013-05-30T19:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96358",
    "user": "chapoton"
}
```

By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..



---

archive/issue_comments_096359.json:
```json
{
    "body": "Replying to [comment:19 chapoton]:\n> By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..\n\nI am currently reworking on that ticket. I folded your patch with mine but there are still some code to complete (especially doctests). I hope it will be finished soon.",
    "created_at": "2013-05-30T20:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96359",
    "user": "vdelecroix"
}
```

Replying to [comment:19 chapoton]:
> By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..

I am currently reworking on that ticket. I folded your patch with mine but there are still some code to complete (especially doctests). I hope it will be finished soon.



---

archive/issue_comments_096360.json:
```json
{
    "body": "apply trac_9806-constellations-all_in_one-vdfc.patch",
    "created_at": "2013-06-18T06:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96360",
    "user": "vdelecroix"
}
```

apply trac_9806-constellations-all_in_one-vdfc.patch



---

archive/issue_comments_096361.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-18T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96361",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096362.json:
```json
{
    "body": "apply trac_9806-constellations-all_in_one-vdfc.patch",
    "created_at": "2013-06-18T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96362",
    "user": "vdelecroix"
}
```

apply trac_9806-constellations-all_in_one-vdfc.patch



---

archive/issue_comments_096363.json:
```json
{
    "body": "documentation is not 100%, see bot report",
    "created_at": "2013-06-19T08:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96363",
    "user": "chapoton"
}
```

documentation is not 100%, see bot report



---

archive/issue_comments_096364.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-19T08:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96364",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096365.json:
```json
{
    "body": "in addition to complete the missing doc, \n\nyou should also replace 2 assert statements with some raise statements",
    "created_at": "2013-06-22T20:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96365",
    "user": "chapoton"
}
```

in addition to complete the missing doc, 

you should also replace 2 assert statements with some raise statements



---

archive/issue_comments_096366.json:
```json
{
    "body": "I have taken care of the assert statements, but there is still a gap in the documentation of perms_canonical_labels",
    "created_at": "2013-07-05T20:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96366",
    "user": "chapoton"
}
```

I have taken care of the assert statements, but there is still a gap in the documentation of perms_canonical_labels



---

archive/issue_comments_096367.json:
```json
{
    "body": "Attachment [trac_9806_review_fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_review_fc.patch) by chapoton created at 2013-07-25 14:37:10",
    "created_at": "2013-07-25T14:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96367",
    "user": "chapoton"
}
```

Attachment [trac_9806_review_fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_review_fc.patch) by chapoton created at 2013-07-25 14:37:10



---

archive/issue_comments_096368.json:
```json
{
    "body": "Well, the bot has turned green. Now we can maybe **start** to discuss the content.\n\nI am still not happy with the function \"perms_canonical_labels\". could you explain what it does, please ?",
    "created_at": "2013-07-25T14:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96368",
    "user": "chapoton"
}
```

Well, the bot has turned green. Now we can maybe **start** to discuss the content.

I am still not happy with the function "perms_canonical_labels". could you explain what it does, please ?



---

archive/issue_comments_096369.json:
```json
{
    "body": "Thanks for your corrections.\n\n`perms_canonical_labels` is a way to conjugate a tuple of permutations (s_1,s_2,\\ldots,s_k) in such way that two conjugate tuples have the same image under this canonical labeling. The reason is that (as in topological graph) we want to consider isomorphism class of objects. Though, in `Graph/DiGraph` the method is simply named `relabel` and perhaps I should stick to this convention. One advantage here is that this method is very fast (complexity O(n<sup>2</sup>) for a tuple of degree n).\n\nI am starting to use intinsively the patch. And the most interesting part is not yet in there: I am interested in the set of constellations with fixed profile (or passport). In other words, I want to fix the conjugacy classes of all permutations. There is no such parent in the current patch. Note that generating constellations of fixed profile is far less trivial than generating constellations. . We have at least one interesting thing: we know the cardinality of that set via representation theory (Frobenius formula). But I do not know how much the formula is praticable (there is a sum over all characters of the group).",
    "created_at": "2013-07-25T16:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96369",
    "user": "vdelecroix"
}
```

Thanks for your corrections.

`perms_canonical_labels` is a way to conjugate a tuple of permutations (s_1,s_2,\ldots,s_k) in such way that two conjugate tuples have the same image under this canonical labeling. The reason is that (as in topological graph) we want to consider isomorphism class of objects. Though, in `Graph/DiGraph` the method is simply named `relabel` and perhaps I should stick to this convention. One advantage here is that this method is very fast (complexity O(n<sup>2</sup>) for a tuple of degree n).

I am starting to use intinsively the patch. And the most interesting part is not yet in there: I am interested in the set of constellations with fixed profile (or passport). In other words, I want to fix the conjugacy classes of all permutations. There is no such parent in the current patch. Note that generating constellations of fixed profile is far less trivial than generating constellations. . We have at least one interesting thing: we know the cardinality of that set via representation theory (Frobenius formula). But I do not know how much the formula is praticable (there is a sum over all characters of the group).



---

archive/issue_comments_096370.json:
```json
{
    "body": "Attachment [trac_9806-constellations-all_in_one-vdfc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-all_in_one-vdfc.patch) by vdelecroix created at 2013-09-22 14:11:01",
    "created_at": "2013-09-22T14:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96370",
    "user": "vdelecroix"
}
```

Attachment [trac_9806-constellations-all_in_one-vdfc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-all_in_one-vdfc.patch) by vdelecroix created at 2013-09-22 14:11:01



---

archive/issue_comments_096371.json:
```json
{
    "body": "Attachment [trac_9806_doc_canonical_labels-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_doc_canonical_labels-vd.patch) by vdelecroix created at 2013-09-22 14:29:54",
    "created_at": "2013-09-22T14:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96371",
    "user": "vdelecroix"
}
```

Attachment [trac_9806_doc_canonical_labels-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_doc_canonical_labels-vd.patch) by vdelecroix created at 2013-09-22 14:29:54



---

archive/issue_comments_096372.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-09-22T14:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96372",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096373.json:
```json
{
    "body": "apply trac_9806-constellations-all_in_one-vdfc.patch trac_9806_review_fc.patch trac_9806_doc_canonical_labels-vd.patch",
    "created_at": "2013-09-22T14:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96373",
    "user": "vdelecroix"
}
```

apply trac_9806-constellations-all_in_one-vdfc.patch trac_9806_review_fc.patch trac_9806_doc_canonical_labels-vd.patch



---

archive/issue_comments_096374.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-04T20:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96374",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_096375.json:
```json
{
    "body": "Rebase on sage-6.2.beta6 and bug corrected in connected_components.\n----\nNew commits:",
    "created_at": "2014-04-08T19:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96375",
    "user": "vdelecroix"
}
```

Rebase on sage-6.2.beta6 and bug corrected in connected_components.
----
New commits:



---

archive/issue_comments_096376.json:
```json
{
    "body": "I have made minor corrections, there were unused imports and undefined variables (found using pyflakes)\n----\nNew commits:",
    "created_at": "2014-05-10T06:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96376",
    "user": "chapoton"
}
```

I have made minor corrections, there were unused imports and undefined variables (found using pyflakes)
----
New commits:



---

archive/issue_comments_096377.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-01-21T12:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96377",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096378.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-01-21T20:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96378",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096379.json:
```json
{
    "body": "Hello,\n\nBetter than pep8 standard, we now have permutations in Sage that start with `0`. The code has to be rewritten using that and not the standalone implementation in `sage.misc.permutation`.\n\nVincent",
    "created_at": "2015-01-21T20:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96379",
    "user": "vdelecroix"
}
```

Hello,

Better than pep8 standard, we now have permutations in Sage that start with `0`. The code has to be rewritten using that and not the standalone implementation in `sage.misc.permutation`.

Vincent



---

archive/issue_comments_096380.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-01-21T20:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96380",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096381.json:
```json
{
    "body": "Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?",
    "created_at": "2015-01-23T12:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96381",
    "user": "chapoton"
}
```

Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?



---

archive/issue_comments_096382.json:
```json
{
    "body": "Replying to [comment:41 chapoton]:\n> Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?\n\n\n```\nsage: S5 = SymmetricGroup(range(5))\nsage: S5.an_element()\n(0,1,2,3,4)\n```\n\n\nVincent",
    "created_at": "2015-01-23T13:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96382",
    "user": "vdelecroix"
}
```

Replying to [comment:41 chapoton]:
> Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?


```
sage: S5 = SymmetricGroup(range(5))
sage: S5.an_element()
(0,1,2,3,4)
```


Vincent



---

archive/issue_comments_096383.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-28T19:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96383",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096384.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-11-20T21:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96384",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096385.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-01T11:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96385",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096386.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-26T12:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96386",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096387.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-26T12:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96387",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096388.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-26T12:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96388",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_096389.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-26T18:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96389",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096390.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-27T08:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96390",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096391.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-27T13:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96391",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096392.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-03-27T13:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96392",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096393.json:
```json
{
    "body": "I have just done a lot of work on that ticket.\n\nI think this is getting closer to be ready. I would like to have somebody else have a look at that.",
    "created_at": "2016-03-27T13:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96393",
    "user": "chapoton"
}
```

I have just done a lot of work on that ticket.

I think this is getting closer to be ready. I would like to have somebody else have a look at that.



---

archive/issue_comments_096394.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-27T17:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96394",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096395.json:
```json
{
    "body": "Vincent, would you *please* have a look ?\n\nWhat should I do with the three remaining functions in permutations.py ? transfer them\nback to the constellation file ?",
    "created_at": "2016-03-29T18:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96395",
    "user": "chapoton"
}
```

Vincent, would you *please* have a look ?

What should I do with the three remaining functions in permutations.py ? transfer them
back to the constellation file ?



---

archive/issue_comments_096396.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-29T19:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96396",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096397.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-29T19:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96397",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096398.json:
```json
{
    "body": "I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.\n\nSince you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.\n\nWhen you check matching with the oeis sequence 220754, you can also do that in Sage\n\n```\nsage: seq = oeis('A220754')\nsage: seq\nA220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.\nsage: seq.first_terms()\n(1,\n 7,\n 194,\n 12858,\n 1647384,\n 361351560,\n 125116670160,\n 64439768489040,\n 47159227114392960,\n 47285264408385951360,\n 63057420721939066617600,\n 109118766834521171299756800,\n 239996135160204867851157273600,\n 659114500480471292127627441484800)\n```\n\n\nThe fact that the associated permutation group is transitive is equivalent to the \"connectedness\". You should either use one or the other.",
    "created_at": "2016-03-29T21:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96398",
    "user": "vdelecroix"
}
```

I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.

Since you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.

When you check matching with the oeis sequence 220754, you can also do that in Sage

```
sage: seq = oeis('A220754')
sage: seq
A220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.
sage: seq.first_terms()
(1,
 7,
 194,
 12858,
 1647384,
 361351560,
 125116670160,
 64439768489040,
 47159227114392960,
 47285264408385951360,
 63057420721939066617600,
 109118766834521171299756800,
 239996135160204867851157273600,
 659114500480471292127627441484800)
```


The fact that the associated permutation group is transitive is equivalent to the "connectedness". You should either use one or the other.



---

archive/issue_comments_096399.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-30T07:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96399",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096400.json:
```json
{
    "body": "Replying to [comment:62 vdelecroix]:\n> I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.\n\nok, done\n\n> Since you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.\n\nmaybe for a later ticket ? this one has been waiting for years\n\n> When you check matching with the oeis sequence 220754, you can also do that in Sage\n> {{{\n> sage: seq = oeis('A220754')\n> sage: seq\n> A220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.\n> sage: seq.first_terms()\n> (1,\n>  7,\n>  194,\n>  12858,\n>  1647384,\n>  361351560,\n>  125116670160,\n>  64439768489040,\n>  47159227114392960,\n>  47285264408385951360,\n>  63057420721939066617600,\n>  109118766834521171299756800,\n>  239996135160204867851157273600,\n>  659114500480471292127627441484800)\n> }}}\n\nI know. I would prefer not to depend on \"optional internet\". The current test is good enough.\n\n> The fact that the associated permutation group is transitive is equivalent to the \"connectedness\". You should either use one or the other.\n\nSorry, but where is the exact problem you talk about ?",
    "created_at": "2016-03-30T08:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96400",
    "user": "chapoton"
}
```

Replying to [comment:62 vdelecroix]:
> I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.

ok, done

> Since you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.

maybe for a later ticket ? this one has been waiting for years

> When you check matching with the oeis sequence 220754, you can also do that in Sage
> {{{
> sage: seq = oeis('A220754')
> sage: seq
> A220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.
> sage: seq.first_terms()
> (1,
>  7,
>  194,
>  12858,
>  1647384,
>  361351560,
>  125116670160,
>  64439768489040,
>  47159227114392960,
>  47285264408385951360,
>  63057420721939066617600,
>  109118766834521171299756800,
>  239996135160204867851157273600,
>  659114500480471292127627441484800)
> }}}

I know. I would prefer not to depend on "optional internet". The current test is good enough.

> The fact that the associated permutation group is transitive is equivalent to the "connectedness". You should either use one or the other.

Sorry, but where is the exact problem you talk about ?



---

archive/issue_comments_096401.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-02T09:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96401",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096402.json:
```json
{
    "body": "Vincent, is the current state good enough for you ?",
    "created_at": "2016-04-06T19:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96402",
    "user": "chapoton"
}
```

Vincent, is the current state good enough for you ?



---

archive/issue_comments_096403.json:
```json
{
    "body": "The support for any symmetric group was completely broken! Moreover, I double checked and many methods were broken.\n\nYou can start the review from the current code. And please keep the code in `perm_X` to work only with list on `0, 1, ..., d-1`.\n----\nNew commits:",
    "created_at": "2016-04-11T01:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96403",
    "user": "vdelecroix"
}
```

The support for any symmetric group was completely broken! Moreover, I double checked and many methods were broken.

You can start the review from the current code. And please keep the code in `perm_X` to work only with list on `0, 1, ..., d-1`.
----
New commits:



---

archive/issue_comments_096404.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-04-11T01:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96404",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_096405.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-11T01:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96405",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096406.json:
```json
{
    "body": "Hello,\n\n* you need to doctest the two functions that you re-introduced \n\n* you need to correct the doctest for hash, which is failing on 32-bit machines (see patchbot reports)",
    "created_at": "2016-04-11T08:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96406",
    "user": "chapoton"
}
```

Hello,

* you need to doctest the two functions that you re-introduced 

* you need to correct the doctest for hash, which is failing on 32-bit machines (see patchbot reports)



---

archive/issue_comments_096407.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-04-11T09:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96407",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096408.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-04-26T19:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96408",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096409.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-04-26T19:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96409",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_096410.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-27T06:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96410",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096411.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-27T09:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96411",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096412.json:
```json
{
    "body": "vincent, would you like to get this in sage ?",
    "created_at": "2016-04-29T19:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96412",
    "user": "chapoton"
}
```

vincent, would you like to get this in sage ?



---

archive/issue_comments_096413.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-05-19T12:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96413",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096414.json:
```json
{
    "body": "I would like to set this to `positive review`. `@`vdelecroix, do you agree ?",
    "created_at": "2016-05-27T07:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96414",
    "user": "chapoton"
}
```

I would like to set this to `positive review`. `@`vdelecroix, do you agree ?



---

archive/issue_comments_096415.json:
```json
{
    "body": "Yes it looks good.",
    "created_at": "2016-05-27T14:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96415",
    "user": "vdelecroix"
}
```

Yes it looks good.



---

archive/issue_comments_096416.json:
```json
{
    "body": "ok, I take this as a green light ot positive review. Thanks.",
    "created_at": "2016-05-27T14:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96416",
    "user": "chapoton"
}
```

ok, I take this as a green light ot positive review. Thanks.



---

archive/issue_comments_096417.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-05-27T14:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96417",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096418.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-05-28T12:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96418",
    "user": "vbraun"
}
```

Resolution: fixed
