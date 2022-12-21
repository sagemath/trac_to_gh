# Issue 8572: Doc of poset appear as void if called from the console.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-03-21 19:52:16

Assignee: mvngu

CC:  jhpalmieri mpatel

Keywords: Poset, sphinx

Try

```
Poset?
```

under the console and nothing appear.
See

```
http://groups.google.com/group/sage-devel/t/b9baaa6943fc0df4
```

for a discussion: It is not clear if it's a sphinx bug or a Poset doc bug. I haven't been able to reproduce it from any other file.


---

Comment by jhpalmieri created at 2010-03-21 20:44:16

A little more data:

```
sage: from sage.misc.sageinspect import _sage_getdoc_unformatted
sage: from sagenb.misc.sphinxify import sphinxify
sage: r = _sage_getdoc_unformatted(Poset)
sage: len(sphinxify(r[:1438], format='text'))
1382
sage: len(sphinxify(r[:1439], format='text'))
0
```



---

Comment by hivert created at 2010-03-21 21:57:33

Changing assignee from mvngu to hivert.


---

Attachment

Hi John,

> A little more data:

```
sage: from sage.misc.sageinspect import _sage_getdoc_unformatted
sage: from sagenb.misc.sphinxify import sphinxify
sage: r = _sage_getdoc_unformatted(Poset)
sage: len(sphinxify(r[:1438], format='text'))
1382
sage: len(sphinxify(r[:1439], format='text'))
0
```


I don't know how you got it but this was exactly the problem: an extraneous space at the 1438th character ! Please review.

Florent


---

Comment by hivert created at 2010-03-21 22:10:29

Changing status from new to needs_review.


---

Comment by hivert created at 2010-03-21 22:10:29

> I don't know how you got it but this was exactly the problem: an extraneous space at the 1438th character ! Please review.

Note: it would be much better if sphinx raised a warning instead of failing silently. Should we open a ticket for this or report it upstream ?


---

Comment by jhpalmieri created at 2010-03-21 22:54:46

Replying to [comment:3 hivert]:
> > I don't know how you got it 

Binary search: `sphinxify(r[:n], format='text')` for various values of n.

> but this was exactly the problem: an extraneous space at the 1438th character ! Please review.
> 
> Note: it would be much better if sphinx raised a warning instead of failing silently. Should we open a ticket for this or report it upstream ?

Or maybe it's how we're invoking Sphinx?  I'm not sure.  We could also add the hack I suggested on sage-devel, as a backup plan for similar situations.  That could go on another ticket.


---

Comment by jhpalmieri created at 2010-03-21 22:54:46

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:48:07

Merged "trac_8572-poset_doc_fix-fh.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-16 18:48:07

Resolution: fixed
