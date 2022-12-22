# Issue 7019: update biopython optional package to 1.52

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-09-26 14:40:37

Assignee: tbd

CC:  tkeller

Keywords: biopython

Updating to biopython-1.52, which was released September 22, 2009.  Main improvements were to alignment and sequence file conversion, population genetics statistics, and the Bio.SeqIO.indexed_dict() for handling large numbers of sequences.

Here is an example that will not work with previous biopython packages:

```
sage: import urllib2 as U
sage: f = U.urlopen('http://biopython.org/DIST/docs/tutorial/examples/ls_orchid.gbk')
sage: orchidfile = file(DATA+"ls_orchid.gbk",'w')
sage: orchidfile.write(f.read())
sage: orchidfile.close()
sage: f.close()
sage: from Bio import SeqIO
sage: orchid_dict = SeqIO.index(DATA+"ls_orchid.gbk", "genbank")
sage: print 'Number of records: ' + str(len(orchid_dict))
sage: orchid_dict.keys()
sage: seq_record = orchid_dict["Z78475.1"]
sage: print 'Description: ' + seq_record.description
sage: seq_record.seq

Number of records: 94
Description: P.supardii 5.8S rRNA gene and ITS1 and ITS2 DNA.
Seq('CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGTTGAGATCACAT...GGT', IUPACAmbiguousDNA())
```



---

Comment by mhampton created at 2009-09-26 14:41:07

Changing assignee from tbd to mhampton.


---

Comment by awebb created at 2009-10-06 08:39:16

Where is the spkg? ~ Adam


---

Comment by mhampton created at 2009-10-06 21:37:58

Oops!  Sorry about that.  I put a copy here:

http://sage.math.washington.edu/home/mhampton/biopython-1.52.spkg

Thanks very much for taking a look!

Marshall


---

Comment by awebb created at 2009-10-07 07:05:18

Changing status from needs_review to needs_work.


---

Comment by awebb created at 2009-10-07 07:05:18

The program itself looks nice but the package does not seem to conform to the guidelines at http://www.sagemath.org/doc/developer/producing_spkgs.html. 

For example:
 * no hg repository
 * no src directory: there is a source directory and then a link to it. 
 * missing parts in the SPKG.txt (Description,License,Upstream Contact)
 * this package does have it's own test suite so a spkg-check would also be nice

Do you have time or should I work on it? 

Cheers,
Adam


---

Comment by awebb created at 2009-10-07 18:50:48

Some suggestions. ;-)

SPKG.txt

```
## Description

Biopython is a set of freely available tools for biological computation written in Python by an international team of developers.

It is a distributed collaborative effort to develop Python libraries and applications which address the needs of current and future work in bioinformatics.

## License

Biopython License

## SPKG Maintainers

  -- Marshall Hampton, mhampton at d.umn.edu or hamptonio at gmail.com.

## Upstream Contact

  -- wiki - http://biopython.org/wiki/Main_Page
```


spkg-check (keeping biopython as directory name)

```/usr/bin/env bash

if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi

cd biopython
python setup.py test

if [ $? -ne 0 ]; then
   echo "Error testing biopython"
   exit 1
fi
```


I hope this is useful,

Adam


---

Comment by mhampton created at 2009-10-08 02:35:38

Thanks, that's very useful.  The biopython optional package has existed for quite a while - William Stein added it for me in 2006 I think - and so it predates some of those good newer conventions.  

I don't have a lot of time for sprucing it up, so if you want to to take the lead on that please go ahead! 

The test suite is quite extensive, and I agree that it would be good to have a spkg-check for it.  I have experienced some funny issues running the tests, with some path-related failures unless I copied the tests into the sage directory structure.  Unfortunately I don't really understand what causes them.  If those path issues are cleared up then everything in the test suite should pass.

Realistically I won't have time to improve the spkg until mid-November at least.


---

Comment by awebb created at 2009-10-08 05:41:35

OK,

I'll see what I can do. ~ Adam


---

Comment by awebb created at 2009-10-08 13:24:32

Where do I put the spkg when I have it done? Is there an in-box or something? ~ Adam


---

Comment by mhampton created at 2009-10-08 23:51:50

Well, uploading it anywhere you have access to is fine.  If you don't have a good place to park it, you should ask for a sage.math account and put it there.  Just email William Stein, or ask on IRC.  I'm not sure, maybe Minh or someone else also has the ability to make sage.math accounts.

-Marshall


---

Comment by awebb created at 2009-10-11 09:31:50

Changing status from needs_work to needs_review.


---

Comment by awebb created at 2009-10-11 09:31:50

I put a new spkg at http://sage.math.washington.edu/home/awebb/biopython-1.52.p0.spkg. 

Adam


---

Comment by mhampton created at 2009-10-24 15:40:25

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2009-10-24 15:40:25

Looks good!  Thanks!
I'm a little confused on how to use the spkg-check script, but that's not your fault I think.  I will write to sage-devel about that.  I just haven't used such a script before.


---

Comment by was created at 2009-10-25 06:52:26

Resolution: fixed


---

Comment by was created at 2009-10-25 06:52:26

I posted it.
