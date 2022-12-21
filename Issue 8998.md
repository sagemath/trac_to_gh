# Issue 8998: galois_action on cusps has a bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-20 05:29:16

Assignee: craigcitro

Ticket  #5822 implemented the action of Galois on cusps.  I think the algorithm was only designed to work for Gamma_0(N).  However, the code runs for other groups, and doesn't raise an error.  Unfortunately, it gives completely wrong results in some cases, e.g., 

```
sage: G = Gamma1(19)
sage: rational_cusps = [c for c in G.cusps() if c.galois_action(2,19).is_gamma1_equiv(c,19)]
sage: rational_cusps
[0, 2/19, 1/9, 1/8, 1/7, 3/19, 1/6, 1/5, 4/19, 1/4, 5/19, 6/19, 1/3,
7/19, 8/19, 9/19, 1/2, Infinity]
```


However, exactly half the cusps are rational (see, e.g., my paper http://wstein.org/papers/j1p/ or the work of Kubert-Lang).  

This came up in research that Michael Stoll and I were doing, and it was temporarily very confusing. 


---

Attachment

It turns out that cusps (P^1(Q)) don't know their group of course. This function is thus somewhat badly named.  A minimal invasive change without breaking backwards compatibility is to clarify the *documentation* and do nothing else.  I think that is enough to close this ticket, though I may want to make another ticket later to add other actions, etc.   But for now, it is certainly a big improvement to at least fix a major incorrect statement in the documentation!     This patch is pretty safe, since it *only* changes documentation.


---

Comment by was created at 2011-03-22 00:59:48

Changing status from new to needs_review.


---

Comment by cremona created at 2011-03-22 19:21:48

Looks good -- testing now.


---

Comment by cremona created at 2011-03-22 19:50:56

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2011-03-22 19:50:56

Replying to [comment:2 cremona]:
> Looks good -- testing now.

OK, tests passed.


---

Comment by jdemeyer created at 2011-04-13 07:42:34

Resolution: fixed


---

Comment by mderickx created at 2012-07-08 01:19:18

This ticket is a false ticket. I just looked in to the article and the code in the article is really general. The problem is that is_gamma1_equiv does not do what you expect it to!


```
if Cusp(0).is_gamma1_equiv(Cusp(infinity),101):
    print "You would not expect to see something printed"
```

Actually prints the above statement.
The reason for this is that is_gamma1_equiv does not return a bool but a tuple. The first element of this tuple is the bool you were actually looking for.

By the way, I find the claim in this ticket that the code of 5882 only works for Gamma0(N) quite stupid because for Gamma0(n) one might as well implement the following:

```
def galois_action(self,t,N):
    return self
```

Since all cusps on X_0(N).

However there is still a bug in the code because:

```
N=5
G=Gamma1(N)
for i in G.cusps():
    print [j.galois_action(2,N).is_gamma1_equiv(i,N)[0] for j in G.cusps()].count(True)
```

Prints

```
2
1
0
1
```

So the the galois action is not even a permutation!

What would be the right thing to do? Reopen this ticket, open a new one?


---

Comment by cremona created at 2012-07-08 09:40:08

Open a new one, with cross-referencing.


---

Comment by mderickx created at 2012-07-14 05:30:25

Ok, I created #13253 for this. And uploaded the patch I already created. It now needs review.
