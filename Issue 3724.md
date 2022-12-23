# Issue 3724: [with patch, depends on other ticket] faster hashs for Matrix_mod2_dense

Issue created by migration from https://trac.sagemath.org/ticket/3724

Original creator: malb

Original creation time: 2008-07-25 12:08:04

Assignee: malb

CC:  simonking

Keywords: m4ri, hash, matrix

Simon King requested faster hashing for matrices over GF(2). This patch implements it, but depends on #3324 and an updated M4RI.


---

Comment by malb created at 2008-07-25 12:08:26

implements faster hashing


---

Attachment

it seems, the patch is independent of the PNG fix.


---

Comment by malb created at 2008-08-24 12:24:42

Simon, can you review my patch?


---

Comment by SimonKing created at 2008-08-26 09:23:14

The patch applies to sage-3.1.1

Consider a little test:

```
sage: M=MatrixSpace(GF(2),10000,10000).random_element()
sage: M.set_immutable()
sage: time M.__hash__()
```

Without the patch, i had to interrupt sage after few ___minutes___ since it ate pretty much of my computer's memory. 

With the patch, we get

```
sage: time M.__hash__()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
-2570088162955604276
```


Well done, Martin! I give a positive review.

The patch contains a doc-test. One problem for me: Typing `M.__hash__?`, i don't see them. What is the user supposed to do in order to see the doc-string of the respective hash method?

I know that the following should be another ticket. But here are two items on my wish list:
 1. Can similar things be done with the hash of matrices over GF(p), p>2?
 2. Please also improve pickling of matrices! Example:
 {{{
sage: M=MatrixSpace(GF(2),1000,1000).random_element()
sage: timeit('x=loads(dumps(M))')
5 loops, best of 3: 2.33 s per loop
 }}}
 which is somehow slowish.


---

Comment by mabshoff created at 2008-08-26 09:30:00

Simon,

please open a thread on sage-devel. I assume the discussion will conclude that speed up is warranted and then we can open tickets for the new issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-26 09:53:44

Resolution: fixed


---

Comment by mabshoff created at 2008-08-26 09:53:44

Merged in Sage 3.1.2.alpha1


---

Comment by malb created at 2008-08-26 10:11:58

Replying to [comment:3 SimonKing]:


> The patch contains a doc-test. One problem for me: Typing `M.__hash__?`, i don't see them. What is the user supposed to do in order to see the doc-string of the respective hash method?

That could be a bug for introspection (or however that thingy is called). Could you open a ticket?
 
>  1. Can similar things be done with the hash of matrices over GF(p), p>2?

Yes it can, please open a Trac ticket and I'll do it as soon as I find some time. 

>  2. Please also improve pickling of matrices! Example:
>  {{{
> sage: M=MatrixSpace(GF(2),1000,1000).random_element()
> sage: timeit('x=loads(dumps(M))')
> 5 loops, best of 3: 2.33 s per loop
>  }}}
>  which is somehow slowish.

That is #3324 which is blocked by a problem on OSX 10.4 and libpng.


---

Comment by SimonKing created at 2008-08-26 13:06:19

Changing status from closed to reopened.


---

Comment by SimonKing created at 2008-08-26 13:06:19

Resolution changed from fixed to 


---

Comment by SimonKing created at 2008-08-26 13:06:19

Sorry, but i think i should re-open the ticket:

```
sage: M = MatrixSpace(GF(2),10000,10000).random_element()
sage: M.is_mutable()
True
sage: M.__hash__()
354973654957594997
```


A mutable object is not allowed to have a hash, AFAIK. 
On the other hand, the hash-value seems not to be cached:

```
sage: M[0,0]
1
sage: M[0,0]=0
sage: M.__hash__()
-8868398381897180811
```


So, the hash value has changed (i.e., was re-computed) by changing the matrix...

```
sage: N=copy(M)
sage: N.__hash__()
-8868398381897180811
```

... and has not changed by copying the matrix.

By consequence, it may be that everything is alright.

However, I re-open the ticket, because I think this should be addressed -- either by a new patch raising an exception when `M` is mutable, or by the assertion that "mutable objects have no hash" is a rule but no law, and that it is fine since the hash is not cached.

Cheers
     Simon


---

Comment by malb created at 2008-08-26 13:25:00

address review


---

Attachment

You're right, good catch. The attached patch addresses that issue.


---

Comment by mabshoff created at 2008-08-26 16:55:16

m4ri_hash2.patch looks good to me. Positive review.


---

Comment by mabshoff created at 2008-08-26 21:50:24

Resolution: fixed


---

Comment by mabshoff created at 2008-08-26 21:50:24

Merged m4ri_hash2.patch in Sage 3.1.2.alpha1


---

Comment by malb created at 2008-08-27 16:59:34

The new hash-ing method does not obey Sage's hashing rules. See Robert's comment at #3956. Obeying this rule however would come with a considerable speed penalty compared to `m4ri_hash.patch`.


---

Comment by malb created at 2008-08-27 16:59:34

Resolution changed from fixed to 


---

Comment by malb created at 2008-08-27 16:59:34

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-08-27 19:07:40

Martin,

can we move the latest issue to a new ticket? As is this ticket is getting rather messy, i.e. in HISTORY.txt as well as here.

Cheers,

Michael


---

Comment by malb created at 2008-08-27 19:51:18

your wish is my command.


---

Comment by malb created at 2008-08-27 19:51:18

Resolution: fixed
