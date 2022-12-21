# Issue 2113: twisted.web2 should be gzip compressing things it sends out to the notebook

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-08 14:32:43

Assignee: boothby

We ought to check to make sure that twisted has the gzip filter enabled and is sending things in zip encoding when it can.



---

Comment by cwitty created at 2008-02-08 19:15:21

This needs to be optional; for local notebooks (where the notebook and web browser are running on the same machine), this would very likely slow things down.


---

Attachment


---

Comment by jason created at 2008-10-19 05:10:03

I posted a new twisted spkg that contains needed modifications to make this work here:  http://sage.math.washington.edu/home/jason/twisted-8.1.0.p2.spkg

The above patch, combined with this new spkg, makes it so that pretty much all javascript, java, css, and a few other things are sent over the network compressed when the receiving host is not 'localhost' or '127.0.0.1'.  It seems to cut the transfer down to about a third of what it was.


---

Comment by jason created at 2008-10-19 05:11:15

I applied this patch on 3.1.4 after I applied the patch at #4267.


---

Comment by ddrake created at 2008-11-03 08:53:57

The spkg and patch here apply fine on top of #4267 with 3.2.alpha2. How do you measure the actual bandwidth usage? The patch seems simple enough -- I'll presume that twisted really does gzip what it claims to -- but I want to see lower bandwidth usage. :)


---

Comment by jason created at 2008-11-28 04:19:06

ddrake: use firebug in firefox.  It will show exactly how much each page and include is taking, bandwidth-wise and speed-wise.


---

Comment by was created at 2008-11-28 04:31:59

REFEREE REPORT:

I will give this a positive review when the following trivial things are all fixed. 

1. The spkg has a file in there that it shouldn't have in the root directory:

```
teragon-2:twisted-8.1.0.p2 wstein$ pwd
/Users/wstein/Desktop/twisted-8.1.0.p2
teragon-2:twisted-8.1.0.p2 wstein$ hg status
? gzip.py.patch
teragon-2:twisted-8.1.0.p2 wstein$ ls
SPKG.txt	gzip.py.patch	patches		spkg-install	src
```

Just delete it and remake the spkg.

The spkg itself compiles fine. 

That said, I'm confused as to what/where gzip.py.patch comes from.  Evidently mhansen wrote it.  It should probably be upstreamed?

2. There is a problem with SPKG.txt claiming mhansen did something, but actually Jason did:

```
20:26 < mhansen> How is this due to me?
20:26 < mhansen> I haven't seen this ticket before.
20:27 < jason--> the patch on the ticket just modifies twist.py
20:28 < ws-4636_2113> === twisted-8.1.0.p2 (Mike Hansen, October 18, 2008) === * Apply the patches to make the gzip filter deal 
                      with javascript mime types.
20:28 < ws-4636_2113> It's in SPKG.txt
20:28 < jason--> in the spkg that is on the ticket?
20:28 < ws-4636_2113> I think Jason Grout may have been impersonating you!
20:28 < mabshoff> And that is why we need SPKG.txt files
20:28 < jason--> is p1 from mhansen?
20:28 < jason--> (did I copy and not change something?)
20:28 < mabshoff> copy & paste?
20:28 < mhansen> I can't for the life of me remember doing that.
20:28 < ws-4636_2113> It's checked in by Jason.
20:29 < ws-4636_2113> So I think you didn't do it -- jason did.
```


3. The patch fails to apply, but almost applies:

```
was`@`sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hg_sage.applsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/2113/gzip.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/2113/gzip.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/9182/tmp_0.patch"
applying /home/was/.sage/temp/sage/9182/tmp_0.patch
patching file sage/server/notebook/twist.py
Hunk #10 FAILED at 1791
1 out of 11 hunks FAILED -- saving rejects to file sage/server/notebook/twist.py.rej
abort: patch failed to apply
```

| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
Only one hunk fails, which doesn't really impact much how this works.


---

Comment by jason created at 2008-11-28 04:35:32

Changing assignee from boothby to jason.


---

Comment by jason created at 2008-11-28 04:35:32

Changing status from new to assigned.


---

Comment by jason created at 2009-02-03 09:16:09

I've refreshed the spkg to address the concerns above.  The patch applies cleanly for me on a (slightly modified) sage 3.3alpha3.


---

Comment by was created at 2009-02-07 00:39:34

Looks good now.


---

Comment by mabshoff created at 2009-02-07 01:09:32

Merged twisted-8.1.0.p2.spkg in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-07 01:09:32

Resolution: fixed


---

Comment by ddrake created at 2009-02-10 10:13:20

Did gzip.patch get merged? On 3.3.alpha6, I don't see anything from that patch in twist.py, and I also don't see anything getting gzip'ed. When I apply the patch, I get some things, but not all, gzip encoded.

Also, on 3.3.alpha6, in spkg/installed, I see twisted-8.1.0.p1 and twisted-8.1.0.p2. Should there just be one there?


---

Comment by mabshoff created at 2009-02-10 10:16:16

Replying to [comment:13 ddrake]:
> Did gzip.patch get merged? On 3.3.alpha6, I don't see anything from that patch in twist.py, and I also don't see anything getting gzip'ed. When I apply the patch, I get some things, but not all, gzip encoded.

Oops, merging the patch now. I thought it was inside the spkg and did not apply to the Sage library. Thanks for checking. 

> Also, on 3.3.alpha6, in spkg/installed, I see twisted-8.1.0.p1 and twisted-8.1.0.p2. Should there just be one there?

Yes, I am deleting p1 now. 

I guess this wasn't the best merge :(

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 10:18:51

Dan,

I checked my 3.3.rc0 merge tree and I only have twisted-8.1.0.p2.spkg, so if you upgraded it would explain why you might have twisted-8.1.0.p1.spkg also in tree. Maybe -bdist also killed the extra twisted.spkg, but I am too lazy to find out :)

Cheers,

Michael
