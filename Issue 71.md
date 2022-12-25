# Issue 71: Better tracebacks

archive/issues_000071.json:
```json
{
    "body": "Assignee: cwitty\n\nWhen a .sage file is \"load\"ed or \"attach\"ed, it gets translated to a .py file before being processed; the result is a file with different structure than the original.  Any errors are described in terms of the .py file, not the .sage file.\n\nOne working solution is to monkey-patch `traceback.extract_tb()` to undo preparsing.\n\nThe traceback below was generated with this patch. It shows the unpreparsed `1/0` and it also shows the Cython source (see #17382):\n\n```\nsage: 1/0\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n<ipython-input-1-3cdd7c9e2324> in <module>()\n----> 1 1/0\n\n/usr/local/src/sage-config/sage/structure/element.pyx in sage.structure.element.RingElement.__div__ (build/cythonized/sage/structure/element.c:17829)()\n   1891                 return (<RingElement>self)._idiv_(<RingElement>right)\n   1892             else:\n-> 1893                 return (<RingElement>self)._div_(<RingElement>right)\n   1894         global coercion_model\n   1895         return coercion_model.bin_op(self, right, div)\n\n/usr/local/src/sage-config/sage/rings/integer.pyx in sage.rings.integer.Integer._div_ (build/cythonized/sage/rings/integer.c:12964)()\n   1795         # This is vastly faster than doing it here, since here\n   1796         # we can't cimport rationals.\n-> 1797         return the_integer_ring._div(self, right)\n   1798 \n   1799     def __floordiv__(x, y):\n\n/usr/local/src/sage-config/sage/rings/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class._div (build/cythonized/sage/rings/integer_ring.c:4578)()\n    443         cdef rational.Rational x = PY_NEW(rational.Rational)\n    444         if mpz_sgn(right.value) == 0:\n--> 445             raise ZeroDivisionError, 'Rational division by zero'\n    446         mpz_set(mpq_numref(x.value), left.value)\n    447         mpz_set(mpq_denref(x.value), right.value)\n\nZeroDivisionError: Rational division by zero\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/71\n\n",
    "created_at": "2006-09-20T21:40:01Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.5",
    "title": "Better tracebacks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/71",
    "user": "Justin Walker (justin@mac.com)"
}
```
Assignee: cwitty

When a .sage file is "load"ed or "attach"ed, it gets translated to a .py file before being processed; the result is a file with different structure than the original.  Any errors are described in terms of the .py file, not the .sage file.

One working solution is to monkey-patch `traceback.extract_tb()` to undo preparsing.

The traceback below was generated with this patch. It shows the unpreparsed `1/0` and it also shows the Cython source (see #17382):

```
sage: 1/0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-1-3cdd7c9e2324> in <module>()
----> 1 1/0

/usr/local/src/sage-config/sage/structure/element.pyx in sage.structure.element.RingElement.__div__ (build/cythonized/sage/structure/element.c:17829)()
   1891                 return (<RingElement>self)._idiv_(<RingElement>right)
   1892             else:
-> 1893                 return (<RingElement>self)._div_(<RingElement>right)
   1894         global coercion_model
   1895         return coercion_model.bin_op(self, right, div)

/usr/local/src/sage-config/sage/rings/integer.pyx in sage.rings.integer.Integer._div_ (build/cythonized/sage/rings/integer.c:12964)()
   1795         # This is vastly faster than doing it here, since here
   1796         # we can't cimport rationals.
-> 1797         return the_integer_ring._div(self, right)
   1798 
   1799     def __floordiv__(x, y):

/usr/local/src/sage-config/sage/rings/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class._div (build/cythonized/sage/rings/integer_ring.c:4578)()
    443         cdef rational.Rational x = PY_NEW(rational.Rational)
    444         if mpz_sgn(right.value) == 0:
--> 445             raise ZeroDivisionError, 'Rational division by zero'
    446         mpz_set(mpq_numref(x.value), left.value)
    447         mpz_set(mpq_denref(x.value), right.value)

ZeroDivisionError: Rational division by zero
```

Issue created by migration from https://trac.sagemath.org/ticket/71





---

archive/issue_comments_000360.json:
```json
{
    "body": "SAGE can embed the original line numbers in the .py file, and even the original\n.sage lines (before parsing) in the .sage file.  Then the error messages will\nalso list the original line number (and line, if you want) in a comment at the end\nof the line.   In the notebook, at least, it would be easy to postparse the error\nmessages so they refer to the original .sage file.",
    "created_at": "2006-09-21T01:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-360",
    "user": "https://github.com/williamstein"
}
```

SAGE can embed the original line numbers in the .py file, and even the original
.sage lines (before parsing) in the .sage file.  Then the error messages will
also list the original line number (and line, if you want) in a comment at the end
of the line.   In the notebook, at least, it would be easy to postparse the error
messages so they refer to the original .sage file.



---

archive/issue_comments_000361.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-13T02:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-361",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000362.json:
```json
{
    "body": "This is not a bug.",
    "created_at": "2007-01-13T02:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-362",
    "user": "https://github.com/williamstein"
}
```

This is not a bug.



---

archive/issue_events_000155.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-11T02:42:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/71#event-155"
}
```



---

archive/issue_comments_000363.json:
```json
{
    "body": "Changing component from basic arithmetic to misc.",
    "created_at": "2009-06-07T13:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-363",
    "user": "https://github.com/loefflerd"
}
```

Changing component from basic arithmetic to misc.



---

archive/issue_comments_000364.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2009-06-07T13:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-364",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_000365.json:
```json
{
    "body": "Hi.  This is a REALLY old ticket.  Is the documentation at [the programming tutorial](http://www.sagemath.org/doc/tutorial/programming.html) now sufficient, or should we still keep this ticket around?  I love the idea in William's (six-year-old) comment:1, so we could repurpose this ticket to implement this if desired.  Or, one could just improve the documentation a little to mention that errors refer to lines in the .py file.",
    "created_at": "2013-01-29T20:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-365",
    "user": "https://github.com/kcrisman"
}
```

Hi.  This is a REALLY old ticket.  Is the documentation at [the programming tutorial](http://www.sagemath.org/doc/tutorial/programming.html) now sufficient, or should we still keep this ticket around?  I love the idea in William's (six-year-old) comment:1, so we could repurpose this ticket to implement this if desired.  Or, one could just improve the documentation a little to mention that errors refer to lines in the .py file.



---

archive/issue_events_000156.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-11-20T16:38:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/71#event-156"
}
```



---

archive/issue_events_000157.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-11-20T16:38:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "milestone": "sage-6.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/71#event-157"
}
```



---

archive/issue_comments_000366.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-20T16:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-366",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000367.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-20T20:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-367",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000368.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-20T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-368",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000369.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-21T06:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-369",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000370.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-23T10:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-370",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:
