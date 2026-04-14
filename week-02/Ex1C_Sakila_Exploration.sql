/*
a) The actor's first and last name, as well as their id number are found here. Including their id numbers
b) In the columns for film you can find info on soecific films like name, release year, the length of the film, as well as ratings and special features
c) You can find the actor and film id in the column named film_actor
d) After analzying the rental columns in a seperate query, I've noticed that it's a little confusing to see who rented what movie. The table mostly includes info on staff and customers, like when a customer last rented a movie and whose staff id number gave said customer the film
e) In the inventory query, I can find info about what films are in stores, like how much of said film is in stock, or finding the store id
f) I believe to find the specific film and the last date it was rented, you would need to use the film and inventory tables. The film table contains the films id number, the title, and the last date it's info was updated. Plus the inventory table includes columns providing the film id, what store has said film, and it also contains the last dated it was updated so you can cross reference
*/

SELECT * FROM film;
SELECT * FROM inventory;