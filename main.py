from parameters import args

__author__ = 'true'

print(args.url)
print(args.dir)
if args.subdirs:
    for subdir in args.subdirs:
        print(subdir)
