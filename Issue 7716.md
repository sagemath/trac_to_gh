# Issue 7716: sage -coverage enhancement

Issue created by migration from https://trac.sagemath.org/ticket/7716

Original creator: roed

Original creation time: 2009-12-17 01:39:31

Assignee: mvngu

Keywords: coverage

Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.
- adds option to check cdef'd functions
- adds option to check docstrings on classes
- adds option to check for the existence of INPUT block
- adds option to check that parameters are all listed in the INPUT block.
- adds option to check for the existence of OUTPUT block

So that we don't bring our coverage level way down, these aren't turned on automatically.  Instead, they can be invoked from the command line by using options ( -cdefs, -classes, -input, -output and -params)


---

Comment by roed created at 2009-12-17 01:45:15

Changing status from new to needs_review.


---

Comment by novoselt created at 2009-12-17 17:02:10

What if a function does not return anything, but uses "return" to exit from the function in the middle? From looking at the patch it seems to me that it will be reported as "bad".


---

Comment by cremona created at 2009-12-17 17:04:00

Looks very useful -- but for me it would not apply to a fresh clone of 4.3.rc0.


---

Comment by jhpalmieri created at 2009-12-17 21:15:23

Overall looks good.  A few comments: It doesn't look like this will detect Sphinx/reST markup for input and output, as described [here](http://sagemath.org/doc/developer/conventions.html#documentation-strings) -- a block like

```
:param x: the length of the rectangle
:type x: float
:param w: the width of the rectangle
:type w: float
:return: the area of the rectange
:rtype: float
```

Or am I missing something?

Also, as I've said on #4323, it takes a certain amount of hubris, or maybe (as mabshoff pointed out) just a strong sense of irony, to put functions with no docstrings into a file like "sage-coverage".

Finally, I couldn't get it to apply cleanly, either.  When applying to the scripts repository in 4.3.rc0, I got the message

```
applying /Users/palmieri/Downloads/7716_coverage.patch
patching file sage-coverage
Hunk #2 FAILED at 15
1 out of 3 hunks FAILED -- saving rejects to file sage-coverage.rej
```



---

Comment by roed created at 2009-12-18 00:47:10

New patch, which should address all the concerns so far (and apply against 4.3.rc0 in particular)


---

Comment by roed created at 2009-12-19 18:55:09

Changes behavior for functions with underscores beginning and ending the name.  Apply on top of previous patch.


---

Attachment

I'm declaring a total feature freeze on sage-4.3.


---

Comment by was created at 2009-12-31 16:46:36

Fails to apply to sage-4.3:

```
wstein@boxen:~/build/referee/sage-4.3/local/bin$ hgimport http://trac.sagemath.org/sage_trac/attachment/ticket/7716/7716_coverage.patch
--08:41:18--  http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7716/7716_coverage.patch
           => `7716_coverage.patch'
Resolving trac.sagemath.org... 128.208.160.197
Connecting to trac.sagemath.org|128.208.160.197|:80... connected.
HTTP request sent, awaiting response... 200 Ok
Length: 58,082 (57K) [text/x-diff]

100%[====================================================================>] 58,082        --.--K/s             

08:41:18 (220.36 MB/s) - `7716_coverage.patch' saved [58082/58082]

applying 7716_coverage.patch
patching file sage-coverage
Hunk #2 FAILED at 15
1 out of 3 hunks FAILED -- saving rejects to file sage-coverage.rej
patching file sage-coverage
Hunk #1 FAILED at 0
Hunk #4 FAILED at 622
2 out of 4 hunks FAILED -- saving rejects to file sage-coverage.rej
patching file sage-coverageall
Hunk #1 FAILED at 0
Hunk #2 FAILED at 22
Hunk #3 FAILED at 38
3 out of 3 hunks FAILED -- saving rejects to file sage-coverageall.rej
abort: patch failed to apply
```


Maybe the patch is broken/corrupt?  It starts

```
# HG changeset patch
# User David Roe <roed@math.harvard.edu>
# Date 1261014209 18000
# Node ID da454b36cda7a92a4cbee40317e86f970a04dd8e
# Parent  e4aff87d1aa188834f14c6f4643beff69879512f
Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
...
```

then line 604 is suddenly:

```
# HG changeset patch
# User David Roe <roed@math.harvard.edu>
# Date 1261014209 18000
# Node ID e5314d3c2ba2b0ec34d8226ee80db4526a8a5678
# Parent  2c17a7cee6e7b76fe67053f34c20ed7c6c33d7cb
Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.
...
```


which involves exactly the same changeset comment and changes to the same file (sage-coverage).

Anyway, I'm pretty confused by this, and can't even referee it.


---

Comment by was created at 2009-12-31 16:46:36

Changing status from needs_review to needs_work.


---

Attachment

Yeah, I don't know what that was.  Here's a new patch (against 4.3.rc0) that gets rid of the weird double header problem.  7716_coverage.patch should be applied first, then 7716_underscores.patch

It doesn't need to be rebased against 4.3, since there are no changes to sage-coverage or sage-coverageall since 4.3.rc0.  William, are you up for reviewing this now that it should apply?


---

Comment by roed created at 2010-01-01 00:34:20

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-09-19 21:47:25

Some issues:

 - sage-coverageall doesn't deal with unrecognized options well, since it just parses the output from sage-coverage.  So if you pass an unrecognized option, it ends up saying "No files in ...".  Instead of doing

```
    r = os.popen('sage -coverage %s * | grep SCORE'%opt).readlines()
```

 we should probably set P to be the process and check its return status before asking for its output.

 - the options should work with either one or two hyphens.

 - We should have a "--help" option for sage-coverage which does the same thing as running sage-coverage with no arguments: print the usage.  I think we should also expand this usage message.

I'm attaching a "diff" which makes these changes.  I haven't looked at the rest of the code in detail yet, but I may soon.


---

Attachment

apply on top of other patches


---

Comment by roed created at 2012-03-02 23:29:34

Another change to sage-coverage that I want to request (and possibly implement later): it should be able to run on .pxi files.


---

Comment by tscrim created at 2013-02-06 12:58:47

Also #14061 seems to have fixed #8699.


---

Comment by roed created at 2013-02-17 20:45:41

Changing status from needs_review to needs_work.


---

Comment by roed created at 2013-02-17 20:45:41

This should be rebased to #14061, which will take some work.
