import sys
# add show to file
def addShow(name, season):
    name = str(name)
    if season:
        season = str(season)
    else:
        season = "1"
    
    shows, _ = getLists()
    updated = []
    found = False
    
    for show in shows:
        if "(" in show and ")" in show:
            ShowName = show[:show.rfind("(")].strip()
            ShowSeasons = show[show.rfind("(") + 1:show.rfind(")")].split(",")
            ShowSeasons = [x.strip() for x in ShowSeasons]

            if ShowName.lower() == name.lower():
                if season not in ShowSeasons:
                    ShowSeasons.append(season)
                ShowSeasons = sorted(set(ShowSeasons), key=int)
                updated.append(f"{ShowName}({','.join(sorted(ShowSeasons))})")
                found = True
            else:
                updated.append(show.strip())
        else:
            updated.append(show.strip())
    if not found:
        updated.append(f"{name}({season})")
    
    with open("shows.txt", "w") as f:
        f.write("\n".join(updated) + "\n")

# add movie to file
def addMovie(name):
    with open("movies.txt", "a") as f:
        f.write(name + "\n")
    print(f"{name} added to movies.txt")

# list all shows or movies
def ListAll(ListType):
    shows, movies = getLists()
    # prints the lists one name after another
    if ListType == "show":
        print("Shows:")
        for show in shows:
            print(show)
    elif ListType == "movie":
        print("Movies:")
        for movie in movies:
            print(movie)
    elif ListType == "all":
        print("Shows:")
        for show in shows:
            print(show)
        print("------------------------------------------\n")
        print("Movies:")
        for movie in movies:
            print(movie)

# sort shows and movies files
def sortLists():
    shows, movies = getLists()

    sorted_shows = []
    for show in shows:
        if "(" in show and ")" in show:
            show_name = show[:show.rfind("(")].strip()
            seasons = show[show.rfind("(")+1:show.rfind(")")].split(",")
            seasons = sorted(set(s.strip() for s in seasons), key=int)
            sorted_shows.append(f"{show_name}({','.join(seasons)})")
        else:
            sorted_shows.append(show.strip())

    # alphabetize both lists
    sorted_shows = sorted(sorted_shows, key=lambda x: x.lower())
    sorted_movies = sorted(set(m.strip() for m in movies), key=lambda x: x.lower())
    
    with open("shows.txt", "w") as f:
        f.write("\n".join(sorted_shows) + "\n")

    with open("movies.txt", "w") as f:
        f.write("\n".join(sorted_movies) + "\n")

    print("Files sorted and cleaned.")

# get show and movie lists
def getLists():
    try:
        with open("shows.txt") as f:
            shows = f.read().splitlines()
        with open("movies.txt") as f:
            movies = f.read().splitlines()
    except:
        print("File(s) not found")
        sys.exit(0)
    return shows, movies

# check if show or movie exists
def Check(nameType, name, season=None):
    shows, movies = getLists()
    
    # checks if season number is given. if it is get show and season if no show and season return false
    if season is not None:
        season = str(season)
        for show in shows:
            if "(" in show and ")" in show:
                ShowName = show[:show.rfind("(")].strip()
                ShowSeasons = show[show.rfind("(") + 1:show.rfind(")")].split(",")
                ShowSeasons = [x.strip() for x in ShowSeasons]
                
                if ShowName.lower() == name.lower() and season in ShowSeasons:
                    return True
        return False
    
    if nameType == "show":
        for show in shows:
            if "(" in show and ")" in show:
                ShowName = show[:show.rfind("(")].strip()
                ShowSeasons = show[show.rfind("(") + 1:show.rfind(")")].split(",")
                ShowSeasons = [x.strip() for x in ShowSeasons]
                
                if ShowName.lower() == name.lower():
                    output = f"\nShow: {ShowName}\nSeasons: {ShowSeasons}\n"
                    return output
        return False

    elif nameType == "movie":
        for movie in movies:
            if movie.lower() == name.lower():
                return True
        return False