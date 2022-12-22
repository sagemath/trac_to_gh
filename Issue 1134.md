# Issue 1134: optimize creating elements of orders and number fields by coercing in lists

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-09 08:20:30

Assignee: was


```
On Nov 8, 2007 9:52 PM, mabshoff <Michael.Abshoff`@`fsmath.mathematik.uni-dortmund.de> wrote:
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



---

Comment by dmharvey created at 2007-11-14 23:30:01

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

Comment by cwitty created at 2007-12-01 03:06:20

I think it's worth applying this patch, even if it doesn't solve the whole problem.

In my tests, it applied cleanly, sage/rings/number_field/* doctests still passed, and the code looks reasonable.  I approve.


---

Comment by mabshoff created at 2007-12-01 11:42:20

Applied 1134.hg (1.4 kB) - added by dmharvey on 11/14/2007 03:30:21 PM.

What are we supposed to do about this now? Close this and open another ticket for the remaining issue?

Cheers,

Michael


---

Comment by davidloeffler created at 2009-07-20 19:59:29

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 19:59:29

Changing assignee from was to davidloeffler.


---

Comment by jason created at 2009-10-06 19:25:09

Changing status from new to needs_work.


---

Attachment


---

Comment by mhansen created at 2013-07-22 13:42:58

I posted a patch which adds a fast case for tuples / lists of coefficients in the power basis.  For the timings with Z_F, most of the time is spent checking the embedding.  I've added a check option to disable that check if you know that the element is already in the order.

The bundle which was attached had been previously merged in.


---

Comment by mhansen created at 2013-07-22 13:42:58

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-02-13 08:22:42

Patch applies with some fuzz to sage-6.0 if you use `patch -l`


---

Comment by vdelecroix created at 2014-06-13 18:31:55

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

Comment by vdelecroix created at 2014-06-13 18:31:55

Changing status from needs_review to needs_info.
