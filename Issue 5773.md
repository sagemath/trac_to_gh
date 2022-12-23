# Issue 5773: notebook -- uploading a corrupted worksheet (sws file) results in blank screen (no useful error message)

Issue created by migration from https://trac.sagemath.org/ticket/5773

Original creator: was

Original creation time: 2009-04-13 04:13:46

Assignee: boothby

CC:  was

I uploaded a corrupted tarball and get a blank screen from the server instead of a useful error.  I also get this in the server logs

```
2009-04-12 21:12:35-0700 [-] cd "/Users/wstein/.sage/temp/teragon.local/61279/dir_1"; tar -jxf "/Users/wstein/.sage/temp/teragon.local/61279/dir_0/Homework_1____Devon_McMinn.sws"

bzip2: Data integrity error when decompressing.
	Input file = (stdin), output file = (stdout)

It is possible that the compressed file(s) have become corrupted.
You can use the -tvv option to test integrity of such files.

You can use the `bzip2recover' program to attempt to recover
data from undamaged sections of corrupted files.

tar: Child returned status 2
tar: Error exit delayed from previous errors


```



---

Comment by timdumol created at 2010-01-18 04:29:07

This is already fixed. Try:


```

$ echo '!@#rsfdsagarbage' > foo.sws

```


and try uploading it.


---

Comment by timdumol created at 2010-01-19 03:05:19

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 03:37:58

Resolution changed from duplicate to fixed
