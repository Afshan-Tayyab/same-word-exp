import streamlit as st
import requests

st.title("🌍 Country Information App")

country = st.text_input("Enter country name")

if st.button("Search"):

    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    data = response.json()

    country_data = data[0]

    st.header(country_data["name"]["common"])
    st.image(country_data["flags"]["png"])

    st.write("Capital:", country_data["capital"][0])
    st.write("Region:", country_data["region"])
    st.write("Population:", country_data["population"])