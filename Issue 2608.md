# Issue 2608: Sequence(ZZ) should fail gracefully

archive/issues_002608.json:
```json
{
    "body": "Assignee: was\n\nSequence(ZZ) should fail immediately in the first place. In the session below, I entered the command, waited some time and pressed CTRL+C many times. The computation was not only interrupted, but my sage session also crashed. Output below:\n \n\n```\nsage: Sequence(ZZ)\n(CTRL+C pressed repeatedly)\nERROR: Internal Python error in the inspect module.\nBelow is the traceback from this internal error.\n\nTraceback (most recent call last):\n  File \"/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/IPython/ultraTB.py\", line 491, in text\n    records = _fixed_getinnerframes(etb, context,self.tb_offset)\n  File \"/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/IPython/ultraTB.py\", line 124, in _fixed_\ngetinnerframes\n    records  = inspect.getinnerframes(etb, context)\n  File \"/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py\", line 877, in getinnerframes\n    framelist.append((tb.tb_frame,) + getframeinfo(tb, context))\n  File \"/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py\", line 841, in getframeinfo\n    lines, lnum = findsource(frame)\n  File \"/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py\", line 462, in findsource\n\n[...]\n\n  File \"/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.py\", line 9, in my_sigint\n    raise KeyboardInterrupt\nKeyboardInterrupt\n\nUnfortunately, your original traceback can not be constructed.\n\ndfdeshom@sage:~/custom/sage/devel/sage-2577$\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2608\n\n",
    "created_at": "2008-03-20T05:12:50Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "Sequence(ZZ) should fail gracefully",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2608",
    "user": "dfdeshom"
}
```
Assignee: was

Sequence(ZZ) should fail immediately in the first place. In the session below, I entered the command, waited some time and pressed CTRL+C many times. The computation was not only interrupted, but my sage session also crashed. Output below:
 

```
sage: Sequence(ZZ)
(CTRL+C pressed repeatedly)
ERROR: Internal Python error in the inspect module.
Below is the traceback from this internal error.

Traceback (most recent call last):
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 491, in text
    records = _fixed_getinnerframes(etb, context,self.tb_offset)
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 124, in _fixed_
getinnerframes
    records  = inspect.getinnerframes(etb, context)
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py", line 877, in getinnerframes
    framelist.append((tb.tb_frame,) + getframeinfo(tb, context))
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py", line 841, in getframeinfo
    lines, lnum = findsource(frame)
  File "/home/dfdeshom/custom/sage/local/lib/python2.5/inspect.py", line 462, in findsource

[...]

  File "/home/dfdeshom/custom/sage/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.py", line 9, in my_sigint
    raise KeyboardInterrupt
KeyboardInterrupt

Unfortunately, your original traceback can not be constructed.

dfdeshom@sage:~/custom/sage/devel/sage-2577$

```


Issue created by migration from https://trac.sagemath.org/ticket/2608





---

archive/issue_comments_017901.json:
```json
{
    "body": "With sage-4.6.alpha1, I cannot reproduce the crashes anymore.  Doing `Sequence(ZZ)` or `list(ZZ)` will still take forever, but I don't think this is a big problem (`ZZ` is infinite, after all).",
    "created_at": "2010-09-28T21:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2608#issuecomment-17901",
    "user": "jdemeyer"
}
```

With sage-4.6.alpha1, I cannot reproduce the crashes anymore.  Doing `Sequence(ZZ)` or `list(ZZ)` will still take forever, but I don't think this is a big problem (`ZZ` is infinite, after all).



---

archive/issue_comments_017902.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-28T21:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2608#issuecomment-17902",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_017903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-03T00:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2608#issuecomment-17903",
    "user": "dfdeshom"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_017904.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-11-03T08:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2608#issuecomment-17904",
    "user": "jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_comments_017905.json:
```json
{
    "body": "dfdeshom: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames).",
    "created_at": "2010-11-03T08:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2608#issuecomment-17905",
    "user": "jdemeyer"
}
```

dfdeshom: please add your real name to [Account Names mapped to Real Names](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames).
