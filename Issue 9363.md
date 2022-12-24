# Issue 9363: load bug when last line of file begins with #

archive/issues_009363.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nConsider the following files and what sage\ndoes with each when they are loaded:\n\n---- foo1.sage ------\ndef add(a,b):\n return a+b\n------------------------\n\n--- foo2.py---\ndef add(a,b):\n return a+b\n# this is a comment\n---------------------\n\n--- foo3.sage---\ndef add(a,b):\n return a+b\n# this is a comment\n---------------------\n\neno% ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: load \"foo1.sage\"\nsage: load \"foo2.py\"\nsage: load \"foo3.sage\"\n------------------------------------------------------------\n  File \"<string>\", line 3\n    # this is a comment\n                      ^\nSyntaxError: invalid syntax\n| Sage Version 4.4.4, Release Date: 2010-06-23                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage:\n\nIs the inability to load foo3.sage a bug or a feature?\n\nAccording to William Stein: \n\n> It's a bug.   Please make a trac ticket for this. \n> Note that adding a newline to the end of the file is enough to \n> fix the problem... \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9363\n\n",
    "created_at": "2010-06-28T19:38:07Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "load bug when last line of file begins with #",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9363",
    "user": "mariah"
}
```
Assignee: somebody


```
Consider the following files and what sage
does with each when they are loaded:

---- foo1.sage ------
def add(a,b):
 return a+b
------------------------

--- foo2.py---
def add(a,b):
 return a+b
# this is a comment
---------------------

--- foo3.sage---
def add(a,b):
 return a+b
# this is a comment
---------------------

eno% ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: load "foo1.sage"
sage: load "foo2.py"
sage: load "foo3.sage"
------------------------------------------------------------
  File "<string>", line 3
    # this is a comment
                      ^
SyntaxError: invalid syntax
| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |
sage:

Is the inability to load foo3.sage a bug or a feature?

According to William Stein: 

> It's a bug.   Please make a trac ticket for this. 
> Note that adding a newline to the end of the file is enough to 
> fix the problem... 
```


Issue created by migration from https://trac.sagemath.org/ticket/9363





---

archive/issue_comments_088932.json:
```json
{
    "body": "One line reproduction recipe:\n\n\n```\nexec(\"if True:\\n pass\\n#\")\n```\n",
    "created_at": "2011-01-07T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88932",
    "user": "@wjp"
}
```

One line reproduction recipe:


```
exec("if True:\n pass\n#")
```




---

archive/issue_comments_088933.json:
```json
{
    "body": "The reason for this is likely this note from the python docs:\n\n\n```\nWhen compiling a string with multi-line code in\n'single' or 'eval' mode, input must be terminated\nby at least one newline character. This is to\nfacilitate detection of incomplete and complete\nstatements in the code module.\n```\n\n\n(Also note:\n\n```\nChanged in version 2.7: Allowed use of Windows and\nMac newlines. Also input in 'exec' mode does not\nhave to end in a newline anymore.\n```\n\n)\n\nThe obvious patch would be to add a newline automatically before passing the input to `exec`. I'll create a patch for this.",
    "created_at": "2011-01-07T23:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88933",
    "user": "@wjp"
}
```

The reason for this is likely this note from the python docs:


```
When compiling a string with multi-line code in
'single' or 'eval' mode, input must be terminated
by at least one newline character. This is to
facilitate detection of incomplete and complete
statements in the code module.
```


(Also note:

```
Changed in version 2.7: Allowed use of Windows and
Mac newlines. Also input in 'exec' mode does not
have to end in a newline anymore.
```

)

The obvious patch would be to add a newline automatically before passing the input to `exec`. I'll create a patch for this.



---

archive/issue_comments_088934.json:
```json
{
    "body": "Attachment [9363_exec_newline.patch](tarball://root/attachments/some-uuid/ticket9363/9363_exec_newline.patch) by @wjp created at 2011-01-07 23:25:24",
    "created_at": "2011-01-07T23:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88934",
    "user": "@wjp"
}
```

Attachment [9363_exec_newline.patch](tarball://root/attachments/some-uuid/ticket9363/9363_exec_newline.patch) by @wjp created at 2011-01-07 23:25:24



---

archive/issue_comments_088935.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-07T23:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88935",
    "user": "@wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088936.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-07T23:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88936",
    "user": "@adeines"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088937.json:
```json
{
    "body": "The patch won't apply:\n\napplying 9363_exec_newline.patch\npatching file sage/misc/preparser.py\nHunk #1 FAILED at 1588\n1 out of 1 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh 9363_exec_newline.patch",
    "created_at": "2011-01-07T23:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88937",
    "user": "@adeines"
}
```

The patch won't apply:

applying 9363_exec_newline.patch
patching file sage/misc/preparser.py
Hunk #1 FAILED at 1588
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 9363_exec_newline.patch



---

archive/issue_comments_088938.json:
```json
{
    "body": "Which version of sage are you using? Unless I messed something up, it's a patch against 4.6.1.rc0, which I should have mentioned, sorry.",
    "created_at": "2011-01-07T23:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88938",
    "user": "@wjp"
}
```

Which version of sage are you using? Unless I messed something up, it's a patch against 4.6.1.rc0, which I should have mentioned, sorry.



---

archive/issue_comments_088939.json:
```json
{
    "body": "Replying to [comment:5 wjp]:\n> Which version of sage are you using? Unless I messed something up, it's a patch against 4.6.1.rc0, which I should have mentioned, sorry.\n\nOkay!  I was just using 4.6.",
    "created_at": "2011-01-08T00:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88939",
    "user": "@adeines"
}
```

Replying to [comment:5 wjp]:
> Which version of sage are you using? Unless I messed something up, it's a patch against 4.6.1.rc0, which I should have mentioned, sorry.

Okay!  I was just using 4.6.



---

archive/issue_comments_088940.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-08T00:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88940",
    "user": "@wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088941.json:
```json
{
    "body": "On sage-4.6.rc0 the following tests failed:\n\n\tsage -t  \"devel/sage/sage/categories/hopf_algebras.py\" # Time out\n\tsage -t  \"devel/sage/sage/interfaces/r.py\"\n\tsage -t  \"devel/sage/sage/plot/plot3d/base.pyx\"\n\nI'll try again on sage-4.6.rc1 and see what happens there.",
    "created_at": "2011-01-08T20:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88941",
    "user": "@adeines"
}
```

On sage-4.6.rc0 the following tests failed:

	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
	sage -t  "devel/sage/sage/interfaces/r.py"
	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"

I'll try again on sage-4.6.rc1 and see what happens there.



---

archive/issue_comments_088942.json:
```json
{
    "body": "Replying to [comment:8 aly.deines]:\n> On sage-4.6.rc0 the following tests failed:\n> \n> \tsage -t  \"devel/sage/sage/categories/hopf_algebras.py\" # Time out\n> \tsage -t  \"devel/sage/sage/interfaces/r.py\"\n> \tsage -t  \"devel/sage/sage/plot/plot3d/base.pyx\"\n> \n> I'll try again on sage-4.6.rc1 and see what happens there.\n\nBetter formatting:\n\n\n```\n\n\tsage -t  \"devel/sage/sage/categories/hopf_algebras.py\" # Time out\n\tsage -t  \"devel/sage/sage/interfaces/r.py\"\n\tsage -t  \"devel/sage/sage/plot/plot3d/base.pyx\"\n```\n",
    "created_at": "2011-01-08T20:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88942",
    "user": "@adeines"
}
```

Replying to [comment:8 aly.deines]:
> On sage-4.6.rc0 the following tests failed:
> 
> 	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
> 	sage -t  "devel/sage/sage/interfaces/r.py"
> 	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
> 
> I'll try again on sage-4.6.rc1 and see what happens there.

Better formatting:


```

	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
	sage -t  "devel/sage/sage/interfaces/r.py"
	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
```




---

archive/issue_comments_088943.json:
```json
{
    "body": "Strange, but those shouldn't be related to this patch (or so I hope). Do they also happen if you run these three tests manually? And without this patch?",
    "created_at": "2011-01-08T23:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88943",
    "user": "@wjp"
}
```

Strange, but those shouldn't be related to this patch (or so I hope). Do they also happen if you run these three tests manually? And without this patch?



---

archive/issue_comments_088944.json:
```json
{
    "body": "Replying to [comment:10 wjp]:\n> Strange, but those shouldn't be related to this patch (or so I hope). Do they also happen if you run these three tests manually? And without this patch?\n\nI get the same thing when the three tests are run manually, and these tests pass when the patch is not applied.",
    "created_at": "2011-01-08T23:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88944",
    "user": "@adeines"
}
```

Replying to [comment:10 wjp]:
> Strange, but those shouldn't be related to this patch (or so I hope). Do they also happen if you run these three tests manually? And without this patch?

I get the same thing when the three tests are run manually, and these tests pass when the patch is not applied.



---

archive/issue_comments_088945.json:
```json
{
    "body": "Can you show the full output of the failing tests? (I can't get them to fail myself on my PC.)",
    "created_at": "2011-01-08T23:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88945",
    "user": "@wjp"
}
```

Can you show the full output of the failing tests? (I can't get them to fail myself on my PC.)



---

archive/issue_comments_088946.json:
```json
{
    "body": "Replying to [comment:9 aly.deines]:\n> Replying to [comment:8 aly.deines]:\n> > On sage-4.6.rc0 the following tests failed:\n> > \n> > \tsage -t  \"devel/sage/sage/categories/hopf_algebras.py\" # Time out\n> > \tsage -t  \"devel/sage/sage/interfaces/r.py\"\n> > \tsage -t  \"devel/sage/sage/plot/plot3d/base.pyx\"\n> > \n> > I'll try again on sage-4.6.rc1 and see what happens there.\n> \n> Better formatting:\n> \n> {{{\n> \n> \tsage -t  \"devel/sage/sage/categories/hopf_algebras.py\" # Time out\n> \tsage -t  \"devel/sage/sage/interfaces/r.py\"\n> \tsage -t  \"devel/sage/sage/plot/plot3d/base.pyx\"\n> }}}\n\nI'll unapply the patch and retry these three doctests, but earlier this afternoon they failed both before and after the patch was applied.\n\n\nHowever, the test\n\n\n```\n      sage -t  \"devel/sage/sage/misc/preparser.py\"\n```\n\n\nPasses both before and after applying the patch.",
    "created_at": "2011-01-09T00:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88946",
    "user": "gbe"
}
```

Replying to [comment:9 aly.deines]:
> Replying to [comment:8 aly.deines]:
> > On sage-4.6.rc0 the following tests failed:
> > 
> > 	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
> > 	sage -t  "devel/sage/sage/interfaces/r.py"
> > 	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
> > 
> > I'll try again on sage-4.6.rc1 and see what happens there.
> 
> Better formatting:
> 
> {{{
> 
> 	sage -t  "devel/sage/sage/categories/hopf_algebras.py" # Time out
> 	sage -t  "devel/sage/sage/interfaces/r.py"
> 	sage -t  "devel/sage/sage/plot/plot3d/base.pyx"
> }}}

I'll unapply the patch and retry these three doctests, but earlier this afternoon they failed both before and after the patch was applied.


However, the test


```
      sage -t  "devel/sage/sage/misc/preparser.py"
```


Passes both before and after applying the patch.



---

archive/issue_comments_088947.json:
```json
{
    "body": "passed all tests for me this afternoon (4.6.4.rc1), but checking coverage yielded: \n\n\n```\n\ndevel/sage/sage/misc/preparser.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE devel/sage/sage/misc/preparser.py: 88% (23 of 26)\n\nMissing documentation:\n\t * isalphadigit_(s):\n\t * for lambda try \"\"\".split() in_single_quote = False in_double_quote = False in_triple_quote = False def in_quote():\n\t * re_no_keyword(pattern, code):\n```\n",
    "created_at": "2011-01-09T00:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88947",
    "user": "jthurber"
}
```

passed all tests for me this afternoon (4.6.4.rc1), but checking coverage yielded: 


```

devel/sage/sage/misc/preparser.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage/sage/misc/preparser.py: 88% (23 of 26)

Missing documentation:
	 * isalphadigit_(s):
	 * for lambda try """.split() in_single_quote = False in_double_quote = False in_triple_quote = False def in_quote():
	 * re_no_keyword(pattern, code):
```




---

archive/issue_comments_088948.json:
```json
{
    "body": "Replying to [comment:14 jthurber]:\n> passed all tests for me this afternoon (4.6.4.rc1), but checking coverage yielded: \n> \n> {{{\n> \n> devel/sage/sage/misc/preparser.py\n> ERROR: Please add a `TestSuite(s).run()` doctest.\n> SCORE devel/sage/sage/misc/preparser.py: 88% (23 of 26)\n> \n> Missing documentation:\n> \t * isalphadigit_(s):\n> \t * for lambda try \"\"\".split() in_single_quote = False in_double_quote = False in_triple_quote = False def in_quote():\n> \t * re_no_keyword(pattern, code):\n> }}}\n\nSo two things, first, I think I ran the tests on a different version of sage, as now I am getting that those three tests fail both with and without the patch applied.  \nSecond, the add 'TestSuit(s).run()' doctest and the missing doctest are not related to this ticket (though completing the coverage could be another ticket.)",
    "created_at": "2011-01-09T00:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88948",
    "user": "@adeines"
}
```

Replying to [comment:14 jthurber]:
> passed all tests for me this afternoon (4.6.4.rc1), but checking coverage yielded: 
> 
> {{{
> 
> devel/sage/sage/misc/preparser.py
> ERROR: Please add a `TestSuite(s).run()` doctest.
> SCORE devel/sage/sage/misc/preparser.py: 88% (23 of 26)
> 
> Missing documentation:
> 	 * isalphadigit_(s):
> 	 * for lambda try """.split() in_single_quote = False in_double_quote = False in_triple_quote = False def in_quote():
> 	 * re_no_keyword(pattern, code):
> }}}

So two things, first, I think I ran the tests on a different version of sage, as now I am getting that those three tests fail both with and without the patch applied.  
Second, the add 'TestSuit(s).run()' doctest and the missing doctest are not related to this ticket (though completing the coverage could be another ticket.)



---

archive/issue_comments_088949.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-09T00:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88949",
    "user": "@adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088950.json:
```json
{
    "body": "Replying to [comment:15 aly.deines]:\n> So two things, first, I think I ran the tests on a different version of sage, as now I am getting that those three tests fail both with and without the patch applied.  \n> Second, the add 'TestSuit(s).run()' doctest and the missing doctest are not related to this ticket (though completing the coverage could be another ticket.)\n\nIt looks to me like those doctest failures were fixed some time between 4.6 and 4.6.1rc0.",
    "created_at": "2011-01-09T01:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88950",
    "user": "gbe"
}
```

Replying to [comment:15 aly.deines]:
> So two things, first, I think I ran the tests on a different version of sage, as now I am getting that those three tests fail both with and without the patch applied.  
> Second, the add 'TestSuit(s).run()' doctest and the missing doctest are not related to this ticket (though completing the coverage could be another ticket.)

It looks to me like those doctest failures were fixed some time between 4.6 and 4.6.1rc0.



---

archive/issue_comments_088951.json:
```json
{
    "body": "I've noticed this before but hadn't diagnosed it - thanks!  Will this also fix the analogous thing for `attach` instead of `load`?",
    "created_at": "2011-01-14T17:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88951",
    "user": "@kcrisman"
}
```

I've noticed this before but hadn't diagnosed it - thanks!  Will this also fix the analogous thing for `attach` instead of `load`?



---

archive/issue_comments_088952.json:
```json
{
    "body": "I haven't actually tried that, but looking at the code `attach` should be following the same code path.",
    "created_at": "2011-01-17T16:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88952",
    "user": "@wjp"
}
```

I haven't actually tried that, but looking at the code `attach` should be following the same code path.



---

archive/issue_comments_088953.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9363#issuecomment-88953",
    "user": "@jdemeyer"
}
```

Resolution: fixed
