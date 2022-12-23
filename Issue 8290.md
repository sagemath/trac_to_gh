# Issue 8290: Support HDF5

Issue created by migration from https://trac.sagemath.org/ticket/8290

Original creator: magawake

Original creation time: 2010-02-17 01:16:46

Assignee: GeorgSWeber

Keywords: hdf5 h5py

We would like to have hdf5 support into sage. This will include the C/C++ bindings and also should have the Java bindings. 

TO obtain HDF5:
http://www.hdfgroup.org/HDF5/release/obtain5.html


---

Comment by was created at 2010-02-17 01:17:53

Here is a quick spkg that works if you have libhdf5 devel packages installed on your computer:

http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg

Install it with

```
sage -i http://sage.math.washington.edu/home/wstein/patches/h5py-1.2.1.spkg
```



---

Comment by magawake created at 2010-02-17 01:21:18

Thanks. Couple of requirements

* Have it completely independent therefore be shipped with SAGE
* Have all the C/C++ bindings includes into the SAGE tar ball


---

Comment by magawake created at 2010-02-17 01:21:38

Changing keywords from "hdf5 h5py" to "hdf5 h5py hdf5python".


---

Comment by was created at 2010-02-17 01:38:24

I also made an hdf5 library spkg, but the hdf5 version is evidently too new for h5py:

http://www.hdfgroup.org/ftp/HDF5/prev-releases/hdf5-1.8.0/src/hdf5-1.8.0.tar.gz

since compiling this, then h5py does not work.


---

Comment by was created at 2010-02-17 01:54:26

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

Comment by was created at 2010-02-17 01:54:26

Changing status from new to needs_review.


---

Comment by was created at 2010-02-17 01:55:00

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

Comment by magawake created at 2010-02-17 02:11:09

Is it possible to have atleast hdf 1.8.2? 1.6.x is too old. Most of our files are 1.8.x format.


---

Comment by jason created at 2010-02-18 15:23:54

pyTables might also be an option.  For comparison, see http://www.pytables.org/moin/FAQ#HowdoesPyTablescomparewiththeh5pyproject.3F and http://code.google.com/p/h5py/wiki/FAQ#What%27s_the_difference_between_h5py_and_PyTables_?


---

Comment by jason created at 2010-02-18 15:25:58

Also, on the front page of the h5py project, it says "Transparently supports both HDF5 1.6 and 1.8.".


---

Comment by jason created at 2010-02-18 15:27:38

On http://code.google.com/p/h5py/wiki/FAQ, it says that Linux supports up to 1.8.3.


---

Comment by jason created at 2010-02-18 15:28:30

On http://code.google.com/p/h5py/wiki/FAQ, it says that Linux supports up to 1.8.3.


---

Comment by aginiewicz created at 2010-03-20 10:30:19

actually h5py should support hdf5 up to 1.8.4 an PyTables up to 1.8.3. I'd say sage should use hdf5 1.8, it's first version to introduce external links and utf8 encoded strings so two things that seems to be quite important, right?


---

Comment by bascorp2 created at 2010-05-26 08:42:07

[pictures of puppies](http://pictures-search.com/)


---

Comment by aginiewicz created at 2010-11-08 19:05:49

I made quick update of those to hdf5 1.8, also this version of h5py works with hdf5 from spkg (at least it works for me - only had to specify "--hdf=$SAGE_LOCAL" to build script).

http://lab15.im.pwr.wroc.pl/~giniew/h5py-1.3.0.spkg

http://lab15.im.pwr.wroc.pl/~giniew/hdf5-1.8.4.spkg (actually, it's 1.8.4 patch 1, latest supported by h5py at time of writing - wasn't sure if I should add the patch1 to name here).

They are based on packages posted here earlier - just updated the src to pointed h5py to local hdf5 copy.


---

Comment by mhansen created at 2011-12-18 13:19:26

Changing status from needs_review to needs_info.


---

Comment by mhansen created at 2011-12-18 13:19:26

Ping.  These spkgs no longer exist.


---

Comment by aginiewicz created at 2011-12-18 13:30:48

Well, after a year I forgot about it - the files are present, but url changed. For now I don't have time to update them though (h5py is now 2.0.1 and hdf5 is 1.8.8). Anyway, working links:

http://im.pwr.wroc.pl/~giniew/h5py-1.3.0.spkg

and

http://im.pwr.wroc.pl/~giniew/hdf5-1.8.4.spkg


---

Comment by aginiewicz created at 2011-12-18 13:30:48

Changing status from needs_info to needs_review.


---

Comment by aginiewicz created at 2012-07-25 08:50:46

I've updated spkgs with latest versions. Also, those spkgs now contains repositories and better descriptions in SPKG.txt files (description, license, dependencies, changelog - usual stuff). I've also added links to description to not hunt for them in comments

 * https://github.com/downloads/aginiewicz/spkgs/hdf5-1.8.9.spkg
 * https://github.com/downloads/aginiewicz/spkgs/h5py-2.0.1.spkg


---

Comment by jdemeyer created at 2012-07-27 20:42:48

Please fill in your real name as Author.


---

Comment by jdemeyer created at 2012-08-13 12:35:07

Are these supposed to be standard packages, optional packages or experimental packages?


---

Comment by jdemeyer created at 2012-08-13 12:35:07

Changing component from build to packages.


---

Comment by jdemeyer created at 2012-08-13 12:35:07

Changing status from needs_review to needs_info.


---

Comment by aginiewicz created at 2012-08-25 13:26:12

In its current state (i.e. only hdf5+h5py) it might be not that useful to include in standard spkg. I believe it could be optional package. But if some other packages would be compiled with hdf5 support (especially R, which is standard package) situation might change. This is of course only my opinion and it might be not mirror others opinion.

Anyway, I got e-mail that h5py package got broken during upload to github. I had to recreate and reupload it (now, I will not trust github any more and keep other copy around) - it should work now.


---

Comment by mister.wardrop created at 2012-11-14 23:38:26

This would be really useful for making data interchangeable with other computing platforms. I look forward to seeing this included in Sage by default :).


---

Comment by jdemeyer created at 2014-11-13 14:05:42

Changing component from packages: standard to packages: optional.


---

Comment by mkoeppe created at 2020-06-19 18:16:00

Setting spkg proposals that have not seen recent activity to "sage-wishlist".
