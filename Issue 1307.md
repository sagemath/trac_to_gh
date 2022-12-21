# Issue 1307: [graphs] Strongly regular graph database

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 19:54:36

Assignee: mhansen

CC:  mvngu dimpase

Keywords: graphs

From Chris Godsil's wishlist:


```
> 
>>> A database of small graphs. Put Ted Spence's strongly regular graphs
>>> into a
>>> database. (In this case the important thing is to have the graphs
>>> themselves,
>>> we would not necessarily need much data.)
```



---

Comment by rlm created at 2007-12-17 15:14:01

Changing component from combinatorics to graph theory.


---

Comment by rlm created at 2007-12-17 15:14:01

Changing keywords from "graphs" to "database".


---

Comment by rlm created at 2007-12-17 15:14:01

Changing assignee from mhansen to rlm.


---

Comment by mvngu created at 2009-06-27 00:45:38

CC'ing myself


---

Comment by ncohen created at 2009-08-22 16:43:36

If it just consists in converting the 32,548 graphs with parameters (36-15-6-6) to some database, I could do that with a bit of scripting... I saw there was in SAGE_DATA a file graphs.db ( sqlite format ), and the trouble is that I do not know what it contains, how to open it, and how to build one myself if it is what you expect... Could I know a bit more about this ? :-)


---

Comment by jason created at 2009-08-22 19:25:37

I believe that database just contains the data that is exposed here:

http://good.math.iastate.edu/grout/graphs/

You can download one of the many SQLITE GUI tools listed at http://www.sqlite.org/cvstrac/wiki?p=ManagementTools and look at the database.


---

Comment by ncohen created at 2009-08-23 09:08:19

Thank you !!! I understand how it works now :-)

Well, so what about this database ? Do you think it would be a good idea to build a sqlite database for Sage with these graphs ? I do not know, for example, if this database will be compressed in any way, because there are a lot of graphs available and it could become a bit heavy.. 
Is there anything more efficient, in case the users needs to enumerate them all ?


---

Comment by jason created at 2011-11-08 14:16:35

Here is a worksheet showing how to convert the graphs on Ted's page to Sage graphs: http://test.sagenb.org/home/pub/17/


---

Comment by kcrisman created at 2014-10-23 14:11:22

Hey, this would be really useful.  Jason, if you see this, can you paste that code here?  Also, I'm not sure where your database lives now.  This could easily become an optional database, and Magma also has such things.


---

Comment by ncohen created at 2014-10-23 14:17:43

(just a note: we have 4 constructors of families of strongly regular graphs from http://www.win.tue.nl/~aeb/graphs/srg/srgtab.html. AffineOrthogonalPolarGraph, OrthogonalPolarGraph, PaleyGraph, SymplecticGraph)


---

Comment by kcrisman created at 2014-10-23 14:34:06

Yes, just that's not a database :)
