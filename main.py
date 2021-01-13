"""
Down bellow is a prezentation of the Thunderstruck song by Ac/DC including the lyrics and some general data about the song

Lyrics
Thunder, thunder, thunder, thunder
I was caught
In the middle of a railroad track
I looked round
And I knew there was no turning back
My mind raced
And I thought what could I do
And I knew
There was no help, no help from you
Sound of the drums
Beating in my heart
The thunder of guns
Tore me apart
You've been
Thunderstruck
Rode down the highway
Broke the limit, we hit the town
Went through to Texas, yeah Texas, and we had some fun
We met some girls
Some dancers who gave a good time
Broke all the rules
Played all the fools
Yeah yeah they, they, they blew our minds
And I was shaking at the knees
Could I come again please
Yeah them ladies were too kind
You've been
Thunderstruck
I was shaking at the knees
Could I come again please
Thunderstruck, Thunderstruck, Thunderstruck, Thunderstruck
It's alright, we're doin' fine
It's alright, we're doin' fine, fine, fine
Thunderstruck, yeah, yeah, yeah
Thunderstruck, Thunderstruck
Thunderstruck, baby, baby
Thunderstruck, you've been Thunderstruck
Thunderstruck, Thunderstruck
You've been Thunderstruck
"""
"""
artist = " AC/DC"
title = "Thunderstruck"
genres = " Heavey Metal, Hard Rock"
y_released = 1990
writers = " Angus McKinnon and Malcom Mitchell Young"
#duration example taken from youtube expressed in decimals, 4 minutes and 53 secods
duration = 4.53
durationinseconds = 293

print("Artist:"+artist)
print("Title:"+title)
print("Genres:"+genres)
print("Year released:",y_released)
print("Song Writers:"+writers)
print("Duration:",duration," minutes or",durationinseconds," seconds")
"""

Artist={"Artist":"AC/DC",
	"Title":"Thunderstruck",
	"Genres":"Heavey Metal, Hard Rock",
	"Year released":1990,
	"Writers":"Angus McKinnon and Malcom Mitchell Young",
	"Duration":4.54,
	"Durationinseconds":293}

for  key,values in Artist.items():
	print(key,":",values)