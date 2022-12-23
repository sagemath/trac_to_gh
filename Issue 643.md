# Issue 643: notebook -- fix space issues with the top bar.

Issue created by migration from https://trac.sagemath.org/ticket/643

Original creator: was

Original creation time: 2007-09-12 18:56:16

Assignee: boothby


```
On 9/12/07, Marshall Hampton <hamptonio@gmail.com> wrote:
>
> I am very happy that the new notebook is more secure, and so I first
> want to thank everyone who worked on it.
>
> There is one thing that bothers me a lot: I treasure my screen real
> estate, and there is a large (about 1") gap between the useful stuff
> in the outer frame (the file menu, use/edit/text/etc) and the frame
> with the cells.  Is there a way to shrink that?
>

Yes, by appropriately rewriting some of the css that defines the page
in sage/notebook/server/css.py.
I wish somebody would do that and send me a patch.

Note that if you just shrink the space on your machine, it will actually
completely cover up all the controls on the top on many other machines.
It's very very system dependent.  Having extra space is the only reasonable
solution until somebody sits down and does this right.
```



---

Comment by was created at 2007-09-12 22:18:06

timothy clemans wrote this example, which seems to be a good idea -- it uses javascript


---

Attachment


---

Attachment


---

Comment by TimothyClemans created at 2007-09-21 04:10:12

Resolution: fixed


---

Comment by TimothyClemans created at 2007-09-21 04:10:45

Resolution changed from fixed to 


---

Comment by TimothyClemans created at 2007-09-21 04:10:45

Changing status from closed to reopened.


---

Comment by was created at 2007-09-21 05:49:21

This doesn't work for me at all.

see attached screenshot in ubuntu 7.04 linux.


---

Comment by was created at 2007-09-21 05:52:31

http://sage.math.washington.edu/tmp/snapshot1.png


---

Attachment

added resize fix


---

Comment by TimothyClemans created at 2007-09-21 15:47:10

Replying to [comment:5 was]:
> http://sage.math.washington.edu/tmp/snapshot1.png

Ok I think I found what happened. I added the div before the last table in the top bar. It is kind of confusing since it is in _html_body instead of html_worksheet_topbar. I'll fix that and upload patch 3.


---

Comment by was created at 2007-09-21 18:56:54

Changing status from reopened to new.


---

Comment by was created at 2007-09-21 18:56:54

Changing assignee from boothby to was.


---

Attachment


---

Comment by mhansen created at 2007-10-03 06:50:07

I made some changes to improve the notebook.  Could people try out my patch and see if it breaks / does anything stupid on other browsers?

It looks like there is a fair amount of cleaning up to do.


---

Attachment


---

Attachment

Accidental upload


---

Attachment


---

Comment by was created at 2007-10-13 06:36:54

Please post one patch bundle, so I know what to actually apply.


---

Comment by was created at 2007-10-13 06:59:39

Resolution: fixed


---

Comment by was created at 2007-10-13 06:59:39

Very nice!
