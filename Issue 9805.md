# Issue 9805: Constellations

archive/issues_009805.json:
```json
{
    "body": "Assignee: @videlec\n\nCC:  @videlec @slel\n\nKeywords: constellation, permutation, surfaces, graphs\n\nA constellation is a combinatorial description (via elements of the symmetric group) of graphs embedded in surfaces (also called G-map). This ticket aims to implement a basic class for it with:\n* fast data type\n* normal form and isomorphism test\n* enumeration/generation with constraints\n\nIssue created by migration from https://trac.sagemath.org/ticket/9806\n\n",
    "created_at": "2010-08-26T14:18:20Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "Constellations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9805",
    "user": "https://github.com/videlec"
}
```
Assignee: @videlec

CC:  @videlec @slel

Keywords: constellation, permutation, surfaces, graphs

A constellation is a combinatorial description (via elements of the symmetric group) of graphs embedded in surfaces (also called G-map). This ticket aims to implement a basic class for it with:
* fast data type
* normal form and isomorphism test
* enumeration/generation with constraints

Issue created by migration from https://trac.sagemath.org/ticket/9806





---

archive/issue_comments_096179.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2011-01-23T11:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96179",
    "user": "https://github.com/loefflerd"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_096180.json:
```json
{
    "body": "I just had a quick look at the code. There are many procedures without documentation and tests. This should be corrected. \n\nMoreover, near the beginning of the patch, an example is given\n\n```\nsage: c = Constellation(['(0,1)', '(0,2)', None])\n```\n\nand the syntax is rather unclear. What is the meaning of none ? Why do we need quotes around permutations ?",
    "created_at": "2012-05-18T12:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96180",
    "user": "https://github.com/fchapoton"
}
```

I just had a quick look at the code. There are many procedures without documentation and tests. This should be corrected. 

Moreover, near the beginning of the patch, an example is given

```
sage: c = Constellation(['(0,1)', '(0,2)', None])
```

and the syntax is rather unclear. What is the meaning of none ? Why do we need quotes around permutations ?



---

archive/issue_comments_096181.json:
```json
{
    "body": "Hello,\n\nThe following line appears twice at the beginning:\n\n\n```\nfrom sage.combinat.partition import Partition \n```\n",
    "created_at": "2012-06-07T09:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96181",
    "user": "https://github.com/fchapoton"
}
```

Hello,

The following line appears twice at the beginning:


```
from sage.combinat.partition import Partition 
```




---

archive/issue_comments_096182.json:
```json
{
    "body": "Using the latest sage-combinat queue, the doctest coverage is clearly bad :\n\n\n```\nSCORE constellation.py: 25% (18 of 70)\n```\n\n\nAnd some tests are failing :\n\n\n```\n2 items had failures:\n   1 of   5 in __main__.example_0\n   2 of   5 in __main__.example_14\n***Test Failed*** 3 failures.\n```\n",
    "created_at": "2012-06-08T19:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96182",
    "user": "https://github.com/fchapoton"
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

archive/issue_comments_096183.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-08T19:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96183",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096184.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-08T19:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96184",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096185.json:
```json
{
    "body": "Here is a patch with more documentation, but there is still lacking a lot of tests.\n\nI have also corrected the previously failing tests, but now some of the new tests are failing, because the procedures last() and first() do not work !",
    "created_at": "2012-06-28T09:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96185",
    "user": "https://github.com/fchapoton"
}
```

Here is a patch with more documentation, but there is still lacking a lot of tests.

I have also corrected the previously failing tests, but now some of the new tests are failing, because the procedures last() and first() do not work !



---

archive/issue_comments_096186.json:
```json
{
    "body": "Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..",
    "created_at": "2012-07-23T19:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96186",
    "user": "https://github.com/fchapoton"
}
```

Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..



---

archive/issue_comments_096187.json:
```json
{
    "body": "Attachment [trac_9806-constellations-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-vd.patch) by @videlec created at 2012-07-23 20:48:36\n\nReplying to [comment:7 chapoton]:\n> Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..\n\nDone.",
    "created_at": "2012-07-23T20:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96187",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_9806-constellations-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-vd.patch) by @videlec created at 2012-07-23 20:48:36

Replying to [comment:7 chapoton]:
> Could you please upload the most recent constellation patch from the sage-combinat queue ? It seems that the version there is not the same, and my review patch does not apply ..

Done.



---

archive/issue_comments_096188.json:
```json
{
    "body": "Apply:\n\n* [attachment:trac_9806-constellations-vd.patch]\n* [attachment:trac_9806-constellations-doc-patch-fc.patch]",
    "created_at": "2012-08-28T19:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96188",
    "user": "https://github.com/fchapoton"
}
```

Apply:

* [attachment:trac_9806-constellations-vd.patch]
* [attachment:trac_9806-constellations-doc-patch-fc.patch]



---

archive/issue_comments_096189.json:
```json
{
    "body": "Attachment [trac_9806-constellations-doc-patch-fc.2.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.2.patch) by @fchapoton created at 2012-09-22 12:29:49",
    "created_at": "2012-09-22T12:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96189",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_9806-constellations-doc-patch-fc.2.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.2.patch) by @fchapoton created at 2012-09-22 12:29:49



---

archive/issue_comments_096190.json:
```json
{
    "body": "Apply:\n\ntrac_9806-constellations-vd.patch \ntrac_9806-constellations-doc-patch-fc.patch",
    "created_at": "2012-09-22T12:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96190",
    "user": "https://github.com/fchapoton"
}
```

Apply:

trac_9806-constellations-vd.patch 
trac_9806-constellations-doc-patch-fc.patch



---

archive/issue_comments_096191.json:
```json
{
    "body": "Apply trac_9806-constellations-vd.patch trac_9806-constellations-doc-patch-fc.patch",
    "created_at": "2012-11-09T16:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96191",
    "user": "https://github.com/fchapoton"
}
```

Apply trac_9806-constellations-vd.patch trac_9806-constellations-doc-patch-fc.patch



---

archive/issue_comments_096192.json:
```json
{
    "body": "more clean up\n\nstill one failing doctest that I am not able to correct\n\nand of course, coverage is only 60% !",
    "created_at": "2013-05-20T09:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96192",
    "user": "https://github.com/fchapoton"
}
```

more clean up

still one failing doctest that I am not able to correct

and of course, coverage is only 60% !



---

archive/issue_comments_096193.json:
```json
{
    "body": "coverage 70%",
    "created_at": "2013-05-20T20:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96193",
    "user": "https://github.com/fchapoton"
}
```

coverage 70%



---

archive/issue_comments_096194.json:
```json
{
    "body": "coverage 80%",
    "created_at": "2013-05-23T18:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96194",
    "user": "https://github.com/fchapoton"
}
```

coverage 80%



---

archive/issue_comments_096195.json:
```json
{
    "body": "Attachment [trac_9806-constellations-doc-patch-fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.patch) by @fchapoton created at 2013-05-24 18:59:21",
    "created_at": "2013-05-24T18:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96195",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_9806-constellations-doc-patch-fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-doc-patch-fc.patch) by @fchapoton created at 2013-05-24 18:59:21



---

archive/issue_comments_096196.json:
```json
{
    "body": "coverage 92 %",
    "created_at": "2013-05-24T18:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96196",
    "user": "https://github.com/fchapoton"
}
```

coverage 92 %



---

archive/issue_comments_096197.json:
```json
{
    "body": "Replying to [comment:16 chapoton]:\n> coverage 92 %\n\nThanks working on doctests !\n\nI would like to split the file in two parts. More precisely, I intend to move the first part (the little functions on permutations) in a file like sage.misc.permutations. What do you think ? Do I have the green light to fold your patch with mine and do the splitting ?\n\nBest,\nVincent",
    "created_at": "2013-05-25T12:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96197",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:16 chapoton]:
> coverage 92 %

Thanks working on doctests !

I would like to split the file in two parts. More precisely, I intend to move the first part (the little functions on permutations) in a file like sage.misc.permutations. What do you think ? Do I have the green light to fold your patch with mine and do the splitting ?

Best,
Vincent



---

archive/issue_comments_096198.json:
```json
{
    "body": "Yes, you can fold and split if you want.\n\nAnd what about removing the Test class ?",
    "created_at": "2013-05-25T12:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96198",
    "user": "https://github.com/fchapoton"
}
```

Yes, you can fold and split if you want.

And what about removing the Test class ?



---

archive/issue_comments_096199.json:
```json
{
    "body": "By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..",
    "created_at": "2013-05-30T19:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96199",
    "user": "https://github.com/fchapoton"
}
```

By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..



---

archive/issue_comments_096200.json:
```json
{
    "body": "Replying to [comment:19 chapoton]:\n> By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..\n\nI am currently reworking on that ticket. I folded your patch with mine but there are still some code to complete (especially doctests). I hope it will be finished soon.",
    "created_at": "2013-05-30T20:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96200",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:19 chapoton]:
> By the way, could you also solve the failing doctest ? Most likely, I have not been able to figure out what input should be fed to this method..

I am currently reworking on that ticket. I folded your patch with mine but there are still some code to complete (especially doctests). I hope it will be finished soon.



---

archive/issue_comments_096201.json:
```json
{
    "body": "apply trac_9806-constellations-all_in_one-vdfc.patch",
    "created_at": "2013-06-18T06:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96201",
    "user": "https://github.com/videlec"
}
```

apply trac_9806-constellations-all_in_one-vdfc.patch



---

archive/issue_comments_096202.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-18T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96202",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096203.json:
```json
{
    "body": "apply trac_9806-constellations-all_in_one-vdfc.patch",
    "created_at": "2013-06-18T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96203",
    "user": "https://github.com/videlec"
}
```

apply trac_9806-constellations-all_in_one-vdfc.patch



---

archive/issue_comments_096204.json:
```json
{
    "body": "documentation is not 100%, see bot report",
    "created_at": "2013-06-19T08:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96204",
    "user": "https://github.com/fchapoton"
}
```

documentation is not 100%, see bot report



---

archive/issue_comments_096205.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-19T08:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96205",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096206.json:
```json
{
    "body": "in addition to complete the missing doc, \n\nyou should also replace 2 assert statements with some raise statements",
    "created_at": "2013-06-22T20:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96206",
    "user": "https://github.com/fchapoton"
}
```

in addition to complete the missing doc, 

you should also replace 2 assert statements with some raise statements



---

archive/issue_comments_096207.json:
```json
{
    "body": "I have taken care of the assert statements, but there is still a gap in the documentation of perms_canonical_labels",
    "created_at": "2013-07-05T20:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96207",
    "user": "https://github.com/fchapoton"
}
```

I have taken care of the assert statements, but there is still a gap in the documentation of perms_canonical_labels



---

archive/issue_comments_096208.json:
```json
{
    "body": "Attachment [trac_9806_review_fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_review_fc.patch) by @fchapoton created at 2013-07-25 14:37:10",
    "created_at": "2013-07-25T14:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96208",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_9806_review_fc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_review_fc.patch) by @fchapoton created at 2013-07-25 14:37:10



---

archive/issue_comments_096209.json:
```json
{
    "body": "Well, the bot has turned green. Now we can maybe **start** to discuss the content.\n\nI am still not happy with the function \"perms_canonical_labels\". could you explain what it does, please ?",
    "created_at": "2013-07-25T14:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96209",
    "user": "https://github.com/fchapoton"
}
```

Well, the bot has turned green. Now we can maybe **start** to discuss the content.

I am still not happy with the function "perms_canonical_labels". could you explain what it does, please ?



---

archive/issue_comments_096210.json:
```json
{
    "body": "Thanks for your corrections.\n\n`perms_canonical_labels` is a way to conjugate a tuple of permutations (s_1,s_2,\\ldots,s_k) in such way that two conjugate tuples have the same image under this canonical labeling. The reason is that (as in topological graph) we want to consider isomorphism class of objects. Though, in `Graph/DiGraph` the method is simply named `relabel` and perhaps I should stick to this convention. One advantage here is that this method is very fast (complexity O(n<sup>2</sup>) for a tuple of degree n).\n\nI am starting to use intinsively the patch. And the most interesting part is not yet in there: I am interested in the set of constellations with fixed profile (or passport). In other words, I want to fix the conjugacy classes of all permutations. There is no such parent in the current patch. Note that generating constellations of fixed profile is far less trivial than generating constellations. . We have at least one interesting thing: we know the cardinality of that set via representation theory (Frobenius formula). But I do not know how much the formula is praticable (there is a sum over all characters of the group).",
    "created_at": "2013-07-25T16:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96210",
    "user": "https://github.com/videlec"
}
```

Thanks for your corrections.

`perms_canonical_labels` is a way to conjugate a tuple of permutations (s_1,s_2,\ldots,s_k) in such way that two conjugate tuples have the same image under this canonical labeling. The reason is that (as in topological graph) we want to consider isomorphism class of objects. Though, in `Graph/DiGraph` the method is simply named `relabel` and perhaps I should stick to this convention. One advantage here is that this method is very fast (complexity O(n<sup>2</sup>) for a tuple of degree n).

I am starting to use intinsively the patch. And the most interesting part is not yet in there: I am interested in the set of constellations with fixed profile (or passport). In other words, I want to fix the conjugacy classes of all permutations. There is no such parent in the current patch. Note that generating constellations of fixed profile is far less trivial than generating constellations. . We have at least one interesting thing: we know the cardinality of that set via representation theory (Frobenius formula). But I do not know how much the formula is praticable (there is a sum over all characters of the group).



---

archive/issue_comments_096211.json:
```json
{
    "body": "Attachment [trac_9806-constellations-all_in_one-vdfc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-all_in_one-vdfc.patch) by @videlec created at 2013-09-22 14:11:01",
    "created_at": "2013-09-22T14:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96211",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_9806-constellations-all_in_one-vdfc.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806-constellations-all_in_one-vdfc.patch) by @videlec created at 2013-09-22 14:11:01



---

archive/issue_comments_096212.json:
```json
{
    "body": "Attachment [trac_9806_doc_canonical_labels-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_doc_canonical_labels-vd.patch) by @videlec created at 2013-09-22 14:29:54",
    "created_at": "2013-09-22T14:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96212",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_9806_doc_canonical_labels-vd.patch](tarball://root/attachments/some-uuid/ticket9806/trac_9806_doc_canonical_labels-vd.patch) by @videlec created at 2013-09-22 14:29:54



---

archive/issue_comments_096213.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-09-22T14:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96213",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096214.json:
```json
{
    "body": "apply trac_9806-constellations-all_in_one-vdfc.patch trac_9806_review_fc.patch trac_9806_doc_canonical_labels-vd.patch",
    "created_at": "2013-09-22T14:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96214",
    "user": "https://github.com/videlec"
}
```

apply trac_9806-constellations-all_in_one-vdfc.patch trac_9806_review_fc.patch trac_9806_doc_canonical_labels-vd.patch



---

archive/issue_comments_096215.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-04T20:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96215",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_096216.json:
```json
{
    "body": "Rebase on sage-6.2.beta6 and bug corrected in connected_components.\n----\nNew commits:",
    "created_at": "2014-04-08T19:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96216",
    "user": "https://github.com/videlec"
}
```

Rebase on sage-6.2.beta6 and bug corrected in connected_components.
----
New commits:



---

archive/issue_comments_096217.json:
```json
{
    "body": "I have made minor corrections, there were unused imports and undefined variables (found using pyflakes)\n----\nNew commits:",
    "created_at": "2014-05-10T06:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96217",
    "user": "https://github.com/fchapoton"
}
```

I have made minor corrections, there were unused imports and undefined variables (found using pyflakes)
----
New commits:



---

archive/issue_comments_096218.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-01-21T12:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96218",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096219.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-01-21T20:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96219",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096220.json:
```json
{
    "body": "Hello,\n\nBetter than pep8 standard, we now have permutations in Sage that start with `0`. The code has to be rewritten using that and not the standalone implementation in `sage.misc.permutation`.\n\nVincent",
    "created_at": "2015-01-21T20:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96220",
    "user": "https://github.com/videlec"
}
```

Hello,

Better than pep8 standard, we now have permutations in Sage that start with `0`. The code has to be rewritten using that and not the standalone implementation in `sage.misc.permutation`.

Vincent



---

archive/issue_comments_096221.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-01-21T20:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96221",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096222.json:
```json
{
    "body": "Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?",
    "created_at": "2015-01-23T12:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96222",
    "user": "https://github.com/fchapoton"
}
```

Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?



---

archive/issue_comments_096223.json:
```json
{
    "body": "Replying to [comment:41 chapoton]:\n> Well, great. This was my main problem with this branch. Where are the permutations starting with 0 inside sage ?\n\n\n```\nsage: S5 = SymmetricGroup(range(5))\nsage: S5.an_element()\n(0,1,2,3,4)\n```\n\n\nVincent",
    "created_at": "2015-01-23T13:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96223",
    "user": "https://github.com/videlec"
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

archive/issue_comments_096224.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-10-28T19:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96224",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096225.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-11-20T21:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96225",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096226.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-01T11:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96226",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096227.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-26T12:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96227",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096228.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-26T12:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96228",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096229.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-03-26T12:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96229",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_096230.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-26T18:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96230",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096231.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-27T08:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96231",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096232.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-27T13:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96232",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096233.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-03-27T13:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96233",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096234.json:
```json
{
    "body": "I have just done a lot of work on that ticket.\n\nI think this is getting closer to be ready. I would like to have somebody else have a look at that.",
    "created_at": "2016-03-27T13:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96234",
    "user": "https://github.com/fchapoton"
}
```

I have just done a lot of work on that ticket.

I think this is getting closer to be ready. I would like to have somebody else have a look at that.



---

archive/issue_comments_096235.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-27T17:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96235",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096236.json:
```json
{
    "body": "Vincent, would you *please* have a look ?\n\nWhat should I do with the three remaining functions in permutations.py ? transfer them\nback to the constellation file ?",
    "created_at": "2016-03-29T18:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96236",
    "user": "https://github.com/fchapoton"
}
```

Vincent, would you *please* have a look ?

What should I do with the three remaining functions in permutations.py ? transfer them
back to the constellation file ?



---

archive/issue_comments_096237.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-29T19:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96237",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096238.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-29T19:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96238",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096239.json:
```json
{
    "body": "I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.\n\nSince you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.\n\nWhen you check matching with the oeis sequence 220754, you can also do that in Sage\n\n```\nsage: seq = oeis('A220754')\nsage: seq\nA220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.\nsage: seq.first_terms()\n(1,\n 7,\n 194,\n 12858,\n 1647384,\n 361351560,\n 125116670160,\n 64439768489040,\n 47159227114392960,\n 47285264408385951360,\n 63057420721939066617600,\n 109118766834521171299756800,\n 239996135160204867851157273600,\n 659114500480471292127627441484800)\n```\n\n\nThe fact that the associated permutation group is transitive is equivalent to the \"connectedness\". You should either use one or the other.",
    "created_at": "2016-03-29T21:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96239",
    "user": "https://github.com/videlec"
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

archive/issue_comments_096240.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-30T07:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96240",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096241.json:
```json
{
    "body": "Replying to [comment:62 vdelecroix]:\n> I guess that it makes sense to move the remaining functions from `sage.misc.permutation` inside `constellation.py`.\n\nok, done\n\n> Since you are now using permutations, I would actually allow any domain. In other words, add a fixed symmetric group attribute to `Constellations`.\n\nmaybe for a later ticket ? this one has been waiting for years\n\n> When you check matching with the oeis sequence 220754, you can also do that in Sage\n> {{{\n> sage: seq = oeis('A220754')\n> sage: seq\n> A220754: Number of ordered triples (a,b,c) of elements of the symmetric group S_n such that the triple a,b,c generates a transitive group.\n> sage: seq.first_terms()\n> (1,\n>  7,\n>  194,\n>  12858,\n>  1647384,\n>  361351560,\n>  125116670160,\n>  64439768489040,\n>  47159227114392960,\n>  47285264408385951360,\n>  63057420721939066617600,\n>  109118766834521171299756800,\n>  239996135160204867851157273600,\n>  659114500480471292127627441484800)\n> }}}\n\nI know. I would prefer not to depend on \"optional internet\". The current test is good enough.\n\n> The fact that the associated permutation group is transitive is equivalent to the \"connectedness\". You should either use one or the other.\n\nSorry, but where is the exact problem you talk about ?",
    "created_at": "2016-03-30T08:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96241",
    "user": "https://github.com/fchapoton"
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

archive/issue_comments_096242.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-02T09:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96242",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096243.json:
```json
{
    "body": "Vincent, is the current state good enough for you ?",
    "created_at": "2016-04-06T19:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96243",
    "user": "https://github.com/fchapoton"
}
```

Vincent, is the current state good enough for you ?



---

archive/issue_comments_096244.json:
```json
{
    "body": "The support for any symmetric group was completely broken! Moreover, I double checked and many methods were broken.\n\nYou can start the review from the current code. And please keep the code in `perm_X` to work only with list on `0, 1, ..., d-1`.\n----\nNew commits:",
    "created_at": "2016-04-11T01:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96244",
    "user": "https://github.com/videlec"
}
```

The support for any symmetric group was completely broken! Moreover, I double checked and many methods were broken.

You can start the review from the current code. And please keep the code in `perm_X` to work only with list on `0, 1, ..., d-1`.
----
New commits:



---

archive/issue_comments_096245.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-04-11T01:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96245",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_096246.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-11T01:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96246",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096247.json:
```json
{
    "body": "Hello,\n\n* you need to doctest the two functions that you re-introduced \n\n* you need to correct the doctest for hash, which is failing on 32-bit machines (see patchbot reports)",
    "created_at": "2016-04-11T08:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96247",
    "user": "https://github.com/fchapoton"
}
```

Hello,

* you need to doctest the two functions that you re-introduced 

* you need to correct the doctest for hash, which is failing on 32-bit machines (see patchbot reports)



---

archive/issue_comments_096248.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-04-11T09:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96248",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_096249.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-04-26T19:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96249",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096250.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-04-26T19:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96250",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_096251.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-27T06:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96251",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096252.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-27T09:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96252",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096253.json:
```json
{
    "body": "vincent, would you like to get this in sage ?",
    "created_at": "2016-04-29T19:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96253",
    "user": "https://github.com/fchapoton"
}
```

vincent, would you like to get this in sage ?



---

archive/issue_comments_096254.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-05-19T12:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96254",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_096255.json:
```json
{
    "body": "I would like to set this to `positive review`. `@`vdelecroix, do you agree ?",
    "created_at": "2016-05-27T07:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96255",
    "user": "https://github.com/fchapoton"
}
```

I would like to set this to `positive review`. `@`vdelecroix, do you agree ?



---

archive/issue_comments_096256.json:
```json
{
    "body": "Yes it looks good.",
    "created_at": "2016-05-27T14:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96256",
    "user": "https://github.com/videlec"
}
```

Yes it looks good.



---

archive/issue_comments_096257.json:
```json
{
    "body": "ok, I take this as a green light ot positive review. Thanks.",
    "created_at": "2016-05-27T14:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96257",
    "user": "https://github.com/fchapoton"
}
```

ok, I take this as a green light ot positive review. Thanks.



---

archive/issue_comments_096258.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-05-27T14:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96258",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096259.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-05-28T12:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9805#issuecomment-96259",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_009929.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-05-28T12:13:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9805",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9805#event-9929"
}
```
