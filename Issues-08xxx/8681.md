# Issue 8681: implement matrix actions on binary quadratic forms

archive/issues_008681.json:
```json
{
    "body": "Assignee: justin\n\nCC:  @tornaria @williamstein @jonhanke @ncalexan @JohnCremona\n\nThe attached patch implements methods for left and right matrix actions on binary quadratic forms.  It also extends the constructor `BinaryQF` to accept a homogeneous polynomial of degree 2 in 2 variables.\n\nI'm ccing other people who have worked on this file to see if anyone is up for a quick review.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8681\n\n",
    "closed_at": "2010-04-29T05:19:31Z",
    "created_at": "2010-04-13T13:05:18Z",
    "labels": [
        "component: quadratic forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "implement matrix actions on binary quadratic forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8681",
    "user": "https://github.com/aghitza"
}
```
Assignee: justin

CC:  @tornaria @williamstein @jonhanke @ncalexan @JohnCremona

The attached patch implements methods for left and right matrix actions on binary quadratic forms.  It also extends the constructor `BinaryQF` to accept a homogeneous polynomial of degree 2 in 2 variables.

I'm ccing other people who have worked on this file to see if anyone is up for a quick review.


Issue created by migration from https://trac.sagemath.org/ticket/8681





---

archive/issue_comments_078985.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-13T13:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78985",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078986.json:
```json
{
    "body": "The patch looks good to me -- pending actually trying it.\n\nI wonder if it would make sense to avoid using polynomials as much as possible, except for convenience printing and input. For instance, `matrix_action_left` could be defined using something like:\n\n```\nv,w = M.columns()\na1 = Q(*v)\nc1 = Q(*w)\nb1 = Q(*(v+w))-a1-c1\nreturn BinaryQF(a1,b1,c1)\n```\nand `matrix_action_right` defined similarly with `rows()` instead of `columns()`.\n\nI see that `__call__` is itself defined using polynomials instead of the other way around --- should that be changed as well?\ne.g.\n\n```\ndef __call__(self, *x):\n  if len(x)==1:\n    x = x[0]\n  x, y = x\n  return (self._a * x + self._b * y) * x + self._c * y**2\n```\n\nand\n\n```\ndef polynomial(self):\n  return self(ZZ['x,y'].gens())\n```\n\nbesides, with the definition of `__call__` I propose above, one can actually evaluate a quadratic form at a vector (so, the * in the proposed matrix actions above would no longer be necessary -- it is because `Q(v)` now fails for v a vector, which is inconvenient IMO).",
    "created_at": "2010-04-13T13:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78986",
    "user": "https://github.com/tornaria"
}
```

The patch looks good to me -- pending actually trying it.

I wonder if it would make sense to avoid using polynomials as much as possible, except for convenience printing and input. For instance, `matrix_action_left` could be defined using something like:

```
v,w = M.columns()
a1 = Q(*v)
c1 = Q(*w)
b1 = Q(*(v+w))-a1-c1
return BinaryQF(a1,b1,c1)
```
and `matrix_action_right` defined similarly with `rows()` instead of `columns()`.

I see that `__call__` is itself defined using polynomials instead of the other way around --- should that be changed as well?
e.g.

```
def __call__(self, *x):
  if len(x)==1:
    x = x[0]
  x, y = x
  return (self._a * x + self._b * y) * x + self._c * y**2
```

and

```
def polynomial(self):
  return self(ZZ['x,y'].gens())
```

besides, with the definition of `__call__` I propose above, one can actually evaluate a quadratic form at a vector (so, the * in the proposed matrix actions above would no longer be necessary -- it is because `Q(v)` now fails for v a vector, which is inconvenient IMO).



---

archive/issue_comments_078987.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-13T21:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78987",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078988.json:
```json
{
    "body": "Gonzalo,\n\nall of this sounds good, pending (to borrow your expression) actually trying it out.  I will do this when I get a chance later today.  I expect a performance gain and no down-sides.",
    "created_at": "2010-04-13T21:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78988",
    "user": "https://github.com/aghitza"
}
```

Gonzalo,

all of this sounds good, pending (to borrow your expression) actually trying it out.  I will do this when I get a chance later today.  I expect a performance gain and no down-sides.



---

archive/issue_comments_078989.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-14T11:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78989",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078990.json:
```json
{
    "body": "Attachment [trac_8681.patch](tarball://root/attachments/some-uuid/ticket8681/trac_8681.patch) by @aghitza created at 2010-04-14 11:18:03\n\nI have implemented Gonzalo's suggestions.  It seems to work great, and indeed it's much faster; the matrix actions are almost 3 times faster with the new code, and `__call__` is an amazing 200 times faster.",
    "created_at": "2010-04-14T11:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78990",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_8681.patch](tarball://root/attachments/some-uuid/ticket8681/trac_8681.patch) by @aghitza created at 2010-04-14 11:18:03

I have implemented Gonzalo's suggestions.  It seems to work great, and indeed it's much faster; the matrix actions are almost 3 times faster with the new code, and `__call__` is an amazing 200 times faster.



---

archive/issue_comments_078991.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-25T17:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78991",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078992.json:
```json
{
    "body": "This looks very good.  After the discussion above I was expecting a much larger patch, but this is nice and simple, and works.\n\nApplies fine to 4.4.rc0 and all tests in sage/quadratic_forms pass.\n\nPositive review!",
    "created_at": "2010-04-25T17:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78992",
    "user": "https://github.com/JohnCremona"
}
```

This looks very good.  After the discussion above I was expecting a much larger patch, but this is nice and simple, and works.

Applies fine to 4.4.rc0 and all tests in sage/quadratic_forms pass.

Positive review!



---

archive/issue_events_021050.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-29T05:19:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8681#event-21050"
}
```



---

archive/issue_comments_078993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78993",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_078994.json:
```json
{
    "body": "[city pictures](http://like-search.info/)",
    "created_at": "2010-05-26T08:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8681#issuecomment-78994",
    "user": "https://trac.sagemath.org/admin/accounts/users/bascorp2"
}
```

[city pictures](http://like-search.info/)
