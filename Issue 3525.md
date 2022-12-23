# Issue 3525: notebook -- new welcome page

Issue created by migration from https://trac.sagemath.org/ticket/3525

Original creator: TimothyClemans

Original creation time: 2008-06-28 06:40:47

Assignee: was

Take the static page at http://timothyclemans.com/nb_homepage/ and merge it into the Sage Notebook code.


---

Attachment


---

Comment by TimothyClemans created at 2008-06-28 08:07:43

Changing component from number theory to notebook.


---

Comment by TimothyClemans created at 2008-06-28 08:07:43

Changing assignee from was to TimothyClemans.


---

Comment by TimothyClemans created at 2008-06-28 08:07:43

Changing status from new to assigned.


---

Attachment


---

Comment by TimothyClemans created at 2008-06-28 08:16:31

Changing keywords from "" to "editor_wstein".


---

Comment by TimothyClemans created at 2008-06-28 10:34:59

From Harald Schilly:


```
Looks good, yes. Just small remarks what I would change...

1) The border around the sign-in formular is thin. Why not the same as
those two below? I would suggest to make all three borders small...

2) The top header is an image. The serif-italic letters don't look
very well on my screen. (no subpixel hinting compared to directly
rendered italic letters on my lcd) .. I would suggest to not use an
image, just the text string with a fixed font size (16pt?, italic,
serif) and absolute placement.

3) The forgot password page does not exist. I think, it should look
the same, except the login box and the middle content replaced by an
explanation and so on.

4) maybe less screenshots (just a 3x2 matrix) but with larger images?
so that someone could see more!

5) it's not xhtml valid
I strongly suggest to use xhtml transitional, since this is better for
compatibility and browsers like ie6 work better with that. xhtml
strict is just some sort of a more theoretical wish that will never
come true ;)
but anyways, ending a formular input tag with /> is not ok. browsers
don't understand real xml ...

6) maybe more margin-borders on the left and right side of the middle
content, to give everything a bit more "air" so that it looks less
tight...

greetings Harald


On Sat, Jun 28, 2008 at 08:38, William Stein <wstein@gmail.com> wrote:
> What do you think of
>
> http://timothyclemans.com/nb_homepage/
>
> --
> William Stein
> Associate Professor of Mathematics
> University of Washington
> http://wstein.org
>
```



---

Comment by TimothyClemans created at 2008-06-28 10:57:34

used Tidy to deal with point 5 of Harald's criticism


---

Attachment


---

Comment by TimothyClemans created at 2008-06-28 14:04:21

Regarding the negative review could you tell me if you want all of Harald's suggestions implemented? 

1) I can do easily by switching in the css which background is called for a:link and a:hover

2) Maybe do this in another ticket if others also complain

3) A very minimalistic "account recovery" page will be in sage-3.0.4. Anything regarding it should be a different ticket

4) I don't want to change them because A) I like it the way it is B) it would be very time consuming for me

5) Done

6) Sure


---

Comment by was created at 2008-06-28 14:21:28

For a positive review it is enough to do 1, 5, 6.


---

Attachment

margins increased blue line under interactive computer programming changed to reflect new margins

Border for "Sign up" and "Published worksheets" is now 1px.


---

Attachment

forgot to change which images are preloaded (the ones for signup and published worksheets)


---

Comment by TimothyClemans created at 2008-06-28 21:47:18

In extcode-3525_3.patch I see 


```
diff -r 84e3731cc21b -r 40c4b0aa9491 notebook/images/head.gif
Binary file notebook/images/head.gif has changed
```


Is the actual image stored in the patch? If not then how do I put package images for inclusion?


---

Comment by TimothyClemans created at 2008-07-06 02:37:11

extcode_combined.patch is a git style patch that should contained the required images


---

Attachment

The combined extcode patch is mess. Various fixes aren't in the patch ...


---

Comment by jason created at 2010-08-27 15:38:38

What is the status of this patch, Timothy?


---

Comment by jason created at 2010-08-27 15:39:04

Changing keywords from "editor_wstein" to "editor_wstein, stale".


---

Comment by kcrisman created at 2014-09-17 18:52:56

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2014-09-17 18:52:56

This is not a bad idea in general, but at this point the discussion about looks are subsumed into ideas about "newUI" and "themes" upstream.  Any new welcome page discussion should arrive there.  Sadly, wontfix is probably most appropriate for this six-year-old ticket.


---

Comment by vbraun created at 2014-09-18 17:56:59

Resolution: wontfix
