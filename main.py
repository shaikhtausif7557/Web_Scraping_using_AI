import streamlit as st
from scrape import scrape_website,extract_body_content,cleaned_body_content,split_dom_content

from parse import parse_with_ollama

st.title("AI Web Scraper")

url=st.text_input("Enter the url: ")

if st.button("scrape site"):
    st.write("scraping the website")
    result=scrape_website(url)

    body_content=extract_body_content(result)
    cleaned_content=cleaned_body_content(body_content)


    st.session_state.dom_content=cleaned_content

    with st.expander("view DOM content"):
        st.text_area("DOM Content",cleaned_content,height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to know from this page:")

    if st.button("Search"):
        if parse_description:
            st.write("getting the results...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)
