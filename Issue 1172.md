# Issue 1172: change the watkins license in SAGE_ROOT/COPYING

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-14 23:25:20

Assignee: was

Change the watkins license in SAGE_ROOT/COPYING to the following, since Mark Watkins told me to do this.


```
The SYMPOW COPYING file says:


Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
 * Redistribution of source code must retain the above copyright notice,
 this list of conditions and the following disclaimer.
 * Redistribution in binary form must reproduce the above copyright
 notice, this list of conditions and the following disclaimer in the
 documentation and/or other materials provided with the distribution.
 * If redistribution is done as a part of a compilation that has a more
 restrictive license (such as the GPL), then the fact that SYMPOW has
 a less restrictive license must be made clear to the recipient.
 For example, a line like (include bracketed text if SYMPOW is modified):
 "This compilation includes [a modification of] SYMPOW whose [original]
  code has a less-restrictive license than the entire compilation."
 should appear in a suitable place in the COPYING and/or LICENSE file.

[followed by the BSD disclaimer]
```



---

Comment by kini created at 2012-06-25 09:26:08

This was a pretty easy patch to make...


---

Comment by kini created at 2012-06-25 09:26:08

Changing status from new to needs_review.


---

Comment by kini created at 2012-06-25 09:27:02

apply to $SAGE_ROOT


---

Attachment

Looks good to me.


---

Comment by ohanar created at 2012-06-25 22:56:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-26 06:46:48

The last clause sounds awfully much like the BSD advertising clause.  Are we sure this is GPL-compatible?  IANAL, but it's a natural question to ask.


---

Comment by jdemeyer created at 2012-06-28 07:56:35

Resolution: fixed


---

Comment by kini created at 2012-06-28 08:26:47

Jeroen: should this be merged if your question remains unanswered?


---

Comment by jdemeyer created at 2012-06-28 08:30:03

Replying to [comment:5 kini]:
> Jeroen: should this be merged if your question remains unanswered?
I guess so.  This patch doesn't change the license, it changes the documentation of the license.  Whether or not this patch gets merged, my question stands.


---

Comment by kini created at 2012-06-28 08:35:40

Good point.
