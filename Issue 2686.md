# Issue 2686: graph generators - new additions

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-03-27 20:53:32

Assignee: rlm

Hoffman-Singleton, Paley graphs, Higman Sims, Johnson, Kneser, etc.


---

Comment by rlm created at 2008-03-28 00:29:17

Some constructions of Chris Godsil, to be transplanted.


---

Attachment

Note - Hoffman-Singleton is included in #2765


---

Comment by chapoton created at 2014-01-09 19:42:42

Is there still something useful here ?


---

Comment by chapoton created at 2014-01-09 19:42:42

Changing keywords from "" to "graphs".


---

Comment by chapoton created at 2014-01-09 19:42:42

Changing status from new to needs_info.


---

Comment by ncohen created at 2014-01-18 16:44:34

Well, I don't even know what the 600-cell is `:-D`

Nathann


---

Comment by ncohen created at 2014-01-18 16:46:11

This being said the code seems to be attached... Looks easy to transform into a real patch. I'll do that right now.

Nathann


---

Comment by ncohen created at 2014-01-18 17:05:32

Well, I just used the code above to build a 600 cell and the construction seems wrong for the number of edges should be 720 according to Wikipedia and is 3168 in Sage.

Sooooooo well, if somebody knows what is wrong ... (given that I don't get a line of what the code does `:-P`)

Nathann


---

Comment by git created at 2014-01-18 17:05:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-01-19 11:19:11

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-01-19 11:20:18

Here is a working version, using exactly the description of vertices given by wikipedia.


---

Comment by ncohen created at 2014-01-19 13:23:04

Wow cool ! Thanks ! I will compute a nice embedding and finish the patch `;-)`

Nathann


---

Comment by ncohen created at 2014-01-19 13:43:22

What do you think ? `;-)`

Nathann


---

Comment by git created at 2014-01-19 13:44:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-01-19 16:45:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-01-19 16:46:47

I have corrected two details. This looks goot to me.

What to do now ? Maybe also use this ticket for the 120-cell graph ?


---

Comment by ncohen created at 2014-01-19 16:48:43

Well,  no problem with that... Do you feel like implementing it ? I will add a nice embedding `:-)`

Nathann


---

Comment by git created at 2014-01-19 17:54:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-01-19 17:55:40

Ok, here is a try. I am not very happy with the efficiency (I had to use Set)

Another question : Cell600 and Cell120 do not sound very good, find better names ?


---

Comment by git created at 2014-01-19 18:34:18

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by ncohen created at 2014-01-19 18:35:34

Hmmmmmm... Well, I removed set and used frozenset instead but it does not change much. And I don't know what to do with the names either : it just can't begin with a number because of Python, so it looks like it is the best we can do `:-/`

Nathann


---

Comment by chapoton created at 2014-01-19 21:15:49

* with some more work, one can maybe avoid creating duplicate vertices. I will not have time to do that soon.

* for the name, one could maybe use SixHundredCell and OneHundredTwentyCell (like they do in some other very expensive stuff named `M*********a`)

* I have never heard of the 200-cell before. One should look for references.

* One still has to make sure that nothing else useful is still hidden there


---

Comment by ncohen created at 2014-01-20 09:59:07

Hellooooooo !

> * with some more work, one can maybe avoid creating duplicate vertices. I will not have time to do that soon.

Well.. It's a bit slow but it isn't really the kind of function that is called very often in a code `:-P`

> * for the name, one could maybe use SixHundredCell and OneHundredTwentyCell (like they do in some other very expensive stuff named `M*********a`)

Tastes... Honestly I think that `Cell<n>` is still easier to find. Plus you cannot build `Cell600` without learning that `Cell120` is implemented too.

> * I have never heard of the 200-cell before. One should look for references.

Well even the 600 was news to me `:-P`

> * One still has to make sure that nothing else useful is still hidden there

In the code ? I just looked at the functions and it looks like we already have all that is contained there.

Nathann


---

Comment by chapoton created at 2014-04-16 19:48:40

Hello,

I have replaced public/2686 by my branch because git was complaining (non-fast-forward updates were rejected)

I have made a more complicated algo for the 120-cell which is a bit less slow, but still rather slow.. I am not sure that was worth the time spent.
----
New commits:


---

Comment by chapoton created at 2014-04-16 19:48:40

Changing status from needs_info to needs_review.


---

Comment by git created at 2014-04-17 19:05:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-17 19:40:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by ncohen created at 2014-04-22 08:10:35

Yooooooooo !!

Well, I do not mind much for as long as the graph can be built, this is very unlikely to become the critical operation of any code in the future `:-D`

If you have problems when pushing a branch, use `git push -f`. This will force the push operation, erasing what was on the othe side if necessary. Weird that you needed it here, though.

Oh. I see. You rebase the whole branch. You should not do that `:-/`

It is much cleaner to "merge" the latest develop release into the branch. This way you just add another commit in the branch which merges it with the latest release, and there is no rebasing going on, while you "copied" all commits on top of the latest release. 

It's not a problem if you rewrote history here, however, as nobody based a branch on our earlier commits.

I just applied your branch, and I have to recompile Sage as a result as I was working on an earlier beta. Will check that tests pass, and then give this ticket a positive review.

Nathann


---

Comment by ncohen created at 2014-04-22 09:02:22

Argggggggg... Okay I had not looked closely at the code, but really it is more complicated... You added a lot of code ! `:-/`

Would you mind including the former version instead ? The speed really isn't a problem here `:-/` 

Nathann


---

Comment by chapoton created at 2014-04-22 09:58:45

Oh, well, no problem, one can keep the long one. But it needs to be tagged with `# long time`


---

Comment by ncohen created at 2014-04-22 09:59:57

Okay, thanks ! Do you feel like playing with git a bit, creating new branches and moving your `# long time` commit a bit lower in the history ? Or do I do that, and you will review it ? `;-)`

Nathann


---

Comment by ncohen created at 2014-04-22 11:33:51

Just did it.

Nathann
----
New commits:


---

Comment by chapoton created at 2014-04-22 19:12:34

Hello,

it seems that you added `long time` on the quickest one only (600 cell). The really bad guy is the 120-cell, which takes almost 10s on my computer (and 6s with my enhanced but abandoned code)


---

Comment by git created at 2014-04-22 21:31:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by ncohen created at 2014-04-22 21:32:12

Dead right ! It is now fixed.

Nathann


---

Comment by chapoton created at 2014-04-24 15:42:27

ok, good enough for me.


---

Comment by chapoton created at 2014-04-24 15:42:27

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2014-04-24 15:44:12

Thaaaaaaaaaanks !

Nathann


---

Comment by vbraun created at 2014-05-06 22:02:53

Resolution: fixed
