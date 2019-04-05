"""
To Run:
python3 -m gibberish

Functions for geting information about gibberish input.
"""

import re
from collections import Counter


def most_common(lines, amount=1):
    words = []
    for line in lines:
        words += line.split(' ')

    ctr = Counter(words)
    most_common = ctr.most_common(amount)
    most_common_vals = [x[0] for x in most_common]
    return most_common_vals


def find_longest_line_length(lines):
    return max([len(line) for line in lines])


def find_longest_line_indices(lines, max_line_length):
    return [
        idx for idx, line in enumerate(lines)
        if len(line) == max_line_length
    ]


def most_unique_chars(lines):
    pattern = re.compile(r'\s+')

    sets = [
        set(re.sub(pattern, '', line)) for line in lines
    ]

    max_set_length = max([len(s) for s in sets])

    return [
        idx for idx, line in enumerate(sets)
        if len(line) == max_set_length
    ]


def main():
    lines = gibberish.splitlines()

    # Find most common word
    assert(most_common(lines) == ['people'])
    # Find ten most common words
    assert(
        most_common(lines, 10) == [
            'people',
            'who',
            'at',
            'call',
            'him',
            'were',
            'an',
            'one',
            'other',
            'most'
        ]
    )

    # Find index/indices of line(s) that is/are the longest
    max_line_length = find_longest_line_length(lines)
    assert(max_line_length == 221)

    line_indices = find_longest_line_indices(lines, max_line_length)
    assert(line_indices == [76])

    assert(len(lines[line_indices[0]]) == max_line_length)

    # Find which line number(s) has the most unique characters in it
    unique_line_indices = most_unique_chars(lines)
    assert(len(unique_line_indices) == 2)
    assert(unique_line_indices == [28, 79])

    set_one = set(lines[unique_line_indices[0]])
    set_two = set(lines[unique_line_indices[1]])
    assert(set_one == set_two)

    print('All tests passed.')


if __name__ == '__main__':
    # We call main below, after gibberish variable
    gibberish = """
may out come come at your him when be down like people and from which is now have were at that one but would by other the other
time with then hot would and
know of was day a see down people see may your people other first with who no most was then of him the it one my other
time about one about so word use said first many who way which the each call be in there were people and call her than them number can out all has were have
who than out would or at can we know
sound see may use have was but are you then other about be her at had has way we if long call many one has day be sound an could
have we may so day her at an number her the it
out who she or other at use at most said by first
what call a thing each how a a we who them were them at as other people do hot who number some down been there
so there this it from or there
they may that write your use were people by to call people had their he you no when so who have the and thing call
an were if people like one day for as them have thing out had find a like a more one it like two her in hot said hot number for them been than one the been
know call up has at all most was water she use but call do did people call but can then your first there an them there
now you one some are by could their and been them is so were for about
him so this their time him other come write a if people about his do more
he number I time were this like a more their my their and are come she your some by down your know like people most may make did two
them him him a do come have an your there was their how so will and and thing thing may my
an write said one were that so
be an down and with word who than with been has time first my all so like we his an from
other may an her can find so be you who who write of one did my said other or was was may number as at like more number as been one many
many down so many do more that the may she we were did
were day your most is each an from who than how you at or each can day an people find at them most who hot him of my is two find which at then write so his than write
a her be and will number people that so see hot down had is their make have can about know has at this their day write which then look
time than who call has have were by so some has he day many no your write will down has if
his than at like first one one most sound other from was been no than do he in we call who most with use have at her each some
you if out all what all
way of most call will or now were long long your be down is each one hot sound other it be people down or her it him up call what who do out like
this one be may she has an many many side so have of at said all number come it may their then there like people these down thing sound a these like
that most them you then each one to other write we but has more him that do way has than were your two so way other be they it it most were is than one or be down
he him first so people have these thing
an people make water has their
she said to time use with was said
a been were were in your of and can sound an of as two two
has other other did there him many other it was water said find other this other
out would the more up your each said she out said there do write have do then of their have
there sound some each and what would
what at hot may it an is time are
would from long out the hot it she hot would she a some she about that like out they did is first thing an the all like people them there how people
other is your find were be a his some about so a first have with their her
but so hot than over is with thing the sound other has a at is his were she call write thing it hot now way come and it he of call
this find two this now
people as they her it many is one who she about or your for do in a her in their
from they about hot said on was that is will look come may I for an people more way with all him were a many him him as can there use he were do see about there call then down
people these than now one long call of did it call them with a sound on who it no use people
day most an him some a one the other she
of the her you is she him down hot was is at you the by as of other sound but see him and may on him were
people find be number do down so many one him hot most down the
may other she call day have you most has people were she an what can him has people most has we see down call down
a them at have most
has we their they the than see their in use were his with his then was have who at more then up then for
each down your have call
them him if the has side him number most find hot said if with each had no out it the people people first is all your people this
but two his would has they one thing come may what if are your this out did
did thing was by who said write
of do her is he were who this to number most time water his or to many know them it
long her I sound call all
what about down him come day may number or one have at at first who it is people about at an is been are
number may see it many was people these who are said if that her about out up come other down call it most these in may no no call call at who a over said no or has did it call number then thing out an are she
go way for sound two a did people do were it sound the out we call said water it most them time but she or said day write her
water in be him there like than two first with more thing the a and their day there the his who
have most were their she for other
find about an will from about him that had at has first use would and for were so would be for who other an you call
so do your in at most write be they out them if their people people most thing all or may a write most or side
know be or than he they
them are about about then this sound down had people hot out come for is were was it many they but two you find what if come have can at were
two him they an her two would be people hot were way people like thing at other for two
who two was long your you find him write people some so an was time would
an was is so no call all who sound use there we is the have this two with long two an was him call other more has in in her
no call are many by one two up your most have their sound for then
no more know and long at way day use thing most who if what all people have
know in down was know time way been who
come like her for an your that the of two how she this
time was as number and call can first is what many who it number them would now some other time write what thing it be the has who day his by so what there
this time people have their so the this about
sound one than sound all number most by he that over she so all could
sound water would water people or many from would than each sound of people who what see number was up at has there the from be is their can at who some was their water day with word have call had I said them with and you
like as this her people may were one two him
down you my his has find one has day by call is one hot it have come from do for many them at is thing would each water down two may are with find were way who then people
thing most an who was number have write day thing your first with him this her they a go number with number we about then call about people use like be him call your like if of than number
up it other their have no hot
at his him if make hot there than we than down of she write the other and
them an from day if we first down they side many my hot a the your the how
has so two then may have than been the your her them now
so them call than no there
make may have each more then go from for an so
then them you she be see way
then then but it up hot about one one some
his there sound most that we them one call thing at that is they all has are a water we we their use hot him come sound day long be two
or him you use all a know her day so out do was with some like then day time her a first most who his are time most two this an have about about it would you
and most this an who write
were most at she about many of were do said sound him
first one with be so this so her it two what one this than them like at other number can number be two was sound these may and for and of most would like were in your with first my but of to their sound
out so people would the will his did up your but one with there time than there some number make
he thing who she she him be other what find with his an or people your her number or two there this water
about she they than would
who a was my said an one she your him would come go use but some now there
has it your we with to this come hot people many did find would can what down him which at she more down these and an sound do out people many do each her said about hot his sound some was they up by make out many
I for than people than she is what over use some hot will said
were use from be be a who
may that is up more sound to by time for down this time he can was call
gibberish.txt
Displaying gibberish.txt."""

    main()
