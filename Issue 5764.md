# Issue 5764: [with patch, needs review] improve doctest coverage for sageinspect.py

archive/issues_005764.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nAs the summary says...\n\nUnfortunately, running 'sage -coverage' on this file doesn't yield 100% because it gets confused by, for example, a string containing 'def test1' -- it thinks this is a function without a doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5764\n\n",
    "created_at": "2009-04-11T22:23:22Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] improve doctest coverage for sageinspect.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5764",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

As the summary says...

Unfortunately, running 'sage -coverage' on this file doesn't yield 100% because it gets confused by, for example, a string containing 'def test1' -- it thinks this is a function without a doctest.

Issue created by migration from https://trac.sagemath.org/ticket/5764





---

archive/issue_comments_044968.json:
```json
{
    "body": "Attachment [sageinspect-doctest.patch](tarball://root/attachments/some-uuid/ticket5764/sageinspect-doctest.patch) by @williamstein created at 2009-04-12 05:35:51\n\nI thought this already got dealt with.  Anyways, right now doctests fail on the sagedoc.py file (and no others).\n\n```\nsage -t  devel/sage/sage/misc/sagedoc.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/misc/sagedoc.py\", line 366:\n    sage: format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[2]>\", line 1, in <module>\n        format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')###line 366:\n    sage: format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')\n    NameError: name 'format_search_as_html' is not defined\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/misc/sagedoc.py\", line 368:\n    sage: format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class=\"math\">c</span>, then', 'antipode antihomomorphism')\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[3]>\", line 1, in <module>\n        format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class=\"math\">c</span>, then', 'antipode antihomomorphism')###line 368:\n    sage: format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class=\"math\">c</span>, then', 'antipode antihomomorphism')\n    NameError: name 'format_search_as_html' is not defined\nhtml/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)\n\n**********************************************************************\n1 items had failures:\n   2 of   4 in __main__.example_7\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_sagedoc.py\n         [24.9 s]\nsage -t  devel/sage/sage/rings/tests.py\n```\n",
    "created_at": "2009-04-12T05:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5764#issuecomment-44968",
    "user": "https://github.com/williamstein"
}
```

Attachment [sageinspect-doctest.patch](tarball://root/attachments/some-uuid/ticket5764/sageinspect-doctest.patch) by @williamstein created at 2009-04-12 05:35:51

I thought this already got dealt with.  Anyways, right now doctests fail on the sagedoc.py file (and no others).

```
sage -t  devel/sage/sage/misc/sagedoc.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/misc/sagedoc.py", line 366:
    sage: format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[2]>", line 1, in <module>
        format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')###line 366:
    sage: format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')
    NameError: name 'format_search_as_html' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/misc/sagedoc.py", line 368:
    sage: format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class="math">c</span>, then', 'antipode antihomomorphism')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class="math">c</span>, then', 'antipode antihomomorphism')###line 368:
    sage: format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class="math">c</span>, then', 'antipode antihomomorphism')
    NameError: name 'format_search_as_html' is not defined
html/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)

**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_7
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_sagedoc.py
         [24.9 s]
sage -t  devel/sage/sage/rings/tests.py
```




---

archive/issue_comments_044969.json:
```json
{
    "body": "I've tried, and I just can't reproduce this doctest failure.  Well, I can, but only by failing to apply one of the patches at #5754: if I apply either both of the patches there or neither of the patches there, I don't see a doctest failure for sagedoc.py.  If I only apply the first one, I see the failure here.",
    "created_at": "2009-04-12T17:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5764#issuecomment-44969",
    "user": "https://github.com/jhpalmieri"
}
```

I've tried, and I just can't reproduce this doctest failure.  Well, I can, but only by failing to apply one of the patches at #5754: if I apply either both of the patches there or neither of the patches there, I don't see a doctest failure for sagedoc.py.  If I only apply the first one, I see the failure here.



---

archive/issue_comments_044970.json:
```json
{
    "body": "The problem is 100% that I forgot to apply the patches at #5754.   Thanks.   Michael, keep in mind that this ticket depends on #5754.\n\nI think this doctest failure is caused by this patch, since you got rid of a lot of strips.\n\n```\nsage -t  devel/sage/sage/server/notebook/cell.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/cell.py\", line 406:\n    sage: C\nExpected:\n    Cell 0; in=2+3, out=20\nGot:\n    Cell 0; in=2+3, out=\n    20\n**********************************************************************\n1 items had failures:\n   1 of  13 in __main__.example_25\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_cell.py\n         [14.3 s]\n```\n\n\nHere are some similar failures:\n\n```\nsage -t  devel/sage/sage/server/notebook/worksheet.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py\", line 326:\n    sage: W.__repr__()\nExpected:\n    '[Cell 0; in=2+3, out=5, Cell 10; in=2+8, out=10]'\nGot:\n    '[Cell 0; in=2+3, out=\\n5, Cell 10; in=2+8, out=\\n10]'\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py\", line 2088:\n    sage: W\nExpected:\n    [Cell 0; in=2+3, out=5, Cell 1; in=2+8, out=10]\nGot:\n    [Cell 0; in=2+3, out=\n    5, Cell 1; in=2+8, out=\n    10]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py\", line 2509:\n    sage: v = W.cell_list(); v\nExpected:\n    [Cell 0; in=2+3, out=5, Cell 1; in=2+8, out=10]\nGot:\n    [Cell 0; in=2+3, out=\n    5, Cell 1; in=2+8, out=\n    10]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py\", line 2511:\n    sage: v[0]\nExpected:\n    Cell 0; in=2+3, out=5\nGot:\n    Cell 0; in=2+3, out=\n    5\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py\", line 3863:\n    sage: W.cell_list()\nExpected:\n    [Cell 0; in=2+3, out=5]\nGot:\n    [Cell 0; in=2+3, out=\n    5]\n**********************************************************************\n4 items had failures:\n   1 of   7 in __main__.example_7\n   1 of   8 in __main__.example_70\n   2 of   7 in __main__.example_79\n   1 of  11 in __main__.example_99\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_worksheet.py\n```\n",
    "created_at": "2009-04-12T19:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5764#issuecomment-44970",
    "user": "https://github.com/williamstein"
}
```

The problem is 100% that I forgot to apply the patches at #5754.   Thanks.   Michael, keep in mind that this ticket depends on #5754.

I think this doctest failure is caused by this patch, since you got rid of a lot of strips.

```
sage -t  devel/sage/sage/server/notebook/cell.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/cell.py", line 406:
    sage: C
Expected:
    Cell 0; in=2+3, out=20
Got:
    Cell 0; in=2+3, out=
    20
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_25
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_cell.py
         [14.3 s]
```


Here are some similar failures:

```
sage -t  devel/sage/sage/server/notebook/worksheet.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 326:
    sage: W.__repr__()
Expected:
    '[Cell 0; in=2+3, out=5, Cell 10; in=2+8, out=10]'
Got:
    '[Cell 0; in=2+3, out=\n5, Cell 10; in=2+8, out=\n10]'
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 2088:
    sage: W
Expected:
    [Cell 0; in=2+3, out=5, Cell 1; in=2+8, out=10]
Got:
    [Cell 0; in=2+3, out=
    5, Cell 1; in=2+8, out=
    10]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 2509:
    sage: v = W.cell_list(); v
Expected:
    [Cell 0; in=2+3, out=5, Cell 1; in=2+8, out=10]
Got:
    [Cell 0; in=2+3, out=
    5, Cell 1; in=2+8, out=
    10]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 2511:
    sage: v[0]
Expected:
    Cell 0; in=2+3, out=5
Got:
    Cell 0; in=2+3, out=
    5
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 3863:
    sage: W.cell_list()
Expected:
    [Cell 0; in=2+3, out=5]
Got:
    [Cell 0; in=2+3, out=
    5]
**********************************************************************
4 items had failures:
   1 of   7 in __main__.example_7
   1 of   8 in __main__.example_70
   2 of   7 in __main__.example_79
   1 of  11 in __main__.example_99
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_worksheet.py
```




---

archive/issue_comments_044971.json:
```json
{
    "body": "I don't think I actually changed any code in sageinspect -- just added doctests.  I think these errors are actually caused by the patch at #5379.  That certainly gets rid of some strips, and after applying the patch here, I don't get failures, but after applying the patch there, I do.  I'm changing this one back go \"needs review\" and I'll mark the other as \"needs work\".",
    "created_at": "2009-04-12T19:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5764#issuecomment-44971",
    "user": "https://github.com/jhpalmieri"
}
```

I don't think I actually changed any code in sageinspect -- just added doctests.  I think these errors are actually caused by the patch at #5379.  That certainly gets rid of some strips, and after applying the patch here, I don't get failures, but after applying the patch there, I do.  I'm changing this one back go "needs review" and I'll mark the other as "needs work".



---

archive/issue_comments_044972.json:
```json
{
    "body": "Hmm, unless this gets reviewed soon it will probably now make it into 3.4.1, even though it seems quite an important ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5764#issuecomment-44972",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, unless this gets reviewed soon it will probably now make it into 3.4.1, even though it seems quite an important ticket.

Cheers,

Michael



---

archive/issue_comments_044973.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T22:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5764#issuecomment-44973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044974.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T22:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5764#issuecomment-44974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_events_006011.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-13T22:57:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5764",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5764#event-6011"
}
```
