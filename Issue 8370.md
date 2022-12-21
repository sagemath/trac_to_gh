# Issue 8370: Add tour_functions to the French tutorial (cf. #5463)

Issue created by migration from Trac.

Original creator: mmezzarobba

Original creation time: 2010-02-25 23:00:17

Assignee: mmezzarobba

CC:  abmasse

tour_functions.rst (added by #5463) is missing from the French translation of the tutorial


---

Comment by mmezzarobba created at 2010-02-27 09:20:38

Changing status from new to needs_review.


---

Attachment


---

Comment by abmasse created at 2010-03-06 09:50:03

Hello, Marc !

This is a good idea. If I'm alright, this patch is adding a missing section to the French tutorial that is mainly a translation of the same section (already present) in English ?

I'll start looking at your patch today.


---

Comment by abmasse created at 2010-03-06 10:08:55

A very stupid question : how can I generate the French documentation ? I'll try to find out, but if you read this message before I find out, don't hesitate to enlighten me !

Thank you.


---

Comment by abmasse created at 2010-03-06 10:13:20

Never mind, I just found out.


```
sage -docbuild fr/tutorial html
```



---

Comment by abmasse created at 2010-03-06 12:18:46

Minor rephrasing and doc syntax fixes -- apply on top of the other patch


---

Attachment

Hello again Marc !
I reviewed your patch. Everything is ok, I made a few changes which are not errors, but mainly suggestions, so if you don't agree with any of it, feel very free to remove them or tell me to remove them. To summarize, I did the following modifications.

1. Since the tabbing is four spaces for Python code in general (not mandatory, but encouraged), I reformatted your examples so that they all start at distance four from the beginning of the lines.

2. For the sage blocks illustrating your examples, you always put `::` alone on a line, while you could put it at the end of the preceding text explaining the example. The effect is that the sentence ends with `:` and the block example follows. This is not a mistake, but this is what I've seen in other patches.

3. I did some rephrasing. These are only suggestions, if you don't agree with all or some of it, let me know.

4. You forgot to put the word "plot" between backticks in one place. I corrected that.

That's pretty much it. As soon as you confirm my changes, I'll be ready to set this ticket to positive review.


---

Comment by mmezzarobba created at 2010-03-26 21:23:52

Sorry for the delay.

Replying to [comment:2 abmasse]:
> This is a good idea. If I'm alright, this patch is adding a missing section to the French tutorial that is mainly a translation of the same section (already present) in English ?

Indeed.

Replying to [comment:5 abmasse]:
> I reviewed your patch. Everything is ok, I made a few changes which are not errors, but mainly suggestions, so if you don't agree with any of it, feel very free to remove them or tell me to remove them. To summarize, I did the following modifications.
> 
> 1. Since the tabbing is four spaces for Python code in general (not mandatory, but encouraged), I reformatted your examples so that they all start at distance four from the beginning of the lines.

Here I just stuck to the style of the English version.  But you are right that (most?) other sections of the original tutorial use four spaces.

> 2. For the sage blocks illustrating your examples, you always put `::` alone on a line, while you could put it at the end of the preceding text explaining the example. The effect is that the sentence ends with `:` and the block example follows. This is not a mistake, but this is what I've seen in other patches.

Same here, except that the format with `::` on its own line seems to be used consistently in the tutorial (in both languages).  I don't think it's a big deal anyway.

However, in some cases, you put a space between the `::` and the preceding word, so that there is no colon (and no period either) in the output.  Was that deliberate?  

> 3. I did some rephrasing. These are only suggestions, if you don't agree with all or some of it, let me know.
> 
> 4. You forgot to put the word "plot" between backticks in one place. I corrected that.

Seems fine to me. Btw, I also checked that the our patches apply correctly on top of 4.3.4 + patches from #8242.


---

Comment by ncohen created at 2010-04-04 15:42:44

Hello !!! This new patch is a concatenation of the two previous given, plus two unimportant fixes for a broken doctest :-)

Do you agree to set it to positive review ? It applied fine, it is indeed french and everything is nicely formatted !!

Nathann


---

Attachment

Hello, Marc and Nathann ! Sorry for the delay...

Nathann, I can't see what changes you made with the merged patch. Could you please add a patch that contains only your changes and that applies on top of the two patches Marc and I have attached so far ? This way, it'll be easier to review.

Thank you !


---

Comment by ncohen created at 2010-04-08 11:16:17

Here it is ! :-)

Nathann


---

Attachment

Hello, everyone !

I'm very sorry for the delay... I just moved back to Montreal and haven't had much time lately to work on Sage patches. I looked once again at the three patches, applied them, checked the documentation generated by Sage and run `sage -t` on the `tour_functions.rst` file. Everything looked fine and all tests passed. Therefore, I give this patch a positive review.

For the release manager, please apply the patches in the following order


```
trac_8370_tour_functions_french.patch
trac_8370_review-abm.patch
trac_8370_fixes.patch
```


and disregard `trac_8370_merged+doctest_fixes.patch`.

Thank you for your patience!


---

Comment by abmasse created at 2010-04-15 20:39:32

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-04-15 20:46:59

Excellent ! I'll be in Montreal in the early days of may, btw ;-)

Nathann


---

Comment by abmasse created at 2010-04-15 21:06:35

Nice! See you then!

By the way, I forgot to mention that I tested the three patches on sage-4.3.5.


---

Comment by was created at 2010-04-29 05:36:02

Resolution: fixed
