import streamlit as st
import pandas as pd
import urllib.parse

# 1. Page Configuration (Sidebar disabled)
st.set_page_config(
    page_title="Mahavir Traders | Maison",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS Injection (Top Nav & Editorial Grid)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap');

    /* Global Typography & Hide Defaults */
    header {visibility: hidden;}
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    
    /* Hide the sidebar toggle icon completely for a pure website feel */
    [data-testid="collapsedControl"] { display: none !important; }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-weight: 300;
    }

    h1, h2, h3, h4, h5 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400 !important;
        letter-spacing: -0.02em;
        color: var(--text-color);
    }

    /* --- TOP NAVIGATION STYLING --- */
    .brand-header {
        text-align: center;
        margin-top: -3rem;
    }
    .brand-title {
        font-family: 'Playfair Display', serif !important;
        font-size: 3.5rem;
        letter-spacing: 0.05em;
        margin-bottom: 0;
        line-height: 1;
    }
    .brand-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 0.65rem;
        text-transform: uppercase;
        letter-spacing: 0.4em;
        color: #9C7B5E;
        margin-top: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    /* Center the Streamlit horizontal radio and style as links */
    [data-testid="stRadio"] > div {
        display: flex;
        justify-content: center;
        gap: 3rem;
        border-bottom: 1px solid rgba(156, 123, 94, 0.2);
        padding-bottom: 1.5rem;
        margin-bottom: 3rem;
    }
    /* Hide the default radio circle (Streamlit hack) */
    [data-testid="stRadio"] div[role="radiogroup"] label > div:first-child {
        display: none !important;
    }
    /* Style the text */
    [data-testid="stRadio"] label p {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.15em !important;
        transition: color 0.3s ease;
    }
    [data-testid="stRadio"] label:hover p {
        color: #9C7B5E !important;
    }


    /* --- EDITORIAL LAYOUT --- */
    .grid-container {
        border-top: 1px solid rgba(156, 123, 94, 0.3);
        border-bottom: 1px solid rgba(156, 123, 94, 0.3);
        padding: 3rem 0;
        margin: 2rem 0;
    }

    .display-title {
        font-size: 5rem;
        line-height: 0.95;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: -0.04em;
    }
    
    .subtitle {
        font-size: 1.2rem;
        opacity: 0.8;
        line-height: 1.6;
        max-width: 800px;
        margin-bottom: 2rem;
        font-weight: 300;
    }

    /* Images */
    .hero-banner {
        width: 100%;
        height: 350px;
        object-fit: cover;
        filter: grayscale(80%) contrast(1.1);
        margin-bottom: 2rem;
        transition: filter 1.5s ease;
    }
    .hero-banner:hover {
        filter: grayscale(0%) contrast(1.1);
    }

    .editorial-img {
        width: 100%;
        height: 500px;
        object-fit: cover;
        filter: grayscale(100%);
        transition: filter 0.8s ease;
        border-radius: 2px;
    }
    .editorial-img:hover {
        filter: grayscale(0%);
    }

    /* Cards */
    .structured-card {
        border: 1px solid rgba(156, 123, 94, 0.2);
        padding: 2.5rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: rgba(156, 123, 94, 0.02);
        transition: background 0.3s ease;
    }
    .structured-card:hover {
        background: rgba(156, 123, 94, 0.06);
    }

    .metric-num {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        color: #9C7B5E;
        line-height: 1;
        margin-bottom: 0.5rem;
    }

    /* Ticker */
    .ticker-wrap {
        width: 100%;
        overflow: hidden;
        background-color: var(--text-color);
        color: var(--background-color);
        padding: 10px 0;
        white-space: nowrap;
        margin-bottom: 3rem;
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
    }
    .ticker {
        display: inline-block;
        animation: ticker 25s linear infinite;
    }
    @keyframes ticker {
        0% { transform: translate3d(0, 0, 0); }
        100% { transform: translate3d(-50%, 0, 0); }
    }
    .ticker-item {
        padding: 0 3rem;
    }

    /* Buttons */
    .btn-sharp {
        display: inline-block;
        background-color: var(--text-color);
        color: var(--background-color) !important;
        text-decoration: none;
        padding: 16px 24px;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        text-align: center;
        border: 1px solid var(--text-color);
        width: 100%;
        transition: all 0.3s ease;
    }
    .btn-sharp:hover {
        background-color: transparent;
        color: var(--text-color) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Top Navigation Header (Replaces Sidebar)
st.markdown("""
<div class="brand-header">
    <h1 class="brand-title">MAHAVIR</h1>
    <p class="brand-subtitle">Wholesale Depot</p>
</div>
""", unsafe_allow_html=True)

selected_page = st.radio(
    "Menu",
    ["The Collection", "Maison & Analytics", "Commodity Archive", "Trade Concierge"],
    horizontal=True,
    label_visibility="collapsed"
)


# ==========================================
# PAGE 1: HOME (THE COLLECTION)
# ==========================================
if selected_page == "The Collection":
    # Dynamic Live Ticker
    st.markdown("""
    <div class="ticker-wrap">
        <div class="ticker">
            <span class="ticker-item">LIVE MANDI RATES (EST)</span>
            <span class="ticker-item">BASMATI 1121 STEAM: INQUIRE</span>
            <span class="ticker-item">LOKWAN WHEAT: INQUIRE</span>
            <span class="ticker-item">TOOR DAL SORTEX: INQUIRE</span>
            <span class="ticker-item">SUGAR M-30: INQUIRE</span>
            <span class="ticker-item">LIVE MANDI RATES (EST)</span>
            <span class="ticker-item">BASMATI 1121 STEAM: INQUIRE</span>
            <span class="ticker-item">LOKWAN WHEAT: INQUIRE</span>
            <span class="ticker-item">TOOR DAL SORTEX: INQUIRE</span>
            <span class="ticker-item">SUGAR M-30: INQUIRE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='display-title'>Purity in<br>Every Grain.</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Curators of premium Basmati, pristine wheat, pulses, and essentials. Sourced directly, sorted immaculately, and supplied to the finest establishments across Navi Mumbai.</p>", unsafe_allow_html=True)

    st.markdown('<img src="https://images.unsplash.com/photo-1506484381205-f7945653044d?auto=format&fit=crop&w=2000&q=80" class="hero-banner">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown('<img class="editorial-img" src="https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&w=800&q=80">', unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top: 1rem; margin-bottom: 0;'>01. Amber Wheat</h4><p style='font-size: 0.8rem; opacity: 0.7;'>High-protein, heavy golden grains.</p>", unsafe_allow_html=True)
    with col2:
        st.markdown('<img class="editorial-img" src="https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=800&q=80">', unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top: 1rem; margin-bottom: 0;'>02. Aged Basmati</h4><p style='font-size: 0.8rem; opacity: 0.7;'>24-month aged, supreme length.</p>", unsafe_allow_html=True)
    with col3:
        st.markdown('<img class="editorial-img" src="https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=800&q=80">', unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top: 1rem; margin-bottom: 0;'>03. Polished Pulses</h4><p style='font-size: 0.8rem; opacity: 0.7;'>Machine-cleaned, stone-free dals.</p>", unsafe_allow_html=True)

    st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.markdown("<h3>Net Weight Precision</h3><p style='font-size: 0.9rem; opacity: 0.7; line-height: 1.6;'>Automated weighbridge protocols ensure absolute volume transparency across every consignment we dispatch.</p>", unsafe_allow_html=True)
    with c2:
        st.markdown("<h3>Sortex Purity</h3><p style='font-size: 0.9rem; opacity: 0.7; line-height: 1.6;'>Optically sorted, machine-cleaned grains guaranteeing zero breakage and uncompromised kitchen yield.</p>", unsafe_allow_html=True)
    with c3:
        st.markdown("<h3>Direct Transit</h3><p style='font-size: 0.9rem; opacity: 0.7; line-height: 1.6;'>Strategically positioned at Uran Road for swift, same-day dispatch to our network of premier clientele.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# PAGE 2: MAISON & ANALYTICS
# ==========================================
elif selected_page == "Maison & Analytics":
    st.markdown("<h2 style='font-size: 4rem; margin-bottom: 0;'>The Maison</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='margin-bottom: 3rem;'>A legacy of trust established in 2017. We bypass standard supply chains to bring mandi-direct pricing and unparalleled quality to institutions.</p>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="structured-card"><div class="metric-num">7</div><div style="text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.75rem;">Years Established</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="structured-card"><div class="metric-num">1.2k</div><div style="text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.75rem;">Active Partners</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="structured-card"><div class="metric-num">3.9★</div><div style="text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.75rem;">Client Rating</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="structured-card"><div class="metric-num">50k</div><div style="text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.75rem;">Quintals Supplied</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1.5, 1], gap="large")
    with left_col:
        st.markdown("<h4 style='text-transform: uppercase; letter-spacing: 0.1em;'>Supply Trajectory (MT)</h4>", unsafe_allow_html=True)
        chart_data = pd.DataFrame({
            "Quarter": ["Q1 '25", "Q2 '25", "Q3 '25", "Q4 '25", "Q1 '26", "Q2 '26"],
            "Basmati Rice": [180, 210, 240, 290, 310, 340],
            "Premium Wheat": [150, 160, 190, 230, 250, 270],
            "Refined Pulses": [90, 105, 120, 140, 160, 175]
        }).set_index("Quarter")
        st.area_chart(chart_data, color=["#111111", "#9C7B5E", "#D4B294"], use_container_width=True)

    with right_col:
        st.markdown("<h4 style='text-transform: uppercase; letter-spacing: 0.1em;'>The Standard</h4>", unsafe_allow_html=True)
        st.markdown("""
        <div class="structured-card" style="padding: 2rem;">
            <div style="border-bottom: 1px solid rgba(156,123,94,0.2); padding-bottom: 10px; margin-bottom: 10px;">
                <span style="font-size: 0.7rem; text-transform: uppercase; color: #9C7B5E;">01</span><br>
                <strong>Direct Sourcing</strong><br>
                <span style="opacity: 0.7; font-size: 0.85rem;">Eliminating intermediary margins.</span>
            </div>
            <div style="border-bottom: 1px solid rgba(156,123,94,0.2); padding-bottom: 10px; margin-bottom: 10px;">
                <span style="font-size: 0.7rem; text-transform: uppercase; color: #9C7B5E;">02</span><br>
                <strong>Hermetic Packaging</strong><br>
                <span style="opacity: 0.7; font-size: 0.85rem;">Moisture-proof 25kg & 50kg variants.</span>
            </div>
            <div style="border-bottom: 1px solid rgba(156,123,94,0.2); padding-bottom: 10px; margin-bottom: 10px;">
                <span style="font-size: 0.7rem; text-transform: uppercase; color: #9C7B5E;">03</span><br>
                <strong>Commercial Compliance</strong><br>
                <span style="opacity: 0.7; font-size: 0.85rem;">End-to-end GST invoicing.</span>
            </div>
            <div>
                <span style="font-size: 0.7rem; text-transform: uppercase; color: #9C7B5E;">04</span><br>
                <strong>Engineered Storage</strong><br>
                <span style="opacity: 0.7; font-size: 0.85rem;">Climate-controlled pest prevention.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# PAGE 3: COMMODITY ARCHIVE
# ==========================================
elif selected_page == "Commodity Archive":
    st.markdown("<h2 style='font-size: 4rem; margin-bottom: 0;'>The Archive</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='margin-bottom: 2rem;'>Explore our curated portfolio of essential commodities. Packed, sealed, and ready for institutional dispatch.</p>", unsafe_allow_html=True)

    category_filter = st.radio(
        "Filter",
        ["All Collections", "Rice", "Wheat & Grains", "Pulses & Dals", "Sugar & Oils"],
        horizontal=True,
        label_visibility="collapsed"
    )

    commodities = [
        {"name": "1121 Steam Basmati", "category": "Rice", "spec": "8.35mm length • Zero breakage • Aged 24 months", "pkg": "25 KG / 50 KG"},
        {"name": "Kolam & Sona Masoori", "category": "Rice", "spec": "Daily culinary standard • High swell • Aromatic", "pkg": "25 KG / 50 KG"},
        {"name": "Sharbati & Lokwan Wheat", "category": "Wheat & Grains", "spec": "Heavy golden grains • High protein • MP sourced", "pkg": "50 KG Sacks"},
        {"name": "Toor Dal (Sortex)", "category": "Pulses & Dals", "spec": "Desi unpolished • Stone-free • Rapid cook", "pkg": "30 KG / 50 KG"},
        {"name": "Moong & Urad Dal", "category": "Pulses & Dals", "spec": "Bold grain • Premium batter yield • Dust free", "pkg": "30 KG / 50 KG"},
        {"name": "Commercial Sugar", "category": "Sugar & Oils", "spec": "M-30 Grade • Sparkling crystal • Maharashtra mills", "pkg": "50 KG Bags"},
    ]

    filtered = [c for c in commodities if category_filter == "All Collections" or c["category"] == category_filter]

    st.markdown("<br>", unsafe_allow_html=True)
    
    cols = st.columns(2, gap="large")
    for idx, item in enumerate(filtered):
        with cols[idx % 2]:
            encoded_name = urllib.parse.quote(f"Inquiry regarding {item['name']}")
            whatsapp_url = f"https://wa.me/919820250255?text={encoded_name}"
            
            st.markdown(f"""
            <div class="structured-card" style="margin-bottom: 2rem; padding: 2rem;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <div style="font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.2em; color: #9C7B5E; margin-bottom: 5px;">{item['category']}</div>
                        <h3 style="font-size: 1.8rem; margin: 0;">{item['name']}</h3>
                    </div>
                    <div style="text-align: right; border-left: 1px solid rgba(156,123,94,0.3); padding-left: 15px;">
                        <span style="font-size: 0.6rem; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.7;">Volume</span><br>
                        <strong>{item['pkg']}</strong>
                    </div>
                </div>
                <p style="font-size: 0.9rem; opacity: 0.7; margin-bottom: 2rem;">{item['spec']}</p>
                <a href="{whatsapp_url}" target="_blank" class="btn-sharp">Request Current Mandi Rate →</a>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# PAGE 4: CONCIERGE & QUOTE
# ==========================================
elif selected_page == "Trade Concierge":
    st.markdown("<h2 style='font-size: 4rem; margin-bottom: 0;'>Trade Concierge</h2>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='margin-bottom: 3rem;'>Configure your procurement requirements below. Our trade desk will respond immediately with live market pricing.</p>", unsafe_allow_html=True)

    calc_col, info_col = st.columns([1.5, 1], gap="large")

    with calc_col:
        st.markdown("<div class='structured-card'>", unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top: 0;'>Draft Mandate</h4><hr style='border: 0; border-top: 1px solid rgba(156,123,94,0.2); margin: 1rem 0 2rem 0;'>", unsafe_allow_html=True)
        
        commodity = st.selectbox(
            "Select Commodity",
            ["Basmati Rice (1121 Steam)", "Kolam / Sona Masoori", "Sharbati / Lokwan Wheat", "Toor Dal (Sortex)", "Moong / Urad Dal", "Sugar (M-30 Grade)"]
        )
        
        c_qty, c_unit = st.columns([1, 1])
        with c_qty:
            quantity = st.number_input("Volume", min_value=1, value=25, step=1)
        with c_unit:
            unit = st.selectbox("Unit Type", ["Quintals (100 KG)", "Bags (50 KG)", "Bags (25 KG)", "Metric Tonnes (MT)"])

        delivery = st.selectbox(
            "Logistics Preference",
            ["Self-Pickup (Panvel Depot)", "Navi Mumbai Transit", "Raigad District Freight"]
        )

        inquiry_text = (
            f"Mahavir Traders Concierge,\n\nI am requesting a wholesale quotation for:\n"
            f"Commodity: {commodity}\n"
            f"Volume: {quantity} {unit}\n"
            f"Logistics: {delivery}\n\n"
            f"Please provide the current mandi rate."
        )

        encoded_inquiry = urllib.parse.quote(inquiry_text)
        wa_link = f"https://wa.me/919820250255?text={encoded_inquiry}"

        st.markdown(f"""
        <div style="background: var(--text-color); padding: 2rem; margin-top: 2rem; text-align: center;">
            <p style="font-size: 0.7rem; color: var(--background-color); text-transform: uppercase; letter-spacing: 0.2em; opacity: 0.8; margin-bottom: 10px;">Final Configuration</p>
            <h3 style="color: var(--background-color); margin-bottom: 2rem; font-size: 2rem;">{quantity} {unit} <span style="font-family: 'Inter', sans-serif; font-weight: 300; font-style: italic; font-size: 1.5rem; opacity: 0.7;">of</span><br>{commodity}</h3>
            <a href="{wa_link}" target="_blank" class="btn-sharp" style="background: var(--background-color); color: var(--text-color) !important; border-color: var(--background-color);">Submit to Trade Desk →</a>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with info_col:
        st.markdown('<img src="https://images.unsplash.com/photo-1605335178652-32b00eb58022?auto=format&fit=crop&w=800&q=80" style="width: 100%; height: 250px; object-fit: cover; filter: grayscale(100%); margin-bottom: 2rem;">', unsafe_allow_html=True)
        
        st.markdown("<h4>The Depot</h4>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 0.95rem; line-height: 2; opacity: 0.8; margin-top: 1rem; border-top: 1px solid rgba(156,123,94,0.3); padding-top: 1rem;">
        <strong>MAHAVIR TRADERS</strong><br>
        Shop No. 7, Plot No. 267<br>
        Uran Road, Near MSEB Office<br>
        Tapal Naka, Panvel<br>
        Navi Mumbai – 410206<br><br>
        
        <strong style="color: #9C7B5E;">HOURS OF OPERATION</strong><br>
        Monday — Saturday<br>
        09:00 — 17:00 IST<br>
        <span style="opacity: 0.5;">Sunday Closed</span>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# GLOBAL FOOTER
# ==========================================
st.markdown("<br><br><br><hr style='border: 0; border-top: 1px solid rgba(156,123,94,0.2); margin-bottom: 3rem;'>", unsafe_allow_html=True)

foot1, foot2, foot3 = st.columns([2, 1, 1])

with foot1:
    st.markdown("<h3 style='font-size: 1.5rem; margin-bottom: 0.5rem;'>MAHAVIR</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; opacity: 0.6;'>Curators of premium grains and wholesale essentials.<br>Established in 2017.</p>", unsafe_allow_html=True)

with foot2:
    st.markdown("<h4 style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; color: #9C7B5E; margin-bottom: 1rem;'>Location</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; opacity: 0.7; line-height: 1.8;'>Shop No. 7, Plot No. 267<br>Uran Road, Tapal Naka<br>Panvel, Navi Mumbai 410206</p>", unsafe_allow_html=True)

with foot3:
    st.markdown("<h4 style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; color: #9C7B5E; margin-bottom: 1rem;'>Trade Inquiries</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; opacity: 0.7; line-height: 1.8;'><a href='tel:+919820250255' style='color: inherit; text-decoration: none;'>+91 9820250255</a><br>Monday — Saturday<br>09:00 — 17:00 IST</p>", unsafe_allow_html=True)