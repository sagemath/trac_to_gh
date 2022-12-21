# Issue 174: all existing open source Hermite Normal Form implementations totally SUCK.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-12-01 02:15:15

Assignee: was

CC:  burcin

Hermite Normal form is the analogue of echelon form over the integers.
It's crucial for almost all efficient computations with Z-modules (infinite 
abelian groups, finite abelian groups, lattices, modular abelian varieties
via lattices, etc).  

MAGMA is 50 times faster even for small examples, and asymptotically
much faster than GAP, PARI, and NTL. 

See this page http://magma.maths.usyd.edu.au/users/allan/mat/hermite.html
which is mirrored here:
http://sage.math.washington.edu/sage/misc/hermite.html





---

Comment by was created at 2006-12-01 02:16:15

a student paper on fast HNF algorithms (and there are other papers out there)


---

Comment by was created at 2007-01-13 01:44:45

Changing type from defect to enhancement.


---

Attachment


---

Comment by was created at 2007-03-08 10:09:32

The attached paper by students describes the super-fast algorithm in MAGMA, and should
be reasonably easy to implement in SAGE given what we now have.


---

Attachment


---

Attachment


---

Attachment


---

Attachment

I've put the final hnf.hg bundle here:

  http://sage.math.washington.edu/home/was/patches/hnf.hg

This is a bundle that I made by cleanly applying all my relevant
patches to 2.10.2.alpha0, then do hg_sage.send(...). 

The code is well documented, works well (very well tested with
automated testing and doctstrings), but has a HUGE MEMORY LEAK somewhere:


```
sage: a = random_matrix(ZZ,200,x=0,y=9)
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'234M+'
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'239M+'
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'244M+'
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
'249M+'
```


I suspect the memleak is in the optimized GMP code I added to matrix_integer_dense, and will find out soon...


---

Comment by was created at 2008-02-17 01:28:28

Here's a big leak:


```
sage: a = random_matrix(ZZ,200,x=0,y=9); e = a.hermite_form(proof=False); p = a.pivots()
sage: get_memory_usage()
'192M+'
sage: w = e._add_row_and_maintain_echelon_form(random_matrix(ZZ,1,200), p)
sage: get_memory_usage()
'210M+'
```



---

Comment by was created at 2008-02-17 03:46:12

ok, the file at http://sage.math.washington.edu/home/was/patches/hnf.hg has all the HNF stuff all working with no known issues.

 finally!


---

Comment by mabshoff created at 2008-02-17 03:52:44

Ok, running the final bundle under valgrind with 

```
sage: a = random_matrix(ZZ,200,x=0,y=9)
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
sage: a._clear_cache(); e = a.hermite_form(proof=False); get_memory_usage()
```

doesn't leak at all. Excellent. So positive review on memory leak issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 11:55:15

FYI: The code has been merged, but still needs "official" review by a third party.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 03:10:21

The bundle has been extensively tested and I have verified via valgrind that it doesn't leak memory. While nobody external ever did a formal review  I am giving this a positive review due to the excessive amount of testing. Feel free to do a formal review, but please open another ticket in case  you come up with any issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 03:10:40

Merged in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-21 03:10:40

Resolution: fixed
