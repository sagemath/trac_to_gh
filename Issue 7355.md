# Issue 7355: Allow sage -i/-f to install packages without stating version number.

archive/issues_007355.json:
```json
{
    "body": "Assignee: tbd\n\nHaving to state the version number of a package all the time is annoying. This fixes that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7355\n\n",
    "created_at": "2009-10-30T08:34:55Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "Allow sage -i/-f to install packages without stating version number.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7355",
    "user": "timdumol"
}
```
Assignee: tbd

Having to state the version number of a package all the time is annoying. This fixes that.

Issue created by migration from https://trac.sagemath.org/ticket/7355





---

archive/issue_comments_061603.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.patch) by timdumol created at 2009-10-30 08:36:25\n\nAdds `sage-latest-online-package` and changes `sage-spkg` to work without version number.",
    "created_at": "2009-10-30T08:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61603",
    "user": "timdumol"
}
```

Attachment [trac_7355-sage-i-no-version.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.patch) by timdumol created at 2009-10-30 08:36:25

Adds `sage-latest-online-package` and changes `sage-spkg` to work without version number.



---

archive/issue_comments_061604.json:
```json
{
    "body": "Apply patch to scripts repo.",
    "created_at": "2009-10-30T08:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61604",
    "user": "timdumol"
}
```

Apply patch to scripts repo.



---

archive/issue_comments_061605.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-30T08:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61605",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061606.json:
```json
{
    "body": "Right now this doesn't quite work: your sage-latest-online-version prints things with \".spkg\" on the end, and that confuses sage-spkg. One fix is to change the line\n\n```\nv = list(set([x.strip() for x in r if x.endswith('.spkg')]))\n```\n\nto\n\n```\nv = list(set([x.strip()[:-5] for x in r if x.endswith('.spkg')]))\n```\n\nto strip off the .spkg at the end.\n\nI'll work on a review this weekend, I hope.",
    "created_at": "2009-10-30T09:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61606",
    "user": "ddrake"
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

archive/issue_comments_061607.json:
```json
{
    "body": "Removed \".spkg\" suffix from return value of `sage-latest-online-version`",
    "created_at": "2009-10-30T10:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61607",
    "user": "timdumol"
}
```

Removed ".spkg" suffix from return value of `sage-latest-online-version`



---

archive/issue_comments_061608.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.2.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.2.patch) by timdumol created at 2009-11-03 21:34:08\n\nThe fix you stated is up. Thanks!",
    "created_at": "2009-11-03T21:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61608",
    "user": "timdumol"
}
```

Attachment [trac_7355-sage-i-no-version.2.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.2.patch) by timdumol created at 2009-11-03 21:34:08

The fix you stated is up. Thanks!



---

archive/issue_comments_061609.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-04T02:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61609",
    "user": "ddrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061610.json:
```json
{
    "body": "I'm looking at the proposed sage-latest-online-package script and have some comments.\n\nI don't really like the 'list.tmp' temporary file business. It's nice to check if the user has the permissions to upgrade, but I think doing so should be the job of whatever actually does the upgrade. The name of the script implies that it tells you the latest online package name, and I'd like to see it do *only* that.\n\nI see that urlretrieve always uses a temporary file automatically (which gets deleted automatically), so perhaps we could do the first part of spkg_list like so:\n\n```\nweb_url = \"%s/%s\"%(PKG_SERVER, url)\nfn = urllib.urlretrieve(web_url)[0]\nr = open(fn).read()\n[etc]\n```\n\n\nAlso, when you build the list of spkgs, why do list(set(..)), then sort the list? The listings are alphabetized anyway, and if we run into a duplicate, the script will exit on the first occurrence anyway. It looks like just this will be fine:\n\n```\nreturn [x.strip()[:-5] for x in r if x.endswith('.spkg')]\n```\n\ninstead of \n\n```\nv = list(set(...))\nv.sort\nreturn v\n```\n\n\nWith the above changes, the script seems to work fine. I'd like to know if anyone uses a nonstandard SAGE_SERVER so we can make sure the script still works for such cases.",
    "created_at": "2009-11-04T02:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61610",
    "user": "ddrake"
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

archive/issue_comments_061611.json:
```json
{
    "body": "Harald Schilly says that each subdirectory of packages has a \"list\" file; for example, http://sagemath.org/packages/standard/list which simplifies the script even more (presuming we can depend on the \"list\" file being present). Something like this should be okay:\n\n```\nfn, hdrs = urllib.urlretrieve(url + '/list')\nspkgs = open(fn).read().splitlines()\nif spkgs[0].endswith('.spkg'):\n    return spkgs\n```\n\nIf you get a 404, the first line will be some html and won't be a string ending in \".spkg\".",
    "created_at": "2009-11-04T07:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61611",
    "user": "ddrake"
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

archive/issue_comments_061612.json:
```json
{
    "body": "Another idea: use urllib2.urlopen (http://docs.python.org/library/urllib2.html#urllib2.urlopen) which throws an HTTPError when we don't find the list, and doesn't use any temporary files at all.\n\n```\ntry:\n  data = urllib2.urlopen(some_url)\nexcept HTTPError:\n  # can explicitly check for a 404 if we want\n  print \"couldn't find it\"\n  sys.exit(whatever)\nreturn data.read().splitlines()\n```\n",
    "created_at": "2009-11-04T07:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61612",
    "user": "ddrake"
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

archive/issue_comments_061613.json:
```json
{
    "body": "I agree with all of your comments. I actually just copied everything from `sage-update`, so I didn't inspect the code. I think that using the list file is also applicable to `sage-update`, so should we also update `sage-update`?",
    "created_at": "2009-11-04T10:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61613",
    "user": "timdumol"
}
```

I agree with all of your comments. I actually just copied everything from `sage-update`, so I didn't inspect the code. I think that using the list file is also applicable to `sage-update`, so should we also update `sage-update`?



---

archive/issue_comments_061614.json:
```json
{
    "body": "This new patch should address all the issues you pointed out. This also strips versions and matches exactly on the package name, instead of using `pkg_name in spkg`.",
    "created_at": "2009-11-04T11:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61614",
    "user": "timdumol"
}
```

This new patch should address all the issues you pointed out. This also strips versions and matches exactly on the package name, instead of using `pkg_name in spkg`.



---

archive/issue_comments_061615.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-04T11:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61615",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061616.json:
```json
{
    "body": "Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.",
    "created_at": "2009-11-04T11:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61616",
    "user": "timdumol"
}
```

Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.



---

archive/issue_comments_061617.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.3.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.3.patch) by ddrake created at 2009-11-12 02:21:30\n\nHrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.",
    "created_at": "2009-11-12T02:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61617",
    "user": "ddrake"
}
```

Attachment [trac_7355-sage-i-no-version.3.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.3.patch) by ddrake created at 2009-11-12 02:21:30

Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.



---

archive/issue_comments_061618.json:
```json
{
    "body": "Replying to [comment:9 ddrake]:\n> Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.\n\nSorry about that. I have posted the actual patch now.",
    "created_at": "2009-11-12T11:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61618",
    "user": "timdumol"
}
```

Replying to [comment:9 ddrake]:
> Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.

Sorry about that. I have posted the actual patch now.



---

archive/issue_comments_061619.json:
```json
{
    "body": "Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.",
    "created_at": "2009-11-12T11:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61619",
    "user": "timdumol"
}
```

Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.



---

archive/issue_comments_061620.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.4.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.4.patch) by ddrake created at 2009-11-13 01:26:42\n\nI have one more suggestion / question, and then I think this will be ready to go: in sage-latest-spkg, you have a couple of bare \"exit()\" statements...do you want sys.exit()? I see that \"exit(1)\" works in Python, but I've always used sys.exit(). I can't find any documentation for the use of exit(), although it seems to work. Any ideas?",
    "created_at": "2009-11-13T01:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61620",
    "user": "ddrake"
}
```

Attachment [trac_7355-sage-i-no-version.4.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.4.patch) by ddrake created at 2009-11-13 01:26:42

I have one more suggestion / question, and then I think this will be ready to go: in sage-latest-spkg, you have a couple of bare "exit()" statements...do you want sys.exit()? I see that "exit(1)" works in Python, but I've always used sys.exit(). I can't find any documentation for the use of exit(), although it seems to work. Any ideas?



---

archive/issue_comments_061621.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-13T01:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61621",
    "user": "ddrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061622.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.5.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.5.patch) by timdumol created at 2009-11-13 19:20:12\n\nReplaces `exit()` calls with `sys.exit()` calls.",
    "created_at": "2009-11-13T19:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61622",
    "user": "timdumol"
}
```

Attachment [trac_7355-sage-i-no-version.5.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.5.patch) by timdumol created at 2009-11-13 19:20:12

Replaces `exit()` calls with `sys.exit()` calls.



---

archive/issue_comments_061623.json:
```json
{
    "body": "I have no idea why `exit()` works. Here's the new patch.",
    "created_at": "2009-11-13T19:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61623",
    "user": "timdumol"
}
```

I have no idea why `exit()` works. Here's the new patch.



---

archive/issue_comments_061624.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-13T19:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61624",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061625.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-14T04:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61625",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061626.json:
```json
{
    "body": "You have to change the license from \n\n```\n \t6\t# License: GPLv2 \n```\n\nto \n\n```\n\n \t6\t# License: GPLv2+ = GPLv2 or any later version at the user's option\n```\n",
    "created_at": "2009-11-14T04:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61626",
    "user": "was"
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

archive/issue_comments_061627.json:
```json
{
    "body": "License changed.",
    "created_at": "2009-11-14T04:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61627",
    "user": "timdumol"
}
```

License changed.



---

archive/issue_comments_061628.json:
```json
{
    "body": "Attachment [trac_7355-sage-i-no-version.6.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.6.patch) by timdumol created at 2009-11-14 04:06:24\n\nDone.",
    "created_at": "2009-11-14T04:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61628",
    "user": "timdumol"
}
```

Attachment [trac_7355-sage-i-no-version.6.patch](tarball://root/attachments/some-uuid/ticket7355/trac_7355-sage-i-no-version.6.patch) by timdumol created at 2009-11-14 04:06:24

Done.



---

archive/issue_comments_061629.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-14T04:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61629",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061630.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-16T23:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61630",
    "user": "ddrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061631.json:
```json
{
    "body": "This now looks good. Positive review! Let's get this into 4.3.",
    "created_at": "2009-11-16T23:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61631",
    "user": "ddrake"
}
```

This now looks good. Positive review! Let's get this into 4.3.



---

archive/issue_comments_061632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T06:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61632",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_061633.json:
```json
{
    "body": "This introduced a bug as fixed at #7544.",
    "created_at": "2009-12-09T01:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7355#issuecomment-61633",
    "user": "mvngu"
}
```

This introduced a bug as fixed at #7544.
