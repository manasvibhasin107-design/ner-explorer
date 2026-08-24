import streamlit as st
import requests


st.set_page_config(
    page_title="NLP Explorer",
    page_icon="🧠",
    layout="wide"
)


st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        #1e3a8a,
        #2563eb
    );
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    font-size: 17px;
    opacity: 0.9;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
}

.entity-card {
    background: white;
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.06);
}

.footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.title("🧠 NLP Explorer")

    st.markdown("---")

    st.subheader("About")

    st.write(
        "An interactive Natural Language Processing "
        "application built using FastAPI, spaCy and Streamlit."
    )

    st.markdown("---")

    st.subheader("Features")

    st.write("🔹 Tokenization")
    st.write("🔹 Lemmatization")
    st.write("🔹 POS Tagging")
    st.write("🔹 Stop Word Detection")
    st.write("🔹 Named Entity Recognition")

    st.markdown("---")

    st.caption("AIML Project")



st.markdown("""
<div class="hero">

<h1>🧠 NLP Explorer</h1>

<p>
Explore text using Natural Language Processing
and discover how machines understand language.
</p>

</div>
""", unsafe_allow_html=True)



st.subheader("📝 Enter Your Text")

text = st.text_area(
    "Enter Text",
    label_visibility="collapsed"
)



analyze = st.button(
    "🔍 Analyze Text",
    use_container_width=True
)


if analyze:

    if not text.strip():

        st.warning("⚠️ Please enter some text first.")

    else:

        with st.spinner("Analyzing your text..."):

            try:

                response = requests.post(
                    "https://ner-explorer.onrender.com/analyze",
                    params={"text": text}
                )

                result = response.json()

            except Exception as e:

                st.error(
                    "❌ Could not connect to the API. "
                    "Make sure FastAPI is running."
                )

                st.stop()


        st.success("✅ Text analyzed successfully!")


        
        st.subheader("📊 Text Statistics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Tokens",
                len(result["tokens"])
            )

        with col2:

            st.metric(
                "Entities",
                len(result["entities"])
            )

        with col3:

            st.metric(
                "Stop Words",
                len(result["stop_words"])
            )

        with col4:

            st.metric(
                "Characters",
                len(text)
            )


        st.markdown("---")


        
        st.subheader("🔎 NLP Analysis")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔤 Tokens",
            "📖 Lemmas",
            "🏷️ POS Tags",
            "🚫 Stop Words",
            "🎯 Entities"
        ])



        with tab1:

            st.write(
                "Individual words and punctuation identified "
                "in the text."
            )

            st.write(result["tokens"])



        with tab2:

            st.write(
                "Base or dictionary form of each word."
            )

            st.write(result["lemmas"])



        with tab3:

            st.write(
                "Part-of-Speech tags assigned to each word."
            )

            for item in result["pos_tags"]:

                st.markdown(
                    f"""
                    **{item['word']}**
                    → `{item['pos']}`
                    """
                )



        with tab4:

            st.write(
                "Common words detected as stop words."
            )

            if result["stop_words"]:

                st.write(
                    " • ".join(result["stop_words"])
                )

            else:

                st.info("No stop words detected.")



        with tab5:

            st.write(
                "Named entities identified by the NLP model."
            )

            if result["entities"]:

                for entity in result["entities"]:

                    st.markdown(
                        f"""
                        <div class="entity-card">

                        <strong>{entity['text']}</strong>

                        <br>

                        🏷️ Entity Type:
                        <strong>{entity['label']}</strong>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.info("No named entities detected.")



st.markdown("""
<div class="footer">

NLP Explorer • Built with Python, FastAPI, spaCy & Streamlit

</div>
""", unsafe_allow_html=True)