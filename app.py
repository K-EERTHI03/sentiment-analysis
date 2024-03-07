import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer=SentimentIntensityAnalyzer()
from streamlit_extras.let_it_rain import rain
st.title("Sentiment Analysis")

message=st.text_area("Enter Your Text")
if st.button("Analyse the Sentiment"):
    scores=analyzer.polarity_scores(message)
    polarity=scores['compound']
    if polarity<0:
        st.warning("Ouch! Your text contains the negative sentiment init")
        rain(
            emoji="😢",
            font_size=30,
            falling_speed=3,
            animation_length="infinite"
        )
    if polarity>=0:
        st.success("wonderful!, Your text contains the positive sentiment")

        rain(
            emoji="😁",
            font_size=30,
            falling_speed=3,
            animation_length="infinite"
        )
    st.write(scores)
