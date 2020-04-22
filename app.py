import streamlit as st


def main():
	"""Streamlit Quick Reference App 
	 For Easy Reference and Quick Ref

	 """

	st.title('Ciao schiappe')

	from PIL import Image 
	img = Image.open("otaria.jpg")
	st.image(img,use_column_width=True,caption='Streamlit Images')


if __name__ == '__main__':
	main()

