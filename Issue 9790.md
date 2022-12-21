# Issue 9790: Fix documentation for weave in the "numerical_sage" document

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2010-08-24 01:38:43

Assignee: mvngu


```
import weave
from weave import converters
```


should be


```
from scipy.weave import converters
```


See http://ask.sagemath.org/question/56/error-while-trying-to-import-weave#comment-213


---

Comment by maldun created at 2011-01-25 15:27:48

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-01-25 17:04:29

Standard indentation in Sage is 4 spaces, so I think there is no reason to change that.


---

Comment by jdemeyer created at 2011-01-25 17:09:32

I have a new patch, keeping indentation and adding a `sage:` prompt so at least the `import` statements are tested.


---

Comment by aapitzsch created at 2011-01-25 17:11:13

Could you also correct

```
	"""

       code="""
```

It should probably be something like

```
       code=""" """
```


The link to the weave tutorial (at the end) doesn't work. Maybe you can fix this, too.


---

Comment by jdemeyer created at 2011-01-25 17:17:05

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-01-25 17:17:05

Apologies, there is an indentation problem, it's just that you fixed it the wrong way.


---

Comment by jdemeyer created at 2011-01-25 17:49:26

This file is a mess, there is more clean-up to do.


---

Attachment

Replaces previous patch


---

Comment by jdemeyer created at 2011-01-25 17:52:44

I can't find an updated weave tutorial, so I just removed the link for now.


---

Comment by maldun created at 2011-01-25 17:54:37

Changing status from needs_work to needs_info.


---

Comment by maldun created at 2011-01-25 17:54:37

Replying to [comment:6 jdemeyer]:
> This file is a mess, there is more clean-up to do.

Replying to [comment:5 jdemeyer]:
> Apologies, there is an indentation problem, it's just that you fixed it the wrong way. 

I wanted just to post that ^^

The thing with the 



```
"""

code="""
```


is correct since it belongs to the support_code

I add a new patch with that thing corrected + a new updated link.
I added some blank lines into the 3rd code snippet for a little optical clan up.


At least all examples should work now.


---

Comment by maldun created at 2011-01-25 17:55:01

Corrected version


---

Attachment

Corrected a small error

So I think we need review again ^^


---

Comment by maldun created at 2011-01-25 18:13:05

Changing status from needs_info to needs_review.


---

Comment by aapitzsch created at 2011-01-26 09:10:22

Changing status from needs_review to positive_review.


---

Comment by aapitzsch created at 2011-01-26 09:10:22

Sorry, I hadn't seen `"""` after `support_code`.

Thanks, everything looks good now.


---

Comment by jdemeyer created at 2011-01-26 22:33:50

Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?


---

Comment by jdemeyer created at 2011-01-26 22:33:50

Changing status from positive_review to needs_work.


---

Comment by maldun created at 2011-01-27 00:36:30

Replying to [comment:11 jdemeyer]:
> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?

Ok I double checked, and have to admit that I oversaw the optical clean up you did. I think a merge will be the best then =)


---

Comment by maldun created at 2011-01-27 11:45:47

Changing status from needs_work to needs_review.


---

Comment by maldun created at 2011-01-27 11:45:47

Replying to [comment:11 jdemeyer]:
> Stefan, I think I have made some useful changes which are not in your patch.  Is there a specific reason for that, or should I try to "combine" both our patches?

Ok found some time to do the merge myself. I simply applied your patch and added my changes + a small change =)


---

Attachment

Latest version that merges all changes together


---

Comment by aapitzsch created at 2011-01-27 12:03:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-28 09:34:08

Fixed commit message, apply only this


---

Attachment


---

Comment by jdemeyer created at 2011-01-28 13:47:51

Resolution: fixed
