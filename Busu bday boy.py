import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Happy Birthday!", layout="centered"
)

# --- CUSTOM CSS & STYLING ---
st.markdown(
    """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Quicksand:wght@400;600&display=swap');

    /* Apply global font and background theme */
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    /* Custom pastel pink birthday background theme */
    .stApp {
        background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 100%);
    }

    /* Customize headers */
    h1, h2, h3 {
        font-family: 'Fredoka', cursive;
        color: #d90429;
    }

    /* Custom styling for message cards */
    .birthday-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #ffb3c1;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- TOP BANNER IMAGE ---
st.image(
    "https://images.unsplash.com/photo-1513151233558-d860c5398176?w=1200",
    use_container_width=True,
)

# Header
st.title("Happy Birthday, Alex")
st.write("Welcome to your custom website built with Python and GitHub.")

# --- PHOTO GALLERY SECTION ---
st.markdown("---")
st.subheader("Memory Gallery")
st.write("A collection of some of our favorite moments together.")

# Create a 3-column layout for the photo grid
col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=400",
        caption="Road Trip",
        use_container_width=True,
    )
    st.image(
        "https://images.unsplash.com/photo-1517457373958-b7bdd4587205?w=400",
        caption="Concert Night",
        use_container_width=True,
    )

with col2:
    st.image(
        "https://images.unsplash.com/photo-1539635278303-d4002c07eae3?w=400",
        caption="Birthday Party",
        use_container_width=True,
    )
    st.image(
        "https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=400",
        caption="Study Session",
        use_container_width=True,
    )

with col3:
    st.image(
        "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=400",
        caption="New Year",
        use_container_width=True,
    )
    st.image(
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400",
        caption="Project Team",
        use_container_width=True,
    )


# --- PERSONAL MESSAGE BOX ---
st.markdown("---")
st.markdown(
    """
    <div class="birthday-card">
        <h3>A Special Note For You</h3>
        <p>Wishing you the absolute happiest of birthdays! Thanks for being an incredible friend, bringing so much laughter, and making every hangout awesome. Here is to another amazing year ahead!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- INTERACTIVE SURPRISE ---
st.markdown("---")
st.subheader("Click for Your Surprise")
if st.button("Open Present"):
    st.success(
        "You unlocked a coupon for free snacks on me. Have an incredible day!"
    )
