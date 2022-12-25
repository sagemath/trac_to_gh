# Issue 7355: Allow sage -i/-f to install packages without stating version number.

archive/issues_007355.json:
```json
{
    "body": "Assignee: tbd\n\nHaving to state the version number of a package all the time is annoying. This fixes that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7355\n\n",
    "created_at": "2009-10-30T08:34:55Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Allow sage -i/-f to install packages without stating version number.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7355",
    "user": "https://github.com/TimDumol"
}
```
Assignee: tbd

Having to state the version number of a package all the time is annoying. This fixes that.

Issue created by migration from https://trac.sagemath.org/ticket/7355





---

archive/issue_comments_061490.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.patch) by @TimDumol created at 2009-10-30 08:36:25\n\nAdds `sage-latest-online-package` and changes `sage-spkg` to work without version number.",
    "created_at": "2009-10-30T08:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61490",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7355-sage-i-no-version.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.patch) by @TimDumol created at 2009-10-30 08:36:25

Adds `sage-latest-online-package` and changes `sage-spkg` to work without version number.



---

archive/issue_comments_061491.json:
```json
{
    "body": "Apply patch to scripts repo.",
    "created_at": "2009-10-30T08:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61491",
    "user": "https://github.com/TimDumol"
}
```

Apply patch to scripts repo.



---

archive/issue_comments_061492.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-30T08:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61492",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061493.json:
```json
{
    "body": "Right now this doesn't quite work: your sage-latest-online-version prints things with \".spkg\" on the end, and that confuses sage-spkg. One fix is to change the line\n\n```\nv = list(set([x.strip() for x in r if x.endswith('.spkg')]))\n```\n\nto\n\n```\nv = list(set([x.strip()[:-5] for x in r if x.endswith('.spkg')]))\n```\n\nto strip off the .spkg at the end.\n\nI'll work on a review this weekend, I hope.",
    "created_at": "2009-10-30T09:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61493",
    "user": "https://github.com/dandrake"
}
```

Right now this doesn't quite work: your sage-latest-online-version prints things with ".spkg" on the end, and that confuses sage-spkg. One fix is to change the line

```
v = list(set([x.strip() for x in r if x.endswith('.spkg')]))
```

to

```
v = list(set([x.strip()[:-5] for x in r if x.endswith('.spkg')]))
```

to strip off the .spkg at the end.

I'll work on a review this weekend, I hope.



---

archive/issue_comments_061494.json:
```json
{
    "body": "Removed \".spkg\" suffix from return value of `sage-latest-online-version`",
    "created_at": "2009-10-30T10:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61494",
    "user": "https://github.com/TimDumol"
}
```

Removed ".spkg" suffix from return value of `sage-latest-online-version`



---

archive/issue_comments_061495.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.2.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.2.patch) by @TimDumol created at 2009-11-03 21:34:08\n\nThe fix you stated is up. Thanks!",
    "created_at": "2009-11-03T21:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61495",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7355-sage-i-no-version.2.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.2.patch) by @TimDumol created at 2009-11-03 21:34:08

The fix you stated is up. Thanks!



---

archive/issue_comments_061496.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-04T02:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61496",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061497.json:
```json
{
    "body": "I'm looking at the proposed sage-latest-online-package script and have some comments.\n\nI don't really like the 'list.tmp' temporary file business. It's nice to check if the user has the permissions to upgrade, but I think doing so should be the job of whatever actually does the upgrade. The name of the script implies that it tells you the latest online package name, and I'd like to see it do *only* that.\n\nI see that urlretrieve always uses a temporary file automatically (which gets deleted automatically), so perhaps we could do the first part of spkg_list like so:\n\n```\nweb_url = \"%s/%s\"%(PKG_SERVER, url)\nfn = urllib.urlretrieve(web_url)[0]\nr = open(fn).read()\n[etc]\n```\n\n\nAlso, when you build the list of spkgs, why do list(set(..)), then sort the list? The listings are alphabetized anyway, and if we run into a duplicate, the script will exit on the first occurrence anyway. It looks like just this will be fine:\n\n```\nreturn [x.strip()[:-5] for x in r if x.endswith('.spkg')]\n```\n\ninstead of \n\n```\nv = list(set(...))\nv.sort\nreturn v\n```\n\n\nWith the above changes, the script seems to work fine. I'd like to know if anyone uses a nonstandard SAGE_SERVER so we can make sure the script still works for such cases.",
    "created_at": "2009-11-04T02:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61497",
    "user": "https://github.com/dandrake"
}
```

I'm looking at the proposed sage-latest-online-package script and have some comments.

I don't really like the 'list.tmp' temporary file business. It's nice to check if the user has the permissions to upgrade, but I think doing so should be the job of whatever actually does the upgrade. The name of the script implies that it tells you the latest online package name, and I'd like to see it do *only* that.

I see that urlretrieve always uses a temporary file automatically (which gets deleted automatically), so perhaps we could do the first part of spkg_list like so:

```
web_url = "%s/%s"%(PKG_SERVER, url)
fn = urllib.urlretrieve(web_url)[0]
r = open(fn).read()
[etc]
```


Also, when you build the list of spkgs, why do list(set(..)), then sort the list? The listings are alphabetized anyway, and if we run into a duplicate, the script will exit on the first occurrence anyway. It looks like just this will be fine:

```
return [x.strip()[:-5] for x in r if x.endswith('.spkg')]
```

instead of 

```
v = list(set(...))
v.sort
return v
```


With the above changes, the script seems to work fine. I'd like to know if anyone uses a nonstandard SAGE_SERVER so we can make sure the script still works for such cases.



---

archive/issue_comments_061498.json:
```json
{
    "body": "Harald Schilly says that each subdirectory of packages has a \"list\" file; for example, http://sagemath.org/packages/standard/list which simplifies the script even more (presuming we can depend on the \"list\" file being present). Something like this should be okay:\n\n```\nfn, hdrs = urllib.urlretrieve(url + '/list')\nspkgs = open(fn).read().splitlines()\nif spkgs[0].endswith('.spkg'):\n    return spkgs\n```\n\nIf you get a 404, the first line will be some html and won't be a string ending in \".spkg\".",
    "created_at": "2009-11-04T07:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61498",
    "user": "https://github.com/dandrake"
}
```

Harald Schilly says that each subdirectory of packages has a "list" file; for example, http://sagemath.org/packages/standard/list which simplifies the script even more (presuming we can depend on the "list" file being present). Something like this should be okay:

```
fn, hdrs = urllib.urlretrieve(url + '/list')
spkgs = open(fn).read().splitlines()
if spkgs[0].endswith('.spkg'):
    return spkgs
```

If you get a 404, the first line will be some html and won't be a string ending in ".spkg".



---

archive/issue_comments_061499.json:
```json
{
    "body": "Another idea: use urllib2.urlopen (http://docs.python.org/library/urllib2.html#urllib2.urlopen) which throws an HTTPError when we don't find the list, and doesn't use any temporary files at all.\n\n```\ntry:\n  data = urllib2.urlopen(some_url)\nexcept HTTPError:\n  # can explicitly check for a 404 if we want\n  print \"couldn't find it\"\n  sys.exit(whatever)\nreturn data.read().splitlines()\n```\n",
    "created_at": "2009-11-04T07:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61499",
    "user": "https://github.com/dandrake"
}
```

Another idea: use urllib2.urlopen (http://docs.python.org/library/urllib2.html#urllib2.urlopen) which throws an HTTPError when we don't find the list, and doesn't use any temporary files at all.

```
try:
  data = urllib2.urlopen(some_url)
except HTTPError:
  # can explicitly check for a 404 if we want
  print "couldn't find it"
  sys.exit(whatever)
return data.read().splitlines()
```




---

archive/issue_comments_061500.json:
```json
{
    "body": "I agree with all of your comments. I actually just copied everything from `sage-update`, so I didn't inspect the code. I think that using the list file is also applicable to `sage-update`, so should we also update `sage-update`?",
    "created_at": "2009-11-04T10:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61500",
    "user": "https://github.com/TimDumol"
}
```

I agree with all of your comments. I actually just copied everything from `sage-update`, so I didn't inspect the code. I think that using the list file is also applicable to `sage-update`, so should we also update `sage-update`?



---

archive/issue_comments_061501.json:
```json
{
    "body": "This new patch should address all the issues you pointed out. This also strips versions and matches exactly on the package name, instead of using `pkg_name in spkg`.",
    "created_at": "2009-11-04T11:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61501",
    "user": "https://github.com/TimDumol"
}
```

This new patch should address all the issues you pointed out. This also strips versions and matches exactly on the package name, instead of using `pkg_name in spkg`.



---

archive/issue_comments_061502.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-04T11:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61502",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061503.json:
```json
{
    "body": "Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.",
    "created_at": "2009-11-04T11:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61503",
    "user": "https://github.com/TimDumol"
}
```

Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.



---

archive/issue_comments_061504.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.3.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.3.patch) by @dandrake created at 2009-11-12 02:21:30\n\nHrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.",
    "created_at": "2009-11-12T02:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61504",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_7355-sage-i-no-version.3.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.3.patch) by @dandrake created at 2009-11-12 02:21:30

Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.



---

archive/issue_comments_061505.json:
```json
{
    "body": "Replying to [comment:9 ddrake]:\n> Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.\n\nSorry about that. I have posted the actual patch now.",
    "created_at": "2009-11-12T11:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61505",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:9 ddrake]:
> Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.

Sorry about that. I have posted the actual patch now.



---

archive/issue_comments_061506.json:
```json
{
    "body": "Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.",
    "created_at": "2009-11-12T11:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61506",
    "user": "https://github.com/TimDumol"
}
```

Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.



---

archive/issue_comments_061507.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.4.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.4.patch) by @dandrake created at 2009-11-13 01:26:42\n\nI have one more suggestion / question, and then I think this will be ready to go: in sage-latest-spkg, you have a couple of bare \"exit()\" statements...do you want sys.exit()? I see that \"exit(1)\" works in Python, but I've always used sys.exit(). I can't find any documentation for the use of exit(), although it seems to work. Any ideas?",
    "created_at": "2009-11-13T01:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61507",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_7355-sage-i-no-version.4.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.4.patch) by @dandrake created at 2009-11-13 01:26:42

I have one more suggestion / question, and then I think this will be ready to go: in sage-latest-spkg, you have a couple of bare "exit()" statements...do you want sys.exit()? I see that "exit(1)" works in Python, but I've always used sys.exit(). I can't find any documentation for the use of exit(), although it seems to work. Any ideas?



---

archive/issue_comments_061508.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-13T01:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61508",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061509.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.5.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.5.patch) by @TimDumol created at 2009-11-13 19:20:12\n\nReplaces `exit()` calls with `sys.exit()` calls.",
    "created_at": "2009-11-13T19:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61509",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7355-sage-i-no-version.5.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.5.patch) by @TimDumol created at 2009-11-13 19:20:12

Replaces `exit()` calls with `sys.exit()` calls.



---

archive/issue_comments_061510.json:
```json
{
    "body": "I have no idea why `exit()` works. Here's the new patch.",
    "created_at": "2009-11-13T19:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61510",
    "user": "https://github.com/TimDumol"
}
```

I have no idea why `exit()` works. Here's the new patch.



---

archive/issue_comments_061511.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-13T19:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61511",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061512.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-14T04:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61512",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061513.json:
```json
{
    "body": "You have to change the license from \n\n```\n \t6\t# License: GPLv2 \n```\n\nto \n\n```\n\n \t6\t# License: GPLv2+ = GPLv2 or any later version at the user's option\n```\n",
    "created_at": "2009-11-14T04:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61513",
    "user": "https://github.com/williamstein"
}
```

You have to change the license from 

```
 	6	# License: GPLv2 
```

to 

```

 	6	# License: GPLv2+ = GPLv2 or any later version at the user's option
```




---

archive/issue_comments_061514.json:
```json
{
    "body": "License changed.",
    "created_at": "2009-11-14T04:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61514",
    "user": "https://github.com/TimDumol"
}
```

License changed.



---

archive/issue_comments_061515.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.6.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.6.patch) by @TimDumol created at 2009-11-14 04:06:24\n\nDone.",
    "created_at": "2009-11-14T04:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61515",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7355-sage-i-no-version.6.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.6.patch) by @TimDumol created at 2009-11-14 04:06:24

Done.



---

archive/issue_comments_061516.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-14T04:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61516",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061517.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-16T23:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61517",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061518.json:
```json
{
    "body": "This now looks good. Positive review! Let's get this into 4.3.",
    "created_at": "2009-11-16T23:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61518",
    "user": "https://github.com/dandrake"
}
```

This now looks good. Positive review! Let's get this into 4.3.



---

archive/issue_comments_061519.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T06:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61519",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007578.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-17T06:11:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7355#event-7578"
}
```



---

archive/issue_comments_061520.json:
```json
{
    "body": "This introduced a bug as fixed at #7544.",
    "created_at": "2009-12-09T01:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61520",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This introduced a bug as fixed at #7544.
