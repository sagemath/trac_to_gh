# Issue 9496: Crypto lattice basis generator

Issue created by migration from https://trac.sagemath.org/ticket/9496

Original creator: rlindner

Original creation time: 2010-07-14 13:36:13

Assignee: mvngu

Keywords: cryptography, lattices

We introduce a generator for different types of integral lattice bases of row vectors relevant in cryptography.

It offers more variety and better usability than fplll's generator.

Contacts:
Richard Lindner <rlindner`@`cdc.informatik.tu-darmstadt.de>
Michael Schneider <mischnei`@`cdc.informatik.tu-darmstadt.de>



---

Comment by malb created at 2010-07-14 20:53:40

I think overall it looks fine, some small points:

 * I think the function is too specialised to be in the main namespace, how about crypto.generate_lattice ?
 * Could you break lines around 80 characters?
 * One shouldn't need to pass a seed, but instead just change the seed with set_random_seed()
 * Id' rename ntl_flag to ntl


---

Comment by malb created at 2010-07-14 22:43:10

Changing status from new to needs_work.


---

Comment by rlindner created at 2010-07-15 14:07:06

Specifically:

 * function is now: sage.crypto.gen_lattice()
 * lines are broken at 79 chars
 * set_random_seed() is honored, but option to use seed remains
 * _flag indicator is removed


---

Comment by rlindner created at 2010-07-15 14:07:06

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-07-15 15:36:25

Hi, I'm having trouble applying your patch on top of the other, many hunks fail. Did you forget to include an intermediate patch (14533?)? Or can you provide a patch with everything rolled into one patch?


---

Comment by rlindner created at 2010-07-15 16:21:56

Candidate #2


---

Attachment

I recreated 14532.patch to include all changes and could not delete the other file, so I did the next best thing.


---

Comment by malb created at 2010-07-15 18:36:06

apply after other patch


---

Attachment

I've just uploaded a referee patch which should be applied on top of your patch. It fixes a few formating issues I probably could do quicker than you. 

Note that this means that I cannot give this ticket a positive review anymore, I cannot referee my own patch. However, since I sign off on your patch iff my patch is applied afterwards, you can review my patch, i.e. accept my changes. Of course, if you have anything to criticise go for it!


---

Comment by malb created at 2010-07-15 19:02:20

btw. this is how the result looks like:

http://sage.math.washington.edu/home/malb/scratch_sage/sage-4.4/devel/sage/doc/output/html/en/reference/sage/crypto/lattice.html


---

Comment by rlindner created at 2010-07-15 19:58:21

Changing status from needs_review to positive_review.


---

Comment by rlindner created at 2010-07-15 19:59:23

Looks so much better, thanks!


---

Comment by mpatel created at 2010-07-20 10:06:54

I've updated the Author(s) and Reviewer(s) fields with guesses.  Please correct them, if I'm wrong.


---

Comment by mpatel created at 2010-07-20 10:06:54

Resolution: fixed


---

Comment by malb created at 2010-07-20 10:27:31

I didn't do much


---

Attachment

An addtional patch to fix some bugs in the dual lattice generation/ description. Candidate 3


---

Comment by malb created at 2010-07-21 08:37:57

Please open a new ticket for your bugfix since this ticket is already closed. Btw.:


```
sage: A
[   1    5   -3    1]
[-290  -14    1    1]
[ -13   -6    6   -1]
[  15   -1    3   62]

sage: A.matrix_from_rows(range(A.nrows())[::-1])
[  15   -1    3   62]
[ -13   -6    6   -1]
[-290  -14    1    1]
[   1    5   -3    1]

```

