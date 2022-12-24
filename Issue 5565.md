# Issue 5565: sage crashes because of too small stacksize

archive/issues_005565.json:
```json
{
    "body": "Assignee: cwitty\n\nit seems a stacksize of 10M is not enough to run Sage, at least under\nFedora 10 (I typed <tab> after Poly):\n\n```\npatate% limit stacksize 10m\npatate% sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: Poly\n| Sage Version 3.4, Release Date: 2009-03-11                         |\n| Type notebook() for the GUI, and license() for information.        |\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n/usr/local/sage-3.4-core2/sage/local/bin/sage-sage: line 197:   816 Segmentation fault      sage-ipython \"$@\" -i\n```\n\nIn addition there is a typo in the above error message, where\n\"occured\" should be \"occurred\". Should I open a separate ticket\nfor that?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5565\n\n",
    "created_at": "2009-03-19T13:25:00Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage crashes because of too small stacksize",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5565",
    "user": "zimmerma"
}
```
Assignee: cwitty

it seems a stacksize of 10M is not enough to run Sage, at least under
Fedora 10 (I typed <tab> after Poly):

```
patate% limit stacksize 10m
patate% sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Poly
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

/usr/local/sage-3.4-core2/sage/local/bin/sage-sage: line 197:   816 Segmentation fault      sage-ipython "$@" -i
```

In addition there is a typo in the above error message, where
"occured" should be "occurred". Should I open a separate ticket
for that?

Issue created by migration from https://trac.sagemath.org/ticket/5565





---

archive/issue_comments_043325.json:
```json
{
    "body": "Some additional comments from Emmanuel Thome:\n\n(1) the problem was on a 64-bit machine, maybe it does not appear on 32-bit machines\n\n(2) maybe this problem is difficult to track down. A sanity check at startup would help,\n  and/or a hint about \"stacksize\" in the error message, to avoid other people spend some time\n  on this issue.",
    "created_at": "2009-03-19T14:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5565#issuecomment-43325",
    "user": "zimmerma"
}
```

Some additional comments from Emmanuel Thome:

(1) the problem was on a 64-bit machine, maybe it does not appear on 32-bit machines

(2) maybe this problem is difficult to track down. A sanity check at startup would help,
  and/or a hint about "stacksize" in the error message, to avoid other people spend some time
  on this issue.



---

archive/issue_comments_043326.json:
```json
{
    "body": "Mhh, odd. On a 64 bit Ubuntu machine (sage.math) with Sage 3.4 even a 4MB stack works. What kind of shell is involved here? It seems to be either a csh or a tcsh.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T00:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5565#issuecomment-43326",
    "user": "mabshoff"
}
```

Mhh, odd. On a 64 bit Ubuntu machine (sage.math) with Sage 3.4 even a 4MB stack works. What kind of shell is involved here? It seems to be either a csh or a tcsh.

Cheers,

Michael



---

archive/issue_comments_043327.json:
```json
{
    "body": "> It seems to be either a csh or a tcsh. \n\nNo, both Pierrick Gaudry and Emmanuel Thome had the problem with bash (I'm the only dinosaur in the\ngroup still using tcsh).",
    "created_at": "2009-03-26T07:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5565#issuecomment-43327",
    "user": "zimmerma"
}
```

> It seems to be either a csh or a tcsh. 

No, both Pierrick Gaudry and Emmanuel Thome had the problem with bash (I'm the only dinosaur in the
group still using tcsh).



---

archive/issue_comments_043328.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-02-05T20:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5565#issuecomment-43328",
    "user": "zimmerma"
}
```

Resolution: worksforme



---

archive/issue_comments_043329.json:
```json
{
    "body": "It seems that problem has gone away with Sage 4.3.1.",
    "created_at": "2010-02-05T20:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5565#issuecomment-43329",
    "user": "zimmerma"
}
```

It seems that problem has gone away with Sage 4.3.1.



---

archive/issue_comments_043330.json:
```json
{
    "body": "Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.",
    "created_at": "2010-02-05T21:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5565#issuecomment-43330",
    "user": "mvngu"
}
```

Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.



---

archive/issue_comments_043331.json:
```json
{
    "body": "sorry again!",
    "created_at": "2010-02-07T21:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5565#issuecomment-43331",
    "user": "zimmerma"
}
```

sorry again!
