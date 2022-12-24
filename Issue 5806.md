# Issue 5806: failing test "devel/sage/sage/misc/sagedoc.py"

archive/issues_005806.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @jhpalmieri\n\nOn fedora 9, 32 bit this fails:\n\n\n\n```\nsage -t  \"devel/sage/sage/misc/sagedoc.py\"                  \n**********************************************************************\nFile \"/home/jaap/downloads/sage-3.4.1.rc0/devel/sage/sage/misc/sagedoc.py\", line 411:\n    sage: print \"ignore this\";  search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.4.1.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.4.1.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.4.1.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[2]>\", line 1, in <module>\n        print \"ignore this\";  search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string###line 411:\n    sage: print \"ignore this\";  search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string\n      File \"/home/jaap/downloads/sage-3.4.1.rc0/local/lib/python2.5/site-packages/sage/misc/sagedoc.py\", line 431, in search_doc\n        pager()(r)\n      File \"/home/jaap/downloads/sage-3.4.1.rc0/local/lib/python2.5/site-packages/IPython/genutils.py\", line 1664, in page\n        term_flags = termios.tcgetattr(sys.stdout)\n    TypeError: argument must be an int, or have a fileno() method.\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_8\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/jaap/downloads/sage-3.4.1.rc0/tmp/.doctest_sagedoc.py\n\t [46.3 s]\nexit code: 1024\n\n```\n\n\nWhatever :)\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/5806\n\n",
    "created_at": "2009-04-16T21:40:09Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "failing test \"devel/sage/sage/misc/sagedoc.py\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5806",
    "user": "@jaapspies"
}
```
Assignee: cwitty

CC:  @jhpalmieri

On fedora 9, 32 bit this fails:



```
sage -t  "devel/sage/sage/misc/sagedoc.py"                  
**********************************************************************
File "/home/jaap/downloads/sage-3.4.1.rc0/devel/sage/sage/misc/sagedoc.py", line 411:
    sage: print "ignore this";  search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[2]>", line 1, in <module>
        print "ignore this";  search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string###line 411:
    sage: print "ignore this";  search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string
      File "/home/jaap/downloads/sage-3.4.1.rc0/local/lib/python2.5/site-packages/sage/misc/sagedoc.py", line 431, in search_doc
        pager()(r)
      File "/home/jaap/downloads/sage-3.4.1.rc0/local/lib/python2.5/site-packages/IPython/genutils.py", line 1664, in page
        term_flags = termios.tcgetattr(sys.stdout)
    TypeError: argument must be an int, or have a fileno() method.
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.4.1.rc0/tmp/.doctest_sagedoc.py
	 [46.3 s]
exit code: 1024

```


Whatever :)

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/5806





---

archive/issue_comments_045571.json:
```json
{
    "body": "For anyone else who wanders in here, we're talking about 3.4.1.rc3.\n\nI'm also seeing a failure in sagedoc.py, but it's a different failure. This is with Ubuntu 8.10 amd64, and happens every time:\n\n\n```\nsage -t -long \"devel/sage/sage/misc/sagedoc.py\"             \n**********************************************************************\nFile \"/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py\", line 480:\n    sage: s = my_getsource(identity_matrix, True)\nExpected nothing\nGot:\n    Error getting source: could not get source code\n**********************************************************************\nFile \"/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py\", line 481:\n    sage: s[:19]\nException raised:\n    Traceback (most recent call last):\n      File \"/var/tmp/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/var/tmp/sage-3.4.1.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/var/tmp/sage-3.4.1.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[4]>\", line 1, in <module>\n        s[:Integer(19)]###line 481:\n    sage: s[:19]\n    TypeError: 'NoneType' object is unsubscriptable\n**********************************************************************\nFile \"/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py\", line 238:\n    sage: format_src('<<<Sqsage:')[5:15]\nExpected:\n    'Sq(*nums):'\nGot:\n    Error getting source: could not get source code\n    <function Sq at 0x25d72a8>\n    ''\nhtml/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)\n\n**********************************************************************\n2 items had failures:\n   2 of   5 in __main__.example_10\n   1 of   5 in __main__.example_4\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /var/tmp/sage-3.4.1.rc/tmp/.doctest_sagedoc.py\n\t [16.4 s]\nexit code: 1024\n \n----------------------------------------------------------------------\n```\n",
    "created_at": "2009-04-17T08:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45571",
    "user": "@dandrake"
}
```

For anyone else who wanders in here, we're talking about 3.4.1.rc3.

I'm also seeing a failure in sagedoc.py, but it's a different failure. This is with Ubuntu 8.10 amd64, and happens every time:


```
sage -t -long "devel/sage/sage/misc/sagedoc.py"             
**********************************************************************
File "/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py", line 480:
    sage: s = my_getsource(identity_matrix, True)
Expected nothing
Got:
    Error getting source: could not get source code
**********************************************************************
File "/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py", line 481:
    sage: s[:19]
Exception raised:
    Traceback (most recent call last):
      File "/var/tmp/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/var/tmp/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/var/tmp/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[4]>", line 1, in <module>
        s[:Integer(19)]###line 481:
    sage: s[:19]
    TypeError: 'NoneType' object is unsubscriptable
**********************************************************************
File "/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py", line 238:
    sage: format_src('<<<Sqsage:')[5:15]
Expected:
    'Sq(*nums):'
Got:
    Error getting source: could not get source code
    <function Sq at 0x25d72a8>
    ''
html/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)

**********************************************************************
2 items had failures:
   2 of   5 in __main__.example_10
   1 of   5 in __main__.example_4
***Test Failed*** 3 failures.
For whitespace errors, see the file /var/tmp/sage-3.4.1.rc/tmp/.doctest_sagedoc.py
	 [16.4 s]
exit code: 1024
 
----------------------------------------------------------------------
```




---

archive/issue_comments_045572.json:
```json
{
    "body": "It seems that the offending changeset is:\n\n```\nchangeset:   11994:e4066f66cdd2\nuser:        J. H. Palmieri <palmieri@math.washington.edu>\ndate:        Sat Apr 11 10:30:03 2009 -0700\nsummary:     fix for #5754 plus doctests\n```\n\nThe patches at #5754 are definitely implicated here. My doctest failures are more like the failures William noted when he reviewed the patches there.",
    "created_at": "2009-04-17T08:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45572",
    "user": "@dandrake"
}
```

It seems that the offending changeset is:

```
changeset:   11994:e4066f66cdd2
user:        J. H. Palmieri <palmieri@math.washington.edu>
date:        Sat Apr 11 10:30:03 2009 -0700
summary:     fix for #5754 plus doctests
```

The patches at #5754 are definitely implicated here. My doctest failures are more like the failures William noted when he reviewed the patches there.



---

archive/issue_comments_045573.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-04-17T08:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45573",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_045574.json:
```json
{
    "body": "Thanks for tracking this down. I am surprised it works on various boxen I tested, but not on yours. Oh well, doctests must be evil :)\n\nI am making this a blocker and also CCed John - maybe something obvious is jumping out at him :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T08:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45574",
    "user": "mabshoff"
}
```

Thanks for tracking this down. I am surprised it works on various boxen I tested, but not on yours. Oh well, doctests must be evil :)

I am making this a blocker and also CCed John - maybe something obvious is jumping out at him :)

Cheers,

Michael



---

archive/issue_comments_045575.json:
```json
{
    "body": "#5764 is somehow involved in this, too. I've poked around a bit, and there is some strange interaction between sagedoc.py and sageinspect.py related to formatting strings, I think. I haven't looked any further than that.",
    "created_at": "2009-04-17T09:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45575",
    "user": "@dandrake"
}
```

#5764 is somehow involved in this, too. I've poked around a bit, and there is some strange interaction between sagedoc.py and sageinspect.py related to formatting strings, I think. I haven't looked any further than that.



---

archive/issue_comments_045576.json:
```json
{
    "body": "What I get in sagedoc.py is this:\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/misc/sagedoc.py\"\nTotal time for all tests: 0.2 seconds\nmasgaj@host-56-150%./sage -t  /home/masgaj/local/sage-3.4.1.rc3/devel/sage/sage/misc/sagedoc.py\nsage -t  \"devel/sage/sage/misc/sagedoc.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [360.1 s]\nexit code: 1024\n```\n\n\nThis is on a different machine than the one where I got a similar problem earlier today (both 32-bit linux, this one is Suse and the other was ubuntu).",
    "created_at": "2009-04-17T12:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45576",
    "user": "@JohnCremona"
}
```

What I get in sagedoc.py is this:

```
The following tests failed:


        sage -t  "devel/sage/sage/misc/sagedoc.py"
Total time for all tests: 0.2 seconds
masgaj@host-56-150%./sage -t  /home/masgaj/local/sage-3.4.1.rc3/devel/sage/sage/misc/sagedoc.py
sage -t  "devel/sage/sage/misc/sagedoc.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [360.1 s]
exit code: 1024
```


This is on a different machine than the one where I got a similar problem earlier today (both 32-bit linux, this one is Suse and the other was ubuntu).



---

archive/issue_comments_045577.json:
```json
{
    "body": "Replying to [comment:2 ddrake]:\n\n\n```\n\n**********************************************************************\nFile \"/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py\", line 238:\n    sage: format_src('<<<Sqsage:')[5:15]\nExpected:\n    'Sq(*nums):'\n```\n\n\nNote that the doctest in the file says `sage: format_src('<<<Sq>>>')[5:15]`.  Why is `>>>` getting changed to `sage:`?\n\nReplying to [comment:6 cremona]:\n\n> What I get in sagedoc.py is this: \n\n[snip] time out failure\n\nI have seen this before, but not repeatably.  I only saw it doing sage -t on the particular file, not when doing sage -testall.  Try `sage -t -verbose`: is it freezing on a `search_src` command?\n\nWe can always revert the changes at #5764 if we have to (or at least reinstate the \"nodoctest\" at the top of the file).\n\nReplying to [ticket:5806 jsp]: \n\nCan you run this successfully from within Sage:\n\n```\nsage: search_doc('this creates a polynomial ring')\n```\n",
    "created_at": "2009-04-17T18:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45577",
    "user": "@jhpalmieri"
}
```

Replying to [comment:2 ddrake]:


```

**********************************************************************
File "/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py", line 238:
    sage: format_src('<<<Sqsage:')[5:15]
Expected:
    'Sq(*nums):'
```


Note that the doctest in the file says `sage: format_src('<<<Sq>>>')[5:15]`.  Why is `>>>` getting changed to `sage:`?

Replying to [comment:6 cremona]:

> What I get in sagedoc.py is this: 

[snip] time out failure

I have seen this before, but not repeatably.  I only saw it doing sage -t on the particular file, not when doing sage -testall.  Try `sage -t -verbose`: is it freezing on a `search_src` command?

We can always revert the changes at #5764 if we have to (or at least reinstate the "nodoctest" at the top of the file).

Replying to [ticket:5806 jsp]: 

Can you run this successfully from within Sage:

```
sage: search_doc('this creates a polynomial ring')
```




---

archive/issue_comments_045578.json:
```json
{
    "body": "It stcks here:\n\n\n```\nsage -t -verbose \"devel/sage/sage/misc/sagedoc.py\"          \n...\nTrying:\n    print \"ignore this\";  print search_src(\" fetch(\", \"def\", interact=False) # random # long###line 286:_sage_    >>> print \"ignore this\";  print search_src(\" fetch(\", \"def\", interact=False) # random # long\nExpecting:\n    ignore ...\n```\n\n\nThis is with --verbose, not --long (it says # long but not #long time so this test does run without the -long option).",
    "created_at": "2009-04-17T19:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45578",
    "user": "@JohnCremona"
}
```

It stcks here:


```
sage -t -verbose "devel/sage/sage/misc/sagedoc.py"          
...
Trying:
    print "ignore this";  print search_src(" fetch(", "def", interact=False) # random # long###line 286:_sage_    >>> print "ignore this";  print search_src(" fetch(", "def", interact=False) # random # long
Expecting:
    ignore ...
```


This is with --verbose, not --long (it says # long but not #long time so this test does run without the -long option).



---

archive/issue_comments_045579.json:
```json
{
    "body": "Okay, I think I've figured out one of these, but not the other two: I think ddrake's problem is caused because he is using a binary-only distribution, and so source codes are not available.  Or something like that. Anyway, adding a #random tag to those tests ought to fix this issue.\n\nI don't know what to do about the other two issues...",
    "created_at": "2009-04-17T21:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45579",
    "user": "@jhpalmieri"
}
```

Okay, I think I've figured out one of these, but not the other two: I think ddrake's problem is caused because he is using a binary-only distribution, and so source codes are not available.  Or something like that. Anyway, adding a #random tag to those tests ought to fix this issue.

I don't know what to do about the other two issues...



---

archive/issue_comments_045580.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> Replying to [comment:2 ddrake]:\n> \n> {{{\n> \n> **********************************************************************\n> File \"/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py\", line 238:\n>     sage: format_src('<<<Sqsage:')[5:15]\n> Expected:\n>     'Sq(*nums):'\n> }}}\n> \n> Note that the doctest in the file says `sage: format_src('<<<Sq>>>')[5:15]`.  Why is `>>>` getting changed to `sage:`?\n\nThat is weird, but `>>>` is the usual prompt command in Python, so something is replacing that prompt with the usual Sage one. Something in the preparser?\n\nReplying to [comment:9 jhpalmieri]:\n> I think ddrake's problem is caused because he is using a binary-only distribution, \n> and so source codes are not available.\n\nNope, I am using a source distribution. Moreover, since these are Python files, shouldn't it *always* be possible to search the source?",
    "created_at": "2009-04-18T04:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45580",
    "user": "@dandrake"
}
```

Replying to [comment:7 jhpalmieri]:
> Replying to [comment:2 ddrake]:
> 
> {{{
> 
> **********************************************************************
> File "/var/tmp/sage-3.4.1.rc/devel/sage/sage/misc/sagedoc.py", line 238:
>     sage: format_src('<<<Sqsage:')[5:15]
> Expected:
>     'Sq(*nums):'
> }}}
> 
> Note that the doctest in the file says `sage: format_src('<<<Sq>>>')[5:15]`.  Why is `>>>` getting changed to `sage:`?

That is weird, but `>>>` is the usual prompt command in Python, so something is replacing that prompt with the usual Sage one. Something in the preparser?

Replying to [comment:9 jhpalmieri]:
> I think ddrake's problem is caused because he is using a binary-only distribution, 
> and so source codes are not available.

Nope, I am using a source distribution. Moreover, since these are Python files, shouldn't it *always* be possible to search the source?



---

archive/issue_comments_045581.json:
```json
{
    "body": "For `search_doc('this creates a polynomial ring')`, at least, the problem seems to be that `ncadoctest.py`'s spoofed version of `sys.stdout` is missing a `fileno()` method.  `IPython.genutils.page` calls this implicitly (line 1664 of `genutils.py`), when it tries to determine the screen size.  Replacing\n\n\n```\n        from sage.misc.all import pager\n        pager()(r)\n```\n\n\nwith something like\n\n\n```\n        from IPython.genutils import page\n        page(r, screen_lines = 1)\n```\n\n\ndisables the check.  The doctest then passes.",
    "created_at": "2009-04-18T05:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45581",
    "user": "@qed777"
}
```

For `search_doc('this creates a polynomial ring')`, at least, the problem seems to be that `ncadoctest.py`'s spoofed version of `sys.stdout` is missing a `fileno()` method.  `IPython.genutils.page` calls this implicitly (line 1664 of `genutils.py`), when it tries to determine the screen size.  Replacing


```
        from sage.misc.all import pager
        pager()(r)
```


with something like


```
        from IPython.genutils import page
        page(r, screen_lines = 1)
```


disables the check.  The doctest then passes.



---

archive/issue_comments_045582.json:
```json
{
    "body": "Okay, I need to investigate more, but I've tried on more machines, and have found that freshly built trees seem to work better. I built from rc3 source on Ubuntu 8.10 amd64 and 32-bit Fedora 10, and can't reproduce this bug. My original report is from an upgraded tree, and I upgraded from rc2 to rc3 on OS X and am seeing the same error that [comment:8 cremona] saw, but it's intermittent; I see it once every four or five tests.\n\nI am building a fresh rc3 tree on OS X and will report what I see, although it will be a day or so until I have time to do this.",
    "created_at": "2009-04-18T15:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45582",
    "user": "@dandrake"
}
```

Okay, I need to investigate more, but I've tried on more machines, and have found that freshly built trees seem to work better. I built from rc3 source on Ubuntu 8.10 amd64 and 32-bit Fedora 10, and can't reproduce this bug. My original report is from an upgraded tree, and I upgraded from rc2 to rc3 on OS X and am seeing the same error that [comment:8 cremona] saw, but it's intermittent; I see it once every four or five tests.

I am building a fresh rc3 tree on OS X and will report what I see, although it will be a day or so until I have time to do this.



---

archive/issue_comments_045583.json:
```json
{
    "body": "Just for the record, mine was from a fresh build.  It happens nearly every time, but not with \"-verbose\" usually.  Just sometimes...",
    "created_at": "2009-04-18T15:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45583",
    "user": "@JohnCremona"
}
```

Just for the record, mine was from a fresh build.  It happens nearly every time, but not with "-verbose" usually.  Just sometimes...



---

archive/issue_comments_045584.json:
```json
{
    "body": "On the \"fetch\" tests:  I'm not sure why, but the problem seems to be os.popen, which is deprecated in favor of the subprocess module:\n\nhttp://docs.python.org/library/subprocess.html\n\nHere's a potential fix:\n\nAt the top of `sagedoc.py` add\n\n```\nfrom subprocess import Popen, PIPE\n```\n\nThen replace\n\n```\nr = os.popen(cmd).read()\n```\n\nwith\n\n```\nr = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]\n```\n\n\nThere's still an issue with `\\n`'s, though.",
    "created_at": "2009-04-18T17:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45584",
    "user": "@qed777"
}
```

On the "fetch" tests:  I'm not sure why, but the problem seems to be os.popen, which is deprecated in favor of the subprocess module:

http://docs.python.org/library/subprocess.html

Here's a potential fix:

At the top of `sagedoc.py` add

```
from subprocess import Popen, PIPE
```

Then replace

```
r = os.popen(cmd).read()
```

with

```
r = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]
```


There's still an issue with `\n`'s, though.



---

archive/issue_comments_045585.json:
```json
{
    "body": "At the moment I am tempted to reinstate the nodoctest for this file and then have the issues for this patch sorted out post 3.4.1.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-19T01:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45585",
    "user": "mabshoff"
}
```

At the moment I am tempted to reinstate the nodoctest for this file and then have the issues for this patch sorted out post 3.4.1.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_045586.json:
```json
{
    "body": "Replying to [comment:15 mabshoff]:\n> At the moment I am tempted to reinstate the nodoctest for this file and then have the issues for this patch sorted out post 3.4.1.\n> \n> Thoughts?\n\nSince I know you really want to get 3.4.1 out, I would go along with putting the nodoctest back in for the moment, since I don't think anyone really knows what's happening here.",
    "created_at": "2009-04-20T02:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45586",
    "user": "@dandrake"
}
```

Replying to [comment:15 mabshoff]:
> At the moment I am tempted to reinstate the nodoctest for this file and then have the issues for this patch sorted out post 3.4.1.
> 
> Thoughts?

Since I know you really want to get 3.4.1 out, I would go along with putting the nodoctest back in for the moment, since I don't think anyone really knows what's happening here.



---

archive/issue_comments_045587.json:
```json
{
    "body": "Please be aware that #5826 adds a nodoctest to this file to get 3.4.1 out the door. This should be reverted in this patch so we do actually doctest something :)\n\nBumped to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-20T03:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45587",
    "user": "mabshoff"
}
```

Please be aware that #5826 adds a nodoctest to this file to get 3.4.1 out the door. This should be reverted in this patch so we do actually doctest something :)

Bumped to 3.4.2.

Cheers,

Michael



---

archive/issue_comments_045588.json:
```json
{
    "body": "I apologize for not posting patches.  Did anyone happen to have any success with the changes I suggested?\n\nFor the \"ring\" and \"fetch\" failures, the general issue seems to be how the doctesting framework interacts with pipes.\n\nI found that pressing Control-C to quit a stalled \"fetch\" test didn't always quit all of the spawned process(es).  If I didn't kill these, subsequent test runs would usually (always?) pass.  This \"explained\" the \"random\" pass/fail behavior.\n\nAnyway, temporarily disabling doctesting seems to be a good idea, since the suggested changes themselves, if they're of any use, need wider, interactive testing.\n\nWhy does trac not use the entire width of the browser window for the change history?",
    "created_at": "2009-04-20T05:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45588",
    "user": "@qed777"
}
```

I apologize for not posting patches.  Did anyone happen to have any success with the changes I suggested?

For the "ring" and "fetch" failures, the general issue seems to be how the doctesting framework interacts with pipes.

I found that pressing Control-C to quit a stalled "fetch" test didn't always quit all of the spawned process(es).  If I didn't kill these, subsequent test runs would usually (always?) pass.  This "explained" the "random" pass/fail behavior.

Anyway, temporarily disabling doctesting seems to be a good idea, since the suggested changes themselves, if they're of any use, need wider, interactive testing.

Why does trac not use the entire width of the browser window for the change history?



---

archive/issue_comments_045589.json:
```json
{
    "body": "Replying to [comment:18 mpatel]:\n> For the \"ring\" and \"fetch\" failures, the general issue seems to be how the doctesting framework interacts with pipes.\n\nI think this is correct. In fact, I think the problem is with pipes and sage-grep (and its companion sage-grepdoc). Those processes never seem to finish; I could insert \"tee\" commands and see that they were outputting what you would expect, but never quitting, so the pipe remained open, and the doctests hung.\n\nI'm attaching a patch against 4.0.alpha0 which avoids the use of sage-grep and sage-grepdoc and directly issues a \"`find ... -exec grep ... `\" command. It also switches to using the subprocess module. This should fix the problems with `search_src` and friends.\n\nThe patch also fixes a small bug in `search_src` when displaying the results in the notebook -- it now sends a correct string of search terms to `format_search_as_html`.\n\nI tested the patch on an amd64 Ubuntu system and a 32-bit Fedora 10 system. It may not work in OS X since the \"find\" command there sometimes behaves strangely when it encounters symlinks. We may need to fiddle with that command.",
    "created_at": "2009-05-20T02:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45589",
    "user": "@dandrake"
}
```

Replying to [comment:18 mpatel]:
> For the "ring" and "fetch" failures, the general issue seems to be how the doctesting framework interacts with pipes.

I think this is correct. In fact, I think the problem is with pipes and sage-grep (and its companion sage-grepdoc). Those processes never seem to finish; I could insert "tee" commands and see that they were outputting what you would expect, but never quitting, so the pipe remained open, and the doctests hung.

I'm attaching a patch against 4.0.alpha0 which avoids the use of sage-grep and sage-grepdoc and directly issues a "`find ... -exec grep ... `" command. It also switches to using the subprocess module. This should fix the problems with `search_src` and friends.

The patch also fixes a small bug in `search_src` when displaying the results in the notebook -- it now sends a correct string of search terms to `format_search_as_html`.

I tested the patch on an amd64 Ubuntu system and a 32-bit Fedora 10 system. It may not work in OS X since the "find" command there sometimes behaves strangely when it encounters symlinks. We may need to fiddle with that command.



---

archive/issue_comments_045590.json:
```json
{
    "body": "This seems to break `search_src` on my mac:\n\n```\nsage: len(search_src(\"matrix\", interact=False).splitlines())\n0\nsage: search_src(\"matrix\", interact=False)\n''\nsage: search_src(\"matrix\")\n\n```\n\nThe problem is the find command, as you suspected.  By using the [man page](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/find.1.html) and a lot of trial and error, I found that a command something like this one works:\n\n```\nfind -f /Applications/sage/devel/sage/sage \".*\\\\.\\\\(py\\\\|pyx\\\\|pxd\\\\)\" -exec grep -i -H matrix {} + \n```\n\nalthough this isn't right either.  I actually really hate the find command...",
    "created_at": "2009-05-20T05:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45590",
    "user": "@jhpalmieri"
}
```

This seems to break `search_src` on my mac:

```
sage: len(search_src("matrix", interact=False).splitlines())
0
sage: search_src("matrix", interact=False)
''
sage: search_src("matrix")

```

The problem is the find command, as you suspected.  By using the [man page](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/find.1.html) and a lot of trial and error, I found that a command something like this one works:

```
find -f /Applications/sage/devel/sage/sage ".*\\.\\(py\\|pyx\\|pxd\\)" -exec grep -i -H matrix {} + 
```

although this isn't right either.  I actually really hate the find command...



---

archive/issue_comments_045591.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-20T13:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45591",
    "user": "@dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045592.json:
```json
{
    "body": "Changing assignee from cwitty to @dandrake.",
    "created_at": "2009-05-20T13:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45592",
    "user": "@dandrake"
}
```

Changing assignee from cwitty to @dandrake.



---

archive/issue_comments_045593.json:
```json
{
    "body": "Replying to [comment:21 jhpalmieri]:\n> The problem is the find command, as you suspected.  By using the [man page](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/find.1.html) and a lot of trial and error, I found that a command something like this one works:\n> {{{\n> find -f /Applications/sage/devel/sage/sage \".*\\\\.\\\\(py\\\\|pyx\\\\|pxd\\\\)\" -exec grep -i -H matrix {} + \n> }}}\n> although this isn't right either.  I actually really hate the find command...\n\nI figured out the problem: it's the regex stuff, not the symlinks. GNU find demands backslashes in `\\(py\\|pyx\\|pxd\\)` unless you specify \"-regextype posix-awk\"; Apple's find demands that you *not* use backslashes and doesn't understand \"-regextype\". Kids, this is why daddy drinks.\n\nI'll punt and just chain together a bunch of \"`-or -name ...`\"; I tested that and it works in OS X and Linux. Next, of course, someone will come along and tell us that it doesn't work in Solaris or BSD. (Right now I'm not even *thinking* about Windows...)",
    "created_at": "2009-05-20T13:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45593",
    "user": "@dandrake"
}
```

Replying to [comment:21 jhpalmieri]:
> The problem is the find command, as you suspected.  By using the [man page](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man1/find.1.html) and a lot of trial and error, I found that a command something like this one works:
> {{{
> find -f /Applications/sage/devel/sage/sage ".*\\.\\(py\\|pyx\\|pxd\\)" -exec grep -i -H matrix {} + 
> }}}
> although this isn't right either.  I actually really hate the find command...

I figured out the problem: it's the regex stuff, not the symlinks. GNU find demands backslashes in `\(py\|pyx\|pxd\)` unless you specify "-regextype posix-awk"; Apple's find demands that you *not* use backslashes and doesn't understand "-regextype". Kids, this is why daddy drinks.

I'll punt and just chain together a bunch of "`-or -name ...`"; I tested that and it works in OS X and Linux. Next, of course, someone will come along and tell us that it doesn't work in Solaris or BSD. (Right now I'm not even *thinking* about Windows...)



---

archive/issue_comments_045594.json:
```json
{
    "body": "All tests pass (with -long) on my mac, on sage.math, and on an ubuntu machine.  Is this enough for a positive review, or do we need more people to test on other types of machines?",
    "created_at": "2009-05-20T14:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45594",
    "user": "@jhpalmieri"
}
```

All tests pass (with -long) on my mac, on sage.math, and on an ubuntu machine.  Is this enough for a positive review, or do we need more people to test on other types of machines?



---

archive/issue_comments_045595.json:
```json
{
    "body": "No luck on Solaris 10 with the standard find command:\n\n```\nbash-3.00$ ./sage -t -long devel/sage/sage/misc/sagedoc.py\nsage -t -long \"devel/sage/sage/misc/sagedoc.py\"             \ngrep: RE error 41: No remembered search string.\nfind: bad option -or\nfind: [-H | -L] path-list predicate-list\nfind: bad option -or\nfind: [-H | -L] path-list predicate-list\nfind: bad option -or\nfind: [-H | -L] path-list predicate-list\nfind: bad option -or\nfind: [-H | -L] path-list predicate-list\nfind: bad option -or\nfind: [-H | -L] path-list predicate-list\nfind: bad option -or\nfind: [-H | -L] path-list predicate-list\n\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.2/sage-3.4.2-mark-gcc-4.3.3/devel/sage/sage/misc/sagedoc.py\", line 373:\n    sage: len(search_src(\"matrix\", interact=False).splitlines()) > 10000 # long time\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_7\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T23:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45595",
    "user": "mabshoff"
}
```

No luck on Solaris 10 with the standard find command:

```
bash-3.00$ ./sage -t -long devel/sage/sage/misc/sagedoc.py
sage -t -long "devel/sage/sage/misc/sagedoc.py"             
grep: RE error 41: No remembered search string.
find: bad option -or
find: [-H | -L] path-list predicate-list
find: bad option -or
find: [-H | -L] path-list predicate-list
find: bad option -or
find: [-H | -L] path-list predicate-list
find: bad option -or
find: [-H | -L] path-list predicate-list
find: bad option -or
find: [-H | -L] path-list predicate-list
find: bad option -or
find: [-H | -L] path-list predicate-list

**********************************************************************
File "/home/mabshoff/build-3.4.2/sage-3.4.2-mark-gcc-4.3.3/devel/sage/sage/misc/sagedoc.py", line 373:
    sage: len(search_src("matrix", interact=False).splitlines()) > 10000 # long time
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_7
```


Cheers,

Michael



---

archive/issue_comments_045596.json:
```json
{
    "body": "Replying to [comment:24 mabshoff]:\n> No luck on Solaris 10 with the standard find command:\n\nWell, '-o' seems to work for everybody, so let's use that. I also refactored the `search_src` and `search_doc` functions since their code was basically a cut-and-paste. I added some better doctests too.\n\nWhen doctesting on sage.math, I started seeing the \"argument must be an int, or have a fileno() method\" error related to sending stuff to the pager, so I put in [comment:11 mpatel's suggestion] to hard-code the number of screen lines. If anyone has a better idea to work around that problem, or wants to patch the IPython sources, let me know.",
    "created_at": "2009-05-21T04:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45596",
    "user": "@dandrake"
}
```

Replying to [comment:24 mabshoff]:
> No luck on Solaris 10 with the standard find command:

Well, '-o' seems to work for everybody, so let's use that. I also refactored the `search_src` and `search_doc` functions since their code was basically a cut-and-paste. I added some better doctests too.

When doctesting on sage.math, I started seeing the "argument must be an int, or have a fileno() method" error related to sending stuff to the pager, so I put in [comment:11 mpatel's suggestion] to hard-code the number of screen lines. If anyone has a better idea to work around that problem, or wants to patch the IPython sources, let me know.



---

archive/issue_comments_045597.json:
```json
{
    "body": "Attachment [trac_5806-part2.patch](tarball://root/attachments/some-uuid/ticket5806/trac_5806-part2.patch) by @dandrake created at 2009-05-21 06:14:38\n\napply in addition to first patch; adds AUTHORS and removes nodoctest from sageinspect.py",
    "created_at": "2009-05-21T06:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45597",
    "user": "@dandrake"
}
```

Attachment [trac_5806-part2.patch](tarball://root/attachments/some-uuid/ticket5806/trac_5806-part2.patch) by @dandrake created at 2009-05-21 06:14:38

apply in addition to first patch; adds AUTHORS and removes nodoctest from sageinspect.py



---

archive/issue_comments_045598.json:
```json
{
    "body": "Looks good except for one doctest failure.  trac_5806_part3.patch should fix this.\n\nWith all three patches, I have no doctest failures on Mac OS X 10.5 and on sage.math.  People should test out other platforms, too.",
    "created_at": "2009-05-23T19:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45598",
    "user": "@jhpalmieri"
}
```

Looks good except for one doctest failure.  trac_5806_part3.patch should fix this.

With all three patches, I have no doctest failures on Mac OS X 10.5 and on sage.math.  People should test out other platforms, too.



---

archive/issue_comments_045599.json:
```json
{
    "body": "Replying to [comment:26 jhpalmieri]:\n> Looks good except for one doctest failure.  trac_5806_part3.patch should fix this.\n\nCan you say more about this doctest failure? I see in the part3 patch, you simply chop off most of the result...is this because of unavoidable inconsistencies between platforms? It took me a long time to get that doctest right and I'd like to see it stay if possible, even though it's perhaps a little too cute for its own good.",
    "created_at": "2009-05-26T03:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45599",
    "user": "@dandrake"
}
```

Replying to [comment:26 jhpalmieri]:
> Looks good except for one doctest failure.  trac_5806_part3.patch should fix this.

Can you say more about this doctest failure? I see in the part3 patch, you simply chop off most of the result...is this because of unavoidable inconsistencies between platforms? It took me a long time to get that doctest right and I'd like to see it stay if possible, even though it's perhaps a little too cute for its own good.



---

archive/issue_comments_045600.json:
```json
{
    "body": "With 'sage -t', all tests pass, but with 'sage -t -long', I get this:\n\n```\nsage -t -long \"devel/sage/sage/misc/sagedoc.py\"             \n**********************************************************************\nFile \"/Applications/sage/devel/sage/sage/misc/sagedoc.py\", line 466:\n    sage: print search_src('^ *sage[:] .*search_src(', interact=False) # long time\nExpected:\n    misc/sagedoc.py:        ... print search_src(\" fetch(\", \"def\", interact=False) # random # long time\n    misc/sagedoc.py:        ... print search_src(\" fetch(\", \"def\", \"pyx\", interact=False) # random # long time\n    misc/sagedoc.py:        ... print search_src('^ *sage[:] .*search_src(', interact=False) # long time\n    misc/sagedoc.py:        ... len(search_src(\"matrix\", interact=False).splitlines()) > 10000 # long time\n    misc/sagedoc.py:        ... print search_src('matrix', 'column', 'row', '0', 'sub', 'start', interact=False) # random # long time\nGot:\n    /misc/sagedoc.py:        sage: print search_src(\" fetch(\", \"def\", interact=False) # random # long time\n    /misc/sagedoc.py:        sage: print search_src(\" fetch(\", \"def\", \"pyx\", interact=False) # random # long time\n    /misc/sagedoc.py:        sage: print search_src('^ *sage[:] .*search_src(', interact=False) # long time\n    /misc/sagedoc.py:        sage: len(search_src(\"matrix\", interact=False).splitlines()) > 10000 # long time\n    /misc/sagedoc.py:        sage: print search_src('matrix', 'column', 'row', '0', 'sub', 'start', interact=False) # random # long time\n/misc/sagedoc.py:        sage: search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string\n/misc/sagedoc.py:        html/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_8\n```\n\nI thought that the ellipses were the problem, but now I see the missing slash at the beginning.  Here's a new version of the part 3 patch which you might be happier with.",
    "created_at": "2009-05-26T04:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45600",
    "user": "@jhpalmieri"
}
```

With 'sage -t', all tests pass, but with 'sage -t -long', I get this:

```
sage -t -long "devel/sage/sage/misc/sagedoc.py"             
**********************************************************************
File "/Applications/sage/devel/sage/sage/misc/sagedoc.py", line 466:
    sage: print search_src('^ *sage[:] .*search_src(', interact=False) # long time
Expected:
    misc/sagedoc.py:        ... print search_src(" fetch(", "def", interact=False) # random # long time
    misc/sagedoc.py:        ... print search_src(" fetch(", "def", "pyx", interact=False) # random # long time
    misc/sagedoc.py:        ... print search_src('^ *sage[:] .*search_src(', interact=False) # long time
    misc/sagedoc.py:        ... len(search_src("matrix", interact=False).splitlines()) > 10000 # long time
    misc/sagedoc.py:        ... print search_src('matrix', 'column', 'row', '0', 'sub', 'start', interact=False) # random # long time
Got:
    /misc/sagedoc.py:        sage: print search_src(" fetch(", "def", interact=False) # random # long time
    /misc/sagedoc.py:        sage: print search_src(" fetch(", "def", "pyx", interact=False) # random # long time
    /misc/sagedoc.py:        sage: print search_src('^ *sage[:] .*search_src(', interact=False) # long time
    /misc/sagedoc.py:        sage: len(search_src("matrix", interact=False).splitlines()) > 10000 # long time
    /misc/sagedoc.py:        sage: print search_src('matrix', 'column', 'row', '0', 'sub', 'start', interact=False) # random # long time
/misc/sagedoc.py:        sage: search_doc('this creates a polynomial ring') # random # this function has no output: it just prints a string
/misc/sagedoc.py:        html/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_8
```

I thought that the ellipses were the problem, but now I see the missing slash at the beginning.  Here's a new version of the part 3 patch which you might be happier with.



---

archive/issue_comments_045601.json:
```json
{
    "body": "I think this is OS specific, and maybe it has to do with the BSD-style find command on Mac OS X.  That is: with just your two patches, all tests pass on sage.math and on another linux box I have access to.  On my Intel Mac running OS X 10.5, I get the error listed above because of the leading slash \"/\".  Even worse, though, from the notebook interface, the links are broken, again because of the slash.  I think the right thing to do is to strip the leading slash if it's present.  Here's a patch which does that; it passes all tests on sage.math and on my mac.",
    "created_at": "2009-05-27T00:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45601",
    "user": "@jhpalmieri"
}
```

I think this is OS specific, and maybe it has to do with the BSD-style find command on Mac OS X.  That is: with just your two patches, all tests pass on sage.math and on another linux box I have access to.  On my Intel Mac running OS X 10.5, I get the error listed above because of the leading slash "/".  Even worse, though, from the notebook interface, the links are broken, again because of the slash.  I think the right thing to do is to strip the leading slash if it's present.  Here's a patch which does that; it passes all tests on sage.math and on my mac.



---

archive/issue_comments_045602.json:
```json
{
    "body": "Attachment [trac_5806-part3.patch](tarball://root/attachments/some-uuid/ticket5806/trac_5806-part3.patch) by @dandrake created at 2009-05-27 01:26:26\n\nReplying to [comment:29 jhpalmieri]:\n> I think this is OS specific, and maybe it has to do with the BSD-style find command on Mac OS X.  That is: with just your two patches, all tests pass on sage.math and on another linux box I have access to.  On my Intel Mac running OS X 10.5, I get the error listed above because of the leading slash \"/\".  Even worse, though, from the notebook interface, the links are broken, again because of the slash.  I think the right thing to do is to strip the leading slash if it's present.  Here's a patch which does that; it passes all tests on sage.math and on my mac.\n\nAh, perfect. Your patch3 passes doctests and works in the notebook on my own machine (amd64 Ubuntu, so no surprise there since it works on sage.math), and passes doctests on a 32-bit Fedora 10 machine.\n\nI did notice that `search_doc` was not actually searching the documentation...I was a little too quick with cut and paste. I'll upload a new version of the first patch (all I did was change a `'src'` to `'doc'`). Now we need to get someone to review this.",
    "created_at": "2009-05-27T01:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45602",
    "user": "@dandrake"
}
```

Attachment [trac_5806-part3.patch](tarball://root/attachments/some-uuid/ticket5806/trac_5806-part3.patch) by @dandrake created at 2009-05-27 01:26:26

Replying to [comment:29 jhpalmieri]:
> I think this is OS specific, and maybe it has to do with the BSD-style find command on Mac OS X.  That is: with just your two patches, all tests pass on sage.math and on another linux box I have access to.  On my Intel Mac running OS X 10.5, I get the error listed above because of the leading slash "/".  Even worse, though, from the notebook interface, the links are broken, again because of the slash.  I think the right thing to do is to strip the leading slash if it's present.  Here's a patch which does that; it passes all tests on sage.math and on my mac.

Ah, perfect. Your patch3 passes doctests and works in the notebook on my own machine (amd64 Ubuntu, so no surprise there since it works on sage.math), and passes doctests on a 32-bit Fedora 10 machine.

I did notice that `search_doc` was not actually searching the documentation...I was a little too quick with cut and paste. I'll upload a new version of the first patch (all I did was change a `'src'` to `'doc'`). Now we need to get someone to review this.



---

archive/issue_comments_045603.json:
```json
{
    "body": "Attachment [trac_5806.patch](tarball://root/attachments/some-uuid/ticket5806/trac_5806.patch) by @dandrake created at 2009-05-27 01:32:07",
    "created_at": "2009-05-27T01:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45603",
    "user": "@dandrake"
}
```

Attachment [trac_5806.patch](tarball://root/attachments/some-uuid/ticket5806/trac_5806.patch) by @dandrake created at 2009-05-27 01:32:07



---

archive/issue_comments_045604.json:
```json
{
    "body": "If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45604",
    "user": "@williamstein"
}
```

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_045605.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45605",
    "user": "@williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_045606.json:
```json
{
    "body": "Works for me on several different linux boxes as well as Mac OS X 10.5 (intel).  Apply all three patches.\n\n(I wrote one of the three patches, but it's a one-liner, and ddrake approved of it above (\"Ah, perfect\").  So positive review for the whole thing.)",
    "created_at": "2009-06-19T23:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45606",
    "user": "@jhpalmieri"
}
```

Works for me on several different linux boxes as well as Mac OS X 10.5 (intel).  Apply all three patches.

(I wrote one of the three patches, but it's a one-liner, and ddrake approved of it above ("Ah, perfect").  So positive review for the whole thing.)



---

archive/issue_comments_045607.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5806#issuecomment-45607",
    "user": "@rlmill"
}
```

Resolution: fixed
