
import streamlit as st
import requests

st.title("🎨 Explore Artworks with MET Museum API")

def search_artworks(query):
    response = requests.get(
        f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}"
    )
    if response.status_code == 200:
        data = response.json()
        return data.get("objectIDs", [])[:5]  # 최대 5개만 표시
    return []

def get_artwork_details(object_id):
    response = requests.get(
        f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    )
    if response.status_code == 200:
        return response.json()
    return {}

query = st.text_input("Search for Artworks:")
if query:
    ids = search_artworks(query)
    if not ids:
        st.warning("No results found.")
    for object_id in ids:
        data = get_artwork_details(object_id)
        st.subheader(data.get("title", "Untitled"))
        if data.get("primaryImageSmall"):
            st.image(data["primaryImageSmall"], width=300)
        st.write(f"Artist: {data.get('artistDisplayName', 'Unknown')}")
        st.write(f"Year: {data.get('objectDate', 'N/A')}")
