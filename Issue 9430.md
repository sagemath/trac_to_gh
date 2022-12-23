# Issue 9430: Update SageNB to version 0.8.1

archive/issues_009430.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  acleone was mpatel leif\n\nDownload at: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.1.spkg\n\nVersion 0.8.1 solves the following tickets:\n\n#9294, #8760, #8758, #8686, #7633, #7418, #7379\n\nPlease merge the Sage main library patch at #7379 when including this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9430\n\n",
    "created_at": "2010-07-05T11:30:03Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "Update SageNB to version 0.8.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9430",
    "user": "timdumol"
}
```
Assignee: jason, was

CC:  acleone was mpatel leif

Download at: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.1.spkg

Version 0.8.1 solves the following tickets:

#9294, #8760, #8758, #8686, #7633, #7418, #7379

Please merge the Sage main library patch at #7379 when including this.

Issue created by migration from https://trac.sagemath.org/ticket/9430





---

archive/issue_comments_090024.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-05T11:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90024",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090025.json:
```json
{
    "body": "I can yet say I get doctest errors related to this spkg (with Sage 4.5.alpha4), but the complete test will take some hours... (i.e. more to come later).",
    "created_at": "2010-07-07T13:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90025",
    "user": "leif"
}
```

I can yet say I get doctest errors related to this spkg (with Sage 4.5.alpha4), but the complete test will take some hours... (i.e. more to come later).



---

archive/issue_comments_090026.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-07T14:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90026",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090027.json:
```json
{
    "body": "Doctest error preview (`ptestlong` still running):\n\n```\nsage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\n**********************************************************************\nFile \"/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 2205:\n    sage: @interact\n    def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):\n        show(factor(x**n - Integer(1)))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/leif/sage-4.5.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/leif/sage-4.5.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/leif/sage-4.5.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_99[9]>\", line 2, in <module>\n        def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):\n      File \"/home/leif/sage-4.5.alpha4/local/lib/python/site-packages/sage/misc/misc.py\", line 2666, in my_wrap\n        return func(*args)\n      File \"/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 2519, in interact\n        html(C.render())\n      File \"/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 2058, in render\n        s = \"%s%s\"%(self.render_controls(), self.render_output())\n      File \"/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py\", line 1994, in render_controls\n        layout = [[c.var()] for c in self.__controls]\n    AttributeError: 'UpdateButton' object has no attribute 'var'\n**********************************************************************\n1 items had failures:\n   1 of  34 in __main__.example_99\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/leif/.sage//tmp/.doctest_interact.py\n\t [6.3 s]\n```\n\n(Ubuntu 9.04 x86, P4 Prescott, gcc 4.3.3, sequential build)\n\nWith vanilla Sage 4.5.**alpha3**, all doctests passed on that system (same with alpha4 on Ubuntu 9.04 x86_64, gcc 4.5.0; `ptestlong`).\n\nI've copied `sagenb-0.8.1.spkg` and `zodb3-3.7.0.p4.spkg` (#9436) to `spkg/standard`, built Sage, applied #7379 (Sage library patch for sagenb 0.8.1), run `./sage -b`, rebuilt the documentation and then started the test.\n\nI blindly guess there won't come up further errors originating from the new sagenb package.",
    "created_at": "2010-07-07T14:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90027",
    "user": "leif"
}
```

Doctest error preview (`ptestlong` still running):

```
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py
**********************************************************************
File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2205:
    sage: @interact
    def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
        show(factor(x**n - Integer(1)))
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/sage-4.5.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/sage-4.5.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_99[9]>", line 2, in <module>
        def _(n=(Integer(10),Integer(100),Integer(1)), auto_update=False):
      File "/home/leif/sage-4.5.alpha4/local/lib/python/site-packages/sage/misc/misc.py", line 2666, in my_wrap
        return func(*args)
      File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2519, in interact
        html(C.render())
      File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 2058, in render
        s = "%s%s"%(self.render_controls(), self.render_output())
      File "/home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/notebook/interact.py", line 1994, in render_controls
        layout = [[c.var()] for c in self.__controls]
    AttributeError: 'UpdateButton' object has no attribute 'var'
**********************************************************************
1 items had failures:
   1 of  34 in __main__.example_99
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_interact.py
	 [6.3 s]
```

(Ubuntu 9.04 x86, P4 Prescott, gcc 4.3.3, sequential build)

With vanilla Sage 4.5.**alpha3**, all doctests passed on that system (same with alpha4 on Ubuntu 9.04 x86_64, gcc 4.5.0; `ptestlong`).

I've copied `sagenb-0.8.1.spkg` and `zodb3-3.7.0.p4.spkg` (#9436) to `spkg/standard`, built Sage, applied #7379 (Sage library patch for sagenb 0.8.1), run `./sage -b`, rebuilt the documentation and then started the test.

I blindly guess there won't come up further errors originating from the new sagenb package.



---

archive/issue_comments_090028.json:
```json
{
    "body": "I forgot to put in the patch for that. New version now at the same url.\n\nTo test sagenb packages, all you need to do is install it via `sage -f sagenb-0.8.1.spkg` and run `sage -t -sagenb`.",
    "created_at": "2010-07-07T15:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90028",
    "user": "timdumol"
}
```

I forgot to put in the patch for that. New version now at the same url.

To test sagenb packages, all you need to do is install it via `sage -f sagenb-0.8.1.spkg` and run `sage -t -sagenb`.



---

archive/issue_comments_090029.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-07T15:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90029",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090030.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> With vanilla Sage 4.5.**alpha3**, all doctests passed on that system (same with alpha4 on Ubuntu 9.04 x86_64, gcc 4.5.0; `ptestlong`).\n\nNot *really* vanilla, actually alpha3 with #9432 (fixing a single doctest error, unrelated to this ticket, merged in alpha4) passed all tests.",
    "created_at": "2010-07-07T17:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90030",
    "user": "leif"
}
```

Replying to [comment:4 leif]:
> With vanilla Sage 4.5.**alpha3**, all doctests passed on that system (same with alpha4 on Ubuntu 9.04 x86_64, gcc 4.5.0; `ptestlong`).

Not *really* vanilla, actually alpha3 with #9432 (fixing a single doctest error, unrelated to this ticket, merged in alpha4) passed all tests.



---

archive/issue_comments_090031.json:
```json
{
    "body": "I don't know if this is sufficient, but after forcing reinstallation of Tim's corrected SageNB package, `./sage -t -sagenb` and `./sage -t -long -sagenb` (there seem to be no `long` tests) passed all tests, especially the (only) one that previously failed.\n\nSo I can give it a **positive review**, unless somebody tells me what further tests should be performed.\n\nI'll test it on Ubuntu 9.04 x86_64 tomorrow.",
    "created_at": "2010-07-07T17:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90031",
    "user": "leif"
}
```

I don't know if this is sufficient, but after forcing reinstallation of Tim's corrected SageNB package, `./sage -t -sagenb` and `./sage -t -long -sagenb` (there seem to be no `long` tests) passed all tests, especially the (only) one that previously failed.

So I can give it a **positive review**, unless somebody tells me what further tests should be performed.

I'll test it on Ubuntu 9.04 x86_64 tomorrow.



---

archive/issue_comments_090032.json:
```json
{
    "body": "Rebuilding the HTML documentation also succeeded (except for the missing `conf.py` in `thematic_tutorials`, which is unrelated).",
    "created_at": "2010-07-07T18:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90032",
    "user": "leif"
}
```

Rebuilding the HTML documentation also succeeded (except for the missing `conf.py` in `thematic_tutorials`, which is unrelated).



---

archive/issue_comments_090033.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> I'll test it on Ubuntu 9.04 x86_64 tomorrow.\n\nI've successfully built Sage 4.5.alpha4 with SageNB 0.8.1 and zodb3 3.7.0.p4 (#9436), both sequentially and in parallel (`SAGE_PARALLEL_SPKG_BUILD=\"yes\", MAKE=\"make -j4\"`).\n\nNo downloads during install, HTML documentation builds (except missing `conf.py` in `thematic_tutorials`), and all long tests passed (`make ptestlong`).\n\nAll builds/tests performed independently, i.e. from scratch.\n\nLeaving as \"needs review\" since IMHO tests by others on other platforms should follow.",
    "created_at": "2010-07-08T16:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90033",
    "user": "leif"
}
```

Replying to [comment:7 leif]:
> I'll test it on Ubuntu 9.04 x86_64 tomorrow.

I've successfully built Sage 4.5.alpha4 with SageNB 0.8.1 and zodb3 3.7.0.p4 (#9436), both sequentially and in parallel (`SAGE_PARALLEL_SPKG_BUILD="yes", MAKE="make -j4"`).

No downloads during install, HTML documentation builds (except missing `conf.py` in `thematic_tutorials`), and all long tests passed (`make ptestlong`).

All builds/tests performed independently, i.e. from scratch.

Leaving as "needs review" since IMHO tests by others on other platforms should follow.



---

archive/issue_comments_090034.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-08T19:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90034",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090035.json:
```json
{
    "body": "Moving to positive review. I'm about to release rc0, so this will get plenty of testing on all platforms.",
    "created_at": "2010-07-08T19:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90035",
    "user": "rlm"
}
```

Moving to positive review. I'm about to release rc0, so this will get plenty of testing on all platforms.



---

archive/issue_comments_090036.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-08T19:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9430#issuecomment-90036",
    "user": "rlm"
}
```

Resolution: fixed
