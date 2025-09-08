import sys
import argparse
from functions import *
# get arguments
parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["add", "sort", "list" , "check"], help="add or sort or list or check")
parser.add_argument("type", choices=["show", "movie", "all"], help="movie or show or all")
parser.add_argument("-n", "--name", help="name of show or movie")
parser.add_argument("-s", "--season", help="season number(only for add)")
args = parser.parse_args()

# main
if args.mode:
    if args.mode == "check":
        if not args.type:
            print("Missing Type")
            sys.exit(1)
        if not args.name:
            print("Missing Name")
            sys.exit(2)
    
        if args.type == "show":
            if Check(args.type, args.name):
                print("-Show found-")
                print(Check(args.type, args.name))
            else:
                print("--Show not found--")
        elif args.type == "movie":
            if Check(args.type, args.name):
                print("-Movie found-")
            else:
                print("--Movie not found--")
        
    if args.mode == "add":
        if not args.type:
            print("Missing Type")
            sys.exit(1)
        if args.type == "show":
            if not args.name or not args.season:
                print("Missing Name or Season Number")
                sys.exit(2)
            if Check(args.type, args.name, args.season):
                print("Show and show season already exists")
                sys.exit(3)
            addShow(args.name, args.season)
        elif args.type == "movie":
            if not args.name:
                print("Missing Name")
                sys.exit(2)
            if Check(args.type, args.name):
                print("Movie already exists")
                sys.exit(3)
            addMovie(args.name)
        
    elif args.mode == "sort":
        sortLists()
        
    elif args.mode == "list":
        ListAll(args.type)