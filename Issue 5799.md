# Issue 5799: [with patch, needs review] jsMath, favicon, and logo for live, static, and offline docs

archive/issues_005799.json:
```json
{
    "body": "Assignee: tba\n\nA few changes to\n\n* Enable jsMath in static and offline docs.\n\n* Display a Sage favicon in static and offline docs.\n\n* Display a Sage logo in live, static, and offline docs.\n\n\"Offline\" docs are just those accessed via file:///.\n\nI'm not sure whether/how Mercurial handles binary files, so I've attached two patches.  One mentions the added favicon and logo files; the other doesn't.  To get the png files themselves in the right place, I first created doc/common/static.  Then, in this directory I did\n\nwget http://www.sagemath.org/pix/sageicon.png\n\nand\n\nln -s ../../../../../data/extcode/notebook/images/sagelogo.png .\n\nI've attached these, too.\n\nNote: There's a favicon.ico in the same extcode directory, but it's not transparent.  There is another sagelogo.png in SAGE_ROOT/data/extcode/images, but its dimensions are larger.\n\nThe jsMath issue was mentioned on sage-devel:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/40eab3f9610e061d/eb93a3930e79ea3a?#eb93a3930e79ea3a\n\nThe favicon and logo were mentioned in connection with a doc sidebar toggle:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725/4807f5553bdbd6b0?#4807f5553bdbd6b0\n\nI'll make a separate ticket for the toggle.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5799\n\n",
    "created_at": "2009-04-16T04:35:32Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] jsMath, favicon, and logo for live, static, and offline docs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5799",
    "user": "https://github.com/qed777"
}
```
Assignee: tba

A few changes to

* Enable jsMath in static and offline docs.

* Display a Sage favicon in static and offline docs.

* Display a Sage logo in live, static, and offline docs.

"Offline" docs are just those accessed via file:///.

I'm not sure whether/how Mercurial handles binary files, so I've attached two patches.  One mentions the added favicon and logo files; the other doesn't.  To get the png files themselves in the right place, I first created doc/common/static.  Then, in this directory I did

wget http://www.sagemath.org/pix/sageicon.png

and

ln -s ../../../../../data/extcode/notebook/images/sagelogo.png .

I've attached these, too.

Note: There's a favicon.ico in the same extcode directory, but it's not transparent.  There is another sagelogo.png in SAGE_ROOT/data/extcode/images, but its dimensions are larger.

The jsMath issue was mentioned on sage-devel:

http://groups.google.com/group/sage-devel/browse_thread/thread/40eab3f9610e061d/eb93a3930e79ea3a?#eb93a3930e79ea3a

The favicon and logo were mentioned in connection with a doc sidebar toggle:

http://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725/4807f5553bdbd6b0?#4807f5553bdbd6b0

I'll make a separate ticket for the toggle.

Issue created by migration from https://trac.sagemath.org/ticket/5799





---

archive/issue_comments_045406.json:
```json
{
    "body": "To create a patch that contains a png you need to export a git style patch. Then export two patches, one for the Sage library and one for the ext repo. The names should be \n\n* trac_5799_sage_$FOO\n* trac_5799_ext_$BAR\n \nrespectively. It is generally a good idea to split tickets into independent tasks, i.e. this is a borderline case and can be done via one ticket.\n\nThis also strikes me as kind of odd:\n\n```\n<script type=\"text/javascript\" src=\"../../../../../../../local/notebook/javascript/jsmath/easy/load.js\"></script> \n```\n\ngiven that everywhere else we use \n\n```\n<script type=\"text/javascript\" src=\"/javascript_local/$FOO\"></script>\n```\n\nbut that might be unavoidable. \n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T05:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

To create a patch that contains a png you need to export a git style patch. Then export two patches, one for the Sage library and one for the ext repo. The names should be 

* trac_5799_sage_$FOO
* trac_5799_ext_$BAR
 
respectively. It is generally a good idea to split tickets into independent tasks, i.e. this is a borderline case and can be done via one ticket.

This also strikes me as kind of odd:

```
<script type="text/javascript" src="../../../../../../../local/notebook/javascript/jsmath/easy/load.js"></script> 
```

given that everywhere else we use 

```
<script type="text/javascript" src="/javascript_local/$FOO"></script>
```

but that might be unavoidable. 


Cheers,

Michael



---

archive/issue_comments_045407.json:
```json
{
    "body": "Attachment [trac_5799_ext_sageicon.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_ext_sageicon.patch) by @qed777 created at 2009-04-16 07:50:07",
    "created_at": "2009-04-16T07:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45407",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5799_ext_sageicon.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_ext_sageicon.patch) by @qed777 created at 2009-04-16 07:50:07



---

archive/issue_comments_045408.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> To create a patch [...]\n\nThanks for the tips!  Take two attached.\n\n> This also strikes me as kind of odd:\n\nI'm about to attach an alternative to trac_5799_sage_jsmath_doc.patch.",
    "created_at": "2009-04-16T08:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45408",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:1 mabshoff]:
> To create a patch [...]

Thanks for the tips!  Take two attached.

> This also strikes me as kind of odd:

I'm about to attach an alternative to trac_5799_sage_jsmath_doc.patch.



---

archive/issue_comments_045409.json:
```json
{
    "body": "Attachment [trac_5799_sage_jsmath_doc_alt.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_sage_jsmath_doc_alt.patch) by @qed777 created at 2009-04-16 08:23:42\n\nSomewhat less efficient alternative to trac_5799_sage_jsmath_doc.patch.",
    "created_at": "2009-04-16T08:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45409",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5799_sage_jsmath_doc_alt.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_sage_jsmath_doc_alt.patch) by @qed777 created at 2009-04-16 08:23:42

Somewhat less efficient alternative to trac_5799_sage_jsmath_doc.patch.



---

archive/issue_comments_045410.json:
```json
{
    "body": "Cool, I deleted the old patches to make the history cleaner. If you post updated patches you should also change back the summary to \"needs review\". I did that in this case already.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T08:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Cool, I deleted the old patches to make the history cleaner. If you post updated patches you should also change back the summary to "needs review". I did that in this case already.

Cheers,

Michael



---

archive/issue_comments_045411.json:
```json
{
    "body": "I applied the 'ext' and 'alt sage' patches, and tested \"en/tutorial html\".  It all looks good.",
    "created_at": "2009-04-17T15:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45411",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

I applied the 'ext' and 'alt sage' patches, and tested "en/tutorial html".  It all looks good.



---

archive/issue_comments_045412.json:
```json
{
    "body": "Better cross-browser favicon support. Goes with trac_5799_sage_jsmath_doc_v2.patch.",
    "created_at": "2009-06-10T09:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45412",
    "user": "https://github.com/qed777"
}
```

Better cross-browser favicon support. Goes with trac_5799_sage_jsmath_doc_v2.patch.



---

archive/issue_comments_045413.json:
```json
{
    "body": "Attachment [trac_5799_sage_jsmath_doc_v2.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_sage_jsmath_doc_v2.patch) by @qed777 created at 2009-06-10 09:26:16\n\nBetter cross-browser favicon support, auto relative paths. Apply trac_5799_ext_icons_v2.patch first.",
    "created_at": "2009-06-10T09:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45413",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5799_sage_jsmath_doc_v2.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_sage_jsmath_doc_v2.patch) by @qed777 created at 2009-06-10 09:26:16

Better cross-browser favicon support, auto relative paths. Apply trac_5799_ext_icons_v2.patch first.



---

archive/issue_comments_045414.json:
```json
{
    "body": "The `*_v2` pair replaces the earlier versions.\n\n* Same [sageicon.png](http://www.sagemath.org/pix/sageicon.png) as in the first patch.\n* ImageMagick gives a \"true\" ico file: `convert sageicon.png favicon.ico`.\n* Tested in FF3, O9 on Linux, and in Cr2, FF3, IE8, O9, S3 on Windows XP. Whether the icon is transparent and visible for live, static, and offline docs is browser-dependent.\n* Automatic relative paths for the favicon, logo, and jsMath.  This is important, e.g., in the reference manual.\n* #4714 should take care of the unknown jsMath macros.",
    "created_at": "2009-06-10T10:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45414",
    "user": "https://github.com/qed777"
}
```

The `*_v2` pair replaces the earlier versions.

* Same [sageicon.png](http://www.sagemath.org/pix/sageicon.png) as in the first patch.
* ImageMagick gives a "true" ico file: `convert sageicon.png favicon.ico`.
* Tested in FF3, O9 on Linux, and in Cr2, FF3, IE8, O9, S3 on Windows XP. Whether the icon is transparent and visible for live, static, and offline docs is browser-dependent.
* Automatic relative paths for the favicon, logo, and jsMath.  This is important, e.g., in the reference manual.
* #4714 should take care of the unknown jsMath macros.



---

archive/issue_comments_045415.json:
```json
{
    "body": "Looks good.  Positive review.\n\nDoes this mean that we should make `--jsmath` the default for building html docs?  It's much faster than building without using jsmath.",
    "created_at": "2009-06-27T17:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45415",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good.  Positive review.

Does this mean that we should make `--jsmath` the default for building html docs?  It's much faster than building without using jsmath.



---

archive/issue_comments_045416.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> Does this mean that we should make `--jsmath` the default for building html docs?  It's much faster than building without using jsmath.\n\nI think `\\QQ` and friends generate an unsightly error message.  I'll try to learn how to make an spkg, for #4714 and #5447.",
    "created_at": "2009-06-27T22:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45416",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:7 jhpalmieri]:
> Does this mean that we should make `--jsmath` the default for building html docs?  It's much faster than building without using jsmath.

I think `\QQ` and friends generate an unsightly error message.  I'll try to learn how to make an spkg, for #4714 and #5447.



---

archive/issue_events_006047.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-04T01:40:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5799#event-6047"
}
```



---

archive/issue_comments_045417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T01:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45417",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_045418.json:
```json
{
    "body": "In order to get the `sage -sdist` command to work after applying this patch, I had to copy all of the files over to `doc/common/static` as actual files, since something in the build system could not find the files as links. I will post the extra patch on this ticket, which was necessary to roll `sage-4.1.rc0`.",
    "created_at": "2009-07-04T21:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45418",
    "user": "https://github.com/rlmill"
}
```

In order to get the `sage -sdist` command to work after applying this patch, I had to copy all of the files over to `doc/common/static` as actual files, since something in the build system could not find the files as links. I will post the extra patch on this ticket, which was necessary to roll `sage-4.1.rc0`.



---

archive/issue_comments_045419.json:
```json
{
    "body": "This is what happened:\n\n```\n[geom sage-4.1.alpha3]$ ./sage -sdist 4.1.rc0\nUpdating Cython code....\nTime to execute 0 commands: 1.50203704834e-05 seconds\nFinished compiling Cython code (time = 0.324697971344 seconds)\nrunning install\nrunning build\nrunning build_py\ncopying sage/version.py -> build/lib.linux-x86_64-2.6/sage\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.00903582572937 seconds.\nrunning install_lib\ncopying build/lib.linux-x86_64-2.6/sage/version.py -> /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage\nbyte-compiling /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage/version.py to version.pyc\nrunning install_egg_info\nWriting /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage-4.1.rc0-py2.6.egg-info\ncp: cannot stat `*.sage': No such file or directory\ncp: cannot stat `ipythonrc': No such file or directory\ncp: cannot stat `spkg/update': No such file or directory\nrm: cannot remove `doc-*.spkg': No such file or directory\ndiff -r f307132d9d7c sage/version.py\n--- a/sage/version.py   Thu Jul 02 11:52:36 2009 +0200\n+++ b/sage/version.py   Sat Jul 04 12:58:13 2009 -0700\n@@ -1,2 +1,2 @@\n \"\"\"nodoctests\"\"\"\n-version='4.1.alpha3'; date='2009-07-02'\n+version='4.1.rc0'; date='2009-07-04'\nM sage/version.py\ncp: cannot stat `build.py': No such file or directory\ncp: cannot stat `clib.py': No such file or directory\ncp: cannot stat `sagebuild.py': No such file or directory\ncp: warning: source file `spkg-delauto' specified more than once\ncp: cannot stat `debian': No such file or directory\nrm: cannot remove `c_lib/*.so': No such file or directory\nrm: cannot remove `c_lib/*.os': No such file or directory\nDeleting autogenerated file ./matrix/matrix_rational_dense.c\n\n...<SNIP>...\n\nDeleting autogenerated file ./algebras/quatalg/quaternion_algebra_cython.cpp\nrunning sdist\nerror: doc/common/static/sageicon.png: No such file or directory\n./spkg-dist: line 54: cd: dist: No such file or directory\ngzip: sage-4.1.rc0.tar.gz: No such file or directory\nbzip2: Can't open input file sage-4.1.rc0.tar: No such file or directory.\nmv: cannot stat `sage-4.1.rc0.tar.bz2': No such file or directory\nmv: cannot stat `dist/sage-4.1.rc0.spkg': No such file or directory\nThe package sage-4.1.rc0.spkg wasn't created.\nError building the Sage packages.\n```\n\n\nNo point in posting a huge patch, so here is a link:\n\nhttp://sage.math.washington.edu/home/rlmill/trac_5799-unlink.patch",
    "created_at": "2009-07-04T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45419",
    "user": "https://github.com/rlmill"
}
```

This is what happened:

```
[geom sage-4.1.alpha3]$ ./sage -sdist 4.1.rc0
Updating Cython code....
Time to execute 0 commands: 1.50203704834e-05 seconds
Finished compiling Cython code (time = 0.324697971344 seconds)
running install
running build
running build_py
copying sage/version.py -> build/lib.linux-x86_64-2.6/sage
running build_ext
Total time spent compiling C/C++ extensions:  0.00903582572937 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/version.py -> /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage
byte-compiling /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage/version.py to version.pyc
running install_egg_info
Writing /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage-4.1.rc0-py2.6.egg-info
cp: cannot stat `*.sage': No such file or directory
cp: cannot stat `ipythonrc': No such file or directory
cp: cannot stat `spkg/update': No such file or directory
rm: cannot remove `doc-*.spkg': No such file or directory
diff -r f307132d9d7c sage/version.py
--- a/sage/version.py   Thu Jul 02 11:52:36 2009 +0200
+++ b/sage/version.py   Sat Jul 04 12:58:13 2009 -0700
@@ -1,2 +1,2 @@
 """nodoctests"""
-version='4.1.alpha3'; date='2009-07-02'
+version='4.1.rc0'; date='2009-07-04'
M sage/version.py
cp: cannot stat `build.py': No such file or directory
cp: cannot stat `clib.py': No such file or directory
cp: cannot stat `sagebuild.py': No such file or directory
cp: warning: source file `spkg-delauto' specified more than once
cp: cannot stat `debian': No such file or directory
rm: cannot remove `c_lib/*.so': No such file or directory
rm: cannot remove `c_lib/*.os': No such file or directory
Deleting autogenerated file ./matrix/matrix_rational_dense.c

...<SNIP>...

Deleting autogenerated file ./algebras/quatalg/quaternion_algebra_cython.cpp
running sdist
error: doc/common/static/sageicon.png: No such file or directory
./spkg-dist: line 54: cd: dist: No such file or directory
gzip: sage-4.1.rc0.tar.gz: No such file or directory
bzip2: Can't open input file sage-4.1.rc0.tar: No such file or directory.
mv: cannot stat `sage-4.1.rc0.tar.bz2': No such file or directory
mv: cannot stat `dist/sage-4.1.rc0.spkg': No such file or directory
The package sage-4.1.rc0.spkg wasn't created.
Error building the Sage packages.
```


No point in posting a huge patch, so here is a link:

http://sage.math.washington.edu/home/rlmill/trac_5799-unlink.patch



---

archive/issue_comments_045420.json:
```json
{
    "body": "The new patch seems to have the same observable effect as the previous set in the usual browsers on Linux and Windows XP.  But the AMS symbol font `msbm10` won't be available in the static and offline docs.\n\nI'll venture that having extra copies of the favicons and logo in the Sage tree is not a big deal.  Ideally, jsMath should have a single home, e.g., so that planned changes (cf. #4714) to `easy/load.js` affect the live, static, and offline docs equally.\n\nPerhaps we can make the symbolic link itself in jsMath's `spkg-install`.  Does this mean we should remove the link from version control?  If so, we're [almost] done.",
    "created_at": "2009-07-05T23:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45420",
    "user": "https://github.com/qed777"
}
```

The new patch seems to have the same observable effect as the previous set in the usual browsers on Linux and Windows XP.  But the AMS symbol font `msbm10` won't be available in the static and offline docs.

I'll venture that having extra copies of the favicons and logo in the Sage tree is not a big deal.  Ideally, jsMath should have a single home, e.g., so that planned changes (cf. #4714) to `easy/load.js` affect the live, static, and offline docs equally.

Perhaps we can make the symbolic link itself in jsMath's `spkg-install`.  Does this mean we should remove the link from version control?  If so, we're [almost] done.



---

archive/issue_comments_045421.json:
```json
{
    "body": "I'm worried, since a fresh install of sage-4.1.rc0 is missing most of these files in `doc/common/static`:\n\n\n```\n[geom sage-main]$ cd doc/common/static/\n[geom static]$ ls\ntotal 4.0K\ndrwxr-xr-x 3 rlmill rlmill 4.0K 2009-07-04 14:18 jsmath\n[geom static]$ ls jsmath\ntotal 16K\n-rw-r--r-- 1 rlmill rlmill  12K 2009-07-04 14:13 COPYING.txt\ndrwxr-xr-x 3 rlmill rlmill 4.0K 2009-07-04 14:18 fonts\n```\n\n\nHas anyone tested a fresh build of sage-4.1.rc0 to see if things related to this ticket work?",
    "created_at": "2009-07-07T18:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45421",
    "user": "https://github.com/rlmill"
}
```

I'm worried, since a fresh install of sage-4.1.rc0 is missing most of these files in `doc/common/static`:


```
[geom sage-main]$ cd doc/common/static/
[geom static]$ ls
total 4.0K
drwxr-xr-x 3 rlmill rlmill 4.0K 2009-07-04 14:18 jsmath
[geom static]$ ls jsmath
total 16K
-rw-r--r-- 1 rlmill rlmill  12K 2009-07-04 14:13 COPYING.txt
drwxr-xr-x 3 rlmill rlmill 4.0K 2009-07-04 14:18 fonts
```


Has anyone tested a fresh build of sage-4.1.rc0 to see if things related to this ticket work?



---

archive/issue_comments_045422.json:
```json
{
    "body": "I'm seriously thinking about reverting this ticket, since there are obviously some assumptions the sdist script is making, which are conflicting with the solutions used for this patch. For now, I'm reopening the ticket, until I can get this resolved one way or another.",
    "created_at": "2009-07-07T18:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45422",
    "user": "https://github.com/rlmill"
}
```

I'm seriously thinking about reverting this ticket, since there are obviously some assumptions the sdist script is making, which are conflicting with the solutions used for this patch. For now, I'm reopening the ticket, until I can get this resolved one way or another.



---

archive/issue_comments_045423.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-07T18:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45423",
    "user": "https://github.com/rlmill"
}
```

Changing status from closed to reopened.



---

archive/issue_events_006048.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-07T18:58:27Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5799#event-6048"
}
```



---

archive/issue_comments_045424.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-07T18:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45424",
    "user": "https://github.com/rlmill"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_045425.json:
```json
{
    "body": "Attachment [trac_5799_manifest.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_manifest.patch) by @jhpalmieri created at 2009-07-07 19:40:57",
    "created_at": "2009-07-07T19:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45425",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_5799_manifest.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799_manifest.patch) by @jhpalmieri created at 2009-07-07 19:40:57



---

archive/issue_comments_045426.json:
```json
{
    "body": "This is a bit of a shot in the dark, but does trac_5799_manifest.patch help?",
    "created_at": "2009-07-07T19:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45426",
    "user": "https://github.com/jhpalmieri"
}
```

This is a bit of a shot in the dark, but does trac_5799_manifest.patch help?



---

archive/issue_comments_045427.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> This is a bit of a shot in the dark, but does trac_5799_manifest.patch help?\n\nI think this is what I was looking for. Thank you!",
    "created_at": "2009-07-07T19:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45427",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:15 jhpalmieri]:
> This is a bit of a shot in the dark, but does trac_5799_manifest.patch help?

I think this is what I was looking for. Thank you!



---

archive/issue_comments_045428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-07T21:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45428",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_006049.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-07T21:22:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5799#event-6049"
}
```



---

archive/issue_comments_045429.json:
```json
{
    "body": "`trac_5799_manifest.patch` merged in sage-4.1.rc1",
    "created_at": "2009-07-07T21:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45429",
    "user": "https://github.com/rlmill"
}
```

`trac_5799_manifest.patch` merged in sage-4.1.rc1



---

archive/issue_comments_045430.json:
```json
{
    "body": "As suggested by William, the `MANIFEST.in` changes were reverted to just adding the line `recursive-include doc/common/static *`.\n\nhttp://docs.python.org/distutils/commandref.html#sdist-cmd",
    "created_at": "2009-07-08T01:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45430",
    "user": "https://github.com/rlmill"
}
```

As suggested by William, the `MANIFEST.in` changes were reverted to just adding the line `recursive-include doc/common/static *`.

http://docs.python.org/distutils/commandref.html#sdist-cmd



---

archive/issue_comments_045431.json:
```json
{
    "body": "Is it possible to include symbolic links in `MANIFEST.in`?  Unless I'm wrong, we now have jsMath installed in `doc/common/static` **and** `javascript_local`.  Do we really want this?  Besides putting upstream code under version control in the Sage library, this complicates, e.g., the resolution of #4714.",
    "created_at": "2009-07-19T06:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45431",
    "user": "https://github.com/qed777"
}
```

Is it possible to include symbolic links in `MANIFEST.in`?  Unless I'm wrong, we now have jsMath installed in `doc/common/static` **and** `javascript_local`.  Do we really want this?  Besides putting upstream code under version control in the Sage library, this complicates, e.g., the resolution of #4714.



---

archive/issue_comments_045432.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n> Is it possible to include symbolic links in `MANIFEST.in`?\n\nI had wondered this myself. The only way to know for sure is to try it, roll a new source tarball (via `sage -sdist`), install the \"new version,\" and see whether the notebook still works...",
    "created_at": "2009-07-20T14:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45432",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:20 mpatel]:
> Is it possible to include symbolic links in `MANIFEST.in`?

I had wondered this myself. The only way to know for sure is to try it, roll a new source tarball (via `sage -sdist`), install the "new version," and see whether the notebook still works...



---

archive/issue_comments_045433.json:
```json
{
    "body": "Attempt to get distutils to preserve symbolic links.",
    "created_at": "2009-07-21T10:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45433",
    "user": "https://github.com/qed777"
}
```

Attempt to get distutils to preserve symbolic links.



---

archive/issue_comments_045434.json:
```json
{
    "body": "Attachment [trac_5799-redux_setup_py.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799-redux_setup_py.patch) by @qed777 created at 2009-07-21 11:28:30\n\nReplying to [comment:21 rlm]:\n> Replying to [comment:20 mpatel]:\n> > Is it possible to include symbolic links in `MANIFEST.in`?\n> I had wondered this myself. The only way to know for sure is to try it, roll a new source tarball (via `sage -sdist`), install the \"new version,\" and see whether the notebook still works...\nThis [attachment:trac_5799-redux_setup_py.patch patch] alters `setup.py` so that it preserves symlinks.  However, I'm far from convinced that it's the right approach.  Is it possible to identify and copy broken links in Python?  In particular:\n\n* In `sage_findall()`, can we refine or avoid using the exception handler?  Perhaps it's better to use [os.walk()](http://markmail.org/message/dcv4g5b2b4exw64u), but the `os.path.is*()` family actually follows symlinks.\n* Is there a Pythonic analogue of `cp --preserve=links --no-dereference`?\n\nPossible alternatives:\n\n* Make a symlink in some `spkg-install`.\n* Have Mercurial reconstitute the link.",
    "created_at": "2009-07-21T11:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45434",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5799-redux_setup_py.patch](tarball://root/attachments/some-uuid/ticket5799/trac_5799-redux_setup_py.patch) by @qed777 created at 2009-07-21 11:28:30

Replying to [comment:21 rlm]:
> Replying to [comment:20 mpatel]:
> > Is it possible to include symbolic links in `MANIFEST.in`?
> I had wondered this myself. The only way to know for sure is to try it, roll a new source tarball (via `sage -sdist`), install the "new version," and see whether the notebook still works...
This [attachment:trac_5799-redux_setup_py.patch patch] alters `setup.py` so that it preserves symlinks.  However, I'm far from convinced that it's the right approach.  Is it possible to identify and copy broken links in Python?  In particular:

* In `sage_findall()`, can we refine or avoid using the exception handler?  Perhaps it's better to use [os.walk()](http://markmail.org/message/dcv4g5b2b4exw64u), but the `os.path.is*()` family actually follows symlinks.
* Is there a Pythonic analogue of `cp --preserve=links --no-dereference`?

Possible alternatives:

* Make a symlink in some `spkg-install`.
* Have Mercurial reconstitute the link.



---

archive/issue_comments_045435.json:
```json
{
    "body": "We really need to create a new ticket for this issue and continue there. I would also suggest taking this up on sage-devel.",
    "created_at": "2009-07-21T14:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45435",
    "user": "https://github.com/rlmill"
}
```

We really need to create a new ticket for this issue and continue there. I would also suggest taking this up on sage-devel.



---

archive/issue_comments_045436.json:
```json
{
    "body": "Replying to [comment:23 rlm]:\n> We really need to create a new ticket for this issue and continue there. I would also suggest taking this up on sage-devel.\nI've opened #6614.",
    "created_at": "2009-07-24T15:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5799#issuecomment-45436",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:23 rlm]:
> We really need to create a new ticket for this issue and continue there. I would also suggest taking this up on sage-devel.
I've opened #6614.
