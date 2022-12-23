# Issue 7692: update the sloane OEIS database to the latest version; it is a little out of date.

Issue created by migration from https://trac.sagemath.org/ticket/7692

Original creator: was

Original creation time: 2009-12-15 22:25:55

Assignee: tbd

The Sloane database hasn't been updated since 2005, so update it. 

   http://sagemath.org/packages/optional/database_sloane_oeis-2005-12.spkg


---

Comment by was created at 2009-12-18 01:10:55


```
Hi William,

I don't want to send a 10 MB attachment (the unzipped database file is now
about 31 MB instead of the former 20), so I've attached a bash script that
should automatically generate the spkg file for you.  As long as you have
wget installed and the database can be downloaded (it doesn't check for
failure) it should work just fine.

Let me know if you have any problems running the script or using the spkg
it generates and I'll get it fixed as quickly as possible.

Best,
Steven
```


(see attachment: update-sloane)


---

Attachment


---

Comment by was created at 2009-12-18 01:35:29

Here is a complete spkg up to the Sage standard for spkg's (hopefully):

http://sage.math.washington.edu/home/wstein/patches/database_sloane_oeis-2009-12.spkg


---

Comment by was created at 2009-12-18 01:35:29

Changing status from new to needs_review.


---

Comment by jsp created at 2009-12-18 18:31:03

Changing status from needs_review to needs_work.


---

Comment by jsp created at 2009-12-18 18:31:03

The package installed ok, but sloane.py needs work:



```
sage: SloaneEncyclopedia.load()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (48, 0))

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/jaap/.sage/temp/vrede.jaapspies.nl/14953/_home_jaap__sage_init_sage_0.py in <module>()

/home/jaap/downloads/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/databases/sloane.pyc in load(self)
    246                 seqnum = int(m.group('num'));
    247                 msg = m.group('body').strip();
--> 248                 self.__data__[seqnum] = [seqnum, None, ','+msg+',']
    249         verbose("Finished loading", tm)
    250         self.__loaded__ = True

IndexError: list assignment index out of range


```


First of all there are more sequence in the databas:



```
class SloaneEncyclopediaClass:
    """
    A local copy of the Sloane Online Encyclopedia of Integer Sequences
    that contains only the sequence numbers and the sequences
    themselves.
    """
    def __init__(self):
        """
        Initialize the database but do not load any of the data.
        """
        self.__file__ = "%s/data/sloane/sloane-oeis.bz2"%os.environ["SAGE_ROOT"]
        self.__arraysize__ = 114751 # maximum sequence number + 1
        self.__loaded__ = False


```



Jaap


---

Comment by was created at 2009-12-19 00:17:25


```
I completely forgot that the array size was hardcoded in SloaneEncyclopediaClass -- this is what caused the error, since now the number of entries is bigger than the array size. There's a bizarre new issue with numbering, though: most of the online sequences are sequentially numbered, but in the version I downloaded last night the sequential numbers end at A175062 and then there's a single sequence, A557274, after that. (To check the numbers in your database file, run "cut -d' ' -f1 sloane-oeis | head".)

The two best fixes I have in mind, other than getting Sloane to renumber that one extra sequence, are to replace SloaneEncyclopediaClass.__data__ with a hashtable whose keys are the indices and to let it be a huge array whose last index is 557274. The first might be slower, but the second one will require storing almost 400000 extra "None" entries in the __data__ array, and they'll have to be iterated through and ignored in the find() method.

If we stick to using an array instead of a hash table, then probably the right thing to do as far as the array size is to add a line to the update-sloane script: something like

cut -d' ' -f1 sloane-oeis | sort -r | head -1 | sed 's/A//' > sloane-maxseq

where sloane-oeis is the unzipped encyclopedia file, to write the maximal sequence number (in this case, 557274) to a file sloane-maxseq. Then the SloaneEncyclopediaClass.load() method could read this number (plus one) from the sloane-maxseq file into the variable self.__arraysize__ before it creates self.__data__, and continue as normal.

Which of these do you think is the best way to proceed?

Steven
```



---

Comment by was created at 2009-12-19 05:39:04

More readable version:

I completely forgot that the array size was hardcoded in SloaneEncyclopediaClass -- this is what caused the error, since now the number of entries is bigger than the array size. There's a bizarre new issue with numbering, though: most of the online sequences are sequentially numbered, but in the version I downloaded last night the sequential numbers end at A175062 and then there's a single sequence, A557274, after that. (To check the numbers in your database file, run "cut -d' ' -f1 sloane-oeis | head".)

The two best fixes I have in mind, other than getting Sloane to renumber that one extra sequence, are to replace SloaneEncyclopediaClass.__data__ with a hashtable whose keys are the indices and to let it be a huge array whose last index is 557274. The first might be slower, but the second one will require storing almost 400000 extra "None" entries in the __data__ array, and they'll have to be iterated through and ignored in the find() method.

If we stick to using an array instead of a hash table, then probably the right thing to do as far as the array size is to add a line to the update-sloane script: something like


```
cut -d' ' -f1 sloane-oeis | sort -r | head -1 | sed 's/A//' > sloane-maxseq
```


where sloane-oeis is the unzipped encyclopedia file, to write the maximal sequence number (in this case, 557274) to a file sloane-maxseq. Then the SloaneEncyclopediaClass.load() method could read this number (plus one) from the sloane-maxseq file into the variable self.__arraysize__ before it creates self.__data__, and continue as normal.

Which of these do you think is the best way to proceed?

Steven


---

Comment by jsp created at 2009-12-19 19:22:59

FWIW, I downloaded a snapshot of the OEIS: all sequences up to date 2009-12-19.

I made a bz2 file: [http://sage.math.washington.edu/home/jsp/cat25.bz2](http://sage.math.washington.edu/home/jsp/cat25.bz2)

43 MB, expanded this is 176 MB.

Nice to have around.

Jaap


---

Attachment

Patch to databases/sloane.py


---

Comment by ssivek created at 2009-12-21 22:02:13

Changing status from needs_work to needs_review.


---

Comment by ssivek created at 2009-12-21 22:02:13

I've added a patch which adds two new functions in SloaneEncyclopediaClass:

- SloaneEncyclopedia.install() will download the stripped.gz file from the OEIS website and install it. The user can specify an alternate URL and whether to overwrite an existing copy of the OEIS.

- SloaneEncyclopedia.install_from_gz() installs the encyclopedia from a local copy of stripped.gz; the user has to specify the filename and (optionally) whether to overwrite an existing copy.

This eliminates the need for a spkg as long as the user can get a copy of stripped.gz, so if we want to continue providing a spkg (assuming we even have permission: see http://www.research.att.com/~njas/sequences/Seis.html#SEARCH2) it should probably just contain stripped.gz and a spkg-install script which passes it to install_from_gz().

The patch should also fix the IndexError issue from the referee report, since now instead of hardcoding the size of the database and allocating an array of that size it just loads the database into a dictionary.


---

Comment by jsp created at 2009-12-22 16:49:48

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2009-12-22 16:49:48

Looks good to me.

Tested the new functions. Worked for me.

Remark: I think there is no problem in offering an optional spkg. Neil excludes distributing the full database.

Suggestion: maybe it is feasible to modify sloane.py to include the file names.gz.
That way sequence can have there proper name from the OEIS.

Cheers,

Jaap


---

Comment by jsp created at 2009-12-22 17:32:23

Two remarks:

[1] Maybe the name of the patch should be conform the standard: trac_7692.patch

[2] Output is in Python:


```
sage: SloaneEncyclopedia[111111]
 [1, 2, 0, 2, 6, 46, 338, 2926, 28146, 298526, 3454434, 43286526, 583835650, 8433987582L, 129941213186L, 2127349165822L, 36889047574274L, 675548628690430L, 13030733384956418L, 264111424634864638L]

```


I would like to see this in Sage.

Shall we open another ticket?

Cheers,

Jaap


---

Attachment

Identical patch, but with the right naming convention


---

Comment by ssivek created at 2009-12-22 18:21:09

Ticket #7749 is now open, and I expect to have a patch submitted in the next day or so.


---

Comment by mhansen created at 2010-01-03 21:22:07

Resolution: fixed
