# Issue 2877: security risk -- several constructors use eval to parse input

archive/issues_002877.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  tscrim slelievre @kliem klee\n\nThere are valid uses for eval() and sage_eval(), it makes it much easier to parse output from  interfaces for example. \n\nIt is difficult (if not impossible) to completely sanitize arbitrary input, but one should be able to be able to (say) write a backend that takes specific data, calls on Sage to process it, and then returns the result. For example, I might want a webpage that uses Sage to compute Julia sets, and takes as input a complex number. That the following work is scary \n\n\n```\nsage: CC(\"os.getpid()\")\n10324.0000000000\nsage: CC(\"os.mkdir('a')\")\nNaN - NaN*I\nsage: CC(\"os.rmdir('a')\")\nNaN - NaN*I\nsage: CC(\"os.exec(...)\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2877\n\n",
    "created_at": "2008-04-11T11:39:56Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.5",
    "title": "security risk -- several constructors use eval to parse input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2877",
    "user": "robertwb"
}
```
Assignee: cwitty

CC:  tscrim slelievre @kliem klee

There are valid uses for eval() and sage_eval(), it makes it much easier to parse output from  interfaces for example. 

It is difficult (if not impossible) to completely sanitize arbitrary input, but one should be able to be able to (say) write a backend that takes specific data, calls on Sage to process it, and then returns the result. For example, I might want a webpage that uses Sage to compute Julia sets, and takes as input a complex number. That the following work is scary 


```
sage: CC("os.getpid()")
10324.0000000000
sage: CC("os.mkdir('a')")
NaN - NaN*I
sage: CC("os.rmdir('a')")
NaN - NaN*I
sage: CC("os.exec(...)")
```


Issue created by migration from https://trac.sagemath.org/ticket/2877





---

archive/issue_comments_019760.json:
```json
{
    "body": "See #2347 which is related.",
    "created_at": "2008-04-11T11:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19760",
    "user": "robertwb"
}
```

See #2347 which is related.



---

archive/issue_comments_019761.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19761",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_019762.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-02T09:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19762",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019763.json:
```json
{
    "body": "Sage is not a secure program and nobody ever claimed it was. Sanitise your input before sending it to Sage!",
    "created_at": "2014-09-02T09:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19763",
    "user": "jdemeyer"
}
```

Sage is not a secure program and nobody ever claimed it was. Sanitise your input before sending it to Sage!



---

archive/issue_comments_019764.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-02T09:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19764",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019765.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-09-09T14:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19765",
    "user": "vbraun"
}
```

Resolution: invalid



---

archive/issue_comments_019766.json:
```json
{
    "body": "A strange response coming from Jeroen.  The use of `sage_eval` to convert arbitrary string inputs to elements of different fields is, I think, obviously bad on so many levels, and badly mishandled in several cases (e.g. some of them will catch `NameError`s, but not `SyntaxError`s; some will just work, but in weird ways, if you pass some arbitrary string; some are just broken as in https://ask.sagemath.org/question/47068/possible-bug-in-cc-needs-confirmation )\n\nIf you want to convert string representations of some elements of a field to actual elements of that field there should be proper parsing, not just arbitrary evals.",
    "created_at": "2019-07-05T16:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19766",
    "user": "embray"
}
```

A strange response coming from Jeroen.  The use of `sage_eval` to convert arbitrary string inputs to elements of different fields is, I think, obviously bad on so many levels, and badly mishandled in several cases (e.g. some of them will catch `NameError`s, but not `SyntaxError`s; some will just work, but in weird ways, if you pass some arbitrary string; some are just broken as in https://ask.sagemath.org/question/47068/possible-bug-in-cc-needs-confirmation )

If you want to convert string representations of some elements of a field to actual elements of that field there should be proper parsing, not just arbitrary evals.



---

archive/issue_comments_019767.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2019-07-05T16:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19767",
    "user": "embray"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_019768.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2019-07-05T16:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19768",
    "user": "embray"
}
```

Changing status from closed to new.



---

archive/issue_comments_019769.json:
```json
{
    "body": "A simpler fix would be to use a limited eval, e.g. https://newville.github.io/asteval/\n\nThe reason for the eval in CC is of course that you want to allow expressions like `2+3*I` that exceed python's `literal_eval` capabilities.",
    "created_at": "2019-07-06T12:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19769",
    "user": "vbraun"
}
```

A simpler fix would be to use a limited eval, e.g. https://newville.github.io/asteval/

The reason for the eval in CC is of course that you want to allow expressions like `2+3*I` that exceed python's `literal_eval` capabilities.



---

archive/issue_comments_019770.json:
```json
{
    "body": "I fully agree with Erik.\n\nThe following does not work (as expected)\n\n```\nsage: ZZ('2**3 + 3*g - 2')\nTraceback (most recent call last):\n...\nTypeError: unable to convert '2**3 + 3*g - 2' to an integer\nsage: RR('2**2 + 3*5 - 2')\nTraceback (most recent call last):\n...\nTypeError: unable to convert '2**3+5*I-2' to a real number\n```\n\nSupporting the following with `CC` is a nonsense\n\n```\nsage: CC('2**2 + 3*5 - 2')\n17.0000000000000\nsage: CC('erf(2)')\n0.995322265018953\n```\n\nWe don't want the element constructor to evaluate a string in hope that it gives a complex number. There should be a clear definition of what is the input format. And the constructor should just stick to specifications. The element constructor of CC is trying to do much more than what it is supposed to.",
    "created_at": "2019-07-11T19:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19770",
    "user": "vdelecroix"
}
```

I fully agree with Erik.

The following does not work (as expected)

```
sage: ZZ('2**3 + 3*g - 2')
Traceback (most recent call last):
...
TypeError: unable to convert '2**3 + 3*g - 2' to an integer
sage: RR('2**2 + 3*5 - 2')
Traceback (most recent call last):
...
TypeError: unable to convert '2**3+5*I-2' to a real number
```

Supporting the following with `CC` is a nonsense

```
sage: CC('2**2 + 3*5 - 2')
17.0000000000000
sage: CC('erf(2)')
0.995322265018953
```

We don't want the element constructor to evaluate a string in hope that it gives a complex number. There should be a clear definition of what is the input format. And the constructor should just stick to specifications. The element constructor of CC is trying to do much more than what it is supposed to.



---

archive/issue_comments_019771.json:
```json
{
    "body": "And to my mind the main problem is **not** the security risk (I agree with Jeroen on that point). I would advice to open another ticket \"fix element constructor of CC\".",
    "created_at": "2019-07-11T19:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19771",
    "user": "vdelecroix"
}
```

And to my mind the main problem is **not** the security risk (I agree with Jeroen on that point). I would advice to open another ticket "fix element constructor of CC".



---

archive/issue_comments_019772.json:
```json
{
    "body": "It's not just CC.  It's all of them.  It's really flaky to allow a general eval to construct instances of some particular type.  Instead, it should really just parse constant-valued expressions for whatever that type is, at the most.  That can either involve custom parsing code, or as Volker suggested a custom AST parser.",
    "created_at": "2019-07-12T08:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19772",
    "user": "embray"
}
```

It's not just CC.  It's all of them.  It's really flaky to allow a general eval to construct instances of some particular type.  Instead, it should really just parse constant-valued expressions for whatever that type is, at the most.  That can either involve custom parsing code, or as Volker suggested a custom AST parser.



---

archive/issue_comments_019773.json:
```json
{
    "body": "Replying to [comment:12 vbraun]:\n> A simpler fix would be to use a limited eval, e.g. https://newville.github.io/asteval/\n> \n> The reason for the eval in CC is of course that you want to allow expressions like `2+3*I` that exceed python's `literal_eval` capabilities.\n\n+1",
    "created_at": "2019-07-12T08:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19773",
    "user": "embray"
}
```

Replying to [comment:12 vbraun]:
> A simpler fix would be to use a limited eval, e.g. https://newville.github.io/asteval/
> 
> The reason for the eval in CC is of course that you want to allow expressions like `2+3*I` that exceed python's `literal_eval` capabilities.

+1



---

archive/issue_comments_019774.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2019-12-30T14:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19774",
    "user": "embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_comments_019775.json:
```json
{
    "body": "Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.",
    "created_at": "2020-04-14T19:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19775",
    "user": "mkoeppe"
}
```

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.



---

archive/issue_comments_019776.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19776",
    "user": "mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_comments_019777.json:
```json
{
    "body": "here is a simple-minded patch. Unless somebody proposes something better, I think it makes sense to merge that now\n----\nNew commits:",
    "created_at": "2021-10-19T15:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19777",
    "user": "chapoton"
}
```

here is a simple-minded patch. Unless somebody proposes something better, I think it makes sense to merge that now
----
New commits:



---

archive/issue_comments_019778.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-10-19T15:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19778",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019779.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-10-19T18:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19779",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_019780.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-10-20T07:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19780",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019781.json:
```json
{
    "body": "bot is morally green, so please review",
    "created_at": "2021-10-20T11:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19781",
    "user": "chapoton"
}
```

bot is morally green, so please review



---

archive/issue_comments_019782.json:
```json
{
    "body": "Do we also want to allow `j` to match Python's convention for complex numbers:\n\n```sage\nsage: complex('1+2j')\n(1+2j)\nsage: complex('1+2i')\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n<ipython-input-2-a2113f9c148b> in <module>\n----> 1 complex('1+2i')\n\nValueError: complex() arg is a malformed string\n```\n",
    "created_at": "2021-10-20T23:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19782",
    "user": "tscrim"
}
```

Do we also want to allow `j` to match Python's convention for complex numbers:

```sage
sage: complex('1+2j')
(1+2j)
sage: complex('1+2i')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-a2113f9c148b> in <module>
----> 1 complex('1+2i')

ValueError: complex() arg is a malformed string
```




---

archive/issue_comments_019783.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-10-21T07:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19783",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_019784.json:
```json
{
    "body": "ok, done (and squashed the commits)",
    "created_at": "2021-10-21T07:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19784",
    "user": "chapoton"
}
```

ok, done (and squashed the commits)



---

archive/issue_comments_019785.json:
```json
{
    "body": "but this will break the doctest in singular.pyx... (sigh)",
    "created_at": "2021-10-21T07:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19785",
    "user": "chapoton"
}
```

but this will break the doctest in singular.pyx... (sigh)



---

archive/issue_comments_019786.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-10-21T07:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19786",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_019787.json:
```json
{
    "body": "bot is morally green now",
    "created_at": "2021-10-21T11:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19787",
    "user": "chapoton"
}
```

bot is morally green now



---

archive/issue_comments_019788.json:
```json
{
    "body": "Sorry for late comment, but how about this?\n\n```diff\n--- a/src/sage/rings/complex_mpfr.pyx\n+++ b/src/sage/rings/complex_mpfr.pyx\n@@ -504,7 +504,7 @@ class ComplexField_class(sage.rings.abc.ComplexField):\n             sage: CC('hello')\n             Traceback (most recent call last):\n             ...\n-            ValueError: given string (hello) is not a complex number\n+            ValueError: given string 'hello' is not a complex number\n         \"\"\"\n         if not isinstance(x, (RealNumber, tuple)):\n             if isinstance(x, ComplexDoubleElement):\n@@ -516,7 +516,7 @@ class ComplexField_class(sage.rings.abc.ComplexField):\n                 x = x.replace('E', 'e')\n                 allowed = '+-.*0123456789Ie'\n                 if not all(letter in allowed for letter in x):\n-                    raise ValueError(f'given string ({x}) is not a complex number')\n+                    raise ValueError(f'given string {x!r} is not a complex number')\n                 # This should rather use a proper parser to validate input.\n                 # TODO: this is probably not the best and most\n                 # efficient way to do this.  -- Martin Albrecht\n```\n\n\nand `does not express a complex number`.",
    "created_at": "2021-10-22T04:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19788",
    "user": "klee"
}
```

Sorry for late comment, but how about this?

```diff
--- a/src/sage/rings/complex_mpfr.pyx
+++ b/src/sage/rings/complex_mpfr.pyx
@@ -504,7 +504,7 @@ class ComplexField_class(sage.rings.abc.ComplexField):
             sage: CC('hello')
             Traceback (most recent call last):
             ...
-            ValueError: given string (hello) is not a complex number
+            ValueError: given string 'hello' is not a complex number
         """
         if not isinstance(x, (RealNumber, tuple)):
             if isinstance(x, ComplexDoubleElement):
@@ -516,7 +516,7 @@ class ComplexField_class(sage.rings.abc.ComplexField):
                 x = x.replace('E', 'e')
                 allowed = '+-.*0123456789Ie'
                 if not all(letter in allowed for letter in x):
-                    raise ValueError(f'given string ({x}) is not a complex number')
+                    raise ValueError(f'given string {x!r} is not a complex number')
                 # This should rather use a proper parser to validate input.
                 # TODO: this is probably not the best and most
                 # efficient way to do this.  -- Martin Albrecht
```


and `does not express a complex number`.



---

archive/issue_comments_019789.json:
```json
{
    "body": "Thank you. I am also wondering a bit if we want to document that `CC` also supports `j` as a valid string input. Although I don't hold a strong opinion on this.",
    "created_at": "2021-10-22T05:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19789",
    "user": "tscrim"
}
```

Thank you. I am also wondering a bit if we want to document that `CC` also supports `j` as a valid string input. Although I don't hold a strong opinion on this.



---

archive/issue_comments_019790.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-10-22T06:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19790",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_019791.json:
```json
{
    "body": "ok, done.\n\nWARNING: note that CC('1.0+2.0*j') works, but not CC('1.0+2.0j').",
    "created_at": "2021-10-22T06:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19791",
    "user": "chapoton"
}
```

ok, done.

WARNING: note that CC('1.0+2.0*j') works, but not CC('1.0+2.0j').



---

archive/issue_comments_019792.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-10-24T07:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19792",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_019793.json:
```json
{
    "body": "I fixed the failing doctest",
    "created_at": "2021-10-24T07:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19793",
    "user": "chapoton"
}
```

I fixed the failing doctest



---

archive/issue_comments_019794.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-24T23:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19794",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019795.json:
```json
{
    "body": "Great, thank you. LGTM. Kwankyu, if you do not agree, feel free to revert the positive review.",
    "created_at": "2021-10-24T23:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19795",
    "user": "tscrim"
}
```

Great, thank you. LGTM. Kwankyu, if you do not agree, feel free to revert the positive review.



---

archive/issue_comments_019796.json:
```json
{
    "body": "Replying to [comment:39 tscrim]:\n> Great, thank you. LGTM. Kwankyu, if you do not agree, feel free to revert the positive review.\n\nI fully agree. Thanks.",
    "created_at": "2021-10-25T06:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19796",
    "user": "klee"
}
```

Replying to [comment:39 tscrim]:
> Great, thank you. LGTM. Kwankyu, if you do not agree, feel free to revert the positive review.

I fully agree. Thanks.



---

archive/issue_comments_019797.json:
```json
{
    "body": "Update ticket summary and description\nto better describe the changes made here?\n\n(Or just contract \"should be able to be able to\"\nif the rest is still fine?)",
    "created_at": "2021-10-25T09:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19797",
    "user": "slelievre"
}
```

Update ticket summary and description
to better describe the changes made here?

(Or just contract "should be able to be able to"
if the rest is still fine?)



---

archive/issue_comments_019798.json:
```json
{
    "body": "voil\u00e0, voil\u00e0.",
    "created_at": "2021-10-25T12:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19798",
    "user": "chapoton"
}
```

voilà, voilà.



---

archive/issue_comments_019799.json:
```json
{
    "body": "Merci.",
    "created_at": "2021-10-25T12:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19799",
    "user": "slelievre"
}
```

Merci.



---

archive/issue_comments_019800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-10-28T22:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2877",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2877#issuecomment-19800",
    "user": "vbraun"
}
```

Resolution: fixed
