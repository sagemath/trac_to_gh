# Issue 5454: [with patch, needs review] Add coercion documentation to the reference manual

archive/issues_005454.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @robertwb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5454\n\n",
    "created_at": "2009-03-07T19:18:38Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, needs review] Add coercion documentation to the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5454",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tba

CC:  @robertwb



Issue created by migration from https://trac.sagemath.org/ticket/5454





---

archive/issue_comments_042179.json:
```json
{
    "body": "Attachment [trac_5454.patch](tarball://root/attachments/some-uuid/ticket5454/trac_5454.patch) by @mwhansen created at 2009-03-07 19:20:04",
    "created_at": "2009-03-07T19:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42179",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5454.patch](tarball://root/attachments/some-uuid/ticket5454/trac_5454.patch) by @mwhansen created at 2009-03-07 19:20:04



---

archive/issue_comments_042180.json:
```json
{
    "body": "sage/structure/coerce* should probably still be in the reference manual.",
    "created_at": "2009-03-07T22:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42180",
    "user": "https://github.com/robertwb"
}
```

sage/structure/coerce* should probably still be in the reference manual.



---

archive/issue_comments_042181.json:
```json
{
    "body": "They are under the coercion section at the bottom.",
    "created_at": "2009-03-07T22:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42181",
    "user": "https://github.com/mwhansen"
}
```

They are under the coercion section at the bottom.



---

archive/issue_comments_042182.json:
```json
{
    "body": "/me should read the patch more carefully. I haven't applied it, but it looks good. \n\nJust as an aside, based on some conversations with people, I'm thinking about getting rid of _l_action_ and _r_action_ (replacing with _act_on_ and _acted_upon_). Thoughts?",
    "created_at": "2009-03-07T22:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42182",
    "user": "https://github.com/robertwb"
}
```

/me should read the patch more carefully. I haven't applied it, but it looks good. 

Just as an aside, based on some conversations with people, I'm thinking about getting rid of _l_action_ and _r_action_ (replacing with _act_on_ and _acted_upon_). Thoughts?



---

archive/issue_comments_042183.json:
```json
{
    "body": "Something other than _l_action_ and _r_action_!  I don't know if _act_on_ and _acted_upon_ are better though.  In every case I've ever used it, I'm always defining how things act on my element from the left or the right (modules) in which case _l_action_ and _r_action_ are reversed.",
    "created_at": "2009-03-07T22:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42183",
    "user": "https://github.com/mwhansen"
}
```

Something other than _l_action_ and _r_action_!  I don't know if _act_on_ and _acted_upon_ are better though.  In every case I've ever used it, I'm always defining how things act on my element from the left or the right (modules) in which case _l_action_ and _r_action_ are reversed.



---

archive/issue_comments_042184.json:
```json
{
    "body": "_act_on_ would be self acting on something, _acted_upon_ would be something acting on self. They would both take a self_on_left argument. I'm open for other names, but haven't come up with any yet. \n\nBTW, thanks for rebasing those other patches.",
    "created_at": "2009-03-07T22:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42184",
    "user": "https://github.com/robertwb"
}
```

_act_on_ would be self acting on something, _acted_upon_ would be something acting on self. They would both take a self_on_left argument. I'm open for other names, but haven't come up with any yet. 

BTW, thanks for rebasing those other patches.



---

archive/issue_comments_042185.json:
```json
{
    "body": "That convention sounds good to me, but we would then have to tell people to only implement one of them.",
    "created_at": "2009-03-07T22:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42185",
    "user": "https://github.com/mwhansen"
}
```

That convention sounds good to me, but we would then have to tell people to only implement one of them.



---

archive/issue_comments_042186.json:
```json
{
    "body": "BTW, the only reason I haven't given this a positive review is because of the potential renaming of _l_action_.",
    "created_at": "2009-03-12T02:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42186",
    "user": "https://github.com/robertwb"
}
```

BTW, the only reason I haven't given this a positive review is because of the potential renaming of _l_action_.



---

archive/issue_comments_042187.json:
```json
{
    "body": "rebased to 4.0.1",
    "created_at": "2009-06-10T10:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42187",
    "user": "https://github.com/loefflerd"
}
```

rebased to 4.0.1



---

archive/issue_comments_042188.json:
```json
{
    "body": "Attachment [trac_5454_rebase.patch](tarball://root/attachments/some-uuid/ticket5454/trac_5454_rebase.patch) by @loefflerd created at 2009-06-10 10:31:20\n\nIt looks like the proposed renaming of _l_action_ etc hasn't yet happened, and we *seriously need* some documentation for the coercion model -- I've written or contributed to dozens of sage parent/element classes and I never knew half of this stuff, I learnt loads just from a five-minute skim-read of the new docs. We must get this into a release ASAP.\n\nIt's a great shame that this patch has been in limbo for three months just because our hackish use of text search for \"positive review\" in the summary field missed it due to a typo.",
    "created_at": "2009-06-10T10:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42188",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5454_rebase.patch](tarball://root/attachments/some-uuid/ticket5454/trac_5454_rebase.patch) by @loefflerd created at 2009-06-10 10:31:20

It looks like the proposed renaming of _l_action_ etc hasn't yet happened, and we *seriously need* some documentation for the coercion model -- I've written or contributed to dozens of sage parent/element classes and I never knew half of this stuff, I learnt loads just from a five-minute skim-read of the new docs. We must get this into a release ASAP.

It's a great shame that this patch has been in limbo for three months just because our hackish use of text search for "positive review" in the summary field missed it due to a typo.



---

archive/issue_comments_042189.json:
```json
{
    "body": "Yes, it is a shame. I got busy with other stuff, like working on my thesis... Here's the renaming patch #5597. The categories patch is holding up lots of good examples.",
    "created_at": "2009-06-10T16:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42189",
    "user": "https://github.com/robertwb"
}
```

Yes, it is a shame. I got busy with other stuff, like working on my thesis... Here's the renaming patch #5597. The categories patch is holding up lots of good examples.



---

archive/issue_comments_042190.json:
```json
{
    "body": "Unfortunately:\n\n\n```\nsage -t -long devel/sage/doc/en/reference/coercion.rst\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst\", line 206:\n    age: cm = sage.structure.element.get_coercion_model()\nExpected:\n    <sage.structure.coerce.CoercionModel_cache_maps object at 0x2f65960>\nGot nothing\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst\", line 235:\n    age: cm.bin_op(77, 9, gcd)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[2]>\", line 1, in <module>\n        cm.bin_op(Integer(77), Integer(9), gcd)###line 235:\n    age: cm.bin_op(77, 9, gcd)\n    NameError: name 'cm' is not defined\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst\", line 244:\n    age: cm.explain(ZZ['x'], ZZ, operator.mul)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[2]>\", line 1, in <module>\n        cm.explain(ZZ['x'], ZZ, operator.mul)###line 244:\n    age: cm.explain(ZZ['x'], ZZ, operator.mul)\n    NameError: name 'cm' is not defined\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst\", line 250:\n    age: cm.explain(ZZ['x'], ZZ, operator.div)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        cm.explain(ZZ['x'], ZZ, operator.div)###line 250:\n    age: cm.explain(ZZ['x'], ZZ, operator.div)\n    NameError: name 'cm' is not defined\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst\", line 631:\n    age: sage.categories.pushout.pushout(Frac(ZZ['x,y,z']), QQ['z, t'])\nExpected:\n    Fraction Field of Multivariate Polynomial Ring in x, y, z, t over Rational Field\nGot:\n    Univariate Polynomial Ring in t over Fraction Field of Multivariate Polynomial Ring in x, y, z over Rational Field\n**********************************************************************\n4 items had failures:\n   1 of   6 in __main__.example_2\n   1 of   3 in __main__.example_3\n   2 of  11 in __main__.example_4\n   1 of   3 in __main__.example_6\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /scratch/ncalexan/sage-4.0.2.alpha1/tmp/.doctest_coercion.py\n         [1.2 s]\n \n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t -long devel/sage/doc/en/reference/coercion.rst # 5 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1.5 seconds\nTests failed!\n```\n",
    "created_at": "2009-06-13T20:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42190",
    "user": "https://github.com/ncalexan"
}
```

Unfortunately:


```
sage -t -long devel/sage/doc/en/reference/coercion.rst
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 206:
    age: cm = sage.structure.element.get_coercion_model()
Expected:
    <sage.structure.coerce.CoercionModel_cache_maps object at 0x2f65960>
Got nothing
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 235:
    age: cm.bin_op(77, 9, gcd)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        cm.bin_op(Integer(77), Integer(9), gcd)###line 235:
    age: cm.bin_op(77, 9, gcd)
    NameError: name 'cm' is not defined
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 244:
    age: cm.explain(ZZ['x'], ZZ, operator.mul)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[2]>", line 1, in <module>
        cm.explain(ZZ['x'], ZZ, operator.mul)###line 244:
    age: cm.explain(ZZ['x'], ZZ, operator.mul)
    NameError: name 'cm' is not defined
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 250:
    age: cm.explain(ZZ['x'], ZZ, operator.div)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        cm.explain(ZZ['x'], ZZ, operator.div)###line 250:
    age: cm.explain(ZZ['x'], ZZ, operator.div)
    NameError: name 'cm' is not defined
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 631:
    age: sage.categories.pushout.pushout(Frac(ZZ['x,y,z']), QQ['z, t'])
Expected:
    Fraction Field of Multivariate Polynomial Ring in x, y, z, t over Rational Field
Got:
    Univariate Polynomial Ring in t over Fraction Field of Multivariate Polynomial Ring in x, y, z over Rational Field
**********************************************************************
4 items had failures:
   1 of   6 in __main__.example_2
   1 of   3 in __main__.example_3
   2 of  11 in __main__.example_4
   1 of   3 in __main__.example_6
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/ncalexan/sage-4.0.2.alpha1/tmp/.doctest_coercion.py
         [1.2 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/doc/en/reference/coercion.rst # 5 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1.5 seconds
Tests failed!
```




---

archive/issue_comments_042191.json:
```json
{
    "body": "apply over trac_5454_rebase.patch",
    "created_at": "2009-06-14T10:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42191",
    "user": "https://github.com/loefflerd"
}
```

apply over trac_5454_rebase.patch



---

archive/issue_comments_042192.json:
```json
{
    "body": "Attachment [trac_5454_fix.patch](tarball://root/attachments/some-uuid/ticket5454/trac_5454_fix.patch) by @loefflerd created at 2009-06-14 10:47:47\n\nI've fixed the above problems, which were all due to trivial typos/thinkos in the doctests. Silly of me not to have run the tests when I was reviewing. Can I just reinstate the positive review, or do we need a second opinion?",
    "created_at": "2009-06-14T10:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42192",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5454_fix.patch](tarball://root/attachments/some-uuid/ticket5454/trac_5454_fix.patch) by @loefflerd created at 2009-06-14 10:47:47

I've fixed the above problems, which were all due to trivial typos/thinkos in the doctests. Silly of me not to have run the tests when I was reviewing. Can I just reinstate the positive review, or do we need a second opinion?



---

archive/issue_comments_042193.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T21:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5454#issuecomment-42193",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_005708.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-14T21:30:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5454",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5454#event-5708"
}
```
