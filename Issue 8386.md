# Issue 8386: iet alphabet bug and rebased datatype

archive/issues_008386.json:
```json
{
    "body": "Assignee: vdelecroix\n\nCC:  sage-combinat tmonteil\n\nKeywords: iet combinatoric\n\nThere was a bug for iet.Permutation comparisons. We have the following\n\n```\nsage: p = iet.Permutation('a b','b a')\nsage: q = iet.Permutation('b a','a b')\nsage: p == q\nTrue\n```\n\n\nThe patch correct this feature (we get wrong) and rebased the datatype used for iet.Permutations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8386\n\n",
    "created_at": "2010-02-27T13:06:33Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "iet alphabet bug and rebased datatype",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8386",
    "user": "vdelecroix"
}
```
Assignee: vdelecroix

CC:  sage-combinat tmonteil

Keywords: iet combinatoric

There was a bug for iet.Permutation comparisons. We have the following

```
sage: p = iet.Permutation('a b','b a')
sage: q = iet.Permutation('b a','a b')
sage: p == q
True
```


The patch correct this feature (we get wrong) and rebased the datatype used for iet.Permutations.

Issue created by migration from https://trac.sagemath.org/ticket/8386





---

archive/issue_comments_075008.json:
```json
{
    "body": "Attachment [trac_8386_iet_alphabet_bug.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_iet_alphabet_bug.patch) by vdelecroix created at 2010-02-27 13:09:22",
    "created_at": "2010-02-27T13:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75008",
    "user": "vdelecroix"
}
```

Attachment [trac_8386_iet_alphabet_bug.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_iet_alphabet_bug.patch) by vdelecroix created at 2010-02-27 13:09:22



---

archive/issue_comments_075009.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-27T22:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75009",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075010.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2010-02-27T22:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75010",
    "user": "vdelecroix"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_075011.json:
```json
{
    "body": "This patch really needs to be rebased (14 hunk failures) `:-)`",
    "created_at": "2011-10-02T10:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75011",
    "user": "ncohen"
}
```

This patch really needs to be rebased (14 hunk failures) `:-)`



---

archive/issue_comments_075012.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-02T10:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75012",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075013.json:
```json
{
    "body": "Changing keywords from \"iet combinatoric\" to \"iet, combinatorics\".",
    "created_at": "2012-03-09T02:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75013",
    "user": "vdelecroix"
}
```

Changing keywords from "iet combinatoric" to "iet, combinatorics".



---

archive/issue_comments_075014.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-09T03:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75014",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075015.json:
```json
{
    "body": "A bunch of doctests are failing with this patch (see patchbot logs)",
    "created_at": "2012-03-12T17:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75015",
    "user": "davidloeffler"
}
```

A bunch of doctests are failing with this patch (see patchbot logs)



---

archive/issue_comments_075016.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-12T17:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75016",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075017.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-13T14:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75017",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075018.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-04-06T10:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75018",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075019.json:
```json
{
    "body": "This seems to work with 4.8 but two doctests consistently fail with recent 5.0 betas:\n\n```\n**********************************************************************\nFile \"/storage/masiao/sage-5.0.beta12-patchbot/devel/sage-8386/sage/dynamics/flat_surfaces/abelian_strata.py\", line 1348:\n    sage: c1 != c2_hyp\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[13]>\", line 1, in <module>\n        c1 != c2_hyp###line 1348:\n    sage: c1 != c2_hyp\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/lib/python/site-packages/sage/dynamics/flat_surfaces/abelian_strata.py\", line 1364, in __cmp__\n        return type.__cmp__(type(self),type(other))\n    AttributeError: type object 'type' has no attribute '__cmp__'\n**********************************************************************\nFile \"/storage/masiao/sage-5.0.beta12-patchbot/devel/sage-8386/sage/dynamics/flat_surfaces/abelian_strata.py\", line 1350:\n    sage: c2_hyp != c2_odd\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[14]>\", line 1, in <module>\n        c2_hyp != c2_odd###line 1350:\n    sage: c2_hyp != c2_odd\n      File \"/storage/masiao/sage-5.0.beta12-patchbot/local/lib/python/site-packages/sage/dynamics/flat_surfaces/abelian_strata.py\", line 1364, in __cmp__\n        return type.__cmp__(type(self),type(other))\n    AttributeError: type object 'type' has no attribute '__cmp__'\n**********************************************************************\n```\n",
    "created_at": "2012-04-06T10:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75019",
    "user": "davidloeffler"
}
```

This seems to work with 4.8 but two doctests consistently fail with recent 5.0 betas:

```
**********************************************************************
File "/storage/masiao/sage-5.0.beta12-patchbot/devel/sage-8386/sage/dynamics/flat_surfaces/abelian_strata.py", line 1348:
    sage: c1 != c2_hyp
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[13]>", line 1, in <module>
        c1 != c2_hyp###line 1348:
    sage: c1 != c2_hyp
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/lib/python/site-packages/sage/dynamics/flat_surfaces/abelian_strata.py", line 1364, in __cmp__
        return type.__cmp__(type(self),type(other))
    AttributeError: type object 'type' has no attribute '__cmp__'
**********************************************************************
File "/storage/masiao/sage-5.0.beta12-patchbot/devel/sage-8386/sage/dynamics/flat_surfaces/abelian_strata.py", line 1350:
    sage: c2_hyp != c2_odd
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[14]>", line 1, in <module>
        c2_hyp != c2_odd###line 1350:
    sage: c2_hyp != c2_odd
      File "/storage/masiao/sage-5.0.beta12-patchbot/local/lib/python/site-packages/sage/dynamics/flat_surfaces/abelian_strata.py", line 1364, in __cmp__
        return type.__cmp__(type(self),type(other))
    AttributeError: type object 'type' has no attribute '__cmp__'
**********************************************************************
```




---

archive/issue_comments_075020.json:
```json
{
    "body": "Attachment [trac_8386-enhanced_iet.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386-enhanced_iet.patch) by vdelecroix created at 2012-04-29 19:28:35\n\napply only this one",
    "created_at": "2012-04-29T19:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75020",
    "user": "vdelecroix"
}
```

Attachment [trac_8386-enhanced_iet.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386-enhanced_iet.patch) by vdelecroix created at 2012-04-29 19:28:35

apply only this one



---

archive/issue_comments_075021.json:
```json
{
    "body": "I modify one line in the __cmp__ method of AbelianStratumComponent in order to make it works.\n\nI suspect an upgrade version of python between sage-4.8 and sage-5.0 as I used the method __cmp__ of 'type' which no longer exists.",
    "created_at": "2012-04-29T19:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75021",
    "user": "vdelecroix"
}
```

I modify one line in the __cmp__ method of AbelianStratumComponent in order to make it works.

I suspect an upgrade version of python between sage-4.8 and sage-5.0 as I used the method __cmp__ of 'type' which no longer exists.



---

archive/issue_comments_075022.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-29T19:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75022",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075023.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75023",
    "user": "jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_075024.json:
```json
{
    "body": "Apply only trac_8386-enhanced_iet.v2.patch",
    "created_at": "2012-08-29T19:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75024",
    "user": "chapoton"
}
```

Apply only trac_8386-enhanced_iet.v2.patch



---

archive/issue_comments_075025.json:
```json
{
    "body": "The bot is not happy: one doctest is missing in dynamics/interval_exchanges/constructors.py\n\nI also complains about the startup, but I do no know what to do about that..",
    "created_at": "2012-09-26T13:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75025",
    "user": "chapoton"
}
```

The bot is not happy: one doctest is missing in dynamics/interval_exchanges/constructors.py

I also complains about the startup, but I do no know what to do about that..



---

archive/issue_comments_075026.json:
```json
{
    "body": "I have added the missing doc.\n\nWhat about the startup problem ?",
    "created_at": "2012-09-27T18:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75026",
    "user": "chapoton"
}
```

I have added the missing doc.

What about the startup problem ?



---

archive/issue_comments_075027.json:
```json
{
    "body": "Apply only trac_8386-enhanced_iet.v2.patch",
    "created_at": "2012-09-28T08:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75027",
    "user": "chapoton"
}
```

Apply only trac_8386-enhanced_iet.v2.patch



---

archive/issue_comments_075028.json:
```json
{
    "body": "Apply only trac_8386-enhanced_iet.v2.patch\n\nHere is a tentative of lazy_import. Let us see what the bot think of that one.",
    "created_at": "2012-11-15T19:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75028",
    "user": "chapoton"
}
```

Apply only trac_8386-enhanced_iet.v2.patch

Here is a tentative of lazy_import. Let us see what the bot think of that one.



---

archive/issue_comments_075029.json:
```json
{
    "body": "Attachment [trac_8386-enhanced_iet.v2.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386-enhanced_iet.v2.patch) by chapoton created at 2012-11-15 20:13:25\n\nApply only trac_8386-enhanced_iet.v2.patch\n\nanother try, even more lazy !",
    "created_at": "2012-11-15T20:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75029",
    "user": "chapoton"
}
```

Attachment [trac_8386-enhanced_iet.v2.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386-enhanced_iet.v2.patch) by chapoton created at 2012-11-15 20:13:25

Apply only trac_8386-enhanced_iet.v2.patch

another try, even more lazy !



---

archive/issue_comments_075030.json:
```json
{
    "body": "Attachment [trac_8386-enhanced_iet.v3.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386-enhanced_iet.v3.patch) by chapoton created at 2012-12-11 20:15:51",
    "created_at": "2012-12-11T20:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75030",
    "user": "chapoton"
}
```

Attachment [trac_8386-enhanced_iet.v3.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386-enhanced_iet.v3.patch) by chapoton created at 2012-12-11 20:15:51



---

archive/issue_comments_075031.json:
```json
{
    "body": "I have rebased on 5.5rc0.\n\nI hope I have not made a mistake in doing that\n\nApply trac_8386-enhanced_iet.v3.patch",
    "created_at": "2012-12-11T20:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75031",
    "user": "chapoton"
}
```

I have rebased on 5.5rc0.

I hope I have not made a mistake in doing that

Apply trac_8386-enhanced_iet.v3.patch



---

archive/issue_comments_075032.json:
```json
{
    "body": "Let me try to do something for this ticket.\n\nHere is a new patch, that **only** moves the files from \"combinat/iet\" to a new folder \"dynamics\".\n\nThis has been done by starting with the code in 5.10.beta3. So there is something lost, which is the refactoring of datatype.\n\nBut it pass all tests.",
    "created_at": "2013-05-19T13:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75032",
    "user": "chapoton"
}
```

Let me try to do something for this ticket.

Here is a new patch, that **only** moves the files from "combinat/iet" to a new folder "dynamics".

This has been done by starting with the code in 5.10.beta3. So there is something lost, which is the refactoring of datatype.

But it pass all tests.



---

archive/issue_comments_075033.json:
```json
{
    "body": "for the bot:\n\napply trac_8386_just_moving-fc.patch",
    "created_at": "2013-05-19T13:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75033",
    "user": "chapoton"
}
```

for the bot:

apply trac_8386_just_moving-fc.patch



---

archive/issue_comments_075034.json:
```json
{
    "body": "If you move files, use `hg mv` for that instead of `hg remove` the old and `hg add` the new file.",
    "created_at": "2013-05-19T13:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75034",
    "user": "jdemeyer"
}
```

If you move files, use `hg mv` for that instead of `hg remove` the old and `hg add` the new file.



---

archive/issue_comments_075035.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-05-19T13:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75035",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075036.json:
```json
{
    "body": "I am happy for this ticket if it simply moves iet to sage.dynamics (and keep the refactoring for another ticket) ! But as jdemeyer mentioned it should be done with hg mv (which is a one line patch) instead of hg remove/hg add (which is a 2x(length of the file) patch long).\n\nvincent",
    "created_at": "2013-05-19T14:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75036",
    "user": "vdelecroix"
}
```

I am happy for this ticket if it simply moves iet to sage.dynamics (and keep the refactoring for another ticket) ! But as jdemeyer mentioned it should be done with hg mv (which is a one line patch) instead of hg remove/hg add (which is a 2x(length of the file) patch long).

vincent



---

archive/issue_comments_075037.json:
```json
{
    "body": "Well, I did not now about hg mv.\n\nI have done a lot of work to make the re-location function, including some work on the toc-trees that was rather painful.\n\nAnd I has also taken the opportunity to \n- put all the raise syntax into python3 form\n- correct orthographic errors\n- make the code much closer to pep8 level\n- removed unused import statements\n- make the desired separation into interval_exchanges and flat_surfaces\n\nI spent a few **hours** today on that, and I have already spent a lot of time on this ticket some **months** ago, but nobody did react at that time.\n\nSo, given that all tests pass **now**, it would be great if my work is not lost again.",
    "created_at": "2013-05-19T16:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75037",
    "user": "chapoton"
}
```

Well, I did not now about hg mv.

I have done a lot of work to make the re-location function, including some work on the toc-trees that was rather painful.

And I has also taken the opportunity to 
- put all the raise syntax into python3 form
- correct orthographic errors
- make the code much closer to pep8 level
- removed unused import statements
- make the desired separation into interval_exchanges and flat_surfaces

I spent a few **hours** today on that, and I have already spent a lot of time on this ticket some **months** ago, but nobody did react at that time.

So, given that all tests pass **now**, it would be great if my work is not lost again.



---

archive/issue_comments_075038.json:
```json
{
    "body": "Replying to [comment:25 chapoton]:\n> Well, I did not now about hg mv.\n> \n> I have done a lot of work to make the re-location function, including some work on the toc-trees that was rather painful.\n> \n> And I has also taken the opportunity to \n> - put all the raise syntax into python3 form\n> - correct orthographic errors\n> - make the code much closer to pep8 level\n> - removed unused import statements\n> - make the desired separation into interval_exchanges and flat_surfaces\n> \n> I spent a few **hours** today on that, and I have already spent a lot of time on this ticket some **months** ago, but nobody did react at that time.\n> \n> So, given that all tests pass **now**, it would be great if my work is not lost again.\n\nI will have a closer look **right now** at your patch. Nevertheless patchbot complains (blue color instead of green) because the doctest framework now wants \"....:\" instead of \"...\" in multiline doctests.",
    "created_at": "2013-05-19T17:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75038",
    "user": "vdelecroix"
}
```

Replying to [comment:25 chapoton]:
> Well, I did not now about hg mv.
> 
> I have done a lot of work to make the re-location function, including some work on the toc-trees that was rather painful.
> 
> And I has also taken the opportunity to 
> - put all the raise syntax into python3 form
> - correct orthographic errors
> - make the code much closer to pep8 level
> - removed unused import statements
> - make the desired separation into interval_exchanges and flat_surfaces
> 
> I spent a few **hours** today on that, and I have already spent a lot of time on this ticket some **months** ago, but nobody did react at that time.
> 
> So, given that all tests pass **now**, it would be great if my work is not lost again.

I will have a closer look **right now** at your patch. Nevertheless patchbot complains (blue color instead of green) because the doctest framework now wants "....:" instead of "..." in multiline doctests.



---

archive/issue_comments_075039.json:
```json
{
    "body": "Attachment [trac_8386_just_moving-fc.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_just_moving-fc.patch) by chapoton created at 2013-05-19 17:57:08\n\nfor the bot: apply trac_8386_just_moving-fc.patch\n\nhere is a patch that should correct the `....:` point\n\nlet us see what the patchbot says",
    "created_at": "2013-05-19T17:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75039",
    "user": "chapoton"
}
```

Attachment [trac_8386_just_moving-fc.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_just_moving-fc.patch) by chapoton created at 2013-05-19 17:57:08

for the bot: apply trac_8386_just_moving-fc.patch

here is a patch that should correct the `....:` point

let us see what the patchbot says



---

archive/issue_comments_075040.json:
```json
{
    "body": "Replying to [comment:25 chapoton]:\n> Well, I did not now about hg mv.\n> ...\n> So, given that all tests pass **now**, it would be great if my work is not lost again.\n\nYou can quickly recreate your patch using `hg mv` as follow:\n\n- With your patch applied, backup the files that have been moved/modified\n- Unapply the patch\n- Replay the moving the files using `hg mv`\n- Reinstate the backed-up files on top of it.\n- hg qnew a new patch with those, and discard the other one.\n\nYou might want to actually do two patches, one with just the moving,\nand the other with the changes.\n\nBtw: thanks Fr\u00e9d\u00e9ric for all the hard work you are doing lately\n(cleaning, reviewing and more ...)!\n\nCheers,\n                                 Nicolas",
    "created_at": "2013-05-19T18:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75040",
    "user": "nthiery"
}
```

Replying to [comment:25 chapoton]:
> Well, I did not now about hg mv.
> ...
> So, given that all tests pass **now**, it would be great if my work is not lost again.

You can quickly recreate your patch using `hg mv` as follow:

- With your patch applied, backup the files that have been moved/modified
- Unapply the patch
- Replay the moving the files using `hg mv`
- Reinstate the backed-up files on top of it.
- hg qnew a new patch with those, and discard the other one.

You might want to actually do two patches, one with just the moving,
and the other with the changes.

Btw: thanks Frédéric for all the hard work you are doing lately
(cleaning, reviewing and more ...)!

Cheers,
                                 Nicolas



---

archive/issue_comments_075041.json:
```json
{
    "body": "Thanks Nicolas for this good advice. I am doing that, and I will upload 2 patches",
    "created_at": "2013-05-19T19:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75041",
    "user": "chapoton"
}
```

Thanks Nicolas for this good advice. I am doing that, and I will upload 2 patches



---

archive/issue_comments_075042.json:
```json
{
    "body": "There is even an option\n\n```\nhg mv --after\n```\n\nwhich allows one to mark the move after it has happened. But it doesn't work well with queues, as a patch which has been `qrefresh`ed is considered committed. So you need a non-committed version of the patch: apply the patch \"by hand\" using `patch -p1 <x.patch`, then `hg mv --after`, then `hg commit` should work (but I haven't really tried).",
    "created_at": "2013-05-19T19:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75042",
    "user": "jdemeyer"
}
```

There is even an option

```
hg mv --after
```

which allows one to mark the move after it has happened. But it doesn't work well with queues, as a patch which has been `qrefresh`ed is considered committed. So you need a non-committed version of the patch: apply the patch "by hand" using `patch -p1 <x.patch`, then `hg mv --after`, then `hg commit` should work (but I haven't really tried).



---

archive/issue_comments_075043.json:
```json
{
    "body": "Attachment [trac_8386_really_just_moving-fc.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_really_just_moving-fc.patch) by chapoton created at 2013-05-19 20:01:31\n\nok, here it is. It seems that my doc framework is now completely broken (I have by mistake removed the output directory and now docbuild complains a lot about intersphinx and missing files), so I do not know if the doc is ok.\n\nfor the bot:\n\napply trac_8386_really_just_moving-fc.patch trac_8386_big_clean_fc.patch",
    "created_at": "2013-05-19T20:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75043",
    "user": "chapoton"
}
```

Attachment [trac_8386_really_just_moving-fc.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_really_just_moving-fc.patch) by chapoton created at 2013-05-19 20:01:31

ok, here it is. It seems that my doc framework is now completely broken (I have by mistake removed the output directory and now docbuild complains a lot about intersphinx and missing files), so I do not know if the doc is ok.

for the bot:

apply trac_8386_really_just_moving-fc.patch trac_8386_big_clean_fc.patch



---

archive/issue_comments_075044.json:
```json
{
    "body": "Replying to [comment:31 chapoton]:\n> ok, here it is. It seems that my doc framework is now completely broken (I have by mistake removed the output directory and now docbuild complains a lot about intersphinx and missing files), so I do not know if the doc is ok.\n\nIt also happens for me. After removing the directory doc/output it works fine again (but you need to rebuild everything with \"sage -docbuild all html\"). If there is a less extremal solution then I would be happy to know.\n\napply trac_8386_really_just_moving-fc.patch trac_8386_big_clean_fc.patch",
    "created_at": "2013-05-19T20:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75044",
    "user": "vdelecroix"
}
```

Replying to [comment:31 chapoton]:
> ok, here it is. It seems that my doc framework is now completely broken (I have by mistake removed the output directory and now docbuild complains a lot about intersphinx and missing files), so I do not know if the doc is ok.

It also happens for me. After removing the directory doc/output it works fine again (but you need to rebuild everything with "sage -docbuild all html"). If there is a less extremal solution then I would be happy to know.

apply trac_8386_really_just_moving-fc.patch trac_8386_big_clean_fc.patch



---

archive/issue_comments_075045.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-05-24T11:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75045",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075046.json:
```json
{
    "body": "Thanks Frederic.\n\nI put you as an author and me as a reviewer as it is more like that now. I postponed the modification of the implementation to #14683.",
    "created_at": "2013-06-03T20:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75046",
    "user": "vdelecroix"
}
```

Thanks Frederic.

I put you as an author and me as a reviewer as it is more like that now. I postponed the modification of the implementation to #14683.



---

archive/issue_comments_075047.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-03T20:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75047",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075048.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-06-04T06:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75048",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_075049.json:
```json
{
    "body": "Needs to be rebased to #14669.",
    "created_at": "2013-06-04T06:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75049",
    "user": "jdemeyer"
}
```

Needs to be rebased to #14669.



---

archive/issue_comments_075050.json:
```json
{
    "body": "Attachment [trac_8386_big_clean_fc.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_big_clean_fc.patch) by chapoton created at 2013-06-13 18:11:11",
    "created_at": "2013-06-13T18:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75050",
    "user": "chapoton"
}
```

Attachment [trac_8386_big_clean_fc.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_big_clean_fc.patch) by chapoton created at 2013-06-13 18:11:11



---

archive/issue_comments_075051.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-13T18:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75051",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075052.json:
```json
{
    "body": "rebased on top of #14669",
    "created_at": "2013-06-13T18:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75052",
    "user": "chapoton"
}
```

rebased on top of #14669



---

archive/issue_comments_075053.json:
```json
{
    "body": "Great !",
    "created_at": "2013-06-18T14:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75053",
    "user": "vdelecroix"
}
```

Great !



---

archive/issue_comments_075054.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-18T14:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75054",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075055.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-06-18T17:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75055",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_075056.json:
```json
{
    "body": "Never use `assert` to check user input, use `raise TypeError()` or other exceptions for that.\nAn `AssertionError` appearing in a public function is by definition a bug.\n\nExample:\n\n```\nsage: QuadraticStratum(\"foo\")\n---------------------------------------------------------------------------\nAssertionError                            Traceback (most recent call last)\n<ipython-input-2-ba2d4d1c0bfc> in <module>()\n----> 1 QuadraticStratum(\"foo\")\n\n/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)()\n\n/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)()\n\n/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/dynamics/flat_surfaces/quadratic_strata.pyc in __init__(self, *l)\n     30         else:\n     31             for i in l:\n---> 32                 assert(isinstance(i, (int, Integer)))\n     33             self._zeroes = sorted(list(l), reverse=True)\n     34 \n\nAssertionError: \n```\n",
    "created_at": "2013-06-18T17:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75056",
    "user": "jdemeyer"
}
```

Never use `assert` to check user input, use `raise TypeError()` or other exceptions for that.
An `AssertionError` appearing in a public function is by definition a bug.

Example:

```
sage: QuadraticStratum("foo")
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-ba2d4d1c0bfc> in <module>()
----> 1 QuadraticStratum("foo")

/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)()

/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/misc/lazy_import.so in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)()

/mazur/release/merger/sage-5.10/local/lib/python2.7/site-packages/sage/dynamics/flat_surfaces/quadratic_strata.pyc in __init__(self, *l)
     30         else:
     31             for i in l:
---> 32                 assert(isinstance(i, (int, Integer)))
     33             self._zeroes = sorted(list(l), reverse=True)
     34 

AssertionError: 
```




---

archive/issue_comments_075057.json:
```json
{
    "body": "Attachment [trac_8386_assert_removal.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_assert_removal.patch) by chapoton created at 2013-06-18 19:49:31",
    "created_at": "2013-06-18T19:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75057",
    "user": "chapoton"
}
```

Attachment [trac_8386_assert_removal.patch](tarball://root/attachments/some-uuid/ticket8386/trac_8386_assert_removal.patch) by chapoton created at 2013-06-18 19:49:31



---

archive/issue_comments_075058.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-18T19:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75058",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075059.json:
```json
{
    "body": "here is patch that\n\n* removes all \"assert\" statements, using some \"raise xxxError()\" instead\n\n* makes an effort to doctest more of the \"raise xxxError()\"\n\nThere remains to make sure all \"raise\" are doctested, but I would prefer to keep that for another ticket, given the age of this one.\n\nNeeds review",
    "created_at": "2013-06-18T19:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75059",
    "user": "chapoton"
}
```

here is patch that

* removes all "assert" statements, using some "raise xxxError()" instead

* makes an effort to doctest more of the "raise xxxError()"

There remains to make sure all "raise" are doctested, but I would prefer to keep that for another ticket, given the age of this one.

Needs review



---

archive/issue_comments_075060.json:
```json
{
    "body": "I haven't checked in detail (Vincent: can you do that please), but it looks good on first sight. Excellent work!",
    "created_at": "2013-06-18T20:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75060",
    "user": "jdemeyer"
}
```

I haven't checked in detail (Vincent: can you do that please), but it looks good on first sight. Excellent work!



---

archive/issue_comments_075061.json:
```json
{
    "body": "Sounds good to me too. Thanks Fr\u00e9d\u00e9ric!\n\nBtw: I noticed a __repr__; but that's probably for another ticket.",
    "created_at": "2013-06-19T05:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75061",
    "user": "nthiery"
}
```

Sounds good to me too. Thanks Frédéric!

Btw: I noticed a __repr__; but that's probably for another ticket.



---

archive/issue_comments_075062.json:
```json
{
    "body": "Vincent, are you able to do the re-review in the next few days? #14772 depends on this ticket because there are two instances in iet which use `Permutation_class`.",
    "created_at": "2013-06-28T16:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75062",
    "user": "tscrim"
}
```

Vincent, are you able to do the re-review in the next few days? #14772 depends on this ticket because there are two instances in iet which use `Permutation_class`.



---

archive/issue_comments_075063.json:
```json
{
    "body": "Good to go! Thanks Frederic.",
    "created_at": "2013-07-04T11:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75063",
    "user": "vdelecroix"
}
```

Good to go! Thanks Frederic.



---

archive/issue_comments_075064.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-04T11:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75064",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-02T14:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8386#issuecomment-75065",
    "user": "jdemeyer"
}
```

Resolution: fixed
