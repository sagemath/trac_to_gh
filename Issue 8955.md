# Issue 8955: random_matrix(GF(2),2,1) always returns all 1 matrix

Issue created by migration from https://trac.sagemath.org/ticket/8955

Original creator: malb

Original creation time: 2010-05-12 10:44:22

Assignee: jason, was

Reported by Roberto Nóbrega on [sage-devel]:

```
Hello, all!

After running

random_matrix(GF(2), 2, 1)

I always get the same matrix, [[1][1]].

Also, the following code

freq = {}
for _ in range(1000):
    M = random_matrix(GF(2), 2, 2)
    M.set_immutable()
    if M not in freq:
        freq[M] = 1
    else:
        freq[M] += 1
show(freq)

gives a very different result from the uniform distribution that I was
expecting. For example, the all-ones 2x2 matrix is the more probable,
and matrices with a full-zero-row does not appear, although matrices
with a full-zero-column does. In general, I noticed that the more
"1's" the matrix has, the more probable it is.

Am I missing something?

Regards,
Roberto.
```



---

Comment by ylchapuy created at 2010-08-15 20:16:13

What is the status of this?


---

Comment by malb created at 2010-08-15 20:18:15

Changing status from new to needs_review.


---

Comment by malb created at 2010-08-15 20:18:15

I always forget to toggle the right status.


---

Comment by ylchapuy created at 2010-08-15 20:35:27

I agree with the proposed solution, but I think there should be some explanations in the docstring about what `density` means exactly.
Seeing 

```
def random_matrix(R, nrows, ncols=None, sparse=False, density=None, *args, **kwds):
    ...
    - ``density``: Integer (default: 1)
    ...
```

seems strange to me.


---

Comment by ylchapuy created at 2010-08-15 20:35:27

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-08-15 21:41:19

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-08-15 21:41:19

I've updated the patch accordingly (and added the ticket number)


---

Comment by ylchapuy created at 2010-08-15 21:53:17

Changing status from needs_review to needs_work.


---

Comment by ylchapuy created at 2010-08-15 21:53:17

Hum, I don't think it's ok now...
My understanding is that:

 * we should stare that default is None
 * we should explain that in this case each element is random and *can be 0*
 * if a density is given, it's the rate of *nonzero* element (thus for GF(2) a density of 1 means an all 1 matrix)
 * by the way, density should be float, not Integer, or?


---

Comment by malb created at 2010-08-16 14:50:37

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-08-16 14:50:37

I've updated the attached patch

 * fixed the docstring as requested
 * fixed the behaviour of randomize() for dense matrices over GF(2) 
 * fixed some docstrings on the way

The patch depends on#9475.


---

Comment by malb created at 2010-08-16 15:02:58

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-08-16 15:02:58

There are some doctest failures due to changes of random matrix generation


---

Comment by malb created at 2010-08-16 15:38:23

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-08-16 15:38:23

I fixed all known doctest failures. It would be good if this patch was reviewed & applied quickly since it is the kind of patch which will bitrot quickly since it touches quite a few files.


---

Comment by ylchapuy created at 2010-08-18 11:15:40

I added a minimal reviewer's patch. Otherwise, everything is fine, applies with minimal fuzz to sage4.5.3.alpha1, all doctests pass. Ok for merging.


---

Comment by ylchapuy created at 2010-08-18 11:15:40

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-08-18 11:35:51

The reviewer patch is fine by me too.


---

Comment by mpatel created at 2010-09-18 07:45:03

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-18 07:45:03

Could someone rebase the patch(es) here against 4.6.alpha1 when it's released (soon) and restore the positive review?


---

Attachment


---

Comment by malb created at 2010-09-20 15:53:13

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-09-20 15:53:13

The updated patch is rebased to 4.6.alpha1. Apply `random_matrix.patch` only.


---

Comment by jason created at 2010-09-23 23:02:46

malb: based on the comment above, should you restore the positive review?


---

Comment by ylchapuy created at 2010-09-27 14:28:36

Changing status from needs_review to positive_review.


---

Attachment

Reviewer's patch also updated ;)
Positive review. (I'm quite sure malb will confirm)


---

Comment by mpatel created at 2010-09-28 10:57:28

Resolution: fixed
