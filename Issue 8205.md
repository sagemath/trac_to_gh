# Issue 8205: sagenb -- the url for published worksheets that's displayed right after publishing is still wrong

Issue created by migration from https://trac.sagemath.org/ticket/8205

Original creator: was

Original creation time: 2010-02-07 05:19:27

Assignee: was

CC:  acleone timdumol

I upgraded sagenb.org to sagenb-0.7.4, and excitedly hoped that when I click publish to publish a worksheet it would give me the correct URL.    Now it says:

"Worksheet is publicly viewable at http://localhost:8888/home/pub/1153"

This is wrong.  This might even be considered worse than before, since before it did "... http://:8888/home/pub/1153" which was obviously wrong.  The above looks less obviously wrong. 


---

Comment by was created at 2010-02-07 05:21:21

I think the most robust fix may be to just add another option to the notebook command that specifies the correct URL base instead of trying to cleverly figure it out.


---

Comment by mpatel created at 2010-02-07 16:49:09

Adding [ProxyPreserveHost On](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#proxypreservehost) to the notebook server `VirtualHost`s in `/etc/apache2/httpd.conf` on `boxen` seems to work.  If it works well, we should mention it in the `notebook?` docstring.


---

Comment by kcrisman created at 2014-12-10 21:49:42

This now works properly on sagenb.org, anyway
> Worksheet is publicly viewable at http://sagenb.org/home/pub/5051

I tested it on another server as well, not sure where this was fixed.


---

Comment by kcrisman created at 2014-12-10 21:49:42

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-12-10 21:49:48

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-11 18:35:23

Resolution: fixed
