# Issue 3155: notebook postdata and behaviour of archive, delete and stop buttons

Issue created by migration from https://trac.sagemath.org/ticket/3155

Original creator: nbruin

Original creation time: 2008-05-11 04:03:00

Assignee: boothby

When I have just logged in to sage, the URL one is connected to is
"https://<sage server>/login" and the relevant page apparently has post-data on it.

If I click one of the "archive", "delete" or "stop" buttons, apparently a reload of the page is triggered. The result is that firefox gives me a warning "The page you are trying to reload contains POSTDATA ...".

If I change the URL to "https://<sage server>" in the same browser I remain authenticated and everything still works. Now the page does not have POSTDATA on it and the reload is not a problem.

Possible fixes:

 - Make sure that the POSTDATA is dumped as quickly as possible, so that reloading does not trigger warnings
 - reprogram the actions of the buttons so that they don't trigger a reload (for instance, force them to do a load of a new page instead)
 - something I cannot think of.


---

Comment by TimothyClemans created at 2008-05-11 13:57:20

Knoboo deals with this problem by redirecting the user to the bookshelf. See http://trac.knoboo.com/browser/trunk/knoboo/knoboo/resources/user.py


```
def render(self, request):
    response = http.RedirectResponse("/bookshelf")
    response.headers.setHeader("set-cookie", [http_headers.Cookie("sid", self.cookie)])
    return response
```



---

Comment by TimothyClemans created at 2008-05-17 15:43:53

Fixed in #3050.


---

Comment by mabshoff created at 2008-05-17 20:30:44

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 20:30:44

Fixed in Sage 3.0.2.alpha1 by merging the patches at #3050.


---

Comment by mabshoff created at 2008-05-18 16:32:35

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-05-18 16:32:35

Since #3050 got reverted I am reopening this ticket, too.


---

Comment by mabshoff created at 2008-05-18 16:32:35

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-05-19 06:08:48

Resolution: fixed


---

Comment by mabshoff created at 2008-05-19 06:08:48

Fixed in Sage 3.0.2.alpha1 by merging the new patches at #3050. ;)
