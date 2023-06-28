curl -X "DELETE" "http://localhost:27018/countries/unitedstates/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 16.1, \"lat\": -138, \"id\": \"unitedstates\"}" "http://localhost:27018/countries/"
curl -X "DELETE" "http://localhost:27018/countries/canada/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 48.748228, \"lat\": -135.7285136, \"id\": \"canada\"}" "http://localhost:27018/countries/"
curl -X "DELETE" "http://localhost:27018/countries/mexico/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 23.188985, \"lat\": -113.3087511, \"id\": \"mexico\"}" "http://localhost:27018/countries/"
curl -X "DELETE" "http://localhost:27018/cities/vancouver/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 49.2578182, \"lat\": -123.2063047, \"id\": \"vancouver\", \"country\": \"canada\"}" "http://localhost:27018/cities/"
curl -X "DELETE" "http://localhost:27018/cities/seattle/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 47.6131419, \"lat\": -122.5068728, \"id\": \"seattle\", \"country\": \"unitedstates\"}" "http://localhost:27018/cities/"
curl -X "DELETE" "http://localhost:27018/cities/atlanta/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 33.7675434, \"lat\": -84.5849418, \"id\": \"atlanta\", \"country\": \"unitedstates\"}" "http://localhost:27018/cities/"
curl -X "DELETE" "http://localhost:27018/cities/toronto/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 43.718371, \"lat\": -79.5428672, \"id\": \"toronto\", \"country\": \"canada\"}" "http://localhost:27018/cities/"
curl -X "DELETE" "http://localhost:27018/cities/guadalajara/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 20.6739329, \"lat\": -103.4178151, \"id\": \"guadalajara\", \"country\": \"mexico\"}" "http://localhost:27018/cities/"
curl -X "DELETE" "http://localhost:27018/cities/mexicocity/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 19.3909832, \"lat\": -99.3084259, \"id\": \"mexicocity\", \"country\": \"mexico\"}" "http://localhost:27018/cities/"
curl -X "DELETE" "http://localhost:27018/stadiums/akron/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 20.6739329, \"lat\": -103.4178151, \"id\": \"akron\", \"city\": \"guadalajara\", \"capacity\": 46355}" "http://localhost:27018/stadiums/"
curl -X "DELETE" "http://localhost:27018/stadiums/bcplace/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 49.2578182, \"lat\": -123.2063047, \"id\": \"bcplace\", \"city\": \"vancouver\", \"capacity\": 54500}" "http://localhost:27018/stadiums/"
curl -X "DELETE" "http://localhost:27018/stadiums/lumen/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 47.6131419, \"lat\": -122.5068728, \"id\": \"lumen\", \"city\": \"seattle\", \"capacity\": 68740}" "http://localhost:27018/stadiums/"
curl -X "DELETE" "http://localhost:27018/stadiums/mercbenz/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 33.7675434, \"lat\": -84.5849418, \"id\": \"mercbenz\", \"city\": \"atlanta\", \"capacity\": 71000}" "http://localhost:27018/stadiums/"
curl -X "DELETE" "http://localhost:27018/stadiums/bmofield/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 43.718371, \"lat\": -79.5428672, \"id\": \"bmofield\", \"city\": \"toronto\", \"capacity\": 30000}" "http://localhost:27018/stadiums/"
curl -X "DELETE" "http://localhost:27018/stadiums/azteca/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"lon\": 19.3909832, \"lat\": -99.3084259, \"id\": \"azteca\", \"city\": \"mexicocity\", \"capacity\": 83264}" "http://localhost:27018/stadiums/"
curl -X "DELETE" "http://localhost:27018/nations/scotland/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"rank\": 36, \"birth\": 1873, \"id\": \"scotland\"}" "http://localhost:27018/nations/"
curl -X "DELETE" "http://localhost:27018/nations/brazil/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"rank\": 1, \"birth\": 1930, \"id\": \"brazil\"}" "http://localhost:27018/nations/"
curl -X "DELETE" "http://localhost:27018/nations/england/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"rank\": 5, \"birth\": 1872, \"id\": \"england\"}" "http://localhost:27018/nations/"
curl -X "DELETE" "http://localhost:27018/clubs/livr/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"rank\": 5, \"birth\": 1892, \"id\": \"livr\"}" "http://localhost:27018/clubs/"
curl -X "DELETE" "http://localhost:27018/clubs/manc/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"rank\": 1, \"birth\": 1880, \"id\": \"manc\"}" "http://localhost:27018/clubs/"
curl -X "DELETE" "http://localhost:27018/clubs/nufc/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"rank\": 4, \"birth\": 1892, \"id\": \"nufc\"}" "http://localhost:27018/clubs/"
curl -X "DELETE" "http://localhost:27018/players/pope/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"birth\": \"1992-04-19\", \"number\": 22, \"id\": \"pope\", \"position\": \"keeper\", \"nation\": \"england\", \"club\": \"nufc\"}" "http://localhost:27018/players/"
curl -X "DELETE" "http://localhost:27018/players/walker/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"birth\": \"1990-05-28\", \"number\": 2, \"id\": \"walker\", \"position\": \"defender\", \"nation\": \"england\", \"club\": \"manc\"}" "http://localhost:27018/players/"
curl -X "DELETE" "http://localhost:27018/players/ederson/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"birth\": \"1993-08-17\", \"number\": 31, \"id\": \"ederson\", \"position\": \"keeper\", \"nation\": \"brazil\", \"club\": \"manc\"}" "http://localhost:27018/players/"
curl -X "DELETE" "http://localhost:27018/players/joelinton/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"birth\": \"1996-08-14\", \"number\": 7, \"id\": \"joelinton\", \"position\": \"midfield\", \"nation\": \"brazil\", \"club\": \"nufc\"}" "http://localhost:27018/players/"
curl -X "DELETE" "http://localhost:27018/players/robertson/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"birth\": \"1994-03-11\", \"number\": 26, \"id\": \"robertson\", \"position\": \"defender\", \"nation\": \"scotland\", \"club\": \"livr\"}" "http://localhost:27018/players/"
curl -X "DELETE" "http://localhost:27018/players/ramsay/"
curl -X "POST" -H "Content-Type: application/json" -d "{\"birth\": \"2003-07-31\", \"number\": 22, \"id\": \"ramsay\", \"position\": \"defender\", \"nation\": \"scotland\", \"club\": \"livr\"}" "http://localhost:27018/players/"
