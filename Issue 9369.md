# Issue 9369: make verbose command flush its output

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-28 23:43:29

Assignee: jason




---

Attachment


---

Comment by was created at 2010-06-28 23:50:01

Changing status from new to needs_review.


---

Comment by was created at 2010-06-28 23:50:01

The point of this is that if you do


```
sage foo.sage > output.out
tail -f output.out
```


and use verbose(...) in foo.sage, you'll see nothing for a while, which sucks.


---

Comment by rlm created at 2010-06-29 18:28:34

This might or might not be slightly off topic. Without verbose, it doesn't seem to be flushing at all. I tried the following in a file called `test.sage` with `./sage test.sage > ~/foo.txt` and `tail -f ~/foo.txt` only showed the output once I interrupted the loop.


```
for E in cremona_optimal_curves(range(10000)):
    print E.label(), E.sha().an()
```


I remember doing something like this a long time ago and it working. Wassupwiddat?


---

Comment by rlm created at 2010-06-29 18:29:22

Also, if I don't stream the output to a file, it does print in real time. Am I missing a linux-ism here?


---

Comment by jsrn created at 2010-07-30 14:14:27

This sort of behaviour is standard in most programming languages for efficiency: whenever the OS is asked to print to a file (and in some cases, also if it is to a terminal), it collects output until some buffer is filled, and this entire buffer is then output in one go. If flushing is needed (e.g. for when output is only produced rarely between heavy computations), it should be explicitly stated.

I am not completely sure if the above usage corresponds well to the intended workflow of the verbose function, but this concern should at least be considered before adding the mandatory flush statement. After all, the flush statement could just have been manually added in foo.sage.


---

Comment by rlm created at 2011-01-19 06:55:47

This is definitely an improvement, regardless. Let's get this merged.


---

Comment by rlm created at 2011-01-19 06:55:47

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:21:09

Resolution: fixed
