# Issue 6939: [with patch, needs review] Make scrollbars appear on cell output when the output is too wide

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-09-15 22:08:01

Assignee: boothby

CC:  mpatel kcrisman boothby

Currently, a scrollbar appears down at the bottom of the entire worksheet, which is only minimally helpful, since you then need to go to the bottom and scroll everything over.

This patch makes scrollbars appear on output that is too wide, but just on that output.

To test, do something like:


```
f=cos(x)-x
show(f.taylor(x,0,50))
```


in the notebook


---

Attachment


---

Comment by kcrisman created at 2009-09-16 13:56:14

Sweet.  I love CSS.  Tested successfully on Safari 4 and Firefox 3.5.  Wish I had access to IE or Linux versions, but this should be okay.

Check out also:

```
show(plot(sin(x),-10,10),figsize=[20,20])
```

So you can now generate big pictures in the notebook if you have a reason to do so.  

But question: why not just overflow, not overflow-x, or also overflow-y?  Those eternally long outputs can be a real pain at times.  Try factorial(10000). Also, how many browsers support CSS3 and not just CSS2?  I can imagine a lot of people on XP having problems with some old version of IE.


---

Comment by jason created at 2009-09-17 07:56:46

Not overflow-y because Sage already handles long vertical outputs by shunting to a file and suppressing text, and besides, who's to say how tall is too tall?  Vertically, we just go by the browser width.  It's a lot harder to guess the magical height that is just right.

If you think this is good, then you can put a positive review and we can discuss the overflow-y and see if it is needed.


---

Comment by kcrisman created at 2009-09-17 13:58:54

No problem with the vertical, though personally I would prefer a little shorter output, as the screen sometimes jumps rather dramatically and it's hard to scroll back and forth...

What about the CSS3 versus CSS2 issue?  On the one hand, I found a quote on css3.info that "Support for these properties is strong as they were first defined by IE6." but on the other hand wikipedia implies that support for this first came in Trident engine 7, which may or may not correspond to IE7...  Maybe the best solution is this one: "Try specifying the CSS2 overflow property first ... then specify the CSS3 overflow-x/y properties to override it on browsers that can."  Of course, that comment was from 2007.

Anyway, as long as it doesn't cause the page to not render at all, I guess this is okay.  If you have time to put in an overflow check first, that would be great.


---

Comment by jason created at 2009-09-17 16:49:30

Good point about CSS3 vs. CSS2.  According to http://msdn.microsoft.com/en-us/library/bb250395%28VS.85%29.aspx, IE6 supports overflow-x (search for "overflow-x") when in standards-compliant mode.


---

Comment by jason created at 2009-09-17 19:22:21

Maybe #6835 should get reviewed and then this should be rebased on that?  #6835 is definitely the larger patch.


---

Comment by jason created at 2009-09-17 19:23:39

I meant #6865 in the above comment.


---

Comment by mvngu created at 2009-09-18 00:01:57

I got the following doctest failure:

```
sage -t -long devel/sage/sage/server/notebook/cell.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/server/notebook/cell.py", line 2293:
    sage: C.html_out()
Expected:
    '\n...<table class="cell_output_box">...</table>'
Got:
    '\n               <div class="cell_output_div">\n               <table class="cell_output_box"><tr>\n               <td class="cell_number" id="cell_number_0" onClick="cycle_cell_output_type(0);">\n                 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n               </td>\n               <td class="output_cell"><div class="cell_div_output_wrap" id="cell_div_output_0"><div class="cell_output_wrap" id="cell_output_0"><pre class="shrunk">5</pre></div><div class="cell_output_nowrap_wrap" id="cell_output_nowrap_0"><pre class="shrunk">5</pre></div><div class="cell_output_html_wrap" id="cell_output_html_0"> </div></div></td></tr></table></div>'
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_94
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_cell.py
	 [28.1 s]
```



---

Comment by jason created at 2009-09-19 02:50:39

It looks like #6865 is getting reviewed pretty quickly, so I'll fix the above doctest when I rebase this patch on top of that one.  If this doesn't happen before next Tuesday, I'll just fix the above doctest anyway, since I'd really like to get this into the next version of Sage.


---

Comment by jason created at 2009-09-19 02:50:46

Changing assignee from boothby to jason.


---

Comment by jason created at 2009-09-19 02:50:46

Changing status from new to assigned.


---

Attachment

Rebased against #6865.  Apply only this patch.


---

Comment by mpatel created at 2009-09-21 01:05:16

[attachment:trac-6939-notebook-css-overflow.2.patch Patch v2] is rebased against #6865's [attachment:ticket:6865:trac_6865-templates-css.3.patch patch v3].

I also prepended `#6939` to the commit string.


---

Comment by mpatel created at 2009-09-21 01:07:36

I should add that I fixed the doctest failure in `cell.py`.  I've set this ticket to WPNR.


---

Comment by jason created at 2009-09-22 17:14:17

mvngu: can you apply the patch now and see if the doctest passes?  If so, then should the positive review above become active again?


---

Comment by jason created at 2009-09-22 17:40:18

positive review on mpatel's rebasing and fixing the doctest (it now works), so I'm putting it back to positive review.

Minh--if there's something wrong with me positive reviewing mpatel's changes, please let me know.


---

Comment by mvngu created at 2009-09-22 18:08:03

Resolution: fixed


---

Comment by mvngu created at 2009-09-22 18:08:03

Replying to [comment:15 jason]:
> Minh--if there's something wrong with me positive reviewing mpatel's changes, please let me know.
I don't see anything wrong, as long as you don't review your own changes and make it positive review. In this case, I see that you reviewed someone else's (mpatel) changes which in this case is a rebase. You never know; rebasing a patch can actually cause unexpected problems. Thank you for your work!




Merged patches in this order:

 1. `#6865`
 1. `trac-6939-notebook-css-overflow.2.patch`


---

Comment by mvngu created at 2009-09-27 09:28:19

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
