# Issue 4511: sage-combinat script won't work with two digit version numbers (for example: 3.2)

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2008-11-13 10:45:09

Assignee: saliola

CC:  sage-combinat

Keywords: sage-combinat script

Change the version number in $SAGE_ROOT/local/bin/sage-banner to 3.2 and then watch 'sage -combinat config' fail.

I'll fix this right away.


---

Attachment

patch against version 3.2.rc0


---

Comment by saliola created at 2008-11-13 11:00:32

For the record: my previous patch to the script did not cause this---it would have failed anyway---but it did make me realize that this would be a problem!

Technical note: the get_sage_version function will now return the version number with any non-numeric stuff stripped off. For example "3.2.rc0" will be returned as "3.2".


---

Comment by nthiery created at 2008-11-13 13:42:47

Thanks!

I am not sure I have the latest sage-combinat script under hand.
Please double check that qselect_backward_compatibility_patches also
supports 2 digits version numbers, in particular in the version
guards.

Once you have done this, I'll give a positive review.

Cheers,
				Nicolas


---

Comment by saliola created at 2008-11-13 13:58:00


```
>> sage -version
>> sage -combinat qselect
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Skip backward compatibility patches for sage 3.1.2
Skip backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect
no active guards
```

| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
And here I've change the version number to 3.1 (by editing sage-banner):

```
>> sage -version
>> sage -combinat qselect
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Keep backward compatibility patches for sage 3.1.2
Keep backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect 3_1_2 3_1_3
```



---

Attachment

apply only this patch


---

Comment by saliola created at 2008-11-14 19:38:53

Whoever reviews this can apply it and test it with the following command (it creates a new branch so it won't mess up your combinat installation):

```
sage -combinat install --branch=temp_combinat
```


But, I checked it throughly and it is working correctly (note that in the above the output the 3.1 guard isn't selected, but below it is).

The docstring of qselect_backward_compatibility_patches:

```
    r"""
    Selects the appropriate guards for this version of sage
    e.g. if we are running sage 3.0.2, then we want to apply all
    the patches which are guarded by 3_0_3, 3_0_4, ...
    """
```


The current available guards are: 3_0_2, 3_0_3, 3_0_4, 3_0_6, 3_1, 3_1_2, 3_1_3. So for the current version 3.2, we should apply no patches, and that is what happens:

```
>> sage -combinat install
...
updating working directory
43 files updated, 0 files merged, 0 files removed, 0 files unresolved
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Skip backward compatibility patches for sage 3.1
Skip backward compatibility patches for sage 3.1.2
Skip backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect
no active guards
...
```


For version 3.1 (I only changed the version number in sage-banner), we want to apply all patches guarded by 3_1_2 and 3_1_3:

```
>> sage -combinat install
...
updating working directory
43 files updated, 0 files merged, 0 files removed, 0 files unresolved
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Skip backward compatibility patches for sage 3.0.6
Skip backward compatibility patches for sage 3.1
Keep backward compatibility patches for sage 3.1.2
Keep backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect 3_1_2 3_1_3
number of unguarded, unapplied patches has changed from 31 to 33
...
```



For version 3.0.6 (again, I only changed the version number in sage-banner), we want to apply all patches guarded by 3_0_6, 3_1, 3_1_2, 3_1_3.

```
>> sage -combinat install
...
updating working directory
43 files updated, 0 files merged, 0 files removed, 0 files unresolved
Active guards:
Skip backward compatibility patches for sage 3.0.2
Skip backward compatibility patches for sage 3.0.3
Skip backward compatibility patches for sage 3.0.4
Keep backward compatibility patches for sage 3.0.6
Keep backward compatibility patches for sage 3.1
Keep backward compatibility patches for sage 3.1.2
Keep backward compatibility patches for sage 3.1.3
Updating guards
  sage -hg qselect -q -n
  sage -hg qselect 3_0_6 3_1 3_1_2 3_1_3
number of unguarded, unapplied patches has changed from 31 to 36
...
```



---

Comment by mabshoff created at 2008-11-14 22:04:59


```
I'd like to give a positive review, but the wiki won't allow me to
access the trac guidelines (surge protection) to check how I am
supposed to do that. I'll try again tomorrow morning, unless someone
does this for me in the mean time.

In case you have 2 minutes, can you update the doc string line 203?

Cheers,
				Nicolas
```



---

Comment by mabshoff created at 2008-11-15 04:48:56

Merged sage-combinat-script-4511-patch2.patch in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-15 04:48:56

Resolution: fixed
