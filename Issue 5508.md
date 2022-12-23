# Issue 5508: [with patch, needs review] Improvements for relative number fields

Issue created by migration from https://trac.sagemath.org/ticket/5508

Original creator: fwclarke

Original creation time: 2009-03-13 11:55:25

Assignee: was

The attached patch implements many improvements for relative number fields.  
In particular a whole load of previously unimplemented functions for ideals in a relative number field now work, and others work better.

Following discussion at
[sage-nt thread](http://groups.google.co.uk/group/sage-nt/browse_thread/thread/16106258cd436515?hl=en-GB),
for several functions the distinction between the relative and absolute 
version has been made explicit, in order to  avoid ambiguity.  
Thus, for example, for a relative number 
field both relative_degree and absolute_degree are defined but degree is 
unimplemented, while for an absolute number field relative_degree, 
absolute_degree and degree are _all_ defined (with the same meaning).  
This has entailed a few minor changes to enable 
functions to work with either absolute or relative number fields.

It has been suggested that `NumberField` should only be allowed to generate 
an absolute number field.  I have not implemented this, but I have made `NumberFieldTower` publicly available and used it in several 
doctests.  If a change was made to `NumberField`, `NumberFieldTower` could 
retain the old functionality of `NumberField`.

A number of other minor changes have been made, and these seem to fix
#5276, #5214 and #2551




---

Attachment

Review:  I read through the patch and was impressed by the thoroughness and attention to detail!  I don't know all the formulas for relative different (etc) off the top of my head, but what is tere looks reasonable.

The patch applies cleanly to 3.4.

Doctesting sage/rings/number_field, the only problem was this:

```
sage -t  "local/sage-3.4/devel/sage-5508/sage/rings/number_field//order.py"
**********************************************************************
File "/home/masgaj/local/sage-3.4/devel/sage-5508/sage/rings/number_field/order.py", line 1196:
    sage: OK(a)
Expected nothing
Got:
    a
**********************************************************************
File "/home/masgaj/local/sage-3.4/devel/sage-5508/sage/rings/number_field/order.py", line 1197:
    sage: a
Expected nothing
Got:
    a
```

which is just a matter of deleting a rogue "sage: " prompt in front of one line of output.

Fix that and this will ready to go.  (I hope it merges ok with my units code at #5513!)


---

Comment by davidloeffler created at 2009-03-17 10:07:48

This also seems to fix #4193.


---

Attachment

replaces previous


---

Comment by cremona created at 2009-03-17 10:35:36

I can confirm that #4193, #5276, #5214 and #2551 can all be closed as fixed once this one is merged.

I have attached a patch whic his identical to the original except that it ocrrects one typo which means that all doctests in sage/rings/number_fields  pass, and hence this one gets a (very!) positive review.


---

Comment by fwclarke created at 2009-03-18 20:56:26

The patch doesn't actually merge well with the #5513 patches.  Moreover, after some intensive testing, I have found a whole lot more minor changes needed to give relative number fields most of the functionality of their absolute versions.  So my intention is to incorporate these a new patch which will merge ok.


---

Comment by davidloeffler created at 2009-03-19 08:36:35

Hmmm -- would you mind leaving this one as it is, since it's already been given a positive review, and making a new ticket for the follow-up patch, which can then be reviewed separately? I spent the best part of a day's work rebasing my patch at #5159 so it would apply happily on top of sage-5508.2.patch! 

(One wouldn't normally try and make improvements to a journal paper after it's been accepted for publication; one writes follow-up papers.)


---

Comment by fwclarke created at 2009-03-19 09:09:14

Yes, fine, let's leave it as it is.  I'll do the new changes separately, but not for a few days.


---

Comment by mabshoff created at 2009-03-23 20:06:20

Does this patch depend on any other patch set? I am seeing the following doctest failure:

```
sage-3.4.1.alpha0$ ./sage -t -long devel/sage/sage/rings/number_field/number_field_ideal_rel.py
sage -t -long "devel/sage/sage/rings/number_field/number_field_ideal_rel.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/number_field/number_field_ideal_rel.py", line 598:
    sage: z = I.element_1_mod(J); z
Expected:
    -21/2*b*a - 21/2
Got:
    -8*b*a + 24
```


Cheers,

Michael


---

Comment by fwclarke created at 2009-03-23 22:48:58

When I built it on top of 3.4 I got `-21/2*b*a - 21/2`, so I think something else must be the cause.  Of course `-8*b*a + 24` is also an acceptable answer.


---

Comment by mabshoff created at 2009-03-24 22:58:44

Replying to [comment:9 fwclarke]:
> When I built it on top of 3.4 I got `-21/2*b*a - 21/2`, so I think something else must be the cause.  Of course `-8*b*a + 24` is also an acceptable answer.

Ok. Can you change the doctest since some other patches depend on this patch?

Cheers,

Michael


---

Comment by fwclarke created at 2009-03-25 08:40:55

Replying to [comment:10 mabshoff]:

> Ok. Can you change the doctest since some other patches depend on this patch?

The new `sage-5508.3.patch` has the revised doctest, but is otherwise the same as `sage-5508.2.patch`

Hope this solves the problem.

Francis


---

Attachment

Replaces previous


---

Comment by mabshoff created at 2009-03-25 08:42:47

Ok, back to positive review then :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 08:52:56

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 08:52:56

Merged sage-5508.3.patch  in Sage 3.4.1.alpha0.

Cheers,

Michael
