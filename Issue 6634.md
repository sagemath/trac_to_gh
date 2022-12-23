# Issue 6634: biopython 1.49b broken with python-2.6

Issue created by migration from https://trac.sagemath.org/ticket/6634

Original creator: mhampton

Original creation time: 2009-07-27 02:44:06

Assignee: tbd

Keywords: biopython, bioinformatics

Biopython 1.49b doesn't install with python-2.6, so we should update the package.  Currently biopython is at 1.51-beta, for which a spkg is provided, but we should switch to 1.51 as soon as it comes out since it will have significant improvements.


---

Comment by mhampton created at 2009-07-27 02:45:10

Temporary spkg to fix this, until 1.51 comes out, is at:
http://www.d.umn.edu/~mhampton/biopython-1.51b.spkg


---

Comment by tkeller created at 2009-07-27 17:33:04

1.51b spkg installs cleanly and works fine with sage 4.1 on my linux kubuntu 9.04


---

Comment by mhampton created at 2009-08-17 15:44:43

I have made a spkg for biopython-1.51, which was released today:

http://sage.math.washington.edu/home/mhampton/biopython-1.51.spkg

Running the test suite gives some errors, but some of these are due to missing optional components.  I am inquiring about these on the biopython development list, but I don't think any of them are important enough to block this as an optional spkg.


---

Comment by mhampton created at 2009-08-18 14:14:25

tkeller,

Can you review this new package?  Besides testing installation, if you check that the spkg-install and SPKG.txt make sense then you can change the heading to [with spkg, positive review] and this can go into the optional packages.

In case you don't know, spkgs are just .tar.bz files with the extension renamed.  I usually unpack a temporary copy somewhere other than my sage folder in order to take a look when reviewing.

-Marshall


---

Comment by AlexGhitza created at 2009-08-19 12:53:13

Marshall,

I had started looking at this yesterday, so I just finished it now.  It builds successfully on sage.math, 32-bit Linux and 32-bit OSX 10.5.  Let's get it in!

One comment: if you happen to have some toy (or serious) Sage code using biopython, I strongly encourage you to get it into Sage so that we have at least some examples.


---

Comment by mvngu created at 2009-09-02 09:03:37

Is there a reason why biopython-1.51.spkg is not under revision control?

```
[mvngu@mod mvngu]$ tar -jxf biopython-1.51.spkg 
[mvngu@mod mvngu]$ cd biopython-1.51/
[mvngu@mod biopython-1.51]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
```



---

Comment by mvngu created at 2009-09-11 18:13:29

Merged in the optional packages repository at

http://www.sagemath.org/packages/optional/

The updated spkg is available at

http://www.sagemath.org/packages/optional/biopython-1.51.spkg


---

Comment by mvngu created at 2009-09-11 18:13:29

Resolution: fixed
