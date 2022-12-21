# Issue 7355: Allow sage -i/-f to install packages without stating version number.

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-30 08:34:55

Assignee: tbd

Having to state the version number of a package all the time is annoying. This fixes that.


---

Attachment

Adds `sage-latest-online-package` and changes `sage-spkg` to work without version number.


---

Comment by timdumol created at 2009-10-30 08:39:27

Apply patch to scripts repo.


---

Comment by timdumol created at 2009-10-30 08:39:27

Changing status from new to needs_review.


---

Comment by ddrake created at 2009-10-30 09:23:40

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

Comment by timdumol created at 2009-10-30 10:16:56

Removed ".spkg" suffix from return value of `sage-latest-online-version`


---

Attachment

The fix you stated is up. Thanks!


---

Comment by ddrake created at 2009-11-04 02:51:19

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2009-11-04 02:51:19

I'm looking at the proposed sage-latest-online-package script and have some comments.

I don't really like the 'list.tmp' temporary file business. It's nice to check if the user has the permissions to upgrade, but I think doing so should be the job of whatever actually does the upgrade. The name of the script implies that it tells you the latest online package name, and I'd like to see it do _only_ that.

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

Comment by ddrake created at 2009-11-04 07:36:33

Harald Schilly says that each subdirectory of packages has a "list" file; for example, http://sagemath.org/packages/standard/list which simplifies the script even more (presuming we can depend on the "list" file being present). Something like this should be okay:

```
fn, hdrs = urllib.urlretrieve(url + '/list')
spkgs = open(fn).read().splitlines()
if spkgs[0].endswith('.spkg'):
    return spkgs
```

If you get a 404, the first line will be some html and won't be a string ending in ".spkg".


---

Comment by ddrake created at 2009-11-04 07:45:30

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

Comment by timdumol created at 2009-11-04 10:45:41

I agree with all of your comments. I actually just copied everything from `sage-update`, so I didn't inspect the code. I think that using the list file is also applicable to `sage-update`, so should we also update `sage-update`?


---

Comment by timdumol created at 2009-11-04 11:07:49

This new patch should address all the issues you pointed out. This also strips versions and matches exactly on the package name, instead of using `pkg_name in spkg`.


---

Comment by timdumol created at 2009-11-04 11:07:49

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-11-04 11:56:01

Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.


---

Attachment

Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.


---

Comment by timdumol created at 2009-11-12 11:50:39

Replying to [comment:9 ddrake]:
> Hrm, I think attachment:rac_7355-sage-i-no-version.3.patch was supposed to be uploaded to another ticket -- I see a one-line patch to `sagenb/data/sage/html/worksheet/worksheet.html`.

Sorry about that. I have posted the actual patch now.


---

Comment by timdumol created at 2009-11-12 11:51:06

Added Dan Drake's suggestions. Also strips package versions and matches packages exactly.


---

Attachment

I have one more suggestion / question, and then I think this will be ready to go: in sage-latest-spkg, you have a couple of bare "exit()" statements...do you want sys.exit()? I see that "exit(1)" works in Python, but I've always used sys.exit(). I can't find any documentation for the use of exit(), although it seems to work. Any ideas?


---

Comment by ddrake created at 2009-11-13 01:26:42

Changing status from needs_review to needs_work.


---

Attachment

Replaces `exit()` calls with `sys.exit()` calls.


---

Comment by timdumol created at 2009-11-13 19:21:13

I have no idea why `exit()` works. Here's the new patch.


---

Comment by timdumol created at 2009-11-13 19:21:13

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-11-14 04:03:35

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-11-14 04:03:35

You have to change the license from 

```
 	6	# License: GPLv2 
```

to 

```

 	6	# License: GPLv2+ = GPLv2 or any later version at the user's option
```



---

Comment by timdumol created at 2009-11-14 04:06:08

License changed.


---

Attachment

Done.


---

Comment by timdumol created at 2009-11-14 04:06:24

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2009-11-16 23:29:38

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2009-11-16 23:29:38

This now looks good. Positive review! Let's get this into 4.3.


---

Comment by mhansen created at 2009-11-17 06:11:03

Resolution: fixed


---

Comment by mvngu created at 2009-12-09 01:08:36

This introduced a bug as fixed at #7544.
