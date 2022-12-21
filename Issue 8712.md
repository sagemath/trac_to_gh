# Issue 8712: Use `optparse` in sage -merge for increased usability.

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2010-04-18 08:52:59

Assignee: GeorgSWeber

Using `optparse` will, at the very least, show a proper usage message, which displays all the options.


---

Comment by timdumol created at 2010-04-18 12:15:42

Makes sage-apply-ticket use `optparse` instead of `getopt`.


---

Comment by timdumol created at 2010-04-18 12:16:53

Changing status from new to needs_review.


---

Attachment

This patch makes `sage-apply-ticket` use `optparse` instead of `getopt`, making things more robust, and adding a help/usage message, which displays all options and normal usage cases.


---

Attachment

Fixes at typo. Apply this patch only.


---

Comment by timdumol created at 2010-04-18 13:00:29

The help message reads:


```
Usage: sage -merge [options] [ticket-number]

Tries to automate the process of merging tickets in release management.
See http://wiki.sagemath.org/devel/ReleaseManagement for more info.

Example usage:

sage -merge -c or sage -merge --candidates

    * List all candidates for merging, i.e. all trac tickets with positive review. 

sage -merge <ticket_number> <options>

    * Download patches from trac for the given ticket number, merge them, run tests, and report the results. 

sage -merge -a <options> or sage -merge --all <options>

    * For each ticket on trac with a positive review, download the patches, apply them, and run doctests. At the end, report which tickets passed, which failed, and which didn't have any files to doctest (as is commonly the case with tickets for new spkg's). 


Options:
  -h, --help            show this help message and exit
  -a, --all             For each ticket on trac with a positive review,
                        download, apply, and test each. At the end, report
                        which pass, fail, and have no files to doctest
  -c, --candidates      List all candidates for merging, i.e., all trac
                        tickets with positive review
  -v, --verbose         Display the results of each test
  -n NUM_THREADS, --num-threads=NUM_THREADS
                        Number of threads to work with
  -r REPOSITORY, --repository=REPOSITORY
                        Which repository to apply to. Choices: ['bin',
                        'extcode', 'sage', 'examples', 'scripts', 'main']
  -t TEST, --test=TEST  What things to doctest. Choices: ['none', 'files',
                        'directory', 'long'] or any prefix of a choice.
  -o, --overwrite       Whether to overwrite files when downloading.
  -d DIRECTORY, --directory=DIRECTORY
                        Directory to store patches in.

  Behavior:
    Behavior after merging. Default is to pop after merging

    -l, --leave-in-queue
                        Leaves the patches in mercurial queue. Conflicts with
                        --finish.
    -f, --finish        Performs qfinish, commiting the patches. Conflicts
                        with --leave-in-queue.
```



---

Comment by jhpalmieri created at 2010-06-22 05:07:09

Looks pretty good. I found two small bugs (num_threads wasn't being passed correctly at one point, and the download directory wasn't dealt with right), and I think that the default values (e.g., the number of threads) should be in the help message.  I also think we can add a little statement saying that doctests were skipped if that is the case.  I'm attaching a reviewer patch implementing all of this.  If you're happy with it, I'm happy with the rest, so it can get a positive review.


---

Attachment

apply on top of trac_8712-sage-merge-optparse.2.patch


---

Comment by timdumol created at 2010-06-23 08:24:46

Nice catches! I'm fine with your changes.


---

Comment by jhpalmieri created at 2010-06-23 15:12:47

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:41:33

Resolution: fixed


---

Comment by rlm created at 2010-06-25 15:41:33

Merged:

    trac_8712-sage-merge-optparse.2.patch
    trac_8712-reviewer.patch
