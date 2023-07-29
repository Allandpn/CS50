--erro na consulta. falta fazer ordenacao do titulo


select movies.title, ratings.rating from movies join ratings on movies.id = ratings.movie_id where movies.year = 2010 order by ratings.rating, movies.title desc limit 50;