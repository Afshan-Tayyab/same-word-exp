import streamlit as st
import requests

st.title("Word Explorer App")

# Input box
word = st.text_input("Enter a word")

# Search button
search = st.button("Search")

# Run only when button is clicked
if search and word:

    # Datamuse API (similar words)
    datamuse_url = f"https://api.datamuse.com/words?ml={word}"
    response = requests.get(datamuse_url)
    words = response.json()

    st.subheader("Similar Words")

    for w in words[:5]:
        st.write(w["word"])


    # Pexels API Key
    PEXELS_API_KEY = "DcogTvUQtXP9acjIPBQdWWSJXw46wQ9WrL5soRTc4Xh7SptwowpjeM52"   


    # Pexels API request
    pexels_url = f"https://api.pexels.com/v1/search?query={word}&per_page=5"

    headers = {
        "Authorization": "DcogTvUQtXP9acjIPBQdWWSJXw46wQ9WrL5soRTc4Xh7SptwowpjeM52"
    }

    image_response = requests.get(pexels_url, headers=headers)
    images = image_response.json()

    st.subheader("Images")

    if "photos" in images:
        for photo in images["photos"]:
            st.image(photo["src"]["medium"])