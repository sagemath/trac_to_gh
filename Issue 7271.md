# Issue 7271: some small polybori interface fixes

Issue created by migration from https://trac.sagemath.org/ticket/7271

Original creator: malb

Original creation time: 2009-10-23 16:41:21

Assignee: malb

CC:  burcin polybori drkirkby

Keywords: polybori, crypto

* implement var()
 * variables() is an iterator


---

Comment by malb created at 2009-10-23 16:42:23

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-10-23 17:49:48

Why does variables() return an iterator?  It returns a tuple for pretty much everything else in Sage.  See #7077


---

Comment by malb created at 2009-10-23 18:24:06

Because that's what PolyBoRi expects internally.


---

Comment by mhansen created at 2009-10-23 18:29:22

Can you explain in a bit more detail?  How is PolyBoRi using that method?


---

Comment by malb created at 2009-10-23 22:31:31

Hi Mike, sorry for being so brief earlier, I was in a rush.

PolyBoRi calls this function from various functions which are called by the `groebner_basis` function. The ones I could find quickly are:


```
polybori-0.6/pyroot/polybori/rank.py:    return p.lex_lead().variables().next()
polybori-0.6/pyroot/polybori/ll.py:      return Monomial(v).variables().next().index()
polybori-0.6/testsuite/py/parsegat.py:    return p.lead().variables().next()
```


As you can see, it calls next() immediatly on the result of `variables()`. Right now, certain GB computations will fail with an `AttributeError` because of this.


---

Comment by malb created at 2009-10-23 22:46:38

I just received word that this will be changed in PolyBoRi.


---

Comment by PolyBoRi created at 2009-10-26 07:18:18

Changing status from needs_review to needs_work.


---

Comment by PolyBoRi created at 2009-10-26 07:18:18

http://bitbucket.org/brickenstein/polybori/changeset/48fab65072e9/

http://bitbucket.org/brickenstein/polybori/changeset/e238ae62b9e6/

Regarding parsegat, as you can see, I moved a corrected version between our repositories (similar one-liner). But there is no dependency on parsegat.py .
The only funny thing about the recent versions of parsegat.py is that, you
can see a poor mathetician trying to recognize patterns from bad encoded circuits.
I still have nightmares from it.


---

Comment by malb created at 2009-10-28 16:27:53

Changing status from needs_work to needs_review.


---

Comment by malb created at 2009-10-28 16:27:53

I prepared a new SPKG and a new patch.

The SPKG is available at:

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.3.r1647-20091028.spkg


---

Attachment


---

Comment by malb created at 2009-10-28 16:28:51

Mike, I reversed the iterator change in the latest patch. Can you review it?


---

Comment by malb created at 2009-11-02 10:41:46

I am attaching a new deps file to this ticket, to address 

   http://groups.google.com/group/sage-devel/browse_thread/thread/122f067d8947148d/


---

Attachment

The only thing changed in the deps file (which isn't under revision control) is that PolyBoRi now depends on M4RI


---

Comment by drkirkby created at 2009-11-18 15:48:09

There are several issues I am aware of with m4ri, which should perhaps be sorted out before code is added that depends on it. 

#7171 - Although reported against HP-UX, this is more serious, as it is broken on Solaris too. 
#7037 - libm4ri thinks the C compiler is broken

I beleive the current version of PolyBoRi might actually build with Sun's compiler, but this would stop that, if it has a dependancy which does not.


---

Comment by drkirkby created at 2009-11-18 15:57:10

Oops, for some reason I was not aware of this ticket despite being CCed on it. Nor of #7375, which aims to address the issues in M4RI, so my comments are probably out of place. I will look at #7375 soon, but would be unable to review this ticket. 

Dave


---

Comment by malb created at 2009-12-03 14:11:39

Hi, I was wondering if I someone could review this ticket now that the M4RI issues are resolved?


---

Comment by mhansen created at 2009-12-07 08:39:06

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-07 08:39:06

The patch looks good.  I'll add it first thing after 4.3, which should hopefully be out in the next day or two.


---

Comment by mhansen created at 2010-01-04 03:24:03

Resolution: fixed
