import streamlit as st

def show_banner():
    banner_css = st.markdown("""
    <style>
    /* Reduce top padding of the main container */
    .block-container {
        padding-top: 0rem;
    }
    
    .banner {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .banner h1 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -2px;
    }
    
    .banner p {
        font-size: 1.1rem;
        opacity: 0.85;
        margin-top: 0.5rem;
    }
    
    .badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 10px;
        border: 1px solid rgba(255, 255, 255, 0.4);
    }
    </style>
    
    <div class="banner">
        <div class="badge">Enterprise Edition</div>
        <h1>Dashboard Pro</h1>
    </div>
    """, unsafe_allow_html=True)

    return banner_css