# Issue 1971: notebook/jsmath -- make an optional spkg with the image fonts

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-29 12:21:42

Assignee: boothby

From the jsmath author:


```
The real solution is, of course, to install the jsMath TeX fonts and
avoid the whole issue.  For a private installation (like I expect most
sage installations are), where you are the only person looking at the
web pages that use jsMath, it is reasonable not to install the image
fonts because once you have the jsMath TeX fonts, there is no need for
anything else.  On the other hand, if you are hosting a public site,
where you don't know whether your reader has installed the fonts or
not, then you have to decide whether it is worth the space in order to
give those users a better view of the mathematics on your site.  My
own feeling is that the image fonts are so much superior to the
unicode results that it is worth it to me (because I know that most
people won't install the TeX fonts, so image-font mode turns out to be
the primary mode used by most viewers).  While I would like a method
with a smaller footprint on the server, I haven't found one that is as
reliable and maintainable as the image fonts.
```



---

Attachment

Necessary patch for the jsmath-image-fonts spkg to work.  Relies on #2116


---

Comment by jason created at 2008-02-09 04:47:48

The spkg is up at http://sage.math.washington.edu/home/jason/jsmath-image-fonts-1.3.spkg


---

Comment by mabshoff created at 2008-02-15 23:52:50

jsmath-fonts.patch looks good to me. I will upload the optional spkg to the repo shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 02:19:46

I am somewhat concerned about performance for this patch. On sage.math I get:

```
sage: %timeit is_package_installed("jsmath-image-fonts")
10 loops, best of 3: 87.9 ms per loop
```

We can easily cache the values and invalidate the catch every time we install a new package. The performance issues isn't critical in case the above code path is only called once per notebook session instantiation, but I don't know the notebook code well enough to make that call.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 02:30:14

Added jsmath-image-fonts-1.3.spkg to the optional spkg repo and mirrored it out.

Cheers,

Michael


---

Attachment

speeds up is-installed with a cache.


---

Comment by jason created at 2008-02-16 04:16:53

The is-installed-cache.patch file makes is_package_installed cached, like Michael suggested.  This patch should be applied *on top of* #2116.

Before:


```
sage: %timeit is_package_installed("jsmath-image")
10 loops, best of 3: 193 ms per loop
```


After:


```
sage: %timeit is_package_installed("jsmath-image")
10000 loops, best of 3: 111 µs per loop
```


I didn't cache the other functions (standard packages, experimental packages, etc.) because I don't know if they are used enough to make a difference.


---

Comment by jason created at 2008-02-16 04:29:25

Apply instead of first jsmath-fonts.patch


---

Attachment

The jsmath-fonts.2.patch also takes the installed package testing out of the page creation loop and just does the test once.  It should be (very marginally) faster, but theoretically better.

The jsmath-fonts.2.patch should be applied instead of the jsmath-fonts.patch.


---

Comment by mabshoff created at 2008-02-16 14:24:51

I like both new patches, so positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 14:27:37

Merged is-installed-cached.patch and jsmath-fonts.2.patch in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-16 14:27:37

Resolution: fixed
