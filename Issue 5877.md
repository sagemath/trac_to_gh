# Issue 5877: calling a group character is broken

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2009-04-23 16:38:58

Assignee: saliola

CC:  wdj


```
sage: G = SymmetricGroup(3)
sage: h = G((2,3))
sage: triv = G.trivial_character()
sage: triv(h)
Traceback ...
```



---

Comment by saliola created at 2009-04-23 16:49:39

It's a small problem, with a small patch.


---

Comment by mabshoff created at 2009-04-23 23:09:00

Just to confirm: This is still a problem with the downgraded GAP in Sage 3.4.1.

Cheers,

Michael


---

Comment by dmharvey created at 2009-04-25 00:56:54

I know very little about GAP and the implementation of groups in Sage, but is this really the most efficient way to do this? It looks like the code has to enumerate the conjugacy classes of the group on every call, is that for real?


---

Comment by saliola created at 2009-04-25 11:04:57

Hello David, thanks for your comments.

Replying to [comment:3 dmharvey]:
> I know very little about GAP and the implementation of groups in Sage, but is this really the most efficient way to do this? It looks like the code has to enumerate the conjugacy classes of the group on every call, is that for real?

I know very little about GAP as well. I just followed the method described below, which I found at
[GAP-Forum](http://www.gap-system.org/ForumArchive/Hulpke.1/Alexande.1/Re__Char.11/2.html):

```
You will (if you like it or not) have to identify the class of the element g.
You can do this in general, by a specific test with \in (but see below):

gap> cl:=ConjugacyClasses(G);;
gap> First([1..Length(cl)],i->g in cl[i]);
4

So you know the class is class number 4, with the name:

    gap> ClassNames(CharacterTable(G))[4];
    "9a"

So the character value is:

gap> Irr(G)[3][4];
E(9)^2+E(9)^4+E(9)^5+E(9)^7
```


I did a bit more research, and I found a direct method to evaluate the class function via GAP. Of course, the computation still needs to determine the class to which the element belongs, but at least there won't be the extra interface overhead of going back and forth between Sage and GAP for each test. Moreover, GAP must have speedups for particular types of groups (the above method is for the generic case).

I'll replace the patch right-away with the better version.


---

Attachment

OK, can I just clarify that the problem with the original code is that the GAP Representative function doesn't return a canonical representative? i.e. if you start with two different group elements in the same class, convert them to classes and then ask for their Representative, you might get different answers?


---

Comment by saliola created at 2009-04-25 12:31:55

Replying to [comment:5 dmharvey]:
> OK, can I just clarify that the problem with the original code is that the GAP Representative function doesn't return a canonical representative? i.e. if you start with two different group elements in the same class, convert them to classes and then ask for their Representative, you might get different answers?

That is correct, here's an illustration.

```
sage: G = SymmetricGroup(3)
sage: g = G((1,2))
sage: h = G((2,3))
sage: gap(G).ConjugacyClass(h).Representative()
(2,3)
sage: gap(G).ConjugacyClass(g).Representative()
(1,2)
sage: gap(G).ConjugacyClass(g) == gap(G).ConjugacyClass(h)
True
```


Franco


---

Comment by dmharvey created at 2009-04-25 20:34:54

Ok, looks good to me.


---

Comment by mabshoff created at 2009-04-30 02:31:23

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 02:31:23

Merged in Sage 3.4.2.rc0.

Cheers,

Michael
