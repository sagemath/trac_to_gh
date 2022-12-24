# Issue 4774: Upgrade matplotlib to 0.98.4

archive/issues_004774.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  ekirkman mhansen\n\nNice things include very nice arrow functionality, new legend functionality, and a fill_between keyword:\n\nhttp://matplotlib.sourceforge.net/users/whats_new.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/4774\n\n",
    "created_at": "2008-12-12T21:47:52Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Upgrade matplotlib to 0.98.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4774",
    "user": "jason"
}
```
Assignee: tbd

CC:  ekirkman mhansen

Nice things include very nice arrow functionality, new legend functionality, and a fill_between keyword:

http://matplotlib.sourceforge.net/users/whats_new.html

Issue created by migration from https://trac.sagemath.org/ticket/4774





---

archive/issue_comments_036152.json:
```json
{
    "body": "0.98.5 which is a bug fix release over 0.98.4 is out.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T00:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36152",
    "user": "mabshoff"
}
```

0.98.5 which is a bug fix release over 0.98.4 is out.

Cheers,

Michael



---

archive/issue_comments_036153.json:
```json
{
    "body": "Changing component from algebra to packages.",
    "created_at": "2008-12-13T00:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36153",
    "user": "mabshoff"
}
```

Changing component from algebra to packages.



---

archive/issue_comments_036154.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-12-13T00:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36154",
    "user": "mabshoff"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_036155.json:
```json
{
    "body": "\n```\n[03:47] <mabshoff> jason-: if you want to update matplotlib make sure to base it off the spkg in 3.2.2.a2.\n[03:47] <jason-> okay\n[03:47] <mabshoff> This one: http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/matplotlib-0.98.3.p4.spkg\n```\n",
    "created_at": "2008-12-13T09:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36155",
    "user": "jason"
}
```


```
[03:47] <mabshoff> jason-: if you want to update matplotlib make sure to base it off the spkg in 3.2.2.a2.
[03:47] <jason-> okay
[03:47] <mabshoff> This one: http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/matplotlib-0.98.3.p4.spkg
```




---

archive/issue_comments_036156.json:
```json
{
    "body": "Latest upstream is 0.98.5.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-23T01:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36156",
    "user": "mabshoff"
}
```

Latest upstream is 0.98.5.2.

Cheers,

Michael



---

archive/issue_comments_036157.json:
```json
{
    "body": "A very preliminary package is up at http://sage.math.washington.edu/home/jason/matplotlib-svn6821.spkg , just in case someone wants to start using it (like Emily).\n\nLots of deprecation warnings and it probably also breaks stuff.  I'm fixing that now.  You probably should delete the directory $SAGE_ROOT/local/lib/python2.5/site-packages/matplotlib before installing to get rid of old cruft.",
    "created_at": "2009-01-24T06:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36157",
    "user": "jason"
}
```

A very preliminary package is up at http://sage.math.washington.edu/home/jason/matplotlib-svn6821.spkg , just in case someone wants to start using it (like Emily).

Lots of deprecation warnings and it probably also breaks stuff.  I'm fixing that now.  You probably should delete the directory $SAGE_ROOT/local/lib/python2.5/site-packages/matplotlib before installing to get rid of old cruft.



---

archive/issue_comments_036158.json:
```json
{
    "body": "(ekirkman: I just posted a *very* preliminary spkg.)",
    "created_at": "2009-01-24T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36158",
    "user": "jason"
}
```

(ekirkman: I just posted a *very* preliminary spkg.)



---

archive/issue_comments_036159.json:
```json
{
    "body": "This upgrade should fix #4465",
    "created_at": "2009-01-26T16:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36159",
    "user": "jason"
}
```

This upgrade should fix #4465



---

archive/issue_comments_036160.json:
```json
{
    "body": "apply in normal sage repository",
    "created_at": "2009-01-26T22:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36160",
    "user": "jason"
}
```

apply in normal sage repository



---

archive/issue_comments_036161.json:
```json
{
    "body": "Attachment [trac_4774_arrow.patch](tarball://root/attachments/some-uuid/ticket4774/trac_4774_arrow.patch) by jason created at 2009-01-26 22:49:47\n\nI've updated the spkg at http://sage.math.washington.edu/home/jason/matplotlib-svn6821.spkg\n\nIt should be ready to be reviewed now.",
    "created_at": "2009-01-26T22:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36161",
    "user": "jason"
}
```

Attachment [trac_4774_arrow.patch](tarball://root/attachments/some-uuid/ticket4774/trac_4774_arrow.patch) by jason created at 2009-01-26 22:49:47

I've updated the spkg at http://sage.math.washington.edu/home/jason/matplotlib-svn6821.spkg

It should be ready to be reviewed now.



---

archive/issue_comments_036162.json:
```json
{
    "body": "Once I've deleted the old `matplotlibrc` files from everywhere, as proposed in\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/11704ed70dc0d6e3\n\nI get failures related to `ft2font`:\n\n\n```\nsage: from matplotlib import ft2font\n\nImportError: dlopen(/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/ft2font.so, 2): Symbol not found: __cg_png_create_info_struct\n  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO\n  Expected in: /Users/rlmill/sage-3.3.alpha5/local/lib//libpng12.0.dylib\n\n```\n\n\nTrying it again doesn't even give the error again: Sage just thrashes.",
    "created_at": "2009-02-05T22:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36162",
    "user": "rlm"
}
```

Once I've deleted the old `matplotlibrc` files from everywhere, as proposed in

http://groups.google.com/group/sage-devel/browse_thread/thread/11704ed70dc0d6e3

I get failures related to `ft2font`:


```
sage: from matplotlib import ft2font

ImportError: dlopen(/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/ft2font.so, 2): Symbol not found: __cg_png_create_info_struct
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Users/rlmill/sage-3.3.alpha5/local/lib//libpng12.0.dylib

```


Trying it again doesn't even give the error again: Sage just thrashes.



---

archive/issue_comments_036163.json:
```json
{
    "body": "Moved my `/opt/local` branch and rebuilt, everything worked this time around. Sorry!\n\nPositive review for the spkg and patches. The thread above resolved the `matplotlibrc` issue. Full sail!",
    "created_at": "2009-02-05T23:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36163",
    "user": "rlm"
}
```

Moved my `/opt/local` branch and rebuilt, everything worked this time around. Sorry!

Positive review for the spkg and patches. The thread above resolved the `matplotlibrc` issue. Full sail!



---

archive/issue_comments_036164.json:
```json
{
    "body": "OK, moving `/opt/local` out of the way wasn't enough:\n\n\n```\nsage: from matplotlib.pyplot import scatter\n\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n<SNIP>\n/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/backends/backend_macosx.py in <module>()\n     18 \n     19 import matplotlib\n---> 20 from matplotlib.backends import _macosx\n     21 \n     22 def show():\n\nImportError: dlopen(/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/backends/_macosx.so, 2): Symbol not found: __cg_png_create_info_struct\n  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO\n  Expected in: /Users/rlmill/sage-3.3.alpha5/local/lib//libpng12.0.dylib\n```\n\n\nSo... wtf the linker is doing in `/System/Library/Frameworks` I can't say, but something is not right in Dodge.",
    "created_at": "2009-02-06T00:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36164",
    "user": "rlm"
}
```

OK, moving `/opt/local` out of the way wasn't enough:


```
sage: from matplotlib.pyplot import scatter

---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<SNIP>
/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/backends/backend_macosx.py in <module>()
     18 
     19 import matplotlib
---> 20 from matplotlib.backends import _macosx
     21 
     22 def show():

ImportError: dlopen(/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/backends/_macosx.so, 2): Symbol not found: __cg_png_create_info_struct
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Users/rlmill/sage-3.3.alpha5/local/lib//libpng12.0.dylib
```


So... wtf the linker is doing in `/System/Library/Frameworks` I can't say, but something is not right in Dodge.



---

archive/issue_comments_036165.json:
```json
{
    "body": "This spkg is twice as large as the previous:\n\n```\n-rw-r--r--@ 1 michaelabshoff  staff  4845513 Feb  2 17:28 matplotlib-0.98.3.p5.spkg\n-rw-r--r--  1 michaelabshoff  staff  8833439 Feb  5 16:52 matplotlib-svn6821.spkg\n```\n\nThere was some discussion on the matplotlib list about the new tarballs containing more documentation than the old ones, so we should look into getting rid of some of the documentation.\n\nThis spkg is important to get graph related plotting improvements into Sage, so let's try for 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T01:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36165",
    "user": "mabshoff"
}
```

This spkg is twice as large as the previous:

```
-rw-r--r--@ 1 michaelabshoff  staff  4845513 Feb  2 17:28 matplotlib-0.98.3.p5.spkg
-rw-r--r--  1 michaelabshoff  staff  8833439 Feb  5 16:52 matplotlib-svn6821.spkg
```

There was some discussion on the matplotlib list about the new tarballs containing more documentation than the old ones, so we should look into getting rid of some of the documentation.

This spkg is important to get graph related plotting improvements into Sage, so let's try for 3.3.

Cheers,

Michael



---

archive/issue_comments_036166.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-06T01:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36166",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_036167.json:
```json
{
    "body": "This needs work: \n\n* setupext.py.diff is not a unified diff, i.e. use -urN when diffing\n* some of the other diffs were created by diffing files in patches with files in src. The standard way in Sage to do this is to copy over foo from under source to foo.orig and then diff the changed foo against foo.orig in the same directory. Here also unified diff is required\n* the size issue need to be investigated, i.e. 4MB extra compressed for the spkg is a substantial increase in size\n* the name of the spkg should reflect the release branch it came from, i.e matplotlib-0.98.5.2-svnXXX\n\nAside from that:\n* We need to potentially make matplotlib not look for certain things on OSX like ghostview since that tends to pull in crap from Fink and/or MacPorts.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T01:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36167",
    "user": "mabshoff"
}
```

This needs work: 

* setupext.py.diff is not a unified diff, i.e. use -urN when diffing
* some of the other diffs were created by diffing files in patches with files in src. The standard way in Sage to do this is to copy over foo from under source to foo.orig and then diff the changed foo against foo.orig in the same directory. Here also unified diff is required
* the size issue need to be investigated, i.e. 4MB extra compressed for the spkg is a substantial increase in size
* the name of the spkg should reflect the release branch it came from, i.e matplotlib-0.98.5.2-svnXXX

Aside from that:
* We need to potentially make matplotlib not look for certain things on OSX like ghostview since that tends to pull in crap from Fink and/or MacPorts.

Cheers,

Michael



---

archive/issue_comments_036168.json:
```json
{
    "body": "I debugged this some more with rlm and the problem is the following:\n\n```\nOPTIONAL USETEX DEPENDENCIES\n               dvipng: /System/Library/Frameworks/ApplicationServices.frame\n                       work/Versions/A/Frameworks/ImageIO.framework/Version\n                       s/A/ImageIO\n          ghostscript: 8.62\n                latex: 3.1415926\n```\n\nSo killing dvipng support on OSX for now should solve the problem. His dvipng comes out of usr/texbin/dvipng.\n\nAnd while looking at this problem I also come up with a workable fix for the libpng issue once and for all - see \n\n   http://groups.google.com/group/sage-devel/t/5c655c1e1a2dc0b8\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T01:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36168",
    "user": "mabshoff"
}
```

I debugged this some more with rlm and the problem is the following:

```
OPTIONAL USETEX DEPENDENCIES
               dvipng: /System/Library/Frameworks/ApplicationServices.frame
                       work/Versions/A/Frameworks/ImageIO.framework/Version
                       s/A/ImageIO
          ghostscript: 8.62
                latex: 3.1415926
```

So killing dvipng support on OSX for now should solve the problem. His dvipng comes out of usr/texbin/dvipng.

And while looking at this problem I also come up with a workable fix for the libpng issue once and for all - see 

   http://groups.google.com/group/sage-devel/t/5c655c1e1a2dc0b8

Cheers,

Michael



---

archive/issue_comments_036169.json:
```json
{
    "body": "Ok, the culprit is this extension: \n\n```\ndef build_macosx(ext_modules, packages):\n    global BUILT_MACOSX\n    if BUILT_MACOSX: return # only build it if you you haven't already\n    module = Extension('matplotlib.backends._macosx',\n                       ['src/_macosx.m'],\n                       extra_link_args = ['-framework','Cocoa'],\n                      )\n    add_numpy_flags(module)\n    ext_modules.append(module)\n    BUILT_MACOSX = True\n```\n\nSince it links against a framework the only fix might be to fix the libpng.dylib issue on OSX once and for all.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T02:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36169",
    "user": "mabshoff"
}
```

Ok, the culprit is this extension: 

```
def build_macosx(ext_modules, packages):
    global BUILT_MACOSX
    if BUILT_MACOSX: return # only build it if you you haven't already
    module = Extension('matplotlib.backends._macosx',
                       ['src/_macosx.m'],
                       extra_link_args = ['-framework','Cocoa'],
                      )
    add_numpy_flags(module)
    ext_modules.append(module)
    BUILT_MACOSX = True
```

Since it links against a framework the only fix might be to fix the libpng.dylib issue on OSX once and for all.

Cheers,

Michael



---

archive/issue_comments_036170.json:
```json
{
    "body": "The next version, 0.98.3, is going to be released Real Soon Now (there's already an RC out).  So I'm biding my time waiting for that before fixing the issues with the spkg.",
    "created_at": "2009-02-13T05:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36170",
    "user": "jason"
}
```

The next version, 0.98.3, is going to be released Real Soon Now (there's already an RC out).  So I'm biding my time waiting for that before fixing the issues with the spkg.



---

archive/issue_comments_036171.json:
```json
{
    "body": "uh, that release is 0.98.5.3.",
    "created_at": "2009-02-13T05:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36171",
    "user": "jason"
}
```

uh, that release is 0.98.5.3.



---

archive/issue_comments_036172.json:
```json
{
    "body": "Here are the directories that changed by more than 100Kb.  A negative number means the directory decreased by that many kb.  A positive number means it increased by that many kb:\n\n\n```\n('src/lib', -4280)\n('src/lib/mpl_examples', -3108)\n('src/lib/enthought', -1936)\n('src/lib/enthought/traits', -1892)\n('src/lib/mpl_examples/data', -1840)\n('src/lib/enthought/traits/ui', -1012)\n('src/lib/mpl_examples/pylab_examples', -728)\n('src/lib/enthought/traits/ui/tk', -316)\n('src/lib/enthought/traits/tests', -240)\n('src/lib/mpl_examples/user_interfaces', -140)\n('src/lib/enthought/traits/ui/tests', -124)\n('src/lib/mpl_examples/api', -112)\n```\n\n\n\n```\n('src/doc/api', 104)\n('src/examples/tests/pngsuite', 108)\n('src/unit', 116)\n('src/examples/tests', 120)\n('src/examples/user_interfaces', 144)\n('src/examples/api', 144)\n('src/lib/matplotlib/mpl-data', 480)\n('src/lib/matplotlib/mpl-data/example', 528)\n('src/lib/matplotlib', 764)\n('src/examples/pylab_examples', 840)\n('src/doc/_static', 1216)\n('src/src', 1340)\n('src/examples/data', 2152)\n('src/doc/pyplots', 2424)\n('src/examples', 3696)\n('src/doc', 3828)\n('src/', 4688)\n```\n",
    "created_at": "2009-02-13T16:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36172",
    "user": "jason"
}
```

Here are the directories that changed by more than 100Kb.  A negative number means the directory decreased by that many kb.  A positive number means it increased by that many kb:


```
('src/lib', -4280)
('src/lib/mpl_examples', -3108)
('src/lib/enthought', -1936)
('src/lib/enthought/traits', -1892)
('src/lib/mpl_examples/data', -1840)
('src/lib/enthought/traits/ui', -1012)
('src/lib/mpl_examples/pylab_examples', -728)
('src/lib/enthought/traits/ui/tk', -316)
('src/lib/enthought/traits/tests', -240)
('src/lib/mpl_examples/user_interfaces', -140)
('src/lib/enthought/traits/ui/tests', -124)
('src/lib/mpl_examples/api', -112)
```



```
('src/doc/api', 104)
('src/examples/tests/pngsuite', 108)
('src/unit', 116)
('src/examples/tests', 120)
('src/examples/user_interfaces', 144)
('src/examples/api', 144)
('src/lib/matplotlib/mpl-data', 480)
('src/lib/matplotlib/mpl-data/example', 528)
('src/lib/matplotlib', 764)
('src/examples/pylab_examples', 840)
('src/doc/_static', 1216)
('src/src', 1340)
('src/examples/data', 2152)
('src/doc/pyplots', 2424)
('src/examples', 3696)
('src/doc', 3828)
('src/', 4688)
```




---

archive/issue_comments_036173.json:
```json
{
    "body": "so from the above, it looks like it was indeed the docs that increased by about 4mb (uncompressed)\n.",
    "created_at": "2009-02-13T16:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36173",
    "user": "jason"
}
```

so from the above, it looks like it was indeed the docs that increased by about 4mb (uncompressed)
.



---

archive/issue_comments_036174.json:
```json
{
    "body": "An updated spkg which addresses all of mabshoff's comments is here: http://sage.math.washington.edu/home/jason/matplotlib-0.98.5.3rc0-svn6910.spkg\n\nI also updated the spkg to the most recent svn, which is after the release candidate for 0.98.5.3.",
    "created_at": "2009-02-13T17:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36174",
    "user": "jason"
}
```

An updated spkg which addresses all of mabshoff's comments is here: http://sage.math.washington.edu/home/jason/matplotlib-0.98.5.3rc0-svn6910.spkg

I also updated the spkg to the most recent svn, which is after the release candidate for 0.98.5.3.



---

archive/issue_comments_036175.json:
```json
{
    "body": "The spkg installs cleanly for me (ubuntu 8.10).",
    "created_at": "2009-02-13T17:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36175",
    "user": "jason"
}
```

The spkg installs cleanly for me (ubuntu 8.10).



---

archive/issue_comments_036176.json:
```json
{
    "body": "Attachment [trac_4774_BIN.patch](tarball://root/attachments/some-uuid/ticket4774/trac_4774_BIN.patch) by jason created at 2009-02-13 17:36:38",
    "created_at": "2009-02-13T17:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36176",
    "user": "jason"
}
```

Attachment [trac_4774_BIN.patch](tarball://root/attachments/some-uuid/ticket4774/trac_4774_BIN.patch) by jason created at 2009-02-13 17:36:38



---

archive/issue_comments_036177.json:
```json
{
    "body": "I updated the bin repository patch to delete a reference to matplotlib that I missed before (in sage-env).",
    "created_at": "2009-02-13T17:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36177",
    "user": "jason"
}
```

I updated the bin repository patch to delete a reference to matplotlib that I missed before (in sage-env).



---

archive/issue_comments_036178.json:
```json
{
    "body": "This patch is on top of Jason's latest spkg and resolved libpng12 linking issues on OSX",
    "created_at": "2009-02-14T10:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36178",
    "user": "mabshoff"
}
```

This patch is on top of Jason's latest spkg and resolved libpng12 linking issues on OSX



---

archive/issue_comments_036179.json:
```json
{
    "body": "Attachment [matplotlib-0.98.5.3rc0-svn6910.p0.patch](tarball://root/attachments/some-uuid/ticket4774/matplotlib-0.98.5.3rc0-svn6910.p0.patch) by mabshoff created at 2009-02-14 10:50:37\n\nThe new spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/matplotlib-0.98.5.3rc0-svn6910.p0.spkg\n\nAll spkg changes by Jason look good, indeed they are **very** clean. I will review the patches to the various repos and hopefully Jason will give my changes a review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T10:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36179",
    "user": "mabshoff"
}
```

Attachment [matplotlib-0.98.5.3rc0-svn6910.p0.patch](tarball://root/attachments/some-uuid/ticket4774/matplotlib-0.98.5.3rc0-svn6910.p0.patch) by mabshoff created at 2009-02-14 10:50:37

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/matplotlib-0.98.5.3rc0-svn6910.p0.spkg

All spkg changes by Jason look good, indeed they are **very** clean. I will review the patches to the various repos and hopefully Jason will give my changes a review.

Cheers,

Michael



---

archive/issue_comments_036180.json:
```json
{
    "body": "Note that even with libpng.dylib and libpng12.dylib on OSX we are definitely linking against libpng12.dylib.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T10:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36180",
    "user": "mabshoff"
}
```

Note that even with libpng.dylib and libpng12.dylib on OSX we are definitely linking against libpng12.dylib.

Cheers,

Michael



---

archive/issue_comments_036181.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T10:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36181",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036182.json:
```json
{
    "body": "Changing assignee from mabshoff to jason.",
    "created_at": "2009-02-14T10:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36182",
    "user": "jason"
}
```

Changing assignee from mabshoff to jason.



---

archive/issue_comments_036183.json:
```json
{
    "body": "Positive review on Jason's patches to the Sage library as well as the bin repo.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T11:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36183",
    "user": "mabshoff"
}
```

Positive review on Jason's patches to the Sage library as well as the bin repo.

Cheers,

Michael



---

archive/issue_comments_036184.json:
```json
{
    "body": "mabshoff's new spkg builds fine for me.",
    "created_at": "2009-02-14T11:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36184",
    "user": "jason"
}
```

mabshoff's new spkg builds fine for me.



---

archive/issue_comments_036185.json:
```json
{
    "body": "Ok, there are some doctesting issues left with -long. Jason is looking into this.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T11:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36185",
    "user": "mabshoff"
}
```

Ok, there are some doctesting issues left with -long. Jason is looking into this.

Cheers,

Michael



---

archive/issue_comments_036186.json:
```json
{
    "body": "On sage.math we are having problems with the tkagg backend. It used to happen only occasionally, but now it happens every time I doctest plot.py:\n\n```\nFile \"/scratch/mabshoff/sage-3.3.rc1/devel/sage/sage/plot/plot.py\", line 172:\n    sage: grid(True)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[60]>\", line 1, in <module>\n        grid(True)###line 172:\n    sage: grid(True)\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py\", line 2453, in grid\n        ret =  gca().grid(*args, **kwargs)\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py\", line 572, in gca\n        ax =  gcf().gca(**kwargs)\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py\", line 274, in gcf\n        return figure()\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py\", line 252, in figure\n        **kwargs)\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/backends/backend_tkagg.py\", line 90, in new_figure_manager\n        window = Tk.Tk()\n      File \"/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/lib-tk/Tkinter.py\", line 1636, in __init__\n        self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)\n    TclError: no display name and no $DISPLAY environment variable\n```\n\n\nWe already disable tkagg on Itanium/Linux, so let's get rid of it globally.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T11:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36186",
    "user": "mabshoff"
}
```

On sage.math we are having problems with the tkagg backend. It used to happen only occasionally, but now it happens every time I doctest plot.py:

```
File "/scratch/mabshoff/sage-3.3.rc1/devel/sage/sage/plot/plot.py", line 172:
    sage: grid(True)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[60]>", line 1, in <module>
        grid(True)###line 172:
    sage: grid(True)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 2453, in grid
        ret =  gca().grid(*args, **kwargs)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 572, in gca
        ax =  gcf().gca(**kwargs)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 274, in gcf
        return figure()
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 252, in figure
        **kwargs)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/backends/backend_tkagg.py", line 90, in new_figure_manager
        window = Tk.Tk()
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/lib-tk/Tkinter.py", line 1636, in __init__
        self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
    TclError: no display name and no $DISPLAY environment variable
```


We already disable tkagg on Itanium/Linux, so let's get rid of it globally.

Cheers,

Michael



---

archive/issue_comments_036187.json:
```json
{
    "body": "I have disabled tkagg globally and the problem above goes away. The spkg by the same names as the last one above is at\n\n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/matplotlib-0.98.5.3rc0-svn6910.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T12:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36187",
    "user": "mabshoff"
}
```

I have disabled tkagg globally and the problem above goes away. The spkg by the same names as the last one above is at


  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/matplotlib-0.98.5.3rc0-svn6910.p0.spkg

Cheers,

Michael



---

archive/issue_comments_036188.json:
```json
{
    "body": "okay, new spkg up here: http://sage.math.washington.edu/home/jason/matplotlib-0.98.5.3rc0-svn6910.p1.spkg\n\nThis adds a fix (i.e., kludge) that lets matplotlib draw very tiny errors, which were giving us problems before.  I also cleaned up a few things from mabshoff's changes :).",
    "created_at": "2009-02-14T12:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36188",
    "user": "jason"
}
```

okay, new spkg up here: http://sage.math.washington.edu/home/jason/matplotlib-0.98.5.3rc0-svn6910.p1.spkg

This adds a fix (i.e., kludge) that lets matplotlib draw very tiny errors, which were giving us problems before.  I also cleaned up a few things from mabshoff's changes :).



---

archive/issue_comments_036189.json:
```json
{
    "body": "Jason's latest patch spkg fixes the problem, so an overall positive review via crossover between Jason's and my work.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T12:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36189",
    "user": "mabshoff"
}
```

Jason's latest patch spkg fixes the problem, so an overall positive review via crossover between Jason's and my work.

Cheers,

Michael



---

archive/issue_comments_036190.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T12:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36190",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036191.json:
```json
{
    "body": "Merged\n\n* matplotlib-0.98.5.3rc0-svn6910.p1.spkg\n* trac_4774_arrow.patch (2.6 kB) \n* trac_4774_BIN.patch \n\nin Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T12:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4774#issuecomment-36191",
    "user": "mabshoff"
}
```

Merged

* matplotlib-0.98.5.3rc0-svn6910.p1.spkg
* trac_4774_arrow.patch (2.6 kB) 
* trac_4774_BIN.patch 

in Sage 3.3.rc1.

Cheers,

Michael
