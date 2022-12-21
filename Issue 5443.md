# Issue 5443: [with patch, needs review] Segfault in congruence subgroup element code

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-03-05 17:32:30

Assignee: craigcitro

CC:  davidloeffler

David Loeffler ran into the following segfault earlier:


```
sage: r,s,t,u = Gamma0(2).gens()
sage: r**(-1)*u**(-1) == t
BOOM
```


The attached patch fixes this, and adds a doctest. There's more work to be done: `matrix_integer_2x2` should inherit from `matrix_integer_dense`, but it doesn't yet. I have 98% of the code to do it done, but it needs to get cleaned up and submitted.

*HOWEVER*: I don't have a copy of sage-3.3 on my machine, so the patch is against sage-3.2.3. I


---

Comment by craigcitro created at 2009-03-05 17:36:46

(I apparently forgot to finish the description.)


---

Comment by davidloeffler created at 2009-03-05 22:48:09

Hi Craig,

Thanks for looking at this so quickly; but as I mentioned in my email to sage-devel, the problem doesn't occur under pre-3.3 versions because the output of Gamma0(2).gens() isn't the same. In 3.3 and 3.4, the matrices returned by Gamma0(2).gens() *should* satisfy r**(-1) * u**(-1) == t. 

In 3.4 with congroup_element's __cmp__ changed to _cmp_ as in your patch, it no longer segfaults; but the answer is False, even though the matrices have the same entries, which isn't great either. And one gets the same crash as before by doing

sage: (r**(-1) * u**(-1)).matrix() == t.matrix()

So I'm afraid I'm giving this a "needs work". I will do some further tinkering myself tomorrow.

David


---

Comment by craigcitro created at 2009-03-06 00:17:10

Ah, touche. Actually, in 3.2.3, I was getting a different crash (a `SIGBUS` instead of a `SIGSEGV`) ... 

In any event, I've written a much better fix now (I hope!). The underlying problem was that there were two ways to create elements of congruence subgroups whose underlying matrix was of type `Matrix_integer_dense` instead of `Matrix_integer_2x2` (and, as I said, the latter sadly doesn't yet derive from the former). Those came from places where `M2Z` was used to create matrices; these have been replaced by calls to create objects of the appropriate type. (I also had to add a wee bit of code so that congruence subgroup elements could determine their underlying list.) 

Hopefully this will fix the issues -- let me know if you run into anything else!


---

Attachment

The patch applies to my 3.4.rc1 merge tree without any rebase problems, so all we need is a review to get this in.

Cheers,

Michael


---

Comment by was created at 2009-03-08 06:52:49

It looks good to my eyes.


---

Comment by mabshoff created at 2009-03-08 06:57:33

Doctests fine in my current merge tree, so positive review via William's comment.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-08 07:13:10

Merged in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-08 07:13:10

Resolution: fixed
