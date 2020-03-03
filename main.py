import sys
sys.path.insert(1, 'src/')
import txt
import gui

def main():

	if len(sys.argv) != 2:
		print("Syntax: %s [gui/txt]" % sys.argv[0])
		exit()
	
	if sys.argv[1] == 'txt':
		txt.main()
	elif sys.argv[1] == 'gui':
		Gui = gui.GUI()
	else:
		print("Argumentet måste vara antingen 'gui' eller 'txt'!")
		exit()


main()
