from parameters import args

__author__ = 'true'

print(args.url)
if args.subdirs:
    for subdir in args.subdirs:
        print(subdir)
