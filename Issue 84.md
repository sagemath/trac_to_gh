# Issue 84: E.torsion_subgroup()

Issue created by migration from Trac.

Original creator: burhanud

Original creation time: 2006-09-25 18:52:35

Assignee: dmharvey

E.torsion_subgroup() returns an abstract group. There is no way to get hold of the torsion points (without some hacking).


```
---------- Forwarded message ----------
Date: Mon, 25 Sep 2006 08:00:43 -0400
From: David Harvey <dmharvey`@`math.harvard.edu>
Reply-To: bug reports and users' support questions
    <sage-support`@`lists.sourceforge.net>
To: bug reports and users' support questions
    <sage-support`@`lists.sourceforge.net>
Cc: Iftikhar Burhanuddin <burhanud`@`usc.edu>
Subject: Re: [SAGEsupport] E(Q) torsion


On Sep 25, 2006, at 1:50 AM, Iftikhar Burhanuddin wrote:

> How do I get hold of the actual torsion points?
>
> ===
> sage: E = EllipticCurve([-5699,427500,427500,0,0])
>
> sage: G = E.torsion_subgroup()
>
> sage: G
>  Multiplicative Abelian Group isomorphic to C7
>
> sage: G[1]
>  f

Use the source, Luke!

E.torsion_subgroup??

You'll see the line:

G = self.pari_curve().elltors(flag)

Then later on you see

self.__torsion = sage.groups.all.AbelianGroup(G[1].python())

So pari computes the group, puts it in G (including generators!) and
then SAGE throws away the generators and only stores G[1].

So I guess you want self.pari_curve().elltors(0)[2].

(Actually what you *really* want is to wrap this in a new function in
SAGE so that others don't have this problem again! My recommendation:
add a new cached private attribute __torsion_generators which gets
computed whenever pari.elltors() gets called, and add a new function
E.torsion_subgroup_generators() which returns it. Even better would

be if somehow SAGE's abelian group type knows how to store
information about the "meaning" of its underlying group, but I don't
know anything about SAGE's abelian groups.

In other words, "implement it and send me -- ahem, William -- a patch!")

If this is not your style, file a bug on trac, and assign it to
dmharvey :-)

David
```




---

Comment by was created at 2007-01-07 18:08:20

Changing type from defect to enhancement.


---

Comment by ncalexan created at 2007-02-19 02:04:04

Changing assignee from dmharvey to ncalexan.


---

Comment by ncalexan created at 2007-02-19 02:05:11

Addressed in 2.1.5.

Added class EllipticCurveTorsionSubgroup class which exposes the points as generators.  This is very much a 'first cut', but it's closer to the expected behaviour.  Use E.torsion_subgroup() to access, as usual.


---

Comment by ncalexan created at 2007-02-19 02:05:11

Resolution: fixed
