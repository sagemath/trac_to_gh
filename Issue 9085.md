# Issue 9085: random_element fails for a cartesian product of fields

Issue created by migration from https://trac.sagemath.org/ticket/9085

Original creator: cremona

Original creation time: 2010-05-29 11:24:12

Assignee: AlexGhitza

CC:  nthiery

Keywords: random element cartesian product

Victor Miller reports:

```
Here's something a bit odd:

sage: F = GF(2)
sage: A = CartesianProduct(F,F)
sage: print A.random_element()

This gets a trace back and the message

TypeError: You must specify the names of the variables 
```


Here is what is happening (certainly a bug).  In the code which picks a random element from F, F is treated as a sequence and then
subscripted with a random subscript.  But (as you can verify)
evaluating F[0] or F[1] raises an error, since the `__getitem__` method of a field is used to create polynomial rings (as in F['x']).

This does not happen when you just do F.random_element() since that
has an independent implementation.

I think the fault lies in line 125 of /sage/misc/prandom.py in the
function choice() which says

```
return _pyrand().choice(seq)
```

but in your example "seq" is the field F.  It would work if that said list(seq), since

```
_pyrand().choice(F)
```

fails but

```
_pyrand().choice(list(F))
```

works.  But it would be more efficient if that choice function tried
to call a random_element() function on its  argument instead --
imagine if the field was very large, it would be stupid to construct a list of its elements for each random choice. 



---

Comment by cremona created at 2010-05-29 17:21:19

Suggestion:  in the {{{__item__}} method for rings, which constructs a polynomial ring (so that mathematicians can be happy writing things like ZZ['x']), it would be possible to test if ring R is finite and the argument was a non-negative integer n, to return the n'th element of list(R).


---

Comment by chapoton created at 2016-02-05 12:27:42

This works now.

```
sage: F = GF(1951)
sage: A = F.cartesian_product(F)
sage: A.random_element()
(1405, 126)
sage: A.random_element()
(1151, 1050)
```



---

Comment by chapoton created at 2016-02-05 12:27:42

Changing status from new to needs_review.


---

Comment by nthiery created at 2016-02-05 13:22:44

And, thanks to #18411, also with the original syntax:

```
    sage: F = GF(2)
    sage: A = CartesianProduct(F,F)
    sage: print A.random_element()
    (1,0)
```


Thanks Frédéric for spotting this outdated ticket.


---

Comment by nthiery created at 2016-02-05 13:22:44

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-02-23 22:53:28

Resolution: invalid
