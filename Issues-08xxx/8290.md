# Issue 8290: Support HDF5

archive/issues_008290.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nKeywords: hdf5 h5py hdf5python\n\nWe would like to have hdf5 support into sage. This will include the C/C++ bindings and also should have the Java bindings. \n\nTo obtain HDF5:\nhttp://www.hdfgroup.org/HDF5/release/obtain5.html\n\nCurrent version of spkg (install in order):\n* https://github.com/downloads/aginiewicz/spkgs/hdf5-1.8.9.spkg\n* https://github.com/downloads/aginiewicz/spkgs/h5py-2.0.1.spkg\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8290\n\n",
    "created_at": "2010-02-17T01:16:46Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Support HDF5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8290",
    "user": "https://trac.sagemath.org/admin/accounts/users/magawake"
}
```
Assignee: GeorgSWeber

Keywords: hdf5 h5py hdf5python

We would like to have hdf5 support into sage. This will include the C/C++ bindings and also should have the Java bindings. 

To obtain HDF5:
http://www.hdfgroup.org/HDF5/release/obtain5.html

Current version of spkg (install in order):
* https://github.com/downloads/aginiewicz/spkgs/hdf5-1.8.9.spkg
* https://github.com/downloads/aginiewicz/spkgs/h5py-2.0.1.spkg


Issue created by migration from https://trac.sagemath.org/ticket/8290





---

archive/issue_comments_073308.json:
```json
{
    "body": "Here is a quick spkg that works if you have libhdf5 devel packages installed on your computer:\n\nhttp://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg\n\nInstall it with\n\n```\nsage -i http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg\n```",
    "created_at": "2010-02-17T01:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73308",
    "user": "https://github.com/williamstein"
}
```

Here is a quick spkg that works if you have libhdf5 devel packages installed on your computer:

http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg

Install it with

```
sage -i http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg
```



---

archive/issue_comments_073309.json:
```json
{
    "body": "Thanks. Couple of requirements\n\n* Have it completely independent therefore be shipped with SAGE\n* Have all the C/C++ bindings includes into the SAGE tar ball",
    "created_at": "2010-02-17T01:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73309",
    "user": "https://trac.sagemath.org/admin/accounts/users/magawake"
}
```

Thanks. Couple of requirements

* Have it completely independent therefore be shipped with SAGE
* Have all the C/C++ bindings includes into the SAGE tar ball



---

archive/issue_comments_073310.json:
```json
{
    "body": "Changing keywords from \"hdf5 h5py\" to \"hdf5 h5py hdf5python\".",
    "created_at": "2010-02-17T01:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73310",
    "user": "https://trac.sagemath.org/admin/accounts/users/magawake"
}
```

Changing keywords from "hdf5 h5py" to "hdf5 h5py hdf5python".



---

archive/issue_comments_073311.json:
```json
{
    "body": "I also made an hdf5 library spkg, but the hdf5 version is evidently too new for h5py:\n\nhttp://www.hdfgroup.org/ftp/HDF5/prev-releases/hdf5-1.8.0/src/hdf5-1.8.0.tar.gz\n\nsince compiling this, then h5py does not work.",
    "created_at": "2010-02-17T01:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73311",
    "user": "https://github.com/williamstein"
}
```

I also made an hdf5 library spkg, but the hdf5 version is evidently too new for h5py:

http://www.hdfgroup.org/ftp/HDF5/prev-releases/hdf5-1.8.0/src/hdf5-1.8.0.tar.gz

since compiling this, then h5py does not work.



---

archive/issue_comments_073312.json:
```json
{
    "body": "Hi,\n\nSo if you build\n\n    http://sage.math.washington.edu/home/wstein/patches/hdf5-1.6.9.spkg\n\nand \n\n    http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg\n\nthen it should work.  Example, do:\n\n```\n   sage -f  http://sage.math.washington.edu/home/wstein/patches/hdf5-1.6.9.spkg  http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg\n```\n\nI'm posting this for inclusion in the *experimental* repo.",
    "created_at": "2010-02-17T01:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73312",
    "user": "https://github.com/williamstein"
}
```

Hi,

So if you build

    http://sage.math.washington.edu/home/wstein/patches/hdf5-1.6.9.spkg

and 

    http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg

then it should work.  Example, do:

```
   sage -f  http://sage.math.washington.edu/home/wstein/patches/hdf5-1.6.9.spkg  http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg
```

I'm posting this for inclusion in the *experimental* repo.



---

archive/issue_comments_073313.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-17T01:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73313",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073314.json:
```json
{
    "body": "Example:\n\n```\nHere's a trivial example showing how to create a new HDF5 file and store a 100 x 20 array of floats:\n\n>>> f = h5py.File(\"myfile.hdf5\", 'w')\n>>> f[\"MyDataset\"] = numpy.ones((100,20))\n\nAnd to get your data back:\n\n>>> dset = f[\"MyDataset\"]\n>>> subset = dset[20:80,:]\n```\nSee http://code.google.com/p/h5py/",
    "created_at": "2010-02-17T01:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73314",
    "user": "https://github.com/williamstein"
}
```

Example:

```
Here's a trivial example showing how to create a new HDF5 file and store a 100 x 20 array of floats:

>>> f = h5py.File("myfile.hdf5", 'w')
>>> f["MyDataset"] = numpy.ones((100,20))

And to get your data back:

>>> dset = f["MyDataset"]
>>> subset = dset[20:80,:]
```
See http://code.google.com/p/h5py/



---

archive/issue_comments_073315.json:
```json
{
    "body": "Is it possible to have atleast hdf 1.8.2? 1.6.x is too old. Most of our files are 1.8.x format.",
    "created_at": "2010-02-17T02:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73315",
    "user": "https://trac.sagemath.org/admin/accounts/users/magawake"
}
```

Is it possible to have atleast hdf 1.8.2? 1.6.x is too old. Most of our files are 1.8.x format.



---

archive/issue_comments_073316.json:
```json
{
    "body": "pyTables might also be an option.  For comparison, see http://www.pytables.org/moin/FAQ#HowdoesPyTablescomparewiththeh5pyproject.3F and http://code.google.com/p/h5py/wiki/FAQ#What%27s_the_difference_between_h5py_and_PyTables_?",
    "created_at": "2010-02-18T15:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73316",
    "user": "https://github.com/jasongrout"
}
```

pyTables might also be an option.  For comparison, see http://www.pytables.org/moin/FAQ#HowdoesPyTablescomparewiththeh5pyproject.3F and http://code.google.com/p/h5py/wiki/FAQ#What%27s_the_difference_between_h5py_and_PyTables_?



---

archive/issue_comments_073317.json:
```json
{
    "body": "Also, on the front page of the h5py project, it says \"Transparently supports both HDF5 1.6 and 1.8.\".",
    "created_at": "2010-02-18T15:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73317",
    "user": "https://github.com/jasongrout"
}
```

Also, on the front page of the h5py project, it says "Transparently supports both HDF5 1.6 and 1.8.".



---

archive/issue_comments_073318.json:
```json
{
    "body": "On http://code.google.com/p/h5py/wiki/FAQ, it says that Linux supports up to 1.8.3.",
    "created_at": "2010-02-18T15:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73318",
    "user": "https://github.com/jasongrout"
}
```

On http://code.google.com/p/h5py/wiki/FAQ, it says that Linux supports up to 1.8.3.



---

archive/issue_comments_073319.json:
```json
{
    "body": "On http://code.google.com/p/h5py/wiki/FAQ, it says that Linux supports up to 1.8.3.",
    "created_at": "2010-02-18T15:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73319",
    "user": "https://github.com/jasongrout"
}
```

On http://code.google.com/p/h5py/wiki/FAQ, it says that Linux supports up to 1.8.3.



---

archive/issue_comments_073320.json:
```json
{
    "body": "actually h5py should support hdf5 up to 1.8.4 an PyTables up to 1.8.3. I'd say sage should use hdf5 1.8, it's first version to introduce external links and utf8 encoded strings so two things that seems to be quite important, right?",
    "created_at": "2010-03-20T10:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73320",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

actually h5py should support hdf5 up to 1.8.4 an PyTables up to 1.8.3. I'd say sage should use hdf5 1.8, it's first version to introduce external links and utf8 encoded strings so two things that seems to be quite important, right?



---

archive/issue_comments_073321.json:
```json
{
    "body": "[pictures of puppies](http://pictures-search.com/)",
    "created_at": "2010-05-26T08:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73321",
    "user": "https://trac.sagemath.org/admin/accounts/users/bascorp2"
}
```

[pictures of puppies](http://pictures-search.com/)



---

archive/issue_comments_073322.json:
```json
{
    "body": "I made quick update of those to hdf5 1.8, also this version of h5py works with hdf5 from spkg (at least it works for me - only had to specify \"--hdf=$SAGE_LOCAL\" to build script).\n\nhttp://lab15.im.pwr.wroc.pl/~giniew/h5py-1.3.0.spkg\n\nhttp://lab15.im.pwr.wroc.pl/~giniew/hdf5-1.8.4.spkg (actually, it's 1.8.4 patch 1, latest supported by h5py at time of writing - wasn't sure if I should add the patch1 to name here).\n\nThey are based on packages posted here earlier - just updated the src to pointed h5py to local hdf5 copy.",
    "created_at": "2010-11-08T19:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73322",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

I made quick update of those to hdf5 1.8, also this version of h5py works with hdf5 from spkg (at least it works for me - only had to specify "--hdf=$SAGE_LOCAL" to build script).

http://lab15.im.pwr.wroc.pl/~giniew/h5py-1.3.0.spkg

http://lab15.im.pwr.wroc.pl/~giniew/hdf5-1.8.4.spkg (actually, it's 1.8.4 patch 1, latest supported by h5py at time of writing - wasn't sure if I should add the patch1 to name here).

They are based on packages posted here earlier - just updated the src to pointed h5py to local hdf5 copy.



---

archive/issue_comments_073323.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-12-18T13:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73323",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_073324.json:
```json
{
    "body": "Ping.  These spkgs no longer exist.",
    "created_at": "2011-12-18T13:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73324",
    "user": "https://github.com/mwhansen"
}
```

Ping.  These spkgs no longer exist.



---

archive/issue_comments_073325.json:
```json
{
    "body": "Well, after a year I forgot about it - the files are present, but url changed. For now I don't have time to update them though (h5py is now 2.0.1 and hdf5 is 1.8.8). Anyway, working links:\n\nhttp://im.pwr.wroc.pl/~giniew/h5py-1.3.0.spkg\n\nand\n\nhttp://im.pwr.wroc.pl/~giniew/hdf5-1.8.4.spkg",
    "created_at": "2011-12-18T13:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73325",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Well, after a year I forgot about it - the files are present, but url changed. For now I don't have time to update them though (h5py is now 2.0.1 and hdf5 is 1.8.8). Anyway, working links:

http://im.pwr.wroc.pl/~giniew/h5py-1.3.0.spkg

and

http://im.pwr.wroc.pl/~giniew/hdf5-1.8.4.spkg



---

archive/issue_comments_073326.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-12-18T13:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73326",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_073327.json:
```json
{
    "body": "I've updated spkgs with latest versions. Also, those spkgs now contains repositories and better descriptions in SPKG.txt files (description, license, dependencies, changelog - usual stuff). I've also added links to description to not hunt for them in comments\n\n* https://github.com/downloads/aginiewicz/spkgs/hdf5-1.8.9.spkg\n* https://github.com/downloads/aginiewicz/spkgs/h5py-2.0.1.spkg",
    "created_at": "2012-07-25T08:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73327",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

I've updated spkgs with latest versions. Also, those spkgs now contains repositories and better descriptions in SPKG.txt files (description, license, dependencies, changelog - usual stuff). I've also added links to description to not hunt for them in comments

* https://github.com/downloads/aginiewicz/spkgs/hdf5-1.8.9.spkg
* https://github.com/downloads/aginiewicz/spkgs/h5py-2.0.1.spkg



---

archive/issue_comments_073328.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73328",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_073329.json:
```json
{
    "body": "Are these supposed to be standard packages, optional packages or experimental packages?",
    "created_at": "2012-08-13T12:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73329",
    "user": "https://github.com/jdemeyer"
}
```

Are these supposed to be standard packages, optional packages or experimental packages?



---

archive/issue_comments_073330.json:
```json
{
    "body": "Changing component from build to packages.",
    "created_at": "2012-08-13T12:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73330",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to packages.



---

archive/issue_comments_073331.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-08-13T12:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73331",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_073332.json:
```json
{
    "body": "In its current state (i.e. only hdf5+h5py) it might be not that useful to include in standard spkg. I believe it could be optional package. But if some other packages would be compiled with hdf5 support (especially R, which is standard package) situation might change. This is of course only my opinion and it might be not mirror others opinion.\n\nAnyway, I got e-mail that h5py package got broken during upload to github. I had to recreate and reupload it (now, I will not trust github any more and keep other copy around) - it should work now.",
    "created_at": "2012-08-25T13:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73332",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

In its current state (i.e. only hdf5+h5py) it might be not that useful to include in standard spkg. I believe it could be optional package. But if some other packages would be compiled with hdf5 support (especially R, which is standard package) situation might change. This is of course only my opinion and it might be not mirror others opinion.

Anyway, I got e-mail that h5py package got broken during upload to github. I had to recreate and reupload it (now, I will not trust github any more and keep other copy around) - it should work now.



---

archive/issue_comments_073333.json:
```json
{
    "body": "This would be really useful for making data interchangeable with other computing platforms. I look forward to seeing this included in Sage by default :).",
    "created_at": "2012-11-14T23:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mister.wardrop"
}
```

This would be really useful for making data interchangeable with other computing platforms. I look forward to seeing this included in Sage by default :).



---

archive/issue_events_019840.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19840"
}
```



---

archive/issue_events_019841.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19841"
}
```



---

archive/issue_events_019842.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19842"
}
```



---

archive/issue_events_019843.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19843"
}
```



---

archive/issue_events_019844.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19844"
}
```



---

archive/issue_events_019845.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19845"
}
```



---

archive/issue_events_019846.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19846"
}
```



---

archive/issue_comments_073334.json:
```json
{
    "body": "Changing component from packages: standard to packages: optional.",
    "created_at": "2014-11-13T14:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73334",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from packages: standard to packages: optional.



---

archive/issue_events_019847.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-19T18:16:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19847"
}
```



---

archive/issue_events_019848.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-19T18:16:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8290#event-19848"
}
```



---

archive/issue_comments_073335.json:
```json
{
    "body": "Setting spkg proposals that have not seen recent activity to \"sage-wishlist\".",
    "created_at": "2020-06-19T18:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8290#issuecomment-73335",
    "user": "https://github.com/mkoeppe"
}
```

Setting spkg proposals that have not seen recent activity to "sage-wishlist".
