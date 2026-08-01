
import streamlit as st
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="🎮 Neon Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
}

h1{
    text-align:center;
    color:#67e8f9;
    text-shadow:0px 0px 15px cyan;
}

h3{
    text-align:center;
    color:white;
}

.stButton > button{

    width:100%;
    height:110px;

    font-size:55px;
    font-weight:bold;

    border-radius:18px;

    background:#111827;

    border:2px solid #22d3ee;

    color:white;

    transition:0.25s;

}

.stButton > button:hover{

    transform:scale(1.05);

    border:2px solid #a855f7;

    box-shadow:0 0 25px cyan;

}

.block-container{

    padding-top:2rem;

}

hr{

    border:1px solid #22d3ee;

}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------

if "board" not in st.session_state:

    st.session_state.board=np.zeros((3,3),dtype=int)

if "current" not in st.session_state:

    st.session_state.current=1

if "game_over" not in st.session_state:

    st.session_state.game_over=False

if "xscore" not in st.session_state:

    st.session_state.xscore=0

if "oscore" not in st.session_state:

    st.session_state.oscore=0

if "drawscore" not in st.session_state:

    st.session_state.drawscore=0

# -----------------------------
# WINNER FUNCTION
# -----------------------------

def check_winner(board):

    if 3 in np.sum(board,axis=1) or 3 in np.sum(board,axis=0):

        return "X"

    if -3 in np.sum(board,axis=1) or -3 in np.sum(board,axis=0):

        return "O"

    if np.trace(board)==3 or np.trace(np.fliplr(board))==3:

        return "X"

    if np.trace(board)==-3 or np.trace(np.fliplr(board))==-3:

        return "O"

    if 0 not in board:

        return "Draw"

    return None

# -----------------------------
# SYMBOLS
# -----------------------------

symbols={

    0:" ",

    1:"❌",

   -1:"⭕"

}

board=st.session_state.board

# -----------------------------
# TITLE
# -----------------------------

st.title("🎮 Neon Tic Tac Toe")

st.markdown(
    "<h3>Play with your Friend</h3>",
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# SCOREBOARD
# -----------------------------

with st.sidebar:

    st.header("🏆 Score Board")

    st.metric("❌ Player X", st.session_state.xscore)

    st.metric("⭕ Player O", st.session_state.oscore)

    st.metric("🤝 Draw", st.session_state.drawscore)

    st.write("---")

    if st.session_state.current == 1:

        st.success("Current Turn : ❌ X")

    else:

        st.info("Current Turn : ⭕ O")

# -----------------------------
# BOARD
# -----------------------------

for r in range(3):

    cols = st.columns(3)

    for c in range(3):

        with cols[c]:

            text = symbols[board[r, c]]

            if st.button(
                text,
                key=f"{r}{c}",
                use_container_width=True
            ):

                if board[r, c] == 0 and not st.session_state.game_over:

                    board[r, c] = st.session_state.current

                    result = check_winner(board)

                    if result:

                        st.session_state.game_over = True

                        if result == "X":

                            st.session_state.xscore += 1

                            st.balloons()

                            st.success("🎉 Player X Wins!")

                        elif result == "O":

                            st.session_state.oscore += 1

                            st.balloons()

                            st.success("🎉 Player O Wins!")

                        else:

                            st.session_state.drawscore += 1

                            st.info("🤝 Match Draw!")

                    else:

                        st.session_state.current *= -1

                    st.rerun()

# -----------------------------
# GAME STATUS
# -----------------------------

st.write("")
st.markdown("---")

if not st.session_state.game_over:

    if st.session_state.current == 1:

        st.info("🎯 Current Turn : ❌ Player X")

    else:

        st.info("🎯 Current Turn : ⭕ Player O")

else:

    result = check_winner(board)

    if result == "X":

        st.success("🏆 Congratulations! Player X Wins!")

    elif result == "O":

        st.success("🏆 Congratulations! Player O Wins!")

    elif result == "Draw":

        st.warning("🤝 It's a Draw!")

# -----------------------------
# CONTROL BUTTONS
# -----------------------------

col1, col2 = st.columns(2)

# ---------- NEW GAME ----------

with col1:

    if st.button("🔄 New Game", use_container_width=True):

        st.session_state.board = np.zeros((3,3), dtype=int)

        st.session_state.current = 1

        st.session_state.game_over = False

        st.rerun()

# ---------- RESET SCORE ----------

with col2:

    if st.button("🗑 Reset Score", use_container_width=True):

        st.session_state.board = np.zeros((3,3), dtype=int)

        st.session_state.current = 1

        st.session_state.game_over = False

        st.session_state.xscore = 0

        st.session_state.oscore = 0

        st.session_state.drawscore = 0

        st.rerun()

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#94a3b8;font-size:16px;">
        🎮 Made with ❤️ using Streamlit & NumPy
    </div>
    """,
    unsafe_allow_html=True
)