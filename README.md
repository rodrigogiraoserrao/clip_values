# `clip_values`

## Clipping values in a human-readable way

Clipping numerical values to make sure they are within a lower and upper bound is a very common task.

For example, if you are dealing with RGB colours, you want each channel to be between 0 and 255,
if you are dealing with shop sales, you need them to be between 0 and 1,
or if you are writing a cool game, you want your character to stay inside the screen.

Now, if you have to do all this clipping, which alternative to clipping do you prefer?

### Using `clip`

`clip` offers human-readable syntax to your clipping operations:

```py
colour_channel = clip(colour_channel).between_(0).and_(255)
discount = clip(discount).between_(0).and_(1)
player_x_pos = clip(player_x_pos).between_(0).and_(SCREEN_WIDTH)
```

The `clip` alternative is the simplest and easiest to read!
Compare it with two other common alternatives:

Using an `if: ... elif: ...` block is also easy to read, but takes up 4x more lines of code:

```py
if colour_channel < 0:
    colour_channel = 0
elif colour_channel > 255:
    colour_channel = 255
    
if discount < 0:
    discount = 0
elif discount > 1:
    discount = 1

if player_x_pos < 0:
    player_x_pos = 0
elif player_x_pos > SCREEN_WIDTH:
    player_x_pos = SCREEN_WIDTH
```

Chaining `min` with `max` (or the other way around) is shorter, but this is much harder to read
and you have to spend a couple of minutes figuring out the interaction between the two consecutive
calls to `min`/`max`:

```py
colour_channel = min(255, max(0, colour_channel))
discount = max(0, min(1, discount))
player_x_pos = min(SCREEN_WIDTH, max(0, player_x_pos))
```