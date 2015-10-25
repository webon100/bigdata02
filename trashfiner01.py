if len(trashed_files) == 0 :
    print "No files trashed from current dir ('%s')" % os.path.realpath(os.curdir)
else :
    index=raw_input("What file to restore [0..%d]: " % (len(trashed_files)-1))
    if index == "*" :
        for tfile in trashed_files :
            try:
                tfile.restore()
            except IOError, e:
                import sys
                print >> sys.stderr, str(e)
                sys.exit(1)
    elif index == "" :
        print "Exiting"
    else :
        index = int(index)
        try:
            trashed_files[index].restore()
        except IOError, e:
            import sys
            print >> sys.stderr, str(e)
            sys.exit(1)