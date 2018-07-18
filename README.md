This a Python implementation of a Pong-like game that was once available on
[DishTV](https://en.wikipedia.org/wiki/Dish_TV)'s Game Channel. The game was not like a regular Pong game. It had some additional mechanics such as:

 * The bats could rotate in plane about their geometric center. (So, angle
 of deflection depended not only on the angle at which the ball approached
 the bat, but also on the angle at which the bat was kept). This made the
 gameplay very interesting.

 * The collision with bat followed the Newtonian laws perfectly. So, if the
 bat was just rotating, but not translating, then the collision would still
 impart some additional velocity to the ball (depending where the ball hit
 the bat, the velocity imparted would be greater if the ball hit the bat
 at the edge, than at the center, as expected from Newtonian laws). This 
 actually made the game much more than _running-after-ball_ like pong is.
 
 * The balls kept slowing down (unless hit by a bat), but would never
 stop. (I suppose this was the because the speed of the ball decayed
 exponentially, so it would slow down indefinitely but never stop. Well,
 atleast, that's how I implemented it.)

 * The game had some additional blocks on the playing area. Some of these
 blocks would break on one collision with the bat, some took multiple
 collisions before breaking, while some didn't break at all. This also
 made the game more interesting as you could hit shots which would be
 unpredictable.

 * The goal of the game was also quite different from that of Pong. The two
 players would each have there own blocks (colored red and blue). The
 player with red blocks had to destroy all the blue colored blocks (using 
 the ball) after which a "goal-post" would open on the blue-end. The red
 player would then have to shoot the ball through this "goal-post" on the
 blue-end.

 * The game had some nice graphics as well. The playing area looked like
 ice; suggesting that this pong was being played on ice. I guess that would
 explain the exponential decay of speed.

#### I HAVE FORGOTTEN THE NAME OF THE GAME.

<small>I used to play it way back in 2006-07. I was 8-9yo. It was something
like "Ice-Pong"? "Snow-Pong"? "Ice-Ball"? I think it had "Ice" or "Snow" in
its name.</small>

#### IF YOU FIND OUT THE NAME OF THIS GAME, PLEASE LET ME KNOW.

### Running:

You must have python and pygame module to run this game.

Just run:

    python pong.py

Controls:
 
 * Hold "W" to move the bat up.
 * Hold "S" to move the bat down.
 * Hold "A" to rotate the bat anti-clockwise.
 * Hold "D" to rotate the bat clockwise.

TODO:

 * Implement ray-tracing for collision detection. (Present collision
 detection is fubar and won't detect collision if the ball is too fast).
 * Pls fix: When the ball is too fast, it goes out of the playing area and 
 gets stuck there.
