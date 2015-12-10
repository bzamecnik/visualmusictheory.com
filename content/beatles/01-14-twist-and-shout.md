Title: The Beatles: Twist and shout
Date: 2015-11-29 16:02
Category: Song Dissection
Tags: The Beatles, Please Please Me
Summary: <div class="row">
	  <div class="col-md-4">
  		<img alt="Alarm clock with pitch classes" title="Alarm clock with pitch classes" width="200" align="left" src="http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/cover.png">
  	</div>
  	<div class="col-md-8">
    	<p>Let's start dissecting songs with <a href="https://en.wikipedia.org/wiki/Twist_and_Shout">Twist and Shout</a> by The Beatles from the album Please, Please Me.</p>
      <p>
      It is a quite simple rock'n'roll song, a nice one to start with. Although it's not complicated it doesn't mean it's boring or there's nothing to explore and learn about. Quite opposite. Even I was surprised what interesting things we can figure out from such a three-chord song.
      </p>
		</div>
	</div>

![](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/cover.png)

Let's start dissecting songs with <a href="https://en.wikipedia.org/wiki/Twist_and_Shout">Twist and Shout</a> by The Beatles from the album Please, Please Me.

It is a quite simple rock'n'roll song, a nice one to start with. Although it's not complicated it doesn't mean it's boring or there's nothing to explore and learn about. Quite opposite. Even I was surprised what interesting things we can figure out from such a three-chord song.

So at first let's listen to it and feel the atmosphere of Beatlemania. And as John Lennon joked to Queen Mum: "People in the cheaper seats, clap your hands. And the rest of you, just rattle your jewelry." :)

<iframe width="420" height="315" src="https://www.youtube.com/embed/iS0wuN_6wyw" frameborder="0" allowfullscreen></iframe>

[TOC]

## Big picture

Then let's look at the overall picture. We'll try to make sense of it through out the article.

![whole song - 1 step](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/all-1s.png)

Another view, a bit "reshuffled":

![whole song - 7 step](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/all-7s.png)

### About the picture

It was drawn from the hand-annotated [chords](http://isophonics.net/files/annotations/chordlab/The%20Beatles/01_-_Please_Please_Me/14_-_Twist_And_Shout.lab) by a software I wrote for this purpose. Actually those are screenshots from a interactive player.

The horizontal axis represents time (left to right) and the vertical axis represents pitch classes (from bottom upwards). See the [Tone circle](tone-circle.html) article for intro, if you are not familiar. Roughly speaking it is the "height" of tones.

Each block represents a [tone](http://www.visualmusictheory.com/sound-and-silence.html) that is playing within that time. All blocks in a each vertical slice are played at the same time. Multiple tones played together are called a *chord* by musicians.

Also note that these chord annotations represent what's being played only roughly and not capture all the nuances of singing (eg. that screaming in the middle...). On the other hand in most cases that's the right level of detail that we need to undestand the "strange chords" in various songs.

Let's ignore the labels and colors for now if you don't understand them. We'll get to them soon.

### What we can see from the picture?

The first-sight observations:

- there's a lot of repeating blocks
- after the middle and at the end there are chords played for quite long
- before the first long chord the repeating pattern is a bit different

Let's zoom a bit to the details. What patterns are actually repeating?

## Zoom into a repeating pattern

The three repetitions from the beginning:

![intro - 1 step](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/intro-1s.png)

For clarity they're separated by thick lines. The thin lines represent *beats*, ie. times when a human naturally stomps or claps to the base rhythm. The [beat annotations](http://isophonics.net/files/annotations/beat/The%20Beatles/01_-_Please_Please_Me/14_-_Twist_And_Shout.txt) for this song are also available (however, in this plot they're just hand-drawn for now).

Now we dig into a single instance of the repeating pattern.

### How the tones are distibuted in time?

There are 3 different chords:

- first is played for 2 beats
- second is played for 2 beats
- third is twice as long - played for 4 beats

In total there are 8 beats per one pattern.

### How the tones are distibuted in "height" (pitch class)?

Observations:

- there appear 7 unique tones out of 12
    - those are labeled at the sidebar as: 1, 2, 3, 4, 5, 6, 7
    - however, their position (number of steps from the bottom) is: 0, 2, 4, 5, 7, 9, 11
- each chord contains 3 tones
- the first and second chord share the tone with label 1
- the first and third chord share the tone with label 5
- the second and third chord do not share anything
- the third chord is the same as the second shifted by 2 steps up
- the second chord is the same as the first shifted by 5 steps up (and wrapped around)
- consequently, the third chord is the same as the first shifted by 7 steps up

### The three chords look similar

Since the pitch classes live in a circular space we can also plot the three different chords in a circle:

![I-IV-V](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/i-iv-v.png)

It can be seen much clearer the shape of the three chords is the same. They just differ by rotation. In other words are rotationally symmetric.

In fact when we take one such chord and rotate it by each of the 12 steps, ie. from 0 to 11, we get a family of 12 chords. We can then select one of them to represent that family. In this case we select the first chord as that representant. Someday, we'll learn how.

### How to name these chords?

In order to distinguish the chord in the family we should name them somehow.

In the representant chord the tone with the lowest label is 1. In the second chord (rotated by 5 steps clockwise) the corresponding tone has label 4. In the third chord (rotated by 7 steps clockwise) the corresponding tone has label 5. One way of labeling chords from this family is to take this lowest tone label and write it as a roman numeral:

- I
- IV
- V

That's exactly what's shown in the middle of each of the circles above.

## What about the unique tones?

We've noticed 7 unique tones. Why about to plot them?

![diatonic scale](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/diatonic-scale.png)

On the left we see a big "chord" made up of all those 7 unique tones present in chords I, IV, and V.

> "These are *tones* that go together well, my [Michelle](https://en.wikipedia.org/wiki/Michelle_(song))". :)

When we take the "other look", ie. walk the circle by steps of 7 instead of 1, we can see this bunch of random tones together make a nice compact group without any holes. Wonderful!

### A beauty just discovered

The set of 7 tones we just discover is the cornerstone of the western music. This lady is so imporant that musicians call it by various names: major scale or [diatonic scale](https://en.wikipedia.org/wiki/Diatonic_scale), diatonic set.

In this article we'll call it diatonic scale when we're interested in the order of tones and diatonic set when we just mean a bunch of unique tones without a particular order.

We'll explore how it behaves, how it relates to chords and melodies, why it is so special and how it can be useful in practice.

But, don't forget, in small steps.

### Another look at the whole song

When we zoom out and look again at the whole song with the step size 7 we can now see one nice thing about this song. Most of tones are *inside* the territory of the diatonic set, except for a single tone at the end that is *outside*.

Musicians call this kind of territory a *key*.

![whole song - 7 steps](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/all-7s.png)

7-step view on the first few repetitions:

![verse - 7 steps](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/intro-7s.png)

### Can we rotate the diatonic set?

We've seen that by rotating a single chord we can get a family of chords. We can do to same to the diatonic set.

Then we get 12 such "territories" - keys. But that's another story and we save it as a mystery for further exploration.

## Lines in the tones

When we look back close to the repeating pattern we can notice another interesting thing. The tones make up "lines"!

*7-step view* - downward lines

![intro - 7-step voice-leadings](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/intro-7s-voice-leadings.png)

### 7-step view - downward lines

In the 7-step view we can se diagonal lines going from top-left to bottom-right. They make a full circle in two periods (marked with grey lines).

However, when we look more carefully and trace down when the tones go just by single step at time we can see this picture:

![intro - 7-step voice-leadings](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/intro-7s-voice-leadings-more-precise.png)

There are two downward slopes, marked in red and blue, that go down by single steps in 7-step view. The red one goes from tone labelled as 7 to 1, the blue on from 5 to 4. The red one period take two I-IV-V chord periods, the blue one takes just one. Note that the lines are not aligned with the chord patterns, they have different [phase](https://en.wikipedia.org/wiki/Phase_(waves)), in this case exactly opposite.

It looks as the blue one continues by wrapping around the circle. But beware that there's just 6 not 7 steps between tones 4 and 7.

### 1-step view - upward lines

When we look at the few chords in the intro in the 1-step view we can notice upward lines.

![intro - 1-step voice-leadings](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/intro-1s-voice-leadings.png)

Their period is three chord periods, and their phase is the same as of the chords. Each pattern goes from tone labeled as 1 to 7. The tones do not increase by single steps - sometimes by 1, sometimes by 2. They increase smoothly within the diatonic scale.

Indeed, the tones that make up the line are: 1, 2, 3, 4, 5, 6, 7. Exactly the same as tones in the diatonic scale.

This leads to an idea how to resuffle the tones and make another view, when tones in a scale would increate by single steps and make a smooth line.

### Voice leadings

The lines we've just discovered is another very imporant concept that is used in vast amount of music.

Musicians call it *voice leading*. Imagine you have multiple people sining and each line corresponds to what a single person sings. When the voices (lines) vary smoothly by small steps rather than random big jumps the music has various qualities. It can be easier to sing and listen. Generally it makes the music more structured.

In the further songs to explore we will encounter a whole lotta lines like we've just seen here. And voice leading will help us understand the strange chords that we're about to demystify.

## Further things to notice in this song

### Dominant chord

As for the long segments with a single chord we can hear the chord is built up by progressively stacking tones:

- 7
- 7-11
- 7-11-2
- 7-11-2-5

This makes the chord called V7. It is the same as V we've already seen but has one more extra tone: 5.

When we subtract 7, ie. the base tone from the V7 chord we get relative tone positions:

- 0
- 0-4
- 0-4-7
- 0-4-7-11

The chord with tones {0, 4, 7} is just the representant of the family of chords we've seen. The 11 in the diatonic set has the position 7. That's where the 7 came into V7.

This chord is one of the most important chord and musicians call it *dominant*. Don't worry, we'll learn much about it in the further songs.

![stacked V7](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/bridge-v7.png)

At the end we have a similar chord called I9. We'll explore it later. Just note that one of the tones from this chord is outside the key.

![I9](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/end-i9.png)

## Different pattern of chord

A small thing to note is that before the stacked chord there a change in the chord pattern. Instead of I-IV-V we have a few repetitions of I-IV-V-IV-V.

![verse with different pattern](http://i.visualmusictheory.com/songs/beatles/01-14-twist-and-shout/verse-with-different-pattern-7s.png)

## What we learned

- two views on the tone circle - 1 vs. 7 steps
- three basic chords - I, IV, V
- set of 7 tones - diatonic scale
- inside and outside
- voice leading lines
- dominant chord

## Questions for future

- Given a family of chords that just differ by rotation how to choose one to <s>rule</s> represent them all?
- How do multiple keys look like?
- How deal with naming chords when there might be multiple chords?
- Can there be other types of "territories"?
- What about other types of chords?
- What about V7 and I9?
- What about the various labels, letters and colors?

## Where to go next?

The list of song by [The Beatles](beatles.html).
