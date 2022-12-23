# Issue 9065: Add support for facade parents

Issue created by migration from https://trac.sagemath.org/ticket/9065

Original creator: nborie

Original creation time: 2010-05-27 13:02:37

Assignee: nthiery

CC:  sage-combinat

Keywords: facade, parent, TestSuite

The goal of this tickets is to add support for facade parents; see:
http://groups.google.com/group/sage-devel/browse_thread/thread/a5ea008c24c17956/00ab8c6d2a16f57a

The main issue currently is that facade parents (Primes, NonNegativeIntegers, SymmetricFunctions, ...) are not aware that they are, which breaks some of the generic TestSuite tests.

This involves:
 - Creating a category or abstract class for facade parents
   Such parents should declare a list of parents they are facade
   for.
 - Adding a method P.check_element(x) (find a better name!) in Sets.ParentMethods which checks that the parent of x is P. Override this method for facade parents to check that the parent of x is one of the declared parents of P.
 - Fix P._test_one(), P._test_zero(), P._test_an_element() (and maybe others) to use P.check_element(x) instead of x in P.


---

Comment by nthiery created at 2011-03-28 14:49:19

Changing status from new to needs_review.


---

Comment by hivert created at 2011-04-04 20:43:43

Hi Nicolas, 

I started to review this. I currently have only the following interface
remark: id there a reason why you need to pass a tuple for parameter
`facade` whereas for `category` you can pass either a category or a
tuple ? For example, why do you force the user to write 

```
Parent.__init__(self, facade = (IntegerRing(), ), category = Sets()) 
```

instead of

```
Parent.__init__(self, facade = IntegerRing(), category = Sets()) 
```



---

Comment by hivert created at 2011-04-04 20:49:31

Sorry for replying to myself...

> I started to review this. I currently have only the following interface
> remark: id there a reason why you need to pass a tuple for parameter
> `facade` whereas for `category` you can pass either a category or a
> tuple ?

Actually, it seems that the code in `Parent` allows for it. So I guess
that the example where the one parameter tuple occur could be simplified. I'm
writing a review patch on the sage-combinat queue.


---

Comment by nthiery created at 2011-04-05 11:38:09

Replying to [comment:6 hivert]:
> 
> Actually, it seems that the code in `Parent` allows for it. So I guess
> that the example where the one parameter tuple occur could be simplified. I'm
> writing a review patch on the sage-combinat queue.

Good point :-) +1 on that change.


---

Comment by nthiery created at 2011-04-21 10:51:34

Hi!

I folded in Florent's reviewer patch for the above issue, added facade option in SearchForest, updated an example there as well as NN and Primes to be facades, and fixed some trivially failing tests reported by the patchbot. The patch should be good to go. Florent: can you confirm?


---

Comment by hivert created at 2011-04-22 22:17:34

Replying to [comment:8 nthiery]:
> I folded in Florent's reviewer patch for the above issue, added facade option in SearchForest, updated an example there as well as NN and Primes to be facades, and fixed some trivially failing tests reported by the patchbot. The patch should be good to go. Florent: can you confirm?

Unfortunately not ! I spotted a few more wrong sphinx markup. Please have a look at my review patch on trac. Otherwise, it is ready to go.


---

Comment by nthiery created at 2011-04-23 01:44:31

I checked your patch, folded it in, and reuploaded. Thanks!


---

Comment by nthiery created at 2011-04-23 01:44:31

Changing status from needs_review to positive_review.


---

Attachment

Fixed another trivial failing test in a separate file. Hopefuly the last one!

Florent just checked it, and is ok to leave the positive review.


---

Comment by jdemeyer created at 2011-05-03 12:28:29

Resolution: fixed
