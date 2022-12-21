# Issue 5844: [with patch, needs review] Improvement of {{{PermutationGroup_generic.has_element()}}} and {{{is_subgroup}}}

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-04-21 09:29:03

Assignee: SimonKing

Keywords: PermutationGroup has_element is_subgroup

The old version of `PermutationGroup_generic.has_element(self,item)` is

```
        item = PermutationGroupElement(item, self, check=False)
        return item in self.list()
```


Hence, the whole list of elements must be created! Instead, I suggest to invoke `PermutationGroup_generic.__contains__()`, hence:

```
        item = PermutationGroupElement(item, self, check=False)
        return item in self
```

The only difference between `has_element` and `__contains__` then is that the former may raise an error if one can not make a `PermutationGroupElement` out of the item.

The performance considerably improves. Here are indirect. The method `is_subgroup()` calls `has_element`.
With the patch, one has:

```
sage: G=SymmetricGroup(7)
sage: H=SymmetricGroup(6)
sage: H.is_subgroup(G)
True
sage: timeit('H.is_subgroup(G)')
625 loops, best of 3: 50.5 Âµs per loop
```


To my surprise, Gap is slower:

```
sage: timeit('gap(H).IsSubgroup(gap(G))')
5 loops, best of 3: 1.55 ms per loop
```


Without the patch, the computation is _very_ slow:

```
sage: time H.is_subgroup(G)
CPU times: user 3.94 s, sys: 0.51 s, total: 4.45 s
Wall time: 4.80 s
True
```


Last, I'd like to demonstrate the difference between `has_element()` and `__contains__()`:

```
sage: 1 in G
True  # since G(1) is the trivial permutation
sage: G.has_element(1) 
ERROR: An unexpected error occurred while tokenizing input
...
TypeError: 'sage.rings.integer.Integer' object is not iterable
```

The latter is what happens when trying conversion of 1 into a `PermutationGroupElement`.

__Conclusion__:

The change that I made is very small but yields a huge improvement. However, what was the original reason to write `has_element` in that way? Does `g in G` sometimes return an answer different from `g in G.list()`, if g is a `PermutationGroupElement`?


---

Comment by SimonKing created at 2009-04-21 09:29:35

Improved performance of has_element and thus of is_subgroup


---

Attachment


---

Comment by SimonKing created at 2009-04-21 09:45:14

Changing type from defect to enhancement.


---

Comment by wdj created at 2009-04-21 19:59:48

I got doc-test failures in these modules:


```
        sage -t  "devel/sage/sage/groups/perm_gps/permgroup.py"
        sage -t  "devel/sage/sage/groups/abelian_gps/abelian_group.py"
        sage -t  "devel/sage/sage/groups/abelian_gps/abelian_group_element.py"
        sage -t  "devel/sage/sage/groups/class_function.py"
```


I'm using gap4.4.10 but the error in permgroup.py seems to
be a result of this patch.


---

Comment by mabshoff created at 2009-04-21 22:15:48

Wiki text has no effect in the summary, so change it.

Cheers,

Michael


---

Comment by SimonKing created at 2009-04-22 07:43:06

Replying to [comment:3 wdj]:
> I got doc-test failures in these modules:
> ...

Here is the reason:

`G.has_element()` first turns the input `item` into a `PermutationGroupElement` with parent `G`, using `check=False`. So, from now on, the parent of `item` is `G`.

The old version then tests if it is contained in the list of elements. The new version tests whether `item in G`. The problem is that `item in G` just tries `PermutationGroupElement(item,G,check=True)` -- if there is an error then False is returned. 

But at that point, the parent of `item` is `G`, hence, `PermutationGroupElement(item,G,check=True)` does not raise an error, and True is returned!

Anyway. What was the reason to implement `has_element`? What is the purpose of it, in contrast to `__contains__`? 

If both are just tests for containment then `has_element` should be removed, respectively should be an alias for `__contains__`.


---

Attachment

Replace has_element by __contains__


---

Comment by SimonKing created at 2009-04-22 07:55:54

OK, here is a second patch, to be applied after the first. With it, all above-mentioned doc tests pass. Now, `G.has_element(x)` just returns `x in G`

Note that above I pointed out one difference between the old version of `has_element()` and `__contains__()`: In the old version, `G.has_element(1)` raised an error. Now, it does not, since `G.__contains__(1)` interpretes 1 as the trivial group element.

But, as much as I understand, this is the only mathematical difference between the old and the new version.


---

Comment by wdj created at 2009-04-25 00:28:52

Applies to 3.4.1.rc3 and seems to pass all tests (my copy has massive failures both due to the gap interface and the maxima interface, but these seem unrelated to these patches).

Postive. Review. Thanks Simon and sorry for the delay - it's the end of the semester here...


---

Comment by mabshoff created at 2009-04-25 01:09:51

Replying to [comment:8 wdj]:

Hi David,

> Applies to 3.4.1.rc3 and seems to pass all tests (my copy has massive failures both due to the gap interface and the maxima interface, but these seem unrelated to these patches).

Why don't you doctest on sage.math? You can do it in parallel, there is *always* a binary and it works unless otherwise noted in the release notes.

> Postive. Review. Thanks Simon and sorry for the delay - it's the end of the semester here...

Do not give positive reviews to any ticket that does not pass doctests, even if you assume it is unrelated to failures you see. The whole point of doctesting is to also verify that no side effects cause any trouble and given that you see GAP failures I cannot honestly see how this patch could not potentially cause trouble here. 

I am doctesting this patch against my current merge tree to see if there are any issues.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-25 02:03:20

For the record: The two patches merge in 3.4.2.a0 and pass all doctests on sage.math.

Cheers,

Michael


---

Comment by SimonKing created at 2009-04-26 10:37:38

Replying to [comment:10 mabshoff]:
> For the record: The two patches merge in 3.4.2.a0 and pass all doctests on sage.math.

Shouldn't the ticket be closed, then? 

Cheers,
 Simon


---

Comment by mabshoff created at 2009-04-26 10:43:28

> Shouldn't the ticket be closed, then? 

Well, I did not merge the patches yet, so no.
 
> Cheers,
>  Simon

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 19:05:31

Resolution: fixed


---

Comment by mabshoff created at 2009-05-13 19:05:31

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
