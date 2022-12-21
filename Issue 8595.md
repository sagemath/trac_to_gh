# Issue 8595: Fixed point of word morphism is broken on some tuple input

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-03-24 14:29:12

Assignee: slabbe

CC:  vdelecroix

From [sage-combinat-devel group](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3d5e4db608049516?hl=en) :


```

2010/3/23 Vincent Delecroix
> Hi,
>
> I tried the following and get an unexpected error
>
> {{{
> sage: s = WordMorphism({'a1': ['a1','a2'], 'a2':['a1']})
> sage: s.fixed_point('a1')
> Traceback
> ...
> KeyError: 'a'
> }}}
>
> and it does the same for tuples
>
> {{{
> sage: s = WordMorphism({('a', 1) : [('a', 1), ('a', 2)], ('a', 2) : [('a', 1)]})
> sage: s.fixed_point(('a', 1))
> Traceback
> ...
> KeyError: 'a'
> }}}
>
> Is it a bug or not the right way to do ?
>
> (On this example it looks strange but I really need product alphabet)
>
> Cheers,
> Vincent

```



---

Attachment


---

Comment by slabbe created at 2010-03-25 10:35:17

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2010-03-25 10:46:13

The bug seems to be resolved by the patch! Great.


---

Comment by vdelecroix created at 2010-03-25 10:46:13

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:49:59

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:49:59

Merged "trac_8595_fixed_point-sl.patch" in 4.4.alpha0.
