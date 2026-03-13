import streamlit as st
import requests

st.title("🌍 COUNTRY INFORMATION APP ")

country = st.text_input("Enter a country name")
is_clicked=st.button('search')
if country:
    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]

        name = data["name"]["common"]
        capital = data["capital"][0]
        region = data["region"]
        population = data["population"]
        flag = data["flags"]["png"]

        st.subheader(name)
        st.image(flag, width=200)

        st.write("**Capital:**", capital)
        st.write("**Region:**", region)
        st.write("**Population:**", population)

    else:
        st.error("Country not found")