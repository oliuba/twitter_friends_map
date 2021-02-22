# Twitter Friends Map

This program is created to build a map of a Twitter user's friends' locations.
As a result, there is an HTML-page with a __friends locations map__.
The program is created for entartainment and searching of movie locations.

This program opens a web page with *2 forms*:

- First form asks the user to enter his/her twitter account screenname.
- Second form asks the user to enter a bearer token - the unique Twitter code to get access to Twitter data.

After the user enters required information, there are two ways:

> If everything is right (the information is entered, the account exists and the bearer token is correct),
> the user is transferred to the web page with a map where are the locations of his/her friends.
>
> If something goes wrong, the user is transferred to a web page with the error message.

The program contains *3 modules* which serve for the problem solving.

- The first module is twitter_api_analysis. It works with Twitter API to get user's friends' locations.
- The second module is friends_map. It works with geopy and folium to transform location names in coordinates and build a map with them.
- The third module is main_twitter. It works with Flask to make a web app and combines other modules together.

All special libraries and downloads are mentioned in requirements.txt.

> To use the program, download all modules, directory templates and all special requirements and start main_twitter.py. 
> Then a web page will open and you will be asked to enter a Twitter account screenname and bearer token.
> Then you will be transferred to a web page with a map if everything is correct and
> to a web page with the error message if something goes wrong.

### An example of the program use

```sh
>>> python main_twitter.py
* Serving Flask app "main_twitter" (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### The first page.
<img width="960" alt="2021-02-22 (1)" src="https://user-images.githubusercontent.com/50978411/108753767-d025c580-754d-11eb-823f-0d69690f4bff.png">


### The second page if everything is right.
<img width="960" alt="2021-02-22 (2)" src="https://user-images.githubusercontent.com/50978411/108753840-e9c70d00-754d-11eb-824d-fe463380f424.png">


### The second page if something goes wrong.
<img width="960" alt="2021-02-22 (4)" src="https://user-images.githubusercontent.com/50978411/108753626-a8366200-754d-11eb-9794-99ed75dfd0e6.png">


#### Have fun using web map program!