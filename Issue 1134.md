# Issue 1134: optimize creating elements of orders and number fields by coercing in lists

archive/issues_001134.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nOn Nov 8, 2007 9:52 PM, mabshoff <Michael.Abshoff@fsmath.mathematik.uni-dortmund.de> wrote:\n[...]\n> > Woah!  Can someone explain to me the various calls above?  I'd think\n> > this should take epsilon time to coerce the elements of the sequence.\n> > Or perhaps is there another better way to coerce into Z_F (or,\n> > equivalently for me, F)?\n> >\n> \n> There is without a doubt something fishy going on with coercion. See\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n> also malb's report with polynomial rings at\n> http://www.sagetrac.org/sage_trac/ticket/1046\n\nI have some doubt that John Voight's observation above has  to do with\nMalb's speed regression report.    I think it's just that a particular way\nof constructing elements in an order (coercing from a list) hasn't been optimized\none speck since when we implement orders a month ago.   And code that\nhas had zero optimization tends to be slow.  The sort answer is that *right now*\nit's vastly faster to construct the element of the order via doing arithmetic\ninstead of explicitly coercing in a list, since we've optimized arithmetic more.\nSee the timings and examples in the worksheet below. \n```\n\ncoerce speed question from john voight\nsystem:sage\n\n```\nid=0|\ndef stupid_function(n):\n     Z_F = NumberField(x^2-x-1, 't').maximal_order()\n     for i in range(n):\n         Z_F([5,1])\n```\n\n```\nid=1|\ntime stupid_function(10^4)\n///\nCPU time: 7.88 s,  Wall time: 9.31 s\n```\n\n```\nid=10|\ndef stupid_function(n):\n     Z_F = NumberField(x^2-x-1, 't').maximal_order()\n     a,b = Z_F.gens()\n     for i in range(n):\n         w = a + 5*b\n```\n\n```\nid=11|\ntime stupid_function(10^4)\n///\nCPU time: 0.05 s,  Wall time: 0.05 s\n```\n\n```\nid=2|\ndef stupid_function(n):\n     K = NumberField(x^2-x-1, 't')\n     for i in range(n):\n         K([5,1])\n```\n\n```\nid=3|\ntime stupid_function(10^4)\n///\nCPU time: 4.81 s,  Wall time: 4.88 s\n```\n\n```\nid=4|\ndef stupid_function(n):\n     K = NumberField(x^2-x-1, 't')\n     v = [5,1]\n     for i in range(n):\n         K(v)\n```\n\n```\nid=5|\ntime stupid_function(10^4)\n///\nCPU time: 4.78 s,  Wall time: 4.81 s\n```\n\n```\nid=6|\ndef stupid_function(n):\n     K = NumberField(x^2-x-1, 't')\n     one = K(1); t = K.gen(); five = K(5)\n     for i in range(n):\n         w = five*t + one\n```\n\n```\nid=7|\ntime stupid_function(10^4)\n///\nCPU time: 0.04 s,  Wall time: 0.04 s\n```\n\n```\nid=8|\ndef stupid_function(n):\n     K = NumberField(x^2-x-1, 't')\n     t = K.gen()\n     for i in range(n):\n         w = 5*t + 1\n```\n\n```\nid=9|\ntime stupid_function(10^4)\n///\nCPU time: 0.38 s,  Wall time: 0.38 s\n```\n\n\n\n```\nid=12|\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1134\n\n",
    "created_at": "2007-11-09T08:20:30Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "optimize creating elements of orders and number fields by coercing in lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1134",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
On Nov 8, 2007 9:52 PM, mabshoff <Michael.Abshoff@fsmath.mathematik.uni-dortmund.de> wrote:
[...]
> > Woah!  Can someone explain to me the various calls above?  I'd think
> > this should take epsilon time to coerce the elements of the sequence.
> > Or perhaps is there another better way to coerce into Z_F (or,
> > equivalently for me, F)?
> >
> 
> There is without a doubt something fishy going on with coercion. See
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> also malb's report with polynomial rings at
> http://www.sagetrac.org/sage_trac/ticket/1046

I have some doubt that John Voight's observation above has  to do with
Malb's speed regression report.    I think it's just that a particular way
of constructing elements in an order (coercing from a list) hasn't been optimized
one speck since when we implement orders a month ago.   And code that
has had zero optimization tends to be slow.  The sort answer is that *right now*
it's vastly faster to construct the element of the order via doing arithmetic
instead of explicitly coercing in a list, since we've optimized arithmetic more.
See the timings and examples in the worksheet below. 
```

coerce speed question from john voight
system:sage

```
id=0|
def stupid_function(n):
     Z_F = NumberField(x^2-x-1, 't').maximal_order()
     for i in range(n):
         Z_F([5,1])
```

```
id=1|
time stupid_function(10^4)
///
CPU time: 7.88 s,  Wall time: 9.31 s
```

```
id=10|
def stupid_function(n):
     Z_F = NumberField(x^2-x-1, 't').maximal_order()
     a,b = Z_F.gens()
     for i in range(n):
         w = a + 5*b
```

```
id=11|
time stupid_function(10^4)
///
CPU time: 0.05 s,  Wall time: 0.05 s
```

```
id=2|
def stupid_function(n):
     K = NumberField(x^2-x-1, 't')
     for i in range(n):
         K([5,1])
```

```
id=3|
time stupid_function(10^4)
///
CPU time: 4.81 s,  Wall time: 4.88 s
```

```
id=4|
def stupid_function(n):
     K = NumberField(x^2-x-1, 't')
     v = [5,1]
     for i in range(n):
         K(v)
```

```
id=5|
time stupid_function(10^4)
///
CPU time: 4.78 s,  Wall time: 4.81 s
```

```
id=6|
def stupid_function(n):
     K = NumberField(x^2-x-1, 't')
     one = K(1); t = K.gen(); five = K(5)
     for i in range(n):
         w = five*t + one
```

```
id=7|
time stupid_function(10^4)
///
CPU time: 0.04 s,  Wall time: 0.04 s
```

```
id=8|
def stupid_function(n):
     K = NumberField(x^2-x-1, 't')
     t = K.gen()
     for i in range(n):
         w = 5*t + 1
```

```
id=9|
time stupid_function(10^4)
///
CPU time: 0.38 s,  Wall time: 0.38 s
```



```
id=12|

```

Issue created by migration from https://trac.sagemath.org/ticket/1134





---

archive/issue_comments_006852.json:
```json
{
    "body": "Attached bundle partially addresses this issue, by implementing a fast QQ => quadratic number field element coercion. Currently this only affects implicit coercions, but when Robert+David's new coercion framework is finished, it should help explicit coercions too. But it still doesn't totally address the issue for this ticket.\n\nExample:\n\n```\ndef stupid_function(n):\n    Z_F = NumberField(x^2-x-1, 't')\n    y = Z_F.gen()\n    u = 2/3\n    for i in range(n):\n        z = y + u\n\ntime stupid_function(50000)\n```\n\n\nBefore:\n\n```\nTime: CPU 13.68 s, Wall: 14.07 s\n```\n\nAfter:\n\n```\nTime: CPU 0.25 s, Wall: 0.52 s\n```",
    "created_at": "2007-11-14T23:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6852",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attached bundle partially addresses this issue, by implementing a fast QQ => quadratic number field element coercion. Currently this only affects implicit coercions, but when Robert+David's new coercion framework is finished, it should help explicit coercions too. But it still doesn't totally address the issue for this ticket.

Example:

```
def stupid_function(n):
    Z_F = NumberField(x^2-x-1, 't')
    y = Z_F.gen()
    u = 2/3
    for i in range(n):
        z = y + u

time stupid_function(50000)
```


Before:

```
Time: CPU 13.68 s, Wall: 14.07 s
```

After:

```
Time: CPU 0.25 s, Wall: 0.52 s
```



---

archive/issue_events_003030.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-16T11:53:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3030"
}
```



---

archive/issue_comments_006853.json:
```json
{
    "body": "I think it's worth applying this patch, even if it doesn't solve the whole problem.\n\nIn my tests, it applied cleanly, sage/rings/number_field/* doctests still passed, and the code looks reasonable.  I approve.",
    "created_at": "2007-12-01T03:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6853",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I think it's worth applying this patch, even if it doesn't solve the whole problem.

In my tests, it applied cleanly, sage/rings/number_field/* doctests still passed, and the code looks reasonable.  I approve.



---

archive/issue_comments_006854.json:
```json
{
    "body": "Applied 1134.hg (1.4 kB) - added by dmharvey on 11/14/2007 03:30:21 PM.\n\nWhat are we supposed to do about this now? Close this and open another ticket for the remaining issue?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-01T11:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Applied 1134.hg (1.4 kB) - added by dmharvey on 11/14/2007 03:30:21 PM.

What are we supposed to do about this now? Close this and open another ticket for the remaining issue?

Cheers,

Michael



---

archive/issue_comments_006855.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T19:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6855",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_006856.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6856",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_006857.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-10-06T19:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6857",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_006858.json:
```json
{
    "body": "Attachment [trac_1134.patch](tarball://root/attachments/some-uuid/ticket1134/trac_1134.patch) by @mwhansen created at 2013-07-22 13:39:33",
    "created_at": "2013-07-22T13:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6858",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_1134.patch](tarball://root/attachments/some-uuid/ticket1134/trac_1134.patch) by @mwhansen created at 2013-07-22 13:39:33



---

archive/issue_comments_006859.json:
```json
{
    "body": "I posted a patch which adds a fast case for tuples / lists of coefficients in the power basis.  For the timings with Z_F, most of the time is spent checking the embedding.  I've added a check option to disable that check if you know that the element is already in the order.\n\nThe bundle which was attached had been previously merged in.",
    "created_at": "2013-07-22T13:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6859",
    "user": "https://github.com/mwhansen"
}
```

I posted a patch which adds a fast case for tuples / lists of coefficients in the power basis.  For the timings with Z_F, most of the time is spent checking the embedding.  I've added a check option to disable that check if you know that the element is already in the order.

The bundle which was attached had been previously merged in.



---

archive/issue_comments_006860.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-22T13:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6860",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_003031.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3031"
}
```



---

archive/issue_events_003032.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3032"
}
```



---

archive/issue_events_003033.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3033"
}
```



---

archive/issue_events_003034.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3034"
}
```



---

archive/issue_comments_006861.json:
```json
{
    "body": "Patch applies with some fuzz to sage-6.0 if you use `patch -l`",
    "created_at": "2014-02-13T08:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6861",
    "user": "https://github.com/rwst"
}
```

Patch applies with some fuzz to sage-6.0 if you use `patch -l`



---

archive/issue_events_003035.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3035"
}
```



---

archive/issue_events_003036.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3036"
}
```



---

archive/issue_comments_006862.json:
```json
{
    "body": "With some careful merge I was able to make the patch applied and work on sage-6.3.beta3. But, the map `list_to_quadratic_field_element` is completely useless as there is no gain at all. Moreover, it is one more map added to the list of conversions. So I would suggest to not add it with that ticket.\n\nOne interesting optimization in the ticket is the `check` parameter added to the `_element_constructor_`. Do you agree if I provide a branch that contains only that?\n\nAlso, as it was said in comment:9 most of the time in the construction is spent in checking. So it would be worth to optimize it. The longest part comes from decomposing a vector on a given basis as the timings below show.\n\nThe construction takes roughly 600 micro seconds\n\n```\nsage: K = NumberField(x^2-x-1, 't')\nsage: Z_F = K.maximal_order()\nsage: x = K([5,1])\nsage: %timeit Z_F(x)\n1000 loops, best of 3: 674 \u00b5s per loop\n```\nBut most of the time is spent in checking that some vector belong to some submodule\n\n```\nsage: %timeit K.vector_space()      # <--- this is very quick\n1000000 loops, best of 3: 431 ns per loop\nsage: embedding = K.vector_space()[2]\nsage: embedding\nIsomorphism map:\n  From: Number Field in t with defining polynomial x^2 - x - 1\n  To:   Vector space of dimension 2 over Rational Field\nsage: %timeit embedding(x)          # <--- this is quick\n10000 loops, best of 3: 49.8 \u00b5s per loop\nsage: v = phi(x)\nsage: %timeit v in Z_F._module_rep  # <--- this is damn slow\n1000 loops, best of 3: 608 \u00b5s per loop\n```\nAnd in `__contains__` of `FreeModule`, the mess comes from calling `coordinates` that decompose the vector on the basis of the module:\n\n```\nsage: V = Z_F._module_rep\nsage: %timeit V.coordinates(v)\n1000 loops, best of 3: 612 \u00b5s per loop\n```",
    "created_at": "2014-06-13T18:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6862",
    "user": "https://github.com/videlec"
}
```

With some careful merge I was able to make the patch applied and work on sage-6.3.beta3. But, the map `list_to_quadratic_field_element` is completely useless as there is no gain at all. Moreover, it is one more map added to the list of conversions. So I would suggest to not add it with that ticket.

One interesting optimization in the ticket is the `check` parameter added to the `_element_constructor_`. Do you agree if I provide a branch that contains only that?

Also, as it was said in comment:9 most of the time in the construction is spent in checking. So it would be worth to optimize it. The longest part comes from decomposing a vector on a given basis as the timings below show.

The construction takes roughly 600 micro seconds

```
sage: K = NumberField(x^2-x-1, 't')
sage: Z_F = K.maximal_order()
sage: x = K([5,1])
sage: %timeit Z_F(x)
1000 loops, best of 3: 674 µs per loop
```
But most of the time is spent in checking that some vector belong to some submodule

```
sage: %timeit K.vector_space()      # <--- this is very quick
1000000 loops, best of 3: 431 ns per loop
sage: embedding = K.vector_space()[2]
sage: embedding
Isomorphism map:
  From: Number Field in t with defining polynomial x^2 - x - 1
  To:   Vector space of dimension 2 over Rational Field
sage: %timeit embedding(x)          # <--- this is quick
10000 loops, best of 3: 49.8 µs per loop
sage: v = phi(x)
sage: %timeit v in Z_F._module_rep  # <--- this is damn slow
1000 loops, best of 3: 608 µs per loop
```
And in `__contains__` of `FreeModule`, the mess comes from calling `coordinates` that decompose the vector on the basis of the module:

```
sage: V = Z_F._module_rep
sage: %timeit V.coordinates(v)
1000 loops, best of 3: 612 µs per loop
```



---

archive/issue_comments_006863.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-06-13T18:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1134#issuecomment-6863",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_events_003037.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3037"
}
```



---

archive/issue_events_003038.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1134",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1134#event-3038"
}
```
