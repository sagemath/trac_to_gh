# Issue 9401: pari(n).isprime(1) does not give the primality certificate to the user

Issue created by migration from https://trac.sagemath.org/ticket/9401

Original creator: zimmerma

Original creation time: 2010-07-01 08:12:38

Assignee: AlexGhitza

CC:  cremona mjo wstein robertwb

Keywords: prime number

The Pari `isprime` function is able to return a primality
certificate:

```
gp: isprime(2^31-1,1)

[2 3 1]

[3 5 1]

[7 3 1]

[11 3 1]

[31 2 1]

[151 3 1]

[331 3 1]
```

However when calling this function from Sage, the certificate is
lost:

```
sage: pari(2^31-1).isprime(1)
True
```



---

Comment by mjo created at 2012-01-16 04:47:26


```
sage: pari(3).isprime()
True
sage: pari(3).isprime(1)
False
sage: pari(3).isprime(2)
True
```


...what?


---

Comment by zimmerma created at 2012-01-16 07:57:47

Changing priority from minor to major.


---

Comment by zimmerma created at 2012-01-16 07:57:47

apparently something changed (in worse) since I reported this, since indeed we now get:

```
sage: pari(2^31-1).isprime(1)
False
```

I change the priority to "major".

Paul


---

Comment by zimmerma created at 2013-08-24 13:34:20

by the way I notice there is no indication on how to access or change the "arithmetic proof flag" mentioned in the documentation of `n.is_prime`.

And the documentation of `get_flag` is ill-formed in the terminal version.

Paul


---

Comment by zimmerma created at 2013-08-25 10:50:43

for the ill-formed documentation of `get_flag`, see #15096.


---

Attachment

the attached patch does several things:

1) it fixes two typos in `gen.pyx`

2) it corrects the behaviour of `pari(n).isprime(1)` which incorrectly was returning `False` for prime n

3) for prime n, now `pari(n).isprime(1)` returns a tuple `(True, cert)` where `cert` is the primality certificate (currently as Pari object, I didn't figure out how to convert it to a Python object)

Comments are welcome.

Paul


---

Comment by zimmerma created at 2013-08-25 12:45:08

Changing status from new to needs_review.


---

Comment by pbruin created at 2013-10-02 20:44:27

Changing status from needs_review to needs_work.


---

Comment by pbruin created at 2013-10-02 20:44:27

In principle OK, but needs to be rebased on #15124.

Also, it would be much cleaner to call `new_gen()` instead of initialising the `gen` and resetting the stack by hand:

```python
cdef GEN x
pari_catch_sig_on()
x = gisprime(self.g, flag)
if typ(x) != t_INT:
    # case flag=1 with prime input: x is the certificate
    return True, P.new_gen(x)
else:
    pari_catch_sig_off()
    return bool(signe(x))
```



---

Comment by rws created at 2014-03-01 16:37:40

Changing status from needs_work to needs_review.


---

Comment by rws created at 2014-03-01 16:37:40

Rebased on 6.2.base2, applied comment:7 by pbruin
----
New commits:


---

Comment by rws created at 2014-03-01 16:39:12

Only the last two commits apply. If I create a new branch without the first stray commits, will trac handle this?


---

Comment by pbruin created at 2014-03-01 17:53:32

Yes, this is no problem.  I did this (using `git rebase -i`) in the branch I just pushed, and made one trivial additional change (in Cython, `s != 0` turns out to be faster than `bool(s)`).  You can set this to `positive_review` if you are happy with this branch.


---

Comment by rws created at 2014-03-02 07:17:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-05 09:36:28

Resolution: fixed
