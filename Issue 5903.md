# Issue 5903: Remove dist directories from Sage distribution

archive/issues_005903.json:
```json
{
    "body": "Assignee: @timabbott\n\nCC:  @nexttime\n\nThe dist/ directories currently shipped in various Sage .spkg's have resulted in confusion for people a few times.\n\nThese directories are no longer used (the Debian packaging for these things are now maintained in my own git repositories).  So, they should be deleted before anyone else gets confused.  The list of packages needing this treatment is as follows:\n\n\n```\ncddlib-094f\neclib-20080310.p7\nextcode-3.4.1\nflint-1.2.4.p1\nflintqs-20070817.p4\ngap-4.4.10.p11\ngenus2reduction-0.3.p5\ngfan-0.3.p4\ngivaro-3.2.13rc2\niml-1.0.1.p11\njmol-11.6.16.p0\nlcalc-20080205.p2\nlibfplll-2.1.6-20071129.p5\nlibm4ri-20090128\nlinbox-1.1.6\nntl-5.4.2.p6\npalp-1.1.p1\npolybori-0.5rc.p6\nrubiks-20070912.p8\nscipy_sandbox-20071020.p3\nsingular-3-0-4-4-20080711.p4\nsymmetrica-2.0.p2\nsympow-1.018.1.p6\ntachyon-0.98beta.p8\nzn_poly-0.9.p0\n```\n\n\nSince this is a huge list, we probably want to handle this issue by just deleting the dist/ directories the next time each of these .spkg files is updated.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5903\n\n",
    "created_at": "2009-04-26T06:03:37Z",
    "labels": [
        "component: debian-package"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.1",
    "title": "Remove dist directories from Sage distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5903",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

CC:  @nexttime

The dist/ directories currently shipped in various Sage .spkg's have resulted in confusion for people a few times.

These directories are no longer used (the Debian packaging for these things are now maintained in my own git repositories).  So, they should be deleted before anyone else gets confused.  The list of packages needing this treatment is as follows:


```
cddlib-094f
eclib-20080310.p7
extcode-3.4.1
flint-1.2.4.p1
flintqs-20070817.p4
gap-4.4.10.p11
genus2reduction-0.3.p5
gfan-0.3.p4
givaro-3.2.13rc2
iml-1.0.1.p11
jmol-11.6.16.p0
lcalc-20080205.p2
libfplll-2.1.6-20071129.p5
libm4ri-20090128
linbox-1.1.6
ntl-5.4.2.p6
palp-1.1.p1
polybori-0.5rc.p6
rubiks-20070912.p8
scipy_sandbox-20071020.p3
singular-3-0-4-4-20080711.p4
symmetrica-2.0.p2
sympow-1.018.1.p6
tachyon-0.98beta.p8
zn_poly-0.9.p0
```


Since this is a huge list, we probably want to handle this issue by just deleting the dist/ directories the next time each of these .spkg files is updated.

Issue created by migration from https://trac.sagemath.org/ticket/5903





---

archive/issue_comments_046568.json:
```json
{
    "body": "As part of #7005, I'll ask that the dist/ be removed from the Singular spkg.",
    "created_at": "2009-09-25T02:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46568",
    "user": "https://github.com/dandrake"
}
```

As part of #7005, I'll ask that the dist/ be removed from the Singular spkg.



---

archive/issue_comments_046569.json:
```json
{
    "body": "Ticket #7109 removes \"dist/\" from cddlib.",
    "created_at": "2010-01-25T13:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46569",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #7109 removes "dist/" from cddlib.



---

archive/issue_comments_046570.json:
```json
{
    "body": "Ticket #7820 removes \"dist/\" from gfan.",
    "created_at": "2010-01-25T13:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46570",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #7820 removes "dist/" from gfan.



---

archive/issue_comments_046571.json:
```json
{
    "body": "I've \"informed\" the Tachyon and the (three) Lcalc upgrade/update tickets...\n\nSome of the packages in the list have meanwhile been upgraded or updated; I'm not sure which of them actually removed the `dist/` directory. (I think I did in the M4RI and/or PolyBoRi spkgs.)",
    "created_at": "2010-09-03T23:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46571",
    "user": "https://github.com/nexttime"
}
```

I've "informed" the Tachyon and the (three) Lcalc upgrade/update tickets...

Some of the packages in the list have meanwhile been upgraded or updated; I'm not sure which of them actually removed the `dist/` directory. (I think I did in the M4RI and/or PolyBoRi spkgs.)



---

archive/issue_comments_046572.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> I've \"informed\" the Tachyon and the (three) Lcalc upgrade/update tickets...\n\nAnd that of genus2reduction (#9591).",
    "created_at": "2010-09-03T23:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46572",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:4 leif]:
> I've "informed" the Tachyon and the (three) Lcalc upgrade/update tickets...

And that of genus2reduction (#9591).



---

archive/issue_comments_046573.json:
```json
{
    "body": "Ticket #9562 removes `dist/` from libm4ri.",
    "created_at": "2010-10-18T09:14:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #9562 removes `dist/` from libm4ri.



---

archive/issue_comments_046574.json:
```json
{
    "body": "Ticket #5281 removes the dist directory from tachyon.",
    "created_at": "2011-01-11T09:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46574",
    "user": "https://github.com/vbraun"
}
```

Ticket #5281 removes the dist directory from tachyon.



---

archive/issue_comments_046575.json:
```json
{
    "body": "Code to identify packages with dist directory\n\n\n```/usr/bin/python\n\n# search spkgs for dist directory \n#\n# assumes you start in spkg/standard\n\nimport sys,os,subprocess\n\ncur = os.getcwd()\nprint cur\n\nfor filename in os.listdir(\".\"):\n  if filename.endswith(\".spkg\"):\n    val = subprocess.check_output([\"file\", filename])\n    if val.find(\"bzip2\") > -1:\n      basename=filename.rstrip(\".spkg\")\n      subprocess.check_output([\"cp\", filename,basename +\".tar.bz2\"])\n      subprocess.check_output([\"bunzip2\", basename + \".tar.bz2\"])\n    else: # fortran.spkg (only tar'ed) \n      basename=filename.rstrip(\".spkg\")\n      subprocess.check_output([\"cp\", filename,basename + \".tar\"])\n    subprocess.check_output([\"tar\", \"xf\", basename + \".tar\"])\n    if os.path.exists(cur + \"/\" + basename + \"/dist\") == True:\n      print filename\n```\n",
    "created_at": "2011-05-19T19:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Code to identify packages with dist directory


```/usr/bin/python

# search spkgs for dist directory 
#
# assumes you start in spkg/standard

import sys,os,subprocess

cur = os.getcwd()
print cur

for filename in os.listdir("."):
  if filename.endswith(".spkg"):
    val = subprocess.check_output(["file", filename])
    if val.find("bzip2") > -1:
      basename=filename.rstrip(".spkg")
      subprocess.check_output(["cp", filename,basename +".tar.bz2"])
      subprocess.check_output(["bunzip2", basename + ".tar.bz2"])
    else: # fortran.spkg (only tar'ed) 
      basename=filename.rstrip(".spkg")
      subprocess.check_output(["cp", filename,basename + ".tar"])
    subprocess.check_output(["tar", "xf", basename + ".tar"])
    if os.path.exists(cur + "/" + basename + "/dist") == True:
      print filename
```




---

archive/issue_comments_046576.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46576",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_046577.json:
```json
{
    "body": "Changing component from debian-package to packages.",
    "created_at": "2012-04-19T10:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46577",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from debian-package to packages.



---

archive/issue_comments_046578.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-01-07T12:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46578",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_046579.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-07T12:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46579",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_046580.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-01-07T14:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46580",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_046581.json:
```json
{
    "body": "Ok, this is indeed the last one where dist still exists. Good enough for me.",
    "created_at": "2014-01-07T17:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46581",
    "user": "https://github.com/fchapoton"
}
```

Ok, this is indeed the last one where dist still exists. Good enough for me.



---

archive/issue_comments_046582.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-07T17:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46582",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046583.json:
```json
{
    "body": "fill in the reviewer field...",
    "created_at": "2014-01-09T06:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46583",
    "user": "https://github.com/vbraun"
}
```

fill in the reviewer field...



---

archive/issue_comments_046584.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-10T07:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5903#issuecomment-46584",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
