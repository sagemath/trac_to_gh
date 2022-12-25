# Issue 7085: fix this laurent series coercion bug

archive/issues_007085.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  mhampton\n\n\n```\n> Ok, I am completely baffled by the following situation:\n>\n> sage: A.<z>=LaurentSeriesRing(QQ)\n> sage: B.<w>=LaurentSeriesRing(A)\n> sage: z/w\n>  1\n> Maybe you will agree this is a bug?\n\nThat's definitely a coercion bug.   You can workaround it like this:\n\n\nsage: sage: A.<z>=LaurentSeriesRing(QQ)\nsage: sage: B.<w>=LaurentSeriesRing(A)\nsage: z/w\n1\nsage: (1/w) * z\nz*w^-1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7085\n\n",
    "created_at": "2009-09-30T23:10:18Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "fix this laurent series coercion bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7085",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

CC:  mhampton


```
> Ok, I am completely baffled by the following situation:
>
> sage: A.<z>=LaurentSeriesRing(QQ)
> sage: B.<w>=LaurentSeriesRing(A)
> sage: z/w
>  1
> Maybe you will agree this is a bug?

That's definitely a coercion bug.   You can workaround it like this:


sage: sage: A.<z>=LaurentSeriesRing(QQ)
sage: sage: B.<w>=LaurentSeriesRing(A)
sage: z/w
1
sage: (1/w) * z
z*w^-1
```


Issue created by migration from https://trac.sagemath.org/ticket/7085





---

archive/issue_comments_058449.json:
```json
{
    "body": "Before any division takes place, z is getting incorrectly coerced to w.  I think this is because in laurent_series_ring_element.pyx, in the LaurentSeries class __init__ method the represention (variable)^n*f is shifted by the code:\n\n```\n        else:\n            val = f.valuation()\n            if val == 0:\n                self.__n = n    # power of the variable\n                self.__u = f    # unit part\n            else:\n                self.__n = n + val\n                self.__u = f >> val\n```\n\n\nand I think that shifting is missing that different variables are involved.",
    "created_at": "2011-01-11T01:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58449",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Before any division takes place, z is getting incorrectly coerced to w.  I think this is because in laurent_series_ring_element.pyx, in the LaurentSeries class __init__ method the represention (variable)^n*f is shifted by the code:

```
        else:
            val = f.valuation()
            if val == 0:
                self.__n = n    # power of the variable
                self.__u = f    # unit part
            else:
                self.__n = n + val
                self.__u = f >> val
```


and I think that shifting is missing that different variables are involved.



---

archive/issue_comments_058450.json:
```json
{
    "body": "Now I'm not sure the above code is the critical place, but this shows that its a coercion rather than a division issue:\n\n```\nsage: A.<z>=LaurentSeriesRing(QQ)\nsage: B.<w>=LaurentSeriesRing(A)\nsage: B(z)\nw\n```\n",
    "created_at": "2011-01-11T02:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Now I'm not sure the above code is the critical place, but this shows that its a coercion rather than a division issue:

```
sage: A.<z>=LaurentSeriesRing(QQ)
sage: B.<w>=LaurentSeriesRing(A)
sage: B(z)
w
```




---

archive/issue_comments_058451.json:
```json
{
    "body": "Attachment [trac_7085_awful_hack.patch](tarball://root/attachments/some-uuid/ticket7085/trac_7085_awful_hack.patch) by mhampton created at 2011-01-11 06:06:47\n\nSolves problem, but in a very hackish way.",
    "created_at": "2011-01-11T06:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58451",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_7085_awful_hack.patch](tarball://root/attachments/some-uuid/ticket7085/trac_7085_awful_hack.patch) by mhampton created at 2011-01-11 06:06:47

Solves problem, but in a very hackish way.



---

archive/issue_comments_058452.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-11T06:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58452",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058453.json:
```json
{
    "body": "The attach patch solves the problem, but not in a very robust way.  I suspect that Simon King's efforts at #8972 are related and might fix the problem in a more fundamental way.  I also hope that my patch rekindles interest in this module and that someone with a deeper understanding of the code can provide a better solution.\n\nOn the positive side, I think this doesn't break anything and solves the immediate problem.  Perhaps when #8972 is ready my workaround can be deleted.",
    "created_at": "2011-01-11T06:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58453",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

The attach patch solves the problem, but not in a very robust way.  I suspect that Simon King's efforts at #8972 are related and might fix the problem in a more fundamental way.  I also hope that my patch rekindles interest in this module and that someone with a deeper understanding of the code can provide a better solution.

On the positive side, I think this doesn't break anything and solves the immediate problem.  Perhaps when #8972 is ready my workaround can be deleted.



---

archive/issue_comments_058454.json:
```json
{
    "body": "I suspect the prolem is that `laurent_series_ring_element.LaurentSeries.__init__` doesn't realize that the base ring may be a LaurentSeriesRing itself. (But I haven't thought about it too much yet.)",
    "created_at": "2011-01-11T19:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58454",
    "user": "https://github.com/wjp"
}
```

I suspect the prolem is that `laurent_series_ring_element.LaurentSeries.__init__` doesn't realize that the base ring may be a LaurentSeriesRing itself. (But I haven't thought about it too much yet.)



---

archive/issue_comments_058455.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-11T19:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58455",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058456.json:
```json
{
    "body": "This seems to fix it, but I haven't looked at the code closely enough to be sure it's correct:\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/7085_attempt.patch",
    "created_at": "2011-01-11T19:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58456",
    "user": "https://github.com/wjp"
}
```

This seems to fix it, but I haven't looked at the code closely enough to be sure it's correct:

http://www.math.leidenuniv.nl/~wpalenst/sage/7085_attempt.patch



---

archive/issue_comments_058457.json:
```json
{
    "body": "...but it unfortunately also breaks coercions between different `LaurentSeriesRings`.",
    "created_at": "2011-01-11T19:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58457",
    "user": "https://github.com/wjp"
}
```

...but it unfortunately also breaks coercions between different `LaurentSeriesRings`.



---

archive/issue_comments_058458.json:
```json
{
    "body": "Changing keywords from \"\" to \"laurent series\".",
    "created_at": "2014-03-04T12:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58458",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "laurent series".



---

archive/issue_comments_058459.json:
```json
{
    "body": "The attached branch fixes the bug by converting `LaurentSeriesRing` to the new coercion framework.  In the situation where *A* -> *B* are two rings with a coercion map between them, this allows us to define a coercion map from *A* to *B*((*u*)) as the composition of the obvious maps *A* -> *B* -> *B*((*u*)).  The `_element_constructor_(x)` for *B*((*u*)) then only has to consider one new special case, namely where *x* is in *B*.  It turns out that the easiest way to treat this case is to convert *x* into a (constant) power series, which has to be done anyway due to the internal representation of Laurent series.",
    "created_at": "2014-05-04T22:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58459",
    "user": "https://github.com/pjbruin"
}
```

The attached branch fixes the bug by converting `LaurentSeriesRing` to the new coercion framework.  In the situation where *A* -> *B* are two rings with a coercion map between them, this allows us to define a coercion map from *A* to *B*((*u*)) as the composition of the obvious maps *A* -> *B* -> *B*((*u*)).  The `_element_constructor_(x)` for *B*((*u*)) then only has to consider one new special case, namely where *x* is in *B*.  It turns out that the easiest way to treat this case is to convert *x* into a (constant) power series, which has to be done anyway due to the internal representation of Laurent series.



---

archive/issue_comments_058460.json:
```json
{
    "body": "Changing component from basic arithmetic to coercion.",
    "created_at": "2014-05-04T22:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58460",
    "user": "https://github.com/pjbruin"
}
```

Changing component from basic arithmetic to coercion.



---

archive/issue_comments_058461.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-04T22:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58461",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058462.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-05T20:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58462",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058463.json:
```json
{
    "body": "Very trivial change of removing a double colon `::`. LGTM otherwise.\n----\nNew commits:",
    "created_at": "2014-05-05T20:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58463",
    "user": "https://github.com/tscrim"
}
```

Very trivial change of removing a double colon `::`. LGTM otherwise.
----
New commits:



---

archive/issue_comments_058464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-05-06T22:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7085#issuecomment-58464",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_007307.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-05-06T22:02:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7085",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7085#event-7307"
}
```
