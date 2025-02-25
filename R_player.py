import streamlit as st
import time
st.title("Introducing R PLayer ")
#st.title('<p style="color:blue;">Introducing R PLayer !</p>', unsafe_allow_html=True)

#st.markdown("feel Your inner soul just click")
st.markdown('<p style="color:blue;">Feel your inner soul, just click and enjoy the music!</p>', unsafe_allow_html=True)

#st.caption("Select a song to play ")

songs = ["ohoho.mp3","osathi.mp3","tiger_zinda.mp3"," roke_na_ruke_naina.mp3"," She_Move_It_Like.mp3","Shona_Shona_Tony_Kakkar (1).mp3 "," Tarasti_Hai_Nigahen_Meri.mp3","Tera_Yaar_Hoon_Main.mp3","Teri_Aankhon_Mein_Darshan_Raval.mp3","Tu Hi Yaar Mera - Pati Patni Aur Woh.mp3"]

selected_song = st.selectbox("Choos a song to play",songs)
st.snow()
st.audio(selected_song,format='audio/mp3',autoplay=True)
# st.progress(100)
#st.audio('tiger_zinda.mp3',format ="tiger_zinda.mp3" )
button = st.button("Snow Fall")
button2 = st.button("Baloons")
if button:
    # st.audio(selected_song,format='audio/mp3',autoplay=True)
    st.snow()
    st.success("Enjoy The Music")
    
if button2:    
    st.balloons()
    st.success("Enjoy The Music")
    


