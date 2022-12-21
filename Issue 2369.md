# Issue 2369: clean up the Notebook HTML & CSS

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-03-02 17:16:05

Assignee: TimothyClemans

CC:  was jhpalmieri

This is critical to the success of the up-coming manipulate functionality.


---

Comment by was created at 2008-03-02 17:21:01

> This is critical to the success of the up-coming manipulate functionality.

Thanks for caring about this issue so much.

I don't think fixing this is critical to the success of manipulate.  I do appreciate your concern.  This ticket is pretty vague...


---

Comment by TimothyClemans created at 2008-03-02 17:36:44

I've had a lot of trouble writing HTML in the Notebook because of how the Notebook HTML & CSS are written. Looking at the output of running the HTML of a worksheet through the W3C Validator I noticed font tags are being used. Font tags are extremely bad for use in the Notebook because block level tags such as P, DIV, etc can't go inside them.


---

Comment by mabshoff created at 2008-03-02 18:10:45

Timothy,

as William pointed out the ticket you opened is vague and cannot really be solved. So I changed the summary to something more achievable and from your comment it is what you intend to do. Feel free to correct the "Summary" line.

Cheers,

Michael


---

Comment by drkirkby created at 2009-12-25 17:44:05

This ticket is 22 months old and the notebook has changed in that time, but I think it is well worth fixing the W3C validation errors, for reasons that are not so obvious. 

When I look at the Wolfram Reserach site

http://www.wolfram.com/

and see 259 Errors, 4 warning(s)

http://validator.w3.org/check?uri=http%3A%2F%2Fwww.wolfram.com&charset=%28detect+automatically%29&doctype=Inline&group=0&user-agent=W3C_Validator%2F1.654


it gives me the impression of not taking care of details. Wolfram Reserach could reasonably argue they would rather devote time to improving Mathematica, than fixing the web site. One can see some logic to that. But I personally still see this as not paying attention to detail. 

In contrast, the Sage web 

site has few if any issues with the W3C validator. The home page is faultless in this respect 

http://validator.w3.org/check?uri=http%3A%2F%2Fwww.sagemath.org%2F&charset=%28detect+automatically%29&doctype=Inline&group=0

As such, even if the notebook looks fine, I believe the errors should be removed, to give the impression that attention is paid to detail. 

A google search on 'W3C validator' shows 2,230,000 hits. It is obvious people do use that tool. 

Dave


---

Comment by kcrisman created at 2014-09-17 19:04:25

Changing priority from major to minor.


---

Comment by kcrisman created at 2014-09-17 19:04:25

Upstream at https://github.com/sagemath/sagenb/issues/232.  Certainly this is worth doing, though I would argue much lower priority than some other things.


---

Comment by chapoton created at 2020-03-28 10:03:55

old ticket about deprecated sagenb. Can we close ?


---

Comment by chapoton created at 2020-03-28 10:47:26

Changing status from new to needs_review.


---

Comment by kcrisman created at 2020-03-28 14:32:16

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-03-28 15:22:00

Resolution: invalid


---

Comment by chapoton created at 2020-03-28 15:22:00

thx
