# Issue 1762: Create optional graphviz package

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-01-12 04:42:08

Assignee: rlm

Graphviz is licensed under the Common Public License Version 1.0, which is incompatible with the GPL. ([see wikipedia](http://en.wikipedia.org/wiki/Common_Public_License))  So, we can't distribute graphviz packaged with Sage, but we can distribute it separately.

The dependencies are rather numerous, but most are optional. Of note, GD and libpng are already included in Sage. [http://www.graphviz.org/doc/build.html](http://www.graphviz.org/doc/build.html)


---

Comment by rlm created at 2008-01-19 01:51:03

Here is a broken spkg:

http://sage.math.washington.edu/home/rlmill/graphviz-broken-2.16.1.spkg

It fails to find the libpng library, because it is looking for `libpng12.dylib`, and the files are `libpng12.la` and `libpng12.a` instead. I bet there are more problems with the spkg, too, besides just missing an SPKG.txt. But this gets the ball rolling...


---

Comment by mabshoff created at 2008-01-19 04:40:44

I will look into this tomorrow. The problem that needs to be solved is autoconf.ac or something alike. I also think that the issue we need to solve is making python work with out libpng.dylib on 10.4.

Cheers,

Michael


---

Comment by rlm created at 2008-01-19 05:35:50

Some comments:

1. On lines 106-110 of `configure.ac`, they basically assume that .dylib is the only type of library name. Who knows where else this kind of assumption will cause trouble...

2. They use this on lines 351-353 of

http://www.graphviz.org/pub/graphviz/CURRENT/doxygen/html/gvconfig_8c-source.html

3. The variable name "DARWIN_DYLIB" is used only by graphviz- don't be fooled!

4. Seems like a fix that should go upstream...


---

Comment by rlm created at 2008-01-19 21:15:52

Yeah, forgot about the existence of:

https://networkx.lanl.gov/wiki/pygraphviz


---

Comment by rlm created at 2008-01-19 21:16:43

Oh, but pygraphviz still depends on graphviz...


---

Comment by boothby created at 2008-03-17 17:04:32

As an alternate solution, I've found a package called OGDF -- a GPL2/3 C++ package for drawing graphs:

http://www.ogdf.net/

this will take more work to wrap, but ultimately solves the problem better.


---

Comment by mabshoff created at 2008-05-23 00:37:36

I am fixing all the issue I am seeing. #3274 fixes the OSX compile, so we ought to be good.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 00:59:49

this patch fixes the OSX build issue


---

Attachment

The updated optional spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2//rc0/graphviz-2.16.1.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 01:41:20

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 01:41:20

The spkg has been uploaded to the optional spkg repo.

Cheers,

Michael
