# Issue 3640: optional spkg polymake is broken with Sage 3.0.3/3.0.4

Issue created by migration from https://trac.sagemath.org/ticket/3640

Original creator: mabshoff

Original creation time: 2008-07-11 12:40:56

Assignee: mabshoff

CC:  mhampton

See http://math.univ-lyon1.fr/~tdumont/sageproblems/problems

The issue is that the spkg-install has hard coded spkg versions of cddlib and gmp.

Fixed spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-24 11:46:21

At

http://sage.math.washington.edu/home/mabshoff/polymake-2.2.p5.spkg

there is an spkg, but it needs cleaning up since it contains a bunch of junk. The actual diff is at 

http://sage.math.washington.edu/home/mabshoff/polymake-2.2.p5.spkg-install.diff

Applying that to the current spkg is probably less work.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-24 14:06:39

I have updated the spkg at

http://sage.math.washington.edu/home/mabshoff/polymake-2.2.p5.spkg

and made substantial improvements over the version I mentioned above a couple hours ago. It is close to something I would find acceptable :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-24 16:33:44

mhampton reported problems on OSX and I can reproduce them:

```
sage -t -long -optional "devel/sage/sage/geometry/polytope.py"
**********************************************************************
File "/Users/mabshoff/sage-3.2.2/devel/sage/sage/geometry/polytope.py", line 145:
    sage: P.facets()                            # optional
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-3.2.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.2.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mabshoff/sage-3.2.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        P.facets()                            # optional###line 145:
    sage: P.facets()                            # optional
      File "/Users/mabshoff/sage-3.2.2/local/lib/python2.5/site-packages/sage/geometry/polytope.py", line 152, in facets
        s = self.cmd('FACETS')
      File "/Users/mabshoff/sage-3.2.2/local/lib/python2.5/site-packages/sage/geometry/polytope.py", line 133, in cmd
        raise RuntimeError, err
    RuntimeError: polymake: WARNING: directory /Users/mabshoff/.polymake created for keeping individual user settings
    polymake: WARNING: file rgb.txt not found - no symbolic color names will be allowed
    polymake: WARNING: common::javaview_configure - autoconfiguration failed:
    'javaview' start script not found
    polymake: WARNING: common::postscript.rules - autoconfiguration failed:
    No known PostScript viewer program found,
    please specify your favorite viewer in the customization file.
    polymake: WARNING: common::geomview.rules - autoconfiguration failed:
    geomview main program not found
    polymake: WARNING: common::povray.rules - autoconfiguration failed:
    No known povray rendering program found,
    please specify your favorite viewer in the customization file.
    polymake: WARNING: graph::check_iso - autoconfiguration failed:
    none of the package nauty programs (dreadnaut*) found
    polymake: WARNING: polytope::porta.rules - autoconfiguration failed:
    PORTA package not found
    polymake: WARNING: polytope::bastat.rules - autoconfiguration failed:
    bastat program 'intpoints' not found
    polymake: WARNING: polytope::vinci.rules - autoconfiguration failed:
    'vinci' program not found
    polymake: WARNING: polytope::qhull.rules - autoconfiguration failed:
    'qhull' program not found
    polymake: WARNING: polytope::topcom.rules - autoconfiguration failed:
    TOPCOM program 'points2chiro' not found
    polymake: WARNING: polytope::splitstree.rules - autoconfiguration failed:
    SplitsTree package not found
     * Remember to run `polymake --reconfigure'
     * as soon as you have changed the customization file
     * and/or installed the missing software!
```


But the same doctest passes flawlessly on Linux, so this is some polymake problem.

Given the situation I would recommend that we merge the updated polymake.spkg and then sort out the problem on OSX afterwards since as is things are plain broken everywhere, which is even worst.

Cheers,

Michael


---

Comment by mhampton created at 2008-12-24 21:44:01

I agree: it is better than the present situation.  If I have time I will try to figure out the failure on OS X, but it is not my top priority right now.


---

Comment by mabshoff created at 2008-12-26 17:09:49

Resolution: fixed


---

Comment by mabshoff created at 2008-12-26 17:09:49

Merged in Sage 3.2.3.final and uploaded to the optional spkg repo.

Cheers,

Michael
