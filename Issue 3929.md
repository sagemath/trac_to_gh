# Issue 3929: Merge the max-flow min-cut code from Scott Clifford and Jerin Schneider

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-22 18:06:59

Assignee: rlm

See http://wiki.wstein.org/2008/480a/theprojects


---

Comment by jason created at 2008-08-25 19:40:23

See #1317 for this request.  I think implementing this might close #1317


---

Comment by rlm created at 2008-08-25 23:24:12

Jason,

You need to stop polluting trac like this. If there was already a ticket for this, you should have put your comments there. Also, I'd like to point out how annoying it is when someone opens a bunch of wishlist tickets with no intention of supplying any patches.

-- Robert


---

Comment by rlm created at 2008-08-25 23:25:10

Also, based on the presentation I saw from these two people, it is questionable whether we want to find a more standard implementation of this algorithm (as they are a dime a dozen, and maybe not all of them were undergraduate projects...).


---

Comment by jason created at 2008-08-26 14:39:40

Resolution: duplicate


---

Comment by jason created at 2008-08-26 14:39:40

Sorry.  I didn't remember there was already a ticket for this until I was going through tickets the other day; apparently I should have searched more carefully.  The reason I opened a few tickets is because I saw that it looked like there was work that could be included and didn't want to lose the reference (especially for this ticket, which is something that would be nice to have).

However, I think in this case a post to sage-devel asking about the projects from the wiki page would have been better than to create tickets for each one.  Sorry for the annoyance.

Third, I do intend to post patches eventually, if someone else doesn't beat me to it.  As I have time, I go through all the tickets I've entered and work on patches.  The reason to put them up on trac is to make sure that the idea doesn't get lost.  I do agree that I opened up a lot of wishlist tickets (probably too many) when I first started with Sage in my eagerness, but I tried to assign them to the wishlist milestone, which has the purpose: "We have many tickets for enhancements in trac that depend on somebody with time to make them happen. In order not to lose them we collect them under this milestone. If you are interested in working on one of the tickets in this category please let us know or retag that ticket to an appropriate milestone."  (maybe I ought to put more tickets under this wishlist, though...)

Given your comments, I'm going to close this as a duplicate, though, and note the link on #1317.  Thanks.


---

Comment by mvngu created at 2009-05-21 11:23:27

Replying to [comment:3 rlm]:
> Also, based on the presentation I saw from these two people, it is questionable whether we want to find a more standard implementation of this algorithm (as they are a dime a dozen, and maybe not all of them were undergraduate projects...).
From my reading of the [source code](http://wiki.wstein.org/2008/480a/theprojects?action=AttachFile&do=get&target=max_flow_min_cut.py), it looks like the code is using the Ford-Fulkerson algorithm, which is pretty bad for some corner cases. And its complexity is in general not polynomial. Of course, one obvious way to get polynomial complexity is to use the modified algorithm by Edmonds and Karp. Chapter 6 from the following text is very relevant to this ticket.
 * D. Jungnickel. Graphs, Networks and Algorithms. 3rd edition, Springer, 2008.
