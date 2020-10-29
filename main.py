"""Import class modules."""
from linked_list import LinkedList

playlist = LinkedList()

playlist.append('The Payback')
playlist.prepend('Mutant')
playlist.append('Xen')
playlist.append('To Live and Die in LA')
playlist.append('Stop Trying to be God')
playlist.prepend('I Love You')
print("PRINTING ORIGINAL PLAYLIST")
playlist.print_songs()

playlist.delete_from_head()
print("PRINTING AFTER DELETING FROM HEAD")
playlist.print_songs()

playlist.delete_from_tail()
print("PRINTING AFTER DELETING FROM TAIL")
playlist.print_songs()

print("FIND MUTANT")
print(playlist.find('Mutant'))

playlist.delete('Mutant')
print("PRINT AFTER DELETING MUTANT")
playlist.print_songs()

playlist.reverse()
print("AFTER REVERSE")
playlist.print_songs()
