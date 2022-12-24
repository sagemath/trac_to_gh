# Issue 7661: maxima interface gives precedence to function dictionary instead of local variables

archive/issues_007661.json:
```json
{
    "body": "Assignee: was\n\nCC:  robert.marik\n\nKeywords: maxima\n\nFrom the sage-devel thread:\n\nhttp://groups.google.com/group/sage-devel/t/c89582242c83a349\n\n\n```\nOn Fri, 11 Dec 2009 13:46:31 +0100\nNathann Cohen <nathann.cohen@gmail.com> wrote:\n\n> sage: var('delta k')\n> sage: m1=2*delta**2 + 2**2*delta*k\n> sage: n=delta*k+2\n> sage: m2=(2*delta)**2+(k-1)*4\n> sage: m=(delta+delta*k-(delta-1))\n> sage: ((m1/n)-(m2/n)).expand().simplify()\n```\n\n\nOn 4.3.rc0, I get this:\n\n```\nTypeError: unsupported operand parent(s) for '*': 'Symbolic Ring' and\n'<class 'sage.functions.generalized.FunctionDiracDelta'>'\n```\n\n\nThe Maxima interface seems to give precedence to the global function\ndictionary instead of the local variables when converting Maxima output\nback to Sage expressions.\n\n```\nsage: dirac_delta(x)\ndirac_delta(x)\nsage: maxima(dirac_delta(x))\ndelta(x)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7661\n\n",
    "created_at": "2009-12-11T14:18:05Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "maxima interface gives precedence to function dictionary instead of local variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7661",
    "user": "burcin"
}
```
Assignee: was

CC:  robert.marik

Keywords: maxima

From the sage-devel thread:

http://groups.google.com/group/sage-devel/t/c89582242c83a349


```
On Fri, 11 Dec 2009 13:46:31 +0100
Nathann Cohen <nathann.cohen@gmail.com> wrote:

> sage: var('delta k')
> sage: m1=2*delta**2 + 2**2*delta*k
> sage: n=delta*k+2
> sage: m2=(2*delta)**2+(k-1)*4
> sage: m=(delta+delta*k-(delta-1))
> sage: ((m1/n)-(m2/n)).expand().simplify()
```


On 4.3.rc0, I get this:

```
TypeError: unsupported operand parent(s) for '*': 'Symbolic Ring' and
'<class 'sage.functions.generalized.FunctionDiracDelta'>'
```


The Maxima interface seems to give precedence to the global function
dictionary instead of the local variables when converting Maxima output
back to Sage expressions.

```
sage: dirac_delta(x)
dirac_delta(x)
sage: maxima(dirac_delta(x))
delta(x)
```


Issue created by migration from https://trac.sagemath.org/ticket/7661





---

archive/issue_comments_065583.json:
```json
{
    "body": "People run into this all the time, evidently:\n\n```\n[15:21] --> SageWWW has joined this channel (~SageWWW@64.241.37.140).\n[15:23] <SageWWW> hey guys.  what do you think about http://pastebin.ca/1772520\n[15:24] <SageWWW> d = var('delta'), so now d is a reference to a sage.symbolic.expression.Expression\n[15:25] <SageWWW> but when we try to add it to something else, it thinks its a sage.functions.generalized.FunctionDiracDelta\n[15:27] <wstein> http://trac.sagemath.org/sage_trac/ticket/7661\n```\n",
    "created_at": "2010-01-30T23:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65583",
    "user": "was"
}
```

People run into this all the time, evidently:

```
[15:21] --> SageWWW has joined this channel (~SageWWW@64.241.37.140).
[15:23] <SageWWW> hey guys.  what do you think about http://pastebin.ca/1772520
[15:24] <SageWWW> d = var('delta'), so now d is a reference to a sage.symbolic.expression.Expression
[15:25] <SageWWW> but when we try to add it to something else, it thinks its a sage.functions.generalized.FunctionDiracDelta
[15:27] <wstein> http://trac.sagemath.org/sage_trac/ticket/7661
```




---

archive/issue_comments_065584.json:
```json
{
    "body": "sage: d = var('delta')\nsage: e = d._maxima_()\nsage: sage.calculus.calculus.symbolic_expression_from_maxima_element(e)\ndirac_delta\n\nsomewhere in symbolic_expression_from_maxima_element(), the string from maxima is looked up in sage.calculus.calculus._syms, which by default has 'delta': dirac_delta .  So this is what's happening, next, SR() barfs on trying to turn dirac_delta into a symbolic expression, at which point people who just wanted their variable 'delta' back get confused and frustrated.\n\nsage: del sage.calculus.calculus._syms['delta']\nsage: sage.calculus.calculus.symbolic_expression_from_maxima_element(e)\ndelta\n\nThat may not be such a good idea, however, since what sage calls dirac_delta, maxima refers to as delta.  Nevertheless, since reset('delta') appears to remove delta from that dictionary, perhaps var('delta') should also do so?\n\nOf course, what happens when someone does a Laplace transform with delta as a sage variable will then come out confusing and wrong.  At least the current behavior is merely broken.",
    "created_at": "2010-01-31T07:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65584",
    "user": "eigenlambda"
}
```

sage: d = var('delta')
sage: e = d._maxima_()
sage: sage.calculus.calculus.symbolic_expression_from_maxima_element(e)
dirac_delta

somewhere in symbolic_expression_from_maxima_element(), the string from maxima is looked up in sage.calculus.calculus._syms, which by default has 'delta': dirac_delta .  So this is what's happening, next, SR() barfs on trying to turn dirac_delta into a symbolic expression, at which point people who just wanted their variable 'delta' back get confused and frustrated.

sage: del sage.calculus.calculus._syms['delta']
sage: sage.calculus.calculus.symbolic_expression_from_maxima_element(e)
delta

That may not be such a good idea, however, since what sage calls dirac_delta, maxima refers to as delta.  Nevertheless, since reset('delta') appears to remove delta from that dictionary, perhaps var('delta') should also do so?

Of course, what happens when someone does a Laplace transform with delta as a sage variable will then come out confusing and wrong.  At least the current behavior is merely broken.



---

archive/issue_comments_065585.json:
```json
{
    "body": "attachment:trac_7661-maxima_convert_back.patch fixes the problem reported above, and a similar problem with function conversions back from maxima reported in comment:2:ticket:8459.",
    "created_at": "2010-04-05T10:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65585",
    "user": "burcin"
}
```

attachment:trac_7661-maxima_convert_back.patch fixes the problem reported above, and a similar problem with function conversions back from maxima reported in comment:2:ticket:8459.



---

archive/issue_comments_065586.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-04-05T10:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65586",
    "user": "burcin"
}
```

Changing priority from major to critical.



---

archive/issue_comments_065587.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-05T10:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65587",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065588.json:
```json
{
    "body": "Attachment [trac_7661-maxima_convert_back.patch](tarball://root/attachments/some-uuid/ticket7661/trac_7661-maxima_convert_back.patch) by burcin created at 2010-04-06 15:42:51\n\nI updated attachment:trac_7661-maxima_convert_back.patch to remove a doctest fix broken by a previous patch in my queue (#6949, `symbol...` line in sage/symbolic/ring.pyx).\n\nThis patch depends on #7748.",
    "created_at": "2010-04-06T15:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65588",
    "user": "burcin"
}
```

Attachment [trac_7661-maxima_convert_back.patch](tarball://root/attachments/some-uuid/ticket7661/trac_7661-maxima_convert_back.patch) by burcin created at 2010-04-06 15:42:51

I updated attachment:trac_7661-maxima_convert_back.patch to remove a doctest fix broken by a previous patch in my queue (#6949, `symbol...` line in sage/symbolic/ring.pyx).

This patch depends on #7748.



---

archive/issue_comments_065589.json:
```json
{
    "body": "Thanks for working onthis. Is #7748 the only prerequisity? I installed three patches as described at #7748 and got the following error\n\n```\npatching file sage/calculus/calculus.py\nHunk #3 succeeded at 1414 with fuzz 1 (offset -4 lines).\nHunk #5 FAILED at 1455\n1 out of 14 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2010-04-09T08:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65589",
    "user": "robert.marik"
}
```

Thanks for working onthis. Is #7748 the only prerequisity? I installed three patches as described at #7748 and got the following error

```
patching file sage/calculus/calculus.py
Hunk #3 succeeded at 1414 with fuzz 1 (offset -4 lines).
Hunk #5 FAILED at 1455
1 out of 14 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_065590.json:
```json
{
    "body": "AFAICT, #8237 also changes that code. Can you try with #8237 applied?\n\nI'm sorry for the dependency hell we get into with these patches for every release. I don't know any way to automatically get a list of dependencies for a patch in my queue.\n\nThanks for your time Robert.",
    "created_at": "2010-04-09T10:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65590",
    "user": "burcin"
}
```

AFAICT, #8237 also changes that code. Can you try with #8237 applied?

I'm sorry for the dependency hell we get into with these patches for every release. I don't know any way to automatically get a list of dependencies for a patch in my queue.

Thanks for your time Robert.



---

archive/issue_comments_065591.json:
```json
{
    "body": "Changing assignee from was to burcin.",
    "created_at": "2010-04-09T10:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65591",
    "user": "burcin"
}
```

Changing assignee from was to burcin.



---

archive/issue_comments_065592.json:
```json
{
    "body": "Hello Burcin\n\nI think that two lines should be removed from the patch\n\n```\nglobal _syms \n_syms = sage.symbolic.pynac.symbol_table.get('maxima', {}) \n```\n\n\nI updated your patch, it is now http://user.mendelu.cz/marik/sage/trac_7661-maxima_convert_back2.patch\n\nIf everything will work, I'll return in few (several) hours with positive review (tests in functions, interfaces, symbolics and calculus passed, now running all the test). \n\nRobert",
    "created_at": "2010-04-09T14:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65592",
    "user": "robert.marik"
}
```

Hello Burcin

I think that two lines should be removed from the patch

```
global _syms 
_syms = sage.symbolic.pynac.symbol_table.get('maxima', {}) 
```


I updated your patch, it is now http://user.mendelu.cz/marik/sage/trac_7661-maxima_convert_back2.patch

If everything will work, I'll return in few (several) hours with positive review (tests in functions, interfaces, symbolics and calculus passed, now running all the test). 

Robert



---

archive/issue_comments_065593.json:
```json
{
    "body": "OK. That is one approach to solving this problem. Now we need to rebase the patch at #8237 so that it applies on top of these. Removing the offending hunk from `calculus.py` should be enough for that.\n\nNote that your updated patch shows you as the author. I'd appreciate it if you changed that back.\n\nThanks.",
    "created_at": "2010-04-09T14:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65593",
    "user": "burcin"
}
```

OK. That is one approach to solving this problem. Now we need to rebase the patch at #8237 so that it applies on top of these. Removing the offending hunk from `calculus.py` should be enough for that.

Note that your updated patch shows you as the author. I'd appreciate it if you changed that back.

Thanks.



---

archive/issue_comments_065594.json:
```json
{
    "body": "Sure, it was intended as temporary patch and from this reason I did not upload to trac server unless tested. I got some doctest failures in three files. See http://boxen.math.washington.edu/home/marik/ and the files a, b and c.\n\nI think that b is simple to fix, but have no idea about a and c.",
    "created_at": "2010-04-09T16:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65594",
    "user": "robert.marik"
}
```

Sure, it was intended as temporary patch and from this reason I did not upload to trac server unless tested. I got some doctest failures in three files. See http://boxen.math.washington.edu/home/marik/ and the files a, b and c.

I think that b is simple to fix, but have no idea about a and c.



---

archive/issue_comments_065595.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-09T16:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65595",
    "user": "robert.marik"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065596.json:
```json
{
    "body": "Attachment [trac_7661-maxima_convert_back.take2.patch](tarball://root/attachments/some-uuid/ticket7661/trac_7661-maxima_convert_back.take2.patch) by burcin created at 2010-04-09 18:54:11\n\napply only this patch",
    "created_at": "2010-04-09T18:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65596",
    "user": "burcin"
}
```

Attachment [trac_7661-maxima_convert_back.take2.patch](tarball://root/attachments/some-uuid/ticket7661/trac_7661-maxima_convert_back.take2.patch) by burcin created at 2010-04-09 18:54:11

apply only this patch



---

archive/issue_comments_065597.json:
```json
{
    "body": "Thanks a lot for the quick feedback. \n* `a` is because you have the pynac package from #8644 installed, but not the corresponding patch from #8565. \n* `b` is a simple import problem, fixed by the updated attachment:trac_7661-maxima_convert_back.take2.patch\n* I can't reproduce `c` here. It doesn't seem to be related to the changes in ticket. Do you have any other patches applied?",
    "created_at": "2010-04-09T18:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65597",
    "user": "burcin"
}
```

Thanks a lot for the quick feedback. 
* `a` is because you have the pynac package from #8644 installed, but not the corresponding patch from #8565. 
* `b` is a simple import problem, fixed by the updated attachment:trac_7661-maxima_convert_back.take2.patch
* I can't reproduce `c` here. It doesn't seem to be related to the changes in ticket. Do you have any other patches applied?



---

archive/issue_comments_065598.json:
```json
{
    "body": "I tested it on a fresh install and seems that all a,b,c are resolved.\nI am running all tests again, to be sure :)",
    "created_at": "2010-04-10T17:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65598",
    "user": "robert.marik"
}
```

I tested it on a fresh install and seems that all a,b,c are resolved.
I am running all tests again, to be sure :)



---

archive/issue_comments_065599.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-10T17:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65599",
    "user": "robert.marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065600.json:
```json
{
    "body": "Tests passed, postive review, thanks for fixing - very very usefull ticket.\n\nRelease manager: apply only trac_7661-maxima_convert_back.take2.patch",
    "created_at": "2010-04-10T19:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65600",
    "user": "robert.marik"
}
```

Tests passed, postive review, thanks for fixing - very very usefull ticket.

Release manager: apply only trac_7661-maxima_convert_back.take2.patch



---

archive/issue_comments_065601.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-10T19:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65601",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065602.json:
```json
{
    "body": "Merged \"trac_7661-maxima_convert_back.take2.patch\" in 4.4.alpha0",
    "created_at": "2010-04-15T20:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65602",
    "user": "jhpalmieri"
}
```

Merged "trac_7661-maxima_convert_back.take2.patch" in 4.4.alpha0



---

archive/issue_comments_065603.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7661#issuecomment-65603",
    "user": "jhpalmieri"
}
```

Resolution: fixed
