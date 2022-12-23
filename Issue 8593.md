# Issue 8593: Add Lehmer code of Permutation as an infinite enumerated set

Issue created by migration from https://trac.sagemath.org/ticket/8593

Original creator: nborie

Original creation time: 2010-03-23 23:37:58

Assignee: nborie

CC:  sage-combinat

Keywords: code, permutation

The goal of this ticket is to implement Lehmer_codes as a parent (InfiniteEnumeratedSets()). One of the goal is to use this features to index Schubert evaluation points and Schubert polynomials.

There is also an iterator over all codes, and two methods for elements
is_dominant() (easy Schubert) and is_anti_dominant() (symmetric Schubert).


---

Attachment


---

Comment by nborie created at 2010-03-23 23:50:08

Changing status from new to needs_review.


---

Comment by nborie created at 2010-03-24 20:38:31

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-04-10 09:28:46

Hi Nicolas,

One quick remark. Since they are many different interesting code for permutations. I'd rather call this file permutations codes and maybe make an abstract class for those. For all the other code, the bijection is different. If you are interested you can have a look at

    Multivariate generalizations of the Foata-Schutzenberger equidistribition (with F. Hivert  and J.-C. Novelli), in  Fourth Colloquium on Mathematics and Computer Science: Algorithms, Trees, Combinatorics and Probabilities, DMTCS Proceedings, 2006
