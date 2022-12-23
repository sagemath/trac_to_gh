# Issue 7346: notebook -- needless vertical scroll bars on output

Issue created by migration from https://trac.sagemath.org/ticket/7346

Original creator: was

Original creation time: 2009-10-29 07:04:01

Assignee: boothby


```
I mentioned this on IRC, but just to make sure it doesn't fall through the cracks:

When the jsmath fonts are installed, the following input gives an output that the browser thinks is slightly bigger than the output div area.
var('x_1')

print jsmath(sqrt(x_1/x))


Since the output div has a (calculated) style of overflow-y: auto, a scrollbar appears on the right of the output div.  However, everything is visible without scrolling, and scrolling down just scrolls the answer out of view.

I think the best thing we can do in this case is make overflow-y: hidden for output divs, or some other value so that scroll bars do not appear.  In other words, in the CSS file:

div.cell_output_div {
overflow-x:auto;
overflow-y:hidden;
}


Thanks,
```



---

Attachment


---

Comment by was created at 2009-10-29 07:05:00

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-11-06 05:59:28

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-09 17:18:48

Resolution: fixed
