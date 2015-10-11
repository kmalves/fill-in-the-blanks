segment_1 = '''Winter is the coldest season of the year in polar and temperate
climates, between autumn and spring. Winter is caused by the axis of the
Earth in that hemisphere being oriented away from the Sun. Different cultures
define different dates as the start of winter, and some use a definition
based on weather. When it is winter in the Northern Hemisphere it is summer
in the Southern Hemisphere, and vice versa. In many regions, winter is associated
with snow and freezing temperatures. The moment of winter solstice is when
the sun's elevation with respect to the North or South Pole is at its most negative
value.'''
segment_2 = '''A molecule that carries most of the genetic instructions used
in the development, functioning and reproduction of all known living
organisms and many viruses is called deoxyribonucleic acid or DNA.
DNA is a nucleic acid. Alongside proteins and carbohydrates, nucleic
acids compose the three major macromolecules essential for all known
forms of life. Within cells, DNA is organized into long structures called
chromosomes. During cell division these chromosomes are duplicated in the
process of DNA replication, providing each cell its own complete set of
chromosomes.'''
segment_3 ='''The SI unit for time, the second, has a long history. For many years it
was defined as 1/86,400 of a mean solar day. More recently, a new standard
was adopted to gain greater accuracy and to define the second in terms of
a non-varying, or constant, physical phenomenon (because the solar day is
getting longer due to very gradual slowing of the Earth's rotation). Cesium
atom can be made to vibrate in a very steady way, and these vibrations can
be readily observed and counted. In 1967 the second was redefined as the
time required for 9,192,631,770 of these vibrations.'''
segment_full = [segment_1, segment_2, segment_3]

substitute_words_1 = ['season', 'spring', 'summer', 'solstice']
substitute_words_2 = ['viruses', 'deoxyribonucleic', 'carbohydrates', 'chromosomes']
substitute_words_3 = ['second', '1/86,400', 'atom', '9,192,631,770']
substitute_words_full = [substitute_words_1, substitute_words_2, substitute_words_3]

blank_list = ['_1_', '_2_', '_3_', '_4_']

def segment_with_blanks (substitute_words, segment):
    """Takes in one of the text segments and a corresponding list of target words and replaces these words with "blanks"."""
    for word in substitute_words:
        if word in segment:
            index = substitute_words.index(word)
            segment = segment.replace(word, blank_list[index])
    return segment            

def play(substitute_words, blank_segment):
    """Plays the full game by taking in one of the modified text segments with blanks depending on the level selected by the player
       and a corresponding list of target words. Prints each step as you go and if all the blanks get filled in correctly returns a
       complete segment that is equal to the original text we started with - mission accomplished!"""
    for blank in blank_list:
        print blank_segment
        if blank in blank_segment:    
            index = blank_list.index(blank)
            replacement = substitute_words[index]
            print ' '#for visual separation like <br> in HTML 
            user_input = raw_input('Fill in blank' + blank + ':' + ' ')
            while user_input != replacement:
                print 'Oops... Try again!'
                user_input = raw_input('Fill in blank' + blank + ':' + ' ')
            print ' '
            print 'CORRECT!'
            print ' '
            blank_segment = blank_segment.replace(blank, user_input)
    return blank_segment   

#Beginning of the game where a player is prompted to select their desired level.
print '''Welcome! Read the text below and fill in the blanks. To start playing choose your difficulty
level from easy, medium or hard using numbers 1, 2 or 3. Have fun!'''
print ' '
user_input = raw_input('Please enter your level:' + ' ')
levels = ['1', '2', '3']
while user_input not in levels:
    user_input = raw_input('Oops... Use numbers 1, 2 or 3 ONLY:' + ' ')
if user_input in levels:
    index_levels = levels.index(user_input)
    blank_segment = segment_with_blanks(substitute_words_full[index_levels], segment_full[index_levels])
    print ' '
    print play (substitute_words_full[index_levels], blank_segment)
#End of the game. Prints out when all the blanks get filled in correctly.    
print ' '
print 'GREAT JOB! Thanks for playing!'    

