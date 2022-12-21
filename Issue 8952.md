# Issue 8952: Odd Girth

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-05-12 00:24:22

Assignee: jason, ncohen, rlm

CC:  rbeezer

Add a function to compute odd girth, and modify Graph.is_perfect accordingly

Nathann


---

Comment by ncohen created at 2010-06-06 11:01:07

Changing status from new to needs_work.


---

Comment by kini created at 2012-09-25 18:08:05

What needs work here exactly? There's no patch on this ticket.


---

Comment by ncohen created at 2012-09-25 18:10:14

Well, nothing actually. I used to use the Trac server as my todo-list, a loooong time ago, so you will find many such tickets in this section `^^;`

I am (desperately) looking for a flat in Paris right now, but I should stop sinking and start swimming in a couple of weeks. 

I hope that all is well on you side !! `:-)`

Nathann


---

Comment by kini created at 2012-09-25 18:28:28

Haha, OK :) I found this ticket because someone asked about it on IRC and wants to work on it. Good luck with your flat!


---

Attachment

Patch performing the ticket request


---

Comment by azi created at 2012-09-25 22:21:21

Changing status from needs_work to needs_review.


---

Comment by azi created at 2012-09-25 22:21:21

Hello!

Attached is the patch that should perform the required task. odd_girth() computes the odd girth of a graph using a property of the characteristic polynomial of the adjacency matrix. Its (theoretic) computational complexity is optimal.


---

Comment by rbeezer created at 2012-09-26 02:51:40

Azi,

I took a quick look and it looks promising, especially since characteristic polynomials are quite fast in Sage.  I can look closer when I have a bit more time.

For now, documentation needs some work.  For example:


```
Any complete graph on more than 2 vertices contains a triangle and has thus odd girth 3 

	            G = graphs.CompleteGraph(10) 
	            sage: G.odd_girth() 
	            3
```


needs a double colon after the lead-in sentence (all 3 of your verbatim blocks need this).  And your line creating the complete graph needs a `sage:` preceding it.

Current documentation style needs "INPUT" and "OUTPUT" blocks - look around for examples.  They will be pretty simple in this case.

You can catch some of these yourself:


```
sage -b
sage -docbuild reference html
```


will rebuild the documentation and you can view the html file for mess-ups with the doc string.

And


```
sage -t <source file>
```


will find broken tests.

Rob


---

Comment by rbeezer created at 2012-09-26 02:55:48

Changing status from needs_review to needs_work.


---

Comment by azi created at 2012-09-26 16:38:33

Second patch implementing the requested comments


---

Attachment

I have added a patch (hopefully valid) with the commends you requested. There is still one missing warning in building the documentation (Literal block expected; none found." is likely an indentiation problem and/or a problem with a double-colon) which I was not able to spot.


---

Comment by azi created at 2012-09-26 16:41:40

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2012-09-26 17:20:50

Dear Azi,

Your "literal block expected" error is caused by a double-colon after "EXAMPLES".  It should be a single, just to be typeset as-is.  A double-colon says verbatim (literal) stuff comes next.

The patch looks severely messed-up to me.  ;-(  I am not all sure how you got it to that state, but I think I can fix it.  Are you using clones or Mercurial queues?  Queues are much easier to deal with, and easier for iterative changes like this.

Don't try to fix the double-colon until I fix the patch (maybe later today).

Rob


---

Comment by azi created at 2012-09-26 17:45:39

The patch was produced using the following guide http://www.sagemath.org/doc/developer/walk_through.html#creating-a-change


---

Comment by rbeezer created at 2012-09-26 19:15:59

Replying to [comment:11 azi]:
> The patch was produced using the following guide http://www.sagemath.org/doc/developer/walk_through.html#creating-a-change

Well, I sort of hope not, since I wrote that guide.  ;-)  It looks like something wasn't done quite right.

Guide discusses two approaches:  clones and queues.  I cannot even begin to help if I don't know which approach you are taking.  Let me know.

Rob


---

Comment by rbeezer created at 2012-09-30 19:15:33

"consolidated" patch has previous work in one (proper) patch - still has azi's name on it, too.

See new "Apply" section in ticket description.

Azi -

1.  Start with a clean Sage installation (even if it means installing from source).
2.  Install a system version of Mercurial, or replace "hg" commands with "sage -hg"
3.  hg import <URL-to-consolidated-patch> (get URL from tiny download icon, not web-view of patch)
4.  hg qpush  (to apply patch)
5.  Rebuild sage, edit source, make changes, etc, etc.
6.  hg qrefresh -m "<A possible new message for patch summary goes here>"
7.  hg export qtip > <file-name-for-revised-patch>
8.  hg qpop (to move changes out of the way, and get back to original Sage, rebuild, etc)

You can use "hg qnew <private-name-for-patch>" to initiate a new project with no interference from previous one.  You can easily manage several activities with qpop/qpush, and "hg qpush --move" will allow applying patches out of order.  "hg qapplied", "hg qunapplied" are informative.  Hope this is helpful.

Rob


---

Comment by ncohen created at 2012-10-01 13:51:21

(same patch with the max 80 characters per line that Minh taught me to respect in the Graph files, some links between odd_girth and girth, and some modifications in the doc so that Sphinx gets what it should)


---

Comment by ncohen created at 2012-10-01 15:53:35

Ahem...


```
sage: graphs.CycleGraph(5).odd_girth()
+Infinity
```


With this additional patch, the functions looks more similar to what page 45 of "Algebraic Graph Theory" seems to say `:-)`

Nathann


---

Comment by kini created at 2012-10-01 16:31:29

Apply trac_8952_odd_girth_consolidated.patch trac_8952_odd_girth-bugfix.patch


---

Comment by rbeezer created at 2012-10-01 17:15:14

Replying to [comment:16 ncohen]:
> With this additional patch, the functions looks more similar to what page 45 of "Algebraic Graph Theory" seems to say `:-)`

I'd been meaning to suggest stepping by -2, mostly for clarity, and less code.  I hadn't realized there was a problem, though!  Good catch.


---

Comment by ncohen created at 2012-10-02 08:10:22

There is always a problem when a book decides to write `\sum_i c_{n-i} x^i` instead of `\sum_i c_{i} x^i` `:-P`

In the end what do we do with this ticket ? 3 peoples modified the patch already `:-D`

To me it looks good as it is... 

Nathann


---

Comment by ncohen created at 2012-10-02 08:14:09

HMmmmmmmm.... I guess I shouldn't put a 's' at the end of "people". And I guess I should have said "persons" instead, by the way `:-)`

Nathann


---

Comment by ncohen created at 2012-10-02 13:20:31

(just updated the patch so that is_odd_hole_free uses this function too !!!)


---

Attachment

The patch looks good to me. Am I allowed to change the status of the ticket to reflect that?


---

Comment by ncohen created at 2012-10-27 22:16:24

Well I guess you can if you think the patch is ready `:-)`

Nathann


---

Comment by ncohen created at 2012-11-05 15:48:09

Ahem. Does everybody here agree that this patch should be merged ?

Nathann


---

Comment by azi created at 2012-11-05 16:05:01

Looks good to me!


---

Comment by ncohen created at 2012-11-05 16:06:26

Ok, fine then... Could you set it to positive_review ? I'm the last one who added something to the ticket `:-)`

Nathann


---

Comment by ncohen created at 2012-11-17 16:36:42

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2012-11-17 16:36:42

Okayyyyyyyyyyyyyyyyyy.................. `:-P`

Nathann


---

Comment by azi created at 2012-11-17 16:44:26

I am sorry. I completely overlooked the "set it to positive_review" part.


---

Comment by ncohen created at 2012-11-17 16:51:41

No problem. Could you add your name to the list of reviewers/authors ? And if possible to the list in "http://trac.sagemath.org/sage_trac/wiki" too `:-)`

Nathann


---

Comment by azi created at 2012-11-17 18:35:32

OK. I have added myself to the wiki link. But I can't find the list of reviewers/authors. Do you happen to know where do I find that?


---

Comment by ncohen created at 2012-11-17 18:40:27

Ahahaah. It's on this page, on the "Modify Ticket" section. When a ticket is positively reviewed, the list of authors and reviewers has to be filled. I often forget that myself `:-)`

Nathann


---

Comment by azi created at 2012-11-17 18:49:06

Oooh ok! I suppose you will add yourself to the list right?


---

Comment by ncohen created at 2012-11-17 19:03:52

Well, I'm not really an author of this ticket, and Rob did some of it too `:-)`

Nathann


---

Comment by kini created at 2012-11-17 19:08:35

If azi is the only author, then he cannot be a reviewer...


---

Comment by ncohen created at 2012-11-17 19:14:44

AHahah. If that's the law, then...`:-)`

Nathann


---

Attachment


---

Comment by jdemeyer created at 2012-12-16 15:36:02

Rebased to sage-5.5.rc0.


---

Comment by jdemeyer created at 2012-12-18 11:14:28

Resolution: fixed
