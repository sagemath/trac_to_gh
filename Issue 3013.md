# Issue 3013: bug in integrate (found during a talk!)

archive/issues_003013.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: integrate(sin(x)*cos(10*x)*log(x))\nTraceback (most recent call last):\n...\nTypeError: Error executing code in Maxima\nCODE:\n\tsage22 : integrate(sage21,sage3)$\nMaxima ERROR:\n\t\n\nToo many contexts.\nsage: show(integrate(sin(x^2)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3013\n\n",
    "created_at": "2008-04-23T23:50:42Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "bug in integrate (found during a talk!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3013",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: integrate(sin(x)*cos(10*x)*log(x))
Traceback (most recent call last):
...
TypeError: Error executing code in Maxima
CODE:
	sage22 : integrate(sage21,sage3)$
Maxima ERROR:
	

Too many contexts.
sage: show(integrate(sin(x^2)
```


Issue created by migration from https://trac.sagemath.org/ticket/3013





---

archive/issue_comments_020708.json:
```json
{
    "body": "This is also a Maxima bug:\n\n```\nLast login: Wed Apr 23 16:43:25 on ttys014\nteragon-2:~ was$ sage -maxima\nMaxima 5.13.0 http://maxima.sourceforge.net\nUsing Lisp CLISP 2.41 (2006-10-13)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) integrate(sin(x)*cos(10*x)*log(x),x);\n\nToo many contexts.\n -- an error.  To debug this try debugmode(true);\n(%i2) \n```\n",
    "created_at": "2008-04-23T23:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3013#issuecomment-20708",
    "user": "@williamstein"
}
```

This is also a Maxima bug:

```
Last login: Wed Apr 23 16:43:25 on ttys014
teragon-2:~ was$ sage -maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.41 (2006-10-13)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) integrate(sin(x)*cos(10*x)*log(x),x);

Too many contexts.
 -- an error.  To debug this try debugmode(true);
(%i2) 
```




---

archive/issue_comments_020709.json:
```json
{
    "body": "This is fixed in Maxima 5.15.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T16:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3013#issuecomment-20709",
    "user": "mabshoff"
}
```

This is fixed in Maxima 5.15.

Cheers,

Michael



---

archive/issue_comments_020710.json:
```json
{
    "body": "This now works:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.1, Release Date: 2008-08-17                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: integrate(sin(x)*cos(10*x)*log(x))\n(9*integrate(cos(11*x)/x, x) - 11*integrate(cos(9*x)/x, x) - 9*log(x)*cos(11*x) + 11*log(x)*cos(9*x))/198\n```\n\nSo once we add a doctest we can close this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T21:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3013#issuecomment-20710",
    "user": "mabshoff"
}
```

This now works:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
| Type notebook() for the GUI, and license() for information.        |
sage: integrate(sin(x)*cos(10*x)*log(x))
(9*integrate(cos(11*x)/x, x) - 11*integrate(cos(9*x)/x, x) - 9*log(x)*cos(11*x) + 11*log(x)*cos(9*x))/198
```

So once we add a doctest we can close this ticket.

Cheers,

Michael



---

archive/issue_comments_020711.json:
```json
{
    "body": "Attachment [trac_3103.patch](tarball://root/attachments/some-uuid/ticket3013/trac_3103.patch) by mabshoff created at 2008-08-22 22:04:27",
    "created_at": "2008-08-22T22:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3013#issuecomment-20711",
    "user": "mabshoff"
}
```

Attachment [trac_3103.patch](tarball://root/attachments/some-uuid/ticket3013/trac_3103.patch) by mabshoff created at 2008-08-22 22:04:27



---

archive/issue_comments_020712.json:
```json
{
    "body": "Maxima returns a solution that is partially unevaluated, so merging this might or might not be a good idea.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T22:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3013#issuecomment-20712",
    "user": "mabshoff"
}
```

Maxima returns a solution that is partially unevaluated, so merging this might or might not be a good idea.

Cheers,

Michael



---

archive/issue_comments_020713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-23T00:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3013#issuecomment-20713",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020714.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-23T00:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3013#issuecomment-20714",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha0
