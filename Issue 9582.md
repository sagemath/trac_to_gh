# Issue 9582: Term order discrepancy in random test on OS X

archive/issues_009582.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  cwitty @dandrake @jhpalmieri @burcin\n\nReported by John Palmieri on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/8c77081af31fc7ef#8c77081af31fc7ef):\n\n```\na 64 bit Mac OS X 10.6.4 box: one failure:\n\nsage -t -long \"devel/sage/sage/symbolic/random_tests.py\"\n**********************************************************************\nFile \"/Applications/sage_builds/sage-4.5.2.alpha0/devel/sage/sage/\nsymbolic/random_tests.py\", line 236:\n    sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)\nExpected:\n    factorial(floor((-0.314177274493 + 0.144437996366*I)/cosh(-v1^2*e/\nv3) + cos((-0.708874026302 - 0.954135400334*I)*v3) -\nzetaderiv(-0.228070288671 + 0.33842966472*I, 0.520184609653 -\n0.734276246499*I)))^(-arccoth(-abs(((-0.804514286089 -\n0.0293247734576*I)*v1 + (-0.804514286089 - 0.0293247734576*I)*v3 -\n1.0)*elliptic_ec((-0.0263902659909 +\n0.153261789843*I)*arccot(pi*catalan)))))\nGot:\n    factorial(floor((-0.314177274493 + 0.144437996366*I)/cosh(-v1^2*e/\nv3) - zetaderiv(-0.228070288671 + 0.33842966472*I, 0.520184609653 -\n0.734276246499*I) + cos((-0.708874026302 - 0.954135400334*I)*v3)))^(-\narccoth(-abs(((-0.804514286089 - 0.0293247734576*I)*v1 +\n(-0.804514286089 - 0.0293247734576*I)*v3 -\n1.0)*elliptic_ec((-0.0263902659909 +\n0.153261789843*I)*arccot(pi*catalan)))))\n**********************************************************************\n\nLooks like a discrepancy in the order terms are printed.\n```\n\nAcccording to Dan Drake:\n\n```\nI'm seeing that on bsd.math too. This is related to #9514, which was\nsupposed to fix this, but evidently doesn't, on OS X at least.\n```\n\nRelated: #9514.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9582\n\n",
    "created_at": "2010-07-23T07:47:16Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Term order discrepancy in random test on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9582",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  cwitty @dandrake @jhpalmieri @burcin

Reported by John Palmieri on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/8c77081af31fc7ef#8c77081af31fc7ef):

```
a 64 bit Mac OS X 10.6.4 box: one failure:

sage -t -long "devel/sage/sage/symbolic/random_tests.py"
**********************************************************************
File "/Applications/sage_builds/sage-4.5.2.alpha0/devel/sage/sage/
symbolic/random_tests.py", line 236:
    sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
Expected:
    factorial(floor((-0.314177274493 + 0.144437996366*I)/cosh(-v1^2*e/
v3) + cos((-0.708874026302 - 0.954135400334*I)*v3) -
zetaderiv(-0.228070288671 + 0.33842966472*I, 0.520184609653 -
0.734276246499*I)))^(-arccoth(-abs(((-0.804514286089 -
0.0293247734576*I)*v1 + (-0.804514286089 - 0.0293247734576*I)*v3 -
1.0)*elliptic_ec((-0.0263902659909 +
0.153261789843*I)*arccot(pi*catalan)))))
Got:
    factorial(floor((-0.314177274493 + 0.144437996366*I)/cosh(-v1^2*e/
v3) - zetaderiv(-0.228070288671 + 0.33842966472*I, 0.520184609653 -
0.734276246499*I) + cos((-0.708874026302 - 0.954135400334*I)*v3)))^(-
arccoth(-abs(((-0.804514286089 - 0.0293247734576*I)*v1 +
(-0.804514286089 - 0.0293247734576*I)*v3 -
1.0)*elliptic_ec((-0.0263902659909 +
0.153261789843*I)*arccot(pi*catalan)))))
**********************************************************************

Looks like a discrepancy in the order terms are printed.
```

Acccording to Dan Drake:

```
I'm seeing that on bsd.math too. This is related to #9514, which was
supposed to fix this, but evidently doesn't, on OS X at least.
```

Related: #9514.

Issue created by migration from https://trac.sagemath.org/ticket/9582





---

archive/issue_comments_092398.json:
```json
{
    "body": "Unlikely that this has anything to do with #9514.  The symptom of #9514 was getting totally different terms, and the cause was that it made a list of all known symbolic functions [sin, cos, factorial, ...], and randomly picked the third element (say) from the list -- but on different systems, the third element might be factorial, or it might be cos.\n\nIf it's producing mathematically equal terms that only print differently, which seems to be the case here, the cause is probably some system dependency in the pynac simplification or printing routines.",
    "created_at": "2010-07-23T09:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92398",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Unlikely that this has anything to do with #9514.  The symptom of #9514 was getting totally different terms, and the cause was that it made a list of all known symbolic functions [sin, cos, factorial, ...], and randomly picked the third element (say) from the list -- but on different systems, the third element might be factorial, or it might be cos.

If it's producing mathematically equal terms that only print differently, which seems to be the case here, the cause is probably some system dependency in the pynac simplification or printing routines.



---

archive/issue_comments_092399.json:
```json
{
    "body": "Evaluating `cos(x) + zeta(x)` in Sage 4.5.2.alpha0 gives\n\n* `zeta(x) + cos(x)` on sage.math.\n* `cos(x) + zeta(x)` on bsd.math.\n\nIs this representative of the underlying problem?",
    "created_at": "2010-07-27T02:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92399",
    "user": "https://github.com/qed777"
}
```

Evaluating `cos(x) + zeta(x)` in Sage 4.5.2.alpha0 gives

* `zeta(x) + cos(x)` on sage.math.
* `cos(x) + zeta(x)` on bsd.math.

Is this representative of the underlying problem?



---

archive/issue_comments_092400.json:
```json
{
    "body": "I compiled [GiNaC](http://www.ginac.de/Download.html) (and [CLN](http://www.ginac.de/CLN/)) on bsd and sage.math.  Evaluating `cos(x) + zeta(x);` in GiNaC's `ginsh` shell gives the same results as in [comment:2 comment 2].  I don't know if this is useful information.",
    "created_at": "2010-07-28T08:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92400",
    "user": "https://github.com/qed777"
}
```

I compiled [GiNaC](http://www.ginac.de/Download.html) (and [CLN](http://www.ginac.de/CLN/)) on bsd and sage.math.  Evaluating `cos(x) + zeta(x);` in GiNaC's `ginsh` shell gives the same results as in [comment:2 comment 2].  I don't know if this is useful information.



---

archive/issue_comments_092401.json:
```json
{
    "body": "On Sage 4.4.4 on OS X 10.6:\n\n```\nsage: cos(x)+zeta(x)\ncos(x) + zeta(x)\nsage: zeta(x)+cos(x)\ncos(x) + zeta(x)\nsage: version()\n'Sage Version 4.4.4, Release Date: 2010-06-23'\n```\nSo this may have been a problem for a while?",
    "created_at": "2010-07-28T16:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92401",
    "user": "https://github.com/kcrisman"
}
```

On Sage 4.4.4 on OS X 10.6:

```
sage: cos(x)+zeta(x)
cos(x) + zeta(x)
sage: zeta(x)+cos(x)
cos(x) + zeta(x)
sage: version()
'Sage Version 4.4.4, Release Date: 2010-06-23'
```
So this may have been a problem for a while?



---

archive/issue_comments_092402.json:
```json
{
    "body": "Maybe so.  Maybe it was just exposed with new tests?",
    "created_at": "2010-07-28T16:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92402",
    "user": "https://github.com/jhpalmieri"
}
```

Maybe so.  Maybe it was just exposed with new tests?



---

archive/issue_comments_092403.json:
```json
{
    "body": "Attachment [trac_9582-workaround-printing-differences.patch](tarball://root/attachments/some-uuid/ticket9582/trac_9582-workaround-printing-differences.patch) by cwitty created at 2010-07-28 20:57:58",
    "created_at": "2010-07-28T20:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92403",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac_9582-workaround-printing-differences.patch](tarball://root/attachments/some-uuid/ticket9582/trac_9582-workaround-printing-differences.patch) by cwitty created at 2010-07-28 20:57:58



---

archive/issue_comments_092404.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T21:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92404",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092405.json:
```json
{
    "body": "If we decide that the actual problem (different printing across platforms) is not a regression, and doesn't have to be fixed in this release, then I've attached a patch that works around the problem (by modifying the doctest to produce an output that prints the same on my Linux box and on bsd.math).\n\nIf you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.",
    "created_at": "2010-07-28T21:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92405",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

If we decide that the actual problem (different printing across platforms) is not a regression, and doesn't have to be fixed in this release, then I've attached a patch that works around the problem (by modifying the doctest to produce an output that prints the same on my Linux box and on bsd.math).

If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.



---

archive/issue_comments_092406.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-29T06:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92406",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092407.json:
```json
{
    "body": "Replying to [comment:6 cwitty]:\n> If we decide that the actual problem (different printing across platforms) is not a regression, and doesn't have to be fixed in this release, then I've attached a patch that works around the problem (by modifying the doctest to produce an output that prints the same on my Linux box and on bsd.math).\n\n\nThis seems reasonable.  Are there any objections?  The workaround patch works for me on bsd, sage, and t2.math. \n\n> If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.\n\n\nI'll give this ticket a positive review, merge it in 4.5.2.rc0, close it, and open a new one for the printing order problem.",
    "created_at": "2010-07-29T06:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92407",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:6 cwitty]:
> If we decide that the actual problem (different printing across platforms) is not a regression, and doesn't have to be fixed in this release, then I've attached a patch that works around the problem (by modifying the doctest to produce an output that prints the same on my Linux box and on bsd.math).


This seems reasonable.  Are there any objections?  The workaround patch works for me on bsd, sage, and t2.math. 

> If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.


I'll give this ticket a positive review, merge it in 4.5.2.rc0, close it, and open a new one for the printing order problem.



---

archive/issue_comments_092408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T06:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92408",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023863.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-29T06:03:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9582#event-23863"
}
```



---

archive/issue_comments_092409.json:
```json
{
    "body": "Replying to [comment:6 cwitty]:\n\n> If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.\n\n\nI've opened #9632.",
    "created_at": "2010-07-29T06:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92409",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:6 cwitty]:

> If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.


I've opened #9632.



---

archive/issue_comments_092410.json:
```json
{
    "body": "Burcin, since we haven't released 4.5.2.rc0 yet, I'm happy to make changes to it, e.g., merging a different patch.  Just let us know within a day or so.  I apologize for not giving you more time to examine this ticket.",
    "created_at": "2010-07-29T07:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92410",
    "user": "https://github.com/qed777"
}
```

Burcin, since we haven't released 4.5.2.rc0 yet, I'm happy to make changes to it, e.g., merging a different patch.  Just let us know within a day or so.  I apologize for not giving you more time to examine this ticket.



---

archive/issue_comments_092411.json:
```json
{
    "body": "I've \"qfinished\" 4.5.2.rc0, and we will release it soon.  Shall we continue at #9632?",
    "created_at": "2010-08-01T09:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92411",
    "user": "https://github.com/qed777"
}
```

I've "qfinished" 4.5.2.rc0, and we will release it soon.  Shall we continue at #9632?



---

archive/issue_comments_092412.json:
```json
{
    "body": "Yes, I couldn't see any quick fix which wouldn't effect performance. Ordering of the terms is already a big performance bottleneck in Python. I'd like to fix things properly once instead of adding kludges all around, but I don't have time to do that right now.\n\nI've been sidetracked by other pynac problems since. Sorry for keeping quiet all this time and thanks for your efforts.",
    "created_at": "2010-08-01T10:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9582#issuecomment-92412",
    "user": "https://github.com/burcin"
}
```

Yes, I couldn't see any quick fix which wouldn't effect performance. Ordering of the terms is already a big performance bottleneck in Python. I'd like to fix things properly once instead of adding kludges all around, but I don't have time to do that right now.

I've been sidetracked by other pynac problems since. Sorry for keeping quiet all this time and thanks for your efforts.
