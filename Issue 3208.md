# Issue 3208: [with patch, needs review] a bunch of small changes to the tutorial

Issue created by migration from https://trac.sagemath.org/ticket/3208

Original creator: jhpalmieri

Original creation time: 2008-05-15 01:48:59

Assignee: somebody

Keywords: tutorial

I've reworded a bunch of things in the first few sections of the tutorial, plus small changes scattered throughout (like changing Sage to \sage).  As time permits, and if these changes are acceptable, I may get to the later parts.

Aside from random rewordings, I made the following changes and/or have the following comments:

1. at various points, I replaced things like $BLAH$ with \verb+BLAH+ or \code{BLAH} or \emph{BLAH}: when converted to html, these other things behave better than $BLAH$.

2. In section 2.2, there is a sentence "You do not have to specify the types of any of the input arguments."  This implies that it's possible to specify those types, I think, so I've removed the words "have to".

3. In section 2.3, one of the examples says

```
 sage: I = ComplexField().0
```

What does the '.0' do?  I can't find out where this might be documented.  Since it's not documented, I've removed its occurrences from this section.  (Replaced with CC(i), for instance.)





---

Comment by jhpalmieri created at 2008-05-15 03:41:09

lots of little changes to the tutorial


---

Attachment

Review: a very worthy effort!  Just two points.  Here:


```
The symbol \code{I} represents a formal square root of $-1$, as does 
\code{i}; of course this is not in $\Q$.  Neither is the square root 
of $-1$ in the complex numbers: 
```


the last part sounds to me as though you are saying that the square root of $-1$ is not in the complex numbers!  Perhaps change that to

```
Neither is the (complex) square root of $-1$ rational:
```


Secondly, I agree that `ComplexField().0` is obscure, as is `CC.0`, but it is just a synonym for `CC.gen(0)` or `CC.gen()` since `CC` has exactly one "generator" (though we had better not start to revive the old argument about what generators are...).  It would never have occurred to me to write `CC(i)` but it works fine.

I vote to accept this after the change of wording suggested (or similar).


---

Comment by jhpalmieri created at 2008-05-15 21:53:51

We could finesse the whole issue and just say "The square root of $-1$ is not rational", followed by 

```
 sage: i in QQ
 False
```


This ignores the fact that i is not actually an element of `CC` (which could mislead users, I suppose), but it means we don't have to use `CC(i)`, or `CC.0` which I think is more confusing, especially so early in the tutorial.  On the other hand, I've added the example

```
 sage: c = GF(3)(1)    # c is the element 1 of the field GF(3)
```

so maybe `CC(i)` is not so obscure?

I'm not sure what the right thing to do is.  I've changed it to the following:

The symbol \code{I} represents the square root of $-1$; \code{i} is a
synonym for \code{I}.  Of course, this is not in $\Q$:

```
 sage: i  # square root of -1
 I     
 sage: i in QQ
 False
```


Because of this change, I've re-inserted a mention of `CC` into the paragraph which follows this in the tutorial.

I'll include a patch, but I'll keep the old patch too, in case people want to compare.


---

Comment by jhpalmieri created at 2008-05-15 21:56:53

new version of patch; this replaces the old patch, if people agree it's actually better


---

Attachment

Now I remember that I used `CC(i)` a few lines later, so I've added a sentence of explanation at the relevant place.


---

Attachment

new version of patch; this replaces the old patch, if people agree it's actually better


---

Comment by cremona created at 2008-05-16 08:05:38

I vote for tut-new.2.patch.

Some of the issues which are now better explained here relate to the recent discussion on sage-devel  where behavious such as this is being discussed:

```
sage: sqrt(-1) in ComplexField()
False
sage: sqrt(2) in RealField()
False
```



---

Comment by jhpalmieri created at 2008-05-18 04:12:39

More patches, in response to a posting on sage-devel:

[http://groups.google.com/group/sage-devel/browse_frm/thread/a58a55f7e8f1a25a](http://groups.google.com/group/sage-devel/browse_frm/thread/a58a55f7e8f1a25a)


---

Attachment

new version; this incorporates the old patch, plus deals with issues from post on sage-devel


---

Comment by cremona created at 2008-05-26 11:08:26

I am happy with tut3.patch (the previous ones may be ignored).

Now if only users would read the tutorial, we may get fewer puzzled postings concerning complex numbers!


---

Attachment

(this has the same content as tut3.patch, but is an hg patch file)


---

Comment by mabshoff created at 2008-05-26 17:32:10

Merged in Sage 3.0.3.alpha0. 

John: Please post mercurial patches in the future so that the changes are properly credited to you in the repo. In this particular case I noticed too late that this is "only" a diff. 
 
Cheers,

Michael


---

Comment by mabshoff created at 2008-05-26 17:32:10

Resolution: fixed
