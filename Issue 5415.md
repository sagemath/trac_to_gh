# Issue 5415: wrong definition of multifactorial?

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-01 22:56:37

Assignee: robertwb

The multifactorial method on integers is different than the one at http://mathworld.wolfram.com/Multifactorial.html and http://www.research.att.com/~njas/sequences/A007661; unless there are multiple competing definitions of multifactorial, this is a bug.

(The references give, for example, (5).multifactorial(3) == 10, whereas Sage currently returns 5.)


---

Comment by mabshoff created at 2009-03-02 06:40:37

Better luck in Sage 3.4.1.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-07-22 02:12:17

I think the problem is that not enough factors are included.  Actually, there are two problems: in the base case, it should return n, not 1; that is, make this change:

```
         # base case
         if 0 < n < k:
-            return ONE
+            return n
```

After making this change, I'm still getting the wrong answers for `a.multifactorial(3)` whenever a is congruent to 2 mod 3 (except for a=2), and for `a.multifactorial(4)` whenever a is congruent to 2 or 3 mod 4 (except for a=2,3).  It seems that not enough factors are used; for example, 10.multifactorial(4) should be 10 x 6 x 2 = 120, but Sage computes it as 10 x 6 = 60.

If we fix this, we can put in doctests like the following:

```
sage: L = sloane_sequence(6882)[2]  # optional - internet
Searching Sloane's online database...
sage: all([Integer(a).multifactorial(2) == L[a] for a in range(1,20)])    # optional - internet
True
```



---

Comment by kcrisman created at 2009-09-29 15:34:46

A careful look at Sloane's functions reveals that the base case is indeed =1, according to his definitions.  I'm not sure if this is standard, but Mathworld doesn't seem to talk about those cases carefully.  On the other hand, Wikipedia [http://en.wikipedia.org/wiki/Factorial#Multifactorials](http://en.wikipedia.org/wiki/Factorial#Multifactorials) suggests that this is somewhat standard.


---

Comment by kcrisman created at 2009-09-29 15:45:17

Or an even more careful look reveals that Sloane starts at n=0 - my bad.  So there is an inconsistency in the definitions.  Sloane's sequences agree with jhpalmieri, while Sage agrees with Wikipedia.

I'm ccing: the author of multifactorial in Sage, who will hopefully weigh in on what definition is okay.


---

Comment by robertwb created at 2009-09-29 18:18:42

I needed the double factorial for something (I can't even remember what now) so I just wrote this. It sounds like there's several competing definitions, but wikipedia is not necessarily the most authoritative. 

I would ask on sage-combinat what the "right" definition is, they're more likely to know.


---

Comment by kcrisman created at 2009-09-29 18:59:12

Can you do that?  I'm not subscribed to them.  Thanks.


---

Comment by ddrake created at 2009-09-30 05:01:32

I would certainly want (5).multifactorial(3) to be 10 and not 5.


---

Comment by kcrisman created at 2009-09-30 17:18:09

Replying to [comment:5 robertwb]:
> I needed the double factorial for something (I can't even remember what now) so I just wrote this. It sounds like there's several competing definitions, but wikipedia is not necessarily the most authoritative. 
(I think it was for making sure gamma(3/2) etc. were correct.)
> 
> I would ask on sage-combinat what the "right" definition is, they're more likely to know. 

But one should definitely document that there isn't a universally agreed-upon definition.

Can you indicate what one would change in integer.pyx?   Changing things that seem right yield horrible allocation errors.


---

Comment by prateek.cs14 created at 2015-11-02 09:08:18

I have tried to redefine multifactorial function.
Please review.
https://github.com/sagemath/sage/pull/52


---

Comment by nbruin created at 2015-11-02 16:45:24

Replying to [comment:14 prateek.cs14]:
> I have tried to redefine multifactorial function.
> Please review.
> https://github.com/sagemath/sage/pull/52

A few notes:
 - Python is notoriously (and if you believe some of Guido's commentary basicaly intentionally so) bad at recursion, so you should avoid it unless your really need it. Here you don't (and the current implementation carefully avoids deep recursion)
 - The current implementation does quite a bit of balancing of factors to ensure good multiplication performance. From what I see on your github branch, you've tacked on a new recursion case to what is called "reflection" there, essentially making the main body (everything below it) unreachable. That code looks like it's pretty carefully written. If you want to throw it out you should do so (and not just leave it in there as unreachable code) but then you should back up your proposal with some serious timings that show your code performs better under all circumstances.
 - Whenever you make a change like this you should adjust the documentation as well, ensuring that the new behaviour is reflected in the documentation and is properly tested (probably adding some new tests that differentiate between old and new behaviour.
 - Github presently really only is a mirror of the sage repository. It isn't really used for development. So before a change can be considered for inclusion, your change should be uploaded as a git branch here (using the `git-trac` command, probably).

I suspect that the appropriate change to make is in line 3967:

```diff
-         for i from 1 <= i <= n//k:
+         for i from 0 <= i <= n//k:
```

but I didn't check in detail.


---

Comment by nbruin created at 2015-11-02 22:25:57

Changing status from new to needs_info.


---

Comment by prateek.cs14 created at 2015-11-04 11:02:55

Thanks nbruin.
Please review the changes made.
https://github.com/prateekcs14/sage/commit/2cb944378c97bdad76a053e37d579d492f68d44c


---

Comment by nbruin created at 2015-11-06 16:47:25

Replying to [comment:17 prateek.cs14]:
> Thanks nbruin.
> Please review the changes made.
> https://github.com/prateekcs14/sage/commit/2cb944378c97bdad76a053e37d579d492f68d44c

Currently, the code is nicely interruptable with CTRL-C if a particularly long computation was being done. Does your code have that property? (you stripped out the `sig_on/sig_off`. On the other hand you revert to using (python?) integers instead of using gmp directly, so perhaps interrupts get enabled in that code)

Currently, the code is taking efforts to balance the size of the factors it was multiplying. This is a well-known technique to improve performance, because it reduces the number of multiplications where a particularly big number is involved (currently there is a 32/64 bit bug in that code, by the way) You strip that out. Do you have data to confirm this is not a problem?

You may want to try things like

```
sage: %timeit 10000001.multifactorial(2)
1 loops, best of 3: 8.47 s per loop
```

and possibly with larger numbers too. You should compare the current implementation with the new one.


---

Comment by prateek.cs14 created at 2015-12-05 09:38:13

Please review the changes made.I increased the sub_products by 1 and set i in k*i+residue from 0.
https://github.com/sagemath/sage/commit/8447058f8bb7f017bdefd7086300c4fc3b46ff21


---

Comment by prateek.cs14 created at 2015-12-10 09:50:49

Changing assignee from robertwb to prateek.cs14.


---

Comment by prateek.cs14 created at 2015-12-10 09:57:28

Remove assignee prateek.cs14.


---

Comment by git created at 2015-12-12 07:54:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nbruin created at 2015-12-12 17:16:46

Congratulations on getting a branch attached. Todo list:
 - make sure documentation is changed to reflect new behaviour and include doctests that confirm it
 - clean up your branch: as you can see in the diffs: `52 files changed, 7057 insertions, 5 deletions`. That's due to your "Merge" commit.

Since the intended change only touches 4 lines, it's probably easier to start with a fresh copy of current "develop", make the edits. and commit that. Then you need no merging at all.


---

Comment by nbruin created at 2015-12-12 17:16:46

Changing status from needs_info to needs_work.


---

Comment by git created at 2015-12-15 14:47:39

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kcrisman created at 2015-12-17 03:50:59

Your indentation is not really working well in your doctests - follow the developer guide and other code.  (Ask if you need help!)  I also agree with Nils' comments.


---

Comment by nbruin created at 2015-12-17 05:09:54

Also note that, as was remarked previously, the original behaviour of multifactorial was consistent with the description in its documentation. So, by changing the behaviour but not the documentation you are basically introducing a bug. Ideally you'd include a reference to a literature source to document which convention you are following, along with a description of what the routine in sage does.


---

Comment by prateek.cs14 created at 2015-12-17 14:29:20

Can I change the definition to 
" Computes the k-th factorial `n!^{(k)}` of self. For k=1
  this is the standard factorial, and for k greater than one it is
  the product of every k-th terms down from self to the smallest possible positive integer. 
  The recursive definition is used to extend this function to the negative integers."
Is this look fine ?


---

Comment by nbruin created at 2015-12-17 18:18:31

Some people have complained about using "self" in the docstring, and they have a point: in the call
`10.multifactorial(3)` there is never any mention of "self". I think it can be avoided here. Your description in words is pretty good, but requires careful reading to pry out the base cases. That might be difficult for non-native speakers. Perhaps

```
Returns the k-th multifactorial.

The k-th multifactorial n, denoted by n!^{(k)}, as implemented in Sage
 is defined by

n!^{(k)} = n for 1 <= n < k and
n!^{(k)} = n * ( (n-k)^{(k)} for n >= k

The recursive definition is used to extend this function to the negative
integers.
```


You'd have to figure out how to ensure that the formulas are rendered acceptably in all output formats of the sage documentation, though.

That said, your proposal is in the style of the current docstring, so I don't think a positive review would be held back by it.

Note that one of the doctests illustrates the behaviour:

```
      sage: 23.multifactorial(2)
      316234143225
      sage: prod([1..23, step=2])
      316234143225
```

It would be very instructive if you would change the parameters there to a case that distinguishes between the old and the new behaviour.


---

Comment by nbruin created at 2016-01-07 22:35:46

Looks like this ticket has been abandoned again.


---

Comment by iconjack created at 2016-08-16 06:46:47

Set assignee to iconjack.


---

Comment by iconjack created at 2016-08-17 01:37:35

The multifactorial implementation is optimized to limit large multiplications by computing e.g.  ((a*b)*(c*d))*((e*f)*(g*h)) instead of (((((((a*b)*c)*d)*e)*f)*g)*h). It's a little tricky, using bit patterns of the index to fold the multiplications, rather than doing it recursively. As others noted, there was an off-by-one error (two actually), which caused 5.factorial(3) to eval to 5 rather than 10.

A different bug was that for example 11.multifactorial(17) was returning 1 instead of 11.

WStein suggested using the already-existing prod function that already implements this balanced multiplication. However, prod is more general, not just integers. The current multifactorial uses GMP's integer functions, and may be faster. 

In the long run, I think that multifactorial, prod, balanced_list_prod, and interator_prod should be refactored, but since this is my first commit, I've decided to simply fix the bugs addressed in this ticket. There's another bug, related to non-integer values being passed in, but I'll make another ticket for that.

Also added a test case.


---

Comment by iconjack created at 2016-08-17 01:37:35

Changing status from needs_work to needs_review.


---

Comment by rws created at 2016-08-17 07:57:47

It seems your branch does not exist. Don't you use git-trac as in the documentation?


---

Comment by git created at 2016-08-18 03:54:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2016-09-19 06:06:45

Do you know why `residue` is not declared as `cdef int`?


---

Comment by iconjack created at 2016-09-20 00:48:00

Replying to [comment:38 vdelecroix]:
> Do you know why `residue` is not declared as `cdef int`?

No, I didn't change that line. I'll change it to cdef int and test but for now I'd like to get this change reviewed and committed.


---

Comment by vdelecroix created at 2016-09-21 06:14:46

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2016-09-21 06:14:46

Your changes look good. Two small things

1. add your name in the "Authors" field of the ticket

2. Add the following doctest in a `TESTS` block

```
sage: for a in range(1,20):
....:     for b in range(1,20):
....:         assert ZZ(a).multifactorial(b) == prod(x for x in range(a,0,-b))
```



---

Comment by chapoton created at 2017-05-24 20:19:11

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2017-05-24 20:19:11

New commits:


---

Comment by chapoton created at 2017-05-26 06:19:03

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2017-05-26 06:19:03

ok, this passes all tests. I am setting to positive.


---

Comment by vbraun created at 2017-05-27 23:42:49

Resolution: fixed
