# Issue 8720: CC and CDF do not display numeric 0

archive/issues_008720.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @zimmermann6 @mwhansen\n\nLook at the inconsistency:\n\n```\nsage: RR(0)\n0.000000000000000\nsage: RDF(0)\n0.0\n```\n\nversus\n\n```\nsage: CDF(0)\n0\nsage: CC(0)\n0\n```\n\n\n---\n\nApply [attachment:trac-8720-printing-complex-zero.patch], [attachment:trac_8720-doctests.patch], [attachment:trac_8720-doctests-2.patch]\nand [attachment:trac_8720-doctests-3.patch].\n\nIssue created by migration from https://trac.sagemath.org/ticket/8720\n\n",
    "closed_at": "2012-04-19T06:43:48Z",
    "created_at": "2010-04-20T02:42:33Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "CC and CDF do not display numeric 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8720",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @aghitza

CC:  @zimmermann6 @mwhansen

Look at the inconsistency:

```
sage: RR(0)
0.000000000000000
sage: RDF(0)
0.0
```

versus

```
sage: CDF(0)
0
sage: CC(0)
0
```


---

Apply [attachment:trac-8720-printing-complex-zero.patch], [attachment:trac_8720-doctests.patch], [attachment:trac_8720-doctests-2.patch]
and [attachment:trac_8720-doctests-3.patch].

Issue created by migration from https://trac.sagemath.org/ticket/8720





---

archive/issue_comments_079472.json:
```json
{
    "body": "I think CDF and CC should display the same output as RDF and RR, respectively.\n\nCCing zimmerma since he may be interested in reviewing this.",
    "created_at": "2010-04-20T03:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79472",
    "user": "https://github.com/jasongrout"
}
```

I think CDF and CC should display the same output as RDF and RR, respectively.

CCing zimmerma since he may be interested in reviewing this.



---

archive/issue_comments_079473.json:
```json
{
    "body": "since I was asked to review this ticket, I first notice that some doctests do not pass any more,\nfor example:\n\n```\nsage -t  gsl/dft.py\n**********************************************************************\nFile \"/usr/local/sage-4.3.5-core2/devel/sage-8720/sage/gsl/dft.py\", line 528:\n    sage: t = s.fft(); t\nExpected:\n    Indexed sequence: [5.00000000000000, 0, 0, 0, 0]\n     indexed by [0, 1, 2, 3, 4]\nGot:\n    Indexed sequence: [5.00000000000000, 0.000000000000000, 0.000000000000000, \\\n0.000000000000000, 0.000000000000000]\n        indexed by [0, 1, 2, 3, 4]\n```\nthus some more work is needed. Please check all doctests still pass.",
    "created_at": "2010-04-20T10:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79473",
    "user": "https://github.com/zimmermann6"
}
```

since I was asked to review this ticket, I first notice that some doctests do not pass any more,
for example:

```
sage -t  gsl/dft.py
**********************************************************************
File "/usr/local/sage-4.3.5-core2/devel/sage-8720/sage/gsl/dft.py", line 528:
    sage: t = s.fft(); t
Expected:
    Indexed sequence: [5.00000000000000, 0, 0, 0, 0]
     indexed by [0, 1, 2, 3, 4]
Got:
    Indexed sequence: [5.00000000000000, 0.000000000000000, 0.000000000000000, \
0.000000000000000, 0.000000000000000]
        indexed by [0, 1, 2, 3, 4]
```
thus some more work is needed. Please check all doctests still pass.



---

archive/issue_comments_079474.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-20T10:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79474",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_079475.json:
```json
{
    "body": "Thanks for looking at it.  When I ran the doctests, a number of them failed, so I posted to sage-devel and kept this ticket as \"needs work\".  I will set it to \"needs review\" when I've taken care of the failing doctests.\n\nThanks again.",
    "created_at": "2010-04-20T13:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79475",
    "user": "https://github.com/jasongrout"
}
```

Thanks for looking at it.  When I ran the doctests, a number of them failed, so I posted to sage-devel and kept this ticket as "needs work".  I will set it to "needs review" when I've taken care of the failing doctests.

Thanks again.



---

archive/issue_comments_079476.json:
```json
{
    "body": "I'm going to run the tests shortly and produce an doctest fixing patch.",
    "created_at": "2011-12-18T16:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79476",
    "user": "https://github.com/mwhansen"
}
```

I'm going to run the tests shortly and produce an doctest fixing patch.



---

archive/issue_comments_079477.json:
```json
{
    "body": "I've attached a patch which should fix all of the doctests in 4.8.alpha4.",
    "created_at": "2011-12-18T23:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79477",
    "user": "https://github.com/mwhansen"
}
```

I've attached a patch which should fix all of the doctests in 4.8.alpha4.



---

archive/issue_comments_079478.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-18T23:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79478",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079479.json:
```json
{
    "body": "note that a consequence of that ticket is that coefficients 0 that were not displayed in Taylor\nseries are now displayed, for example:\n\n```\nsage: E = EllipticCurve('37a')\nsage: L = E.lseries().dokchitser()\nsage: L.taylor_series(1,4)\n0.0000000000000 + 0.305999773834052*z + 0.186547797268162*z^2 - 0.136791463097188*z^3 + O(z^4)\n```\n(Before this ticket, the leading `0.000000000000000` was not printed.)\n\nI find it good, since those 0.0 values can come from numerical cancellation.\n\nPaul",
    "created_at": "2011-12-19T11:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79479",
    "user": "https://github.com/zimmermann6"
}
```

note that a consequence of that ticket is that coefficients 0 that were not displayed in Taylor
series are now displayed, for example:

```
sage: E = EllipticCurve('37a')
sage: L = E.lseries().dokchitser()
sage: L.taylor_series(1,4)
0.0000000000000 + 0.305999773834052*z + 0.186547797268162*z^2 - 0.136791463097188*z^3 + O(z^4)
```
(Before this ticket, the leading `0.000000000000000` was not printed.)

I find it good, since those 0.0 values can come from numerical cancellation.

Paul



---

archive/issue_comments_079480.json:
```json
{
    "body": "all tests work on top of Sage 4.7.2, I give a positive review.\n\nPaul",
    "created_at": "2011-12-19T11:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79480",
    "user": "https://github.com/zimmermann6"
}
```

all tests work on top of Sage 4.7.2, I give a positive review.

Paul



---

archive/issue_comments_079481.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-19T17:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79481",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079482.json:
```json
{
    "body": "> all tests work on top of Sage 4.7.2, I give a positive review.\n\nJust doing the radio button for this.  Nice teamwork on this!",
    "created_at": "2011-12-19T17:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79482",
    "user": "https://github.com/kcrisman"
}
```

> all tests work on top of Sage 4.7.2, I give a positive review.

Just doing the radio button for this.  Nice teamwork on this!



---

archive/issue_comments_079483.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-12-23T16:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79483",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_079484.json:
```json
{
    "body": "A few more doctests need to be fixed:\n\n```\nsage -t  -force_lib devel/sage/sage/matrix/matrix2.pyx\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx\", line 7987:\n    sage: M.round(6).zero_at(10^-6)\nExpected:\n    [             -1.528503                      0                      0]\n    [  0.459974 - 0.40061*I              -1.741233                      0]\n    [-0.934304 + 0.148868*I   0.54833 + 0.073202*I              -0.550725]\nGot:\n    [             -1.528503                    0.0                    0.0]\n    [  0.459974 - 0.40061*I              -1.741233                    0.0]\n    [-0.934304 + 0.148868*I   0.54833 + 0.073202*I              -0.550725]\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx\", line 7991:\n    sage: (A - M*G).zero_at(10^-12)\nExpected:\n    [0 0 0]\n    [0 0 0]\n    [0 0 0]\nGot:\n    [0.0 0.0 0.0]\n    [0.0 0.0 0.0]\n    [0.0 0.0 0.0]\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx\", line 7995:\n    sage: (G*G.conjugate().transpose()).zero_at(10^-12)\nExpected:\n    [1.0   0   0]\n    [  0 1.0   0]\n    [  0   0 1.0]\nGot:\n    [1.0 0.0 0.0]\n    [0.0 1.0 0.0]\n    [0.0 0.0 1.0]\n**********************************************************************\n\n```",
    "created_at": "2011-12-23T16:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79484",
    "user": "https://github.com/jdemeyer"
}
```

A few more doctests need to be fixed:

```
sage -t  -force_lib devel/sage/sage/matrix/matrix2.pyx
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx", line 7987:
    sage: M.round(6).zero_at(10^-6)
Expected:
    [             -1.528503                      0                      0]
    [  0.459974 - 0.40061*I              -1.741233                      0]
    [-0.934304 + 0.148868*I   0.54833 + 0.073202*I              -0.550725]
Got:
    [             -1.528503                    0.0                    0.0]
    [  0.459974 - 0.40061*I              -1.741233                    0.0]
    [-0.934304 + 0.148868*I   0.54833 + 0.073202*I              -0.550725]
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx", line 7991:
    sage: (A - M*G).zero_at(10^-12)
Expected:
    [0 0 0]
    [0 0 0]
    [0 0 0]
Got:
    [0.0 0.0 0.0]
    [0.0 0.0 0.0]
    [0.0 0.0 0.0]
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx", line 7995:
    sage: (G*G.conjugate().transpose()).zero_at(10^-12)
Expected:
    [1.0   0   0]
    [  0 1.0   0]
    [  0   0 1.0]
Got:
    [1.0 0.0 0.0]
    [0.0 1.0 0.0]
    [0.0 0.0 1.0]
**********************************************************************

```



---

archive/issue_comments_079485.json:
```json
{
    "body": "sorry, but there is no such doctest in 4.7.2. There must be some interaction with some\nother patch which you included. My positive review was valid for 4.7.2 only.\n\nPaul",
    "created_at": "2011-12-23T16:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79485",
    "user": "https://github.com/zimmermann6"
}
```

sorry, but there is no such doctest in 4.7.2. There must be some interaction with some
other patch which you included. My positive review was valid for 4.7.2 only.

Paul



---

archive/issue_comments_079486.json:
```json
{
    "body": "Replying to [comment:11 zimmerma]:\n> sorry, but there is no such doctest in 4.7.2. There must be some interaction with some\n> other patch which you included. My positive review was valid for 4.7.2 only.\n\n\nProbably Jeroen is referring to doctests in the latest alpha, on which (for better or for worse) patches need to be based on.",
    "created_at": "2011-12-23T16:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79486",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:11 zimmerma]:
> sorry, but there is no such doctest in 4.7.2. There must be some interaction with some
> other patch which you included. My positive review was valid for 4.7.2 only.


Probably Jeroen is referring to doctests in the latest alpha, on which (for better or for worse) patches need to be based on.



---

archive/issue_comments_079487.json:
```json
{
    "body": "*** bump ***",
    "created_at": "2012-02-07T22:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79487",
    "user": "https://github.com/jdemeyer"
}
```

*** bump ***



---

archive/issue_comments_079488.json:
```json
{
    "body": "I posted a patch fixing these problems.",
    "created_at": "2012-02-08T01:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79488",
    "user": "https://github.com/mwhansen"
}
```

I posted a patch fixing these problems.



---

archive/issue_comments_079489.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-08T01:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79489",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079490.json:
```json
{
    "body": "Note that the second patch applies with a little fuzz.\n\n```\n$ hg qpush\napplying trac_8720-doctests.patch\npatching file sage/matrix/matrix_double_dense.pyx\nHunk #1 succeeded at 189 with fuzz 2 (offset 9 lines).\nnow at: trac_8720-doctests.patch\n```\nI'll run tests and check.  I should have set `sage -b` to do parallel building",
    "created_at": "2012-02-08T01:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79490",
    "user": "https://github.com/kcrisman"
}
```

Note that the second patch applies with a little fuzz.

```
$ hg qpush
applying trac_8720-doctests.patch
patching file sage/matrix/matrix_double_dense.pyx
Hunk #1 succeeded at 189 with fuzz 2 (offset 9 lines).
now at: trac_8720-doctests.patch
```
I'll run tests and check.  I should have set `sage -b` to do parallel building



---

archive/issue_comments_079491.json:
```json
{
    "body": "{{[\n\nDoctesting 1 file using 1 thread\nsage -t  devel/sage-main/sage/matrix/matrix_double_dense.pyx\n\t [19.7 s]\n \n}}}\n\nNow running full long doctests.",
    "created_at": "2012-02-08T02:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79491",
    "user": "https://github.com/kcrisman"
}
```

{{[

Doctesting 1 file using 1 thread
sage -t  devel/sage-main/sage/matrix/matrix_double_dense.pyx
	 [19.7 s]
 
}}}

Now running full long doctests.



---

archive/issue_comments_079492.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-08T03:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79492",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079493.json:
```json
{
    "body": "```\n\n$ ../../sage -tp 4 -long sage/lfunctions/lcalc.py \nGlobal iterations: 1\nFile iterations: 1\nUsing long cached timings to run longest doctests first.\nDoctesting 1 file using 1 thread\nsage -t -long devel/sage-main/sage/lfunctions/lcalc.py\n  ***   Warning: new stack size = 1028976 (0.981 Mbytes).\n  ***   Warning: new stack size = 1003360 (0.957 Mbytes).\n  ***   Warning: new stack size = 1001472 (0.955 Mbytes).\n**********************************************************************\nFile \"/Users/.../sage-5.0.beta2/devel/sage-main/sage/lfunctions/lcalc.py\", line 229:\n    sage: E.lseries().values_along_line(0.5, 3, 5)\nExpected:\n    [(0.000000000, 0.209951303), (0.500000000, -2.92081722e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]\nGot:\n    [(0.000000000, 0.209951303), (0.500000000, -2.92081723e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/.../.sage/tmp/new_host_2.home-37994/lcalc_37997.py\n\t [3.0 s]\n```\nThe difference was in the e-16 one. I think there is a reason that one used to be `-...e-16` in the old doctest.  I'm going to ignore the stack size warnings, since they don't seem to have affected the outcome, though I'm sure they're not ideal.\n\nAll else is fine!",
    "created_at": "2012-02-08T03:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79493",
    "user": "https://github.com/kcrisman"
}
```

```

$ ../../sage -tp 4 -long sage/lfunctions/lcalc.py 
Global iterations: 1
File iterations: 1
Using long cached timings to run longest doctests first.
Doctesting 1 file using 1 thread
sage -t -long devel/sage-main/sage/lfunctions/lcalc.py
  ***   Warning: new stack size = 1028976 (0.981 Mbytes).
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
  ***   Warning: new stack size = 1001472 (0.955 Mbytes).
**********************************************************************
File "/Users/.../sage-5.0.beta2/devel/sage-main/sage/lfunctions/lcalc.py", line 229:
    sage: E.lseries().values_along_line(0.5, 3, 5)
Expected:
    [(0.000000000, 0.209951303), (0.500000000, -2.92081722e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
Got:
    [(0.000000000, 0.209951303), (0.500000000, -2.92081723e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/.../.sage/tmp/new_host_2.home-37994/lcalc_37997.py
	 [3.0 s]
```
The difference was in the e-16 one. I think there is a reason that one used to be `-...e-16` in the old doctest.  I'm going to ignore the stack size warnings, since they don't seem to have affected the outcome, though I'm sure they're not ideal.

All else is fine!



---

archive/issue_comments_079494.json:
```json
{
    "body": "Can you double-check to make sure that test was passing before the patches?  It seems odd to me that error would have been triggered by this patch.",
    "created_at": "2012-02-08T03:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79494",
    "user": "https://github.com/jasongrout"
}
```

Can you double-check to make sure that test was passing before the patches?  It seems odd to me that error would have been triggered by this patch.



---

archive/issue_comments_079495.json:
```json
{
    "body": "> Can you double-check to make sure that test was passing before the patches?  It seems odd to me that error would have been triggered by this patch.\n\nNotice that the test now fails because we used to ignore all digits before the exponent, not because of the stack thing - the doc even points out that warnings might happen, it's no big deal for now.\n\n```\n        Sometimes warnings are printed (by lcalc) when this command is\n        run::\n        \n            sage: E = EllipticCurve('389a')\n            sage: E.lseries().values_along_line(0.5, 3, 5)\n            [(0, 0.209951303),\n             (0.500000000, -...e-16),\n             (1.00000000, 0.133768433),\n             (1.50000000, 0.360092864),\n             (2.00000000, 0.552975867)]\n```\nHere is 5.0.beta1:\n\n```\n$ ./sage -t -long devel/sage/sage/lfunctions/lcalc.py \nsage -t -long \"devel/sage/sage/lfunctions/lcalc.py\"         \n\t [20.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 20.5 seconds\n<snip>\nsage:             sage: E = EllipticCurve('389a')\nsage:             sage: E.lseries().values_along_line(0.5, 3, 5)\n  ***   Warning: new stack size = 1003360 (0.957 Mbytes).\n[(0, 0.209951303), (0.500000000, -2.92081723e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]\n```\nso we can see that all that has to be done is go back to the previous doctest for that one number (not even the whole list).",
    "created_at": "2012-02-08T03:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79495",
    "user": "https://github.com/kcrisman"
}
```

> Can you double-check to make sure that test was passing before the patches?  It seems odd to me that error would have been triggered by this patch.

Notice that the test now fails because we used to ignore all digits before the exponent, not because of the stack thing - the doc even points out that warnings might happen, it's no big deal for now.

```
        Sometimes warnings are printed (by lcalc) when this command is
        run::
        
            sage: E = EllipticCurve('389a')
            sage: E.lseries().values_along_line(0.5, 3, 5)
            [(0, 0.209951303),
             (0.500000000, -...e-16),
             (1.00000000, 0.133768433),
             (1.50000000, 0.360092864),
             (2.00000000, 0.552975867)]
```
Here is 5.0.beta1:

```
$ ./sage -t -long devel/sage/sage/lfunctions/lcalc.py 
sage -t -long "devel/sage/sage/lfunctions/lcalc.py"         
	 [20.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 20.5 seconds
<snip>
sage:             sage: E = EllipticCurve('389a')
sage:             sage: E.lseries().values_along_line(0.5, 3, 5)
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
[(0, 0.209951303), (0.500000000, -2.92081723e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
```
so we can see that all that has to be done is go back to the previous doctest for that one number (not even the whole list).



---

archive/issue_comments_079496.json:
```json
{
    "body": "Ah, I understand.  Mike made this test much more rigid, and that is what is failing here.  Yeah, I agree with your conclusion, Karl-Dieter.",
    "created_at": "2012-02-08T04:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79496",
    "user": "https://github.com/jasongrout"
}
```

Ah, I understand.  Mike made this test much more rigid, and that is what is failing here.  Yeah, I agree with your conclusion, Karl-Dieter.



---

archive/issue_comments_079497.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-28T21:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79497",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079498.json:
```json
{
    "body": "I've gone ahead and fixed that doctest.",
    "created_at": "2012-03-28T21:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79498",
    "user": "https://github.com/mwhansen"
}
```

I've gone ahead and fixed that doctest.



---

archive/issue_comments_079499.json:
```json
{
    "body": "I'm afraid that, according to the patchbot, this new patch works on latest release (4.8) but fails a doctest on 5.0.beta3, and doesn't even apply to 5.0.beta11.",
    "created_at": "2012-03-29T17:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79499",
    "user": "https://github.com/loefflerd"
}
```

I'm afraid that, according to the patchbot, this new patch works on latest release (4.8) but fails a doctest on 5.0.beta3, and doesn't even apply to 5.0.beta11.



---

archive/issue_comments_079500.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-29T17:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79500",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079501.json:
```json
{
    "body": "Attachment [trac-8720-printing-complex-zero.patch](tarball://root/attachments/some-uuid/ticket8720/trac-8720-printing-complex-zero.patch) by @mwhansen created at 2012-03-29 20:20:06",
    "created_at": "2012-03-29T20:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79501",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac-8720-printing-complex-zero.patch](tarball://root/attachments/some-uuid/ticket8720/trac-8720-printing-complex-zero.patch) by @mwhansen created at 2012-03-29 20:20:06



---

archive/issue_comments_079502.json:
```json
{
    "body": "Attachment [trac_8720-doctests-2.patch](tarball://root/attachments/some-uuid/ticket8720/trac_8720-doctests-2.patch) by @mwhansen created at 2012-03-29 20:20:19",
    "created_at": "2012-03-29T20:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79502",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8720-doctests-2.patch](tarball://root/attachments/some-uuid/ticket8720/trac_8720-doctests-2.patch) by @mwhansen created at 2012-03-29 20:20:19



---

archive/issue_comments_079503.json:
```json
{
    "body": "I've rebased the files on beta11.",
    "created_at": "2012-03-29T20:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79503",
    "user": "https://github.com/mwhansen"
}
```

I've rebased the files on beta11.



---

archive/issue_comments_079504.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-29T20:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79504",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079505.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-30T07:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79505",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079506.json:
```json
{
    "body": "The beta11 patchbot brings up some doctest failures:\n\n```\nThe following tests failed:\n\n\tsage -t  -force_lib devel/sage-8720/sage/plot/hyperbolic_triangle.py # 2 doctests failed\n\tsage -t  -force_lib devel/sage-8720/sage/plot/hyperbolic_arc.py # 1 doctests failed\n\tsage -t  -force_lib devel/sage-8720/sage/matrix/matrix_space.py # 1 doctests failed\n\tsage -t  -force_lib devel/sage-8720/sage/matrix/constructor.py # 1 doctests failed\n```",
    "created_at": "2012-03-30T07:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79506",
    "user": "https://github.com/loefflerd"
}
```

The beta11 patchbot brings up some doctest failures:

```
The following tests failed:

	sage -t  -force_lib devel/sage-8720/sage/plot/hyperbolic_triangle.py # 2 doctests failed
	sage -t  -force_lib devel/sage-8720/sage/plot/hyperbolic_arc.py # 1 doctests failed
	sage -t  -force_lib devel/sage-8720/sage/matrix/matrix_space.py # 1 doctests failed
	sage -t  -force_lib devel/sage-8720/sage/matrix/constructor.py # 1 doctests failed
```



---

archive/issue_comments_079507.json:
```json
{
    "body": "Attachment [trac_8720-doctests-3.patch](tarball://root/attachments/some-uuid/ticket8720/trac_8720-doctests-3.patch) by @zimmermann6 created at 2012-04-03 06:57:15\n\napply this patch on top of the other three",
    "created_at": "2012-04-03T06:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79507",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8720-doctests-3.patch](tarball://root/attachments/some-uuid/ticket8720/trac_8720-doctests-3.patch) by @zimmermann6 created at 2012-04-03 06:57:15

apply this patch on top of the other three



---

archive/issue_comments_079508.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-03T06:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79508",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079509.json:
```json
{
    "body": "I have attached a patch for sage-5.0.beta11, which makes the 4 doctests from comment [comment:24] work. Note that the change in `matrix/constructor.py` seems to indicate it\nwas not working properly before this ticket. Please review.\n\nPaul",
    "created_at": "2012-04-03T06:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79509",
    "user": "https://github.com/zimmermann6"
}
```

I have attached a patch for sage-5.0.beta11, which makes the 4 doctests from comment [comment:24] work. Note that the change in `matrix/constructor.py` seems to indicate it
was not working properly before this ticket. Please review.

Paul



---

archive/issue_comments_079510.json:
```json
{
    "body": "changed description for the patchbot.\n\nPaul",
    "created_at": "2012-04-03T07:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79510",
    "user": "https://github.com/zimmermann6"
}
```

changed description for the patchbot.

Paul



---

archive/issue_comments_079511.json:
```json
{
    "body": "Seems to work fine on these files.  Running long doctests now but I don't anticipate any more problems.\n\nAs to constructor.py, the `-0.1` was removed in the first doctest patch, so the problem was in the test, not the behavior.",
    "created_at": "2012-04-03T13:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79511",
    "user": "https://github.com/kcrisman"
}
```

Seems to work fine on these files.  Running long doctests now but I don't anticipate any more problems.

As to constructor.py, the `-0.1` was removed in the first doctest patch, so the problem was in the test, not the behavior.



---

archive/issue_comments_079512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-04-03T16:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79512",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021167.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-04-19T06:43:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8720#event-21167"
}
```



---

archive/issue_comments_079513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-04-19T06:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8720#issuecomment-79513",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
