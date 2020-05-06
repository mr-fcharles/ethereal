import streamlit as st

def main():

	#pages
	from home import home
	from biography import biography
	from hypothesis import hypothesis
	from stars import stars

	page = st.sidebar.selectbox("Choose a page", ["Homepage","L'importanza delle ipotesi", "Guardando le stelle","Su di me"])

	##################################### HOME PAGE #########################################
	if (page == 'Homepage'):
		home()

	####################################### BIO #########################################
	if(page=='Su di me'):
		biography()

	####################################### HYPOTHESYS #############################################
	if(page=="L'importanza delle ipotesi"):
		hypothesis()

	######################################### GUARDANDO LE STELLE ################################
	if (page == 'Guardando le stelle'):
		stars()



if __name__ == '__main__':
	main()




