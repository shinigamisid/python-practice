# Welcome to another Stormfather project.
x = "There are %d types of Allomantic metals." % 2 # This is the first piece of code, where I assign a variable to a string.
binary = 'one metal' # You can do this using single quotes or double quotes. どうでもいい
do_not = 'all metals'
y = "Those who can burn %s and those who %s." % (binary, do_not)

print "\n" + x
print y

print "I said: %r." % x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e + "\n"

# End of code, officially.... now, time for experimentation.
print "これはプリントされるかな？"
# Apparently not.
# This is what I saw: "SyntaxError: Non-ASCII character '\xe3' in file strings_and_text.py on line 3, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details"
# Line 3... so, you can't use Japanese at all, huh. Yare yare... _impish grin_
