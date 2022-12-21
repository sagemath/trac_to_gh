# Issue 6032: split boost-1.34.1.cropped off the polybori.spkg

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-05-12 18:11:48

Assignee: mabshoff

To make it easier to update boost it should be split off the polybori.spkg. Some time in the future we should also update to a more current release. 

Note the following should be added to SPKG.txt since it makes the creation of the cropped boost automatic:

```
extract BoRing.tar.gz in src
extract boost-jam-3.1.14.tar.gz in src
copy cropped boost to src/boost_${BOOST_VER}.cropped
	create cropped boost with
	bcp --boost=boost_1_34_1 --scan PolyBoRi/M4RI/* PolyBoRi/polybori/include/* PolyBoRi/groebner/src/* PolyBoRi/PyPolyBoRi/* ../boost/t/boost_new/

	boost build subset
	tar jcvf boost.build.crop.tar.bz2 tools/build/v2/{kernel,util,build,tools,*.jam} boost-build.jam project-root.jam Jamfile.v2 Jamrules
```



---

Comment by mabshoff created at 2009-05-12 18:11:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-15 12:42:38

Two spkgs are at

 * http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/boost-cropped-1.34.1.spkg
 * http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/polybori-0.5rc.p7.spkg

You also need to apply the patches for install and deps.

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by malb created at 2009-05-15 20:41:43

Looks good.


---

Comment by mabshoff created at 2009-05-16 00:21:48

Resolution: fixed


---

Comment by mabshoff created at 2009-05-16 00:21:48

Merged both spkgs and both patches in Sage 4.0.alpha0.

Cheers,

Michael
