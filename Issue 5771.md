# Issue 5771: [with patch, positive review] %latex should issue a warning if latex isn't installed on the system

archive/issues_005771.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @rbeezer\n\nRight now on sagenb latex is not installed. So when someone evaluates a %latex cell, i.e. someone == Bill Hart, it just hangs:\n\n```\nmabshoff@sagenb:~$ latex\nThe program 'latex' is currently not installed.  You can install it by typing:\nsudo apt-get install texlive-latex-base\n-bash: latex: command not found\nmabshoff@sagenb:~$ echo $?\n127\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5771\n\n",
    "closed_at": "2009-06-13T21:44:11Z",
    "created_at": "2009-04-13T03:21:10Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, positive review] %latex should issue a warning if latex isn't installed on the system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5771",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @jhpalmieri

CC:  @rbeezer

Right now on sagenb latex is not installed. So when someone evaluates a %latex cell, i.e. someone == Bill Hart, it just hangs:

```
mabshoff@sagenb:~$ latex
The program 'latex' is currently not installed.  You can install it by typing:
sudo apt-get install texlive-latex-base
-bash: latex: command not found
mabshoff@sagenb:~$ echo $?
127
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5771





---

archive/issue_comments_045050.json:
```json
{
    "body": "just an fyi, i just issued the command on sagenb.org to install latex, so it will be there soon...",
    "created_at": "2009-04-13T14:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45050",
    "user": "https://github.com/williamstein"
}
```

just an fyi, i just issued the command on sagenb.org to install latex, so it will be there soon...



---

archive/issue_comments_045051.json:
```json
{
    "body": "Changing assignee from cwitty to @jhpalmieri.",
    "created_at": "2009-06-11T01:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45051",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from cwitty to @jhpalmieri.



---

archive/issue_comments_045052.json:
```json
{
    "body": "Here's a patch.  This depends on #6089.",
    "created_at": "2009-06-11T01:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45052",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch.  This depends on #6089.



---

archive/issue_comments_045053.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-11T01:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45053",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045054.json:
```json
{
    "body": "This all looks good, especially since #6089 makes it so easy to add in these checks.\n\nI'm getting a doctest failure at line 119, the first \"have_dvipng\" test is failing.  I suspect some other test is setting the global variable so it is no longer \"None\" and due to the way tests get re-ordered and since there are now more tests, by the time this test is run, it will fail.  Indeed,\n\n`sage -t --randorder sage/misc/latex.py`\n\ncan sometimes make all four of the \"have_xxx\" tests fail at the first check of each group, all in the same way.  So I think just the tests need adjustment where they don't assume they are the first ones run.\n\nIf I simulate having `latex` and `pdflatex` missing, then I get appropriate error messages.  But if I run the doctests with the two executables missing, then these error messages also bleed through in two doctests (at line 410 and line 1565).  Maybe the tests should each be converted into two variants and somehow logically combined with the values of `_have_latex` and `_have_pdflatex` and just return a logical value.  This doctest failure behavior is present with only #6089 applied (i.e. without the current patch) so we have a chance to fix it before #6089 gets merged (or we could hold it up).  I hadn't thought before to test with latex or pdflatex missing.  I'm presuming we don't want test failures just because a system does not include tex.\n\nSo I'm ready to give a positive review with adjusted doctests - everything else looks good.",
    "created_at": "2009-06-11T04:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45054",
    "user": "https://github.com/rbeezer"
}
```

This all looks good, especially since #6089 makes it so easy to add in these checks.

I'm getting a doctest failure at line 119, the first "have_dvipng" test is failing.  I suspect some other test is setting the global variable so it is no longer "None" and due to the way tests get re-ordered and since there are now more tests, by the time this test is run, it will fail.  Indeed,

`sage -t --randorder sage/misc/latex.py`

can sometimes make all four of the "have_xxx" tests fail at the first check of each group, all in the same way.  So I think just the tests need adjustment where they don't assume they are the first ones run.

If I simulate having `latex` and `pdflatex` missing, then I get appropriate error messages.  But if I run the doctests with the two executables missing, then these error messages also bleed through in two doctests (at line 410 and line 1565).  Maybe the tests should each be converted into two variants and somehow logically combined with the values of `_have_latex` and `_have_pdflatex` and just return a logical value.  This doctest failure behavior is present with only #6089 applied (i.e. without the current patch) so we have a chance to fix it before #6089 gets merged (or we could hold it up).  I hadn't thought before to test with latex or pdflatex missing.  I'm presuming we don't want test failures just because a system does not include tex.

So I'm ready to give a positive review with adjusted doctests - everything else looks good.



---

archive/issue_comments_045055.json:
```json
{
    "body": "Here's a new patch.  This deletes the initial doctests for have_dvipng (etc.); I think the remaining doctests still adequately test whether the functions are working, and should work in any order of execution.  For the doctest failures when latex is missing, I just changed the doctests like this:\n\n```\n-        sage: _run_latex_(file)\n+        sage: _run_latex_(file) # random - depends on whether latex is installed\n``` \nand similarly for the `png` doctest.  Do you think that's good enough?  It now passes all tests for me if latex and pdflatex are missing.",
    "created_at": "2009-06-11T19:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45055",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a new patch.  This deletes the initial doctests for have_dvipng (etc.); I think the remaining doctests still adequately test whether the functions are working, and should work in any order of execution.  For the doctest failures when latex is missing, I just changed the doctests like this:

```
-        sage: _run_latex_(file)
+        sage: _run_latex_(file) # random - depends on whether latex is installed
``` 
and similarly for the `png` doctest.  Do you think that's good enough?  It now passes all tests for me if latex and pdflatex are missing.



---

archive/issue_comments_045056.json:
```json
{
    "body": "Attachment [trac_5771.patch](tarball://root/attachments/some-uuid/ticket5771/trac_5771.patch) by @jhpalmieri created at 2009-06-11 19:55:40",
    "created_at": "2009-06-11T19:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45056",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_5771.patch](tarball://root/attachments/some-uuid/ticket5771/trac_5771.patch) by @jhpalmieri created at 2009-06-11 19:55:40



---

archive/issue_comments_045057.json:
```json
{
    "body": "I was thinking today about the doctest failure with the global variable being set in the \"wrong\" order.  We've seen that movie before with this file, no?  :-;\n\nLatex patch applies and builds against 4.0.1, now passes randomized testing on sage/misc/latex.py, documentation builds properly.\n\nI think the current doctests are fine.  My thought for the two that failed with missing latex and missing pdflatex were along the lines of the following (but I haven't tested this at all).\n\n```\nsage: h, s = have_pdflatex(), png(ZZ[x], \"zz.png\", do_in_background=False)\nsage: (h and s == None) or (not(h) and s.find('Error: PDFLatex') == 0)\nTrue\n```\n\nThat'd cover both possibilities, which was not really possible before the two new \"have_xxx\" checks.  So consider that simply a suggestion for the next time you are sprucing up the doctests in this file.\n\nPositive review.\n\nRelease manager: Apply #6089 before the \"trac_5771.patch\" patch.",
    "created_at": "2009-06-12T00:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45057",
    "user": "https://github.com/rbeezer"
}
```

I was thinking today about the doctest failure with the global variable being set in the "wrong" order.  We've seen that movie before with this file, no?  :-;

Latex patch applies and builds against 4.0.1, now passes randomized testing on sage/misc/latex.py, documentation builds properly.

I think the current doctests are fine.  My thought for the two that failed with missing latex and missing pdflatex were along the lines of the following (but I haven't tested this at all).

```
sage: h, s = have_pdflatex(), png(ZZ[x], "zz.png", do_in_background=False)
sage: (h and s == None) or (not(h) and s.find('Error: PDFLatex') == 0)
True
```

That'd cover both possibilities, which was not really possible before the two new "have_xxx" checks.  So consider that simply a suggestion for the next time you are sprucing up the doctests in this file.

Positive review.

Release manager: Apply #6089 before the "trac_5771.patch" patch.



---

archive/issue_comments_045058.json:
```json
{
    "body": "Oh, I see, that's a nice idea.",
    "created_at": "2009-06-12T01:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45058",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, I see, that's a nice idea.



---

archive/issue_comments_045059.json:
```json
{
    "body": "Replying to [comment:6 jhpalmieri]:\n> Oh, I see, that's a nice idea.\n\n\nI tried to do something similar on #5975 (which is coming along) and it didn't work so well.  The error messages come along via a \"print\", so are not part of a string that can be tested easily.\n\nThe minute you lose control over the user's environment it gets quite messy.  Oh well, ....",
    "created_at": "2009-06-12T05:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45059",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:6 jhpalmieri]:
> Oh, I see, that's a nice idea.


I tried to do something similar on #5975 (which is coming along) and it didn't work so well.  The error messages come along via a "print", so are not part of a string that can be tested easily.

The minute you lose control over the user's environment it gets quite messy.  Oh well, ....



---

archive/issue_events_013538.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-13T21:44:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5771#event-13538"
}
```



---

archive/issue_comments_045060.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5771#issuecomment-45060",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
