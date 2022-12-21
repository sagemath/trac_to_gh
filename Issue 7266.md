# Issue 7266: implement computation of Silverman height bounds

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-23 03:16:15

Assignee: was

CC:  robertwb cremona

The Silverman height bound isn't necessarily as tight at the CPS bound, but it works uniformly over all field extensions, which makes it very useful for some applications, e.g., computing mordell-weil groups over number fields.   So let's add it to Sage!


---

Attachment


---

Comment by was created at 2009-10-23 06:38:55

Changing status from new to needs_review.


---

Comment by cremona created at 2009-10-23 20:08:39

Is there any particular reason for using a native Sage implementation instead of using mwrank/eclib?

I know that #360 has still not been done, but I can't quite see the  point of this patch for curves over Q.


---

Comment by robertwb created at 2009-10-25 06:06:56

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-10-25 06:06:56

Looks good to me. It's a simple enough formula that I'd say the redundant implementation is worth it if just for the ease of introspection. 

We're looking at using this for provable computations of Heegner points, where the field of definition is not a priori known.


---

Comment by cremona created at 2009-10-25 14:32:38

Replying to [comment:3 robertwb]:
> Looks good to me. It's a simple enough formula that I'd say the redundant implementation is worth it if just for the ease of introspection. 
> 
> We're looking at using this for provable computations of Heegner points, where the field of definition is not a priori known. 

Fair point(s).  One reason for getting better (usually) bounds for *rational* points via the CPS method is precisely due to this restriction.  I have no objection!


---

Comment by mhansen created at 2009-10-31 15:48:36

Resolution: fixed


---

Comment by was created at 2009-10-31 21:00:09

But I read here that the Sage project "religiously avoiding redundant code.": http://www.metafilter.com/86262/unbump
