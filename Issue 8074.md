# Issue 8074: corner cases in RealField and real numbers

archive/issues_008074.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  robertwb was jkantor zimmerma leif\n\nWhat should these return?\n\n\n```\n\nsage: RR('inf').is_real()\nTrue\nsage: RR('nan').is_real()\nTrue\nsage: RR('inf').is_unit()\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8074\n\n",
    "created_at": "2010-01-26T08:37:57Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "corner cases in RealField and real numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8074",
    "user": "jason"
}
```
Assignee: jkantor

CC:  robertwb was jkantor zimmerma leif

What should these return?


```

sage: RR('inf').is_real()
True
sage: RR('nan').is_real()
True
sage: RR('inf').is_unit()
True
```


Issue created by migration from https://trac.sagemath.org/ticket/8074





---

archive/issue_comments_070743.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-01-26T08:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70743",
    "user": "jason"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_070744.json:
```json
{
    "body": "And this:\n\n\n```\nsage: RR('nan').__nonzero__()\nFalse\n\n```\n",
    "created_at": "2010-01-26T08:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70744",
    "user": "jason"
}
```

And this:


```
sage: RR('nan').__nonzero__()
False

```




---

archive/issue_comments_070745.json:
```json
{
    "body": "And another corner case:\n\n\n```\nsage: RR('nan')==RR('nan')\nTrue\n```\n",
    "created_at": "2010-01-26T08:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70745",
    "user": "jason"
}
```

And another corner case:


```
sage: RR('nan')==RR('nan')
True
```




---

archive/issue_comments_070746.json:
```json
{
    "body": "Another one:\n\n\n```\nsage: RR('nan').__pow(0.5)\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.RuntimeError'> ignored\n^CERROR: Internal Python error in the inspect module.\nBelow is the traceback from this internal error.\n\nTraceback (most recent call last):\n  File \"/home/grout/sage/local/lib/python2.6/site-packages/IPython/ultraTB.py\", line 614, in text\n    records = _fixed_getinnerframes(etb, context,self.tb_offset)\n  File \"/home/grout/sage/local/lib/python2.6/site-packages/IPython/ultraTB.py\", line 230, in _fixed_getinnerframes\n    records  = fix_frame_records_filenames(inspect.getinnerframes(etb, context))\n  File \"/home/grout/sage/local/lib/python/inspect.py\", line 942, in getinnerframes\n    framelist.append((tb.tb_frame,) + getframeinfo(tb, context))\n  File \"/home/grout/sage/local/lib/python/inspect.py\", line 902, in getframeinfo\n    filename = getsourcefile(frame) or getfile(frame)\n  File \"/home/grout/sage/local/lib/python/inspect.py\", line 451, in getsourcefile\n    if hasattr(getmodule(object, filename), '__loader__'):\n  File \"/home/grout/sage/local/lib/python/inspect.py\", line 485, in getmodule\n    if ismodule(module) and hasattr(module, '__file__'):\n  File \"/home/grout/sage/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.py\", line 9, in my_sigint\n    raise KeyboardInterrupt\nKeyboardInterrupt\n\nUnfortunately, your original traceback can not be constructed.\n```\n",
    "created_at": "2010-01-26T09:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70746",
    "user": "jason"
}
```

Another one:


```
sage: RR('nan').__pow(0.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.RuntimeError'> ignored
^CERROR: Internal Python error in the inspect module.
Below is the traceback from this internal error.

Traceback (most recent call last):
  File "/home/grout/sage/local/lib/python2.6/site-packages/IPython/ultraTB.py", line 614, in text
    records = _fixed_getinnerframes(etb, context,self.tb_offset)
  File "/home/grout/sage/local/lib/python2.6/site-packages/IPython/ultraTB.py", line 230, in _fixed_getinnerframes
    records  = fix_frame_records_filenames(inspect.getinnerframes(etb, context))
  File "/home/grout/sage/local/lib/python/inspect.py", line 942, in getinnerframes
    framelist.append((tb.tb_frame,) + getframeinfo(tb, context))
  File "/home/grout/sage/local/lib/python/inspect.py", line 902, in getframeinfo
    filename = getsourcefile(frame) or getfile(frame)
  File "/home/grout/sage/local/lib/python/inspect.py", line 451, in getsourcefile
    if hasattr(getmodule(object, filename), '__loader__'):
  File "/home/grout/sage/local/lib/python/inspect.py", line 485, in getmodule
    if ismodule(module) and hasattr(module, '__file__'):
  File "/home/grout/sage/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.py", line 9, in my_sigint
    raise KeyboardInterrupt
KeyboardInterrupt

Unfortunately, your original traceback can not be constructed.
```




---

archive/issue_comments_070747.json:
```json
{
    "body": "\n```\nsage: RR('-inf').__pow(0.5)\n+infinity\nsage: sqrt(RR('-inf'))     \n+infinity*I\n```\n",
    "created_at": "2010-01-26T09:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70747",
    "user": "jason"
}
```


```
sage: RR('-inf').__pow(0.5)
+infinity
sage: sqrt(RR('-inf'))     
+infinity*I
```




---

archive/issue_comments_070748.json:
```json
{
    "body": "Paul,\n\nYou are one of the best experts around on floating point issues.  If you have time, could you comment on the corner cases listed in the description---do you agree with the current output of Sage, or should it be changed?\n\nThanks, Jason\n\n(I put all of the corner cases from #7682 and from the comments on this ticket up in the description.)",
    "created_at": "2010-02-09T17:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70748",
    "user": "jason"
}
```

Paul,

You are one of the best experts around on floating point issues.  If you have time, could you comment on the corner cases listed in the description---do you agree with the current output of Sage, or should it be changed?

Thanks, Jason

(I put all of the corner cases from #7682 and from the comments on this ticket up in the description.)



---

archive/issue_comments_070749.json:
```json
{
    "body": "> You are one of the best experts around on floating point issues...\n\nthanks, you are putting pressure on me! I'll try to do my best...\n\nOne first problem is that `is_real` is not documented, thus I don't know what the intended\nsemantics is or was. In MPFR there is no such function:\n\n```\n -- Function: int mpfr_nan_p (mpfr_t OP)\n -- Function: int mpfr_inf_p (mpfr_t OP)\n -- Function: int mpfr_number_p (mpfr_t OP)\n -- Function: int mpfr_zero_p (mpfr_t OP)\n     Return non-zero if OP is respectively NaN, an infinity, an ordinary\n     number (i.e. neither NaN nor an infinity) or zero. Return zero\n     otherwise.\n```\n\n\nAbout `RR('inf').is_unit()`, if one considers that x is a unit if 1/x is in RR, then since\n1/inf = 0 is in RR, it should return true.\n\n`RR('nan')==RR('nan')` should return False according to IEEE 754.\n\n`RR('nan').__pow(0.5)` should return NaN (here NaN means \"can be any real number\").\n\n`RR('-inf').__pow(0.5)` is ok according to the MPFR rules (here I assume that we try to stay\nin RR):\n\n```\n        * `pow(-Inf, Y)' returns plus infinity for Y positive and not\n          an odd integer.\n```\n\n\nFor `sqrt(RR('-inf'))` it depends on the semantics of the sqrt function. Apparently it\nextends to the complex plane (try `sqrt(RR(-1))`) thus the answer seems ok to me.\n\n`RR('nan').__nonzero__()` is more difficult, since \"NaN\" means \"can be any real\", thus in\nparticular it can be zero, thus the answer should be \"maybe\". If no ternary answer is possible,\nfalse seems the best one.",
    "created_at": "2010-02-09T20:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70749",
    "user": "zimmerma"
}
```

> You are one of the best experts around on floating point issues...

thanks, you are putting pressure on me! I'll try to do my best...

One first problem is that `is_real` is not documented, thus I don't know what the intended
semantics is or was. In MPFR there is no such function:

```
 -- Function: int mpfr_nan_p (mpfr_t OP)
 -- Function: int mpfr_inf_p (mpfr_t OP)
 -- Function: int mpfr_number_p (mpfr_t OP)
 -- Function: int mpfr_zero_p (mpfr_t OP)
     Return non-zero if OP is respectively NaN, an infinity, an ordinary
     number (i.e. neither NaN nor an infinity) or zero. Return zero
     otherwise.
```


About `RR('inf').is_unit()`, if one considers that x is a unit if 1/x is in RR, then since
1/inf = 0 is in RR, it should return true.

`RR('nan')==RR('nan')` should return False according to IEEE 754.

`RR('nan').__pow(0.5)` should return NaN (here NaN means "can be any real number").

`RR('-inf').__pow(0.5)` is ok according to the MPFR rules (here I assume that we try to stay
in RR):

```
        * `pow(-Inf, Y)' returns plus infinity for Y positive and not
          an odd integer.
```


For `sqrt(RR('-inf'))` it depends on the semantics of the sqrt function. Apparently it
extends to the complex plane (try `sqrt(RR(-1))`) thus the answer seems ok to me.

`RR('nan').__nonzero__()` is more difficult, since "NaN" means "can be any real", thus in
particular it can be zero, thus the answer should be "maybe". If no ternary answer is possible,
false seems the best one.



---

archive/issue_comments_070750.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n\n```\nsage: RR('nan').__pow(0.5)\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.RuntimeError'> ignored\n...\n```\n\n\nRegardless of whatever the output of `RR('nan').__pow(0.5)` should be, it is a bug by itself that we don't get a decent exception here...",
    "created_at": "2010-09-28T20:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8074#issuecomment-70750",
    "user": "jdemeyer"
}
```

Replying to [comment:5 jason]:

```
sage: RR('nan').__pow(0.5)
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.RuntimeError'> ignored
...
```


Regardless of whatever the output of `RR('nan').__pow(0.5)` should be, it is a bug by itself that we don't get a decent exception here...
