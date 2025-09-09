# Movie and Show Checher

# Usage

Adding a show:
```bash
python main.py add show -n "<Name of show>" -s <season number>  
```
Adding a Movie:
```bash
python main.py add movie -n "<Name of movie>" 
```

You can list all shows/movies:
```bash
python main.py list {show/movie}
```
or both:
```bash
python main.py list all
```

once adding you should sort them:
```bash
python main.py sort all
```

you can chech if a movie/show is in the list:
```bash
python main.py check {show/movie}
```