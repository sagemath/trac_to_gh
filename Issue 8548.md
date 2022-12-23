# Issue 8548: Permutation : a bad error message in hyperoctahedral_double_coset_type

Issue created by migration from https://trac.sagemath.org/ticket/8548

Original creator: giraudo

Original creation time: 2010-03-16 16:21:26

Assignee: sage-combinat

Obviously, the instructions

```
pp = Permutation([3, 1, 2])
pp.hyperoctahedral_double_coset_type()
```

lead to an error because the permutation has an odd size. However, there is an error in the raised error message : 

```
NameError: global name 'p' is not defined
```

The string should be

```
ValueError: pp is a permutation of odd size and has no coset-type
```



---

Comment by giraudo created at 2010-03-16 16:37:33

Resolution: fixed


---

Attachment


---

Comment by jbandlow created at 2010-03-16 16:48:42

Changing status from closed to needs_work.


---

Comment by jbandlow created at 2010-03-16 16:48:42

Samuele,

Thanks for catching this problem and submitting a patch!  However, you should not close tickets--that is for the release manager.  See [http://sagemath.org/doc/developer/trac.html](http://sagemath.org/doc/developer/trac.html) for more detail on the process.


---

Comment by jbandlow created at 2010-03-16 16:48:53

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-03-21 22:07:43

Hi Samuele,

You're able to fix problems that as not yet in sage ! Impressive :-) See #8420 where the problem should be solve. 

For the release manager: please close this as a duplicate.


---

Comment by mvngu created at 2010-04-19 03:07:59

Close as fixed by #8420.
