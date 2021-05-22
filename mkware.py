import os
import random

def main()
	os.system("clear")
	print("""
	
	███╗   ███╗██╗  ██╗██╗    ██╗ █████╗ ██████╗ ███████╗
	████╗ ████║██║ ██╔╝██║    ██║██╔══██╗██╔══██╗██╔════╝
	██╔████╔██║█████╔╝ ██║ █╗ ██║███████║██████╔╝█████╗  
	██║╚██╔╝██║██╔═██╗ ██║███╗██║██╔══██║██╔══██╗██╔══╝  
	██║ ╚═╝ ██║██║  ██╗╚███╔███╔╝██║  ██║██║  ██║███████╗
	╚═╝     ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
	                                                     
	Desenvolvido by >> Iboy
	Telegram >> @iboynerd
	Discord >> Iboy #3048
	Malware para fins educacionais.
		""")
	
	decisao = str(input("Esse Malware irá criar varias pastas. S/N: "))
	if decisao=='s':
		while True:
		    ran = random.randint(10,55)
		    os.system(f"mkdir {ran}")
	else:
		os.system("clear")
		print("goodbye amigo")
		exit()

if __name__ == '__main__':
	main()
