
'''
Write user-friendly code with pep-8 naming conventions
What is PEP 8?
** PEP => a python enhancement Proposal
** PEP 8 => a set of style guidlines for python

https://www.python.org/dev/peps/pep-0008/


Why follow PEP 8?

Readable Code :
** mostly for yourself (and other developers)

User-friendly Code:
** following naming conventions is a way to document your code
** mostly useful for users (which can be developers too)
'''

# The most important naming conventions

# regular variables => variable names should be lowercase, where necessary separating words by underscore
import random
a_tango_artist = 'Astor Piazzolla'


# Constants => in Python all variables can be modiefied, therefore, real constants don't exisit. but to indicate that a variable should
# be treated as if it were a constant, names should be uppercase, where necessary separating words by underscore
TANGO_ARTISTS = [
    'Astor Piazzolla',
    'Hugo Díaz',
    'Aníbal Troilo'
]


# function_names()  => names of functions and class methods should be lowercase, where necessary separating words by underscore
def random_tango_artist():
    return random.choice(TANGO_ARTISTS)


print(random_tango_artist())


# ClassNames  => class names should be capitalized the first letter of each word
class TangoArtist:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return self.name


anibal_trolio = TangoArtist(name='Aníbal Troilo')
print(anibal_trolio)


# FactoryFunctionNames()  => factory functions return an object, therefore to users of your code, factory functions act like class
# definitions. to reflect this, factory-function names should also capitalize the first letter of each word.
def AstroPiazzolla():
    return TangoArtist(name='Astor Piazzolla')


astro_piazzolla = AstroPiazzolla()
print(astro_piazzolla)


# _non_public_properties => in python, properties can be accessed from anywhere, therefore private class properties don't exist,
# to indicate that a property should be treated as private, it should be fixed with an underscore
class HugoDiaz(TangoArtist):
    def __init__(self):
        TangoArtist.__init__(self, name='Hugo Diaz')
        self._instrument = 'Harmonica'

    @property
    def instrument(self):
        return self._instrument


hugo_diaz = HugoDiaz()
print(hugo_diaz.instrument)


# conflicting_names_  => if a name is already taken, suffix it with underscore _
in_ = 'Tango'
