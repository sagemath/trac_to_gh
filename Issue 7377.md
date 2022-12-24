# Issue 7377: Symbolic Ring to Maxima via EclObject

archive/issues_007377.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @burcin @saliola jpflori\n\nThis ticket is dependent on #6781, #7287.\n\nWith maxima-as-an-ecl-library and ecl accessible as a library, we can start interfacing with maxima via a binary library interface.\nThis should be more efficient and more robust, because expressions\ncan be transmitted in a much richer format than text and parsing does\nnot have to recognise error messages and questions (since communication does not go via STDIN/STDOUT anymore)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7377\n\n",
    "created_at": "2009-11-03T08:05:51Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Symbolic Ring to Maxima via EclObject",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7377",
    "user": "@nbruin"
}
```
Assignee: @burcin

CC:  @burcin @saliola jpflori

This ticket is dependent on #6781, #7287.

With maxima-as-an-ecl-library and ecl accessible as a library, we can start interfacing with maxima via a binary library interface.
This should be more efficient and more robust, because expressions
can be transmitted in a much richer format than text and parsing does
not have to recognise error messages and questions (since communication does not go via STDIN/STDOUT anymore)

Issue created by migration from https://trac.sagemath.org/ticket/7377





---

archive/issue_comments_061819.json:
```json
{
    "body": "Attachment [sagemax.py](tarball://root/attachments/some-uuid/ticket7377/sagemax.py) by @nbruin created at 2009-11-03 08:06:44\n\nexample package for how to accomplish said interface",
    "created_at": "2009-11-03T08:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61819",
    "user": "@nbruin"
}
```

Attachment [sagemax.py](tarball://root/attachments/some-uuid/ticket7377/sagemax.py) by @nbruin created at 2009-11-03 08:06:44

example package for how to accomplish said interface



---

archive/issue_comments_061820.json:
```json
{
    "body": "Changing assignee from @burcin to @nbruin.",
    "created_at": "2009-11-03T08:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61820",
    "user": "@nbruin"
}
```

Changing assignee from @burcin to @nbruin.



---

archive/issue_comments_061821.json:
```json
{
    "body": "I think the following email might be of interest to other people wanting to hack maxima:\n\n> Since there is already a decent string parser for taking Sage stuff to\n> Maxima and (especially) getting back Sage stuff from Maxima, would\n> there be a way to modify the above - or ecl_eval - to give back the\n> Maxima expression directly?  Perhaps this is already in the\n> lib/ecl.pyx file, though I didn't see it on the first reading.\n\nlib/ecl.pyx has nothing to do with maxima-specific stuff. That is all in\nsagemax.py. It is actually a little bit important to keep that distinction.\nMaxima is not the only lisp program we might want to interface with.\n\nThere is `max_read(S) = cadadr(EclObject(\"#$%s\"%S))`, which *reads* the string\nS as a maxima expression and returns its parsed result.\n\nSo `meval(max_read(S))` would do the trick. I do not know what routines maxima\nhas to convert expressions to a string. If I wanted to know, I would find it\nout by looking at something like\n\n`max_read(\"maxima-command-to-print-to-string(x)\")`\n\nand see what token the maxima reader puts in. I imagine you get something\nlike\n\n\n```\n<ECL: ((MAX-PRINT-STRING) x)>\n```\n\n\nback, So do:\n\n\n```\nmaxprint:=EclObject(\"MAX-PRINT-STRING\") #do this once globally\nmeval(EclObject([[maxprint], maxexpression])).python()\n```\n\n\nIndeed:\n\n\n```\nsage: max_read(\"string(x)\")\n<ECL: (($STRING) $X)>\nsage: meval(max_read(\"string(x)\"))\n<ECL: \"x\">\nsage: meval(max_read(\"string(x)\")).python()\n'\"x\"'\nsage: meval(max_read(\"string(x)\")).python()[1:-1]\n'x'\n```\n\n\nSo\n\n\n```\nsage: maxprint=EclObject(\"$STRING\")\nsage: def max_to_string(s):\n....:      return meval(EclObject([[maxprint],s])).python()[1:-1]\n```\n\n\nwould give you a string representation. Be aware that #$...$ suffers from\nperformance loss, so if you repeatedly use it, your timings will go south\nquickly. See Dodier's comments on this a while ago. Apparently you could\npatch Maxima to lose the performance-losing routine (at the expense of\nlosing the wonderful linear-search history the maxima parser offers now).\n\n> Sage command -> calls Maxima command -> Maxima command evaluated, but\n> in the ECL library version, not the pexpect version -> Maxima output\n> (a string) converted back using the stuff in Sage\n\nYes, that would be an approach virtually orthogonal to the one taken in sagemax.py.\n\n\n```\n> sage: str(ecl_eval(\"#$load(to_poly_solver)$\"))\n> append: argument must be a non-atomic expression; found false\n> -- an error.  To debug this try debugmode(true);\n```\n\nTo illustrate the inner workings:\n\n\n```\nsage: from sagemax import *\nsage: e=max_read('load(\"to_poly_solver\")')\nsage: e\n<ECL: (($LOAD) \"to_poly_solver\")>\nsage: meval(e)\nappend: argument must be a non-atomic expression; found false\n -- an error.  To debug this try debugmode(true);\n\nsage: meval(max_read(\"append(a,b)\"))\nappend: argument must be a non-atomic expression; found a\n -- an error.  To debug this try debugmode(true);\n```\n\n\nSo my guess is that \"load\" is trying to append to an improperly initialized\nmaxima list. I guess that means that in the current setting, our maxima\nenvironment hasn't properly been set up yet. That is no surprise. It is\nactually surprising that so much of maxima works without any initialization\nat all.",
    "created_at": "2009-11-04T17:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61821",
    "user": "@nbruin"
}
```

I think the following email might be of interest to other people wanting to hack maxima:

> Since there is already a decent string parser for taking Sage stuff to
> Maxima and (especially) getting back Sage stuff from Maxima, would
> there be a way to modify the above - or ecl_eval - to give back the
> Maxima expression directly?  Perhaps this is already in the
> lib/ecl.pyx file, though I didn't see it on the first reading.

lib/ecl.pyx has nothing to do with maxima-specific stuff. That is all in
sagemax.py. It is actually a little bit important to keep that distinction.
Maxima is not the only lisp program we might want to interface with.

There is `max_read(S) = cadadr(EclObject("#$%s"%S))`, which *reads* the string
S as a maxima expression and returns its parsed result.

So `meval(max_read(S))` would do the trick. I do not know what routines maxima
has to convert expressions to a string. If I wanted to know, I would find it
out by looking at something like

`max_read("maxima-command-to-print-to-string(x)")`

and see what token the maxima reader puts in. I imagine you get something
like


```
<ECL: ((MAX-PRINT-STRING) x)>
```


back, So do:


```
maxprint:=EclObject("MAX-PRINT-STRING") #do this once globally
meval(EclObject([[maxprint], maxexpression])).python()
```


Indeed:


```
sage: max_read("string(x)")
<ECL: (($STRING) $X)>
sage: meval(max_read("string(x)"))
<ECL: "x">
sage: meval(max_read("string(x)")).python()
'"x"'
sage: meval(max_read("string(x)")).python()[1:-1]
'x'
```


So


```
sage: maxprint=EclObject("$STRING")
sage: def max_to_string(s):
....:      return meval(EclObject([[maxprint],s])).python()[1:-1]
```


would give you a string representation. Be aware that #$...$ suffers from
performance loss, so if you repeatedly use it, your timings will go south
quickly. See Dodier's comments on this a while ago. Apparently you could
patch Maxima to lose the performance-losing routine (at the expense of
losing the wonderful linear-search history the maxima parser offers now).

> Sage command -> calls Maxima command -> Maxima command evaluated, but
> in the ECL library version, not the pexpect version -> Maxima output
> (a string) converted back using the stuff in Sage

Yes, that would be an approach virtually orthogonal to the one taken in sagemax.py.


```
> sage: str(ecl_eval("#$load(to_poly_solver)$"))
> append: argument must be a non-atomic expression; found false
> -- an error.  To debug this try debugmode(true);
```

To illustrate the inner workings:


```
sage: from sagemax import *
sage: e=max_read('load("to_poly_solver")')
sage: e
<ECL: (($LOAD) "to_poly_solver")>
sage: meval(e)
append: argument must be a non-atomic expression; found false
 -- an error.  To debug this try debugmode(true);

sage: meval(max_read("append(a,b)"))
append: argument must be a non-atomic expression; found a
 -- an error.  To debug this try debugmode(true);
```


So my guess is that "load" is trying to append to an improperly initialized
maxima list. I guess that means that in the current setting, our maxima
environment hasn't properly been set up yet. That is no surprise. It is
actually surprising that so much of maxima works without any initialization
at all.



---

archive/issue_comments_061822.json:
```json
{
    "body": "Attachment [7377-abstract-maxima.patch](tarball://root/attachments/some-uuid/ticket7377/7377-abstract-maxima.patch) by @robertwb created at 2010-01-17 06:33:44",
    "created_at": "2010-01-17T06:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61822",
    "user": "@robertwb"
}
```

Attachment [7377-abstract-maxima.patch](tarball://root/attachments/some-uuid/ticket7377/7377-abstract-maxima.patch) by @robertwb created at 2010-01-17 06:33:44



---

archive/issue_comments_061823.json:
```json
{
    "body": "Finally success! Recipe for getting calculus use\nmaxima in ecl library mode do the following\n* apply the patch from #6781\n* apply Robert's 7377-abstract-maxima.patch\n* apply maxlib.patch\nThe calculus doctests currently fail because maxima asking questions does not get handled yet.",
    "created_at": "2010-01-17T08:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61823",
    "user": "@nbruin"
}
```

Finally success! Recipe for getting calculus use
maxima in ecl library mode do the following
* apply the patch from #6781
* apply Robert's 7377-abstract-maxima.patch
* apply maxlib.patch
The calculus doctests currently fail because maxima asking questions does not get handled yet.



---

archive/issue_comments_061824.json:
```json
{
    "body": "Updated maxlib.patch. Changes made:\n* Code catches (throw 'macsyma-quit) and tries to recognise errors (often successful)\n* suppress questions and throw errors instead\n* suppress \";;; load ...\" lines and load warnings\n* set environment appropriately for calculus instance\nThere is a nasty problem that \"forget(facts())\" gets executed by sage, but throws errors. These get caught by the classic interface, but mess up the printing.\n\nDoctesting calculus/calculus.py leads to 10 failures. All have to do with either forget() acting up or the fact that \"maxima asks a question\" gets reported differently by the two interfaces.\n\n(the uploaded code has some diagnostic output in `maxima_eval` to try to debug the \"forget\" issues. The \"ask\" errors should just consist of updating the doctest.\n\nGo at it!",
    "created_at": "2010-01-18T01:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61824",
    "user": "@nbruin"
}
```

Updated maxlib.patch. Changes made:
* Code catches (throw 'macsyma-quit) and tries to recognise errors (often successful)
* suppress questions and throw errors instead
* suppress ";;; load ..." lines and load warnings
* set environment appropriately for calculus instance
There is a nasty problem that "forget(facts())" gets executed by sage, but throws errors. These get caught by the classic interface, but mess up the printing.

Doctesting calculus/calculus.py leads to 10 failures. All have to do with either forget() acting up or the fact that "maxima asks a question" gets reported differently by the two interfaces.

(the uploaded code has some diagnostic output in `maxima_eval` to try to debug the "forget" issues. The "ask" errors should just consist of updating the doctest.

Go at it!



---

archive/issue_comments_061825.json:
```json
{
    "body": "Maxima via library; used by calculus",
    "created_at": "2010-01-19T09:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61825",
    "user": "@nbruin"
}
```

Maxima via library; used by calculus



---

archive/issue_comments_061826.json:
```json
{
    "body": "Attachment [maxlib.patch](tarball://root/attachments/some-uuid/ticket7377/maxlib.patch) by @nbruin created at 2010-01-19 09:15:05\n\nAnother update:\n\n* change to symbolic/assumptions.py to not try: ... error: pass (gentler removal of assumptions makes the interface behave a bit better)\n\n* monkey patch maxima to throw error on divergent integral instead of *printing* \"Principal Value\" and giving an answer.\n(maxima does behave as documented, so it is a matter of taste to change maxima's behaviour)\n\n* slightly more pretty/informative error messages\n\nDoctests failures on calculus.py are only 5 and are restricted to whitespace and differently formatted error messages (in other words, for real use, the two interfaces shouldn't be distinguishable anymore).",
    "created_at": "2010-01-19T09:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61826",
    "user": "@nbruin"
}
```

Attachment [maxlib.patch](tarball://root/attachments/some-uuid/ticket7377/maxlib.patch) by @nbruin created at 2010-01-19 09:15:05

Another update:

* change to symbolic/assumptions.py to not try: ... error: pass (gentler removal of assumptions makes the interface behave a bit better)

* monkey patch maxima to throw error on divergent integral instead of *printing* "Principal Value" and giving an answer.
(maxima does behave as documented, so it is a matter of taste to change maxima's behaviour)

* slightly more pretty/informative error messages

Doctests failures on calculus.py are only 5 and are restricted to whitespace and differently formatted error messages (in other words, for real use, the two interfaces shouldn't be distinguishable anymore).



---

archive/issue_comments_061827.json:
```json
{
    "body": "Very sadly I do not have time right now to look at this properly, but if it behaves as advertised, the layout is very understandable and I think might even improve the previous interface in terms of future customization.  \n\nDo you think you can post some sample timings, just for information?  After all, one (not the only) reason for this would be to significantly speed up repeated use of Maxima for certain applications.\n\nThanks to nbruin and robertwb for working so hard on this!",
    "created_at": "2010-02-04T14:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61827",
    "user": "@kcrisman"
}
```

Very sadly I do not have time right now to look at this properly, but if it behaves as advertised, the layout is very understandable and I think might even improve the previous interface in terms of future customization.  

Do you think you can post some sample timings, just for information?  After all, one (not the only) reason for this would be to significantly speed up repeated use of Maxima for certain applications.

Thanks to nbruin and robertwb for working so hard on this!



---

archive/issue_comments_061828.json:
```json
{
    "body": "Patch to get faster calculus routines",
    "created_at": "2010-02-09T05:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61828",
    "user": "@nbruin"
}
```

Patch to get faster calculus routines



---

archive/issue_comments_061829.json:
```json
{
    "body": "Attachment [fastcalculus.patch](tarball://root/attachments/some-uuid/ticket7377/fastcalculus.patch) by @nbruin created at 2010-02-09 06:05:29\n\nThe latest patch must be applied after `abstract-maxima` and `maxlib`. It adds routines `sr_to_max` and `max_to_sr` that try to translate between maxima's internal datastructure and SR while avoiding string transformations as much as possible. It falls back to the old interface to establish many of its symbol and operator translations, but takes note of them and uses a dictionary directly the next time around. It also avoids the overhead of binding expressions to maxima variables.\n\nto go back and forth, `maxima_lib.MaximaElement()` as a new function {ecl()} which passes back the underlying EclObject. Conversely, `maxima_lib.maxima` accepts EclObjects and returns a corresponding expect interface object.\n\nThis patch also rewrite calculus integral, limit and sum to directly pass back and forth to maxima. There is a lot of overhead in SR itself, so speed gains are not that big. New times are:\n\n```\nsage: timeit(\"integral(cos(x),x)\")\n625 loops, best of 3: 1.1 ms per loop\nsage: timeit(\"integral(cos(x^2),x)\")\n5 loops, best of 3: 31.2 ms per loop\n```\n\nwhere old were\n\n```\nsage: timeit(\"integral(cos(x),x)\")\n25 loops, best of 3: 8.08 ms per loop\nsage: timeit(\"integral(cos(x^2),x)\")\n5 loops, best of 3: 37 ms per loop\n```\n\n\nIt is easy to swap the old and new interfaces: simply comment/uncomment the appropriate lines in `calculus.py` to define the appropriate calculus.maxima\n\nThere are 7 doctest failures in `calculus.py`. All of them are whitespace, errors and changed precision in floats:\nthe binary interface passes `double`s directly, so there are no digits rounded. This affects some doctests. In other words, as far is `calculus.py` is concerned the two interfaces are functionally equivalent.",
    "created_at": "2010-02-09T06:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61829",
    "user": "@nbruin"
}
```

Attachment [fastcalculus.patch](tarball://root/attachments/some-uuid/ticket7377/fastcalculus.patch) by @nbruin created at 2010-02-09 06:05:29

The latest patch must be applied after `abstract-maxima` and `maxlib`. It adds routines `sr_to_max` and `max_to_sr` that try to translate between maxima's internal datastructure and SR while avoiding string transformations as much as possible. It falls back to the old interface to establish many of its symbol and operator translations, but takes note of them and uses a dictionary directly the next time around. It also avoids the overhead of binding expressions to maxima variables.

to go back and forth, `maxima_lib.MaximaElement()` as a new function {ecl()} which passes back the underlying EclObject. Conversely, `maxima_lib.maxima` accepts EclObjects and returns a corresponding expect interface object.

This patch also rewrite calculus integral, limit and sum to directly pass back and forth to maxima. There is a lot of overhead in SR itself, so speed gains are not that big. New times are:

```
sage: timeit("integral(cos(x),x)")
625 loops, best of 3: 1.1 ms per loop
sage: timeit("integral(cos(x^2),x)")
5 loops, best of 3: 31.2 ms per loop
```

where old were

```
sage: timeit("integral(cos(x),x)")
25 loops, best of 3: 8.08 ms per loop
sage: timeit("integral(cos(x^2),x)")
5 loops, best of 3: 37 ms per loop
```


It is easy to swap the old and new interfaces: simply comment/uncomment the appropriate lines in `calculus.py` to define the appropriate calculus.maxima

There are 7 doctest failures in `calculus.py`. All of them are whitespace, errors and changed precision in floats:
the binary interface passes `double`s directly, so there are no digits rounded. This affects some doctests. In other words, as far is `calculus.py` is concerned the two interfaces are functionally equivalent.



---

archive/issue_comments_061830.json:
```json
{
    "body": "Does this need any rebasing? I am willing to give it a spin in sage-on-gentoo\nto see if there are any obvious problems on linux.",
    "created_at": "2010-11-16T02:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61830",
    "user": "@kiwifb"
}
```

Does this need any rebasing? I am willing to give it a spin in sage-on-gentoo
to see if there are any obvious problems on linux.



---

archive/issue_comments_061831.json:
```json
{
    "body": "Replying to [comment:11 fbissey]:\n> Does this need any rebasing?\n\nUnfortunately, it does. Since Robert split off the Maxima pexpect interface, there were a few minor changes to `sage/interfaces/maxima.py`. His patch needs to be rebased.\n\nAFAIR, the only reason that held this ticket back was a mix-up in the updates to the ecl/maxima packages. The version that properly built maxima as a library got lost since there were several new packages at the same time. I don't know if that problem is fixed in the latest release.",
    "created_at": "2010-11-16T14:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61831",
    "user": "@burcin"
}
```

Replying to [comment:11 fbissey]:
> Does this need any rebasing?

Unfortunately, it does. Since Robert split off the Maxima pexpect interface, there were a few minor changes to `sage/interfaces/maxima.py`. His patch needs to be rebased.

AFAIR, the only reason that held this ticket back was a mix-up in the updates to the ecl/maxima packages. The version that properly built maxima as a library got lost since there were several new packages at the same time. I don't know if that problem is fixed in the latest release.



---

archive/issue_comments_061832.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-11-16T14:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61832",
    "user": "@burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_061833.json:
```json
{
    "body": "Note that there's a ticket to update both Maxima and ECL open just now. See #10187\n\nAt this point in time, it does not have positive review, but I think it is pretty close to getting it. The packages work together, but there's a doctest failure which needs to be resolved. As far as I can see, its just that Maxima is outputing results in a different form (yet again). \n\nI would suggest you use the packages at #10187 and make this dependent on that, which I think will be merged in the next alpha.",
    "created_at": "2010-11-17T11:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61833",
    "user": "drkirkby"
}
```

Note that there's a ticket to update both Maxima and ECL open just now. See #10187

At this point in time, it does not have positive review, but I think it is pretty close to getting it. The packages work together, but there's a doctest failure which needs to be resolved. As far as I can see, its just that Maxima is outputing results in a different form (yet again). 

I would suggest you use the packages at #10187 and make this dependent on that, which I think will be merged in the next alpha.



---

archive/issue_comments_061834.json:
```json
{
    "body": "I tried to update the patches so that they apply on Sage 4.6.1 with Maxima 5.22.1, some things moved since the last patches were produced, but there was nothing too terrible. I'll up them right now.\n\nHowever, there is now a problem when loading Maxima as a library. Maybe some changes in the spkg (in init-cl.lisp where set-pathnames is defined ?) are responsible for this. Without that line, there is a problem later.\n\n\n```\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py in <module>()\n    487 ecl_eval(\"(defvar *MAXIMA-LANG-SUBDIR* NIL)\")\n    488 ecl_eval(\"(set-locale-subdir)\")\n--> 489 ecl_eval(\"(set-pathnames)\")\n    490 ecl_eval(\"(defun add-lineinfo (x) x)\")\n    491 ecl_eval(\"\"\"(defun retrieve (msg flag &aux (print? nil))(error (concatenate 'string \"Maxima asks:\" (meval (list '($string) msg)))))\"\"\")\n\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5616)()\n\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5570)()\n\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2403)()\n\nRuntimeError: ECL says: In function PATHNAME, the value of the only argument is\n  NIL\nwhich is not of the expected type (OR FILE-STREAM STRING PATHNAME)\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n\n```\n\nI don't know anything about Lisp, ECL and Maxima, so I was not able to fix that in the little time I tried.\n\nAs far as the patches as concerned, I feel that more work is needed. Deleting duplicate examples and methods, moving the library interface to libs directory, not sure where maxima abstract should go (if it is kept, should something be done like MaximaLib/Maxima as for Pari/GP ? no idea if those two \"interfaces\" share something...), getting rid of the inheritance on Expect in Maxima_lib and Maxima_abstract.\n\nI'm ready to have a look at all of this, if someone helps me launching Maxima as library with latest versions of everything.",
    "created_at": "2011-01-24T09:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61834",
    "user": "jpflori"
}
```

I tried to update the patches so that they apply on Sage 4.6.1 with Maxima 5.22.1, some things moved since the last patches were produced, but there was nothing too terrible. I'll up them right now.

However, there is now a problem when loading Maxima as a library. Maybe some changes in the spkg (in init-cl.lisp where set-pathnames is defined ?) are responsible for this. Without that line, there is a problem later.


```
/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py in <module>()
    487 ecl_eval("(defvar *MAXIMA-LANG-SUBDIR* NIL)")
    488 ecl_eval("(set-locale-subdir)")
--> 489 ecl_eval("(set-pathnames)")
    490 ecl_eval("(defun add-lineinfo (x) x)")
    491 ecl_eval("""(defun retrieve (msg flag &aux (print? nil))(error (concatenate 'string "Maxima asks:" (meval (list '($string) msg)))))""")

/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5616)()

/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5570)()

/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2403)()

RuntimeError: ECL says: In function PATHNAME, the value of the only argument is
  NIL
which is not of the expected type (OR FILE-STREAM STRING PATHNAME)
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

```

I don't know anything about Lisp, ECL and Maxima, so I was not able to fix that in the little time I tried.

As far as the patches as concerned, I feel that more work is needed. Deleting duplicate examples and methods, moving the library interface to libs directory, not sure where maxima abstract should go (if it is kept, should something be done like MaximaLib/Maxima as for Pari/GP ? no idea if those two "interfaces" share something...), getting rid of the inheritance on Expect in Maxima_lib and Maxima_abstract.

I'm ready to have a look at all of this, if someone helps me launching Maxima as library with latest versions of everything.



---

archive/issue_comments_061835.json:
```json
{
    "body": "Attachment [trac_7377-abstract-maxima-rebased.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-abstract-maxima-rebased.patch) by jpflori created at 2011-01-24 09:25:24\n\nRebased on Sage 4.6.1",
    "created_at": "2011-01-24T09:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61835",
    "user": "jpflori"
}
```

Attachment [trac_7377-abstract-maxima-rebased.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-abstract-maxima-rebased.patch) by jpflori created at 2011-01-24 09:25:24

Rebased on Sage 4.6.1



---

archive/issue_comments_061836.json:
```json
{
    "body": "Rebased on Sage 4.6.1",
    "created_at": "2011-01-24T09:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61836",
    "user": "jpflori"
}
```

Rebased on Sage 4.6.1



---

archive/issue_comments_061837.json:
```json
{
    "body": "Attachment [trac_7377-maximalib-rebased.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-maximalib-rebased.patch) by @kiwifb created at 2011-01-24 09:38:15\n\nWhat happens if you just remove that line?\nI just noticed a typo - marking makes you terrible at that kind of things :)\n\"We begin here by initializing maxima in library more\"\n                                                   ^",
    "created_at": "2011-01-24T09:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61837",
    "user": "@kiwifb"
}
```

Attachment [trac_7377-maximalib-rebased.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-maximalib-rebased.patch) by @kiwifb created at 2011-01-24 09:38:15

What happens if you just remove that line?
I just noticed a typo - marking makes you terrible at that kind of things :)
"We begin here by initializing maxima in library more"
                                                   ^



---

archive/issue_comments_061838.json:
```json
{
    "body": "It fails later, here is the piece of code involved:\n\n\n```\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py in __init__(self, script_subdirectory, logfile, server, init_code)\n    586         ecl_eval(\"(setf *standard-output* *dev-null*)\")\n    587         for l in init_code:\n--> 588             ecl_eval(\"#$%s$\"%l)\n    589         ecl_eval(\"(setf *standard-output* original-standard-output)\")\n    590 \n\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5616)()\n\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5570)()\n\n/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2403)()\n\nRuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\nTried to google that, but couldn't find anything meaningful to me.",
    "created_at": "2011-01-24T09:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61838",
    "user": "jpflori"
}
```

It fails later, here is the piece of code involved:


```
/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py in __init__(self, script_subdirectory, logfile, server, init_code)
    586         ecl_eval("(setf *standard-output* *dev-null*)")
    587         for l in init_code:
--> 588             ecl_eval("#$%s$"%l)
    589         ecl_eval("(setf *standard-output* original-standard-output)")
    590 

/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5616)()

/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5570)()

/home/jp/boulot/sage/sage-current/local/lib/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2403)()

RuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

Tried to google that, but couldn't find anything meaningful to me.



---

archive/issue_comments_061839.json:
```json
{
    "body": "me neither :(",
    "created_at": "2011-01-24T09:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61839",
    "user": "@kiwifb"
}
```

me neither :(



---

archive/issue_comments_061840.json:
```json
{
    "body": "I don't know what happened but I rebuilt ecl and maxima while trying to add debug information and everything is fine now. I surely did something wrong at some point...\n\nThere are some problems left with what I uploaded earlier in sage.symbolic.integration.external I'll upload fixed version of the patches soon.",
    "created_at": "2011-01-24T11:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61840",
    "user": "jpflori"
}
```

I don't know what happened but I rebuilt ecl and maxima while trying to add debug information and everything is fine now. I surely did something wrong at some point...

There are some problems left with what I uploaded earlier in sage.symbolic.integration.external I'll upload fixed version of the patches soon.



---

archive/issue_comments_061841.json:
```json
{
    "body": "Attachment [trac_7377-fastcalculus-rebased.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-fastcalculus-rebased.patch) by jpflori created at 2011-01-24 11:39:35\n\nRebased on Sage 4.6.1, fixed changes in sage.symbolic.integration.external",
    "created_at": "2011-01-24T11:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61841",
    "user": "jpflori"
}
```

Attachment [trac_7377-fastcalculus-rebased.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-fastcalculus-rebased.patch) by jpflori created at 2011-01-24 11:39:35

Rebased on Sage 4.6.1, fixed changes in sage.symbolic.integration.external



---

archive/issue_comments_061842.json:
```json
{
    "body": "Ok I will give it a spin in sage-on-gentoo.",
    "created_at": "2011-01-25T07:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61842",
    "user": "@kiwifb"
}
```

Ok I will give it a spin in sage-on-gentoo.



---

archive/issue_comments_061843.json:
```json
{
    "body": "I tried the patch against 4.6.2.alpha2 and it builds but it doesn't run properly\nhere:\n\n```\n/usr/lib64/python2.6/site-packages/sage/calculus/calculus.py in <module>()\n    375         definite_integral\n    376 import sage.symbolic.pynac\n--> 377 import sage.interfaces.maxima_lib\n    378 \n    379 \"\"\"\n\n/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py in <module>()\n    482 from sage.libs.ecl import *\n    483 ecl_eval(\"(setf *load-verbose* NIL)\")\n--> 484 ecl_eval(\"(require 'maxima)\")\n    485 ecl_eval(\"(in-package :maxima)\")\n    486 ecl_eval(\"(setq $nolabels t))\")\n\n/usr/lib64/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5617)()\n    992 \n    993 \n--> 994 \n    995 \n    996 \n\n/usr/lib64/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5571)()\n   1007 \n   1008 \n-> 1009 \n   1010 \n   1011 \n\n/usr/lib64/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2404)()\n    184 \n    185 \n--> 186 \n    187 \n    188 \n\nRuntimeError: ECL says: Module error: Don't know how to REQUIRE MAXIMA.\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\nI am currently also running ecl-11.1.1 which is a source of trouble but\nI don't think it is responsible here.",
    "created_at": "2011-01-28T03:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61843",
    "user": "@kiwifb"
}
```

I tried the patch against 4.6.2.alpha2 and it builds but it doesn't run properly
here:

```
/usr/lib64/python2.6/site-packages/sage/calculus/calculus.py in <module>()
    375         definite_integral
    376 import sage.symbolic.pynac
--> 377 import sage.interfaces.maxima_lib
    378 
    379 """

/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py in <module>()
    482 from sage.libs.ecl import *
    483 ecl_eval("(setf *load-verbose* NIL)")
--> 484 ecl_eval("(require 'maxima)")
    485 ecl_eval("(in-package :maxima)")
    486 ecl_eval("(setq $nolabels t))")

/usr/lib64/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5617)()
    992 
    993 
--> 994 
    995 
    996 

/usr/lib64/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:5571)()
   1007 
   1008 
-> 1009 
   1010 
   1011 

/usr/lib64/python2.6/site-packages/sage/libs/ecl.so in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2404)()
    184 
    185 
--> 186 
    187 
    188 

RuntimeError: ECL says: Module error: Don't know how to REQUIRE MAXIMA.
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

I am currently also running ecl-11.1.1 which is a source of trouble but
I don't think it is responsible here.



---

archive/issue_comments_061844.json:
```json
{
    "body": "> RuntimeError: ECL says: Module error: Don't know how to REQUIRE MAXIMA.\n> Error importing ipy_profile_sage - perhaps you should run %upgrade?\n> WARNING: Loading of ipy_profile_sage failed.\n\nMy first guess is that maxima.fas is not available to your newly built ecl-11.1.1.\n\nNote that in 4.6.1, building maxima produces this library:\n\n$SAGE_ROOT/local/lib/ecl-10.4.1/maxima.fas\n\nso once you upgrade ecl, you need to rebuild maxima as well. Did you do that?",
    "created_at": "2011-01-28T05:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61844",
    "user": "@nbruin"
}
```

> RuntimeError: ECL says: Module error: Don't know how to REQUIRE MAXIMA.
> Error importing ipy_profile_sage - perhaps you should run %upgrade?
> WARNING: Loading of ipy_profile_sage failed.

My first guess is that maxima.fas is not available to your newly built ecl-11.1.1.

Note that in 4.6.1, building maxima produces this library:

$SAGE_ROOT/local/lib/ecl-10.4.1/maxima.fas

so once you upgrade ecl, you need to rebuild maxima as well. Did you do that?



---

archive/issue_comments_061845.json:
```json
{
    "body": "I downgraded to ecl-10.4.1 and rebuilt maxima and sage but I don't seem to have\nmaxima.fas, I have a number of other fas but not maxima.fas.\nIt was done on sage-on-gentoo, so it is possible that this particular file wasn't\ninstalled for a reason or another.\nI will check what the maxima spkg do.",
    "created_at": "2011-01-28T08:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61845",
    "user": "@kiwifb"
}
```

I downgraded to ecl-10.4.1 and rebuilt maxima and sage but I don't seem to have
maxima.fas, I have a number of other fas but not maxima.fas.
It was done on sage-on-gentoo, so it is possible that this particular file wasn't
installed for a reason or another.
I will check what the maxima spkg do.



---

archive/issue_comments_061846.json:
```json
{
    "body": "OK pity it is not build in maxima by default, works for me now.\nNot sure how i will sell that one to the maintainer of maxima in Gentoo.\nEven if I have a good relationship with him.",
    "created_at": "2011-01-28T10:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61846",
    "user": "@kiwifb"
}
```

OK pity it is not build in maxima by default, works for me now.
Not sure how i will sell that one to the maintainer of maxima in Gentoo.
Even if I have a good relationship with him.



---

archive/issue_comments_061847.json:
```json
{
    "body": "I just upgraded to 4.6.2.aplha2 (hoping I won't have to rebuild from scratch for next upgrade...) and everything went fine, it gives me better timings than with the Pexpect interface. Before patches:\n\n\n```\nLoading Sage library. Current Mercurial branch is: jp\nsage: timeit(\"integral(cos(x^2),x)\")\n5 loops, best of 3: 96.6 ms per loop\nsage: \nExiting Sage (CPU time 0m1.02s, Wall time 0m8.17s).\nExiting spawned Maxima process.\n\n```\n\nAfter:\n\n\n```\nLoading Sage library. Current Mercurial branch is: jp\nsage: timeit(\"integral(cos(x^2),x)\")\n5 loops, best of 3: 62.8 ms per loop\nsage: \nExiting Sage (CPU time 0m1.56s, Wall time 3m5.27s).\n\n```\n\nHowever those are much more than what was posted above.\n\nGlad to hear it also ran on Sage on Gentoo.\n\nI think some refactoring still has to be done for the new classes. The abstract class is a good idea to transparently switch interface but I think it would be cleaner if it did not inherit from Expect class (and so \"Maxima as a lib\" does not too). I'll try to work on this this weekend.\n\nIt should be also be decided, which interface is used for what, especially since we can only have one \"Maxima as a lib\" running. Should that Maxima as lib be used for calculus and be given a direct access (maybe as \"maximalib\" variable as \"maxima\" gives access to a copy of Maxima in Sage, even if currently the \"maxima\" variable points to a different instance of Maxima than the one used by calculus).",
    "created_at": "2011-01-28T10:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61847",
    "user": "jpflori"
}
```

I just upgraded to 4.6.2.aplha2 (hoping I won't have to rebuild from scratch for next upgrade...) and everything went fine, it gives me better timings than with the Pexpect interface. Before patches:


```
Loading Sage library. Current Mercurial branch is: jp
sage: timeit("integral(cos(x^2),x)")
5 loops, best of 3: 96.6 ms per loop
sage: 
Exiting Sage (CPU time 0m1.02s, Wall time 0m8.17s).
Exiting spawned Maxima process.

```

After:


```
Loading Sage library. Current Mercurial branch is: jp
sage: timeit("integral(cos(x^2),x)")
5 loops, best of 3: 62.8 ms per loop
sage: 
Exiting Sage (CPU time 0m1.56s, Wall time 3m5.27s).

```

However those are much more than what was posted above.

Glad to hear it also ran on Sage on Gentoo.

I think some refactoring still has to be done for the new classes. The abstract class is a good idea to transparently switch interface but I think it would be cleaner if it did not inherit from Expect class (and so "Maxima as a lib" does not too). I'll try to work on this this weekend.

It should be also be decided, which interface is used for what, especially since we can only have one "Maxima as a lib" running. Should that Maxima as lib be used for calculus and be given a direct access (maybe as "maximalib" variable as "maxima" gives access to a copy of Maxima in Sage, even if currently the "maxima" variable points to a different instance of Maxima than the one used by calculus).



---

archive/issue_comments_061848.json:
```json
{
    "body": "Replying to [comment:24 jpflori]:\n\nHi Jean-Pierre,\n\nIt's great you're taking on this project! It has the potential of being a lot of fun. I won't be working on it, so I'm very happy to see someone else interested in taking it on. I'll give you some background on the points you raise, so that you can take more informed design decisions.\n\n> I think some refactoring still has to be done for the new classes. The abstract class is a good idea to transparently switch interface but I think it would be cleaner if it did not inherit from Expect class (and so \"Maxima as a lib\" does not too). I'll try to work on this this weekend.\n\nThe *only* reason to organize the maxima interfaces as they are now is because Robert remarked that whatever was needed to communicate with maxlib at a string-level was going to have a lot of overlap with the present maxima interface. Hence, he abstracted out the common stuff and I modified the concrete maxlib interface to talk to ecllib instead of a separate process. This was experimental and at the time I had no idea how much was necessary, so I changed as little as possible: The original interface inherited from expect, so the new one did too, just overriding whatever methods needed overriding. So yes, there will be a lot of lint and extraneous stuff in there. What you're looking at is a first hack.\n\n> It should be also be decided, which interface is used for what, especially since we can only have one \"Maxima as a lib\" running. Should that Maxima as lib be used for calculus and be given a direct access (maybe as \"maximalib\" variable as \"maxima\" gives access to a copy of Maxima in Sage, even if currently the \"maxima\" variable points to a different instance of Maxima than the one used by calculus).\n\nThe largest benefit is to be gained when the communication can avoid string parsing altogether. (ecllib at the moment converts Integers to ecl bignums via strings, which is silly: They are both implemented as gmp/mpir integers! The only reason is that I never succeeded in importing the gmp/mpir headers in a usable way in ecl.pyx, to copy over the integer. ECL largely avoids gmp's registered memory manager, so some care must be taken to transfer the integer to properly allocated memory.) The routines sr_to_max and max_to_sr (in the fastcalculus patch) implement this strategy. If you want to have this benefit, the maxlib instance *has* to be the \"calculus\" instance. Note that the default \"maxima\" instance is already distinct from the \"calculus\" instance:\n\n```\nsage: integrate(cos(x),x);\nsage: maxima(x);\nsage: \nExiting Sage (CPU time 0m0.12s, Wall time 0m16.73s).\nExiting spawned Maxima process.\nExiting spawned Maxima process.\n```\n\n(note the two maxima spawns)\n\nOnce the design has stabilized, it would be possible to make max_to_sr and sr_to_max more intelligent. For instance, SR variables would not need to be translated to maxima identifiers with the same name. This currently leads to problems, because this conversion collapses namespaces:\n\n```\nsage: cosvar=SR.var(\"cos\")\nsage: cos(cosvar)\ncos(cos)\nsage: integrate(cos(cosvar),cosvar)\nintegrate(cos(cos), cos)\nsage: cosvar=SR.var(\"sage_cos\")\nsage: integrate(cos(cosvar),cosvar)\nsin(sage_cos)\n```\n\nas you see, the print name of the SR.var matters!\n\nLet me know if you have further questions. I might be able to help with information.",
    "created_at": "2011-01-28T19:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61848",
    "user": "@nbruin"
}
```

Replying to [comment:24 jpflori]:

Hi Jean-Pierre,

It's great you're taking on this project! It has the potential of being a lot of fun. I won't be working on it, so I'm very happy to see someone else interested in taking it on. I'll give you some background on the points you raise, so that you can take more informed design decisions.

> I think some refactoring still has to be done for the new classes. The abstract class is a good idea to transparently switch interface but I think it would be cleaner if it did not inherit from Expect class (and so "Maxima as a lib" does not too). I'll try to work on this this weekend.

The *only* reason to organize the maxima interfaces as they are now is because Robert remarked that whatever was needed to communicate with maxlib at a string-level was going to have a lot of overlap with the present maxima interface. Hence, he abstracted out the common stuff and I modified the concrete maxlib interface to talk to ecllib instead of a separate process. This was experimental and at the time I had no idea how much was necessary, so I changed as little as possible: The original interface inherited from expect, so the new one did too, just overriding whatever methods needed overriding. So yes, there will be a lot of lint and extraneous stuff in there. What you're looking at is a first hack.

> It should be also be decided, which interface is used for what, especially since we can only have one "Maxima as a lib" running. Should that Maxima as lib be used for calculus and be given a direct access (maybe as "maximalib" variable as "maxima" gives access to a copy of Maxima in Sage, even if currently the "maxima" variable points to a different instance of Maxima than the one used by calculus).

The largest benefit is to be gained when the communication can avoid string parsing altogether. (ecllib at the moment converts Integers to ecl bignums via strings, which is silly: They are both implemented as gmp/mpir integers! The only reason is that I never succeeded in importing the gmp/mpir headers in a usable way in ecl.pyx, to copy over the integer. ECL largely avoids gmp's registered memory manager, so some care must be taken to transfer the integer to properly allocated memory.) The routines sr_to_max and max_to_sr (in the fastcalculus patch) implement this strategy. If you want to have this benefit, the maxlib instance *has* to be the "calculus" instance. Note that the default "maxima" instance is already distinct from the "calculus" instance:

```
sage: integrate(cos(x),x);
sage: maxima(x);
sage: 
Exiting Sage (CPU time 0m0.12s, Wall time 0m16.73s).
Exiting spawned Maxima process.
Exiting spawned Maxima process.
```

(note the two maxima spawns)

Once the design has stabilized, it would be possible to make max_to_sr and sr_to_max more intelligent. For instance, SR variables would not need to be translated to maxima identifiers with the same name. This currently leads to problems, because this conversion collapses namespaces:

```
sage: cosvar=SR.var("cos")
sage: cos(cosvar)
cos(cos)
sage: integrate(cos(cosvar),cosvar)
integrate(cos(cos), cos)
sage: cosvar=SR.var("sage_cos")
sage: integrate(cos(cosvar),cosvar)
sin(sage_cos)
```

as you see, the print name of the SR.var matters!

Let me know if you have further questions. I might be able to help with information.



---

archive/issue_comments_061849.json:
```json
{
    "body": "Thanks so much, Nils and JP, for resurrecting this.  JP, I stand ready to test anything you feel is ready to look at.  If you know little about ECL, I know even less, so I can't do more than that, but this would be a great start to improving some of Sage's interface.  It's true that the timing on average doesn't improve so greatly (yet), but the point is that not having to start Maxima up when you want to do an integral means more immediate gratification for the user.  (Assuming immediate gratification is a good thing.)",
    "created_at": "2011-01-28T19:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61849",
    "user": "@kcrisman"
}
```

Thanks so much, Nils and JP, for resurrecting this.  JP, I stand ready to test anything you feel is ready to look at.  If you know little about ECL, I know even less, so I can't do more than that, but this would be a great start to improving some of Sage's interface.  It's true that the timing on average doesn't improve so greatly (yet), but the point is that not having to start Maxima up when you want to do an integral means more immediate gratification for the user.  (Assuming immediate gratification is a good thing.)



---

archive/issue_comments_061850.json:
```json
{
    "body": "Ok so it runs but in its present state it breaks quite a lot of doctests for me.\nUnless you can point out something else I would need to do.\nexample 1\n\n```\nsage -t  -force_lib \"devel/sage/sage/symbolic/function_factory.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/symbolic/function_factory.py\", line 174:\n    sage: g\nExpected:\n    b*D[0](cr)(a)\nGot:\n    b*del(a)\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/symbolic/function_factory.py\", line 184:\n    sage: g.substitute_function(cr, cos)\nExpected:\n    -b*sin(a)\nGot:\n    b*del(a)\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/symbolic/function_factory.py\", line 187:\n    sage: g.substitute_function(cr, (sin(x) + cos(x)).function(x))\nExpected:\n    -(sin(a) - cos(a))*b\nGot:\n    b*del(a)\n**********************************************************************\n1 items had failures:\n   3 of  58 in __main__.example_6\n```\n\nexample 2\n\n```\nsage -t -force_lib \"devel/sage/sage/interfaces/maxima.py\"   \n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 426:\n    sage: t.limit(Ax=0, dir='+')\nException raised:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[93]>\", line 1, in <module>\n        t.limit(Ax=Integer(0), dir='+')###line 426:\n    sage: t.limit(Ax=0, dir='+')\n      File \"expression.pyx\", line 8202, in sage.symbolic.expression.Expression.limit (sage/symbolic/expression.cpp:31252)\n      File \"/usr/lib/python2.6/site-packages/sage/calculus/calculus.py\", line 1122, in limit\n        return l.sage()\n      File \"element.pyx\", line 327, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2715)\n      File \"parent.pyx\", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2841)\n      File \"parent.pyx\", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2636)\n    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'sage'\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 894:\n    sage: f(3.2)\nExpected:\n    -.05837414342758009\nGot:\n    -.058374143427580086\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 1006:\n    sage: maxima.version()\nExpected:\n    '5.22.1'\nGot:\n    '5.23.2'\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 1087:\n    sage: maxima_version()\nExpected:\n    '5.22.1'\nGot:\n    '5.23.2'\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 608:\n    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):\n    Is  a  positive or negative?\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[3]>\", line 1, in <module>\n        integrate(Integer(1)/(x**Integer(3) *(a+b*x)**(Integer(1)/Integer(3))),x)###line 608:\n    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)\n      File \"/usr/lib/python2.6/site-packages/sage/misc/functional.py\", line 718, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 601, in integrate\n        return indefinite_integral(expression, v)\n      File \"function.pyx\", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 85, in _eval_\n        res = integrator(f, x)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py\", line 19, in maxima_integrator\n        result = maxima.sr_integral(expression,v)\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 983, in sr_integral\n        raise error\n    RuntimeError: ECL says: Maxima asks:?mtext(\"Is  \",a,\"  positive or negative?\")\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 618:\n    sage: integral(x^n,x)\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):\n    Is  n+1  zero or nonzero?\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[7]>\", line 1, in <module>\n        integral(x**n,x)###line 618:\n    sage: integral(x^n,x)\n      File \"/usr/lib/python2.6/site-packages/sage/misc/functional.py\", line 718, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 601, in integrate\n        return indefinite_integral(expression, v)\n      File \"function.pyx\", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 85, in _eval_\n        res = integrator(f, x)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py\", line 19, in maxima_integrator\n        result = maxima.sr_integral(expression,v)\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 983, in sr_integral\n        raise error\n    RuntimeError: ECL says: Maxima asks:?mtext(\"Is  \",n+1,\"  zero or nonzero?\")\n**********************************************************************\n5 items had failures:\n   1 of  95 in __main__.example_0\n   1 of  16 in __main__.example_13\n   1 of   3 in __main__.example_17\n   1 of   4 in __main__.example_21\n   2 of  11 in __main__.example_6\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/francois/.sage/tmp/.doctest_maxima.py\n```\n\nand there are more. Tests are still running on this slow machine.",
    "created_at": "2011-01-29T03:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61850",
    "user": "@kiwifb"
}
```

Ok so it runs but in its present state it breaks quite a lot of doctests for me.
Unless you can point out something else I would need to do.
example 1

```
sage -t  -force_lib "devel/sage/sage/symbolic/function_factory.py"
**********************************************************************
File "/usr/share/sage/devel/sage/sage/symbolic/function_factory.py", line 174:
    sage: g
Expected:
    b*D[0](cr)(a)
Got:
    b*del(a)
**********************************************************************
File "/usr/share/sage/devel/sage/sage/symbolic/function_factory.py", line 184:
    sage: g.substitute_function(cr, cos)
Expected:
    -b*sin(a)
Got:
    b*del(a)
**********************************************************************
File "/usr/share/sage/devel/sage/sage/symbolic/function_factory.py", line 187:
    sage: g.substitute_function(cr, (sin(x) + cos(x)).function(x))
Expected:
    -(sin(a) - cos(a))*b
Got:
    b*del(a)
**********************************************************************
1 items had failures:
   3 of  58 in __main__.example_6
```

example 2

```
sage -t -force_lib "devel/sage/sage/interfaces/maxima.py"   
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 426:
    sage: t.limit(Ax=0, dir='+')
Exception raised:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[93]>", line 1, in <module>
        t.limit(Ax=Integer(0), dir='+')###line 426:
    sage: t.limit(Ax=0, dir='+')
      File "expression.pyx", line 8202, in sage.symbolic.expression.Expression.limit (sage/symbolic/expression.cpp:31252)
      File "/usr/lib/python2.6/site-packages/sage/calculus/calculus.py", line 1122, in limit
        return l.sage()
      File "element.pyx", line 327, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2715)
      File "parent.pyx", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2841)
      File "parent.pyx", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2636)
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'sage'
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 894:
    sage: f(3.2)
Expected:
    -.05837414342758009
Got:
    -.058374143427580086
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 1006:
    sage: maxima.version()
Expected:
    '5.22.1'
Got:
    '5.23.2'
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 1087:
    sage: maxima_version()
Expected:
    '5.22.1'
Got:
    '5.23.2'
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 608:
    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):
    Is  a  positive or negative?
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        integrate(Integer(1)/(x**Integer(3) *(a+b*x)**(Integer(1)/Integer(3))),x)###line 608:
    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)
      File "/usr/lib/python2.6/site-packages/sage/misc/functional.py", line 718, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 601, in integrate
        return indefinite_integral(expression, v)
      File "function.pyx", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 85, in _eval_
        res = integrator(f, x)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py", line 19, in maxima_integrator
        result = maxima.sr_integral(expression,v)
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 983, in sr_integral
        raise error
    RuntimeError: ECL says: Maxima asks:?mtext("Is  ",a,"  positive or negative?")
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 618:
    sage: integral(x^n,x)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):
    Is  n+1  zero or nonzero?
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        integral(x**n,x)###line 618:
    sage: integral(x^n,x)
      File "/usr/lib/python2.6/site-packages/sage/misc/functional.py", line 718, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 601, in integrate
        return indefinite_integral(expression, v)
      File "function.pyx", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 85, in _eval_
        res = integrator(f, x)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py", line 19, in maxima_integrator
        result = maxima.sr_integral(expression,v)
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 983, in sr_integral
        raise error
    RuntimeError: ECL says: Maxima asks:?mtext("Is  ",n+1,"  zero or nonzero?")
**********************************************************************
5 items had failures:
   1 of  95 in __main__.example_0
   1 of  16 in __main__.example_13
   1 of   3 in __main__.example_17
   1 of   4 in __main__.example_21
   2 of  11 in __main__.example_6
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/francois/.sage/tmp/.doctest_maxima.py
```

and there are more. Tests are still running on this slow machine.



---

archive/issue_comments_061851.json:
```json
{
    "body": "> {{{\n> sage -t  -force_lib \"devel/sage/sage/symbolic/function_factory.py\"\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage/sage/symbolic/function_factory.py\", line 174:\n>     sage: g\n> Expected:\n>     b*D[0](cr)(a)\n> Got:\n>     b*del(a)\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage/sage/symbolic/function_factory.py\", line 184:\n>     sage: g.substitute_function(cr, cos)\n> Expected:\n>     -b*sin(a)\n> Got:\n>     b*del(a)\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage/sage/symbolic/function_factory.py\", line 187:\n>     sage: g.substitute_function(cr, (sin(x) + cos(x)).function(x))\n> Expected:\n>     -(sin(a) - cos(a))*b\n> Got:\n>     b*del(a)\n> **********************************************************************\n\nHmm, that is very interesting.  I am not quite sure what this `del` thing is, but I remember seeing something about it on the Maxima list...\n> File \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 426:\n>     sage: t.limit(Ax=0, dir='+')\n>         return l.sage()\n>       File \"element.pyx\", line 327, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2715)\n>       File \"parent.pyx\", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2841)\n>       File \"parent.pyx\", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2636)\n>     AttributeError: 'sage.rings.integer.Integer' object has no attribute 'sage'\n\nThis must be us using Sage Integers somehow at the library level where before they were coming back from Maxima?\n\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage/sage/interfaces/maxima.py\", line 608:\n>     sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)\n> Expected:\n>     Traceback (most recent call last):\n>     ...\n>     TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):\n>     Is  a  positive or negative?\n\nNotice we expect a TypeError.\n>     RuntimeError: ECL says: Maxima asks:?mtext(\"Is  \",a,\"  positive or negative?\")\n\nNow we just get a different error.  I assume that the new code interface has something about ECL asking.  We would want to make sure that this still is turned into the helpful type of message we have here, but that should be easy (if tedious) to make work.\n\nThank you for beginning this testing!",
    "created_at": "2011-01-29T03:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61851",
    "user": "@kcrisman"
}
```

> {{{
> sage -t  -force_lib "devel/sage/sage/symbolic/function_factory.py"
> **********************************************************************
> File "/usr/share/sage/devel/sage/sage/symbolic/function_factory.py", line 174:
>     sage: g
> Expected:
>     b*D[0](cr)(a)
> Got:
>     b*del(a)
> **********************************************************************
> File "/usr/share/sage/devel/sage/sage/symbolic/function_factory.py", line 184:
>     sage: g.substitute_function(cr, cos)
> Expected:
>     -b*sin(a)
> Got:
>     b*del(a)
> **********************************************************************
> File "/usr/share/sage/devel/sage/sage/symbolic/function_factory.py", line 187:
>     sage: g.substitute_function(cr, (sin(x) + cos(x)).function(x))
> Expected:
>     -(sin(a) - cos(a))*b
> Got:
>     b*del(a)
> **********************************************************************

Hmm, that is very interesting.  I am not quite sure what this `del` thing is, but I remember seeing something about it on the Maxima list...
> File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 426:
>     sage: t.limit(Ax=0, dir='+')
>         return l.sage()
>       File "element.pyx", line 327, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2715)
>       File "parent.pyx", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2841)
>       File "parent.pyx", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2636)
>     AttributeError: 'sage.rings.integer.Integer' object has no attribute 'sage'

This must be us using Sage Integers somehow at the library level where before they were coming back from Maxima?

> **********************************************************************
> File "/usr/share/sage/devel/sage/sage/interfaces/maxima.py", line 608:
>     sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)
> Expected:
>     Traceback (most recent call last):
>     ...
>     TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):
>     Is  a  positive or negative?

Notice we expect a TypeError.
>     RuntimeError: ECL says: Maxima asks:?mtext("Is  ",a,"  positive or negative?")

Now we just get a different error.  I assume that the new code interface has something about ECL asking.  We would want to make sure that this still is turned into the helpful type of message we have here, but that should be easy (if tedious) to make work.

Thank you for beginning this testing!



---

archive/issue_comments_061852.json:
```json
{
    "body": "I don't have the cedille, pardon me :(",
    "created_at": "2011-01-29T03:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61852",
    "user": "@kcrisman"
}
```

I don't have the cedille, pardon me :(



---

archive/issue_comments_061853.json:
```json
{
    "body": "I have a cedilla thanks to the international setting on my desktop.\n\nMore seriously, it should be pointed out that this is done with ecl-11.1.1\nand it may have an influence. I have a faster machine at work and I'll test\necl-10.4.1 on Monday.",
    "created_at": "2011-01-29T03:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61853",
    "user": "@kiwifb"
}
```

I have a cedilla thanks to the international setting on my desktop.

More seriously, it should be pointed out that this is done with ecl-11.1.1
and it may have an influence. I have a faster machine at work and I'll test
ecl-10.4.1 on Monday.



---

archive/issue_comments_061854.json:
```json
{
    "body": "Ok so I have a lot of failures that I attribute to maxima-lib, I am making a list\nfor quick reference. I have another sage-on-gentoo report on there being a lot failure with it and this time with ecl-10.4.1.\n\n  sage -t  -force_lib \"devel/sage/sage/functions/special.py\" # Time out\n\n  sage -t  -force_lib \"devel/sage/sage/functions/piecewise.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/functions/min_max.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/functions/orthogonal_polys.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/interfaces/maxima_lib.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/interfaces/maxima_abstract.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/interfaces/maxima.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/function_factory.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/integration/integral.py\" # Time out\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/integration/external.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/relation.py\" # Time out\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/assumptions.py\" # Time out\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/power_helper.pyx\"\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/expression_conversions.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/ring.pyx\"\n\n  sage -t  -force_lib \"devel/sage/sage/symbolic/expression.pyx\" # Time out\n\n  sage -t  -force_lib \"devel/sage/sage/rings/number_field/number_field_element_quadratic.pyx\"\n\n  sage -t  -force_lib \"devel/sage/sage/rings/number_field/number_field_element.pyx\"\n\n  sage -t  -force_lib \"devel/sage/sage/structure/sage_object.pyx\"\n\n  sage -t  -force_lib \"devel/sage/sage/misc/functional.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/modules/free_module_element.pyx\"\n\n  sage -t  -force_lib \"devel/sage/sage/modular/modform/ambient_R.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/calculus/desolvers.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/calculus/calculus.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/calculus/tests.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/calculus/functional.py\"\n\n  sage -t  -force_lib \"devel/sage/sage/calculus/interpolators.pyx\"\n\n  sage -t  -force_lib \"devel/sage/sage/calculus/wester.py\"\n\n\nSome are probably due to ecl-11.1.1 so it should shrink, but it will take a bit\nof time since ecl, maxima and sage have to be rebuild.",
    "created_at": "2011-01-29T07:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61854",
    "user": "@kiwifb"
}
```

Ok so I have a lot of failures that I attribute to maxima-lib, I am making a list
for quick reference. I have another sage-on-gentoo report on there being a lot failure with it and this time with ecl-10.4.1.

  sage -t  -force_lib "devel/sage/sage/functions/special.py" # Time out

  sage -t  -force_lib "devel/sage/sage/functions/piecewise.py"

  sage -t  -force_lib "devel/sage/sage/functions/min_max.py"

  sage -t  -force_lib "devel/sage/sage/functions/orthogonal_polys.py"

  sage -t  -force_lib "devel/sage/sage/interfaces/maxima_lib.py"

  sage -t  -force_lib "devel/sage/sage/interfaces/maxima_abstract.py"

  sage -t  -force_lib "devel/sage/sage/interfaces/maxima.py"

  sage -t  -force_lib "devel/sage/sage/symbolic/function_factory.py"

  sage -t  -force_lib "devel/sage/sage/symbolic/integration/integral.py" # Time out

  sage -t  -force_lib "devel/sage/sage/symbolic/integration/external.py"

  sage -t  -force_lib "devel/sage/sage/symbolic/relation.py" # Time out

  sage -t  -force_lib "devel/sage/sage/symbolic/assumptions.py" # Time out

  sage -t  -force_lib "devel/sage/sage/symbolic/power_helper.pyx"

  sage -t  -force_lib "devel/sage/sage/symbolic/expression_conversions.py"

  sage -t  -force_lib "devel/sage/sage/symbolic/ring.pyx"

  sage -t  -force_lib "devel/sage/sage/symbolic/expression.pyx" # Time out

  sage -t  -force_lib "devel/sage/sage/rings/number_field/number_field_element_quadratic.pyx"

  sage -t  -force_lib "devel/sage/sage/rings/number_field/number_field_element.pyx"

  sage -t  -force_lib "devel/sage/sage/structure/sage_object.pyx"

  sage -t  -force_lib "devel/sage/sage/misc/functional.py"

  sage -t  -force_lib "devel/sage/sage/modules/free_module_element.pyx"

  sage -t  -force_lib "devel/sage/sage/modular/modform/ambient_R.py"

  sage -t  -force_lib "devel/sage/sage/calculus/desolvers.py"

  sage -t  -force_lib "devel/sage/sage/calculus/calculus.py"

  sage -t  -force_lib "devel/sage/sage/calculus/tests.py"

  sage -t  -force_lib "devel/sage/sage/calculus/functional.py"

  sage -t  -force_lib "devel/sage/sage/calculus/interpolators.pyx"

  sage -t  -force_lib "devel/sage/sage/calculus/wester.py"


Some are probably due to ecl-11.1.1 so it should shrink, but it will take a bit
of time since ecl, maxima and sage have to be rebuild.



---

archive/issue_comments_061855.json:
```json
{
    "body": "ecl-10.4.1, maxima-5.23.2:\n\nsage -t --verbose -force_lib \"devel/sage/sage/functions/special.py\" times out because it stops:\n\n```\nTrying:\n    elliptic_e(arccoth(Integer(1)), x**Integer(2)*e)###line 535:_sage_    >>> elliptic_e(arccoth(1), x^2*e)\nExpecting:\n    elliptic_e(arccoth(1), x^2*e)\nThe number 1 isn't in the domain of acoth\n -- an error. To debug this try: debugmode(true);\n\nError in format: Unknown format directive.\n  The number ~:M isn't in the domain of ~A\n               ^\nwhile processing indirect format string:\n  ~?\n   ^\nNo restarts available.\n\nBroken at LAMBDA.\nMAXIMA>> \n```\n",
    "created_at": "2011-01-29T10:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61855",
    "user": "@kiwifb"
}
```

ecl-10.4.1, maxima-5.23.2:

sage -t --verbose -force_lib "devel/sage/sage/functions/special.py" times out because it stops:

```
Trying:
    elliptic_e(arccoth(Integer(1)), x**Integer(2)*e)###line 535:_sage_    >>> elliptic_e(arccoth(1), x^2*e)
Expecting:
    elliptic_e(arccoth(1), x^2*e)
The number 1 isn't in the domain of acoth
 -- an error. To debug this try: debugmode(true);

Error in format: Unknown format directive.
  The number ~:M isn't in the domain of ~A
               ^
while processing indirect format string:
  ~?
   ^
No restarts available.

Broken at LAMBDA.
MAXIMA>> 
```




---

archive/issue_comments_061856.json:
```json
{
    "body": "Interesting one, notice that it still wants maxima-5.19.1\n\n```\nsage -t -force_lib \"devel/sage/sage/interfaces/maxima_lib.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py\", line 426:\n    sage: t.limit(Ax=0,dir='above')\nException raised:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[93]>\", line 1, in <module>\n        t.limit(Ax=Integer(0),dir='above')###line 426:\n    sage: t.limit(Ax=0,dir='above')\n      File \"expression.pyx\", line 8202, in sage.symbolic.expression.Expression.limit (sage/symbolic/expression.cpp:31252)\n      File \"/usr/lib/python2.6/site-packages/sage/calculus/calculus.py\", line 1122, in limit\n        return l.sage()\n      File \"element.pyx\", line 327, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2715)\n      File \"parent.pyx\", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2841)\n      File \"parent.pyx\", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2636)\n    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'sage'\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py\", line 966:\n    sage: maxima.version()\nExpected:\n    '5.19.1'\nGot:\n    '5.23.2'\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py\", line 1076:\n    sage: maxima_version()\nExpected:\n    '5.19.1'\nGot:\n    '5.23.2'\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py\", line 639:\n    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):\n    Is  a  positive or negative?\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[3]>\", line 1, in <module>\n        integrate(Integer(1)/(x**Integer(3) *(a+b*x)**(Integer(1)/Integer(3))),x)###line 639:\n    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)\n      File \"/usr/lib/python2.6/site-packages/sage/misc/functional.py\", line 718, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 601, in integrate\n        return indefinite_integral(expression, v)\n      File \"function.pyx\", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 85, in _eval_\n        res = integrator(f, x)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py\", line 19, in maxima_integrator\n        result = maxima.sr_integral(expression,v)\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 983, in sr_integral\n        raise error\n    RuntimeError: ECL says: Maxima asks:?mtext(\"Is  \",a,\"  positive or negative?\")\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py\", line 649:\n    sage: integral(x^n,x)\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):\n    Is  n+1  zero or nonzero?\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[7]>\", line 1, in <module>\n        integral(x**n,x)###line 649:\n    sage: integral(x^n,x)\n      File \"/usr/lib/python2.6/site-packages/sage/misc/functional.py\", line 718, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 601, in integrate\n        return indefinite_integral(expression, v)\n      File \"function.pyx\", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 85, in _eval_\n        res = integrator(f, x)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py\", line 19, in maxima_integrator\n        result = maxima.sr_integral(expression,v)\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 983, in sr_integral\n        raise error\n    RuntimeError: ECL says: Maxima asks:?mtext(\"Is  \",n+1,\"  zero or nonzero?\")\n**********************************************************************\n4 items had failures:\n   1 of  95 in __main__.example_0\n   1 of   3 in __main__.example_18\n   1 of   4 in __main__.example_23\n   2 of  11 in __main__.example_8\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /home/francois/.sage/tmp/.doctest_maxima_lib.py\n         [17.3 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -force_lib \"devel/sage/sage/interfaces/maxima_lib.py\"\nTotal time for all tests: 17.3 seconds\n```\n\n\nsage -t -force_lib \"devel/sage/sage/symbolic/integration/integral.py times out because:\n\n```\nTrying:\n    integrate(sin(x)*cos(Integer(10)*x)*log(x), x)###line 462:_sage_    >>> integrate(sin(x)*cos(10*x)*log(x), x)\nExpecting:\n    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)\nWrong number of arguments to gamma_incomplete\n -- an error. To debug this try: debugmode(true);\n\nError in format: Unknown format directive.\n  Wrong number of arguments to ~:@M\n                                  ^\nwhile processing indirect format string:\n  ~?\n   ^\nNo restarts available.\n\nBroken at LAMBDA.\n```\n\n\nsage -t -force_lib \"devel/sage/sage/symbolic/relation.py\" times out because of this:\n\n```\nTrying:\n    solve([sqrt(x) + sqrt(y) == Integer(5), x + y == Integer(10)], x, y)###line 492:_sage_    >>> solve([sqrt(x) + sqrt(y) == 5, x + y == 10], x, y)\nExpecting:\n    [[x == -5/2*I*sqrt(5) + 5, y == 5/2*I*sqrt(5) + 5], [x == 5/2*I*sqrt(5) + 5, y == -5/2*I*sqrt(5) + 5]]\nassoc: every list element must be an expression with two arguments; found: [sage147]\n#0: simp_%solve(e=sage135,v=sage146,extraargs=[sage147])\n -- an error. To debug this try: debugmode(true);\n\nError in format: Unknown format directive.\n  assoc: every list element must be an expression with two arguments; found: ~:M\n                                                                               ^\nwhile processing indirect format string:\n  ~?\n   ^\nNo restarts available.\n```\n\n\nsage -t -force_lib \"devel/sage/sage/symbolic/assumptions.py\":\n\n```\nTrying:\n    decl2.assume()###line 89:_sage_    >>> decl2.assume()\nExpecting:\n    Traceback (most recent call last):\n    ...\n    ValueError: Assumption is inconsistent\ndeclare: inconsistent declaration declare(x,odd)\n -- an error. To debug this try: debugmode(true);\n\nError in format: Unknown format directive.\n  declare: inconsistent declaration ~:M\n                                      ^\nwhile processing indirect format string:\n  ~?\n   ^\nNo restarts available.\n```\n\n\nsage -t -force_lib \"devel/sage/sage/symbolic/expression.pyx\":\n\n```\nTrying:\n    solve(acot(x),x)###line 7453:_sage_    >>> solve(acot(x),x)\nExpecting:\n    []\nThe number 0 isn't in the domain of cot\n -- an error. To debug this try: debugmode(true);\n\nError in format: Unknown format directive.\n  The number ~:M isn't in the domain of ~A\n               ^\nwhile processing indirect format string:\n  ~?\n   ^\nNo restarts available.\n```\n\n\nsage -t -force_lib \"devel/sage/sage/structure/sage_object.pyx\" is interesting:\n\n```\nFile \"/usr/share/sage/devel/sage/sage/structure/sage_object.pyx\", line 1053:\n    sage: print \"x\"; sage.structure.sage_object.unpickle_all()\nExpected:\n    x...\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    x\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead\n     * unpickle failure: load('/home/francois/.sage/temp/vrooom/13483/dir_2/pickle_jar/_class__sage_interfaces_maxima_MaximaFunction__.sobj')\n    Failed:\n    _class__sage_interfaces_maxima_MaximaFunction__.sobj\n    Successfully unpickled 585 objects.\n    Failed to unpickle 1 objects.\n```\n\n\nsage -t -force_lib \"devel/sage/sage/modules/free_module_element.pyx\" now pass, so probably ecl-11.1.1 related.\n\nsage -t -force_lib \"devel/sage/sage/calculus/tests.py\" (extracts):\n\n```\nFile \"/usr/share/sage/devel/sage/sage/calculus/tests.py\", line 107:\n    sage: integrate(log(1-x^2)/x, x)\nException raised:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[41]>\", line 1, in <module>\n        integrate(log(Integer(1)-x**Integer(2))/x, x)###line 107:\n    sage: integrate(log(1-x^2)/x, x)\n      File \"/usr/lib/python2.6/site-packages/sage/misc/functional.py\", line 718, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 601, in integrate\n        return indefinite_integral(expression, v)\n      File \"function.pyx\", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 85, in _eval_\n        res = integrator(f, x)\n      File \"/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py\", line 19, in maxima_integrator\n        result = maxima.sr_integral(expression,v)\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 977, in sr_integral\n        return max_to_sr(maxima_eval(([max_integrate],[sr_to_max(SR(a)) for a in args])))\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 1228, in max_to_sr\n        args.append(max_to_sr(car(max_args)))\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 1228, in max_to_sr\n        args.append(max_to_sr(car(max_args)))\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 1228, in max_to_sr\n        args.append(max_to_sr(car(max_args)))\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 1221, in max_to_sr\n        sage_expr=SR(maxima(expr))\n      File \"parent.pyx\", line 915, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6668)\n      File \"coerce_maps.pyx\", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4045)\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_abstract.py\", line 1373, in _symbolic_\n        return R(self._sage_())\n      File \"/usr/lib/python2.6/site-packages/sage/interfaces/maxima_abstract.py\", line 1354, in _sage_\n        maxima=self.parent())\n      File \"/usr/lib/python2.6/site-packages/sage/calculus/calculus.py\", line 1646, in symbolic_expression_from_maxima_string\n        raise TypeError, \"unable to make sense of Maxima expression '%s' in Sage\"%s\n    TypeError: unable to make sense of Maxima expression 'li[2]' in Sage\n```\n\n\n```\nFile \"/usr/share/sage/devel/sage/sage/calculus/tests.py\", line 151:\n    sage: integrate(ceil(x^2 + floor(x)), x, 0, 5)    # todo: Mathematica can do this\nExpected:\n    integrate(ceil(x^2) + floor(x), x, 0, 5)\nGot:\n    155/3\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/calculus/tests.py\", line 189:\n    sage: integrate(sin(x), x, a, b)\nExpected:\n    cos(a) - cos(b)\nGot:\n    ceil(cos(a))\n```\n\n\nsage -t -force_lib \"devel/sage/sage/calculus/interpolators.pyx\" is actually unrelated to maxima I think.",
    "created_at": "2011-01-29T10:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61856",
    "user": "@kiwifb"
}
```

Interesting one, notice that it still wants maxima-5.19.1

```
sage -t -force_lib "devel/sage/sage/interfaces/maxima_lib.py"
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py", line 426:
    sage: t.limit(Ax=0,dir='above')
Exception raised:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[93]>", line 1, in <module>
        t.limit(Ax=Integer(0),dir='above')###line 426:
    sage: t.limit(Ax=0,dir='above')
      File "expression.pyx", line 8202, in sage.symbolic.expression.Expression.limit (sage/symbolic/expression.cpp:31252)
      File "/usr/lib/python2.6/site-packages/sage/calculus/calculus.py", line 1122, in limit
        return l.sage()
      File "element.pyx", line 327, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2715)
      File "parent.pyx", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2841)
      File "parent.pyx", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2636)
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'sage'
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py", line 966:
    sage: maxima.version()
Expected:
    '5.19.1'
Got:
    '5.23.2'
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py", line 1076:
    sage: maxima_version()
Expected:
    '5.19.1'
Got:
    '5.23.2'
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py", line 639:
    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):
    Is  a  positive or negative?
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[3]>", line 1, in <module>
        integrate(Integer(1)/(x**Integer(3) *(a+b*x)**(Integer(1)/Integer(3))),x)###line 639:
    sage: integrate(1/(x^3 *(a+b*x)^(1/3)),x)
      File "/usr/lib/python2.6/site-packages/sage/misc/functional.py", line 718, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 601, in integrate
        return indefinite_integral(expression, v)
      File "function.pyx", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 85, in _eval_
        res = integrator(f, x)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py", line 19, in maxima_integrator
        result = maxima.sr_integral(expression,v)
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 983, in sr_integral
        raise error
    RuntimeError: ECL says: Maxima asks:?mtext("Is  ",a,"  positive or negative?")
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima_lib.py", line 649:
    sage: integral(x^n,x)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):
    Is  n+1  zero or nonzero?
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[7]>", line 1, in <module>
        integral(x**n,x)###line 649:
    sage: integral(x^n,x)
      File "/usr/lib/python2.6/site-packages/sage/misc/functional.py", line 718, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 601, in integrate
        return indefinite_integral(expression, v)
      File "function.pyx", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 85, in _eval_
        res = integrator(f, x)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py", line 19, in maxima_integrator
        result = maxima.sr_integral(expression,v)
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 983, in sr_integral
        raise error
    RuntimeError: ECL says: Maxima asks:?mtext("Is  ",n+1,"  zero or nonzero?")
**********************************************************************
4 items had failures:
   1 of  95 in __main__.example_0
   1 of   3 in __main__.example_18
   1 of   4 in __main__.example_23
   2 of  11 in __main__.example_8
***Test Failed*** 5 failures.
For whitespace errors, see the file /home/francois/.sage/tmp/.doctest_maxima_lib.py
         [17.3 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -force_lib "devel/sage/sage/interfaces/maxima_lib.py"
Total time for all tests: 17.3 seconds
```


sage -t -force_lib "devel/sage/sage/symbolic/integration/integral.py times out because:

```
Trying:
    integrate(sin(x)*cos(Integer(10)*x)*log(x), x)###line 462:_sage_    >>> integrate(sin(x)*cos(10*x)*log(x), x)
Expecting:
    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
Wrong number of arguments to gamma_incomplete
 -- an error. To debug this try: debugmode(true);

Error in format: Unknown format directive.
  Wrong number of arguments to ~:@M
                                  ^
while processing indirect format string:
  ~?
   ^
No restarts available.

Broken at LAMBDA.
```


sage -t -force_lib "devel/sage/sage/symbolic/relation.py" times out because of this:

```
Trying:
    solve([sqrt(x) + sqrt(y) == Integer(5), x + y == Integer(10)], x, y)###line 492:_sage_    >>> solve([sqrt(x) + sqrt(y) == 5, x + y == 10], x, y)
Expecting:
    [[x == -5/2*I*sqrt(5) + 5, y == 5/2*I*sqrt(5) + 5], [x == 5/2*I*sqrt(5) + 5, y == -5/2*I*sqrt(5) + 5]]
assoc: every list element must be an expression with two arguments; found: [sage147]
#0: simp_%solve(e=sage135,v=sage146,extraargs=[sage147])
 -- an error. To debug this try: debugmode(true);

Error in format: Unknown format directive.
  assoc: every list element must be an expression with two arguments; found: ~:M
                                                                               ^
while processing indirect format string:
  ~?
   ^
No restarts available.
```


sage -t -force_lib "devel/sage/sage/symbolic/assumptions.py":

```
Trying:
    decl2.assume()###line 89:_sage_    >>> decl2.assume()
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: Assumption is inconsistent
declare: inconsistent declaration declare(x,odd)
 -- an error. To debug this try: debugmode(true);

Error in format: Unknown format directive.
  declare: inconsistent declaration ~:M
                                      ^
while processing indirect format string:
  ~?
   ^
No restarts available.
```


sage -t -force_lib "devel/sage/sage/symbolic/expression.pyx":

```
Trying:
    solve(acot(x),x)###line 7453:_sage_    >>> solve(acot(x),x)
Expecting:
    []
The number 0 isn't in the domain of cot
 -- an error. To debug this try: debugmode(true);

Error in format: Unknown format directive.
  The number ~:M isn't in the domain of ~A
               ^
while processing indirect format string:
  ~?
   ^
No restarts available.
```


sage -t -force_lib "devel/sage/sage/structure/sage_object.pyx" is interesting:

```
File "/usr/share/sage/devel/sage/sage/structure/sage_object.pyx", line 1053:
    sage: print "x"; sage.structure.sage_object.unpickle_all()
Expected:
    x...
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    x
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
     * unpickle failure: load('/home/francois/.sage/temp/vrooom/13483/dir_2/pickle_jar/_class__sage_interfaces_maxima_MaximaFunction__.sobj')
    Failed:
    _class__sage_interfaces_maxima_MaximaFunction__.sobj
    Successfully unpickled 585 objects.
    Failed to unpickle 1 objects.
```


sage -t -force_lib "devel/sage/sage/modules/free_module_element.pyx" now pass, so probably ecl-11.1.1 related.

sage -t -force_lib "devel/sage/sage/calculus/tests.py" (extracts):

```
File "/usr/share/sage/devel/sage/sage/calculus/tests.py", line 107:
    sage: integrate(log(1-x^2)/x, x)
Exception raised:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[41]>", line 1, in <module>
        integrate(log(Integer(1)-x**Integer(2))/x, x)###line 107:
    sage: integrate(log(1-x^2)/x, x)
      File "/usr/lib/python2.6/site-packages/sage/misc/functional.py", line 718, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 8153, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:30871)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 601, in integrate
        return indefinite_integral(expression, v)
      File "function.pyx", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4486)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/integral.py", line 85, in _eval_
        res = integrator(f, x)
      File "/usr/lib/python2.6/site-packages/sage/symbolic/integration/external.py", line 19, in maxima_integrator
        result = maxima.sr_integral(expression,v)
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 977, in sr_integral
        return max_to_sr(maxima_eval(([max_integrate],[sr_to_max(SR(a)) for a in args])))
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 1228, in max_to_sr
        args.append(max_to_sr(car(max_args)))
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 1228, in max_to_sr
        args.append(max_to_sr(car(max_args)))
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 1228, in max_to_sr
        args.append(max_to_sr(car(max_args)))
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 1221, in max_to_sr
        sage_expr=SR(maxima(expr))
      File "parent.pyx", line 915, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6668)
      File "coerce_maps.pyx", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4045)
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_abstract.py", line 1373, in _symbolic_
        return R(self._sage_())
      File "/usr/lib/python2.6/site-packages/sage/interfaces/maxima_abstract.py", line 1354, in _sage_
        maxima=self.parent())
      File "/usr/lib/python2.6/site-packages/sage/calculus/calculus.py", line 1646, in symbolic_expression_from_maxima_string
        raise TypeError, "unable to make sense of Maxima expression '%s' in Sage"%s
    TypeError: unable to make sense of Maxima expression 'li[2]' in Sage
```


```
File "/usr/share/sage/devel/sage/sage/calculus/tests.py", line 151:
    sage: integrate(ceil(x^2 + floor(x)), x, 0, 5)    # todo: Mathematica can do this
Expected:
    integrate(ceil(x^2) + floor(x), x, 0, 5)
Got:
    155/3
**********************************************************************
File "/usr/share/sage/devel/sage/sage/calculus/tests.py", line 189:
    sage: integrate(sin(x), x, a, b)
Expected:
    cos(a) - cos(b)
Got:
    ceil(cos(a))
```


sage -t -force_lib "devel/sage/sage/calculus/interpolators.pyx" is actually unrelated to maxima I think.



---

archive/issue_comments_061857.json:
```json
{
    "body": "Replying to [comment:32 fbissey]:\n> ecl-10.4.1, maxima-5.23.2:\n\n> sage -t --verbose -force_lib \"devel/sage/sage/functions/special.py\" times out because it stops:\n> {{{\n> Trying:\n>     elliptic_e(arccoth(Integer(1)), x**Integer(2)*e)###line 535:_sage_    >>> elliptic_e(arccoth(1), x^2*e)\n> Expecting:\n>     elliptic_e(arccoth(1), x^2*e)\n> The number 1 isn't in the domain of acoth\n\nHmm, this must have to do with 5.23.2, because \"Here arccoth doesn't have 1 in its domain, so we just hold the expression:\" in the past.  So Maxima must have improved something here.\n\n\n```\n    sage: integrate(ceil(x^2 + floor(x)), x, 0, 5)    # todo: Mathematica can do this\nExpected:\n    integrate(ceil(x^2) + floor(x), x, 0, 5)\nGot:\n    155/3\n```\n\nIf this is right, that's good.  No idea what's going on with the next one.\n\nIn general, I'm seeing a lot of stuff that's related to having the newer Maxima.  I think that we should either upgrade Maxima first, and take care of things related to better error handling/functionality in Maxima, and then address this ticket separately, OR do this first with our current Maxima and then upgrade Maxima.    My preference would be to upgrade Maxima first, assuming one can do that relatively easily (would ECL also have to be upgraded?  It's annoying that one has to do them simultaneously at times, at least with some of my slower test machines.).",
    "created_at": "2011-01-29T14:52:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61857",
    "user": "@kcrisman"
}
```

Replying to [comment:32 fbissey]:
> ecl-10.4.1, maxima-5.23.2:

> sage -t --verbose -force_lib "devel/sage/sage/functions/special.py" times out because it stops:
> {{{
> Trying:
>     elliptic_e(arccoth(Integer(1)), x**Integer(2)*e)###line 535:_sage_    >>> elliptic_e(arccoth(1), x^2*e)
> Expecting:
>     elliptic_e(arccoth(1), x^2*e)
> The number 1 isn't in the domain of acoth

Hmm, this must have to do with 5.23.2, because "Here arccoth doesn't have 1 in its domain, so we just hold the expression:" in the past.  So Maxima must have improved something here.


```
    sage: integrate(ceil(x^2 + floor(x)), x, 0, 5)    # todo: Mathematica can do this
Expected:
    integrate(ceil(x^2) + floor(x), x, 0, 5)
Got:
    155/3
```

If this is right, that's good.  No idea what's going on with the next one.

In general, I'm seeing a lot of stuff that's related to having the newer Maxima.  I think that we should either upgrade Maxima first, and take care of things related to better error handling/functionality in Maxima, and then address this ticket separately, OR do this first with our current Maxima and then upgrade Maxima.    My preference would be to upgrade Maxima first, assuming one can do that relatively easily (would ECL also have to be upgraded?  It's annoying that one has to do them simultaneously at times, at least with some of my slower test machines.).



---

archive/issue_comments_061858.json:
```json
{
    "body": "I will do another run of tests with maxima-5.22.1 later. It is not too hard\nto go from one version of maxima to another. At least you don't have to rebuild\nanything else. \n\nBut it definitely looks like upgrading maxima would be a good thing,\nwe'll have to make a ticket about it.",
    "created_at": "2011-01-29T19:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61858",
    "user": "@kiwifb"
}
```

I will do another run of tests with maxima-5.22.1 later. It is not too hard
to go from one version of maxima to another. At least you don't have to rebuild
anything else. 

But it definitely looks like upgrading maxima would be a good thing,
we'll have to make a ticket about it.



---

archive/issue_comments_061859.json:
```json
{
    "body": "Something blows up rather badly here. The `MAXIMA>>` prompt indicates that you're dropped into to ECL debugger [the default behaviour of LISPs is to drop you into a debugger when an uncaught condition arises]. Ecllib tries to avoid this by executing any LISP code inside the LISP equivalent of try/except (being HANDLER-CASE). You can get tracebacks and code to see what is happening from the debugger (try \":h\" to get help about the ECL debugger)\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: dev\nsage: elliptic_e(arccoth(1), x^2*e)\nThe number 1 isn't in the domain of acoth\n -- an error. To debug this try: debugmode(true);\n```\n\nThis is Maxima printing something on the STDOUT. We should be catching this before it gets printed! In other words, find which routine in maxima prints this and monkey-patch it to raise an error *before* printing this. Apparently, maxima does raise an error after printing this, which normally gets caught on maxima's top level. But since we decapitated maxima, we're getting that now, and that is where the next thing goes wrong:\n\n```\nError in format: Unknown format directive.\n  The number ~:M isn't in the domain of ~A\n               ^\nwhile processing indirect format string:\n  ~?\n   ^\nNo restarts available.\n| Sage Version 4.6.1, Release Date: 2011-01-11                       |\n| Type notebook() for the GUI, and license() for information.        |\nBroken at LAMBDA.\nMAXIMA>> :b\n\nBacktrace:\n  > LAMBDA\n  > print-object\n  > common-lisp-user::sage-safe-apply\n\nMAXIMA>> :le\n\n(LAMBDA (CONDITION STREAM)\n  (FORMAT STREAM\n          \"~?\"\n          (SIMPLE-CONDITION-FORMAT-CONTROL CONDITION)\n          (SIMPLE-CONDITION-FORMAT-ARGUMENTS CONDITION)))\n```\n\nso a FORMAT statement is failing here. Apparently \"Condition\" objects (roughly \"exception\" objects in python) can have a format string and items hanging off them. FORMAT is LISPs \"printf\", but with a much more baroque set of options. FORMAT format specifiers have been rumoured to be Turing complete. Let's look at the parameters:\n\n```\nMAXIMA>> (SIMPLE-CONDITION-FORMAT-CONTROL CONDITION)\n\n\"The number ~:M isn't in the domain of ~A\"\nMAXIMA>> (SIMPLE-CONDITION-FORMAT-ARGUMENTS CONDITION)\n\nNIL\n```\n\nSo the \"~:M\" is probably a Maxima extension to format which is not accessible at the point where we are trying it. The fact that there are no arguments also indicates that Maxima might be forming a condition object that is not fit for general consumption.\n\nLet's see where this error really arose by stepping further up in the backtrace:\n\n```\nMAXIMA>> :p\n\nBroken at PRINT-OBJECT.\nMAXIMA>> :le\n\n(SI:LAMBDA-BLOCK PRINT-OBJECT\n                 (SI::X STREAM)\n                 (DECLARE (TYPE SIMPLE-CONDITION SI::X)\n                  (SI::NO-CHECK-TYPE SI::X))\n                 (IF *PRINT-ESCAPE*\n                     (CALL-NEXT-METHOD)\n                     ((LAMBDA (CONDITION STREAM)\n                        (FORMAT STREAM\n                                \"~?\"\n                                (SIMPLE-CONDITION-FORMAT-CONTROL CONDITION)\n                                (SIMPLE-CONDITION-FORMAT-ARGUMENTS CONDITION)))\n                      SI::X STREAM)))\n{{{\nSo this is LISP trying to print a CONDITION object. Apparently, Maxima has created a CONDITION object that doesn't allow this method to work. This could be a bug in ECL or it could be Maxima being non-compliant.\n}}}\nMAXIMA>> :p\n\nBroken at COMMON-LISP-USER::SAGE-SAFE-APPLY.\nMAXIMA>> :le\n\n(SI:LAMBDA-BLOCK COMMON-LISP-USER::SAGE-SAFE-APPLY\n                 (COMMON-LISP-USER::FUNC COMMON-LISP-USER::ARGS)\n                 (DECLARE (SI::C-GLOBAL))\n                 (HANDLER-CASE\n                  (VALUES\n                   (APPLY COMMON-LISP-USER::FUNC COMMON-LISP-USER::ARGS))\n                  (SERIOUS-CONDITION (COMMON-LISP-USER::CND)\n                   (VALUES NIL (PRINC-TO-STRING COMMON-LISP-USER::CND)))))\nMAXIMA>> COMMON-LISP-USER::FUNC\n\nMAXIMA-EVAL\nMAXIMA>> COMMON-LISP-USER::ARGS\n\n((MEVAL* '((MSETQ) $SAGE1 (($ELLIPTIC_E) ((%ACOTH) 1) ((MTIMES) ((MEXPT) $X 2) ((%EXP) 1))))))\n```\n\nFinally we're at the ecllib level. SAGE-SAFE-APPLY is the way ecllib tries to execute LISP code\nAs you can see, the arguments here indicate that this is the original call we started with, translated to maxima (well, the underlying LISP representation of maxima).\nWe know this raised an error, which gets processed by the HANDLER-CASE/SERIOUS-CONDITION. The PRINC-TO-STRING tries to make a string rendition of the CONDITION object, which fails for the reasons we have seen above.\n\nSo, the most direct way to solve the problem is to monkey-patch Maxima to raise an acceptable error *instead* of printing a message and sending a CONDITION object that crashes PRINC (which should be a near-universal printing routine). This should be relatively straightforward, because that Maxima routine already produces an acceptable string. Simply produce that string but instead of printing it, do an (ERROR string) or whatever is acceptable (the way \"retrieve\" gets monkey-patched in maximalib is already an example of that).\n\nIt does make me a bit pessimistic, though: Maxima improves some of its error reporting and in the process immediately blows up our error catching! This looks like something that is going to happen every time Maxima changes something. It's bad enough when dealing with the pexpect interface, but in this case we're basically using an unsupported and undocumented API! I know Robert Dodier is definitely sympathetic to making Maxima usable as a library, so perhaps if we can get reasonable functionality, he might be willing to take into account the required hooks when changing Maxima.",
    "created_at": "2011-01-29T21:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61859",
    "user": "@nbruin"
}
```

Something blows up rather badly here. The `MAXIMA>>` prompt indicates that you're dropped into to ECL debugger [the default behaviour of LISPs is to drop you into a debugger when an uncaught condition arises]. Ecllib tries to avoid this by executing any LISP code inside the LISP equivalent of try/except (being HANDLER-CASE). You can get tracebacks and code to see what is happening from the debugger (try ":h" to get help about the ECL debugger)


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: dev
sage: elliptic_e(arccoth(1), x^2*e)
The number 1 isn't in the domain of acoth
 -- an error. To debug this try: debugmode(true);
```

This is Maxima printing something on the STDOUT. We should be catching this before it gets printed! In other words, find which routine in maxima prints this and monkey-patch it to raise an error *before* printing this. Apparently, maxima does raise an error after printing this, which normally gets caught on maxima's top level. But since we decapitated maxima, we're getting that now, and that is where the next thing goes wrong:

```
Error in format: Unknown format directive.
  The number ~:M isn't in the domain of ~A
               ^
while processing indirect format string:
  ~?
   ^
No restarts available.
| Sage Version 4.6.1, Release Date: 2011-01-11                       |
| Type notebook() for the GUI, and license() for information.        |
Broken at LAMBDA.
MAXIMA>> :b

Backtrace:
  > LAMBDA
  > print-object
  > common-lisp-user::sage-safe-apply

MAXIMA>> :le

(LAMBDA (CONDITION STREAM)
  (FORMAT STREAM
          "~?"
          (SIMPLE-CONDITION-FORMAT-CONTROL CONDITION)
          (SIMPLE-CONDITION-FORMAT-ARGUMENTS CONDITION)))
```

so a FORMAT statement is failing here. Apparently "Condition" objects (roughly "exception" objects in python) can have a format string and items hanging off them. FORMAT is LISPs "printf", but with a much more baroque set of options. FORMAT format specifiers have been rumoured to be Turing complete. Let's look at the parameters:

```
MAXIMA>> (SIMPLE-CONDITION-FORMAT-CONTROL CONDITION)

"The number ~:M isn't in the domain of ~A"
MAXIMA>> (SIMPLE-CONDITION-FORMAT-ARGUMENTS CONDITION)

NIL
```

So the "~:M" is probably a Maxima extension to format which is not accessible at the point where we are trying it. The fact that there are no arguments also indicates that Maxima might be forming a condition object that is not fit for general consumption.

Let's see where this error really arose by stepping further up in the backtrace:

```
MAXIMA>> :p

Broken at PRINT-OBJECT.
MAXIMA>> :le

(SI:LAMBDA-BLOCK PRINT-OBJECT
                 (SI::X STREAM)
                 (DECLARE (TYPE SIMPLE-CONDITION SI::X)
                  (SI::NO-CHECK-TYPE SI::X))
                 (IF *PRINT-ESCAPE*
                     (CALL-NEXT-METHOD)
                     ((LAMBDA (CONDITION STREAM)
                        (FORMAT STREAM
                                "~?"
                                (SIMPLE-CONDITION-FORMAT-CONTROL CONDITION)
                                (SIMPLE-CONDITION-FORMAT-ARGUMENTS CONDITION)))
                      SI::X STREAM)))
{{{
So this is LISP trying to print a CONDITION object. Apparently, Maxima has created a CONDITION object that doesn't allow this method to work. This could be a bug in ECL or it could be Maxima being non-compliant.
}}}
MAXIMA>> :p

Broken at COMMON-LISP-USER::SAGE-SAFE-APPLY.
MAXIMA>> :le

(SI:LAMBDA-BLOCK COMMON-LISP-USER::SAGE-SAFE-APPLY
                 (COMMON-LISP-USER::FUNC COMMON-LISP-USER::ARGS)
                 (DECLARE (SI::C-GLOBAL))
                 (HANDLER-CASE
                  (VALUES
                   (APPLY COMMON-LISP-USER::FUNC COMMON-LISP-USER::ARGS))
                  (SERIOUS-CONDITION (COMMON-LISP-USER::CND)
                   (VALUES NIL (PRINC-TO-STRING COMMON-LISP-USER::CND)))))
MAXIMA>> COMMON-LISP-USER::FUNC

MAXIMA-EVAL
MAXIMA>> COMMON-LISP-USER::ARGS

((MEVAL* '((MSETQ) $SAGE1 (($ELLIPTIC_E) ((%ACOTH) 1) ((MTIMES) ((MEXPT) $X 2) ((%EXP) 1))))))
```

Finally we're at the ecllib level. SAGE-SAFE-APPLY is the way ecllib tries to execute LISP code
As you can see, the arguments here indicate that this is the original call we started with, translated to maxima (well, the underlying LISP representation of maxima).
We know this raised an error, which gets processed by the HANDLER-CASE/SERIOUS-CONDITION. The PRINC-TO-STRING tries to make a string rendition of the CONDITION object, which fails for the reasons we have seen above.

So, the most direct way to solve the problem is to monkey-patch Maxima to raise an acceptable error *instead* of printing a message and sending a CONDITION object that crashes PRINC (which should be a near-universal printing routine). This should be relatively straightforward, because that Maxima routine already produces an acceptable string. Simply produce that string but instead of printing it, do an (ERROR string) or whatever is acceptable (the way "retrieve" gets monkey-patched in maximalib is already an example of that).

It does make me a bit pessimistic, though: Maxima improves some of its error reporting and in the process immediately blows up our error catching! This looks like something that is going to happen every time Maxima changes something. It's bad enough when dealing with the pexpect interface, but in this case we're basically using an unsupported and undocumented API! I know Robert Dodier is definitely sympathetic to making Maxima usable as a library, so perhaps if we can get reasonable functionality, he might be willing to take into account the required hooks when changing Maxima.



---

archive/issue_comments_061860.json:
```json
{
    "body": "Attachment [errorcatching.patch](tarball://root/attachments/some-uuid/ticket7377/errorcatching.patch) by @nbruin created at 2011-01-30 07:25:59\n\nimprove maxima-eval error reporting",
    "created_at": "2011-01-30T07:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61860",
    "user": "@nbruin"
}
```

Attachment [errorcatching.patch](tarball://root/attachments/some-uuid/ticket7377/errorcatching.patch) by @nbruin created at 2011-01-30 07:25:59

improve maxima-eval error reporting



---

archive/issue_comments_061861.json:
```json
{
    "body": "I have looked a little into the error reporting and it looks like maxima was not creating the error that crashed ecllib's error string creation routine -- instead it was maxima-eval, the maxima \"top level\" replacement we run to catch and interpret maxima's error reporting. Maxima's error reporting hasn't changed since 1985. It just happened that this was the first time we stumbled into an error message that was not properly handled. The new patch \"errorcatching.patch\" (to be applied after all the \"rebased\" patches) fixes this.\n\nWe now get:\n\n```\nsage: arccoth(1).simplify()\n -- an error. To debug this try: debugmode(true);\n(result= MAXIMA-ERROR)\n($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))\nTypeError: ECL says: The number 1 isn't in the domain of acoth\nsage: elliptic_e(arccoth(1), x^2*e)\n(result=\n (MAXIMA_EVAL\n  . /usr/local/sage/4.6/local/share/maxima/5.22.1/share/orthopoly/orthopoly.lisp))\n($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))\n(result= (MAXIMA_EVAL))\n($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))\n -- an error. To debug this try: debugmode(true);\n(result= MAXIMA-ERROR)\n($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))\nelliptic_e(arccoth(1), x^2*e)\n```\n\n\nSo we see a bunch of things:\n* printing the error has now been turned off, but a quick glance at the code shows that the message `-- an error. To debug this try: debugmode(true);` cannot be turned off. I regard that a bug in Maxima and we can consider reporting that. We could also just monkeypatch MERROR.\n* the error now gets properly reported\n* there is a lot of junk diagnostic output generated by my fixed routine. Feel free to comment that back out.\n* the actual simplification of elliptic_e (whatever is tried there) apparently is wrapped in a try/except and the error reported by ecl is nicely hidden and the result is left unchanged.\n\nThis should be closer to how sage handled this first.",
    "created_at": "2011-01-30T07:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61861",
    "user": "@nbruin"
}
```

I have looked a little into the error reporting and it looks like maxima was not creating the error that crashed ecllib's error string creation routine -- instead it was maxima-eval, the maxima "top level" replacement we run to catch and interpret maxima's error reporting. Maxima's error reporting hasn't changed since 1985. It just happened that this was the first time we stumbled into an error message that was not properly handled. The new patch "errorcatching.patch" (to be applied after all the "rebased" patches) fixes this.

We now get:

```
sage: arccoth(1).simplify()
 -- an error. To debug this try: debugmode(true);
(result= MAXIMA-ERROR)
($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))
TypeError: ECL says: The number 1 isn't in the domain of acoth
sage: elliptic_e(arccoth(1), x^2*e)
(result=
 (MAXIMA_EVAL
  . /usr/local/sage/4.6/local/share/maxima/5.22.1/share/orthopoly/orthopoly.lisp))
($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))
(result= (MAXIMA_EVAL))
($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))
 -- an error. To debug this try: debugmode(true);
(result= MAXIMA-ERROR)
($error= ((MLIST) The number ~:M isn't in the domain of ~A 1 ACOTH))
elliptic_e(arccoth(1), x^2*e)
```


So we see a bunch of things:
* printing the error has now been turned off, but a quick glance at the code shows that the message `-- an error. To debug this try: debugmode(true);` cannot be turned off. I regard that a bug in Maxima and we can consider reporting that. We could also just monkeypatch MERROR.
* the error now gets properly reported
* there is a lot of junk diagnostic output generated by my fixed routine. Feel free to comment that back out.
* the actual simplification of elliptic_e (whatever is tried there) apparently is wrapped in a try/except and the error reported by ecl is nicely hidden and the result is left unchanged.

This should be closer to how sage handled this first.



---

archive/issue_comments_061862.json:
```json
{
    "body": "The following doctest from calculus.py now goes wrong:\n\n```\nlimit(-e^(x^2)*erf(x) + e^(x^2), x=oo)\n```\n\nWhich stumbles at calculus.calculus.limit at these lines:\n\n```\n   1122     return l.sage()\n   1123     return ex.parent()(l)\n```\n\nTwo return statements??? A little `hg -blame` points to #7661. Indeed, commenting out line 1122 fixes a lot of the limit problems. However, Burcin put in that line for a reason, I assume, so I'm hesitant to just commit a reversal.\n\nNote that the issue of #7661 is exactly due to a namespace collapse from SR -> Maxima; something this interface could eventually solve much more elegantly, by just mapping (at no cost) SR.var('x') to the maxima identifier \"sage_SR_var_x\".",
    "created_at": "2011-02-01T04:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61862",
    "user": "@nbruin"
}
```

The following doctest from calculus.py now goes wrong:

```
limit(-e^(x^2)*erf(x) + e^(x^2), x=oo)
```

Which stumbles at calculus.calculus.limit at these lines:

```
   1122     return l.sage()
   1123     return ex.parent()(l)
```

Two return statements??? A little `hg -blame` points to #7661. Indeed, commenting out line 1122 fixes a lot of the limit problems. However, Burcin put in that line for a reason, I assume, so I'm hesitant to just commit a reversal.

Note that the issue of #7661 is exactly due to a namespace collapse from SR -> Maxima; something this interface could eventually solve much more elegantly, by just mapping (at no cost) SR.var('x') to the maxima identifier "sage_SR_var_x".



---

archive/issue_comments_061863.json:
```json
{
    "body": "two return statements is indeed strange. Is the second return ever reached?\nCould it be a left over forgotten there? Looking at the code I am not sure\nwhat ex.parent()(l) is supposed to be.\nI haven't had time to test the errorcatching patch but will try ASAP.\nOne of my testing friend noted that maxima as a lib and ecl compiled\nwith thread support are not compatible (ever seen a SIGPWR?). I am mentioning\nthat, in case it becomes the default in ecl in the future.",
    "created_at": "2011-02-01T08:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61863",
    "user": "@kiwifb"
}
```

two return statements is indeed strange. Is the second return ever reached?
Could it be a left over forgotten there? Looking at the code I am not sure
what ex.parent()(l) is supposed to be.
I haven't had time to test the errorcatching patch but will try ASAP.
One of my testing friend noted that maxima as a lib and ecl compiled
with thread support are not compatible (ever seen a SIGPWR?). I am mentioning
that, in case it becomes the default in ecl in the future.



---

archive/issue_comments_061864.json:
```json
{
    "body": "> two return statements is indeed strange. Is the second return ever reached?\n\nNo, it isn't. However, Burcin apparently thought that `l.sage()` would give better results. I'm actually thankful that he left in the original return statement because that served as a nice flag that something had changed there.\n\n> Could it be a left over forgotten there? Looking at the code I am not sure\n> what ex.parent()(l) is supposed to be.\n\nIt is \"Coerce l into the parent of ex\", the original input parameter, i.e., coerce l into the Symbolic Ring. In the new code, \"sr_limit\" produces something that is hopefully *coercible* into the SymbolicRing -- it probably isn't a maxima object at all anymore. I think in all cases it's better to coerce into SR instead of calling l.sage(): On maxima objects it should be about the same and if limit produces something that cannot be represented in the SymbolicRing we should get an error. I'll ping him about it.\n\n> One of my testing friend noted that maxima as a lib and ecl compiled\n> with thread support are not compatible (ever seen a SIGPWR?). I am mentioning\n> that, in case it becomes the default in ecl in the future. \n\nGood to know! A little googling found http://www.hpl.hp.com/personal/Hans_Boehm/gc/debugging.html\nIt's the garbage collector that uses SIGXCPU and SIGPWR to synchronise cross-thread garbage collection. So if we want ecllib+threads we need to adjust the sage signal handler to properly handle those. BoehmGC is made for integration into C programs, so this may be doable.",
    "created_at": "2011-02-01T17:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61864",
    "user": "@nbruin"
}
```

> two return statements is indeed strange. Is the second return ever reached?

No, it isn't. However, Burcin apparently thought that `l.sage()` would give better results. I'm actually thankful that he left in the original return statement because that served as a nice flag that something had changed there.

> Could it be a left over forgotten there? Looking at the code I am not sure
> what ex.parent()(l) is supposed to be.

It is "Coerce l into the parent of ex", the original input parameter, i.e., coerce l into the Symbolic Ring. In the new code, "sr_limit" produces something that is hopefully *coercible* into the SymbolicRing -- it probably isn't a maxima object at all anymore. I think in all cases it's better to coerce into SR instead of calling l.sage(): On maxima objects it should be about the same and if limit produces something that cannot be represented in the SymbolicRing we should get an error. I'll ping him about it.

> One of my testing friend noted that maxima as a lib and ecl compiled
> with thread support are not compatible (ever seen a SIGPWR?). I am mentioning
> that, in case it becomes the default in ecl in the future. 

Good to know! A little googling found http://www.hpl.hp.com/personal/Hans_Boehm/gc/debugging.html
It's the garbage collector that uses SIGXCPU and SIGPWR to synchronise cross-thread garbage collection. So if we want ecllib+threads we need to adjust the sage signal handler to properly handle those. BoehmGC is made for integration into C programs, so this may be doable.



---

archive/issue_comments_061865.json:
```json
{
    "body": "Re-running sage -testall with maxima-lib enabled, ecl-10.4.1 maxima-5.22.1, sage-4.6.2_alpha3. Most of the time out have disappeared expect for three which at first\nsight are unrelated, but don't fail without maxima-lib\n\n```\nsage -t  -force_lib devel/sage/sage/misc/randstate.pyx\nsage -t  -force_lib devel/sage/sage/interfaces/psage.py\nsage -t  -force_lib devel/sage/sage/interfaces/sage0.py\n```\n\nFrom the first one:\n\n```\nTrying:\n    subsage = Sage()###line 134:_sage_    >>> subsage = Sage()\nExpecting nothing\nok\nTrying:\n    s = ZZ(subsage('initial_seed()'))###line 135:_sage_    >>> s = ZZ(subsage('initial_seed()'))\nExpecting nothing\n```\n\nAnd it hangs there.\n\nI also have SIGFPE in the following\n\n```\nsage -t -force_lib \"devel/sage/sage/functions/other.py\"     *\nsage -t  -force_lib devel/sage/sage/functions/log.py        *\nsage -t  -force_lib devel/sage/sage/symbolic/constants.py\nsage -t  -force_lib devel/sage/sage/symbolic/pynac.pyx \nsage -t  -force_lib devel/sage/sage/rings/complex_number.pyx \nsage -t  -force_lib devel/sage/sage/rings/real_double.pyx\nsage -t  -force_lib devel/sage/sage/rings/real_mpfr.pyx \nsage -t  -force_lib devel/sage/sage/libs/mpmath/utils.pyx\nsage -t  -force_lib devel/sage/sage/libs/mpmath/ext_libmp.pyx\nsage -t  -force_lib devel/sage/sage/libs/mpmath/ext_impl.pyx\nsage -t  -force_lib devel/sage/sage/libs/mpmath/ext_main.pyx\nsage -t  -force_lib devel/sage/sage/calculus/calculus.py    *\nsage -t  -force_lib devel/sage/sage/structure/element.pyx\nsage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_point.py \nsage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_generic.py  *\n```\n\nThe stars indicate where I also had some verbose out from maxima, usually ending\nwith\n\n```\n($error= ((MLIST SIMP) No error.))\n```\n\nAnd there is quite few more. I am doing another run with the little correction\nin calculus.py to see if that solve some of them.",
    "created_at": "2011-02-02T03:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61865",
    "user": "@kiwifb"
}
```

Re-running sage -testall with maxima-lib enabled, ecl-10.4.1 maxima-5.22.1, sage-4.6.2_alpha3. Most of the time out have disappeared expect for three which at first
sight are unrelated, but don't fail without maxima-lib

```
sage -t  -force_lib devel/sage/sage/misc/randstate.pyx
sage -t  -force_lib devel/sage/sage/interfaces/psage.py
sage -t  -force_lib devel/sage/sage/interfaces/sage0.py
```

From the first one:

```
Trying:
    subsage = Sage()###line 134:_sage_    >>> subsage = Sage()
Expecting nothing
ok
Trying:
    s = ZZ(subsage('initial_seed()'))###line 135:_sage_    >>> s = ZZ(subsage('initial_seed()'))
Expecting nothing
```

And it hangs there.

I also have SIGFPE in the following

```
sage -t -force_lib "devel/sage/sage/functions/other.py"     *
sage -t  -force_lib devel/sage/sage/functions/log.py        *
sage -t  -force_lib devel/sage/sage/symbolic/constants.py
sage -t  -force_lib devel/sage/sage/symbolic/pynac.pyx 
sage -t  -force_lib devel/sage/sage/rings/complex_number.pyx 
sage -t  -force_lib devel/sage/sage/rings/real_double.pyx
sage -t  -force_lib devel/sage/sage/rings/real_mpfr.pyx 
sage -t  -force_lib devel/sage/sage/libs/mpmath/utils.pyx
sage -t  -force_lib devel/sage/sage/libs/mpmath/ext_libmp.pyx
sage -t  -force_lib devel/sage/sage/libs/mpmath/ext_impl.pyx
sage -t  -force_lib devel/sage/sage/libs/mpmath/ext_main.pyx
sage -t  -force_lib devel/sage/sage/calculus/calculus.py    *
sage -t  -force_lib devel/sage/sage/structure/element.pyx
sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_point.py 
sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_generic.py  *
```

The stars indicate where I also had some verbose out from maxima, usually ending
with

```
($error= ((MLIST SIMP) No error.))
```

And there is quite few more. I am doing another run with the little correction
in calculus.py to see if that solve some of them.



---

archive/issue_comments_061866.json:
```json
{
    "body": "scrap the three time out. They still happen without maxima-lib I was mistaken.",
    "created_at": "2011-02-02T04:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61866",
    "user": "@kiwifb"
}
```

scrap the three time out. They still happen without maxima-lib I was mistaken.



---

archive/issue_comments_061867.json:
```json
{
    "body": "Thank you all for working on this again. I hope this will also solve some of the long standing issues we had with the maxima interface, like setting domains for variables #6862, or recognizing special symbols #6882.\n\nReplying to [comment:40 nbruin]:\n> > two return statements is indeed strange. Is the second return ever reached?\n> \n> No, it isn't. However, Burcin apparently thought that `l.sage()` would give better results. I'm actually thankful that he left in the original return statement because that served as a nice flag that something had changed there.\n\nIt was clearly a mistake on my part to leave the second return statement. I'm glad it ended up being useful though.\n\nI don't have much time these days to investigate this. So it would be great if someone can update me on the progress. Especially, when rebasing Robert's patch to split off the maxima interface, did you merge in the changes that were made to sage/interfaces/maxima.py in the meantime?\n\n> > Could it be a left over forgotten there? Looking at the code I am not sure\n> > what ex.parent()(l) is supposed to be.\n> \n> It is \"Coerce l into the parent of ex\", the original input parameter, i.e., coerce l into the Symbolic Ring. In the new code, \"sr_limit\" produces something that is hopefully *coercible* into the SymbolicRing -- it probably isn't a maxima object at all anymore. I think in all cases it's better to coerce into SR instead of calling l.sage(): On maxima objects it should be about the same and if limit produces something that cannot be represented in the SymbolicRing we should get an error. I'll ping him about it.\n\nThe operation we are using is conversion, not coercion. IMHO, the code for converting maxima objects (of any kind, pexpect or library) to Sage symbolics objects should be within the maxima objects. Most of this functionality is in sage/calculus/calculus.py at the moment, I would like to see that moved to sage/interfaces/maxima.py or it's variants.\n\nAdding a .sage() method to maxima interface objects was a step in this direction. This method knows which lookup tables to use to convert functions, etc. from maxima back to Sage. The code for this function is simply\n\n```\n   def _sage_(self):\n       import sage.calculus.calculus as calculus\n       return calculus.symbolic_expression_from_maxima_string(self.name(),\n               maxima=self.parent())\n```\n\naround line 1775 of sage/interfaces/maxima.py. I would expect this to work for the library interface to maxima as well, since AFAIK, this is also string based ATM.\n\nI am not quite sure what a conversion to the symbolic ring does for maxima interface objects. I don't expect it to have special behavior if the input is a maxima interface object. It would make sense, if it called the .sage() or ._sage_() methods of the argument though.\n\nSorry I can't be more helpful.",
    "created_at": "2011-02-02T06:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61867",
    "user": "@burcin"
}
```

Thank you all for working on this again. I hope this will also solve some of the long standing issues we had with the maxima interface, like setting domains for variables #6862, or recognizing special symbols #6882.

Replying to [comment:40 nbruin]:
> > two return statements is indeed strange. Is the second return ever reached?
> 
> No, it isn't. However, Burcin apparently thought that `l.sage()` would give better results. I'm actually thankful that he left in the original return statement because that served as a nice flag that something had changed there.

It was clearly a mistake on my part to leave the second return statement. I'm glad it ended up being useful though.

I don't have much time these days to investigate this. So it would be great if someone can update me on the progress. Especially, when rebasing Robert's patch to split off the maxima interface, did you merge in the changes that were made to sage/interfaces/maxima.py in the meantime?

> > Could it be a left over forgotten there? Looking at the code I am not sure
> > what ex.parent()(l) is supposed to be.
> 
> It is "Coerce l into the parent of ex", the original input parameter, i.e., coerce l into the Symbolic Ring. In the new code, "sr_limit" produces something that is hopefully *coercible* into the SymbolicRing -- it probably isn't a maxima object at all anymore. I think in all cases it's better to coerce into SR instead of calling l.sage(): On maxima objects it should be about the same and if limit produces something that cannot be represented in the SymbolicRing we should get an error. I'll ping him about it.

The operation we are using is conversion, not coercion. IMHO, the code for converting maxima objects (of any kind, pexpect or library) to Sage symbolics objects should be within the maxima objects. Most of this functionality is in sage/calculus/calculus.py at the moment, I would like to see that moved to sage/interfaces/maxima.py or it's variants.

Adding a .sage() method to maxima interface objects was a step in this direction. This method knows which lookup tables to use to convert functions, etc. from maxima back to Sage. The code for this function is simply

```
   def _sage_(self):
       import sage.calculus.calculus as calculus
       return calculus.symbolic_expression_from_maxima_string(self.name(),
               maxima=self.parent())
```

around line 1775 of sage/interfaces/maxima.py. I would expect this to work for the library interface to maxima as well, since AFAIK, this is also string based ATM.

I am not quite sure what a conversion to the symbolic ring does for maxima interface objects. I don't expect it to have special behavior if the input is a maxima interface object. It would make sense, if it called the .sage() or ._sage_() methods of the argument though.

Sorry I can't be more helpful.



---

archive/issue_comments_061868.json:
```json
{
    "body": "Thank you, Burcin. That is very useful information indeed.\n> I don't have much time these days to investigate this. So it would be great if someone can update me on the progress. Especially, when rebasing Robert's patch to split off the maxima interface, did you merge in the changes that were made to sage/interfaces/maxima.py in the meantime?\nI'll leave that to JP\n\n> The operation we are using is conversion, not coercion. IMHO, the code for converting maxima objects (of any kind, pexpect or library) to Sage symbolics objects should be within the maxima objects. Most of this functionality is in sage/calculus/calculus.py at the moment, I would like to see that moved to sage/interfaces/maxima.py or it's variants.\n\nOK, conversion indeed. Good to know there is a philosophy behind the change\n\n> Adding a .sage() method to maxima interface objects was a step in this direction. This method knows which lookup tables to use to convert functions, etc. from maxima back to Sage.\n\nUltimately, this model might fit better with maximalib, but currently it means some refactoring of what we already had (or just go back to the SR coercion)\n\n> around line 1775 of sage/interfaces/maxima.py. I would expect this to work for the library interface to maxima as well, since AFAIK, this is also string based ATM.\n\nWith the fastcalculus patch it is not, though. In principle one could try to polish the abstract_maxima and maxima_lib patches so that they give a drop-in string-based library interface to maxima, but I never really went that far. That would be (probably boring but) very well-defined project and might speed up adoption. \n\nWhat happens with the current set of patches:\n* a maxima_lib interface is made available that in principle should be a drop-in replacement for maxima (except that only one instance can exist)\n* this interface adds some extra methods to get \"under the hood\" of objects:\n\n  (1) There is an .ecl() method that returns the underlying EclObject (i.e., direct access to the LISP object implementing the maxima object)\n\n  (2) the maxima() method also accepts EclObjects and returns the appropriate wrapper, so maxima(M.ecl()) and maxima(eclobject).ecl() are supposed to be the identity (In a strong sense: The python wrapped might change Id but the ecl object not) where defined.\n\n  (3) sr_to_max(), a method to translate an SR object into an EclObject ready for wrapping in maxima.\n\n  (4) max_to_sr(), a method to translate an EclObject representing a maxima expression to something in or coercible to SR. Note that maxima expressions can be lists, which should be translated into a python list of SR elements, so the mapping cannot be perfectly into SR.\n\n  (5) methods sr_limit, sr_sum, sr_integrate which expect arguments living in SR and return something convertible to SR\n\nThe idea is that (3) and (4) offer a way to go back and forth between SR and maxima without using strings. maxima(E) and maxima(sr_to_max(E)) should have the same result. Similarly, SR(M) and SR(max_to_sr(M.ecl())) should have the similar result. Under the hood, sr_to_max and max_to_sr keep mappings between SR symbols and their EclObject counterparts. They build up these mappings via the string-based interface, but avoid strings once they know the mappings.\n\nThe methods in (5) were an attempt to make \"compute limit/sum/integral via maxima\" dependent on which maxima interface was in use. The old maxima-interface got stubs that just returned the result of calling the appropriate maxima expression, which returns a maxima expression, which is coercible into SR again.\n\nThe maxima-lib implementation uses sr_to_max and max_to_sr as much as possible and returns the result of a max_to_sr, so that should be coercible into SR as well.\n\nDoing it this way (at the time) was the smallest change and left as much as possible in the calculus.limit routine. The general setup fits will in Burcin's philosophy, but is presently broken because the result of a max_to_sr likely doesn't have a .sage() method. An alternative would be to push the actual conversion of the answer to SR into the sr_limit routine as well. But then one would have to tell sr_limit into which SR the answer has to be pushed. (I guess expr.parent())\n\nI think the _proper_ way to do all these computations is to construct a dummy_limit or a dummy_integral in SR first (\"inert\" limit and \"inert\" integral being the less opinionated synonyms), convert that to maxima (via sr_to_max or string-based), call the appropriate simplification on it there (note that sr_to_max will absolutely not do any simplification. It's just mapping over expression trees) and then pull the answer back via max_to_sr or string based.\n\nTo come up with a truly robust design for this (the present was just a first hack and proof-of-concept), people who know a lot about SR and the general calculus architecture need to be involved. I've tried to show with various examples on this ticket that you don't need to understand much of lisp to make sense of what happens in maxima. The sage side of this is really much more complicated than the maxima side. The ECL objects representing maxima expressions look messy and have a lot of parentheses, but have a very straightforward structure.\n\nFinally for (4): I know maxima functions like li[n] and psi[n] are not translated yet, because recognising them means looking a bit deeper in the maxima constructs. This is straightforward to do. There may be more of these constructs. Whoever wrote the string-based converter probably knows them already, because there they need special treatment too.",
    "created_at": "2011-02-02T18:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61868",
    "user": "@nbruin"
}
```

Thank you, Burcin. That is very useful information indeed.
> I don't have much time these days to investigate this. So it would be great if someone can update me on the progress. Especially, when rebasing Robert's patch to split off the maxima interface, did you merge in the changes that were made to sage/interfaces/maxima.py in the meantime?
I'll leave that to JP

> The operation we are using is conversion, not coercion. IMHO, the code for converting maxima objects (of any kind, pexpect or library) to Sage symbolics objects should be within the maxima objects. Most of this functionality is in sage/calculus/calculus.py at the moment, I would like to see that moved to sage/interfaces/maxima.py or it's variants.

OK, conversion indeed. Good to know there is a philosophy behind the change

> Adding a .sage() method to maxima interface objects was a step in this direction. This method knows which lookup tables to use to convert functions, etc. from maxima back to Sage.

Ultimately, this model might fit better with maximalib, but currently it means some refactoring of what we already had (or just go back to the SR coercion)

> around line 1775 of sage/interfaces/maxima.py. I would expect this to work for the library interface to maxima as well, since AFAIK, this is also string based ATM.

With the fastcalculus patch it is not, though. In principle one could try to polish the abstract_maxima and maxima_lib patches so that they give a drop-in string-based library interface to maxima, but I never really went that far. That would be (probably boring but) very well-defined project and might speed up adoption. 

What happens with the current set of patches:
* a maxima_lib interface is made available that in principle should be a drop-in replacement for maxima (except that only one instance can exist)
* this interface adds some extra methods to get "under the hood" of objects:

  (1) There is an .ecl() method that returns the underlying EclObject (i.e., direct access to the LISP object implementing the maxima object)

  (2) the maxima() method also accepts EclObjects and returns the appropriate wrapper, so maxima(M.ecl()) and maxima(eclobject).ecl() are supposed to be the identity (In a strong sense: The python wrapped might change Id but the ecl object not) where defined.

  (3) sr_to_max(), a method to translate an SR object into an EclObject ready for wrapping in maxima.

  (4) max_to_sr(), a method to translate an EclObject representing a maxima expression to something in or coercible to SR. Note that maxima expressions can be lists, which should be translated into a python list of SR elements, so the mapping cannot be perfectly into SR.

  (5) methods sr_limit, sr_sum, sr_integrate which expect arguments living in SR and return something convertible to SR

The idea is that (3) and (4) offer a way to go back and forth between SR and maxima without using strings. maxima(E) and maxima(sr_to_max(E)) should have the same result. Similarly, SR(M) and SR(max_to_sr(M.ecl())) should have the similar result. Under the hood, sr_to_max and max_to_sr keep mappings between SR symbols and their EclObject counterparts. They build up these mappings via the string-based interface, but avoid strings once they know the mappings.

The methods in (5) were an attempt to make "compute limit/sum/integral via maxima" dependent on which maxima interface was in use. The old maxima-interface got stubs that just returned the result of calling the appropriate maxima expression, which returns a maxima expression, which is coercible into SR again.

The maxima-lib implementation uses sr_to_max and max_to_sr as much as possible and returns the result of a max_to_sr, so that should be coercible into SR as well.

Doing it this way (at the time) was the smallest change and left as much as possible in the calculus.limit routine. The general setup fits will in Burcin's philosophy, but is presently broken because the result of a max_to_sr likely doesn't have a .sage() method. An alternative would be to push the actual conversion of the answer to SR into the sr_limit routine as well. But then one would have to tell sr_limit into which SR the answer has to be pushed. (I guess expr.parent())

I think the _proper_ way to do all these computations is to construct a dummy_limit or a dummy_integral in SR first ("inert" limit and "inert" integral being the less opinionated synonyms), convert that to maxima (via sr_to_max or string-based), call the appropriate simplification on it there (note that sr_to_max will absolutely not do any simplification. It's just mapping over expression trees) and then pull the answer back via max_to_sr or string based.

To come up with a truly robust design for this (the present was just a first hack and proof-of-concept), people who know a lot about SR and the general calculus architecture need to be involved. I've tried to show with various examples on this ticket that you don't need to understand much of lisp to make sense of what happens in maxima. The sage side of this is really much more complicated than the maxima side. The ECL objects representing maxima expressions look messy and have a lot of parentheses, but have a very straightforward structure.

Finally for (4): I know maxima functions like li[n] and psi[n] are not translated yet, because recognising them means looking a bit deeper in the maxima constructs. This is straightforward to do. There may be more of these constructs. Whoever wrote the string-based converter probably knows them already, because there they need special treatment too.



---

archive/issue_comments_061869.json:
```json
{
    "body": "Attachment [trac_7377-fastcalculus-p1.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-fastcalculus-p1.patch) by @nbruin created at 2011-02-11 09:06:50\n\nimproved fastcalculus (includes previous fixes)",
    "created_at": "2011-02-11T09:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61869",
    "user": "@nbruin"
}
```

Attachment [trac_7377-fastcalculus-p1.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-fastcalculus-p1.patch) by @nbruin created at 2011-02-11 09:06:50

improved fastcalculus (includes previous fixes)



---

archive/issue_comments_061870.json:
```json
{
    "body": "doctesting on 4.6.1 yields failures in only 12 files, and most of these are just changed formatting of output, numerical noise because floats are now binarily copied rather than transcribed via decimal string representations, and because some errors get reported differently. (For ECL everything is a RuntimeError, for instance).\n\nList here:\n\n* `devel/sage/sage/symbolic/assumptions.py`: \"Assumption\nis inconsistent\" errors get reported differently\n\n* `devel/sage/sage/symbolic/function_factory.py`: Serious issues with\ntranslating FDerivative constructs (it doesn't work at the moment)\n\n* `devel/sage/sage/symbolic/expression.pyx`: A strange\nissue with `(x*log(9)).simplify_log('all')`. Oddly,\n`(x*log(3/7)).simplify_log('all')` does behave correctly.\n\n* `devel/sage/sage/symbolic/integration/integral.py`:\n\"Maxima asks a question\" errors get reported differently, float issues\n\n* `devel/sage/sage/interfaces/maxima.py`: \"Maxima asks\na question\" errors get reported differently. These doctests are wrong, because\nthey test the maxima_lib interface via calculus, not a real maxima interface.\n\n* `devel/sage/sage/interfaces/maxima_abstract.py`:\nThese doctests were never adapted\n\n* `devel/sage/sage/calculus/calculus.py`: Whitespace\nand nintegral reports failure differently.\n\n* `devel/sage/sage/calculus/wester.py`: Looks like\ncorrect answer, but differently collected.\n\n* `devel/sage/sage/calculus/tests.py`: Odd errors. They seem to depend on\ncontext. Perhaps assumptions that aren't properly forgotten or max_to_sr cache\nthat gets spoilt?\n\n* `devel/sage/sage/calculus/desolvers.py`: lots of\nproblems. The desolve interface probably needs treatment like the to_poly_solve\nroutine.\n\n* `devel/sage/sage/calculus/functional.py`: \"Maxima\nasks a question\" gets reported differently\n\n* `devel/sage/sage/symbolic/assumptions.py`:\nInconsistent assumptions get reported differently.\n\nMost of these are a matter of changing the doctests to the generated answer, but\na few serious issues remain.",
    "created_at": "2011-02-11T09:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61870",
    "user": "@nbruin"
}
```

doctesting on 4.6.1 yields failures in only 12 files, and most of these are just changed formatting of output, numerical noise because floats are now binarily copied rather than transcribed via decimal string representations, and because some errors get reported differently. (For ECL everything is a RuntimeError, for instance).

List here:

* `devel/sage/sage/symbolic/assumptions.py`: "Assumption
is inconsistent" errors get reported differently

* `devel/sage/sage/symbolic/function_factory.py`: Serious issues with
translating FDerivative constructs (it doesn't work at the moment)

* `devel/sage/sage/symbolic/expression.pyx`: A strange
issue with `(x*log(9)).simplify_log('all')`. Oddly,
`(x*log(3/7)).simplify_log('all')` does behave correctly.

* `devel/sage/sage/symbolic/integration/integral.py`:
"Maxima asks a question" errors get reported differently, float issues

* `devel/sage/sage/interfaces/maxima.py`: "Maxima asks
a question" errors get reported differently. These doctests are wrong, because
they test the maxima_lib interface via calculus, not a real maxima interface.

* `devel/sage/sage/interfaces/maxima_abstract.py`:
These doctests were never adapted

* `devel/sage/sage/calculus/calculus.py`: Whitespace
and nintegral reports failure differently.

* `devel/sage/sage/calculus/wester.py`: Looks like
correct answer, but differently collected.

* `devel/sage/sage/calculus/tests.py`: Odd errors. They seem to depend on
context. Perhaps assumptions that aren't properly forgotten or max_to_sr cache
that gets spoilt?

* `devel/sage/sage/calculus/desolvers.py`: lots of
problems. The desolve interface probably needs treatment like the to_poly_solve
routine.

* `devel/sage/sage/calculus/functional.py`: "Maxima
asks a question" gets reported differently

* `devel/sage/sage/symbolic/assumptions.py`:
Inconsistent assumptions get reported differently.

Most of these are a matter of changing the doctests to the generated answer, but
a few serious issues remain.



---

archive/issue_comments_061871.json:
```json
{
    "body": "David Kirkby and I have started to look at up updating ecl to 11.1.1 in #10766.\nFrom my own experiments some of this patch set will need rebasing if it goes in.\n\nI will certainly test your new patch.",
    "created_at": "2011-02-11T09:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61871",
    "user": "@kiwifb"
}
```

David Kirkby and I have started to look at up updating ecl to 11.1.1 in #10766.
From my own experiments some of this patch set will need rebasing if it goes in.

I will certainly test your new patch.



---

archive/issue_comments_061872.json:
```json
{
    "body": "improved formatting of error message when maxima asks a question",
    "created_at": "2011-02-14T07:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61872",
    "user": "@nbruin"
}
```

improved formatting of error message when maxima asks a question



---

archive/issue_comments_061873.json:
```json
{
    "body": "Attachment [trac_7377-better-ask-error.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-better-ask-error.patch) by @nbruin created at 2011-02-14 07:12:01\n\nthe lisp function `retrieve` in maxima is responsible for asking questions, so we just monkey-patch it to throw an error with an informative message instead. The patch trac_7377-better-ask-error.patch improves the readability of this message by executing exactly the original code in retrieve, but wrapped in a `(with-output-to-string (*standard-output*) ...)`. The method is generally applicable and may be useful in adapting other printing bits.\n\nOddly enough, this patch does not invalidate any additional doctests, but:\n\n```\nsage -t  \"devel/sage-devel/sage/interfaces/maxima_lib.py\"   \n**********************************************************************\nError: TAB character found.\n```\n\nso perhaps maxima inserts a TAB in the error message. Are TABs not allowed in doctest output?\n(it looks like one gets produced and matched by a \"...\" in the doctest template). A `sage -t --verbose` shows that no individual test fails.",
    "created_at": "2011-02-14T07:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61873",
    "user": "@nbruin"
}
```

Attachment [trac_7377-better-ask-error.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-better-ask-error.patch) by @nbruin created at 2011-02-14 07:12:01

the lisp function `retrieve` in maxima is responsible for asking questions, so we just monkey-patch it to throw an error with an informative message instead. The patch trac_7377-better-ask-error.patch improves the readability of this message by executing exactly the original code in retrieve, but wrapped in a `(with-output-to-string (*standard-output*) ...)`. The method is generally applicable and may be useful in adapting other printing bits.

Oddly enough, this patch does not invalidate any additional doctests, but:

```
sage -t  "devel/sage-devel/sage/interfaces/maxima_lib.py"   
**********************************************************************
Error: TAB character found.
```

so perhaps maxima inserts a TAB in the error message. Are TABs not allowed in doctest output?
(it looks like one gets produced and matched by a "..." in the doctest template). A `sage -t --verbose` shows that no individual test fails.



---

archive/issue_comments_061874.json:
```json
{
    "body": "I accidentally introduced a TAB by mistake in a doctest the other and it was flagged so I'd say it is not allowed. Good news, bad news time. David Kirkby and I are updating ecl to 11.1.1 and maxima to 5.23.2 in #10766 (ecl) and #10773 (maxima).\n\nThe bad news is that the current patches in this ticket will need rebasing again because of the patches I had to apply for ecl-11.1.1. Actually I wouldn't mind some input on #10766 as it seem to resurrect #6189.",
    "created_at": "2011-02-14T09:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61874",
    "user": "@kiwifb"
}
```

I accidentally introduced a TAB by mistake in a doctest the other and it was flagged so I'd say it is not allowed. Good news, bad news time. David Kirkby and I are updating ecl to 11.1.1 and maxima to 5.23.2 in #10766 (ecl) and #10773 (maxima).

The bad news is that the current patches in this ticket will need rebasing again because of the patches I had to apply for ecl-11.1.1. Actually I wouldn't mind some input on #10766 as it seem to resurrect #6189.



---

archive/issue_comments_061875.json:
```json
{
    "body": "I forgot I already posted about ecl. Anyway, Nils could you put in the description the list of patches to apply and in which order if it is relevant?\n\nI mean, is the error_catching.patch still necessary with the 2 new patches?",
    "created_at": "2011-02-14T09:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61875",
    "user": "@kiwifb"
}
```

I forgot I already posted about ecl. Anyway, Nils could you put in the description the list of patches to apply and in which order if it is relevant?

I mean, is the error_catching.patch still necessary with the 2 new patches?



---

archive/issue_comments_061876.json:
```json
{
    "body": "Never mind. I'll just go to bed.",
    "created_at": "2011-02-14T09:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61876",
    "user": "@kiwifb"
}
```

Never mind. I'll just go to bed.



---

archive/issue_comments_061877.json:
```json
{
    "body": "#10766 and #10773 now both have positive review.  #10766 vis-a-vis #6189 does happen, but maybe it just doesn't matter - that's what we concluded, but we'll see how the release manager(s) feels (feel).\n\nI would like to work on fixing some of these issues soon enough for this to be in 4.7, but I have a feeling the desolver and abstract derivative piece might be a little time-consuming.  At worst with the deriv, we could just figure out what Sage was passing/getting from Maxima before and jerry-rig that, though it's not a long-term solution.",
    "created_at": "2011-02-14T19:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61877",
    "user": "@kcrisman"
}
```

#10766 and #10773 now both have positive review.  #10766 vis-a-vis #6189 does happen, but maybe it just doesn't matter - that's what we concluded, but we'll see how the release manager(s) feels (feel).

I would like to work on fixing some of these issues soon enough for this to be in 4.7, but I have a feeling the desolver and abstract derivative piece might be a little time-consuming.  At worst with the deriv, we could just figure out what Sage was passing/getting from Maxima before and jerry-rig that, though it's not a long-term solution.



---

archive/issue_comments_061878.json:
```json
{
    "body": ">  desolver \nThis might be not so bad.\n\nThe main thing there is that the call forms for \"desolve\" are rather complicated, because there are all kinds of auxiliary arguments. to_poly_solve had a similar problem. I solved that by declaring an explicit to_poly_solve method on maxima_lib.MaximaElement.\n\nProbably just parsing the optional arguments and putting them together in the right kind of structure (see to_poly_solve for an example) solves most problems.\n\nI don't know how bad the structures are that come back from desolve, but for most cases I have had surprisingly little problems in that direction.\n\n> abstract derivative\n\nThe whole `D[0](f)` syntax needs separate treatment. I realized later that currently, only\n`D[i,j,k](f)(x1,x2,...,xn)` is allowed if `x1,...,xn` are distinct symbolic variables. This surprised me a bit. Sage support for functional derivatives is only rudimentary.\n\nI think that if we have an expression: `D[i0,...,ir](f)(e0,...,en)`, we should just do\n`diff( f(t0,...,tn), [[t0,...,tn][i] for i in [i0,...,ir]]).subs({t0:e0,...,tn:en})`\ni.e., introduce temporary variables t0,...,tn to take the appropriate derivate relative to named variables and then specialize to the evaluation point requested. Is there a reason this approach has not been taken? Just lack of need/implementation time?\n\nIn Maxima one can take exactly the same approach:\n\n```\nat(diff( f(t0,t1,t2,t3) , t0,1,t1,1,t0,1 ), [t0=e0,t1=e1,t2=e2])\n```\n\nthe documentation of at is scary: substitutions are done in series, not in parallel. That's basically a bug given the intended use of the routine, even though it is documented behaviour. However, if we make sure that our temporary variables are truly unique, there should be no problem. Perhaps call `gensym`.",
    "created_at": "2011-02-14T20:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61878",
    "user": "@nbruin"
}
```

>  desolver 
This might be not so bad.

The main thing there is that the call forms for "desolve" are rather complicated, because there are all kinds of auxiliary arguments. to_poly_solve had a similar problem. I solved that by declaring an explicit to_poly_solve method on maxima_lib.MaximaElement.

Probably just parsing the optional arguments and putting them together in the right kind of structure (see to_poly_solve for an example) solves most problems.

I don't know how bad the structures are that come back from desolve, but for most cases I have had surprisingly little problems in that direction.

> abstract derivative

The whole `D[0](f)` syntax needs separate treatment. I realized later that currently, only
`D[i,j,k](f)(x1,x2,...,xn)` is allowed if `x1,...,xn` are distinct symbolic variables. This surprised me a bit. Sage support for functional derivatives is only rudimentary.

I think that if we have an expression: `D[i0,...,ir](f)(e0,...,en)`, we should just do
`diff( f(t0,...,tn), [[t0,...,tn][i] for i in [i0,...,ir]]).subs({t0:e0,...,tn:en})`
i.e., introduce temporary variables t0,...,tn to take the appropriate derivate relative to named variables and then specialize to the evaluation point requested. Is there a reason this approach has not been taken? Just lack of need/implementation time?

In Maxima one can take exactly the same approach:

```
at(diff( f(t0,t1,t2,t3) , t0,1,t1,1,t0,1 ), [t0=e0,t1=e1,t2=e2])
```

the documentation of at is scary: substitutions are done in series, not in parallel. That's basically a bug given the intended use of the routine, even though it is documented behaviour. However, if we make sure that our temporary variables are truly unique, there should be no problem. Perhaps call `gensym`.



---

archive/issue_comments_061879.json:
```json
{
    "body": "OK so I tested the new patch set on sage-on-gentoo and it is strange. I see all the doctests failures that Nils is seeing. Plus a few more strangely enough in scheme/elliptic_curves/ that you wouldn't think are related. But I also get a lot of SIGFPE all over the place from seemingly unrelated components (mpmath, pynac...).\nThey go away when I rebuild without the patches.\n\nI fail to see the cause to effect relation between maxima-lib and these, but there they are.\n\nI almost forgot I have an unpickling failure as well\n\n```\nsage -t -force_lib \"devel/sage-main/sage/structure/sage_object.pyx\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/structure/sage_object.pyx\", line 1053:\n    sage: print \"x\"; sage.structure.sage_object.unpickle_all()\nExpected:\n    x...\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    x\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead\n     * unpickle failure: load('/home/fbissey/.sage/temp/QCD_nzi3/26167/dir_2/pickle_jar/_class__sage_interfaces_maxima_MaximaFunction__.sobj')\n    Failed:\n    _class__sage_interfaces_maxima_MaximaFunction__.sobj\n    Successfully unpickled 585 objects.\n    Failed to unpickle 1 objects.\n```\n",
    "created_at": "2011-02-15T02:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61879",
    "user": "@kiwifb"
}
```

OK so I tested the new patch set on sage-on-gentoo and it is strange. I see all the doctests failures that Nils is seeing. Plus a few more strangely enough in scheme/elliptic_curves/ that you wouldn't think are related. But I also get a lot of SIGFPE all over the place from seemingly unrelated components (mpmath, pynac...).
They go away when I rebuild without the patches.

I fail to see the cause to effect relation between maxima-lib and these, but there they are.

I almost forgot I have an unpickling failure as well

```
sage -t -force_lib "devel/sage-main/sage/structure/sage_object.pyx"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/structure/sage_object.pyx", line 1053:
    sage: print "x"; sage.structure.sage_object.unpickle_all()
Expected:
    x...
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    x
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
     * unpickle failure: load('/home/fbissey/.sage/temp/QCD_nzi3/26167/dir_2/pickle_jar/_class__sage_interfaces_maxima_MaximaFunction__.sobj')
    Failed:
    _class__sage_interfaces_maxima_MaximaFunction__.sobj
    Successfully unpickled 585 objects.
    Failed to unpickle 1 objects.
```




---

archive/issue_comments_061880.json:
```json
{
    "body": "Replying to [comment:55 fbissey]:\n>  But I also get a lot of SIGFPE all over the place from seemingly unrelated components \nECL does normally install SIG handlers, but we try to put them back (at the time Juanjo said this should be basically safe). The responsible code is in `sage.libs.ecl.init_ecl()`,\n`sage/libs/ecl.pyx:131`.\n\n```\n    #get all the signal handlers (does any system have signal numbers above 32?)\n    for i in range(1,33):\n        sigaction(i,NULL,&(act[i])) \n \n    #initialize ECL\n    cl_boot(0, argv)\n    \n    #and put the signal handlers back\n    for i in range(1,33):\n        sigaction(i,&(act[i]),NULL)\n```\n\nTo see if this is the culprit, take a pristine sage and ensure that sage.libs.ecl_init() gets called upon initialization (i.e., insert a call into some module to ensure this gets called. Normally it doesn't)\nNow run the SIGFPE producing doctests. Do they offend again? Perhaps you can improve ecllib's initialization?\n\nOther things to watch out for:\n- Your Boehm-Weiser GC might be built with different options\n- Make sure that ecl.so links against the same MPIR/GMP library. Having two GMPs hang around will definitely wreak havoc.\n\n(I think I saw the pickling error too. Some gherkin expert can probably easily pinpoint what's wrong and how to fix it)",
    "created_at": "2011-02-15T04:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61880",
    "user": "@nbruin"
}
```

Replying to [comment:55 fbissey]:
>  But I also get a lot of SIGFPE all over the place from seemingly unrelated components 
ECL does normally install SIG handlers, but we try to put them back (at the time Juanjo said this should be basically safe). The responsible code is in `sage.libs.ecl.init_ecl()`,
`sage/libs/ecl.pyx:131`.

```
    #get all the signal handlers (does any system have signal numbers above 32?)
    for i in range(1,33):
        sigaction(i,NULL,&(act[i])) 
 
    #initialize ECL
    cl_boot(0, argv)
    
    #and put the signal handlers back
    for i in range(1,33):
        sigaction(i,&(act[i]),NULL)
```

To see if this is the culprit, take a pristine sage and ensure that sage.libs.ecl_init() gets called upon initialization (i.e., insert a call into some module to ensure this gets called. Normally it doesn't)
Now run the SIGFPE producing doctests. Do they offend again? Perhaps you can improve ecllib's initialization?

Other things to watch out for:
- Your Boehm-Weiser GC might be built with different options
- Make sure that ecl.so links against the same MPIR/GMP library. Having two GMPs hang around will definitely wreak havoc.

(I think I saw the pickling error too. Some gherkin expert can probably easily pinpoint what's wrong and how to fix it)



---

archive/issue_comments_061881.json:
```json
{
    "body": "I produced new versions of the patches based on Sage 4.6.2.alpha4, ECL 11.1.1 of !#10766 and Maxima 5.23.1 of #10773.\n\nI think I forgot to include some changes in Sage in the previous rebased patches, things should be better with those versions.\n\nThe patches will follow shortly.\n\nI'm currently running \"make ptest\" to check I get the same failures as what was posted above.\n\nI'm also currently trying to get rid of the Pexpect class inheritage of MaximaAbstract and MaximaLib classes.\n\nThe best idea I got so far is to split all the non-pexpect and non-communication things of Sage pexpect class into a parent class and make MaximaAbstract inherit from that class so that we still have access to all the nice features defined in Pexpect class.\n\nMaximaLib would just inherit MaximaAbstract and Maxima woulb inherit both MaximaAbstract and Pexpect.\n\nI'll post this set of patches asap.",
    "created_at": "2011-02-15T17:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61881",
    "user": "jpflori"
}
```

I produced new versions of the patches based on Sage 4.6.2.alpha4, ECL 11.1.1 of !#10766 and Maxima 5.23.1 of #10773.

I think I forgot to include some changes in Sage in the previous rebased patches, things should be better with those versions.

The patches will follow shortly.

I'm currently running "make ptest" to check I get the same failures as what was posted above.

I'm also currently trying to get rid of the Pexpect class inheritage of MaximaAbstract and MaximaLib classes.

The best idea I got so far is to split all the non-pexpect and non-communication things of Sage pexpect class into a parent class and make MaximaAbstract inherit from that class so that we still have access to all the nice features defined in Pexpect class.

MaximaLib would just inherit MaximaAbstract and Maxima woulb inherit both MaximaAbstract and Pexpect.

I'll post this set of patches asap.



---

archive/issue_comments_061882.json:
```json
{
    "body": "Attachment [trac_7377-abstract-maxima_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-abstract-maxima_p2.patch) by jpflori created at 2011-02-15 17:06:50\n\nPatch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 1",
    "created_at": "2011-02-15T17:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61882",
    "user": "jpflori"
}
```

Attachment [trac_7377-abstract-maxima_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-abstract-maxima_p2.patch) by jpflori created at 2011-02-15 17:06:50

Patch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 1



---

archive/issue_comments_061883.json:
```json
{
    "body": "Patch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 2",
    "created_at": "2011-02-15T17:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61883",
    "user": "jpflori"
}
```

Patch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 2



---

archive/issue_comments_061884.json:
```json
{
    "body": "Attachment [trac_7377-maximalib_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-maximalib_p2.patch) by jpflori created at 2011-02-15 17:07:24\n\nPatch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 3",
    "created_at": "2011-02-15T17:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61884",
    "user": "jpflori"
}
```

Attachment [trac_7377-maximalib_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-maximalib_p2.patch) by jpflori created at 2011-02-15 17:07:24

Patch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 3



---

archive/issue_comments_061885.json:
```json
{
    "body": "Attachment [trac_7377-fastcalculus_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-fastcalculus_p2.patch) by jpflori created at 2011-02-15 17:07:51\n\nPatch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 4",
    "created_at": "2011-02-15T17:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61885",
    "user": "jpflori"
}
```

Attachment [trac_7377-fastcalculus_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-fastcalculus_p2.patch) by jpflori created at 2011-02-15 17:07:51

Patch based on Sage 4.6.2.alpha4, ECL 11.1.1 and Maxima 5.23.1, apply 4



---

archive/issue_comments_061886.json:
```json
{
    "body": "Attachment [trac_7377-better-ask-error_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-better-ask-error_p2.patch) by @kcrisman created at 2011-02-15 17:16:11\n\n> The best idea I got so far is to split all the non-pexpect and non-communication things of Sage pexpect class into a parent class and make MaximaAbstract inherit from that class so that we still have access to all the nice features defined in Pexpect class.\n\nYes, we want to make sure that we can still use Maxima via the console as before, with all the usual stuff.   I don't know exactly the best way to do that, but we definitely want that.",
    "created_at": "2011-02-15T17:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61886",
    "user": "@kcrisman"
}
```

Attachment [trac_7377-better-ask-error_p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-better-ask-error_p2.patch) by @kcrisman created at 2011-02-15 17:16:11

> The best idea I got so far is to split all the non-pexpect and non-communication things of Sage pexpect class into a parent class and make MaximaAbstract inherit from that class so that we still have access to all the nice features defined in Pexpect class.

Yes, we want to make sure that we can still use Maxima via the console as before, with all the usual stuff.   I don't know exactly the best way to do that, but we definitely want that.



---

archive/issue_comments_061887.json:
```json
{
    "body": "Here is the list of the failure left in \"make ptest\" with all \"_p2\" patches applied:\n\n\n```\nThe following tests failed:\n\n\tsage -t  -force_lib devel/sage/sage/symbolic/assumptions.py # 2 doctests failed\n\tsage -t  -force_lib devel/sage/sage/symbolic/function_factory.py # 3 doctests failed\n\tsage -t  -force_lib devel/sage/sage/symbolic/expression.pyx # 1 doctests failed\n\tsage -t  -force_lib devel/sage/sage/symbolic/integration/integral.py # 5 doctests failed\n\tsage -t  -force_lib devel/sage/sage/interfaces/maxima_lib.py # 0 doctests failed\n\tsage -t  -force_lib devel/sage/sage/interfaces/maxima.py # 2 doctests failed\n\tsage -t  -force_lib devel/sage/sage/calculus/tests.py # 4 doctests failed\n\tsage -t  -force_lib devel/sage/sage/calculus/wester.py # 1 doctests failed\n\tsage -t  -force_lib devel/sage/sage/calculus/calculus.py # 2 doctests failed\n\tsage -t  -force_lib devel/sage/sage/calculus/desolvers.py # 7 doctests failed\n\tsage -t  -force_lib devel/sage/sage/calculus/functional.py # 1 doctests failed\n\tsage -t  -force_lib devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\n\n```\n\n1. symbolic/assumptions.py : Error reporting changed (RuntimeError ...)\n2. symbolic/function_factory.py : \"del\" thing as posted earlier\n3. symbolic/expression.pyx : got \"x*log(9)\" instead of \"log(9!^x)\" so Maxima got better in simplify_all, but also a lot of blabbering : \"solve: using arc-trig functions to get a solution.\nSome solutions will be lost.\" and \"rat: replaced -0.032 by -4/125 = -0.032\"\n\n1. symbolic/integration/integral.py : error reporting, numerical noise and same kind of verbosity as mentionned above (\"rat: replaced ...\")\n2. interfaces/maxima_lib.py : TAB character (anyway changes are still missing)\n3. interfaces/maxima.py : Error reporting\n4. calculus/tests.py :\n\n   * integrate(ceil(x!^2 + floor(x)), x, 0, 5) gives 155/3 instead of integrate(ceil(x!^2) + floor(x), x, 0, 5), Maple gives me 145\n   * integrate(sin(x), x, a, b) gives cos(a) - cos(b) instead of ceil(cos(a)) ...\n   * next 2 errors are !__call!__() takes at most 3 arguments (4 given)\u00a0\n5. calculus/wester.py : some verbosity (\"solve:...\"), the results are printed differently but are equal (I'll test with #9880)\n6. calculus/calculus.py : \n\n   * a = sage.calculus.calculus.maxima(\"x!#0\"); a gives x # 0 and a lot of strange verbosity (\"***JOB ABORT DUE TO UNRECOVERED ERROR.\") instead of x#0\n   * nintegral reports error differently\n7. calculus/desolvers.py : seems broken, lots of ascii art displayed things\n8. calculus/functional.py : error reporting\n9. structure/sage_object.pyx : unpickle failure: load('/home/jp/.sage/temp/napoleon/8057/dir_2/pickle_jar/_class!__sage_interfaces_maxima_MaximaFunction!__.sobj')\n\nSo I get the same errors as reported above. I don't know why Maxima gets so verbose (\"rat:...\", \"solve:...\", ascii art things in desolve, \"-- an error.  To debug this try debugmode(true);\"...), was it intended in the patches ?\n\nCheers,",
    "created_at": "2011-02-16T09:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61887",
    "user": "jpflori"
}
```

Here is the list of the failure left in "make ptest" with all "_p2" patches applied:


```
The following tests failed:

	sage -t  -force_lib devel/sage/sage/symbolic/assumptions.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/function_factory.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/integration/integral.py # 5 doctests failed
	sage -t  -force_lib devel/sage/sage/interfaces/maxima_lib.py # 0 doctests failed
	sage -t  -force_lib devel/sage/sage/interfaces/maxima.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/tests.py # 4 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/wester.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/calculus.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/desolvers.py # 7 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/functional.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/structure/sage_object.pyx # 1 doctests failed

```

1. symbolic/assumptions.py : Error reporting changed (RuntimeError ...)
2. symbolic/function_factory.py : "del" thing as posted earlier
3. symbolic/expression.pyx : got "x*log(9)" instead of "log(9!^x)" so Maxima got better in simplify_all, but also a lot of blabbering : "solve: using arc-trig functions to get a solution.
Some solutions will be lost." and "rat: replaced -0.032 by -4/125 = -0.032"

1. symbolic/integration/integral.py : error reporting, numerical noise and same kind of verbosity as mentionned above ("rat: replaced ...")
2. interfaces/maxima_lib.py : TAB character (anyway changes are still missing)
3. interfaces/maxima.py : Error reporting
4. calculus/tests.py :

   * integrate(ceil(x!^2 + floor(x)), x, 0, 5) gives 155/3 instead of integrate(ceil(x!^2) + floor(x), x, 0, 5), Maple gives me 145
   * integrate(sin(x), x, a, b) gives cos(a) - cos(b) instead of ceil(cos(a)) ...
   * next 2 errors are !__call!__() takes at most 3 arguments (4 given) 
5. calculus/wester.py : some verbosity ("solve:..."), the results are printed differently but are equal (I'll test with #9880)
6. calculus/calculus.py : 

   * a = sage.calculus.calculus.maxima("x!#0"); a gives x # 0 and a lot of strange verbosity ("***JOB ABORT DUE TO UNRECOVERED ERROR.") instead of x#0
   * nintegral reports error differently
7. calculus/desolvers.py : seems broken, lots of ascii art displayed things
8. calculus/functional.py : error reporting
9. structure/sage_object.pyx : unpickle failure: load('/home/jp/.sage/temp/napoleon/8057/dir_2/pickle_jar/_class!__sage_interfaces_maxima_MaximaFunction!__.sobj')

So I get the same errors as reported above. I don't know why Maxima gets so verbose ("rat:...", "solve:...", ascii art things in desolve, "-- an error.  To debug this try debugmode(true);"...), was it intended in the patches ?

Cheers,



---

archive/issue_comments_061888.json:
```json
{
    "body": "My experience is totally different. I patched my sage-on-gentoo to the max (ecl/maxima/cython/mpmath/ppl+this set), reinstall ecl-11.1.1, maxima-5.23.2 and sage-4.6.2.alpha4 and ran the tests.\n\nThe only abnormal failure for sage-on-gentoo was interfaces/r.py and it didn't show up again when I tried it individually. No SIGFPE, everything fine. \nThis is a 64 bit intel machine and the install of the sage spkg itself was from scratch. \n\nIt's the first time this patch set doesn't give me a huge amount of broken doctests back.",
    "created_at": "2011-02-16T10:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61888",
    "user": "@kiwifb"
}
```

My experience is totally different. I patched my sage-on-gentoo to the max (ecl/maxima/cython/mpmath/ppl+this set), reinstall ecl-11.1.1, maxima-5.23.2 and sage-4.6.2.alpha4 and ran the tests.

The only abnormal failure for sage-on-gentoo was interfaces/r.py and it didn't show up again when I tried it individually. No SIGFPE, everything fine. 
This is a 64 bit intel machine and the install of the sage spkg itself was from scratch. 

It's the first time this patch set doesn't give me a huge amount of broken doctests back.



---

archive/issue_comments_061889.json:
```json
{
    "body": "Replying to [comment:59 jpflori]:\n> So I get the same errors as reported above. I don't know why Maxima gets so verbose (\"rat:...\", \"solve:...\", ascii art things in desolve, \"-- an error.  To debug this try debugmode(true);\"...), was it intended in the patches ?\n\nThat's wonderful! A cleaner refactoring as proposed above would be great. Concerning the verbosity: Maxima is always like that. With the current interface, pexpect receives this and filters it out. With the library setup, we're not listening to stdout anymore, so this ends up with the user. Possible solutions:\n\n- get maxima patched to have options to remove these warnings & verbosity. There are already a few out there (no error message is printed anymore thanks to turning one off), but others survive (the \" -- an error occurred ...\" is hard-wired. I've reported that one to Maxima)\n\n- live with it (that shouldn't be necessary)\n\n- redirect lisp standard output. Thankfully, lisp wraps all its I/O in its own stream system which allows for redirection so if we feed (setf *standard-output* *dev-null*) to ECL during maxima initialization, we'll never see anything (obviously not a good idea for debugging). Perhaps we also need that on *standard-error*. In fact, since a lot of this output does not seem to affect doctesting, perhaps it's already ending up on stderr.\n\nThis actually suggests another approach to getting a strings-based interface to maxima/ECLlib:\n\n- locate the Maxima Read/Evaluate/Print loop and break it open to just be a Read/Evaluate/Print routine maxima-rep (i.e., it returns instead of looping)\n- wrap this routine:\n\n```\n(defun mrep-with-stringio (maxima-input-string)\n   (let ((*standard-input* (make-string-input-stream maxima-input-string))\n         (*standard-output* (make-string-output-stream)))\n      (maxima-rep)\n      (get-output-stream-string *standard-output*)\n))\n```\n\nThis approach would be a little closer to the current pexpect interface, so you could possibly reuse more of the current maxima pexpect interface. You'd still only be communicating with maxima via string I/O, though, whereas we can do much better with the library. It would be an option if all you're interested in is creating an I/O based interface to maxima without fork.",
    "created_at": "2011-02-16T17:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61889",
    "user": "@nbruin"
}
```

Replying to [comment:59 jpflori]:
> So I get the same errors as reported above. I don't know why Maxima gets so verbose ("rat:...", "solve:...", ascii art things in desolve, "-- an error.  To debug this try debugmode(true);"...), was it intended in the patches ?

That's wonderful! A cleaner refactoring as proposed above would be great. Concerning the verbosity: Maxima is always like that. With the current interface, pexpect receives this and filters it out. With the library setup, we're not listening to stdout anymore, so this ends up with the user. Possible solutions:

- get maxima patched to have options to remove these warnings & verbosity. There are already a few out there (no error message is printed anymore thanks to turning one off), but others survive (the " -- an error occurred ..." is hard-wired. I've reported that one to Maxima)

- live with it (that shouldn't be necessary)

- redirect lisp standard output. Thankfully, lisp wraps all its I/O in its own stream system which allows for redirection so if we feed (setf *standard-output* *dev-null*) to ECL during maxima initialization, we'll never see anything (obviously not a good idea for debugging). Perhaps we also need that on *standard-error*. In fact, since a lot of this output does not seem to affect doctesting, perhaps it's already ending up on stderr.

This actually suggests another approach to getting a strings-based interface to maxima/ECLlib:

- locate the Maxima Read/Evaluate/Print loop and break it open to just be a Read/Evaluate/Print routine maxima-rep (i.e., it returns instead of looping)
- wrap this routine:

```
(defun mrep-with-stringio (maxima-input-string)
   (let ((*standard-input* (make-string-input-stream maxima-input-string))
         (*standard-output* (make-string-output-stream)))
      (maxima-rep)
      (get-output-stream-string *standard-output*)
))
```

This approach would be a little closer to the current pexpect interface, so you could possibly reuse more of the current maxima pexpect interface. You'd still only be communicating with maxima via string I/O, though, whereas we can do much better with the library. It would be an option if all you're interested in is creating an I/O based interface to maxima without fork.



---

archive/issue_comments_061890.json:
```json
{
    "body": "Replying to [comment:60 fbissey]:\n> My experience is totally different. I patched my sage-on-gentoo to the max (ecl/maxima/cython/mpmath/ppl+this set), reinstall ecl-11.1.1, maxima-5.23.2 and sage-4.6.2.alpha4 and ran the tests.\n> \n> The only abnormal failure for sage-on-gentoo was interfaces/r.py and it didn't show up again when I tried it individually. No SIGFPE, everything fine. \n> This is a 64 bit intel machine and the install of the sage spkg itself was from scratch. \n> \n> It's the first time this patch set doesn't give me a huge amount of broken doctests back.\n\nDear me. I should have a curfew. I hadn't applied the maximalib patch after all. :(",
    "created_at": "2011-02-16T18:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61890",
    "user": "@kiwifb"
}
```

Replying to [comment:60 fbissey]:
> My experience is totally different. I patched my sage-on-gentoo to the max (ecl/maxima/cython/mpmath/ppl+this set), reinstall ecl-11.1.1, maxima-5.23.2 and sage-4.6.2.alpha4 and ran the tests.
> 
> The only abnormal failure for sage-on-gentoo was interfaces/r.py and it didn't show up again when I tried it individually. No SIGFPE, everything fine. 
> This is a 64 bit intel machine and the install of the sage spkg itself was from scratch. 
> 
> It's the first time this patch set doesn't give me a huge amount of broken doctests back.

Dear me. I should have a curfew. I hadn't applied the maximalib patch after all. :(



---

archive/issue_comments_061891.json:
```json
{
    "body": "I get the same thing that Jean-Pierre in the end. But the SIGFPE I had before are gone. For some tests it is indeed just a matter of change in error reporting and we could just fix the doctests. I notice that sage/interfaces/maxima.py and sage/symbolic/integration/integral.py have a test in common:\"integral(x^n,x)\"\nI also got an ecl error already mentioned\n\n```\nFile \"/usr/share/sage/devel/sage-main/sage/libs/ecl.pyx\", line 415:\n    sage: a\nExpected:\n    <ECL: 9.999999999999999E39>\nGot:\n    <ECL: 9.999999999999999e39>\n```\n",
    "created_at": "2011-02-16T21:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61891",
    "user": "@kiwifb"
}
```

I get the same thing that Jean-Pierre in the end. But the SIGFPE I had before are gone. For some tests it is indeed just a matter of change in error reporting and we could just fix the doctests. I notice that sage/interfaces/maxima.py and sage/symbolic/integration/integral.py have a test in common:"integral(x^n,x)"
I also got an ecl error already mentioned

```
File "/usr/share/sage/devel/sage-main/sage/libs/ecl.pyx", line 415:
    sage: a
Expected:
    <ECL: 9.999999999999999E39>
Got:
    <ECL: 9.999999999999999e39>
```




---

archive/issue_comments_061892.json:
```json
{
    "body": "I've put a first (very) rough version of a patch to refactor the different interfaces:\n\n* It split the previous Expect classes in Interface classes (without pexpect stuff, did not find a better name) and Expect classes (inheriting from the previous ones + pexpect stuff)\n* MaximaAbstract classes depends on Interface classes\n* MaximaLib on MaximaAbstract\n* Maxima (classic) on MaximaAbstract and Expect\n\nIt kind of works easily thanks to the current Method Resolution Order used by the version of Python in Sage but it obviously introduces a lot of new failures in addition to the one above.\n\nThe patch must be applied after the \"_p2\" patches (and ecl_iter).\n\nIt is quite big, touches a lot of files, and should be splitted in at least two parts (split Expect; refactor).\n\nIt is absolutely not considered as finished (very far from it) and I did not test it (apart from trivial things like integrate(x)), it is mainly to get some feedback on the choices I made, so any comments are mare than welcome.",
    "created_at": "2011-02-17T18:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61892",
    "user": "jpflori"
}
```

I've put a first (very) rough version of a patch to refactor the different interfaces:

* It split the previous Expect classes in Interface classes (without pexpect stuff, did not find a better name) and Expect classes (inheriting from the previous ones + pexpect stuff)
* MaximaAbstract classes depends on Interface classes
* MaximaLib on MaximaAbstract
* Maxima (classic) on MaximaAbstract and Expect

It kind of works easily thanks to the current Method Resolution Order used by the version of Python in Sage but it obviously introduces a lot of new failures in addition to the one above.

The patch must be applied after the "_p2" patches (and ecl_iter).

It is quite big, touches a lot of files, and should be splitted in at least two parts (split Expect; refactor).

It is absolutely not considered as finished (very far from it) and I did not test it (apart from trivial things like integrate(x)), it is mainly to get some feedback on the choices I made, so any comments are mare than welcome.



---

archive/issue_comments_061893.json:
```json
{
    "body": "You should probably be aware of #10766 (an update of ECL), which has positive review and #10773 (an update of Maxima) which also has positive review. \n\nDave",
    "created_at": "2011-02-17T18:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61893",
    "user": "drkirkby"
}
```

You should probably be aware of #10766 (an update of ECL), which has positive review and #10773 (an update of Maxima) which also has positive review. 

Dave



---

archive/issue_comments_061894.json:
```json
{
    "body": "Replying to [comment:65 drkirkby]:\n> You should probably be aware of #10766 (an update of ECL), which has positive review and #10773 (an update of Maxima) which also has positive review. \n\nIf you look at the descriptions of the `p2` patches, they all mention they depend on those new versions, though not by ticket number.  I think they are based on Maxima 5.23.1 it says, but probably that is not 100% necessary.",
    "created_at": "2011-02-17T18:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61894",
    "user": "@kcrisman"
}
```

Replying to [comment:65 drkirkby]:
> You should probably be aware of #10766 (an update of ECL), which has positive review and #10773 (an update of Maxima) which also has positive review. 

If you look at the descriptions of the `p2` patches, they all mention they depend on those new versions, though not by ticket number.  I think they are based on Maxima 5.23.1 it says, but probably that is not 100% necessary.



---

archive/issue_comments_061895.json:
```json
{
    "body": "Replying to [comment:64 jpflori]:\n> It kind of works easily thanks to the current Method Resolution Order used by the version of Python in Sage but it obviously introduces a lot of new failures in addition to the one above.\n\nPerhaps you can do a quick test if depending on multiple inheritance causes a huge slowdown in method resolution? (I guess that is the only major architectural change you're making). Since it's the *proper* thing to do even a small slowdown should be acceptable, but we wouldn't want to degrade too badly.\n\n> The patch must be applied after the \"_p2\" patches (and ecl_iter).\n\nI recommend that you first do the refactoring *without* fast-calculus. That basically takes maxima_lib out of the equation and means you'll be refactoring code that is known to be good (actually, a quick test seems to indicate that the pexpect maxima interface based on abstract_maxima already breaks doctests. I think that back in 4.1.* or whatever Robert's work was based on, they were fine, so there may be some changes that didn't properly get adapted for the _p2 patches).\n\nPerhaps open a separate ticket \"refactor maxima to multiply inherit from a new class maxima_abstract and pexpect\". It would reduce the number of complicating factors you'd be considering.\n\nWork here would basically remain exploratory until that ticket is finished. We can then rebase the work here to your new organization of maxima interfaces. I noticed that your changes to maxima_lib.py were minimal so at least for now, that should be easy.",
    "created_at": "2011-02-17T20:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61895",
    "user": "@nbruin"
}
```

Replying to [comment:64 jpflori]:
> It kind of works easily thanks to the current Method Resolution Order used by the version of Python in Sage but it obviously introduces a lot of new failures in addition to the one above.

Perhaps you can do a quick test if depending on multiple inheritance causes a huge slowdown in method resolution? (I guess that is the only major architectural change you're making). Since it's the *proper* thing to do even a small slowdown should be acceptable, but we wouldn't want to degrade too badly.

> The patch must be applied after the "_p2" patches (and ecl_iter).

I recommend that you first do the refactoring *without* fast-calculus. That basically takes maxima_lib out of the equation and means you'll be refactoring code that is known to be good (actually, a quick test seems to indicate that the pexpect maxima interface based on abstract_maxima already breaks doctests. I think that back in 4.1.* or whatever Robert's work was based on, they were fine, so there may be some changes that didn't properly get adapted for the _p2 patches).

Perhaps open a separate ticket "refactor maxima to multiply inherit from a new class maxima_abstract and pexpect". It would reduce the number of complicating factors you'd be considering.

Work here would basically remain exploratory until that ticket is finished. We can then rebase the work here to your new organization of maxima interfaces. I noticed that your changes to maxima_lib.py were minimal so at least for now, that should be easy.



---

archive/issue_comments_061896.json:
```json
{
    "body": "Ok I found the reason of the strange \"ceil\" function appearing.\n\nThat's because sr_to_max calls op_max=caar(maxima(expr).ecl()) and maxima(expr) can simplify the object change its structure, so the dictionary is wrongly built (we get \"ceil\" for \"+\").\n\nPutting op_max=maxima(op).ecl() seems functional.\n\nThe issue with (log(9)*x).simplify_log('all') is similar.\n\nMaxima transforms log(9!^x) back to log(9)*x before it is passed to string function in max_to_string:\n\n\n```\n(%i8) logexpand:false$\n\n(%i9) string(log(9^x));\n\n(%o9) \"log(9)*x\"\n\n(%i10) log(9^x);\n\n(%o10) log(9)*x\n(%i11) simp:false$\n\n(%i12) log(9^x);\n\n(%o12) log(9^x)\n(%i13) string(log(9^x));\n\n(%o13) \"log(9^x)\"\n\n```\n\nAs far as the classic pexpect interface is concerned, a lot of problems are solved if one changes  \"back\" return result to return result._sage_() in sage.symbolic.integration.external\n\nIt used to be return result.sage() but some routines in the fastcalculus patch for maxlib return symbolic object which do not have such a method but one with underscores.\n\nI'll post updated patches when they are in a better shape.",
    "created_at": "2011-02-18T16:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61896",
    "user": "jpflori"
}
```

Ok I found the reason of the strange "ceil" function appearing.

That's because sr_to_max calls op_max=caar(maxima(expr).ecl()) and maxima(expr) can simplify the object change its structure, so the dictionary is wrongly built (we get "ceil" for "+").

Putting op_max=maxima(op).ecl() seems functional.

The issue with (log(9)*x).simplify_log('all') is similar.

Maxima transforms log(9!^x) back to log(9)*x before it is passed to string function in max_to_string:


```
(%i8) logexpand:false$

(%i9) string(log(9^x));

(%o9) "log(9)*x"

(%i10) log(9^x);

(%o10) log(9)*x
(%i11) simp:false$

(%i12) log(9^x);

(%o12) log(9^x)
(%i13) string(log(9^x));

(%o13) "log(9^x)"

```

As far as the classic pexpect interface is concerned, a lot of problems are solved if one changes  "back" return result to return result._sage_() in sage.symbolic.integration.external

It used to be return result.sage() but some routines in the fastcalculus patch for maxlib return symbolic object which do not have such a method but one with underscores.

I'll post updated patches when they are in a better shape.



---

archive/issue_comments_061897.json:
```json
{
    "body": "First of all, great sleuthing! Excellent progress.\n\n> Ok I found the reason of the strange \"ceil\" function appearing.\n> \n> That's because sr_to_max calls op_max=caar(maxima(expr).ecl()) and maxima(expr) can simplify the object change its structure, so the dictionary is wrongly built (we get \"ceil\" for \"+\").\n> \n> Putting op_max=maxima(op).ecl() seems functional.\n\nI think I tried your alternative before, but that could also lead to parse errors (feeding just the operator to maxima may not lead to a syntactical expression on the other side). Note that the \"learning\" via the strings-based interface is only a hack to profit from work done there (and to stay compatible with it). Most of this knowledge on how to map SR.operator() objects to maxima and back, is hand-coded somewhere in sage anyway. If we could get that info once and for all and transcribe it to the sr_to_max dicts, we wouldn't need this hack anymore.\n\n> The issue with (log(9)*x).simplify_log('all') is similar.\n> \n> Maxima transforms log(9!^x) back to log(9)*x before it is passed to string function in max_to_string:\n\nInteresting! So this problem would disappear again if simplify_log were wrapped similarly to sr_integral etc., where sr_to_max and max_to_sr are used as much as possible.",
    "created_at": "2011-02-18T17:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61897",
    "user": "@nbruin"
}
```

First of all, great sleuthing! Excellent progress.

> Ok I found the reason of the strange "ceil" function appearing.
> 
> That's because sr_to_max calls op_max=caar(maxima(expr).ecl()) and maxima(expr) can simplify the object change its structure, so the dictionary is wrongly built (we get "ceil" for "+").
> 
> Putting op_max=maxima(op).ecl() seems functional.

I think I tried your alternative before, but that could also lead to parse errors (feeding just the operator to maxima may not lead to a syntactical expression on the other side). Note that the "learning" via the strings-based interface is only a hack to profit from work done there (and to stay compatible with it). Most of this knowledge on how to map SR.operator() objects to maxima and back, is hand-coded somewhere in sage anyway. If we could get that info once and for all and transcribe it to the sr_to_max dicts, we wouldn't need this hack anymore.

> The issue with (log(9)*x).simplify_log('all') is similar.
> 
> Maxima transforms log(9!^x) back to log(9)*x before it is passed to string function in max_to_string:

Interesting! So this problem would disappear again if simplify_log were wrapped similarly to sr_integral etc., where sr_to_max and max_to_sr are used as much as possible.



---

archive/issue_comments_061898.json:
```json
{
    "body": "Replying to [comment:68 jpflori]:\n> Maxima transforms log(9!^x) back to log(9)*x before it is passed to string function in max_to_string:\n\nThanks for locating the error! It's simply that maxima's `string` (in lisp `$STRING`) does too much work, meaning that max_to_string involves a new call to MEVAL. The definition is in `suprv1.lisp` and points to what to do differently. Two definitions in maxima_lib.py need adjusting:\n\n```\nmaxprint=EclObject(\"(defun mstring-for-sage (form) (coerce (mstring form) 'string))\").eval()\n\ndef max_to_string(s):\n     return maxprint(s).python()[1:-1]\n```\n\nWARNING: the routine maxprint is lisp, not maxima and is presently not run under maxima-eval's control, so maxima errors will be poorly reported. If converting maxima expressions to strings can trigger errors we need an adjusted version of maxima-eval that calls EVAL rather than MEVAL on the parameter (to execute lisp code under our replacement of maxima's toplevel)",
    "created_at": "2011-02-18T21:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61898",
    "user": "@nbruin"
}
```

Replying to [comment:68 jpflori]:
> Maxima transforms log(9!^x) back to log(9)*x before it is passed to string function in max_to_string:

Thanks for locating the error! It's simply that maxima's `string` (in lisp `$STRING`) does too much work, meaning that max_to_string involves a new call to MEVAL. The definition is in `suprv1.lisp` and points to what to do differently. Two definitions in maxima_lib.py need adjusting:

```
maxprint=EclObject("(defun mstring-for-sage (form) (coerce (mstring form) 'string))").eval()

def max_to_string(s):
     return maxprint(s).python()[1:-1]
```

WARNING: the routine maxprint is lisp, not maxima and is presently not run under maxima-eval's control, so maxima errors will be poorly reported. If converting maxima expressions to strings can trigger errors we need an adjusted version of maxima-eval that calls EVAL rather than MEVAL on the parameter (to execute lisp code under our replacement of maxima's toplevel)



---

archive/issue_comments_061899.json:
```json
{
    "body": "Replying to [comment:68 jpflori]:\n> That's because sr_to_max calls op_max=caar(maxima(expr).ecl()) and maxima(expr) can simplify the object change its structure, so the dictionary is wrongly built (we get \"ceil\" for \"+\").\n> \n> Putting op_max=maxima(op).ecl() seems functional.\n\nA little digging gives us a way to access *just* the maxima reader, without the extra evaluation:\n\n```\nmymread=ecl_eval(\"\"\"\n(defun my-mread (cmd)\n  (caddr (mread (make-string-input-stream cmd))))\n\"\"\")\n\ndef parsemaxstring(l):\n  return mymread('\"%s;\"'%l)\n```\n\nExamples:\n\n```\nsage: parsemaxstring(\"integral(x^2,x)\")\n<ECL: (($INTEGRAL) ((MEXPT) $X 2) $X)>\nsage: parsemaxstring(\"ceiling(x^2+floor(x))\")\n<ECL: (($CEILING) ((MPLUS) ((MEXPT) $X 2) (($FLOOR) $X)))>\nsage: parsemaxstring(\"log(9^x)\")\n<ECL: ((%LOG) ((MEXPT) 9 $X))>\n```\n\nThe effect is about the same as\n\n```\nsage: EclObject(\"#$ceiling(x^2+floor(x))$\").cdr().car().cdr().car()\n<ECL: (($CEILING) ((MPLUS) ((MEXPT) $X 2) (($FLOOR) $X)))>\n```\n",
    "created_at": "2011-02-19T04:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61899",
    "user": "@nbruin"
}
```

Replying to [comment:68 jpflori]:
> That's because sr_to_max calls op_max=caar(maxima(expr).ecl()) and maxima(expr) can simplify the object change its structure, so the dictionary is wrongly built (we get "ceil" for "+").
> 
> Putting op_max=maxima(op).ecl() seems functional.

A little digging gives us a way to access *just* the maxima reader, without the extra evaluation:

```
mymread=ecl_eval("""
(defun my-mread (cmd)
  (caddr (mread (make-string-input-stream cmd))))
""")

def parsemaxstring(l):
  return mymread('"%s;"'%l)
```

Examples:

```
sage: parsemaxstring("integral(x^2,x)")
<ECL: (($INTEGRAL) ((MEXPT) $X 2) $X)>
sage: parsemaxstring("ceiling(x^2+floor(x))")
<ECL: (($CEILING) ((MPLUS) ((MEXPT) $X 2) (($FLOOR) $X)))>
sage: parsemaxstring("log(9^x)")
<ECL: ((%LOG) ((MEXPT) 9 $X))>
```

The effect is about the same as

```
sage: EclObject("#$ceiling(x^2+floor(x))$").cdr().car().cdr().car()
<ECL: (($CEILING) ((MPLUS) ((MEXPT) $X 2) (($FLOOR) $X)))>
```




---

archive/issue_comments_061900.json:
```json
{
    "body": "With the new version of the patch only the following errors persist with maxima as a lib:\n\n* unpickling problems,\n* some timeouts (sage.interfaces.gap3).\n\nAnd trivial to fix:\n\n* error reporting,\n* floating point precision.\n\nWith the classical maxima, I only get the first set of errors.\n\nThe translation of the derivatives seems better than before and the errors in desolver disappeared.",
    "created_at": "2011-02-20T20:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61900",
    "user": "jpflori"
}
```

With the new version of the patch only the following errors persist with maxima as a lib:

* unpickling problems,
* some timeouts (sage.interfaces.gap3).

And trivial to fix:

* error reporting,
* floating point precision.

With the classical maxima, I only get the first set of errors.

The translation of the derivatives seems better than before and the errors in desolver disappeared.



---

archive/issue_comments_061901.json:
```json
{
    "body": "Version 0.2",
    "created_at": "2011-02-20T20:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61901",
    "user": "jpflori"
}
```

Version 0.2



---

archive/issue_comments_061902.json:
```json
{
    "body": "Attachment [trac_7377-split_and_refactor.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-split_and_refactor.patch) by @nbruin created at 2011-02-21 03:55:09\n\nGreat work! The patches don't apply on 4.6.1 so I can't test them at the moment. Reading through the patch:\n* Line 74\n\n```\n  (string-trim '(#\\Newline) (with-output-to-string (*standard-output*)\n      (terpri)\n```\n\nIf you're going to trim the newlines, don't bother with terpri. It just inserts a newline. Perhaps if you delete the terpri the trimming isn't necessary (I put it there because previously, the \"ask\" error messages had a newline before the question)\n* derivatives: If you want FDerivativeOperator handled by special_sage_to_max you'll need to change a bit more than just the API of the functions in that dictionary (for that, you can just put \"op\" as the first parameter and not use it in most cases)\n\nOne possibility is to index special_sage_to_max by type(op) rather than op. Then it makes a lot more sense to pass op as a parameter too (because currently, the op would be a constant for any entry in special_sage_to_max).\n\n* the line:\n\n```\n[deriv_max.extend([sr_to_max(args[i]), EclObject(params.count(i))]) for i in set(params)]\n```\n\nleads to an algorithm that is quadratic in the number of variables, but it should be (soft) linear. It should be interesting to design an example where this matters ...)",
    "created_at": "2011-02-21T03:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61902",
    "user": "@nbruin"
}
```

Attachment [trac_7377-split_and_refactor.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-split_and_refactor.patch) by @nbruin created at 2011-02-21 03:55:09

Great work! The patches don't apply on 4.6.1 so I can't test them at the moment. Reading through the patch:
* Line 74

```
  (string-trim '(#\Newline) (with-output-to-string (*standard-output*)
      (terpri)
```

If you're going to trim the newlines, don't bother with terpri. It just inserts a newline. Perhaps if you delete the terpri the trimming isn't necessary (I put it there because previously, the "ask" error messages had a newline before the question)
* derivatives: If you want FDerivativeOperator handled by special_sage_to_max you'll need to change a bit more than just the API of the functions in that dictionary (for that, you can just put "op" as the first parameter and not use it in most cases)

One possibility is to index special_sage_to_max by type(op) rather than op. Then it makes a lot more sense to pass op as a parameter too (because currently, the op would be a constant for any entry in special_sage_to_max).

* the line:

```
[deriv_max.extend([sr_to_max(args[i]), EclObject(params.count(i))]) for i in set(params)]
```

leads to an algorithm that is quadratic in the number of variables, but it should be (soft) linear. It should be interesting to design an example where this matters ...)



---

archive/issue_comments_061903.json:
```json
{
    "body": "There is currently a problem with ecl and signals.\n\nWith the current initialization, interrupting a computation does not work well.\n\nYou can try the example of sage.interfaces.maxima with maxima as a lib:\n\n\n```\nsage: from sage.interfaces.maxima_lib import maxima_lib as maxlib\nsage: maxlib('sum(1/x^2, x, 1, 10000)') # or bigger to be convinced\n\n```\n\nand hit Ctrl+C immediately.",
    "created_at": "2011-02-21T09:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61903",
    "user": "jpflori"
}
```

There is currently a problem with ecl and signals.

With the current initialization, interrupting a computation does not work well.

You can try the example of sage.interfaces.maxima with maxima as a lib:


```
sage: from sage.interfaces.maxima_lib import maxima_lib as maxlib
sage: maxlib('sum(1/x^2, x, 1, 10000)') # or bigger to be convinced

```

and hit Ctrl+C immediately.



---

archive/issue_comments_061904.json:
```json
{
    "body": "Replying to [comment:74 jpflori]:\n> There is currently a problem with ecl and signals.\nYes, sage.lib.ecl simply does not enable them. \n\nIt looks like ECL development has carefully looked at how to best handle signals. See http://ecls.sourceforge.net/new-manual/ch22.html . But it also looks like a non-trivial task to adapt Sage's signal handling to play nice with the way ECL expects it. The ECL_OPT_SIGNAL_HANDLING_THREAD way sounds patently incompatible with sage.\n\nYou could of course try to just insert the appropriate sig_on() and sig_off() around the calls to ecl's \"eval\" and hope for the best. This must be a problem that has arisen for other libraries, such as pari, singular, ginac, gap etc.",
    "created_at": "2011-02-21T09:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61904",
    "user": "@nbruin"
}
```

Replying to [comment:74 jpflori]:
> There is currently a problem with ecl and signals.
Yes, sage.lib.ecl simply does not enable them. 

It looks like ECL development has carefully looked at how to best handle signals. See http://ecls.sourceforge.net/new-manual/ch22.html . But it also looks like a non-trivial task to adapt Sage's signal handling to play nice with the way ECL expects it. The ECL_OPT_SIGNAL_HANDLING_THREAD way sounds patently incompatible with sage.

You could of course try to just insert the appropriate sig_on() and sig_off() around the calls to ecl's "eval" and hope for the best. This must be a problem that has arisen for other libraries, such as pari, singular, ginac, gap etc.



---

archive/issue_comments_061905.json:
```json
{
    "body": "Replying to [comment:74 jpflori]:\n> There is currently a problem with ecl and signals.\nThis is now #10818 . It has a rudimentary patch which seems to work, but I'm confident it can break badly. Also note that leaving ECL in a consistent state does not mean that Maxima is also left in a consistent state.",
    "created_at": "2011-02-21T22:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61905",
    "user": "@nbruin"
}
```

Replying to [comment:74 jpflori]:
> There is currently a problem with ecl and signals.
This is now #10818 . It has a rudimentary patch which seems to work, but I'm confident it can break badly. Also note that leaving ECL in a consistent state does not mean that Maxima is also left in a consistent state.



---

archive/issue_comments_061906.json:
```json
{
    "body": "Replying to [comment:76 nbruin]:\n> This is now #10818\nThis has now something that should be fairly robust.",
    "created_at": "2011-02-25T22:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61906",
    "user": "@nbruin"
}
```

Replying to [comment:76 nbruin]:
> This is now #10818
This has now something that should be fairly robust.



---

archive/issue_comments_061907.json:
```json
{
    "body": "I have tested the new packages with 4.6.2.alpha4 and I am finding largely agreement with JP. As a baseline, I have used ECL and Maxima from #10766 and #10773 respectively, with applied patches:\n\n```\ntrac_10766-fix_doctest.patch\ntrac_10766-fix_symbolic_integration_integral.patch\ntrac_10773-fix_maxima_version.patch\ntrac_10743-ecl-iter_p1.patch\nhandlerswap.p2.patch #this is from ticket #10818\n```\n\nAll doctests are OK there. When I further apply\n\n```\ntrac_7377-abstract-maxima_p2.patch\ntrac_7377-maximalib_p2.patch\ntrac_7377-fastcalculus_p2.patch\ntrac_7377-better-ask-error_p2.patch\ntrac_7377-split_and_refactor.patch\n```\n\nI am finding doctest failures that are just due to different errors reporting and floating point, so these can be fixed by changing the doctests:\n\n```\nsage -t  devel/sage-main/sage/calculus/functional.py # 1 doctests failed\nsage -t  devel/sage-main/sage/interfaces/maxima.py # 2 doctests failed\nsage -t  devel/sage-main/sage/symbolic/assumptions.py # 2 doctests failed\nsage -t  devel/sage-main/sage/symbolic/integration/integral.py # 5 doctests failed\n```\n\nFurthermore,\n\n```\nsage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed\n```\n\nusually fails. Note that we are now initializing ECL upon startup, so we're really doing more work. Should we be lazy with this? This just means that the calculus maxima instance would have to be made lazy (i.e., set to a function that initializes maxima and then rebinds sage.calculus.maxima)\n\n```\nsage -t  devel/sage-main/sage/structure/sage_object.pyx # 1 doctests failed\n```\n\nneeds a pickling expert\n\n```\nsage -t  devel/sage-main/sage/interfaces/gap3.py # Time out\n```\n\nthis is a real error that was probably introduced by `split_and_refactor`. The timeout is caused by an infinite recursion upon exit (run with -verbose) and probably has to do with the fact that\n\n```\nsage: gap3(\"1+2\")\n```\n\nnow fails differently. It seems that a \"name()\" attribute is missing. If you now try to \"quit()\", an infinite loop on some Exception resolution is triggered, but I expect the damage happened in the line above. gap3 is optional, by the way, but the error apparently already happens with tests that check the absence of gap3.\n\nImpressive progress indeed!",
    "created_at": "2011-02-27T02:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61907",
    "user": "@nbruin"
}
```

I have tested the new packages with 4.6.2.alpha4 and I am finding largely agreement with JP. As a baseline, I have used ECL and Maxima from #10766 and #10773 respectively, with applied patches:

```
trac_10766-fix_doctest.patch
trac_10766-fix_symbolic_integration_integral.patch
trac_10773-fix_maxima_version.patch
trac_10743-ecl-iter_p1.patch
handlerswap.p2.patch #this is from ticket #10818
```

All doctests are OK there. When I further apply

```
trac_7377-abstract-maxima_p2.patch
trac_7377-maximalib_p2.patch
trac_7377-fastcalculus_p2.patch
trac_7377-better-ask-error_p2.patch
trac_7377-split_and_refactor.patch
```

I am finding doctest failures that are just due to different errors reporting and floating point, so these can be fixed by changing the doctests:

```
sage -t  devel/sage-main/sage/calculus/functional.py # 1 doctests failed
sage -t  devel/sage-main/sage/interfaces/maxima.py # 2 doctests failed
sage -t  devel/sage-main/sage/symbolic/assumptions.py # 2 doctests failed
sage -t  devel/sage-main/sage/symbolic/integration/integral.py # 5 doctests failed
```

Furthermore,

```
sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed
```

usually fails. Note that we are now initializing ECL upon startup, so we're really doing more work. Should we be lazy with this? This just means that the calculus maxima instance would have to be made lazy (i.e., set to a function that initializes maxima and then rebinds sage.calculus.maxima)

```
sage -t  devel/sage-main/sage/structure/sage_object.pyx # 1 doctests failed
```

needs a pickling expert

```
sage -t  devel/sage-main/sage/interfaces/gap3.py # Time out
```

this is a real error that was probably introduced by `split_and_refactor`. The timeout is caused by an infinite recursion upon exit (run with -verbose) and probably has to do with the fact that

```
sage: gap3("1+2")
```

now fails differently. It seems that a "name()" attribute is missing. If you now try to "quit()", an infinite loop on some Exception resolution is triggered, but I expect the damage happened in the line above. gap3 is optional, by the way, but the error apparently already happens with tests that check the absence of gap3.

Impressive progress indeed!



---

archive/issue_comments_061908.json:
```json
{
    "body": "Improves startup time by lazily loading maxima_lib in calculus",
    "created_at": "2011-02-27T03:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61908",
    "user": "@nbruin"
}
```

Improves startup time by lazily loading maxima_lib in calculus



---

archive/issue_comments_061909.json:
```json
{
    "body": "Attachment [trac_7377-lazy-maxlib.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-lazy-maxlib.patch) by jpflori created at 2011-02-27 11:39:40\n\nReplying to [comment:78 nbruin]:\n\n> ` sage -t  devel/sage-main/sage/interfaces/gap3.py # Time out ` this is a real error that was probably introduced by `split_and_refactor`. The timeout is caused by an infinite recursion upon exit (run with -verbose) and probably has to do with the fact that ` sage: gap3(\"1+2\") ` now fails differently. It seems that a \"name()\" attribute is missing. If you now try to \"quit()\", an infinite loop on some Exception resolution is triggered, but I expect the damage happened in the line above. gap3 is optional, by the way, but the error apparently already happens with tests that check the absence of gap3. Impressive progress indeed!\n\nThanks for that one, I do not have gap3 installed and get the time out, but did not bother. I'll have a look at it.",
    "created_at": "2011-02-27T11:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61909",
    "user": "jpflori"
}
```

Attachment [trac_7377-lazy-maxlib.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-lazy-maxlib.patch) by jpflori created at 2011-02-27 11:39:40

Replying to [comment:78 nbruin]:

> ` sage -t  devel/sage-main/sage/interfaces/gap3.py # Time out ` this is a real error that was probably introduced by `split_and_refactor`. The timeout is caused by an infinite recursion upon exit (run with -verbose) and probably has to do with the fact that ` sage: gap3("1+2") ` now fails differently. It seems that a "name()" attribute is missing. If you now try to "quit()", an infinite loop on some Exception resolution is triggered, but I expect the damage happened in the line above. gap3 is optional, by the way, but the error apparently already happens with tests that check the absence of gap3. Impressive progress indeed!

Thanks for that one, I do not have gap3 installed and get the time out, but did not bother. I'll have a look at it.



---

archive/issue_comments_061910.json:
```json
{
    "body": "Attachment [trac_7377-interface-namefix.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-interface-namefix.patch) by @nbruin created at 2011-02-27 19:09:05\n\nFixes gap3 timeout problem",
    "created_at": "2011-02-27T19:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61910",
    "user": "@nbruin"
}
```

Attachment [trac_7377-interface-namefix.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-interface-namefix.patch) by @nbruin created at 2011-02-27 19:09:05

Fixes gap3 timeout problem



---

archive/issue_comments_061911.json:
```json
{
    "body": "The benefits of unexpected snow ... It looks like the gap3 problem was due to some unqualified references to `name()` in sage.interfaces.interface, where it should be `self.name()`. Patch attached, but since this was a rather low-brained search-and-replace, JP should check I didn't miss any/didn't change any erroneously.\n\nThe one pickling problem is the only issue left!",
    "created_at": "2011-02-27T19:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61911",
    "user": "@nbruin"
}
```

The benefits of unexpected snow ... It looks like the gap3 problem was due to some unqualified references to `name()` in sage.interfaces.interface, where it should be `self.name()`. Patch attached, but since this was a rather low-brained search-and-replace, JP should check I didn't miss any/didn't change any erroneously.

The one pickling problem is the only issue left!



---

archive/issue_comments_061912.json:
```json
{
    "body": "Some forensics on:\n\n```\nsage -t  devel/sage-main/sage/structure/sage_object.pyx\n```\n\nThe error occurs on\n`_class__sage_interfaces_maxima_MaximaFunction__.sobj` in the pickle jar, coming from the doctest (slightly adapted):\n\n```\nsage: f=maxima.function('x,y','sin(x+y)')\nsage: save(f,\"newpickle.sobj\")\nsage: load(\"newpickle.sobj\")==f\nTrue\n```\n\nThe incompatibility seems to come from a rearranging of the abstract_maxima interface etc.\nTo pin down version information:\n\n```\n$ ls -l _class__sage_interfaces_maxima_MaximaFunction__.*\n-rw-r--r-- 1 nbruin nbruin  96 2009-03-10 13:04 _class__sage_interfaces_maxima_MaximaFunction__.sobj\n-rw-r--r-- 1 nbruin nbruin 130 2009-03-10 13:04 _class__sage_interfaces_maxima_MaximaFunction__.txt\n$ cat _class__sage_interfaces_maxima_MaximaFunction__.txt\ntype(obj) = <class 'sage.interfaces.maxima.MaximaFunction'>\nversion = 3.4.rc1\nobj =\n'                                    sage270'\n```\n\nLoading this pickle into a new version yields:\n\n```\nsage: load(\"/home/nbruin/_class__sage_interfaces_maxima_MaximaFunction__.sobj\");\nAttributeError: 'module' object has no attribute 'reduce_load_Maxima_function'\n```\n\nOn the other hand, loading the new pickle into an old version (4.3.4):\n\n```\nsage: load(\"newpickle.sobj\");\nImportError: No module named maxima_abstract\n```\n\nSo this seems to be not so much an error but more a non-compatible change. I am sure these have happened before elsewhere. I'd be happy to just accept the fact that these pickles aren't portable across these versions, but if someone has an example we might be able to put the hooks in to preserve backwards compatibility (really, no-one should have a reason to pickle maxima functions from sage).",
    "created_at": "2011-03-01T09:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61912",
    "user": "@nbruin"
}
```

Some forensics on:

```
sage -t  devel/sage-main/sage/structure/sage_object.pyx
```

The error occurs on
`_class__sage_interfaces_maxima_MaximaFunction__.sobj` in the pickle jar, coming from the doctest (slightly adapted):

```
sage: f=maxima.function('x,y','sin(x+y)')
sage: save(f,"newpickle.sobj")
sage: load("newpickle.sobj")==f
True
```

The incompatibility seems to come from a rearranging of the abstract_maxima interface etc.
To pin down version information:

```
$ ls -l _class__sage_interfaces_maxima_MaximaFunction__.*
-rw-r--r-- 1 nbruin nbruin  96 2009-03-10 13:04 _class__sage_interfaces_maxima_MaximaFunction__.sobj
-rw-r--r-- 1 nbruin nbruin 130 2009-03-10 13:04 _class__sage_interfaces_maxima_MaximaFunction__.txt
$ cat _class__sage_interfaces_maxima_MaximaFunction__.txt
type(obj) = <class 'sage.interfaces.maxima.MaximaFunction'>
version = 3.4.rc1
obj =
'                                    sage270'
```

Loading this pickle into a new version yields:

```
sage: load("/home/nbruin/_class__sage_interfaces_maxima_MaximaFunction__.sobj");
AttributeError: 'module' object has no attribute 'reduce_load_Maxima_function'
```

On the other hand, loading the new pickle into an old version (4.3.4):

```
sage: load("newpickle.sobj");
ImportError: No module named maxima_abstract
```

So this seems to be not so much an error but more a non-compatible change. I am sure these have happened before elsewhere. I'd be happy to just accept the fact that these pickles aren't portable across these versions, but if someone has an example we might be able to put the hooks in to preserve backwards compatibility (really, no-one should have a reason to pickle maxima functions from sage).



---

archive/issue_comments_061913.json:
```json
{
    "body": "Attachment [trac_7377-pickle-fix.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-pickle-fix.patch) by @nbruin created at 2011-03-01 09:18:55\n\nFixes MaximaFunction pickle issue",
    "created_at": "2011-03-01T09:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61913",
    "user": "@nbruin"
}
```

Attachment [trac_7377-pickle-fix.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-pickle-fix.patch) by @nbruin created at 2011-03-01 09:18:55

Fixes MaximaFunction pickle issue



---

archive/issue_comments_061914.json:
```json
{
    "body": "Replying to [nbruin](http://trac.sagemath.org/sage_trac/search/opensearch?q=comment%3A80):\n\n> The benefits of unexpected snow ... It looks like the gap3 problem was due to some unqualified references to `name()` in sage.interfaces.interface, where it should be `self.name()`.  Patch attached, but since this was a rather low-brained  search-and-replace, JP should check I didn't miss any/didn't change any  erroneously. The one pickling problem is the only issue left!\n\nThanks for the fix, that was my mistake: I changed some references to self.!__name to calls to a name() function which was much more clear with the new class hierarchy.\n\nI confirm that your patch fixes the gap3 timeout (without gap3 installed).\n\nI'll post an updated patch \"split_and_refactor\" including your fixes and some changes so that the name of \"MaximaLib\" is now \"_maxima_lib_\" (even if most of the time, if not always, the related objects are treated like maxima ones for now).\n\nAs far as the pickling problem is concerned, I was aware that it was \"just\" caused by the changes in class hierarchy (and names).\n\nI search a little bit through Google (!http://ask.sagemath.org/question/123/what-is-the-standard-pickle-jar-for-and-how-do-i), and I think the Sage general policy is to be able to pick up old pickles (quite lgical), so I guess that we should try to include a workaround.\n\n...Ok you've just posted a fix for that one too, so I'll include it as well.",
    "created_at": "2011-03-01T09:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61914",
    "user": "jpflori"
}
```

Replying to [nbruin](http://trac.sagemath.org/sage_trac/search/opensearch?q=comment%3A80):

> The benefits of unexpected snow ... It looks like the gap3 problem was due to some unqualified references to `name()` in sage.interfaces.interface, where it should be `self.name()`.  Patch attached, but since this was a rather low-brained  search-and-replace, JP should check I didn't miss any/didn't change any  erroneously. The one pickling problem is the only issue left!

Thanks for the fix, that was my mistake: I changed some references to self.!__name to calls to a name() function which was much more clear with the new class hierarchy.

I confirm that your patch fixes the gap3 timeout (without gap3 installed).

I'll post an updated patch "split_and_refactor" including your fixes and some changes so that the name of "MaximaLib" is now "_maxima_lib_" (even if most of the time, if not always, the related objects are treated like maxima ones for now).

As far as the pickling problem is concerned, I was aware that it was "just" caused by the changes in class hierarchy (and names).

I search a little bit through Google (!http://ask.sagemath.org/question/123/what-is-the-standard-pickle-jar-for-and-how-do-i), and I think the Sage general policy is to be able to pick up old pickles (quite lgical), so I guess that we should try to include a workaround.

...Ok you've just posted a fix for that one too, so I'll include it as well.



---

archive/issue_comments_061915.json:
```json
{
    "body": "That sounds great. Just to be picky could the split_and_refactor patch be consolidated? By that I mean that the patchset patch some files like sage/interfaces/expect.py and then patch over that patch. It makes things fairly difficult to follow from my point of view.",
    "created_at": "2011-03-01T09:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61915",
    "user": "@kiwifb"
}
```

That sounds great. Just to be picky could the split_and_refactor patch be consolidated? By that I mean that the patchset patch some files like sage/interfaces/expect.py and then patch over that patch. It makes things fairly difficult to follow from my point of view.



---

archive/issue_comments_061916.json:
```json
{
    "body": "I'm currently running \"make ptestlong\" to check for errors we could have missed.\n\nAs soon as it is finished (say in a couple of hours), I'll post a new version of \"split_and_refactor\" including the following patches:\n\n\n```\ntrac_7377-split_and_refactor.patch\ntrac_7377-interface-namefix.patch\ntrac_7377-pickle-fix.patch\n\n```\n\nAnd a minor change I made inbetween which is in none of these patches (setting the \"name\" of maxima lib to \"_maxima_lib_\" rather than \"_maxima_\").\n\nIs that what you wanted (there will still be successive patches applied to maxima* files... however) ?",
    "created_at": "2011-03-01T09:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61916",
    "user": "jpflori"
}
```

I'm currently running "make ptestlong" to check for errors we could have missed.

As soon as it is finished (say in a couple of hours), I'll post a new version of "split_and_refactor" including the following patches:


```
trac_7377-split_and_refactor.patch
trac_7377-interface-namefix.patch
trac_7377-pickle-fix.patch

```

And a minor change I made inbetween which is in none of these patches (setting the "name" of maxima lib to "_maxima_lib_" rather than "_maxima_").

Is that what you wanted (there will still be successive patches applied to maxima* files... however) ?



---

archive/issue_comments_061917.json:
```json
{
    "body": "That's not what I meant Jean-Pierre. The current split_and_refactor patch starts with:\n\n```\ndiff -r a928dca2950b -r b766df9c3439 sage/interfaces/expect.py\n--- a/sage/interfaces/expect.py\tFri Feb 04 14:19:57 2011 -0800\n+++ b/sage/interfaces/expect.py\tMon Feb 14 14:06:15 2011 +0100\n@@ -42,6 +42,8 @@\n import time\n```\n\nand some patching is done to that file. Then later in the same patch file file we have\n\n```\n from mupad import mupad, mupad_console, Mupad  # NOT functional yet\ndiff -r b766df9c3439 -r fba59ed64da6 sage/interfaces/expect.py\n--- a/sage/interfaces/expect.py\tMon Feb 14 14:06:15 2011 +0100\n+++ b/sage/interfaces/expect.py\tWed Feb 16 16:38:39 2011 +0100\n@@ -489,12 +489,6 @@\n         except Exception, msg:\n```\n\nWhich is applied on top of the previous one. sage/interfaces/maxima_lib.py\nis also in that case and I am fairly sure there is a third one like that.\n\nI am guessing the first set is the \"split\" part and the second \"refactor\". In short I would prefer if there was only one instance of patching these files rather than two in succession in the same patch. But as I said that's because I am being picky.\nMercurial seems to cope fine with those, gnu patch doesn't really like them.",
    "created_at": "2011-03-01T10:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61917",
    "user": "@kiwifb"
}
```

That's not what I meant Jean-Pierre. The current split_and_refactor patch starts with:

```
diff -r a928dca2950b -r b766df9c3439 sage/interfaces/expect.py
--- a/sage/interfaces/expect.py	Fri Feb 04 14:19:57 2011 -0800
+++ b/sage/interfaces/expect.py	Mon Feb 14 14:06:15 2011 +0100
@@ -42,6 +42,8 @@
 import time
```

and some patching is done to that file. Then later in the same patch file file we have

```
 from mupad import mupad, mupad_console, Mupad  # NOT functional yet
diff -r b766df9c3439 -r fba59ed64da6 sage/interfaces/expect.py
--- a/sage/interfaces/expect.py	Mon Feb 14 14:06:15 2011 +0100
+++ b/sage/interfaces/expect.py	Wed Feb 16 16:38:39 2011 +0100
@@ -489,12 +489,6 @@
         except Exception, msg:
```

Which is applied on top of the previous one. sage/interfaces/maxima_lib.py
is also in that case and I am fairly sure there is a third one like that.

I am guessing the first set is the "split" part and the second "refactor". In short I would prefer if there was only one instance of patching these files rather than two in succession in the same patch. But as I said that's because I am being picky.
Mercurial seems to cope fine with those, gnu patch doesn't really like them.



---

archive/issue_comments_061918.json:
```json
{
    "body": "With the new patch that follows (and without lazy patch!), I only get the following failures due to error reporting and float precision:\n\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  -long -force_lib devel/sage/sage/interfaces/maxima.py # 2 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/calculus/functional.py # 1 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/symbolic/assumptions.py # 2 doctests failed\n\tsage -t  -long -force_lib devel/sage/sage/symbolic/integration/integral.py # 5 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 2633.7 seconds\n\n```\n\nThe update patch should be \"consolidated\" as asked (that was because of the command I used to generate it).\n\nSo the patches should be applied as follows:\n\n\n```\ntrac_7377-abstract-maxima_p2.patch\ntrac_7377-maximalib_p2.patch\ntrac_7377-fastcalculus_p2.patch\ntrac_7377-better-ask-error_p2.patch\ntrac_7377-split_and_refactor_p2.patch\n\n```\n\nApplying \"lazy\" patch breaks more test for me:\n\n* lazy objects are not callable so maxima(x) fails in sage.plot.plot3d.plot3d\n* exception raised in sage.plot.line",
    "created_at": "2011-03-01T11:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61918",
    "user": "jpflori"
}
```

With the new patch that follows (and without lazy patch!), I only get the following failures due to error reporting and float precision:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  -long -force_lib devel/sage/sage/interfaces/maxima.py # 2 doctests failed
	sage -t  -long -force_lib devel/sage/sage/calculus/functional.py # 1 doctests failed
	sage -t  -long -force_lib devel/sage/sage/symbolic/assumptions.py # 2 doctests failed
	sage -t  -long -force_lib devel/sage/sage/symbolic/integration/integral.py # 5 doctests failed
----------------------------------------------------------------------
Total time for all tests: 2633.7 seconds

```

The update patch should be "consolidated" as asked (that was because of the command I used to generate it).

So the patches should be applied as follows:


```
trac_7377-abstract-maxima_p2.patch
trac_7377-maximalib_p2.patch
trac_7377-fastcalculus_p2.patch
trac_7377-better-ask-error_p2.patch
trac_7377-split_and_refactor_p2.patch

```

Applying "lazy" patch breaks more test for me:

* lazy objects are not callable so maxima(x) fails in sage.plot.plot3d.plot3d
* exception raised in sage.plot.line



---

archive/issue_comments_061919.json:
```json
{
    "body": "Replying to [comment:87 jpflori]:\n> Applying \"lazy\" patch breaks more test for me:\n> \n>  * lazy objects are not callable so maxima(x) fails in sage.plot.plot3d.plot3d\n>  * exception raised in sage.plot.line\n\nSorry and thanks for catching. Both are solved by adding a \"__call__\" method to lazy:\n\n```\n    def __call__(self,*args,**kwargs):\n        import sage.interfaces.maxima_lib\n        sage.calculus.calculus.maxima = sage.interfaces.maxima_lib.maxima\n        return sage.calculus.calculus.maxima(*args,**kwargs)\n```\n\nbut in fact `sage.misc.lazy_import` does exactly what we need here. (See attached patch). I've ran doctests and I don't think the lazy causes additional fails.\n\nIncidentally, I'm getting a silly doctest failure\n\n```\nsage -t  \"devel/sage-main/sage/interfaces/maxima_abstract.py\"\n```\n\nfor the result of\n\n```\nsage: sorted(maxima._commands(verbose=False))\n```\n\nbut it looks like nothing has changed. Perhaps my build is corrupted.",
    "created_at": "2011-03-01T18:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61919",
    "user": "@nbruin"
}
```

Replying to [comment:87 jpflori]:
> Applying "lazy" patch breaks more test for me:
> 
>  * lazy objects are not callable so maxima(x) fails in sage.plot.plot3d.plot3d
>  * exception raised in sage.plot.line

Sorry and thanks for catching. Both are solved by adding a "__call__" method to lazy:

```
    def __call__(self,*args,**kwargs):
        import sage.interfaces.maxima_lib
        sage.calculus.calculus.maxima = sage.interfaces.maxima_lib.maxima
        return sage.calculus.calculus.maxima(*args,**kwargs)
```

but in fact `sage.misc.lazy_import` does exactly what we need here. (See attached patch). I've ran doctests and I don't think the lazy causes additional fails.

Incidentally, I'm getting a silly doctest failure

```
sage -t  "devel/sage-main/sage/interfaces/maxima_abstract.py"
```

for the result of

```
sage: sorted(maxima._commands(verbose=False))
```

but it looks like nothing has changed. Perhaps my build is corrupted.



---

archive/issue_comments_061920.json:
```json
{
    "body": "Attachment [trac_7377-lazy-maxlib.p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-lazy-maxlib.p2.patch) by @nbruin created at 2011-03-01 18:20:22\n\nLazy import of maxima in calculus using sage.misc.lazy_import",
    "created_at": "2011-03-01T18:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61920",
    "user": "@nbruin"
}
```

Attachment [trac_7377-lazy-maxlib.p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-lazy-maxlib.p2.patch) by @nbruin created at 2011-03-01 18:20:22

Lazy import of maxima in calculus using sage.misc.lazy_import



---

archive/issue_comments_061921.json:
```json
{
    "body": "Turns out the rounding errors weren't really that. Rather, max_to_sr preferred to return floats rather than RealDoubleElement, which are apparently the sage default type for float, and these print differently:\n\n```\nsage: var('x,y')\n(x, y)\nsage: assume(y>1)\nsage: M=sage.calculus.calculus.maxima\nsage: I1=SR(M(\"integrate(log(x^2+y^2),x,0.0001414,1.0)\"))\nsage: I2=integrate(log(x^2+y^2),x,0.0001414,1.0)\nsage: c1=I1.operands()[2].operands()[1].pyobject()\nsage: c2=I2.operands()[2].operands()[1].pyobject()\nsage: [c1,c2]\n[-0.0001414, -0.00014139999999999999]\nsage: [type(c1),type(c2)]\n[<type 'sage.rings.real_double.RealDoubleElement'>, <type 'float'>]\n```\n\nPatch attached. That means that the __only__ doctest failures now are due to the fact that \"maxima asks a question\" gets reported via a different error. Ready for review?",
    "created_at": "2011-03-01T21:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61921",
    "user": "@nbruin"
}
```

Turns out the rounding errors weren't really that. Rather, max_to_sr preferred to return floats rather than RealDoubleElement, which are apparently the sage default type for float, and these print differently:

```
sage: var('x,y')
(x, y)
sage: assume(y>1)
sage: M=sage.calculus.calculus.maxima
sage: I1=SR(M("integrate(log(x^2+y^2),x,0.0001414,1.0)"))
sage: I2=integrate(log(x^2+y^2),x,0.0001414,1.0)
sage: c1=I1.operands()[2].operands()[1].pyobject()
sage: c2=I2.operands()[2].operands()[1].pyobject()
sage: [c1,c2]
[-0.0001414, -0.00014139999999999999]
sage: [type(c1),type(c2)]
[<type 'sage.rings.real_double.RealDoubleElement'>, <type 'float'>]
```

Patch attached. That means that the __only__ doctest failures now are due to the fact that "maxima asks a question" gets reported via a different error. Ready for review?



---

archive/issue_comments_061922.json:
```json
{
    "body": "make max_to_sr return RealDoubleElement rather than float",
    "created_at": "2011-03-01T21:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61922",
    "user": "@nbruin"
}
```

make max_to_sr return RealDoubleElement rather than float



---

archive/issue_comments_061923.json:
```json
{
    "body": "Attachment [trac_7377-floatcast.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-floatcast.patch) by @nbruin created at 2011-03-01 21:52:22",
    "created_at": "2011-03-01T21:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61923",
    "user": "@nbruin"
}
```

Attachment [trac_7377-floatcast.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-floatcast.patch) by @nbruin created at 2011-03-01 21:52:22



---

archive/issue_comments_061924.json:
```json
{
    "body": "> Patch attached. That means that the __only__ doctest failures now are due to the fact that \"maxima asks a question\" gets reported via a different error. Ready for review?\n\nI'm sorry I haven't been able to test this lately.  Can you give an example?  As long as the end user still knows what to do (as in, `assume(x>0)` etc.) that should be fine.",
    "created_at": "2011-03-02T02:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61924",
    "user": "@kcrisman"
}
```

> Patch attached. That means that the __only__ doctest failures now are due to the fact that "maxima asks a question" gets reported via a different error. Ready for review?

I'm sorry I haven't been able to test this lately.  Can you give an example?  As long as the end user still knows what to do (as in, `assume(x>0)` etc.) that should be fine.



---

archive/issue_comments_061925.json:
```json
{
    "body": "Replying to [comment:91 kcrisman]:\n\n> > Patch attached. That means that the __only__ doctest failures now are due to the fact that \"maxima asks a question\" gets reported via a different error. Ready for review?\n> I'm sorry I haven't been able to test this lately.  Can you give an example?  As long as the end user still knows what to do (as in, `assume(x>0)` etc.) that should be fine.\n\nFor example:\n\n\n```\n    sage: integral(x^n,x)\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):\n    Is  n+1  zero or nonzero?\nGot:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: ECL says: Maxima asks: Is  n+1  zero or nonzero?\n\n```\n\nSo we do not parse the error message and are less explicit than before.\n\nThere are still some things I'd like to change before a potential review:\n\n1. Currently the interact function is broken for maxima_lib, it would be nicer to have it working than deleting it (and we should not leave something broken)\n2. I'll update \"split_and_refactor\" to get rid of superfluous terpri or string-trim as stated in comment 73\n3. Someone should check error stated in comment 88, I also got it sometimes, not sure why because that code was not so much touched\n4. I could merge \"floatcast\" with \"fast_calulculus\" or \"split_and_refactor\" so that we have less patches to apply and it is easier to test\n5. Parse error messages or just change the doctests and do bettor error reporting later.\n\nAfterwards (in other tickets ?):\n\n1. Add doctests to maxima_abstract and maxima_lib\n2. Avoid as much as possible string conversion in maxima_lib and take into account comment 73.",
    "created_at": "2011-03-02T09:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61925",
    "user": "jpflori"
}
```

Replying to [comment:91 kcrisman]:

> > Patch attached. That means that the __only__ doctest failures now are due to the fact that "maxima asks a question" gets reported via a different error. Ready for review?
> I'm sorry I haven't been able to test this lately.  Can you give an example?  As long as the end user still knows what to do (as in, `assume(x>0)` etc.) that should be fine.

For example:


```
    sage: integral(x^n,x)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):
    Is  n+1  zero or nonzero?
Got:
    Traceback (most recent call last):
    ...
    RuntimeError: ECL says: Maxima asks: Is  n+1  zero or nonzero?

```

So we do not parse the error message and are less explicit than before.

There are still some things I'd like to change before a potential review:

1. Currently the interact function is broken for maxima_lib, it would be nicer to have it working than deleting it (and we should not leave something broken)
2. I'll update "split_and_refactor" to get rid of superfluous terpri or string-trim as stated in comment 73
3. Someone should check error stated in comment 88, I also got it sometimes, not sure why because that code was not so much touched
4. I could merge "floatcast" with "fast_calulculus" or "split_and_refactor" so that we have less patches to apply and it is easier to test
5. Parse error messages or just change the doctests and do bettor error reporting later.

Afterwards (in other tickets ?):

1. Add doctests to maxima_abstract and maxima_lib
2. Avoid as much as possible string conversion in maxima_lib and take into account comment 73.



---

archive/issue_comments_061926.json:
```json
{
    "body": "Here is a patch to fix the interact function. It was only broken because python_to_ecl did not convert unicode objects.\n\nMy workaround is to convert the unicode object to an str object and convert that object as before.\n\nThere is surely a better way to do it, feel free to post a better patch and I'll integrate it to split_and_refactor instead of this one.",
    "created_at": "2011-03-02T09:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61926",
    "user": "jpflori"
}
```

Here is a patch to fix the interact function. It was only broken because python_to_ecl did not convert unicode objects.

My workaround is to convert the unicode object to an str object and convert that object as before.

There is surely a better way to do it, feel free to post a better patch and I'll integrate it to split_and_refactor instead of this one.



---

archive/issue_comments_061927.json:
```json
{
    "body": "Convert unicode objects to str objects to build ecl objects.",
    "created_at": "2011-03-02T09:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61927",
    "user": "jpflori"
}
```

Convert unicode objects to str objects to build ecl objects.



---

archive/issue_comments_061928.json:
```json
{
    "body": "Attachment [trac_7377-unicode_to_ecl.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-unicode_to_ecl.patch) by @kiwifb created at 2011-03-02 10:03:36\n\nDoes this patch means that sage won't be allergic to ecl being compiled with unicode support anymore?\n[https://github.com/cschwan/sage-on-gentoo/issues/closed#issue/2](https://github.com/cschwan/sage-on-gentoo/issues/closed#issue/2)",
    "created_at": "2011-03-02T10:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61928",
    "user": "@kiwifb"
}
```

Attachment [trac_7377-unicode_to_ecl.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-unicode_to_ecl.patch) by @kiwifb created at 2011-03-02 10:03:36

Does this patch means that sage won't be allergic to ecl being compiled with unicode support anymore?
[https://github.com/cschwan/sage-on-gentoo/issues/closed#issue/2](https://github.com/cschwan/sage-on-gentoo/issues/closed#issue/2)



---

archive/issue_comments_061929.json:
```json
{
    "body": "Thanks for indulging me, that helps a lot.\n\n> {{{\n>     sage: integral(x^n,x)\n> Expected:\n>     Traceback (most recent call last):\n>     ...\n>     TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):\n>     Is  n+1  zero or nonzero?\n> Got:\n>     Traceback (most recent call last):\n>     ...\n>     RuntimeError: ECL says: Maxima asks: Is  n+1  zero or nonzero?\n> \n> }}}\n> So we do not parse the error message and are less explicit than before.\n> \n\nHmm, we should really catch this particular RuntimeError (enough to search for 'Maxima asks', I think) and then copy the code which gave the user a potential way to fix it.  This behavior will be too confusing for the most likely people to be using Maxima, which is why we changed it the first time.  Should be pretty easy to copy from the previous behavior, though, if you are still getting this error.",
    "created_at": "2011-03-02T13:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61929",
    "user": "@kcrisman"
}
```

Thanks for indulging me, that helps a lot.

> {{{
>     sage: integral(x^n,x)
> Expected:
>     Traceback (most recent call last):
>     ...
>     TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n+1>0)' before integral or limit evaluation, for example):
>     Is  n+1  zero or nonzero?
> Got:
>     Traceback (most recent call last):
>     ...
>     RuntimeError: ECL says: Maxima asks: Is  n+1  zero or nonzero?
> 
> }}}
> So we do not parse the error message and are less explicit than before.
> 

Hmm, we should really catch this particular RuntimeError (enough to search for 'Maxima asks', I think) and then copy the code which gave the user a potential way to fix it.  This behavior will be too confusing for the most likely people to be using Maxima, which is why we changed it the first time.  Should be pretty easy to copy from the previous behavior, though, if you are still getting this error.



---

archive/issue_comments_061930.json:
```json
{
    "body": "* Better organization of patches: Yes! Keep in mind that separate patches have served us well previously, though, when initial fixes were amended (e.g., lazy loading).\n\n* unicode_to_ecl: seems like a reasonable approach to me. ECL can support unicode, but that is probably not of much use to us. Should that one go on a separate ticket, though? (think bitrot)\n\n* doctest in http://trac.sagemath.org/sage_trac/ticket/7377#comment:88 Perhaps the following helps. I tried that test on a pristine patched 4.6.2 and it passed. Then I ran `make ptestlong` and now it fails -- also when run individually. So that would point to ptestlong changing something. Does it rewrite/invalidate some maxima cache somewhere?\n\n* errors: I realized I was not quite correct. Errors about inconsistent assumptions now get reported differently too.\n\n* effort on error messages: Exceptions get used as a program flow control tool (e.g., in the coercion system) so any extra effort on constructing an error message has the potential of slowing down the system. So if you want extra info in the error message, put it where the string is created. We're controlling both sides of the plumbing anyway. See the better-ask-error patch. You could change it to something like\n\n```\n      (cond ((not print?)               ;;I'm not sure we want to honour this flag\n             (setq print? t)\n             (princ *prompt-prefix*)    ;;and I'm not sure we care about pre/suffices either\n             (princ *prompt-suffix*))\n            ((null msg)\n             (princ \"nothing\")\n            ((atom msg)\n             (format t \"~a~a~a\" *prompt-prefix* msg *prompt-suffix*)\n           ;;(format t \"~a\" msg )       ;;if we don't care about pre/suff\n             (mterpri))\n            ((eq flag t)\n             (princ *prompt-prefix*)\n             (mapc #'princ (cdr msg))\n             (princ *prompt-suffix*)\n             (mterpri))\n            (t\n             (princ *prompt-prefix*)\n             (displa msg)\n             (princ *prompt-suffix*)\n             (mterpri))))))\n      (princ \" You maybe able to answer this by using assume(...)\")) ;;put helpful advice here\n```\n\n\n* the same applies to the python_to_ecl error message: By using a \"...%s...\"%... in constructing the error message, you are slowing down the exception propagation. People can easily figure out which type it failed on by letting python drop into a debugger (%pdb 1) that allows them to analyze the local environment upon exception raising. (OK, you have to go \"u\" one time because pdb isn't terribly helpful with cython functions)\n\n* ecl+unicode: I doubt this patch solves it, since this implements something that was previously properly signalled by an exception, whereas the bugreport deals with a timeout. I suspect that bug might come from something in the other direction: ECL producing unicode that EclObject doesn't know how to deal with. I am sure this failure originates from __me__ being non-unicode compliant, since both ecl and python individually can handle this properly.",
    "created_at": "2011-03-02T18:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61930",
    "user": "@nbruin"
}
```

* Better organization of patches: Yes! Keep in mind that separate patches have served us well previously, though, when initial fixes were amended (e.g., lazy loading).

* unicode_to_ecl: seems like a reasonable approach to me. ECL can support unicode, but that is probably not of much use to us. Should that one go on a separate ticket, though? (think bitrot)

* doctest in http://trac.sagemath.org/sage_trac/ticket/7377#comment:88 Perhaps the following helps. I tried that test on a pristine patched 4.6.2 and it passed. Then I ran `make ptestlong` and now it fails -- also when run individually. So that would point to ptestlong changing something. Does it rewrite/invalidate some maxima cache somewhere?

* errors: I realized I was not quite correct. Errors about inconsistent assumptions now get reported differently too.

* effort on error messages: Exceptions get used as a program flow control tool (e.g., in the coercion system) so any extra effort on constructing an error message has the potential of slowing down the system. So if you want extra info in the error message, put it where the string is created. We're controlling both sides of the plumbing anyway. See the better-ask-error patch. You could change it to something like

```
      (cond ((not print?)               ;;I'm not sure we want to honour this flag
             (setq print? t)
             (princ *prompt-prefix*)    ;;and I'm not sure we care about pre/suffices either
             (princ *prompt-suffix*))
            ((null msg)
             (princ "nothing")
            ((atom msg)
             (format t "~a~a~a" *prompt-prefix* msg *prompt-suffix*)
           ;;(format t "~a" msg )       ;;if we don't care about pre/suff
             (mterpri))
            ((eq flag t)
             (princ *prompt-prefix*)
             (mapc #'princ (cdr msg))
             (princ *prompt-suffix*)
             (mterpri))
            (t
             (princ *prompt-prefix*)
             (displa msg)
             (princ *prompt-suffix*)
             (mterpri))))))
      (princ " You maybe able to answer this by using assume(...)")) ;;put helpful advice here
```


* the same applies to the python_to_ecl error message: By using a "...%s..."%... in constructing the error message, you are slowing down the exception propagation. People can easily figure out which type it failed on by letting python drop into a debugger (%pdb 1) that allows them to analyze the local environment upon exception raising. (OK, you have to go "u" one time because pdb isn't terribly helpful with cython functions)

* ecl+unicode: I doubt this patch solves it, since this implements something that was previously properly signalled by an exception, whereas the bugreport deals with a timeout. I suspect that bug might come from something in the other direction: ECL producing unicode that EclObject doesn't know how to deal with. I am sure this failure originates from __me__ being non-unicode compliant, since both ecl and python individually can handle this properly.



---

archive/issue_comments_061931.json:
```json
{
    "body": "Replying to [comment:96 nbruin]:\n\n> * doctest in http://trac.sagemath.org/sage_trac/ticket/7377#comment:88 Perhaps the following helps. I tried that test on a pristine patched 4.6.2 and it passed. Then I ran `make ptestlong` and now it fails -- also when run individually. So that would point to ptestlong changing something. Does it rewrite/invalidate some maxima cache somewhere?\n\nIt messes something in ~/.sage/maxima_commandlist_cache.sobj on my computer.\n\nDid not took the time to investigate it further.\n\nIf you delete that file it runs again.\n\n> * errors: I realized I was not quite correct. Errors about inconsistent assumptions now get reported differently too.\n\nI was aware of the inconsistent assumptions, I guess that's not a big problem.\n\n> * the same applies to the python_to_ecl error message: By using a \"...%s...\"%... in constructing the error message, you are slowing down the exception propagation. People can easily figure out which type it failed on by letting python drop into a debugger (%pdb 1) that allows them to analyze the local environment upon exception raising. (OK, you have to go \"u\" one time because pdb isn't terribly helpful with cython functions)\n\nI'll remove it.",
    "created_at": "2011-03-02T18:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61931",
    "user": "jpflori"
}
```

Replying to [comment:96 nbruin]:

> * doctest in http://trac.sagemath.org/sage_trac/ticket/7377#comment:88 Perhaps the following helps. I tried that test on a pristine patched 4.6.2 and it passed. Then I ran `make ptestlong` and now it fails -- also when run individually. So that would point to ptestlong changing something. Does it rewrite/invalidate some maxima cache somewhere?

It messes something in ~/.sage/maxima_commandlist_cache.sobj on my computer.

Did not took the time to investigate it further.

If you delete that file it runs again.

> * errors: I realized I was not quite correct. Errors about inconsistent assumptions now get reported differently too.

I was aware of the inconsistent assumptions, I guess that's not a big problem.

> * the same applies to the python_to_ecl error message: By using a "...%s..."%... in constructing the error message, you are slowing down the exception propagation. People can easily figure out which type it failed on by letting python drop into a debugger (%pdb 1) that allows them to analyze the local environment upon exception raising. (OK, you have to go "u" one time because pdb isn't terribly helpful with cython functions)

I'll remove it.



---

archive/issue_comments_061932.json:
```json
{
    "body": "> * effort on error messages: Exceptions get used as a program flow control tool (e.g., in the coercion system) so any extra effort on constructing an error message has the potential of slowing down the system. So if you want extra info in the error message, put it where the string is created. We're controlling both sides of the plumbing anyway. See the better-ask-error patch. You could change it to something like\n\n```\n      (princ \" You maybe able to answer this by using assume(...)\")) ;;put helpful advice here\n```\n\nYes, this would be ideal of course, it's just not something I know enough Lisp to do properly.  Is there a way to format the returned message in a similar way to how it currently happens (so that your ellipses above are filled in)?  It's currently something like\n\n```\n                j = v.find('Is ')\n                v = v[j:]\n                k = v.find(' ',4)\n                msg = \"Computation failed since Maxima requested additional constraints (try the command 'assume(\" + v[4:k] +\">0)' before integral or limit evaluation, for example):\\n\" + v + self._ask[i-1]\n                self._sendline(\";\")\n```\n\nSo if one could do the same extracting of the Of course, this is at the end of a long line of other things it does with respect to the `self._ask` business, which might be annoying.  Still, anything which does not explicitly give a Sage command which has a chance to work would be a downgrade.\n\nOtherwise amazing work, by the way!  So cool to see this nearly done.",
    "created_at": "2011-03-02T19:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61932",
    "user": "@kcrisman"
}
```

> * effort on error messages: Exceptions get used as a program flow control tool (e.g., in the coercion system) so any extra effort on constructing an error message has the potential of slowing down the system. So if you want extra info in the error message, put it where the string is created. We're controlling both sides of the plumbing anyway. See the better-ask-error patch. You could change it to something like

```
      (princ " You maybe able to answer this by using assume(...)")) ;;put helpful advice here
```

Yes, this would be ideal of course, it's just not something I know enough Lisp to do properly.  Is there a way to format the returned message in a similar way to how it currently happens (so that your ellipses above are filled in)?  It's currently something like

```
                j = v.find('Is ')
                v = v[j:]
                k = v.find(' ',4)
                msg = "Computation failed since Maxima requested additional constraints (try the command 'assume(" + v[4:k] +">0)' before integral or limit evaluation, for example):\n" + v + self._ask[i-1]
                self._sendline(";")
```

So if one could do the same extracting of the Of course, this is at the end of a long line of other things it does with respect to the `self._ask` business, which might be annoying.  Still, anything which does not explicitly give a Sage command which has a chance to work would be a downgrade.

Otherwise amazing work, by the way!  So cool to see this nearly done.



---

archive/issue_comments_061933.json:
```json
{
    "body": "Replying to [comment:98 kcrisman]:\n> Is there a way to format the returned message in a similar way to how it currently happens (so that your ellipses above are filled in)?\nYes, you could do the string processing in lisp, but in that case you may want to intercept that various ask... routines to preformat the question that gets sent to retrieve to begin with. Those should have more structured information on what question is asked, so formatting the question differently there should be quite cheap. However, there are two points why I think it's a bad idea anyway:\n\n* The advice currently is wrong! Why would \"...>0\" be the right thing? That just propagates a kind of halfbrained trial-and-error mathematics that I cannot bring myself to endorse. The proper advice is for the user to read up on the assume(...) facility.\n\n* There are big problems with relying on the print names of symbols agreeing between maxima and sage. Now that we're moving away from string-based communication it would be quite easy to let SR(\"x\") correspond to EclObject(\"$SAGE-SYMBOLIC-VARIABLE-4711\"). The actual question that maxima asks is not so enlightening anymore in that situation.\n\nIn fact, currently, the advice already leads to errors\n\n```\nsage: my_symbolic_n=SR.var('n')\nsage: limit(x^my_symbolic_n,x=oo)\nTypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n>0)' before integral or limit evaluation, for example):\nIs  n  positive, negative, or zero?\nsage: assume(n>0)\nAttributeError: 'bool' object has no attribute 'assume'\nsage: n\n<function numerical_approx at 0x18e0410>\n```\n\nso the user actually has a good reason to not shadow the python binding of n, but of course the print name n for a symbolic variable is very desirable. You CANNOT assume that the print name corresponds with the python variable bound to your object and sage SHOULD NOT propagate such assumptions in its error messages. It's nice to make a program accessible to starters but not at the expense of allowing them to progress to experienced users.",
    "created_at": "2011-03-02T20:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61933",
    "user": "@nbruin"
}
```

Replying to [comment:98 kcrisman]:
> Is there a way to format the returned message in a similar way to how it currently happens (so that your ellipses above are filled in)?
Yes, you could do the string processing in lisp, but in that case you may want to intercept that various ask... routines to preformat the question that gets sent to retrieve to begin with. Those should have more structured information on what question is asked, so formatting the question differently there should be quite cheap. However, there are two points why I think it's a bad idea anyway:

* The advice currently is wrong! Why would "...>0" be the right thing? That just propagates a kind of halfbrained trial-and-error mathematics that I cannot bring myself to endorse. The proper advice is for the user to read up on the assume(...) facility.

* There are big problems with relying on the print names of symbols agreeing between maxima and sage. Now that we're moving away from string-based communication it would be quite easy to let SR("x") correspond to EclObject("$SAGE-SYMBOLIC-VARIABLE-4711"). The actual question that maxima asks is not so enlightening anymore in that situation.

In fact, currently, the advice already leads to errors

```
sage: my_symbolic_n=SR.var('n')
sage: limit(x^my_symbolic_n,x=oo)
TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n>0)' before integral or limit evaluation, for example):
Is  n  positive, negative, or zero?
sage: assume(n>0)
AttributeError: 'bool' object has no attribute 'assume'
sage: n
<function numerical_approx at 0x18e0410>
```

so the user actually has a good reason to not shadow the python binding of n, but of course the print name n for a symbolic variable is very desirable. You CANNOT assume that the print name corresponds with the python variable bound to your object and sage SHOULD NOT propagate such assumptions in its error messages. It's nice to make a program accessible to starters but not at the expense of allowing them to progress to experienced users.



---

archive/issue_comments_061934.json:
```json
{
    "body": ">  * The advice currently is wrong! Why would \"...>0\" be the right thing? That just propagates a kind of halfbrained trial-and-error mathematics that I cannot bring myself to endorse. The proper advice is for the user to read up on the assume(...) facility.\n\nThen you did not read the words, \"for example\".  And the 'trial-and-error mathematics' comment may then be aimed at Maxima as well, especially when it asks all kinds of questions and the result is always the same.  (rjf would no doubt comment that this is undecidable.)    Perhaps the user really didn't consider whether `x>0` until just then, and might as well try all possibilities.  That certainly happens in real life.\n\nThis is the best we have to deal with it right now, and until Maxima stops asking such questions, what else can one do?  The error message gives the syntax, not the mathematics.  Can you think of a different way to phrase it that makes it clear we aren't actually suggesting `x>0` in reality?  \n\nSaying to read up on assume() is sort of like telling people to read the man page; totally useless if you do not already have an idea that such a thing exists.  Read `assume?` if you don't believe me.  Obviously that could be improved, but it would be strange to put things about integrals and limits at the top of that file (where they'd need to be to catch attention), and there is no reason not to give a maximally helpful error message right off the bat.\n\n> In fact, currently, the advice already leads to errors\n> sage: my_symbolic_n=SR.var('n')\n> sage: limit(x^my_symbolic_n,x=oo)\n> TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n>0)' before integral or limit evaluation, for example):\n> Is  n  positive, negative, or zero?\n> sage: assume(n>0)\n> AttributeError: 'bool' object has no attribute 'assume'\n> sage: n\n> <function numerical_approx at 0x18e0410>\n>You CANNOT assume that the print name corresponds with the python variable bound to your object and sage SHOULD NOT propagate such assumptions in its error messages. It's nice to make a program accessible to starters but not at the expense of allowing them to progress to experienced users.\n\nNothing here is stopping someone from advancing to being experienced.  This problem occurs other places than here - see many discussions on sage-devel about print names not coinciding, or about var() being annoying in general.  If someone knows anything about what you are saying, they will be plenty experienced to realize that this message isn't talking about 'their' n.  \n\nSorry if I sound irked.  But there is a place for such lawyering - lawyering over a minor thing which would make Sage more friendly to beginners and which doesn't actually harm the advanced users - and that place is not in a program that is trying to become a 'viable replacement for Mathematica and Maple'.   I've seen this over and over, and can't figure out who this is hurting in many such cases.\n\nAnyway, I hope we can come to some reasonable compromise on this.  The current suggestion would make a very common error message less useful.",
    "created_at": "2011-03-02T21:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61934",
    "user": "@kcrisman"
}
```

>  * The advice currently is wrong! Why would "...>0" be the right thing? That just propagates a kind of halfbrained trial-and-error mathematics that I cannot bring myself to endorse. The proper advice is for the user to read up on the assume(...) facility.

Then you did not read the words, "for example".  And the 'trial-and-error mathematics' comment may then be aimed at Maxima as well, especially when it asks all kinds of questions and the result is always the same.  (rjf would no doubt comment that this is undecidable.)    Perhaps the user really didn't consider whether `x>0` until just then, and might as well try all possibilities.  That certainly happens in real life.

This is the best we have to deal with it right now, and until Maxima stops asking such questions, what else can one do?  The error message gives the syntax, not the mathematics.  Can you think of a different way to phrase it that makes it clear we aren't actually suggesting `x>0` in reality?  

Saying to read up on assume() is sort of like telling people to read the man page; totally useless if you do not already have an idea that such a thing exists.  Read `assume?` if you don't believe me.  Obviously that could be improved, but it would be strange to put things about integrals and limits at the top of that file (where they'd need to be to catch attention), and there is no reason not to give a maximally helpful error message right off the bat.

> In fact, currently, the advice already leads to errors
> sage: my_symbolic_n=SR.var('n')
> sage: limit(x^my_symbolic_n,x=oo)
> TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(n>0)' before integral or limit evaluation, for example):
> Is  n  positive, negative, or zero?
> sage: assume(n>0)
> AttributeError: 'bool' object has no attribute 'assume'
> sage: n
> <function numerical_approx at 0x18e0410>
>You CANNOT assume that the print name corresponds with the python variable bound to your object and sage SHOULD NOT propagate such assumptions in its error messages. It's nice to make a program accessible to starters but not at the expense of allowing them to progress to experienced users.

Nothing here is stopping someone from advancing to being experienced.  This problem occurs other places than here - see many discussions on sage-devel about print names not coinciding, or about var() being annoying in general.  If someone knows anything about what you are saying, they will be plenty experienced to realize that this message isn't talking about 'their' n.  

Sorry if I sound irked.  But there is a place for such lawyering - lawyering over a minor thing which would make Sage more friendly to beginners and which doesn't actually harm the advanced users - and that place is not in a program that is trying to become a 'viable replacement for Mathematica and Maple'.   I've seen this over and over, and can't figure out who this is hurting in many such cases.

Anyway, I hope we can come to some reasonable compromise on this.  The current suggestion would make a very common error message less useful.



---

archive/issue_comments_061935.json:
```json
{
    "body": "Solve it how you like. I don't particularly mind what sage does. I've given you the reasons why __I__ won't be doing it. I think you can settle on some fixed example expression inside the error message, a la \"A declaration along the lines of assume(x>0) may help solve your problem.\", because the surgery that is currently done doesn't always lead to useful suggestions anyway, i.e.,\n\n```\nsage: var('x,y')\nsage: integrate(log(x^2+y^2),x,0,1)\n```\n\nsuggests `assume( (y+1)*(y-1) > 0 )` which doesn't make the question go away, and the fact that sage clearly goes out of its way to make a suggestion that doesn't turn out to help really does look silly.\nLet's keep this issue outside the ticket comments, because they are getting too long to scroll already.",
    "created_at": "2011-03-02T23:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61935",
    "user": "@nbruin"
}
```

Solve it how you like. I don't particularly mind what sage does. I've given you the reasons why __I__ won't be doing it. I think you can settle on some fixed example expression inside the error message, a la "A declaration along the lines of assume(x>0) may help solve your problem.", because the surgery that is currently done doesn't always lead to useful suggestions anyway, i.e.,

```
sage: var('x,y')
sage: integrate(log(x^2+y^2),x,0,1)
```

suggests `assume( (y+1)*(y-1) > 0 )` which doesn't make the question go away, and the fact that sage clearly goes out of its way to make a suggestion that doesn't turn out to help really does look silly.
Let's keep this issue outside the ticket comments, because they are getting too long to scroll already.



---

archive/issue_comments_061936.json:
```json
{
    "body": "There are tickets with three times as many comments, and I have never heard that complaint before.  If a ticket causes a regression - and this is one, if slight - then that should be dealt with appropriately on that ticket.  \n\nIf one insists that it is not relevant, or that it should not hold up a valuable improvement, then it would seem courteous for the person who believes it no longer belongs on that ticket to open a followup ticket along with relevant links to the discussion on the previous ticket.  Given the work that has gone into this, that might be appropriate, but it seems to me it could also be dealt with on this one.\n\nAs to the error report, it doesn't always make it go away, sure.  This is because some integration problems are just hard, and because Maxima can't do all the ones that might not be hard, and because Maxima's assumption framework is in fact weak, as they always say.  It doesn't really seem any sillier than Maxima asking a million questions all to come up with the same answer.",
    "created_at": "2011-03-03T01:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61936",
    "user": "@kcrisman"
}
```

There are tickets with three times as many comments, and I have never heard that complaint before.  If a ticket causes a regression - and this is one, if slight - then that should be dealt with appropriately on that ticket.  

If one insists that it is not relevant, or that it should not hold up a valuable improvement, then it would seem courteous for the person who believes it no longer belongs on that ticket to open a followup ticket along with relevant links to the discussion on the previous ticket.  Given the work that has gone into this, that might be appropriate, but it seems to me it could also be dealt with on this one.

As to the error report, it doesn't always make it go away, sure.  This is because some integration problems are just hard, and because Maxima can't do all the ones that might not be hard, and because Maxima's assumption framework is in fact weak, as they always say.  It doesn't really seem any sillier than Maxima asking a million questions all to come up with the same answer.



---

archive/issue_comments_061937.json:
```json
{
    "body": "Tried all the patches on top of the current 4.7.alpha2. Apart from the already much discussed doctests errors mentioned so far I had one in interfaces/maxima_abstract.py\n\n```\nsage -t -long -force_lib \"devel/sage/sage/interfaces/maxima_abstract.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/interfaces/maxima_abstract.py\", line 197:\n    sage: sorted(maxima._commands(verbose=False))\nExpected:\n    ['Alpha',\n     'Beta',\n     ...\n     'zunderflow']\nGot:\n    ['Alpha', 'Beta', \n<cut a very long list>\n 'zunderflow', 'zz']\n```\n",
    "created_at": "2011-03-03T09:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61937",
    "user": "@kiwifb"
}
```

Tried all the patches on top of the current 4.7.alpha2. Apart from the already much discussed doctests errors mentioned so far I had one in interfaces/maxima_abstract.py

```
sage -t -long -force_lib "devel/sage/sage/interfaces/maxima_abstract.py"
**********************************************************************
File "/usr/share/sage/devel/sage/sage/interfaces/maxima_abstract.py", line 197:
    sage: sorted(maxima._commands(verbose=False))
Expected:
    ['Alpha',
     'Beta',
     ...
     'zunderflow']
Got:
    ['Alpha', 'Beta', 
<cut a very long list>
 'zunderflow', 'zz']
```




---

archive/issue_comments_061938.json:
```json
{
    "body": "Attachment [trac_7377-split_and_refactor-p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-split_and_refactor-p2.patch) by jpflori created at 2011-03-03 09:52:22\n\nUpdatred version for newlines in error reporting.",
    "created_at": "2011-03-03T09:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61938",
    "user": "jpflori"
}
```

Attachment [trac_7377-split_and_refactor-p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-split_and_refactor-p2.patch) by jpflori created at 2011-03-03 09:52:22

Updatred version for newlines in error reporting.



---

archive/issue_comments_061939.json:
```json
{
    "body": "I just updated the split_and_refactor patch to rmove supefluous calls to \"terpri\" and \"mterpri\".\n\nI left the \"strim-string\" because it seems that \"displa\" adds one.\n\nAnyway, there should be work done on error reporting (I'd say later, let's try to get the lib interface reviewed and merged now).\n\nNils and I got the same problem as Fran\u00e7ois in maxima_abstract.\n\nIt's related to the data saved in ~/.sage/maxima_commandlist_cache.sobj which seems to get updated with unrelated data.\n\nIf you delete the file and rerun the test, it gives you what it should.\n\nI'll have a look at it.",
    "created_at": "2011-03-03T09:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61939",
    "user": "jpflori"
}
```

I just updated the split_and_refactor patch to rmove supefluous calls to "terpri" and "mterpri".

I left the "strim-string" because it seems that "displa" adds one.

Anyway, there should be work done on error reporting (I'd say later, let's try to get the lib interface reviewed and merged now).

Nils and I got the same problem as François in maxima_abstract.

It's related to the data saved in ~/.sage/maxima_commandlist_cache.sobj which seems to get updated with unrelated data.

If you delete the file and rerun the test, it gives you what it should.

I'll have a look at it.



---

archive/issue_comments_061940.json:
```json
{
    "body": "Simpler patch not to slow exception propagation.",
    "created_at": "2011-03-03T09:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61940",
    "user": "jpflori"
}
```

Simpler patch not to slow exception propagation.



---

archive/issue_comments_061941.json:
```json
{
    "body": "Attachment [trac_7377-unicode_to_ecl-p1.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-unicode_to_ecl-p1.patch) by jpflori created at 2011-03-03 10:00:15",
    "created_at": "2011-03-03T10:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61941",
    "user": "jpflori"
}
```

Attachment [trac_7377-unicode_to_ecl-p1.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-unicode_to_ecl-p1.patch) by jpflori created at 2011-03-03 10:00:15



---

archive/issue_comments_061942.json:
```json
{
    "body": "Replying to [comment:103 fbissey]:\n\n> Tried all the patches on top of the current 4.7.alpha2. Apart from the already much discussed doctests errors mentioned so far I had one in interfaces/maxima_abstract.py ` sage -t -long -force_lib \"devel/sage/sage/interfaces/maxima_abstract.py\" ********************************************************************** File \"/usr/share/sage/devel/sage/sage/interfaces/maxima_abstract.py\", line 197: sage: sorted(maxima._commands(verbose=False)) Expected: ['Alpha', 'Beta', ... 'zunderflow'] Got: ['Alpha', 'Beta',  <cut a very long list> 'zunderflow', 'zz'] `\n\nThe problem here is that some doctest in maxima_abstract.py creates something called 'zz' and if the test line 197 gets executed afterwards, self.!__commands gets built then and includes 'zz', it fails... not really sure why this happens now and did not before.\n\nIf I put a call to self._commands() at the beginning of the doctest for trait_names(), self.!__commands is built without 'zz'.\n\nSo we could consider that this is not a bug.\n\nWhat's more problematic is that the result of _commands() gets cached and includes a fraction of random variable names (as 'sage???' and the problematic 'zz'). that was already the case before but fortunately no var between 'Alpha' and 'Beta' or after 'zunderflow' was created.",
    "created_at": "2011-03-03T14:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61942",
    "user": "jpflori"
}
```

Replying to [comment:103 fbissey]:

> Tried all the patches on top of the current 4.7.alpha2. Apart from the already much discussed doctests errors mentioned so far I had one in interfaces/maxima_abstract.py ` sage -t -long -force_lib "devel/sage/sage/interfaces/maxima_abstract.py" ********************************************************************** File "/usr/share/sage/devel/sage/sage/interfaces/maxima_abstract.py", line 197: sage: sorted(maxima._commands(verbose=False)) Expected: ['Alpha', 'Beta', ... 'zunderflow'] Got: ['Alpha', 'Beta',  <cut a very long list> 'zunderflow', 'zz'] `

The problem here is that some doctest in maxima_abstract.py creates something called 'zz' and if the test line 197 gets executed afterwards, self.!__commands gets built then and includes 'zz', it fails... not really sure why this happens now and did not before.

If I put a call to self._commands() at the beginning of the doctest for trait_names(), self.!__commands is built without 'zz'.

So we could consider that this is not a bug.

What's more problematic is that the result of _commands() gets cached and includes a fraction of random variable names (as 'sage???' and the problematic 'zz'). that was already the case before but fortunately no var between 'Alpha' and 'Beta' or after 'zunderflow' was created.



---

archive/issue_comments_061943.json:
```json
{
    "body": "Okay, I think I learned enough just barely enough Lisp now that I might be able to help on the assumptions/declarations issue.  \n\nHowever, there are other Maxima errors that might get reported.  So one would, at the minimum, want to have a conditional error situation.  One princ option wouldn't be enough.  That seems to be a nightmare to do (at least for someone not an expert in Lisp).  I even briefly wondered whether we might want Sage people at the command line to be able to interact and type 'y' like in Maxima, which perhaps is possible now... anyway, that was lies madness, at least for me.\n\nSo would it be terribly horrible to catch in the same way the function already does?\n\n```\n    def sr_integral(self,*args):\n        try:\n            return max_to_sr(maxima_eval(([max_integrate],[sr_to_max(SR(a)) for a in args])))\n        except RuntimeError, error:\n            s = str(error)\n            if \"Divergent\" in s or \"divergent\" in s:\n                raise ValueError, \"Integral is divergent.\"\n            else:\n                raise error\n```\n\nThis is only going to slow things down if there is, in fact, an error.  I don't see why one couldn't put something here, if we are already going to catch divergent integrals.  And this is basically how it was handled before.\n\nOne could similarly do this with `sr_limit` (what is `sr_tlimit`?), with examples like \n\n```\nsage: var('a')    \na\nsage: limit(x^a,x=0)\n<snip>\nRuntimeError: ECL says: Maxima asks: Is  a  positive, negative, or zero?\n```\n\nwhich, remarkably, is not in the doctests (there is no limit question-asking error, that is, despite the fact that Maxima certainly will ask about this).\n\nSimilarly, with the inconsistent assumptions, one could change the try/except\n\n```\n      File \"/Users/student/Desktop/sage-4.6.2/local/lib/python/site-packages/sage/symbolic/assumptions.py\", line 104, in assume\n        maxima.eval(\"declare(%s, %s)\" % (repr(self._var), self._assumption))\n      File \"/Users/student/Desktop/sage-4.6.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py\", line 266, in eval\n        if statement: result = ((result + '\\n') if result else '') + max_to_string(maxima_eval(\"#$%s$\"%statement))\n      File \"ecl.pyx\", line 619, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:4425)\n      File \"ecl.pyx\", line 202, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:2609)\n    RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)\n```\n\nin assumptions.py to look for a RuntimeError.  \n\nThe latter is pretty easy to fix, I think.  But hopefully all of these could lead to finishing this off.\n\n\n\n----\n\nWhat about doctests?  I noticed that definitely not all functions are doctested - no surprise, this is a huge project.  Will that hold up merging of this, though?  \n\n\n```\ndevel/sage/sage/interfaces//maxima_lib.py\nSCORE devel/sage/sage/interfaces//maxima_lib.py: 37% (13 of 35)\ndevel/sage/sage/interfaces//maxima_abstract.py\nSCORE devel/sage/sage/interfaces//maxima_abstract.py: 96% (78 of 81)\ndevel/sage/sage/interfaces//maxima.py\nSCORE devel/sage/sage/interfaces//maxima.py: 61% (19 of 31)\n```\n\n\nThe current Maxima interface has 94 of 100 functions doctested.  Just throwing it out there, I know jpflori also has mentioned it above, but this is a little data on it.",
    "created_at": "2011-03-09T21:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61943",
    "user": "@kcrisman"
}
```

Okay, I think I learned enough just barely enough Lisp now that I might be able to help on the assumptions/declarations issue.  

However, there are other Maxima errors that might get reported.  So one would, at the minimum, want to have a conditional error situation.  One princ option wouldn't be enough.  That seems to be a nightmare to do (at least for someone not an expert in Lisp).  I even briefly wondered whether we might want Sage people at the command line to be able to interact and type 'y' like in Maxima, which perhaps is possible now... anyway, that was lies madness, at least for me.

So would it be terribly horrible to catch in the same way the function already does?

```
    def sr_integral(self,*args):
        try:
            return max_to_sr(maxima_eval(([max_integrate],[sr_to_max(SR(a)) for a in args])))
        except RuntimeError, error:
            s = str(error)
            if "Divergent" in s or "divergent" in s:
                raise ValueError, "Integral is divergent."
            else:
                raise error
```

This is only going to slow things down if there is, in fact, an error.  I don't see why one couldn't put something here, if we are already going to catch divergent integrals.  And this is basically how it was handled before.

One could similarly do this with `sr_limit` (what is `sr_tlimit`?), with examples like 

```
sage: var('a')    
a
sage: limit(x^a,x=0)
<snip>
RuntimeError: ECL says: Maxima asks: Is  a  positive, negative, or zero?
```

which, remarkably, is not in the doctests (there is no limit question-asking error, that is, despite the fact that Maxima certainly will ask about this).

Similarly, with the inconsistent assumptions, one could change the try/except

```
      File "/Users/student/Desktop/sage-4.6.2/local/lib/python/site-packages/sage/symbolic/assumptions.py", line 104, in assume
        maxima.eval("declare(%s, %s)" % (repr(self._var), self._assumption))
      File "/Users/student/Desktop/sage-4.6.2/local/lib/python/site-packages/sage/interfaces/maxima_lib.py", line 266, in eval
        if statement: result = ((result + '\n') if result else '') + max_to_string(maxima_eval("#$%s$"%statement))
      File "ecl.pyx", line 619, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:4425)
      File "ecl.pyx", line 202, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:2609)
    RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)
```

in assumptions.py to look for a RuntimeError.  

The latter is pretty easy to fix, I think.  But hopefully all of these could lead to finishing this off.



----

What about doctests?  I noticed that definitely not all functions are doctested - no surprise, this is a huge project.  Will that hold up merging of this, though?  


```
devel/sage/sage/interfaces//maxima_lib.py
SCORE devel/sage/sage/interfaces//maxima_lib.py: 37% (13 of 35)
devel/sage/sage/interfaces//maxima_abstract.py
SCORE devel/sage/sage/interfaces//maxima_abstract.py: 96% (78 of 81)
devel/sage/sage/interfaces//maxima.py
SCORE devel/sage/sage/interfaces//maxima.py: 61% (19 of 31)
```


The current Maxima interface has 94 of 100 functions doctested.  Just throwing it out there, I know jpflori also has mentioned it above, but this is a little data on it.



---

archive/issue_comments_061944.json:
```json
{
    "body": "So there are 3 identified problems left:\n\n* We could catch errors as suggested in the previous comment to report them as before. It could be changed back to something else in a later ticket (hopefully this ticket could be merged quickly, and anyway there is still a lot of work left to communicate directly with Maxima as a lib avoiding strings transformations).\n* I'll try to add doctests this weekend.\n* As far as the problem mentionned in comment 106 is concerned, we could mark its output as random or something like ![... ,gcd,...another function,...] (and modify commands() later if really needed).\n\nAfterwards the ticket would finally be ready for review.",
    "created_at": "2011-03-10T15:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61944",
    "user": "jpflori"
}
```

So there are 3 identified problems left:

* We could catch errors as suggested in the previous comment to report them as before. It could be changed back to something else in a later ticket (hopefully this ticket could be merged quickly, and anyway there is still a lot of work left to communicate directly with Maxima as a lib avoiding strings transformations).
* I'll try to add doctests this weekend.
* As far as the problem mentionned in comment 106 is concerned, we could mark its output as random or something like ![... ,gcd,...another function,...] (and modify commands() later if really needed).

Afterwards the ticket would finally be ready for review.



---

archive/issue_comments_061945.json:
```json
{
    "body": ">  * We could catch errors as suggested in the previous comment to report them as before. It could be changed back to something else in a later ticket (hopefully this ticket could be merged quickly, and anyway there is still a lot of work left to communicate directly with Maxima as a lib avoiding strings transformations).\nOkay, that seems best to me as well so it can actually get merged.  Presumably lots of potential followup tickets.\n\nSo I will try to do this today on top of the current list of patches, though I expect whatever I create will be merged by one of you into a p3 patch if that makes it easier to follow.\n\n>  * I'll try to add doctests this weekend.\nImpressive! Hopefully at least some can be nearly copied from the previous doctests (?)\n>  * As far as the problem mentionned in comment 106 is concerned, we could mark its output as random or something like ![... ,gcd,...another function,...] (and modify commands() later if really needed).\nProbably better to have an actual doctest like that, as random might allow weird things to slip through.\n> Afterwards the ticket would finally be ready for review.\nYes!",
    "created_at": "2011-03-10T16:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61945",
    "user": "@kcrisman"
}
```

>  * We could catch errors as suggested in the previous comment to report them as before. It could be changed back to something else in a later ticket (hopefully this ticket could be merged quickly, and anyway there is still a lot of work left to communicate directly with Maxima as a lib avoiding strings transformations).
Okay, that seems best to me as well so it can actually get merged.  Presumably lots of potential followup tickets.

So I will try to do this today on top of the current list of patches, though I expect whatever I create will be merged by one of you into a p3 patch if that makes it easier to follow.

>  * I'll try to add doctests this weekend.
Impressive! Hopefully at least some can be nearly copied from the previous doctests (?)
>  * As far as the problem mentionned in comment 106 is concerned, we could mark its output as random or something like ![... ,gcd,...another function,...] (and modify commands() later if really needed).
Probably better to have an actual doctest like that, as random might allow weird things to slip through.
> Afterwards the ticket would finally be ready for review.
Yes!



---

archive/issue_comments_061946.json:
```json
{
    "body": "Another minor issue with the doctests.  Am I correct that `maxima` still gives the pexpect interface, while all 'calculus' stuff is done with the library interface?  In that case the stuff about calculus at the top of `maxima.py` needs to be deleted, probably - perhaps put at the top of `maxima_lib.py`, since we would want to keep the doctests and information?\n\nAlso, probably JP, Nils, and/or Robert's names should be added at the top of these files!",
    "created_at": "2011-03-10T17:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61946",
    "user": "@kcrisman"
}
```

Another minor issue with the doctests.  Am I correct that `maxima` still gives the pexpect interface, while all 'calculus' stuff is done with the library interface?  In that case the stuff about calculus at the top of `maxima.py` needs to be deleted, probably - perhaps put at the top of `maxima_lib.py`, since we would want to keep the doctests and information?

Also, probably JP, Nils, and/or Robert's names should be added at the top of these files!



---

archive/issue_comments_061947.json:
```json
{
    "body": "Replying to [comment:110 kcrisman]:\n\n> Another minor issue with the doctests.  Am I correct that `maxima` still gives the pexpect interface, while all 'calculus' stuff is done with the library interface?  In that case the stuff about calculus at the top of `maxima.py` needs to be deleted, probably - perhaps put at the top of `maxima_lib.py`, since we would want to keep the doctests and information?\nYou're right about maxima and calculus, I'll have a look at that while working on doctests.\n> Also, probably JP, Nils, and/or Robert's names should be added at the top of these files!\nI'll do it also.",
    "created_at": "2011-03-10T17:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61947",
    "user": "jpflori"
}
```

Replying to [comment:110 kcrisman]:

> Another minor issue with the doctests.  Am I correct that `maxima` still gives the pexpect interface, while all 'calculus' stuff is done with the library interface?  In that case the stuff about calculus at the top of `maxima.py` needs to be deleted, probably - perhaps put at the top of `maxima_lib.py`, since we would want to keep the doctests and information?
You're right about maxima and calculus, I'll have a look at that while working on doctests.
> Also, probably JP, Nils, and/or Robert's names should be added at the top of these files!
I'll do it also.



---

archive/issue_comments_061948.json:
```json
{
    "body": "Replying to [comment:111 jpflori]:\n> Replying to [comment:110 kcrisman]:\n> \n> > Another minor issue with the doctests.  Am I correct that `maxima` still gives the pexpect interface, while all 'calculus' stuff is done with the library interface?  In that case the stuff about calculus at the top of `maxima.py` needs to be deleted, probably - perhaps put at the top of `maxima_lib.py`, since we would want to keep the doctests and information?\n> You're right about maxima and calculus, I'll have a look at that while working on doctests.\n> \nNever mind, this is all correct as it stands.  I have been singularly unhelpful, though not by design.  Maybe one could copy the material at the top of `maxima.py` and put it in `maxima_lib.py` with a `from sage.interface.maxima_lib import maxima` at the very beginning, with some clarifying words.  That would provide a double check, too.\n\nThere are also a few places in a few docs that still mention expect wrongly, I think - I'll keep looking for them.  \n\nIssues I think I can deal with while taking care of the error handling:\n\n* `maxima._expect_expr`, while usefully staying the same as before, certainly isn't doctested by those tests any more.\n* Can the old `sr_integral` etc. in `maxima.py` be removed, or should they be kept in case someone wanted to use the pexpect for doing calculus?  I would think remove.\n* With respect to `sr_sum` and `sr_integral`, since they are implementing the divergent integral/sum check, should we remove those from `calculus.py` and `symbolic.integration.external.py`?  Those pieces of code will probably never be reached, since the ValueError is already raised in `maxima_lib.py`.\n\nI'll keep looking for things like this, hopefully catch as many as possible.",
    "created_at": "2011-03-10T17:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61948",
    "user": "@kcrisman"
}
```

Replying to [comment:111 jpflori]:
> Replying to [comment:110 kcrisman]:
> 
> > Another minor issue with the doctests.  Am I correct that `maxima` still gives the pexpect interface, while all 'calculus' stuff is done with the library interface?  In that case the stuff about calculus at the top of `maxima.py` needs to be deleted, probably - perhaps put at the top of `maxima_lib.py`, since we would want to keep the doctests and information?
> You're right about maxima and calculus, I'll have a look at that while working on doctests.
> 
Never mind, this is all correct as it stands.  I have been singularly unhelpful, though not by design.  Maybe one could copy the material at the top of `maxima.py` and put it in `maxima_lib.py` with a `from sage.interface.maxima_lib import maxima` at the very beginning, with some clarifying words.  That would provide a double check, too.

There are also a few places in a few docs that still mention expect wrongly, I think - I'll keep looking for them.  

Issues I think I can deal with while taking care of the error handling:

* `maxima._expect_expr`, while usefully staying the same as before, certainly isn't doctested by those tests any more.
* Can the old `sr_integral` etc. in `maxima.py` be removed, or should they be kept in case someone wanted to use the pexpect for doing calculus?  I would think remove.
* With respect to `sr_sum` and `sr_integral`, since they are implementing the divergent integral/sum check, should we remove those from `calculus.py` and `symbolic.integration.external.py`?  Those pieces of code will probably never be reached, since the ValueError is already raised in `maxima_lib.py`.

I'll keep looking for things like this, hopefully catch as many as possible.



---

archive/issue_comments_061949.json:
```json
{
    "body": "Okay, while this patch is not 100% ready, it is certainly good enough to look at and give feedback on.  It takes care of the three things I mention above, and adds a little doctesting.  It also documents `assume` more comprehensively early in its docstring.\n\nI get a weird error with this, though:\n\n```\nsage:             sage: var('x, n')\n(x, n)\nsage:             sage: integral(x^n,x)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (534, 0))\n<snip - then the expected ValueError>\n```\n\nwhich I cannot explain.",
    "created_at": "2011-03-10T21:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61949",
    "user": "@kcrisman"
}
```

Okay, while this patch is not 100% ready, it is certainly good enough to look at and give feedback on.  It takes care of the three things I mention above, and adds a little doctesting.  It also documents `assume` more comprehensively early in its docstring.

I get a weird error with this, though:

```
sage:             sage: var('x, n')
(x, n)
sage:             sage: integral(x^n,x)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (534, 0))
<snip - then the expected ValueError>
```

which I cannot explain.



---

archive/issue_comments_061950.json:
```json
{
    "body": "Attachment [trac_7377-assumptions.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-assumptions.patch) by @kcrisman created at 2011-03-10 21:26:20\n\nTrial patch to improve assumption messages and documentation of helper functions",
    "created_at": "2011-03-10T21:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61950",
    "user": "@kcrisman"
}
```

Attachment [trac_7377-assumptions.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-assumptions.patch) by @kcrisman created at 2011-03-10 21:26:20

Trial patch to improve assumption messages and documentation of helper functions



---

archive/issue_comments_061951.json:
```json
{
    "body": "Slightly reworked patch.",
    "created_at": "2011-03-14T15:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61951",
    "user": "jpflori"
}
```

Slightly reworked patch.



---

archive/issue_comments_061952.json:
```json
{
    "body": "Attachment [trac_7377-doctests.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests.patch) by jpflori created at 2011-03-14 15:59:06\n\n(Really) basic tests and doc for every functions in sage.interfaces.maxima*",
    "created_at": "2011-03-14T15:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61952",
    "user": "jpflori"
}
```

Attachment [trac_7377-doctests.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests.patch) by jpflori created at 2011-03-14 15:59:06

(Really) basic tests and doc for every functions in sage.interfaces.maxima*



---

archive/issue_comments_061953.json:
```json
{
    "body": "We now have 100% ((really) basic (and stupid)) doctests coverage.\n\nI also fixed some minor issues here and there.\n\nWhat could be postponed to later tickets:\n\n* better doctests\n* better error handling\n* better conversions between maxima and sr\n* reorganize the code in maxima_lib to make it clearer",
    "created_at": "2011-03-14T16:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61953",
    "user": "jpflori"
}
```

We now have 100% ((really) basic (and stupid)) doctests coverage.

I also fixed some minor issues here and there.

What could be postponed to later tickets:

* better doctests
* better error handling
* better conversions between maxima and sr
* reorganize the code in maxima_lib to make it clearer



---

archive/issue_comments_061954.json:
```json
{
    "body": "Thanks for catching the calculus/functional one.  I also noticed something that will cause a Sphinx error - which was my bad - so I'm uploading a trivially changed p2.",
    "created_at": "2011-03-14T16:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61954",
    "user": "@kcrisman"
}
```

Thanks for catching the calculus/functional one.  I also noticed something that will cause a Sphinx error - which was my bad - so I'm uploading a trivially changed p2.



---

archive/issue_comments_061955.json:
```json
{
    "body": "Attachment [trac_7377-assumptions-p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-assumptions-p2.patch) by @kcrisman created at 2011-03-14 16:40:41\n\ntrivial correction to p1 patch",
    "created_at": "2011-03-14T16:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61955",
    "user": "@kcrisman"
}
```

Attachment [trac_7377-assumptions-p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-assumptions-p2.patch) by @kcrisman created at 2011-03-14 16:40:41

trivial correction to p1 patch



---

archive/issue_comments_061956.json:
```json
{
    "body": "Sorry I do not have time to check this properly today.  Do you get the \n\n```\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\n```\n\nproblem with these patches?  I hope not :)\n\nA couple very small points about the doctests patch, which by the way is nontrivial and nice all by itself.\n* You should have a `loads(dumps(foo))==foo` test if possible for class definitions.  I think there are eight of these? \n* You probably don't need to put `INPUT` and/or `OUTPUT` blocks if there isn't one or it's essentially stated in the first line of the documentation - I'm thinking of `_false_symbol` or `version`.  Up to you, of course, since you already did it.\n* In a few places where you have more than 'really basic and stupid' documentation (you sell yourself short! it's not bad at all) you have some lines that aren't going to work.  Ones like\n\n```\n- ``use_disk_cache`` - boolean (default: True); if set to True, try to read cached result from disk \n```\n\nare too long, and should be made into two lines like you did for \n\n```\n- ``eqns`` - a list of m strings; each representing a linear \nquestion in m = n variables \n```\n\nHowever, these will cause a problem in Sphinx, I think, unless you reformat them like so\n\n```\n- ``eqns`` - a list of m strings; each representing a linear \n  question in m = n variables \n```\n\nThis won't show up well on Trac, but notice that the 'q' in 'question' is lined up with the first '`' in '``eqns``'.  This was correctly done for 'pts_list', for example.\n\nIt looks like the `zunderflow zz` was fixed as well, and assuming that fix passes tests as well, I think it can be 'needs review'.  \n\nIn fact, as long as everyone involved is not reviewing their own patch, this can even be 'positive review'.  For instance, I will assume that JP slightly changing my reviewer patch indicates no problems with it.   \n\nCan anyone say what would still need to be done for positive review, other than passing all long doctests, which I can't check right now, and taking care of the things above which will lead to Sphinx errors?",
    "created_at": "2011-03-14T17:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61956",
    "user": "@kcrisman"
}
```

Sorry I do not have time to check this properly today.  Do you get the 

```
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
```

problem with these patches?  I hope not :)

A couple very small points about the doctests patch, which by the way is nontrivial and nice all by itself.
* You should have a `loads(dumps(foo))==foo` test if possible for class definitions.  I think there are eight of these? 
* You probably don't need to put `INPUT` and/or `OUTPUT` blocks if there isn't one or it's essentially stated in the first line of the documentation - I'm thinking of `_false_symbol` or `version`.  Up to you, of course, since you already did it.
* In a few places where you have more than 'really basic and stupid' documentation (you sell yourself short! it's not bad at all) you have some lines that aren't going to work.  Ones like

```
- ``use_disk_cache`` - boolean (default: True); if set to True, try to read cached result from disk 
```

are too long, and should be made into two lines like you did for 

```
- ``eqns`` - a list of m strings; each representing a linear 
question in m = n variables 
```

However, these will cause a problem in Sphinx, I think, unless you reformat them like so

```
- ``eqns`` - a list of m strings; each representing a linear 
  question in m = n variables 
```

This won't show up well on Trac, but notice that the 'q' in 'question' is lined up with the first '`' in '``eqns``'.  This was correctly done for 'pts_list', for example.

It looks like the `zunderflow zz` was fixed as well, and assuming that fix passes tests as well, I think it can be 'needs review'.  

In fact, as long as everyone involved is not reviewing their own patch, this can even be 'positive review'.  For instance, I will assume that JP slightly changing my reviewer patch indicates no problems with it.   

Can anyone say what would still need to be done for positive review, other than passing all long doctests, which I can't check right now, and taking care of the things above which will lead to Sphinx errors?



---

archive/issue_comments_061957.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-14T17:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61957",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061958.json:
```json
{
    "body": "> Can anyone say what would still need to be done for positive review, other than passing all long doctests, which I can't check right now, and taking care of the things above which will lead to Sphinx errors?\nSorry, and adding the loads/dumps tests, if they are possible.  Some should be, based on the discussion about pickling above and previous behavior working:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: loads(dumps(Maxima))==Maxima\nTrue\nsage: a = maxima(5)\nsage: type(a)\n<class 'sage.interfaces.maxima.MaximaElement'>\nsage: loads(dumps(a))==a\nTrue\n```\n",
    "created_at": "2011-03-14T17:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61958",
    "user": "@kcrisman"
}
```

> Can anyone say what would still need to be done for positive review, other than passing all long doctests, which I can't check right now, and taking care of the things above which will lead to Sphinx errors?
Sorry, and adding the loads/dumps tests, if they are possible.  Some should be, based on the discussion about pickling above and previous behavior working:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: loads(dumps(Maxima))==Maxima
True
sage: a = maxima(5)
sage: type(a)
<class 'sage.interfaces.maxima.MaximaElement'>
sage: loads(dumps(a))==a
True
```




---

archive/issue_comments_061959.json:
```json
{
    "body": "Replying to [comment:116 kcrisman]:\n\n> Sorry I do not have time to check this properly today.  Do you get the  ` ERROR: An unexpected error occurred while tokenizing input The following traceback may be corrupted or invalid ` problem with these patches?  I hope not :)\n\nI do not get that one.\n\n> A couple very small points about the doctests patch, which by the way is nontrivial and nice all by itself. * You should have a `loads(dumps(foo))==foo` test if possible for class definitions.  I think there are eight of these?  * You probably don't need to put `INPUT` and/or `OUTPUT` blocks if there isn't one or it's essentially stated in the first line of the documentation - I'm thinking of `_false_symbol` or `version`.  Up to you, of course, since you already did it. * In a few places where you have more than 'really basic and stupid' documentation (you sell yourself short! it's not bad at all) you have some lines that aren't going to work.  Ones like ` - use_disk_cache - boolean (default: True); if set to True, try to read cached result from disk  ` are too long, and should be made into two lines like you did for  ` - eqns - a list of m strings; each representing a linear  question in m = n variables  ` However, these will cause a problem in Sphinx, I think, unless you reformat them like so ` - eqns - a list of m strings; each representing a linear  question in m = n variables  ` This won't show up well on Trac, but notice that the 'q' in 'question' is lined up with the first '`' in '``eqns``'.  This was correctly done for 'pts_list', for example.\n\nI was not aware of line length limitation, I'll have a look at that tonight. For the eqns one, you are right, I just forgot to indent it correctly.\n\nFor the INPUT and OUTPUT blocks, I just tried to follow http://www.sagemath.org/doc/developer/conventions.html as much as possible to get something consistent even if it is often redundant or empty.\n\n> It looks like the `zunderflow zz` was fixed as well, and assuming that fix passes tests as well, I think it can be 'needs review'.   In fact, as long as everyone involved is not reviewing their own patch, this can even be 'positive review'.  For instance, I will assume that JP slightly changing my reviewer patch indicates no problems with it.    Can anyone say what would still need to be done for positive review, other than passing all long doctests, which I can't check right now, and taking care of the things above which will lead to Sphinx errors?\n\nIt is fixed because I changed the check to something else.\n\nThe real problem is that this test gives a somewhat random output according to when it is run.\n\nSo I guess the problem, if there is one, does not lie in the test used now, but in the implementation of the function itself.\n\nSee http://trac.sagemath.org/sage_trac/ticket/7377#comment:106 I guess we could open another ticket if we want to change the current behavior.",
    "created_at": "2011-03-14T17:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61959",
    "user": "jpflori"
}
```

Replying to [comment:116 kcrisman]:

> Sorry I do not have time to check this properly today.  Do you get the  ` ERROR: An unexpected error occurred while tokenizing input The following traceback may be corrupted or invalid ` problem with these patches?  I hope not :)

I do not get that one.

> A couple very small points about the doctests patch, which by the way is nontrivial and nice all by itself. * You should have a `loads(dumps(foo))==foo` test if possible for class definitions.  I think there are eight of these?  * You probably don't need to put `INPUT` and/or `OUTPUT` blocks if there isn't one or it's essentially stated in the first line of the documentation - I'm thinking of `_false_symbol` or `version`.  Up to you, of course, since you already did it. * In a few places where you have more than 'really basic and stupid' documentation (you sell yourself short! it's not bad at all) you have some lines that aren't going to work.  Ones like ` - use_disk_cache - boolean (default: True); if set to True, try to read cached result from disk  ` are too long, and should be made into two lines like you did for  ` - eqns - a list of m strings; each representing a linear  question in m = n variables  ` However, these will cause a problem in Sphinx, I think, unless you reformat them like so ` - eqns - a list of m strings; each representing a linear  question in m = n variables  ` This won't show up well on Trac, but notice that the 'q' in 'question' is lined up with the first '`' in '``eqns``'.  This was correctly done for 'pts_list', for example.

I was not aware of line length limitation, I'll have a look at that tonight. For the eqns one, you are right, I just forgot to indent it correctly.

For the INPUT and OUTPUT blocks, I just tried to follow http://www.sagemath.org/doc/developer/conventions.html as much as possible to get something consistent even if it is often redundant or empty.

> It looks like the `zunderflow zz` was fixed as well, and assuming that fix passes tests as well, I think it can be 'needs review'.   In fact, as long as everyone involved is not reviewing their own patch, this can even be 'positive review'.  For instance, I will assume that JP slightly changing my reviewer patch indicates no problems with it.    Can anyone say what would still need to be done for positive review, other than passing all long doctests, which I can't check right now, and taking care of the things above which will lead to Sphinx errors?

It is fixed because I changed the check to something else.

The real problem is that this test gives a somewhat random output according to when it is run.

So I guess the problem, if there is one, does not lie in the test used now, but in the implementation of the function itself.

See http://trac.sagemath.org/sage_trac/ticket/7377#comment:106 I guess we could open another ticket if we want to change the current behavior.



---

archive/issue_comments_061960.json:
```json
{
    "body": "> I was not aware of line length limitation, I'll have a look at that tonight. For the eqns one, you are right, I just forgot to indent it correctly.\nIt's not hard and fast, but it makes it so that when it shows up in a terminal window it doesn't look weird. \n> For the INPUT and OUTPUT blocks, I just tried to follow http://www.sagemath.org/doc/developer/conventions.html as much as possible to get something consistent even if it is often redundant or empty.\nMaybe we need to add something here about that...\n\n> It is fixed because I changed the check to something else.\nYes, I saw that the fix was the one you suggested earlier - sorry for not being clear about that.\n> The real problem is that this test gives a somewhat random output according to when it is run.\nWell, not too bad.  One would expect this, given the nature of the function.\n\nOkay, so I'll put this to 'needs work' and then hopefully it will be very easy to produce a p1 of the doctests patch that has the loads/dumps and fixes the other very minor issues.  I can try to review that patch tomorrow or Wednesday (US East Coast) and run tests.\n\nCan you think of anything that you have done that hasn't been positively reviewed by Nils or Francois?  It's a little hard to determine that from the comments.  At any rate this will be one of the better-tested major changes in how we interface to a sub-program, thanks to the long gestation period.",
    "created_at": "2011-03-14T17:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61960",
    "user": "@kcrisman"
}
```

> I was not aware of line length limitation, I'll have a look at that tonight. For the eqns one, you are right, I just forgot to indent it correctly.
It's not hard and fast, but it makes it so that when it shows up in a terminal window it doesn't look weird. 
> For the INPUT and OUTPUT blocks, I just tried to follow http://www.sagemath.org/doc/developer/conventions.html as much as possible to get something consistent even if it is often redundant or empty.
Maybe we need to add something here about that...

> It is fixed because I changed the check to something else.
Yes, I saw that the fix was the one you suggested earlier - sorry for not being clear about that.
> The real problem is that this test gives a somewhat random output according to when it is run.
Well, not too bad.  One would expect this, given the nature of the function.

Okay, so I'll put this to 'needs work' and then hopefully it will be very easy to produce a p1 of the doctests patch that has the loads/dumps and fixes the other very minor issues.  I can try to review that patch tomorrow or Wednesday (US East Coast) and run tests.

Can you think of anything that you have done that hasn't been positively reviewed by Nils or Francois?  It's a little hard to determine that from the comments.  At any rate this will be one of the better-tested major changes in how we interface to a sub-program, thanks to the long gestation period.



---

archive/issue_comments_061961.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-14T17:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61961",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061962.json:
```json
{
    "body": "> Okay, so I'll put this to 'needs work' and then hopefully it will be very easy to produce a p1 of the doctests patch \n\nFor you, I mean :) I don't have access to the computer where I tested all this right now, and unfortunately not time to do it on this one today.",
    "created_at": "2011-03-14T17:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61962",
    "user": "@kcrisman"
}
```

> Okay, so I'll put this to 'needs work' and then hopefully it will be very easy to produce a p1 of the doctests patch 

For you, I mean :) I don't have access to the computer where I tested all this right now, and unfortunately not time to do it on this one today.



---

archive/issue_comments_061963.json:
```json
{
    "body": "After applying the patches I am now getting:\n\n```\nsage -t -force_lib \"devel/sage-main/sage/symbolic/assumptions.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 89:\n    sage: decl2.assume()\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Assumption is inconsistent\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[7]>\", line 1, in <module>\n        decl2.assume()###line 89:\n    sage: decl2.assume()\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/assumptions.py\", line 104, in assume\n        maxima.eval(\"declare(%s, %s)\" % (repr(self._var), self._assumption))\n      File \"/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 395, in _eval_line\n        if statement: result = ((result + '\\n') if result else '') + max_to_string(maxima_eval(\"#$%s$\"%statement))\n      File \"ecl.pyx\", line 619, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:4422)\n      File \"ecl.pyx\", line 202, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:2606)\n    RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 294:\n    sage: sum(a*q^k, k, 0, oo)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Sum is divergent.\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[12]>\", line 1, in <module>\n        sum(a*q**k, k, Integer(0), oo)###line 294:\n    sage: sum(a*q^k, k, 0, oo)\n    NameError: name 'k' is not defined\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 300:\n    sage: sum(a*q^k, k, 0, oo)\nException raised:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[15]>\", line 1, in <module>\n        sum(a*q**k, k, Integer(0), oo)###line 300:\n    sage: sum(a*q^k, k, 0, oo)\n    NameError: name 'k' is not defined\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 340:\n    sage: assume(x,'odd')\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Assumption is inconsistent\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[32]>\", line 1, in <module>\n        assume(x,'odd')###line 340:\n    sage: assume(x,'odd')\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/assumptions.py\", line 390, in assume\n        x.assume()\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/assumptions.py\", line 104, in assume\n        maxima.eval(\"declare(%s, %s)\" % (repr(self._var), self._assumption))\n      File \"/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 395, in _eval_line\n        if statement: result = ((result + '\\n') if result else '') + max_to_string(maxima_eval(\"#$%s$\"%statement))\n      File \"ecl.pyx\", line 619, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:4422)\n      File \"ecl.pyx\", line 202, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:2606)\n    RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)\n**********************************************************************\n```\n\nand\n\n```\nsage -t -force_lib \"devel/sage-main/sage/symbolic/integration/integral.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py\", line 356:\n    sage: integrate(1/x^3,x,-1,3)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Integral is divergent.\nGot:\n    4/9\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py\", line 446:\n    sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):\n    Is  a  positive or negative?\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[47]>\", line 1, in <module>\n        integrate(Integer(1)/(x**Integer(3) *(a+b*x)**(Integer(1)/Integer(3))), x)###line 446:\n    sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)\n      File \"/usr/lib64/python2.6/site-packages/sage/misc/functional.py\", line 718, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 8188, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:31363)\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 601, in integrate\n        return indefinite_integral(expression, v)\n      File \"function.pyx\", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4504)\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 85, in _eval_\n        res = integrator(f, x)\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/integration/external.py\", line 19, in maxima_integrator\n        result = maxima.sr_integral(expression,v)\n      File \"/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 654, in sr_integral\n        raise ValueError, \"Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(\" + s[4:k] +\">0)', see `assume?` for more details)\\n\" + s\n    ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(a>0)', see `assume?` for more details)\n    Is  a  positive or negative?\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py\", line 484:\n    sage: res = integral(f,x,0.0001414, 1.); res\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: Computation failed since Maxima requested additional\n    constraints (try the command 'assume((y-1)*(y+1)>0)' before integral\n    or limit evaluation, for example):\n    Is  (y-1)*(y+1)  positive, negative, or zero?\nGot:\n    Traceback (most recent call last):\n      File \"/usr/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/usr/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[56]>\", line 1, in <module>\n        res = integral(f,x,RealNumber('0.0001414'), RealNumber('1.')); res###line 484:\n    sage: res = integral(f,x,0.0001414, 1.); res\n      File \"/usr/lib64/python2.6/site-packages/sage/misc/functional.py\", line 718, in integral\n        return x.integral(*args, **kwds)\n      File \"expression.pyx\", line 8188, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:31363)\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 603, in integrate\n        return definite_integral(expression, v, a, b)\n      File \"function.pyx\", line 414, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4443)\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py\", line 174, in _eval_\n        return integrator(*args)\n      File \"/usr/lib64/python2.6/site-packages/sage/symbolic/integration/external.py\", line 21, in maxima_integrator\n        result = maxima.sr_integral(expression, v, a, b)\n      File \"/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py\", line 654, in sr_integral\n        raise ValueError, \"Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(\" + s[4:k] +\">0)', see `assume?` for more details)\\n\" + s\n    ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume((y-1)*(y+1)>0)', see `assume?` for more details)\n    Is  (y-1)*(y+1)  positive, negative, or zero?\n```\n\nDid I forget a patch or somehow something didn't apply?",
    "created_at": "2011-03-15T01:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61963",
    "user": "@kiwifb"
}
```

After applying the patches I am now getting:

```
sage -t -force_lib "devel/sage-main/sage/symbolic/assumptions.py"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 89:
    sage: decl2.assume()
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Assumption is inconsistent
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[7]>", line 1, in <module>
        decl2.assume()###line 89:
    sage: decl2.assume()
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/assumptions.py", line 104, in assume
        maxima.eval("declare(%s, %s)" % (repr(self._var), self._assumption))
      File "/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 395, in _eval_line
        if statement: result = ((result + '\n') if result else '') + max_to_string(maxima_eval("#$%s$"%statement))
      File "ecl.pyx", line 619, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:4422)
      File "ecl.pyx", line 202, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:2606)
    RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 294:
    sage: sum(a*q^k, k, 0, oo)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Sum is divergent.
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[12]>", line 1, in <module>
        sum(a*q**k, k, Integer(0), oo)###line 294:
    sage: sum(a*q^k, k, 0, oo)
    NameError: name 'k' is not defined
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 300:
    sage: sum(a*q^k, k, 0, oo)
Exception raised:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[15]>", line 1, in <module>
        sum(a*q**k, k, Integer(0), oo)###line 300:
    sage: sum(a*q^k, k, 0, oo)
    NameError: name 'k' is not defined
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 340:
    sage: assume(x,'odd')
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Assumption is inconsistent
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[32]>", line 1, in <module>
        assume(x,'odd')###line 340:
    sage: assume(x,'odd')
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/assumptions.py", line 390, in assume
        x.assume()
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/assumptions.py", line 104, in assume
        maxima.eval("declare(%s, %s)" % (repr(self._var), self._assumption))
      File "/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 395, in _eval_line
        if statement: result = ((result + '\n') if result else '') + max_to_string(maxima_eval("#$%s$"%statement))
      File "ecl.pyx", line 619, in sage.libs.ecl.EclObject.__call__ (sage/libs/ecl.c:4422)
      File "ecl.pyx", line 202, in sage.libs.ecl.ecl_safe_apply (sage/libs/ecl.c:2606)
    RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)
**********************************************************************
```

and

```
sage -t -force_lib "devel/sage-main/sage/symbolic/integration/integral.py"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py", line 356:
    sage: integrate(1/x^3,x,-1,3)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Integral is divergent.
Got:
    4/9
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py", line 446:
    sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(a>0)' before integral or limit evaluation, for example):
    Is  a  positive or negative?
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[47]>", line 1, in <module>
        integrate(Integer(1)/(x**Integer(3) *(a+b*x)**(Integer(1)/Integer(3))), x)###line 446:
    sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)
      File "/usr/lib64/python2.6/site-packages/sage/misc/functional.py", line 718, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 8188, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:31363)
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py", line 601, in integrate
        return indefinite_integral(expression, v)
      File "function.pyx", line 419, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4504)
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py", line 85, in _eval_
        res = integrator(f, x)
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/integration/external.py", line 19, in maxima_integrator
        result = maxima.sr_integral(expression,v)
      File "/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 654, in sr_integral
        raise ValueError, "Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(" + s[4:k] +">0)', see `assume?` for more details)\n" + s
    ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(a>0)', see `assume?` for more details)
    Is  a  positive or negative?
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py", line 484:
    sage: res = integral(f,x,0.0001414, 1.); res
Expected:
    Traceback (most recent call last):
    ...
    TypeError: Computation failed since Maxima requested additional
    constraints (try the command 'assume((y-1)*(y+1)>0)' before integral
    or limit evaluation, for example):
    Is  (y-1)*(y+1)  positive, negative, or zero?
Got:
    Traceback (most recent call last):
      File "/usr/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/usr/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[56]>", line 1, in <module>
        res = integral(f,x,RealNumber('0.0001414'), RealNumber('1.')); res###line 484:
    sage: res = integral(f,x,0.0001414, 1.); res
      File "/usr/lib64/python2.6/site-packages/sage/misc/functional.py", line 718, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 8188, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:31363)
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py", line 603, in integrate
        return definite_integral(expression, v, a, b)
      File "function.pyx", line 414, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4443)
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/integration/integral.py", line 174, in _eval_
        return integrator(*args)
      File "/usr/lib64/python2.6/site-packages/sage/symbolic/integration/external.py", line 21, in maxima_integrator
        result = maxima.sr_integral(expression, v, a, b)
      File "/usr/lib64/python2.6/site-packages/sage/interfaces/maxima_lib.py", line 654, in sr_integral
        raise ValueError, "Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(" + s[4:k] +">0)', see `assume?` for more details)\n" + s
    ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume((y-1)*(y+1)>0)', see `assume?` for more details)
    Is  (y-1)*(y+1)  positive, negative, or zero?
```

Did I forget a patch or somehow something didn't apply?



---

archive/issue_comments_061964.json:
```json
{
    "body": "Replying to [comment:121 fbissey]:\n> After applying the patches I am now getting:\n\nThank you so much!  I knew I was tired when I made that patch, hence it not being quite ready for prime time.  To be fair, I warned of this.  But it shouldn't be too bad to make a p3 of it.\n\n{{[\n> sage -t -force_lib \"devel/sage-main/sage/symbolic/assumptions.py\"\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 89:\n>     sage: decl2.assume()\n> Expected:\n>     Traceback (most recent call last):\n>     ...\n>     ValueError: Assumption is inconsistent\n>     RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 340:\n>     sage: assume(x,'odd')\n> Expected:\n>     Traceback (most recent call last):\n>     ...\n>     ValueError: Assumption is inconsistent\n>     RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)\n> **********************************************************************\n}}}\nIn this case, the new message is just as informative as the old one (though longer).  So we could just replace all of those and remove the catch for inconsistent declarations in the code, I guess.\n\n```\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 294:\n>     sage: sum(a*q^k, k, 0, oo)\n>     NameError: name 'k' is not defined\n```\n\nOops.  Sorry.  Same for the next one.\n\n```\n> File \"/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py\", line 300:\n>     sage: sum(a*q^k, k, 0, oo)\n>     NameError: name 'k' is not defined\n```\n\nThis is interesting.  That means we can't just remove the piece about this in the integration code, as I thought.  Since ECL returns the divergent error, it seemed like we could, but apparently skipping the error still outputs the principal value.  I would need someone with knowledge of how the new interface works to figure out how to make sure this reports an error.\n\n```\n> sage -t -force_lib \"devel/sage-main/sage/symbolic/integration/integral.py\"\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py\", line 356:\n>     sage: integrate(1/x^3,x,-1,3)\n> Expected:\n>     Traceback (most recent call last):\n>     ...\n>     ValueError: Integral is divergent.\n> Got:\n>     4/9\n```\n\nSame thing for this one - we are catching it, but it still prints the question.  How do we make sure it doesn't do that?  I don't think it did that before, so it may be one of the apparently-not-innocuous things JP removed in the last patch.\n\n```\n>     sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)\n>     ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(a>0)', see `assume?` for more details)\n>     Is  a  positive or negative?\n> **********************************************************************\n> File \"/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py\", line 484:\n>     sage: res = integral(f,x,0.0001414, 1.); res\n>     ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume((y-1)*(y+1)>0)', see `assume?` for more details)\n>     Is  (y-1)*(y+1)  positive, negative, or zero?\n```\n",
    "created_at": "2011-03-15T03:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61964",
    "user": "@kcrisman"
}
```

Replying to [comment:121 fbissey]:
> After applying the patches I am now getting:

Thank you so much!  I knew I was tired when I made that patch, hence it not being quite ready for prime time.  To be fair, I warned of this.  But it shouldn't be too bad to make a p3 of it.

{{[
> sage -t -force_lib "devel/sage-main/sage/symbolic/assumptions.py"
> **********************************************************************
> File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 89:
>     sage: decl2.assume()
> Expected:
>     Traceback (most recent call last):
>     ...
>     ValueError: Assumption is inconsistent
>     RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)
> **********************************************************************
> File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 340:
>     sage: assume(x,'odd')
> Expected:
>     Traceback (most recent call last):
>     ...
>     ValueError: Assumption is inconsistent
>     RuntimeError: ECL says: Error executing code in Maxima: declare: inconsistent declaration declare(x,odd)
> **********************************************************************
}}}
In this case, the new message is just as informative as the old one (though longer).  So we could just replace all of those and remove the catch for inconsistent declarations in the code, I guess.

```
> **********************************************************************
> File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 294:
>     sage: sum(a*q^k, k, 0, oo)
>     NameError: name 'k' is not defined
```

Oops.  Sorry.  Same for the next one.

```
> File "/usr/share/sage/devel/sage-main/sage/symbolic/assumptions.py", line 300:
>     sage: sum(a*q^k, k, 0, oo)
>     NameError: name 'k' is not defined
```

This is interesting.  That means we can't just remove the piece about this in the integration code, as I thought.  Since ECL returns the divergent error, it seemed like we could, but apparently skipping the error still outputs the principal value.  I would need someone with knowledge of how the new interface works to figure out how to make sure this reports an error.

```
> sage -t -force_lib "devel/sage-main/sage/symbolic/integration/integral.py"
> **********************************************************************
> File "/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py", line 356:
>     sage: integrate(1/x^3,x,-1,3)
> Expected:
>     Traceback (most recent call last):
>     ...
>     ValueError: Integral is divergent.
> Got:
>     4/9
```

Same thing for this one - we are catching it, but it still prints the question.  How do we make sure it doesn't do that?  I don't think it did that before, so it may be one of the apparently-not-innocuous things JP removed in the last patch.

```
>     sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)
>     ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume(a>0)', see `assume?` for more details)
>     Is  a  positive or negative?
> **********************************************************************
> File "/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py", line 484:
>     sage: res = integral(f,x,0.0001414, 1.); res
>     ValueError: Computation failed since Maxima requested additional constraints; using the 'assume' command before integral evaluation *may* help (example of legal syntax is 'assume((y-1)*(y+1)>0)', see `assume?` for more details)
>     Is  (y-1)*(y+1)  positive, negative, or zero?
```




---

archive/issue_comments_061965.json:
```json
{
    "body": "Attachment [trac_7377-assumptions-p3.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-assumptions-p3.patch) by jpflori created at 2011-03-15 09:33:18\n\nMore fixes",
    "created_at": "2011-03-15T09:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61965",
    "user": "jpflori"
}
```

Attachment [trac_7377-assumptions-p3.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-assumptions-p3.patch) by jpflori created at 2011-03-15 09:33:18

More fixes



---

archive/issue_comments_061966.json:
```json
{
    "body": "Updated doctests.",
    "created_at": "2011-03-15T13:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61966",
    "user": "jpflori"
}
```

Updated doctests.



---

archive/issue_comments_061967.json:
```json
{
    "body": "Attachment [trac_7377-doctests-p1.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests-p1.patch) by jpflori created at 2011-03-15 13:08:08\n\nI uploaded updated versions of both last patches. I accidently deleted two lines in the previous one which cause the principal error, they are restored now. I added pickling tests, not sure they make sense. Also some various fixes and cosmetic changes to reduce line lengths for sphynx and readibility.\n\nAfterwards \"make ptestlong\" reported no errors on my computer.\n\nDon't know if someone already took a look at what I did to split Interface class out of Expect class.\n\nIt seems functional now, but maybe I left some mistakes there.",
    "created_at": "2011-03-15T13:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61967",
    "user": "jpflori"
}
```

Attachment [trac_7377-doctests-p1.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests-p1.patch) by jpflori created at 2011-03-15 13:08:08

I uploaded updated versions of both last patches. I accidently deleted two lines in the previous one which cause the principal error, they are restored now. I added pickling tests, not sure they make sense. Also some various fixes and cosmetic changes to reduce line lengths for sphynx and readibility.

Afterwards "make ptestlong" reported no errors on my computer.

Don't know if someone already took a look at what I did to split Interface class out of Expect class.

It seems functional now, but maybe I left some mistakes there.



---

archive/issue_comments_061968.json:
```json
{
    "body": "Thanks, JP - I was planning on making the fixes today, but you beat me to it.  They were all oversights of mine, except...\n\n> I uploaded updated versions of both last patches. I accidently deleted two lines in the previous one which cause the principal error, they are restored now. \n\nAh, I wondered if that ecl principal value thing was important.\n\n>I added pickling tests, not sure they make sense. \n\nI don't know if they do either, but this is one of the things Sage has come to a consensus on, for better or for worse.  Some were already there, as it turned out - in the `__init__`, not class definition - but doesn't hurt to have the others.\n\n>Also some various fixes and cosmetic changes to reduce line lengths for sphynx and readibility.\n\nI'll check that all out next, after running my own tests.  There is one final 'evalutation' that I should be able to fix very easily.\n\n> \n> Afterwards \"make ptestlong\" reported no errors on my computer.\n> \n> Don't know if someone already took a look at what I did to split Interface class out of Expect class.\n\nI'll try to look at it, but I fear there is a little too much ECL there for me to feel comfortable reviewing that.\n\n> It seems functional now, but maybe I left some mistakes there.\n\nMaybe Francois can then give positive review :)\n\nI should point out that if this depends on #10743, in principle this ticket's positive review wouldn't be very useful until that one is reviewed.",
    "created_at": "2011-03-15T13:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61968",
    "user": "@kcrisman"
}
```

Thanks, JP - I was planning on making the fixes today, but you beat me to it.  They were all oversights of mine, except...

> I uploaded updated versions of both last patches. I accidently deleted two lines in the previous one which cause the principal error, they are restored now. 

Ah, I wondered if that ecl principal value thing was important.

>I added pickling tests, not sure they make sense. 

I don't know if they do either, but this is one of the things Sage has come to a consensus on, for better or for worse.  Some were already there, as it turned out - in the `__init__`, not class definition - but doesn't hurt to have the others.

>Also some various fixes and cosmetic changes to reduce line lengths for sphynx and readibility.

I'll check that all out next, after running my own tests.  There is one final 'evalutation' that I should be able to fix very easily.

> 
> Afterwards "make ptestlong" reported no errors on my computer.
> 
> Don't know if someone already took a look at what I did to split Interface class out of Expect class.

I'll try to look at it, but I fear there is a little too much ECL there for me to feel comfortable reviewing that.

> It seems functional now, but maybe I left some mistakes there.

Maybe Francois can then give positive review :)

I should point out that if this depends on #10743, in principle this ticket's positive review wouldn't be very useful until that one is reviewed.



---

archive/issue_comments_061969.json:
```json
{
    "body": "Updated to fix two trivial typos",
    "created_at": "2011-03-15T17:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61969",
    "user": "@kcrisman"
}
```

Updated to fix two trivial typos



---

archive/issue_comments_061970.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-15T17:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61970",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061971.json:
```json
{
    "body": "Attachment [trac_7377-doctests-p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests-p2.patch) by @kcrisman created at 2011-03-15 17:24:52\n\nCoverage is great, I haven't tested formatting in built html but looks like it will be fine overall, and in general very impressive work here.  The refactoring is at least working well with the interfaces in doctesting; it would be nice to have more testing of that by heavy users of (say) R or GAP, but at the very least we can set to 'needs review'.",
    "created_at": "2011-03-15T17:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61971",
    "user": "@kcrisman"
}
```

Attachment [trac_7377-doctests-p2.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests-p2.patch) by @kcrisman created at 2011-03-15 17:24:52

Coverage is great, I haven't tested formatting in built html but looks like it will be fine overall, and in general very impressive work here.  The refactoring is at least working well with the interfaces in doctesting; it would be nice to have more testing of that by heavy users of (say) R or GAP, but at the very least we can set to 'needs review'.



---

archive/issue_comments_061972.json:
```json
{
    "body": "Okay, the HTML docs look fine in general.  Good catch on a few of the indentations that were incorrect before in any case.  \n\n```\n   1.\n\n      Sage can currently only understand a subset of the output of Maxima,\n\n      Maple and Mathematica, so even if the chosen backend can perform\n\n      the summation the result might not be convertable into a Sage\n\n      expression.\n```\n\nshouldn't be double-spaced, but this is not really a big deal because it still looks ok.\n\nMore importantly, but still not enough to stop positive review, is the fact that the new files are not in the documentation!  We will need to fix `interfaces.rst` in the sage/doc/en/ folder to be accurate, as well as to include the new `sage/interfaces/maxima_lib`, `sage/interfaces/maxima_abstract`, and `sage/interfaces/interface` documentation.  This is now #10942.",
    "created_at": "2011-03-15T19:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61972",
    "user": "@kcrisman"
}
```

Okay, the HTML docs look fine in general.  Good catch on a few of the indentations that were incorrect before in any case.  

```
   1.

      Sage can currently only understand a subset of the output of Maxima,

      Maple and Mathematica, so even if the chosen backend can perform

      the summation the result might not be convertable into a Sage

      expression.
```

shouldn't be double-spaced, but this is not really a big deal because it still looks ok.

More importantly, but still not enough to stop positive review, is the fact that the new files are not in the documentation!  We will need to fix `interfaces.rst` in the sage/doc/en/ folder to be accurate, as well as to include the new `sage/interfaces/maxima_lib`, `sage/interfaces/maxima_abstract`, and `sage/interfaces/interface` documentation.  This is now #10942.



---

archive/issue_comments_061973.json:
```json
{
    "body": "All done the long tests passed with flying colors. No more problems for me, I am happy with it.",
    "created_at": "2011-03-15T21:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61973",
    "user": "@kiwifb"
}
```

All done the long tests passed with flying colors. No more problems for me, I am happy with it.



---

archive/issue_comments_061974.json:
```json
{
    "body": "It's embarrassing I hadn't recompiled with the patches in. Re-running the long test now.",
    "created_at": "2011-03-16T02:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61974",
    "user": "@kiwifb"
}
```

It's embarrassing I hadn't recompiled with the patches in. Re-running the long test now.



---

archive/issue_comments_061975.json:
```json
{
    "body": "I had made some extra comments yesterday but obviously it was during the time trac was having a fit. So I'll repeat. I have one failing test left\n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/symbolic/integration/integral.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py\", line 359:\n    sage: integrate(1/x^3,x,-1,3)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Integral is divergent.\nGot:\n    4/9\n**********************************************************************\n```\n",
    "created_at": "2011-03-16T22:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61975",
    "user": "@kiwifb"
}
```

I had made some extra comments yesterday but obviously it was during the time trac was having a fit. So I'll repeat. I have one failing test left

```
sage -t -long -force_lib "devel/sage-main/sage/symbolic/integration/integral.py"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/symbolic/integration/integral.py", line 359:
    sage: integrate(1/x^3,x,-1,3)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Integral is divergent.
Got:
    4/9
**********************************************************************
```




---

archive/issue_comments_061976.json:
```json
{
    "body": "Hmm, that shouldn't be failing now that JP put that back in - it was fine for me.  Did you use attachment:trac_7377-doctests-p1.patch or attachment:trac_7377-doctests-p2.patch (either of these should be fine) instead of attachment:trac_7377-doctests.patch (bad)?",
    "created_at": "2011-03-16T23:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61976",
    "user": "@kcrisman"
}
```

Hmm, that shouldn't be failing now that JP put that back in - it was fine for me.  Did you use attachment:trac_7377-doctests-p1.patch or attachment:trac_7377-doctests-p2.patch (either of these should be fine) instead of attachment:trac_7377-doctests.patch (bad)?



---

archive/issue_comments_061977.json:
```json
{
    "body": "Replying to [comment:130 kcrisman]:\n> Hmm, that shouldn't be failing now that JP put that back in - it was fine for me.  Did you use attachment:trac_7377-doctests-p1.patch or attachment:trac_7377-doctests-p2.patch (either of these should be fine) instead of attachment:trac_7377-doctests.patch (bad)?\n\nNot sure what the problem was. I did a bit of rewriting on how I apply the patches in sage-on-gentoo to make it a bit more transparent. Reapplied all the patches, rebuild and now the test looks fine\n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/symbolic/integration/integral.py\"\n         [4.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.6 seconds\n```\n\nSo I am OK with it :)\nAt last!",
    "created_at": "2011-03-17T01:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61977",
    "user": "@kiwifb"
}
```

Replying to [comment:130 kcrisman]:
> Hmm, that shouldn't be failing now that JP put that back in - it was fine for me.  Did you use attachment:trac_7377-doctests-p1.patch or attachment:trac_7377-doctests-p2.patch (either of these should be fine) instead of attachment:trac_7377-doctests.patch (bad)?

Not sure what the problem was. I did a bit of rewriting on how I apply the patches in sage-on-gentoo to make it a bit more transparent. Reapplied all the patches, rebuild and now the test looks fine

```
sage -t -long -force_lib "devel/sage-main/sage/symbolic/integration/integral.py"
         [4.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.6 seconds
```

So I am OK with it :)
At last!



---

archive/issue_comments_061978.json:
```json
{
    "body": "It looks like then the only thing that remains is to officially review JP's refactoring of expect/interface and !maxima_abstract/maxima/maxima_lib.  I am comfortable with it, and have checked the outlines of the refactoring which are more than satisfactory, but simply have not had the time (and will not) to go over that with a fine-toothed comb to check whether there is some missing function.  \n\nPresumably not!  Since we never remove doctests, right?  So in my opinion it's ready for positive review, since the interfaces to GAP and R and Pari etc. are used heavily elsewhere in Sage, so it's not like the interface stuff isn't tested (not to mention the Maxima stuff, of course, but that is not what is at issue here).  Still, maybe someone else wants to comment on this.  Otherwise we should be sure we get this in 4.7, before bitrot sets in.",
    "created_at": "2011-03-17T01:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61978",
    "user": "@kcrisman"
}
```

It looks like then the only thing that remains is to officially review JP's refactoring of expect/interface and !maxima_abstract/maxima/maxima_lib.  I am comfortable with it, and have checked the outlines of the refactoring which are more than satisfactory, but simply have not had the time (and will not) to go over that with a fine-toothed comb to check whether there is some missing function.  

Presumably not!  Since we never remove doctests, right?  So in my opinion it's ready for positive review, since the interfaces to GAP and R and Pari etc. are used heavily elsewhere in Sage, so it's not like the interface stuff isn't tested (not to mention the Maxima stuff, of course, but that is not what is at issue here).  Still, maybe someone else wants to comment on this.  Otherwise we should be sure we get this in 4.7, before bitrot sets in.



---

archive/issue_comments_061979.json:
```json
{
    "body": "The principal stuff should indeed be ok with the doctests p1 or p2 patch.\n\nFor patchbot which does not seem to read or understand the desciption:\n\nDepends on #10766, #10773, #10743. Ticket #10818 is desirable but not essential.\n Apply trac_7377-abstract-maxima_p2.patch, trac_7377-maximalib_p2.patch, trac_7377-fastcalculus_p2.patch, trac_7377-better-ask-error_p2.patch, trac_7377-split_and_refactor-p2.patch, trac_7377-lazy-maxlib.p2.patch, trac_7377-floatcast.patch, trac_7377-unicode_to_ecl-p1.patch, trac_7377-assumptions-p3.patch, trac_7377-doctests-p2.patch",
    "created_at": "2011-03-17T08:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61979",
    "user": "jpflori"
}
```

The principal stuff should indeed be ok with the doctests p1 or p2 patch.

For patchbot which does not seem to read or understand the desciption:

Depends on #10766, #10773, #10743. Ticket #10818 is desirable but not essential.
 Apply trac_7377-abstract-maxima_p2.patch, trac_7377-maximalib_p2.patch, trac_7377-fastcalculus_p2.patch, trac_7377-better-ask-error_p2.patch, trac_7377-split_and_refactor-p2.patch, trac_7377-lazy-maxlib.p2.patch, trac_7377-floatcast.patch, trac_7377-unicode_to_ecl-p1.patch, trac_7377-assumptions-p3.patch, trac_7377-doctests-p2.patch



---

archive/issue_comments_061980.json:
```json
{
    "body": "Let's try a bit of cleaning.",
    "created_at": "2011-03-17T08:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61980",
    "user": "@kiwifb"
}
```

Let's try a bit of cleaning.



---

archive/issue_comments_061981.json:
```json
{
    "body": "I would definitely give the bits I haven't written a positive review. Great work, JP and KDC! Thank you very much for finishing off this project. Your knowledge of the system was definitely required to get the last bits right.",
    "created_at": "2011-03-19T20:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61981",
    "user": "@nbruin"
}
```

I would definitely give the bits I haven't written a positive review. Great work, JP and KDC! Thank you very much for finishing off this project. Your knowledge of the system was definitely required to get the last bits right.



---

archive/issue_comments_061982.json:
```json
{
    "body": "I am adding Karl to the list of authors, do a little fiddling and take the responsibility of switching that to positive review. I think we have a large consensus among the people involved that this works. Now is the time to have a bigger test.",
    "created_at": "2011-03-19T21:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61982",
    "user": "@kiwifb"
}
```

I am adding Karl to the list of authors, do a little fiddling and take the responsibility of switching that to positive review. I think we have a large consensus among the people involved that this works. Now is the time to have a bigger test.



---

archive/issue_comments_061983.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-19T21:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61983",
    "user": "@kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061984.json:
```json
{
    "body": "That is extremely gracious of you - I don't feel like I did much.  I definitely agree about the consensus and time to have a bigger test.  Hopefully it will end up in alpha2 or alpha3.",
    "created_at": "2011-03-20T00:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61984",
    "user": "@kcrisman"
}
```

That is extremely gracious of you - I don't feel like I did much.  I definitely agree about the consensus and time to have a bigger test.  Hopefully it will end up in alpha2 or alpha3.



---

archive/issue_comments_061985.json:
```json
{
    "body": "Replying to [comment:137 kcrisman]:\n> That is extremely gracious of you - I don't feel like I did much.  I definitely agree about the consensus and time to have a bigger test.  Hopefully it will end up in alpha2 or alpha3.\n\nNot at all. You contributed, even if it has been revised by someone else afterwards. I doubt very much it will be in alpha2. I think (gut feeling) that Jeroen wants to have alpha2 out soon and won't add something that will delay it further.\n\nI am not sure about alpha3 either, it is a big change. He may object to it for 4.7 altogether. In any case we'll be ready to be picked up at the next opportunity.",
    "created_at": "2011-03-20T00:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61985",
    "user": "@kiwifb"
}
```

Replying to [comment:137 kcrisman]:
> That is extremely gracious of you - I don't feel like I did much.  I definitely agree about the consensus and time to have a bigger test.  Hopefully it will end up in alpha2 or alpha3.

Not at all. You contributed, even if it has been revised by someone else afterwards. I doubt very much it will be in alpha2. I think (gut feeling) that Jeroen wants to have alpha2 out soon and won't add something that will delay it further.

I am not sure about alpha3 either, it is a big change. He may object to it for 4.7 altogether. In any case we'll be ready to be picked up at the next opportunity.



---

archive/issue_comments_061986.json:
```json
{
    "body": "Added Robert Bradshaw to authors. He did the original splitting of the maxima_abstract interface, which was instrumental to making this project doable. JP can probably judge how much of Robert's work remained after his refactoring and is welcome to reverse this change if he feels that to be appropriate.",
    "created_at": "2011-03-30T11:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61986",
    "user": "@nbruin"
}
```

Added Robert Bradshaw to authors. He did the original splitting of the maxima_abstract interface, which was instrumental to making this project doable. JP can probably judge how much of Robert's work remained after his refactoring and is welcome to reverse this change if he feels that to be appropriate.



---

archive/issue_comments_061987.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-01T12:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61987",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_061988.json:
```json
{
    "body": "Please rebase:\n\n```\napplying /scratch/jdemeyer/merger/downloads/trac_7377-split_and_refactor-p2.patch\npatching file sage/interfaces/expect.py\nHunk #13 FAILED at 1025\nHunk #17 FAILED at 1285\nHunk #18 FAILED at 1339\n```\n",
    "created_at": "2011-04-01T12:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61988",
    "user": "@jdemeyer"
}
```

Please rebase:

```
applying /scratch/jdemeyer/merger/downloads/trac_7377-split_and_refactor-p2.patch
patching file sage/interfaces/expect.py
Hunk #13 FAILED at 1025
Hunk #17 FAILED at 1285
Hunk #18 FAILED at 1339
```




---

archive/issue_comments_061989.json:
```json
{
    "body": "I rebased the patches against sage 4.7.alpha3.\nI could run make ptestlong yet because upgrade from 4.6.2 failed (givaro problem) and the binary provided for 4.7.alpha3 would not run (some liblapack problem).\nHowever it should apply cleanly.\nI'm building 4.7.alpha3 from source and will test when finished.",
    "created_at": "2011-04-01T15:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61989",
    "user": "jpflori"
}
```

I rebased the patches against sage 4.7.alpha3.
I could run make ptestlong yet because upgrade from 4.6.2 failed (givaro problem) and the binary provided for 4.7.alpha3 would not run (some liblapack problem).
However it should apply cleanly.
I'm building 4.7.alpha3 from source and will test when finished.



---

archive/issue_comments_061990.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-01T15:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61990",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061991.json:
```json
{
    "body": "After applying this patch, everything compiles but Sage doesn't run properly:\n\n```\n$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n| Sage Version 4.7.alpha0, Release Date: 2011-03-04                  |\n| Type notebook() for the GUI, and license() for information.        |\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67\n     68\n\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ipy_profile_sage.py in <module>()\n      5     preparser(True)\n      6\n----> 7     import sage.all_cmdline\n      8     sage.all_cmdline._init_cmdline(globals())\n      9\n\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13\n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/all.py in <module>()\n     57 from time                import sleep\n     58\n---> 59 from sage.misc.all       import *         # takes a while\n     60\n     61 from sage.misc.sh import sh\n\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/misc/all.py in <module>()\n     77 from func_persist import func_persist\n     78\n---> 79 from functional import (additive_order,\n     80                         sqrt as numerical_sqrt,\n     81                         arg,\n\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/misc/functional.py in <module>()\n     32 import sage.misc.latex\n     33 import sage.server.support\n---> 34 import sage.interfaces.expect\n     35 import sage.interfaces.mathematica\n     36\n\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.py in <module>()\n     56 import pexpect\n     57 from pexpect import ExceptionPexpect\n---> 58 from sage.interfaces.interface import Interface, InterfaceElement, InterfaceFunction, InterfaceFunctionElement, AsciiArtString\n     59\n     60 from sage.structure.sage_object import SageObject\n\nImportError: No module named interface\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n\nsage:\n```\n",
    "created_at": "2011-04-04T08:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61991",
    "user": "@jdemeyer"
}
```

After applying this patch, everything compiles but Sage doesn't run properly:

```
$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
| Sage Version 4.7.alpha0, Release Date: 2011-03-04                  |
| Type notebook() for the GUI, and license() for information.        |
/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67
     68

/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9

/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/all.py in <module>()
     57 from time                import sleep
     58
---> 59 from sage.misc.all       import *         # takes a while
     60
     61 from sage.misc.sh import sh

/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/misc/all.py in <module>()
     77 from func_persist import func_persist
     78
---> 79 from functional import (additive_order,
     80                         sqrt as numerical_sqrt,
     81                         arg,

/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/misc/functional.py in <module>()
     32 import sage.misc.latex
     33 import sage.server.support
---> 34 import sage.interfaces.expect
     35 import sage.interfaces.mathematica
     36

/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.py in <module>()
     56 import pexpect
     57 from pexpect import ExceptionPexpect
---> 58 from sage.interfaces.interface import Interface, InterfaceElement, InterfaceFunction, InterfaceFunctionElement, AsciiArtString
     59
     60 from sage.structure.sage_object import SageObject

ImportError: No module named interface
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

sage:
```




---

archive/issue_comments_061992.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-04T08:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61992",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061993.json:
```json
{
    "body": "interface.py is missing in the trac_7377-split_and_refactor-p3.patch, it must have been overlooked. That's the cause of the problem.",
    "created_at": "2011-04-04T10:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61993",
    "user": "@kiwifb"
}
```

interface.py is missing in the trac_7377-split_and_refactor-p3.patch, it must have been overlooked. That's the cause of the problem.



---

archive/issue_comments_061994.json:
```json
{
    "body": "Attachment [trac_7377-doctests-p3.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests-p3.patch) by jpflori created at 2011-04-04 10:47:30\n\nRebased on Sage 4.7.alpha3, put back forgotten interface.py",
    "created_at": "2011-04-04T10:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61994",
    "user": "jpflori"
}
```

Attachment [trac_7377-doctests-p3.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-doctests-p3.patch) by jpflori created at 2011-04-04 10:47:30

Rebased on Sage 4.7.alpha3, put back forgotten interface.py



---

archive/issue_comments_061995.json:
```json
{
    "body": "Currently, there is a patch at #10818 (ECL interrupts) which needs review.  Is anyone able to review that?",
    "created_at": "2011-04-04T20:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61995",
    "user": "@jdemeyer"
}
```

Currently, there is a patch at #10818 (ECL interrupts) which needs review.  Is anyone able to review that?



---

archive/issue_comments_061996.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-04T20:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61996",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061997.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-05T07:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61997",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061998.json:
```json
{
    "body": "Doctest failures most likely caused by this patch:\n\n```\nsage -t  -force_lib devel/sage/sage/misc/sage_eval.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/devel/sage-main/sage/misc/sage_eval.py\", line 237:\n    sage: a._sage_()\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[12]>\", line 1, in <module>\n        a._sage_()###line 237:\n    sage: a._sage_()\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/interfaces/interface.py\", line 855, in _sage_\n        raise NotImplementedError, \"Unable to parse output: %s\" % string\n    NotImplementedError: Unable to parse output: 313131/811\n**********************************************************************\n```\n\n\n```\nsage -t  -force_lib devel/sage/sage/groups/perm_gps/permgroup.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/devel/sage-main/sage/groups/perm_gps/permgroup.py\", line 881:\n    sage: G.orbits()\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_26[3]>\", line 1, in <module>\n        G.orbits()###line 881:\n    sage: G.orbits()\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/misc/cachefunc.py\", line 555, in __call__\n        w = self._cachedmethod._instance_call(self._instance, *args, **kwds)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/misc/cachefunc.py\", line 778, in _instance_call\n        return self._cachedfunc.f(inst, *args, **kwds)\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/groups/perm_gps/permgroup.py\", line 896, in orbits\n        return self._gap_().Orbits(\"[1..%d]\" % self.largest_moved_point()).sage()\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/interfaces/interface.py\", line 869, in sage\n        return self._sage_()\n      File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/interfaces/interface.py\", line 855, in _sage_\n        raise NotImplementedError, \"Unable to parse output: %s\" % string\n    NotImplementedError: Unable to parse output: [ [ 1, 3, 4 ], [ 2 ] ]\n**********************************************************************\n[...lots more...]\n```\n",
    "created_at": "2011-04-05T07:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61998",
    "user": "@jdemeyer"
}
```

Doctest failures most likely caused by this patch:

```
sage -t  -force_lib devel/sage/sage/misc/sage_eval.py
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/devel/sage-main/sage/misc/sage_eval.py", line 237:
    sage: a._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[12]>", line 1, in <module>
        a._sage_()###line 237:
    sage: a._sage_()
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/interfaces/interface.py", line 855, in _sage_
        raise NotImplementedError, "Unable to parse output: %s" % string
    NotImplementedError: Unable to parse output: 313131/811
**********************************************************************
```


```
sage -t  -force_lib devel/sage/sage/groups/perm_gps/permgroup.py
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/devel/sage-main/sage/groups/perm_gps/permgroup.py", line 881:
    sage: G.orbits()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_26[3]>", line 1, in <module>
        G.orbits()###line 881:
    sage: G.orbits()
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/misc/cachefunc.py", line 555, in __call__
        w = self._cachedmethod._instance_call(self._instance, *args, **kwds)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/misc/cachefunc.py", line 778, in _instance_call
        return self._cachedfunc.f(inst, *args, **kwds)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/groups/perm_gps/permgroup.py", line 896, in orbits
        return self._gap_().Orbits("[1..%d]" % self.largest_moved_point()).sage()
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/interfaces/interface.py", line 869, in sage
        return self._sage_()
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha4/local/lib/python/site-packages/sage/interfaces/interface.py", line 855, in _sage_
        raise NotImplementedError, "Unable to parse output: %s" % string
    NotImplementedError: Unable to parse output: [ [ 1, 3, 4 ], [ 2 ] ]
**********************************************************************
[...lots more...]
```




---

archive/issue_comments_061999.json:
```json
{
    "body": "Got the same failures here.",
    "created_at": "2011-04-05T08:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-61999",
    "user": "@kiwifb"
}
```

Got the same failures here.



---

archive/issue_comments_062000.json:
```json
{
    "body": "That's because of split_and_refactor (at least from p2, strange it did not occur before).\nHopefully I fixed it.\nI'm currently trying to run make ptestlong.\nI'll post the patch this afternoon.",
    "created_at": "2011-04-05T08:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62000",
    "user": "jpflori"
}
```

That's because of split_and_refactor (at least from p2, strange it did not occur before).
Hopefully I fixed it.
I'm currently trying to run make ptestlong.
I'll post the patch this afternoon.



---

archive/issue_comments_062001.json:
```json
{
    "body": "Attachment [trac_7377-split_and_refactor-p3.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-split_and_refactor-p3.patch) by jpflori created at 2011-04-05 11:05:37\n\nRebased on Sage 4.7.alpha3, put back forgotten interface.py",
    "created_at": "2011-04-05T11:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62001",
    "user": "jpflori"
}
```

Attachment [trac_7377-split_and_refactor-p3.patch](tarball://root/attachments/some-uuid/ticket7377/trac_7377-split_and_refactor-p3.patch) by jpflori created at 2011-04-05 11:05:37

Rebased on Sage 4.7.alpha3, put back forgotten interface.py



---

archive/issue_comments_062002.json:
```json
{
    "body": "It should be ok now. It applied against 4.7.alpha3 and ran make ptestlong:\n\n\n```\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2519.7 seconds\n```\n",
    "created_at": "2011-04-05T11:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62002",
    "user": "jpflori"
}
```

It should be ok now. It applied against 4.7.alpha3 and ran make ptestlong:


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2519.7 seconds
```




---

archive/issue_comments_062003.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-05T11:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62003",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062004.json:
```json
{
    "body": "I was finally able to build 4.7.alpha3 from source (previous test was with prebuilt binary) and encountered no problem either.\n\n\n```\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2601.1 seconds\n```\n",
    "created_at": "2011-04-06T08:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62004",
    "user": "jpflori"
}
```

I was finally able to build 4.7.alpha3 from source (previous test was with prebuilt binary) and encountered no problem either.


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2601.1 seconds
```




---

archive/issue_comments_062005.json:
```json
{
    "body": "I did a new build against 4.7.alpha3 as well. And finally managed to test it.\nSo I am putting this back to positive review. Hopefully it won't be in vain.",
    "created_at": "2011-04-06T09:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62005",
    "user": "@kiwifb"
}
```

I did a new build against 4.7.alpha3 as well. And finally managed to test it.
So I am putting this back to positive review. Hopefully it won't be in vain.



---

archive/issue_comments_062006.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-06T09:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62006",
    "user": "@kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062007.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-11T19:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62007",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_062008.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-04-14T18:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62008",
    "user": "@jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_062009.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-04-14T18:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62009",
    "user": "@jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_062010.json:
```json
{
    "body": "Because of some issues with #10818 on Mac OS X and because of comments at #10296, my \"gut\" feeling says that maybe it is best to postpone this patch to the sage-4.7.1 cycle.  I can't point at anything particular which is wrong, but I think it is not justified to merge this patchbomb at this point in the sage-4.7 cycle.\n\nOf course, I remain open for arguments stating the contrary.",
    "created_at": "2011-04-14T18:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62010",
    "user": "@jdemeyer"
}
```

Because of some issues with #10818 on Mac OS X and because of comments at #10296, my "gut" feeling says that maybe it is best to postpone this patch to the sage-4.7.1 cycle.  I can't point at anything particular which is wrong, but I think it is not justified to merge this patchbomb at this point in the sage-4.7 cycle.

Of course, I remain open for arguments stating the contrary.



---

archive/issue_comments_062011.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-04-14T18:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62011",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062012.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-14T18:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62012",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062013.json:
```json
{
    "body": "I'll admit that I was surprised you took that \"patch bomb\" in at all initially in alpha4 then alpha5. I am not completely sure but I think the new interface.py makes a number of components chatty. When I reviewed the test logs from my experiments with python-2.7 I have seen plenty of chatter of stuff going by pexpect that I don't remember being there before.",
    "created_at": "2011-04-14T21:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62013",
    "user": "@kiwifb"
}
```

I'll admit that I was surprised you took that "patch bomb" in at all initially in alpha4 then alpha5. I am not completely sure but I think the new interface.py makes a number of components chatty. When I reviewed the test logs from my experiments with python-2.7 I have seen plenty of chatter of stuff going by pexpect that I don't remember being there before.



---

archive/issue_comments_062014.json:
```json
{
    "body": "Well, if that is the case then I guess this is wise.  I do think that it's not appropriate to ask JP or Nils or anyone else to make more fixes until it's tested on a more wide basis by being in an alpha - as long as JP has time to rebase to 4.7, if that's necessary! 150+ comments is enough.",
    "created_at": "2011-04-15T00:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62014",
    "user": "@kcrisman"
}
```

Well, if that is the case then I guess this is wise.  I do think that it's not appropriate to ask JP or Nils or anyone else to make more fixes until it's tested on a more wide basis by being in an alpha - as long as JP has time to rebase to 4.7, if that's necessary! 150+ comments is enough.



---

archive/issue_comments_062015.json:
```json
{
    "body": "Replying to [comment:156 fbissey]:\n\n> I'll admit that I was surprised you took that \"patch bomb\" in at all initially in alpha4 then alpha5. I am not completely sure but I think the new interface.py makes a number of components chatty. When I reviewed the test logs from my experiments with python-2.7 I have seen plenty of chatter of stuff going by pexpect that I don't remember being there before.\n\nCould you tell me where to have a look for those chatty things ? Don't have much time to investigate that alone right now.\n\nIt is also a little bit surprising because the splitting of the expect class into expect and interface classes should be kind of trivial (just take a bunch of methods in expect and paste them in a superclass).\n\nAt least for most classes inheriting expect it should not have dramatic consequences. Of course I could have screwed up something in the way.\n\nBoth Maxima classes are more problematic because of multiple inheritance. It \"works\" now thanks to python MRO, but IIRC, that MRO will change with python 3.0 and could break everything.",
    "created_at": "2011-04-15T06:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62015",
    "user": "jpflori"
}
```

Replying to [comment:156 fbissey]:

> I'll admit that I was surprised you took that "patch bomb" in at all initially in alpha4 then alpha5. I am not completely sure but I think the new interface.py makes a number of components chatty. When I reviewed the test logs from my experiments with python-2.7 I have seen plenty of chatter of stuff going by pexpect that I don't remember being there before.

Could you tell me where to have a look for those chatty things ? Don't have much time to investigate that alone right now.

It is also a little bit surprising because the splitting of the expect class into expect and interface classes should be kind of trivial (just take a bunch of methods in expect and paste them in a superclass).

At least for most classes inheriting expect it should not have dramatic consequences. Of course I could have screwed up something in the way.

Both Maxima classes are more problematic because of multiple inheritance. It "works" now thanks to python MRO, but IIRC, that MRO will change with python 3.0 and could break everything.



---

archive/issue_comments_062016.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-15T06:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62016",
    "user": "jpflori"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062017.json:
```json
{
    "body": "I get the following error on SunOS 5.10-32 (marks) with a trial sage-4.7.alpha5.  I'm sure whether the error is repeatable and whether it is related to this ticket, but I'm copying it here anyway:\n\n```\nsage -t -long  -force_lib devel/sage/sage/misc/trace.py\n**********************************************************************\nFile \"/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/devel/sage-main/sage/misc/trace.py\", line 54:\n    sage: _ = s.expect('100')\nException raised:\n    Traceback (most recent call last):\n      File \"/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[6]>\", line 1, in <module>\n        _ = s.expect('100')###line 54:\n    sage: _ = s.expect('100')\n      File \"/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/lib/python/site-packages/pexpect.py\", line 912, in expect\n        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)\n      File \"/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/lib/python/site-packages/pexpect.py\", line 989, in expect_list\n        raise TIMEOUT (str(e) + '\\n' + str(self))\n    TIMEOUT: Timeout exceeded in read_nonblocking().\n    <pexpect.spawn instance at 0x32b4990>\n    version: 2.0 ($Revision: 1.151 $)\n    command: /home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/sage\n    args: ['/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/sage']\n    patterns:\n        100\n    buffer (last 100 chars): \n    before (last 100 chars):                          *\n\n    **********************************************************************\n\n\n    after: <class 'pexpect.TIMEOUT'>\n    match: None\n    match_index: None\n    exitstatus: None\n    flag_eof: 0\n    pid: 24906\n    child_fd: 4\n    timeout: 30\n    delimiter: <class 'pexpect.EOF'>\n    logfile: None\n    maxread: 2000\n    searchwindowsize: None\n    delaybeforesend: 0.1\n**********************************************************************\nFile \"/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/devel/sage-main/sage/misc/trace.py\", line 61:\n    sage: print s.before[s.before.find('-'):]\nExpected:\n    ---...\n    ipdb> c\n    2 * 5\nGot:\n    ----------------------------------------------------------------------\n\n    | Sage Version 4.7.alpha5, Release Date: 2011-04-13                  |\n\n    | Type notebook() for the GUI, and license() for information.        |\n\n    ----------------------------------------------------------------------\n\n    **********************************************************************\n\n    *                                                                    *\n\n    * Warning: this is a prerelease version, and it may be unstable.     *\n\n    *                                                                    *\n\n    **********************************************************************\n\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   2 of  11 in __main__.example_1\n```\n",
    "created_at": "2011-04-15T08:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62017",
    "user": "@jdemeyer"
}
```

I get the following error on SunOS 5.10-32 (marks) with a trial sage-4.7.alpha5.  I'm sure whether the error is repeatable and whether it is related to this ticket, but I'm copying it here anyway:

```
sage -t -long  -force_lib devel/sage/sage/misc/trace.py
**********************************************************************
File "/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/devel/sage-main/sage/misc/trace.py", line 54:
    sage: _ = s.expect('100')
Exception raised:
    Traceback (most recent call last):
      File "/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        _ = s.expect('100')###line 54:
    sage: _ = s.expect('100')
      File "/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/lib/python/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/local/lib/python/site-packages/pexpect.py", line 989, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x32b4990>
    version: 2.0 ($Revision: 1.151 $)
    command: /home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/sage
    args: ['/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/sage']
    patterns:
        100
    buffer (last 100 chars): 
    before (last 100 chars):                          *

    **********************************************************************


    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 24906
    child_fd: 4
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
File "/home/buildbot/build/sage/mark2-1/mark_full/build/sage-4.7.alpha5/devel/sage-main/sage/misc/trace.py", line 61:
    sage: print s.before[s.before.find('-'):]
Expected:
    ---...
    ipdb> c
    2 * 5
Got:
    ----------------------------------------------------------------------

    | Sage Version 4.7.alpha5, Release Date: 2011-04-13                  |

    | Type notebook() for the GUI, and license() for information.        |

    ----------------------------------------------------------------------

    **********************************************************************

    *                                                                    *

    * Warning: this is a prerelease version, and it may be unstable.     *

    *                                                                    *

    **********************************************************************

    <BLANKLINE>
**********************************************************************
1 items had failures:
   2 of  11 in __main__.example_1
```




---

archive/issue_comments_062018.json:
```json
{
    "body": "Replying to [comment:158 jpflori]:\n> Replying to [comment:156 fbissey]:\n> \n> > I'll admit that I was surprised you took that \"patch bomb\" in at all initially in alpha4 then alpha5. I am not completely sure but I think the new interface.py makes a number of components chatty. When I reviewed the test logs from my experiments with python-2.7 I have seen plenty of chatter of stuff going by pexpect that I don't remember being there before.\n> \n> Could you tell me where to have a look for those chatty things ? Don't have much time to investigate that alone right now.\n> \nI have posted a log at #9958 (sage-4.7.alpha4-test.log.bz2) look for mwrank.py for example.",
    "created_at": "2011-04-15T08:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62018",
    "user": "@kiwifb"
}
```

Replying to [comment:158 jpflori]:
> Replying to [comment:156 fbissey]:
> 
> > I'll admit that I was surprised you took that "patch bomb" in at all initially in alpha4 then alpha5. I am not completely sure but I think the new interface.py makes a number of components chatty. When I reviewed the test logs from my experiments with python-2.7 I have seen plenty of chatter of stuff going by pexpect that I don't remember being there before.
> 
> Could you tell me where to have a look for those chatty things ? Don't have much time to investigate that alone right now.
> 
I have posted a log at #9958 (sage-4.7.alpha4-test.log.bz2) look for mwrank.py for example.



---

archive/issue_comments_062019.json:
```json
{
    "body": "Replying to [comment:161 fbissey]:\n\n> I have posted a log at #9958 (sage-4.7.alpha4-test.log.bz2) look for mwrank.py for example.\n\nAre you sure that mwrank is related in any way to the expect.py/interface.py we've modified here ?\n\nmwrank.pyx provides access to a C++ library and the interface.py in the same folder just provides direct python access to methods defined in the first file or am I completely missing something here ?",
    "created_at": "2011-04-15T09:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62019",
    "user": "jpflori"
}
```

Replying to [comment:161 fbissey]:

> I have posted a log at #9958 (sage-4.7.alpha4-test.log.bz2) look for mwrank.py for example.

Are you sure that mwrank is related in any way to the expect.py/interface.py we've modified here ?

mwrank.pyx provides access to a C++ library and the interface.py in the same folder just provides direct python access to methods defined in the first file or am I completely missing something here ?



---

archive/issue_comments_062020.json:
```json
{
    "body": "I've search through the logs for \"interfaces\" (the main directory wa are concerned with), \"calculus\" and \"symbolic\".\n\nThe only noise I found so far is:\n\n\n```\nFile \"/usr/share/sage/devel/sage-main/sage/symbolic/expression.pyx\", line 7728:\n    sage: f = 1 + x + sqrt(x+2); f.find_root(-2,10)\nExpected:\n    -1.6180339887498949\nGot:\n    -1.618033988749895\n#0: simplify_sum(expr='sum(q^k,k,0,inf))\n#1: simplify_sum(expr=a*'sum(q^k,k,0,inf))\n\n```\n\nand:\n\n\n```\nFile \"/usr/share/sage/devel/sage-main/sage/calculus/calculus.py\", line 223:\n    sage: float(z)\nExpected:\n    4.6467837624329356\nGot:\n    4.646783762432936\n#0: simplify_sum(expr='sum(q^k,k,0,inf))\n#1: simplify_sum(expr=a*'sum(q^k,k,0,inf))\n\n```\n\nWhich does not cause any problem if the doctest passes (i.e. if we set the expected answer to the correct precision).\n\nIt's caused in some way by ECL (I've tried to redirect as much as possible toward \"/dev/null\" slightly modifying the first version of the patches but could not get better result, I'm no expert in Lisp) and not by the refactoring of expect.py into expect.py/interface.py",
    "created_at": "2011-04-15T09:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62020",
    "user": "jpflori"
}
```

I've search through the logs for "interfaces" (the main directory wa are concerned with), "calculus" and "symbolic".

The only noise I found so far is:


```
File "/usr/share/sage/devel/sage-main/sage/symbolic/expression.pyx", line 7728:
    sage: f = 1 + x + sqrt(x+2); f.find_root(-2,10)
Expected:
    -1.6180339887498949
Got:
    -1.618033988749895
#0: simplify_sum(expr='sum(q^k,k,0,inf))
#1: simplify_sum(expr=a*'sum(q^k,k,0,inf))

```

and:


```
File "/usr/share/sage/devel/sage-main/sage/calculus/calculus.py", line 223:
    sage: float(z)
Expected:
    4.6467837624329356
Got:
    4.646783762432936
#0: simplify_sum(expr='sum(q^k,k,0,inf))
#1: simplify_sum(expr=a*'sum(q^k,k,0,inf))

```

Which does not cause any problem if the doctest passes (i.e. if we set the expected answer to the correct precision).

It's caused in some way by ECL (I've tried to redirect as much as possible toward "/dev/null" slightly modifying the first version of the patches but could not get better result, I'm no expert in Lisp) and not by the refactoring of expect.py into expect.py/interface.py



---

archive/issue_comments_062021.json:
```json
{
    "body": "OK, no problem Jean-Pierre. There are a lot of things going on with python 2.7 that may just be one of them. I thought the mwrank executable was called by the expect interface. There probably wouldn't be anything to spot if it weren't for all these doctests failures. It doesn't cause the test failure either I think.",
    "created_at": "2011-04-15T20:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62021",
    "user": "@kiwifb"
}
```

OK, no problem Jean-Pierre. There are a lot of things going on with python 2.7 that may just be one of them. I thought the mwrank executable was called by the expect interface. There probably wouldn't be anything to spot if it weren't for all these doctests failures. It doesn't cause the test failure either I think.



---

archive/issue_comments_062022.json:
```json
{
    "body": "I definitely think the mwrank problem is complete unrelated to this ticket.\n\nCould someone repoduce Jeroen bug ? I've got no problems on my debian amd64 with 4.7.alpha3, but I won't have the time to build the latest alpha today or next week, nor working on this ticket, but is there anything preventing it to go back to needs_review or even positive_review ?",
    "created_at": "2011-04-22T09:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62022",
    "user": "jpflori"
}
```

I definitely think the mwrank problem is complete unrelated to this ticket.

Could someone repoduce Jeroen bug ? I've got no problems on my debian amd64 with 4.7.alpha3, but I won't have the time to build the latest alpha today or next week, nor working on this ticket, but is there anything preventing it to go back to needs_review or even positive_review ?



---

archive/issue_comments_062023.json:
```json
{
    "body": "[This bug](http://trac.sagemath.org/sage_trac/ticket/7377#comment:160) is most likely **not** related to this ticket.",
    "created_at": "2011-04-25T10:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62023",
    "user": "@jdemeyer"
}
```

[This bug](http://trac.sagemath.org/sage_trac/ticket/7377#comment:160) is most likely **not** related to this ticket.



---

archive/issue_comments_062024.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-25T16:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62024",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062025.json:
```json
{
    "body": "I think we are now clear. The chattiness is likely to come from somewhere else and Jeroen says his bug is probably unrelated. I'll put that back to positive review - again.",
    "created_at": "2011-04-25T19:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62025",
    "user": "@kiwifb"
}
```

I think we are now clear. The chattiness is likely to come from somewhere else and Jeroen says his bug is probably unrelated. I'll put that back to positive review - again.



---

archive/issue_comments_062026.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-25T19:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62026",
    "user": "@kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062027.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-26T09:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7377#issuecomment-62027",
    "user": "@jdemeyer"
}
```

Resolution: fixed
