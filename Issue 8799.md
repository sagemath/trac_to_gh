# Issue 8799: Bring doctests for mwrank.pyx up to 100% (from 3%)

archive/issues_008799.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @rlmill\n\nKeywords: mwrank\n\nImprove documentation for this:\n\n```\nsage/libs/mwrank/mwrank.pyx:  3% (1 of 30)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8799\n\n",
    "created_at": "2010-04-28T08:11:56Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Bring doctests for mwrank.pyx up to 100% (from 3%)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8799",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: mvngu

CC:  @rlmill

Keywords: mwrank

Improve documentation for this:

```
sage/libs/mwrank/mwrank.pyx:  3% (1 of 30)
```


Issue created by migration from https://trac.sagemath.org/ticket/8799





---

archive/issue_comments_080459.json:
```json
{
    "body": "I am working on this (started 2010-04-28) -- John",
    "created_at": "2010-04-28T20:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80459",
    "user": "https://github.com/JohnCremona"
}
```

I am working on this (started 2010-04-28) -- John



---

archive/issue_comments_080460.json:
```json
{
    "body": "The patch provides 100% doctests to sage/libs/mwrank (both files mwrank.pyx and interface.py), as well as adding them to the reference manual.\n\nThis is 95% in the docstrings, but I did find a few fairly minor bugs (mainly in the documentation not saying what various parameters did precisely).\n\nPatch up very soon -- just doing final testing.",
    "created_at": "2010-05-02T19:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80460",
    "user": "https://github.com/JohnCremona"
}
```

The patch provides 100% doctests to sage/libs/mwrank (both files mwrank.pyx and interface.py), as well as adding them to the reference manual.

This is 95% in the docstrings, but I did find a few fairly minor bugs (mainly in the documentation not saying what various parameters did precisely).

Patch up very soon -- just doing final testing.



---

archive/issue_comments_080461.json:
```json
{
    "body": "Applies to 4.4",
    "created_at": "2010-05-02T20:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80461",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.4



---

archive/issue_comments_080462.json:
```json
{
    "body": "Attachment [trac_8799-mwrank-doctest.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-mwrank-doctest.patch) by @JohnCremona created at 2010-05-02 20:01:50\n\nI am flagging this as \"needs review\", while still testing.  Not expecting any surprises since the patch is almost entirely in docstrings.  (I did also test the building of the docs).",
    "created_at": "2010-05-02T20:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80462",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8799-mwrank-doctest.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-mwrank-doctest.patch) by @JohnCremona created at 2010-05-02 20:01:50

I am flagging this as "needs review", while still testing.  Not expecting any surprises since the patch is almost entirely in docstrings.  (I did also test the building of the docs).



---

archive/issue_comments_080463.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-02T20:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80463",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080464.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> I am flagging this as \"needs review\", while still testing.  Not expecting any surprises since the patch is almost entirely in docstrings.  (I did also test the building of the docs).\n\nJust in case anyone reading the above thinks that this is not ready for testing & reviewing -- it is!",
    "created_at": "2010-05-09T21:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80464",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 cremona]:
> I am flagging this as "needs review", while still testing.  Not expecting any surprises since the patch is almost entirely in docstrings.  (I did also test the building of the docs).

Just in case anyone reading the above thinks that this is not ready for testing & reviewing -- it is!



---

archive/issue_comments_080465.json:
```json
{
    "body": "Attachment [trac_8799-reviewer.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer.patch) by mvngu created at 2010-05-10 11:36:43\n\nbased on Sage 4.4.2.alpha0",
    "created_at": "2010-05-10T11:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8799-reviewer.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer.patch) by mvngu created at 2010-05-10 11:36:43

based on Sage 4.4.2.alpha0



---

archive/issue_comments_080466.json:
```json
{
    "body": "With the patch [trac_8799-mwrank-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-mwrank-doctest.patch), I got the following failures on sage.math:\n\n\n```\n[mvngu@sage sage-4.4.2.alpha0-8799-mwrank-doctest]$ ./sage -t -long devel/sage-main/sage/libs/mwrank/mwrank.pyx\nsage -t -long \"devel/sage-main/sage/libs/mwrank/mwrank.pyx\" \n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8799-mwrank-doctest/devel/sage-main/sage/libs/mwrank/mwrank.pyx\", line 428:\n    sage: E.discriminant()\nExpected:\n    -1269581104000000L\nGot:\n    -1269581104000000\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8799-mwrank-doctest/devel/sage-main/sage/libs/mwrank/mwrank.pyx\", line 455:\n    sage: E.conductor()\nExpected:\n    126958110400L\nGot:\n    126958110400\nP1 = [0:1:0]\t is torsion point, order 1\nP1 = [-3:0:1]\t  is generator number 1\nsaturating up to 20...Checking 2-saturation \n\n<output truncated>\n\nSearching for points (bound = 8)...done:\n  found points of rank 3\n  and regulator 0.41714355875838396981711954461809339674981010609846\nProcessing points found during 2-descent...done:\n  now regulator = 0.41714355875838396981711954461809339674981010609846\nNo saturation being done\n```\n\n\nThe reviewer patch fix this issue and a bunch of typos. What we need now is someone to review the technical aspect of John's patch. Unfortunately, I'm not at all familiar with elliptic curves.",
    "created_at": "2010-05-10T11:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

With the patch [trac_8799-mwrank-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-mwrank-doctest.patch), I got the following failures on sage.math:


```
[mvngu@sage sage-4.4.2.alpha0-8799-mwrank-doctest]$ ./sage -t -long devel/sage-main/sage/libs/mwrank/mwrank.pyx
sage -t -long "devel/sage-main/sage/libs/mwrank/mwrank.pyx" 
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8799-mwrank-doctest/devel/sage-main/sage/libs/mwrank/mwrank.pyx", line 428:
    sage: E.discriminant()
Expected:
    -1269581104000000L
Got:
    -1269581104000000
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8799-mwrank-doctest/devel/sage-main/sage/libs/mwrank/mwrank.pyx", line 455:
    sage: E.conductor()
Expected:
    126958110400L
Got:
    126958110400
P1 = [0:1:0]	 is torsion point, order 1
P1 = [-3:0:1]	  is generator number 1
saturating up to 20...Checking 2-saturation 

<output truncated>

Searching for points (bound = 8)...done:
  found points of rank 3
  and regulator 0.41714355875838396981711954461809339674981010609846
Processing points found during 2-descent...done:
  now regulator = 0.41714355875838396981711954461809339674981010609846
No saturation being done
```


The reviewer patch fix this issue and a bunch of typos. What we need now is someone to review the technical aspect of John's patch. Unfortunately, I'm not at all familiar with elliptic curves.



---

archive/issue_comments_080467.json:
```json
{
    "body": "Many thanks for the reviewer patch, and many many apologies for all those typose & other things which I missed converting from old-style docstring format to ReST.\n\nFor info:  the removal of the trailing L on those output constants is correct:  I converted various integers in the output to Sage integers (they were python ints).\n\nI CC'd rlm, hoping that he'll be able to look at this too.",
    "created_at": "2010-05-10T16:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80467",
    "user": "https://github.com/JohnCremona"
}
```

Many thanks for the reviewer patch, and many many apologies for all those typose & other things which I missed converting from old-style docstring format to ReST.

For info:  the removal of the trailing L on those output constants is correct:  I converted various integers in the output to Sage integers (they were python ints).

I CC'd rlm, hoping that he'll be able to look at this too.



---

archive/issue_comments_080468.json:
```json
{
    "body": "Hmm, what's the convention for typesetting numbers, isolated or e.g. in *2-descent*?\n\nMath mode looks very ugly (and isn't consistently used).\n\nAlso, *Python* should be uppercase, and *Sha* should be *SHA* I guess.\n\nThere are also some (non-)references e.g. to *2-descent* where I guess `:meth:`two_descent`` should be used.\n\nBtw, both patches work for 4.4.1.rc0 (which is almost 4.4.1), too, and doctests pass.\nI only get an error when building PDF documentation, due to some reference with an underscore(?), haven't yet closely looked at that.\n\n-Leif",
    "created_at": "2010-05-10T17:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80468",
    "user": "https://github.com/nexttime"
}
```

Hmm, what's the convention for typesetting numbers, isolated or e.g. in *2-descent*?

Math mode looks very ugly (and isn't consistently used).

Also, *Python* should be uppercase, and *Sha* should be *SHA* I guess.

There are also some (non-)references e.g. to *2-descent* where I guess `:meth:`two_descent`` should be used.

Btw, both patches work for 4.4.1.rc0 (which is almost 4.4.1), too, and doctests pass.
I only get an error when building PDF documentation, due to some reference with an underscore(?), haven't yet closely looked at that.

-Leif



---

archive/issue_comments_080469.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> I only get an error when building PDF documentation, due to some reference with an underscore(?), haven't yet closely looked at that.\n\nSorry, perhaps completely unrelated to *this* patch/ticket.",
    "created_at": "2010-05-10T17:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80469",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:7 leif]:
> I only get an error when building PDF documentation, due to some reference with an underscore(?), haven't yet closely looked at that.

Sorry, perhaps completely unrelated to *this* patch/ticket.



---

archive/issue_comments_080470.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> Also, ..[...] *Sha* should be *SHA* I guess.\n\nOuch, it's actually the cyrillic Sha. :)\n\nSorry again.",
    "created_at": "2010-05-10T17:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80470",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:7 leif]:
> Also, ..[...] *Sha* should be *SHA* I guess.

Ouch, it's actually the cyrillic Sha. :)

Sorry again.



---

archive/issue_comments_080471.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> Replying to [comment:7 leif]:\n> > Also, ..[...] *Sha* should be *SHA* I guess.\n> \n> Ouch, it's actually the cyrillic Sha. :)\n\nThat's right.  I don't know if we can access such fonts in the docs.  I think the other inconsistencies have been dealt with by Minh.\n\n   John\n\n> Sorry again.",
    "created_at": "2010-05-10T17:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80471",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:9 leif]:
> Replying to [comment:7 leif]:
> > Also, ..[...] *Sha* should be *SHA* I guess.
> 
> Ouch, it's actually the cyrillic Sha. :)

That's right.  I don't know if we can access such fonts in the docs.  I think the other inconsistencies have been dealt with by Minh.

   John

> Sorry again.



---

archive/issue_comments_080472.json:
```json
{
    "body": "Replying to [comment:10 cremona]:\n> I think the other inconsistencies have been dealt with by Minh.\nNo, not really. Minh introduced *some* math-typeset numbers - isolated and within words (but did not change all occurrences), and did not \"change\" all method references.\n\nThere's also some reference to Python's (deprecated) `long`.\n\nThe typesetting of Python (variable) names (and e.g. *true* instead of `True`) is not fully consistent, too.\n\n(The return value descriptions use both passive and imperative form, too. ;-) )\n\nBut I don't want to grumble to much...",
    "created_at": "2010-05-10T18:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80472",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:10 cremona]:
> I think the other inconsistencies have been dealt with by Minh.
No, not really. Minh introduced *some* math-typeset numbers - isolated and within words (but did not change all occurrences), and did not "change" all method references.

There's also some reference to Python's (deprecated) `long`.

The typesetting of Python (variable) names (and e.g. *true* instead of `True`) is not fully consistent, too.

(The return value descriptions use both passive and imperative form, too. ;-) )

But I don't want to grumble to much...



---

archive/issue_comments_080473.json:
```json
{
    "body": "Feel free to add a second reviewer's patch!",
    "created_at": "2010-05-10T19:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80473",
    "user": "https://github.com/JohnCremona"
}
```

Feel free to add a second reviewer's patch!



---

archive/issue_comments_080474.json:
```json
{
    "body": "Attachment [trac_8799-reviewer_too.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer_too.patch) by @nexttime created at 2010-05-10 23:08:32\n\nA (rough) second reviewer patch based on Minh's.",
    "created_at": "2010-05-10T23:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80474",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8799-reviewer_too.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer_too.patch) by @nexttime created at 2010-05-10 23:08:32

A (rough) second reviewer patch based on Minh's.



---

archive/issue_comments_080475.json:
```json
{
    "body": "Better first look at the diff (before applying the patch); I've changed various things (including a typo in the actual code), but haven't reverted anything Minh changed (at least I think so), i.e. math-typeset numbers etc. still look ugly. ;-)\n\nI've (yet) changed little in `mwrank.pyx`, because I can't find documentation generated from anything but the two pure Python functions... ;-)\n\n-Leif\n\nP.S.: Minh, the prev/next topic for me doesn't work as expected... 8|",
    "created_at": "2010-05-10T23:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80475",
    "user": "https://github.com/nexttime"
}
```

Better first look at the diff (before applying the patch); I've changed various things (including a typo in the actual code), but haven't reverted anything Minh changed (at least I think so), i.e. math-typeset numbers etc. still look ugly. ;-)

I've (yet) changed little in `mwrank.pyx`, because I can't find documentation generated from anything but the two pure Python functions... ;-)

-Leif

P.S.: Minh, the prev/next topic for me doesn't work as expected... 8|



---

archive/issue_comments_080476.json:
```json
{
    "body": "P.P.S.: John, I've also added some `TODO`s. Btw, do we initialise or initialize? ;-)",
    "created_at": "2010-05-10T23:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80476",
    "user": "https://github.com/nexttime"
}
```

P.P.S.: John, I've also added some `TODO`s. Btw, do we initialise or initialize? ;-)



---

archive/issue_comments_080477.json:
```json
{
    "body": "Attachment [trac_8799-reviewer-part3.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer-part3.patch) by mvngu created at 2010-05-11 01:00:35\n\nI have made some more changes to the docstring of `interface.py` and `mwrank.pyx`. My second reviewer patch [trac_8799-reviewer-part3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-part3.patch) includes changes in addition to the original reviewer patch and leif's patch. With many patches to apply, it can be confusing to see what changes the reviewers propose. So I have folded the reviewers' patches into one mega patch called [trac_8799-reviewer-total.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-total.patch).\n\n\n\nAlso notice that I move documentation for constructor methods, i.e. `__init__`, into the docstring of a class. The main reason is that, currently the docstring of `__init__` don't show up on the reference manual once you built it. \n\n\n\nTo rebuild the whole reference manual, you could do the following from `SAGE_ROOT`, assuming you applied the patches to the branch main:\n\n\n```sh\n./sage -b main\n./sage -docbuild reference html\n```\n\n\nIf you want to be thorough and want to check that the new documentation build OK, do:\n\n\n```sh\nrm -rf devel/sage-main/doc/output/\n./sage -b main\n./sage -docbuild reference html\n```\n",
    "created_at": "2010-05-11T01:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8799-reviewer-part3.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer-part3.patch) by mvngu created at 2010-05-11 01:00:35

I have made some more changes to the docstring of `interface.py` and `mwrank.pyx`. My second reviewer patch [trac_8799-reviewer-part3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-part3.patch) includes changes in addition to the original reviewer patch and leif's patch. With many patches to apply, it can be confusing to see what changes the reviewers propose. So I have folded the reviewers' patches into one mega patch called [trac_8799-reviewer-total.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-total.patch).



Also notice that I move documentation for constructor methods, i.e. `__init__`, into the docstring of a class. The main reason is that, currently the docstring of `__init__` don't show up on the reference manual once you built it. 



To rebuild the whole reference manual, you could do the following from `SAGE_ROOT`, assuming you applied the patches to the branch main:


```sh
./sage -b main
./sage -docbuild reference html
```


If you want to be thorough and want to check that the new documentation build OK, do:


```sh
rm -rf devel/sage-main/doc/output/
./sage -b main
./sage -docbuild reference html
```




---

archive/issue_comments_080478.json:
```json
{
    "body": "4th reviewer patch on top of Minh' second (-part3). Fixes 1 doctest failure, too.",
    "created_at": "2010-05-11T02:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80478",
    "user": "https://github.com/nexttime"
}
```

4th reviewer patch on top of Minh' second (-part3). Fixes 1 doctest failure, too.



---

archive/issue_comments_080479.json:
```json
{
    "body": "Attachment [trac_8799-reviewer-part4.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer-part4.patch) by @nexttime created at 2010-05-11 02:41:42\n\nSorry, yet another patch. (It also fixes a doctest failure **introduced by me**. 8/ )\n\nMinh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)\n\nShouldn't we replace\n\n```\n - foo (bool) -- ...\n - bar (int, default 12) -- ...\n```\n\nby\n\n```\n - foo (:class:`bool`) -- ...\n - bar (:class:`int`, default 12) -- ...\n```\n\ntoo?\n\n-Leif\n\nP.S.: Note that despite the ticket title, my patches also change the code.",
    "created_at": "2010-05-11T02:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80479",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8799-reviewer-part4.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer-part4.patch) by @nexttime created at 2010-05-11 02:41:42

Sorry, yet another patch. (It also fixes a doctest failure **introduced by me**. 8/ )

Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)

Shouldn't we replace

```
 - foo (bool) -- ...
 - bar (int, default 12) -- ...
```

by

```
 - foo (:class:`bool`) -- ...
 - bar (:class:`int`, default 12) -- ...
```

too?

-Leif

P.S.: Note that despite the ticket title, my patches also change the code.



---

archive/issue_comments_080480.json:
```json
{
    "body": "cumulative of all reviewers' patches",
    "created_at": "2010-05-11T03:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80480",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

cumulative of all reviewers' patches



---

archive/issue_comments_080481.json:
```json
{
    "body": "Attachment [trac_8799-reviewer-total.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer-total.patch) by mvngu created at 2010-05-11 03:55:08\n\nReplying to [comment:16 leif]:\n> Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)\n\nI'm not particularly picky about this issue. What you proposed in your patches are OK by me. I have folded all our reviewer patches into one cumulative patch. Even your second reviewer patch has been folded into [trac_8799-reviewer-total.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-total.patch).\n\n\n\n\n> Shouldn't we replace\n\n```\n- foo (bool) -- ...\n- bar (int, default 12) -- ...\n```\n\n> by\n\n```\n- foo (:class:`bool`) -- ...\n- bar (:class:`int`, default 12) -- ...\n```\n\n> too?\n\nThat is OK by me. But I would prefer something like \"boolean\", \"integer\", \"real number\", etc. Something as \"meaningful\" as possible, without recourse to type information. We now need someone to review the technical (mathematical) aspect of John's patch, and a sign off on my review patch. I'm OK with your patches. That is, someone other than myself need to look over the cumulative reviewer patch.",
    "created_at": "2010-05-11T03:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80481",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8799-reviewer-total.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-reviewer-total.patch) by mvngu created at 2010-05-11 03:55:08

Replying to [comment:16 leif]:
> Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)

I'm not particularly picky about this issue. What you proposed in your patches are OK by me. I have folded all our reviewer patches into one cumulative patch. Even your second reviewer patch has been folded into [trac_8799-reviewer-total.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-total.patch).




> Shouldn't we replace

```
- foo (bool) -- ...
- bar (int, default 12) -- ...
```

> by

```
- foo (:class:`bool`) -- ...
- bar (:class:`int`, default 12) -- ...
```

> too?

That is OK by me. But I would prefer something like "boolean", "integer", "real number", etc. Something as "meaningful" as possible, without recourse to type information. We now need someone to review the technical (mathematical) aspect of John's patch, and a sign off on my review patch. I'm OK with your patches. That is, someone other than myself need to look over the cumulative reviewer patch.



---

archive/issue_comments_080482.json:
```json
{
    "body": "Replying to [comment:17 mvngu]:\n> Replying to [comment:16 leif]:\n> > Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)\n> \n> I'm not particularly picky about this issue. What you proposed in your patches are OK by me.\nWell, I haven't reverted your changes of e.g. `1` to ``1``; the HTML output is not very nice...\n\n> I have folded all our reviewer patches into one cumulative patch.\nYes, of course noticed that.\n\n> I would prefer something like \"boolean\", \"integer\", \"real number\", etc. Something as \"meaningful\" as possible, without recourse to type information.\nThis might not sound pythonic, but I'd prefer documenting the concrete type if the function actually expects some Python type (rather than a duck).\n\n> We now need someone to review the technical (mathematical) aspect of John's patch,\nrlm?\n\n> and a sign off on my review patch.\nI've positively reviewed *your* changes... :)\n\nSo unfortunately someone else (other than John and us) has to review the cumulative reviewer patch to avoid mutual peer-reviewing on the same ticket (some people seem to have no problems with this, I do).",
    "created_at": "2010-05-11T04:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80482",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:17 mvngu]:
> Replying to [comment:16 leif]:
> > Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)
> 
> I'm not particularly picky about this issue. What you proposed in your patches are OK by me.
Well, I haven't reverted your changes of e.g. `1` to ``1``; the HTML output is not very nice...

> I have folded all our reviewer patches into one cumulative patch.
Yes, of course noticed that.

> I would prefer something like "boolean", "integer", "real number", etc. Something as "meaningful" as possible, without recourse to type information.
This might not sound pythonic, but I'd prefer documenting the concrete type if the function actually expects some Python type (rather than a duck).

> We now need someone to review the technical (mathematical) aspect of John's patch,
rlm?

> and a sign off on my review patch.
I've positively reviewed *your* changes... :)

So unfortunately someone else (other than John and us) has to review the cumulative reviewer patch to avoid mutual peer-reviewing on the same ticket (some people seem to have no problems with this, I do).



---

archive/issue_comments_080483.json:
```json
{
    "body": "Changing assignee from mvngu to @JohnCremona.",
    "created_at": "2010-05-11T08:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80483",
    "user": "https://github.com/JohnCremona"
}
```

Changing assignee from mvngu to @JohnCremona.



---

archive/issue_comments_080484.json:
```json
{
    "body": "For what it's worth, thanks again to both, and I am quite happy with the combined reviewer patch (trac_8799-reviewer-total.patch).\n\nI did not see the typo in the code which Leif mentioned.  Is it where we test height_bound > 21.4 and not 21.48?  In that place, it is true that this could be approximately doubled on 64-bit machines (I guess that when this code was first written the person doing it did not know how to test that) but in practice using bounds > 21 will take a very very long time.\n\nSo we still need an independent reviewer... and some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?",
    "created_at": "2010-05-11T08:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80484",
    "user": "https://github.com/JohnCremona"
}
```

For what it's worth, thanks again to both, and I am quite happy with the combined reviewer patch (trac_8799-reviewer-total.patch).

I did not see the typo in the code which Leif mentioned.  Is it where we test height_bound > 21.4 and not 21.48?  In that place, it is true that this could be approximately doubled on 64-bit machines (I guess that when this code was first written the person doing it did not know how to test that) but in practice using bounds > 21 will take a very very long time.

So we still need an independent reviewer... and some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?



---

archive/issue_comments_080485.json:
```json
{
    "body": "Replying to [comment:19 cremona]:\n> I did not see the typo in the code which Leif mentioned.  Is it where we test height_bound > 21.4 and not 21.48?\nNo. I meant:\n\n```\n-        verbose == bool(verbose)\n+        verbose = bool(verbose)\n```\n\n> In that place, it is true that this could be approximately doubled on 64-bit machines (I guess that when this code was first written the person doing it did not know how to test that) but in practice using bounds > 21 will take a very very long time.\nIt's just that the implementation doesn't meet the documentation:\n\n```\n        - ``height_limit`` (float, default: 18) -- search up to this\n          logarithmic height.\n\n        .. note::\n        \n          On 32-bit machines, this *must* be < 21.48 else\n          `\\exp(h_{\\text{lim}}) > 2^{31}` and overflows.  On 64-bit machines, it\n          must be *at most* 43.668.  However, this bound is a logarithmic\n          bound and increasing it by just 1 increases the running time\n          by (roughly) `\\exp(1.5)=4.5`, so searching up to even 20\n          takes a very long time.\n```\n\n(We could add here that larger heights for 64-bit code currently aren't implemented in the Python interface.) \n\n```\n        height_limit = float(height_limit)\n        if height_limit >= 21.4:\t# TODO: docstring says 21.48 (for 32-bit machines; what about 64-bit...?)\n            raise ValueError, \"The height limit must be < 21.4.\"\n```\n\nAlso, if the docstring says `21.48`, the code should use the same value.\n\n(Note that the code should check for what machine the code/`mwrank` was compiled for, not what machine Sage is currently running on...)\n\nBut that (change of the implementation, and perhaps other TODOs, like in `mwrank_EllipticCurve.__repr__()`) should be fixed on another ticket.\n\n\n\n> [...] some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?\nDefinitely. :)\n\n-Leif",
    "created_at": "2010-05-12T17:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80485",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:19 cremona]:
> I did not see the typo in the code which Leif mentioned.  Is it where we test height_bound > 21.4 and not 21.48?
No. I meant:

```
-        verbose == bool(verbose)
+        verbose = bool(verbose)
```

> In that place, it is true that this could be approximately doubled on 64-bit machines (I guess that when this code was first written the person doing it did not know how to test that) but in practice using bounds > 21 will take a very very long time.
It's just that the implementation doesn't meet the documentation:

```
        - ``height_limit`` (float, default: 18) -- search up to this
          logarithmic height.

        .. note::
        
          On 32-bit machines, this *must* be < 21.48 else
          `\exp(h_{\text{lim}}) > 2^{31}` and overflows.  On 64-bit machines, it
          must be *at most* 43.668.  However, this bound is a logarithmic
          bound and increasing it by just 1 increases the running time
          by (roughly) `\exp(1.5)=4.5`, so searching up to even 20
          takes a very long time.
```

(We could add here that larger heights for 64-bit code currently aren't implemented in the Python interface.) 

```
        height_limit = float(height_limit)
        if height_limit >= 21.4:	# TODO: docstring says 21.48 (for 32-bit machines; what about 64-bit...?)
            raise ValueError, "The height limit must be < 21.4."
```

Also, if the docstring says `21.48`, the code should use the same value.

(Note that the code should check for what machine the code/`mwrank` was compiled for, not what machine Sage is currently running on...)

But that (change of the implementation, and perhaps other TODOs, like in `mwrank_EllipticCurve.__repr__()`) should be fixed on another ticket.



> [...] some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?
Definitely. :)

-Leif



---

archive/issue_comments_080486.json:
```json
{
    "body": "Replying to [comment:19 cremona]:\n> [...] some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?\n\nI've opened a ticket for that at http://trac.sagemath.org/sage_trac/ticket/8958.",
    "created_at": "2010-05-12T23:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80486",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:19 cremona]:
> [...] some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?

I've opened a ticket for that at http://trac.sagemath.org/sage_trac/ticket/8958.



---

archive/issue_comments_080487.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-15T17:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80487",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080488.json:
```json
{
    "body": "I just checked that the patches apply fine to 4.4.2.rc0 (they do) and did a full make ptest.\n\nThis reveals a small problem in sage/libs/mwrank.pyx:  The reviewer patch removes two L suffixes from the output of E.discriminant() and E.conductor(), on long python ints.  I think this must be 32/64-bit dependent.  The best soution (surely) is to make those functions return Sage integers in the first place.  I will add that.\n\nIn the mean time I have put this back to \"need work\", realising that it has missged the boat for 4.4.2 anyway...",
    "created_at": "2010-05-15T17:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80488",
    "user": "https://github.com/JohnCremona"
}
```

I just checked that the patches apply fine to 4.4.2.rc0 (they do) and did a full make ptest.

This reveals a small problem in sage/libs/mwrank.pyx:  The reviewer patch removes two L suffixes from the output of E.discriminant() and E.conductor(), on long python ints.  I think this must be 32/64-bit dependent.  The best soution (surely) is to make those functions return Sage integers in the first place.  I will add that.

In the mean time I have put this back to "need work", realising that it has missged the boat for 4.4.2 anyway...



---

archive/issue_comments_080489.json:
```json
{
    "body": "Replying to [comment:22 cremona]:\n> In the mean time I have put this back to \"need work\", realising that it has missged the boat for 4.4.2 anyway...\n\nmvngu wrote:\n> From hereon, only critical fixes would be merged. **Fixes for documentation could also be merged.**\n\n;-)",
    "created_at": "2010-05-15T17:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80489",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:22 cremona]:
> In the mean time I have put this back to "need work", realising that it has missged the boat for 4.4.2 anyway...

mvngu wrote:
> From hereon, only critical fixes would be merged. **Fixes for documentation could also be merged.**

;-)



---

archive/issue_comments_080490.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> Replying to [comment:22 cremona]:\n> > In the mean time I have put this back to \"need work\", realising that it has missged the boat for 4.4.2 anyway...\n> \n> mvngu wrote:\n> > From hereon, only critical fixes would be merged. **Fixes for documentation could also be merged.**\n> \n> ;-)\n\nI know (and with that in mind I asked a couple of people of they would step in) but now I am suggesting a non-docstring change...",
    "created_at": "2010-05-15T19:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80490",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:23 leif]:
> Replying to [comment:22 cremona]:
> > In the mean time I have put this back to "need work", realising that it has missged the boat for 4.4.2 anyway...
> 
> mvngu wrote:
> > From hereon, only critical fixes would be merged. **Fixes for documentation could also be merged.**
> 
> ;-)

I know (and with that in mind I asked a couple of people of they would step in) but now I am suggesting a non-docstring change...



---

archive/issue_comments_080491.json:
```json
{
    "body": "Attachment [trac_8799-extra.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-extra.patch) by @JohnCremona created at 2010-05-15 19:49:15\n\nAdditional small fixes",
    "created_at": "2010-05-15T19:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80491",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8799-extra.patch](tarball://root/attachments/some-uuid/ticket8799/trac_8799-extra.patch) by @JohnCremona created at 2010-05-15 19:49:15

Additional small fixes



---

archive/issue_comments_080492.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-15T19:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80492",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080493.json:
```json
{
    "body": "The final patch trac_8799-extra.patch fixes the issues raised by returning python ints (which display differently on 32 and 64 bit machines): the return types are Sage Integers, which is better anyway.",
    "created_at": "2010-05-15T19:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80493",
    "user": "https://github.com/JohnCremona"
}
```

The final patch trac_8799-extra.patch fixes the issues raised by returning python ints (which display differently on 32 and 64 bit machines): the return types are Sage Integers, which is better anyway.



---

archive/issue_comments_080494.json:
```json
{
    "body": "The code looks fine, the patch applies and builds fine, the reference manual builds with no warnings, and all doctests pass. Positive review.",
    "created_at": "2010-05-16T12:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80494",
    "user": "https://github.com/loefflerd"
}
```

The code looks fine, the patch applies and builds fine, the reference manual builds with no warnings, and all doctests pass. Positive review.



---

archive/issue_comments_080495.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-16T12:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80495",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008964.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T08:41:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8799#event-8964"
}
```



---

archive/issue_comments_080496.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8799#issuecomment-80496",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
