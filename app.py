"""
app.py

AI Recruiter Assistant
"""

import streamlit as st
import streamlit.components.v1 as components

from src.preprocess import (
    load_candidates,
    candidate_file
)

from src.jd_parser import read_job_description

from src.jd_analyzer import analyze_job_description

from src.ranking_engine import rank_candidates


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Recruiter Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# UI Styles & Scripts Injector (Visual Overhaul)
# ----------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

custom_css = """
:root {
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    
    --bg-app: linear-gradient(135deg, #F5F7FF 0%, #FAFAFC 50%, #FAF5FF 100%);
    --bg-card: #FFFFFF;
    --primary: #4F46E5;
    --primary-hover: #4338CA;
    --text-main: #111827;
    --text-secondary: #6B7280;
    --border: #E5E7EB;
    --bg-hover: #F3F4F6;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
}

[data-theme="dark"] {
    --bg-app: linear-gradient(135deg, #0A0A10 0%, #09090B 50%, #110E1B 100%);
    --bg-card: #18181B;
    --primary: #6366F1;
    --primary-hover: #4F46E5;
    --text-main: #FAFAFA;
    --text-secondary: #A1A1AA;
    --border: #3F3F46;
    --bg-hover: #27272A;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.4);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
}

html, body {
    margin: 0 !important;
    padding: 0 !important;
    background: var(--bg-app) !important;
}

html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], .main, [data-testid="stMainView"] {
    font-family: var(--font-sans) !important;
    background: var(--bg-app) !important;
    color: var(--text-main) !important;
    transition: background 0.25s ease, border-color 0.25s ease, color 0.25s ease !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
}

.stApp {
    padding-top: 16px !important;
}
[data-testid="stAppViewContainer"] {
    padding: 0 32px 32px 32px !important;
    position: relative !important;
}
[data-testid="stAppViewContainer"]::before {
    content: "" !important;
    position: absolute !important;
    top: -10% !important;
    left: -10% !important;
    width: 50vw !important;
    height: 50vw !important;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.08) 0%, rgba(99, 102, 241, 0) 70%) !important;
    filter: blur(80px) !important;
    z-index: -1 !important;
    pointer-events: none !important;
}
[data-testid="stAppViewContainer"]::after {
    content: "" !important;
    position: absolute !important;
    bottom: -10% !important;
    right: -10% !important;
    width: 50vw !important;
    height: 50vw !important;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.06) 0%, rgba(59, 130, 246, 0) 70%) !important;
    filter: blur(80px) !important;
    z-index: -1 !important;
    pointer-events: none !important;
}
[data-theme="dark"] [data-testid="stAppViewContainer"]::before {
    background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, rgba(99, 102, 241, 0) 70%) !important;
}
[data-theme="dark"] [data-testid="stAppViewContainer"]::after {
    background: radial-gradient(circle, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0) 70%) !important;
}
[data-testid="stVerticalBlock"] {
    gap: 1.2rem !important;
}
.stElementContainer {
    margin-bottom: 0.5rem !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    border-bottom: none !important;
    border-top: none !important;
    box-shadow: none !important;
}
iframe {
    border: none !important;
}
[data-testid="stHeader"] button:not([data-testid="collapsedControl"]):not([class*="collapsedControl"]):not([data-testid="collapsedControl"] *):not([class*="collapsedControl"] *),
[data-testid="stHeader"] span:not([data-testid="collapsedControl"] *):not([class*="collapsedControl"] *),
[data-testid="stHeader"] a,
[data-testid="stHeader"] div[data-testid="stConnectionStatus"],
[data-testid="stHeader"] div[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
}
[data-testid="stSidebar"] button[class*="CollapseButton"],
button[class*="SidebarCollapseButton"] {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
}
[data-testid="collapsedControl"],
[class*="collapsedControl"] {
    position: absolute !important;
    left: -9999px !important;
    top: -9999px !important;
    opacity: 0 !important;
}
[data-testid="stDecoration"] {
    display: none !important;
    visibility: hidden !important;
    height: 0px !important;
}
footer {
    display: none !important;
    visibility: hidden !important;
    height: 0px !important;
}

h1, h2, h3, h4, h5, h6 {
    color: var(--text-main) !important;
    font-weight: 600 !important;
    font-family: var(--font-sans) !important;
}

p, label {
    font-family: var(--font-sans) !important;
}

hr {
    border-color: var(--border) !important;
    margin: 24px 0 !important;
}

[data-testid="stMetric"] {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 16px 20px !important;
    box-shadow: var(--shadow-sm) !important;
    transition: var(--transition) !important;
}
[data-testid="stMetric"]:hover {
    box-shadow: var(--shadow-md) !important;
    border-color: var(--primary) !important;
}
[data-testid="stMetricValue"] {
    color: var(--primary) !important;
    font-size: 28px !important;
    font-weight: 700 !important;
}
[data-testid="stMetricLabel"] {
    color: var(--text-secondary) !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

[data-testid="stBaseButton-secondary"], [data-testid="stBaseButton-primary"] {
    border-radius: 8px !important;
    padding: 8px 16px !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    transition: var(--transition) !important;
}
[data-testid="stBaseButton-secondary"] {
    background-color: var(--bg-card) !important;
    color: var(--text-main) !important;
    border: 1px solid var(--border) !important;
}
[data-testid="stBaseButton-secondary"]:hover {
    background-color: var(--bg-hover) !important;
    border-color: var(--text-secondary) !important;
}
[data-testid="stBaseButton-primary"] {
    background-color: var(--primary) !important;
    color: #FFFFFF !important;
    border: none !important;
}
[data-testid="stBaseButton-primary"]:hover {
    background-color: var(--primary-hover) !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2) !important;
}

[data-testid="stFileUploader"] {
    border: 2px dashed var(--border) !important;
    border-radius: 16px !important;
    background-color: var(--bg-card) !important;
    padding: 24px !important;
    transition: var(--transition) !important;
    box-shadow: var(--shadow-sm) !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--primary) !important;
}

div[data-baseweb="select"] {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] * {
    color: var(--text-main) !important;
    background-color: transparent !important;
}

[data-testid="stExpander"] {
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    background-color: var(--bg-card) !important;
    box-shadow: var(--shadow-sm) !important;
    margin-bottom: 12px !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    background-color: var(--bg-card) !important;
}

div[data-testid="stNotification"] {
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
    background-color: var(--bg-card) !important;
    box-shadow: var(--shadow-sm) !important;
}
div[data-testid="stNotification"] * {
    color: var(--text-main) !important;
}

[data-testid="stSidebar"], [data-testid="stSidebar"] * {
    text-align: left !important;
}
[data-testid="stSidebar"] {
    background-color: var(--bg-card) !important;
    border-right: 1px solid var(--border) !important;
    transform: translate(0px, 0px) !important;
    margin-left: 0px !important;
    left: 0px !important;
    width: 244px !important;
    min-width: 244px !important;
    visibility: visible !important;
    display: block !important;
}
[data-testid="stSidebar"] [data-testid="stForm"] {
    border: none !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] button {
    border: none !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 10px 16px !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    transition: var(--transition) !important;
    width: 100% !important;
}
[data-testid="stSidebar"] button[data-testid="baseButton-secondary"] {
    background-color: transparent !important;
    color: var(--text-secondary) !important;
}
[data-testid="stSidebar"] button[data-testid="baseButton-secondary"]:hover {
    background-color: var(--bg-hover) !important;
    color: var(--text-main) !important;
}
[data-testid="stSidebar"] button[data-testid="baseButton-primary"] {
    background-color: #EEF2FF !important;
    color: #4F46E5 !important;
    font-weight: 600 !important;
}
[data-theme="dark"] [data-testid="stSidebar"] button[data-testid="baseButton-primary"] {
    background-color: #1E1B4B !important;
    color: #A5B4FC !important;
}

[data-testid="stFileUploader"] {
    border: 2px dashed var(--border) !important;
    border-radius: 16px !important;
    background-color: var(--bg-card) !important;
    padding: 40px 20px !important;
    text-align: center !important;
    box-shadow: var(--shadow-sm) !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--primary) !important;
}
[data-testid="stFileUploader"] section {
    background-color: transparent !important;
    border: none !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
}
[data-testid="stFileUploader"] input[type="file"] {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    opacity: 0 !important;
    cursor: pointer !important;
    z-index: 10 !important;
}
[data-testid="stFileUploader"] section > div {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
}
[data-testid="stFileUploader"] button {
    background-color: #2563EB !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    font-weight: 500 !important;
    margin: 12px auto !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: var(--transition) !important;
    z-index: 2 !important;
}
[data-testid="stFileUploader"] button:hover {
    background-color: #1D4ED8 !important;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
}
[data-testid="stFileUploader"] section::before {
    content: "☁️" !important;
    font-size: 40px !important;
    color: var(--primary) !important;
    margin-bottom: 12px !important;
    background-color: #EEF2FF !important;
    width: 72px !important;
    height: 72px !important;
    border-radius: 50% !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: var(--shadow-sm) !important;
}
[data-theme="dark"] [data-testid="stFileUploader"] section::before {
    background-color: #1E1B4B !important;
    color: #A5B4FC !important;
}
[data-testid="stFileUploader"] section::after {
    content: "Drag & Drop your Job Description or Browse Files" !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: var(--text-secondary) !important;
    margin-top: 12px !important;
    display: block !important;
}

.how-it-works-card {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 24px !important;
    box-shadow: var(--shadow-sm) !important;
}
.how-it-works-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 24px;
}
.how-it-works-header h3 {
    margin: 0 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}
.sparkle-icon {
    font-size: 18px;
    color: #6366F1;
}
.stepper-container {
    display: flex;
    flex-direction: column;
    gap: 0;
}
.stepper-item {
    display: flex;
    gap: 16px;
    align-items: stretch;
}
.stepper-badge-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 24px;
    flex-shrink: 0;
}
.stepper-number {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    font-size: 11px;
    font-weight: 600;
    background-color: var(--primary);
    color: white !important;
    z-index: 2;
}
.stepper-thin-line {
    width: 2px;
    flex-grow: 1;
    background-color: var(--border);
    margin: 4px 0;
    z-index: 1;
}
.stepper-content-card {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    background-color: transparent;
    padding-bottom: 24px;
    flex-grow: 1;
}
.stepper-item:last-child .stepper-content-card {
    padding-bottom: 0;
}
.stepper-card-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 8px;
    font-size: 15px;
    flex-shrink: 0;
    box-shadow: var(--shadow-sm);
}
.stepper-card-icon.blue-theme {
    background-color: #EFF6FF;
    border: 1px solid #BFDBFE;
}
[data-theme="dark"] .stepper-card-icon.blue-theme {
    background-color: #1E3A8A;
    border-color: #1E40AF;
}
.stepper-card-icon.purple-theme {
    background-color: #F5F3FF;
    border: 1px solid #DDD6FE;
}
[data-theme="dark"] .stepper-card-icon.purple-theme {
    background-color: #4C1D95;
    border-color: #5B21B6;
}
.stepper-card-icon.amber-theme {
    background-color: #FFFBEB;
    border: 1px solid #FDE68A;
}
[data-theme="dark"] .stepper-card-icon.amber-theme {
    background-color: #78350F;
    border-color: #92400E;
}
.stepper-card-text h4 {
    margin: 0 0 2px 0 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    color: var(--text-main) !important;
}
.stepper-card-text p {
    margin: 0 !important;
    font-size: 12px !important;
    color: var(--text-secondary) !important;
    line-height: 1.4 !important;
}

.fixed-top-nav {
    position: fixed;
    top: 20px;
    right: 24px;
    z-index: 999999;
    display: flex;
    align-items: center;
    gap: 12px;
}
.deploy-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    background-color: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-main);
    padding: 6px 12px;
    font-size: 13px;
    font-weight: 500;
    border-radius: 8px;
    cursor: pointer;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
}
.deploy-btn:hover {
    background-color: var(--bg-hover);
}
.play-icon {
    font-size: 10px;
    color: var(--text-secondary);
}
.user-avatar {
    width: 32px;
    height: 32px;
    background-color: #EFF6FF;
    color: #1D4ED8;
    border: 1px solid #BFDBFE;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 600;
    border-radius: 50%;
    user-select: none;
}
[data-theme="dark"] .user-avatar {
    background-color: #1E3A8A;
    color: #93C5FD;
    border-color: #172554;
}

.fixed-theme-toggle {
    position: fixed;
    left: 24px;
    bottom: 24px;
    z-index: 999999;
}
.theme-toggle-label {
    font-size: 12px;
    font-weight: 500;
    color: var(--text-secondary);
    margin-bottom: 8px;
    font-family: var(--font-sans);
}
.fixed-theme-btn {
    position: relative;
    width: 60px;
    height: 30px;
    border-radius: 999px;
    background-color: var(--bg-card);
    border: 1px solid var(--border);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 6px;
    outline: none;
    box-shadow: var(--shadow-sm);
    transition: var(--transition);
}
.fixed-theme-btn-slider {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background-color: var(--primary);
    transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
[data-theme="dark"] .fixed-theme-btn-slider {
    transform: translateX(30px);
}
.fixed-sun-icon, .fixed-moon-icon {
    font-size: 14px;
    z-index: 1;
    user-select: none;
}
"""

html_content = """
<script>
(function() {
    const getDocument = () => {
        try {
            return window.parent.document || document;
        } catch(e) {
            return document;
        }
    };

    const applyTheme = (theme) => {
        const doc = getDocument();
        const root = doc.documentElement;
        const rootLocal = document.documentElement;
        
        if (theme === 'dark') {
            root.setAttribute('data-theme', 'dark');
            root.classList.add('dark-theme');
            rootLocal.setAttribute('data-theme', 'dark');
            rootLocal.classList.add('dark-theme');
        } else {
            root.setAttribute('data-theme', 'light');
            root.classList.remove('dark-theme');
            rootLocal.setAttribute('data-theme', 'light');
            rootLocal.classList.remove('dark-theme');
        }
    };

    const injectStyles = () => {
        try {
            const doc = getDocument();
            let styleEl = doc.getElementById('antigravity-custom-styles');
            if (!styleEl) {
                styleEl = doc.createElement('style');
                styleEl.id = 'antigravity-custom-styles';
                doc.head.appendChild(styleEl);
            }
            styleEl.textContent = `__CUSTOM_CSS__`;
        } catch(e) {
        }
    };

    const createThemeToggle = () => {
        try {
            const doc = getDocument();
            let toggleContainer = doc.getElementById('fixed-theme-toggle-container');
            if (!toggleContainer) {
                toggleContainer = doc.createElement('div');
                toggleContainer.id = 'fixed-theme-toggle-container';
                toggleContainer.className = 'fixed-theme-toggle';
                toggleContainer.innerHTML = `
                    <div class="theme-toggle-label">Theme</div>
                    <button id="fixed-theme-btn" class="fixed-theme-btn">
                        <span class="fixed-theme-btn-slider"></span>
                        <span class="fixed-sun-icon">☀️</span>
                        <span class="fixed-moon-icon">🌙</span>
                    </button>
                `;
                doc.body.appendChild(toggleContainer);
            }
            
            const btn = doc.getElementById('fixed-theme-btn');
            if (btn && !btn.dataset.hasListener) {
                btn.addEventListener('click', () => {
                    try {
                        const currentTheme = window.parent.localStorage.getItem('theme') || 'dark';
                        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                        window.parent.localStorage.setItem('theme', newTheme);
                        applyTheme(newTheme);
                    } catch(e) {
                        const currentTheme = localStorage.getItem('theme') || 'dark';
                        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                        localStorage.setItem('theme', newTheme);
                        applyTheme(newTheme);
                    }
                });
                btn.dataset.hasListener = 'true';
            }
        } catch(e) {
        }
    };

    const createTopNavActions = () => {
        try {
            const doc = getDocument();
            let topNav = doc.getElementById('fixed-top-nav-actions');
            if (!topNav) {
                topNav = doc.createElement('div');
                topNav.id = 'fixed-top-nav-actions';
                topNav.className = 'fixed-top-nav';
                topNav.innerHTML = `
                    <button class="deploy-btn"><span class="play-icon">▶</span> Deploy</button>
                    <div class="user-avatar">A</div>
                `;
                doc.body.appendChild(topNav);
            }
        } catch(e) {
        }
    };

    const enforceSidebarExpanded = () => {
        try {
            const doc = getDocument();
            const appContainer = doc.querySelector('[data-testid="stAppViewContainer"]');
            const isClosed = appContainer && appContainer.getAttribute('data-sidebar-visible') === 'false';
            const sidebar = doc.querySelector('[data-testid="stSidebar"]');
            const isSidebarClosedFallback = sidebar && (sidebar.getBoundingClientRect().width === 0 || sidebar.getBoundingClientRect().left < 0);
            if (isClosed || isSidebarClosedFallback) {
                const expandBtn = doc.querySelector('[data-testid="collapsedControl"] button') || 
                                  doc.querySelector('button[data-testid="collapsedControl"]') || 
                                  doc.querySelector('[data-testid="collapsedControl"]') ||
                                  doc.querySelector('button[class*="collapsedControl"]');
                if (expandBtn) {
                    expandBtn.click();
                }
            }
        } catch(e) {
        }
    };

    const removeTopDecoration = () => {
        try {
            const doc = getDocument();
            const decoration = doc.querySelector('[data-testid="stDecoration"]') || 
                              doc.querySelector('.stDecoration') || 
                              doc.querySelector('[class*="stDecoration"]');
            if (decoration) {
                decoration.remove();
            }
        } catch(e) {}
    };

    injectStyles();
    createThemeToggle();
    createTopNavActions();
    enforceSidebarExpanded();
    removeTopDecoration();
    
    setInterval(() => {
        injectStyles();
        createThemeToggle();
        createTopNavActions();
        enforceSidebarExpanded();
        removeTopDecoration();
    }, 1000);

    try {
        const savedTheme = window.parent.localStorage.getItem('theme') || 'dark';
        applyTheme(savedTheme);
    } catch(e) {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        applyTheme(savedTheme);
    }

    setInterval(() => {
        try {
            const theme = window.parent.localStorage.getItem('theme') || 'dark';
            applyTheme(theme);
        } catch(e) {
            const theme = localStorage.getItem('theme') || 'dark';
            applyTheme(theme);
        }
    }, 1000);
})();
</script>
""".replace("__CUSTOM_CSS__", custom_css)

components.html(html_content, height=0, width=0)

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Dashboard"
if "analysis_completed" not in st.session_state:
    st.session_state.analysis_completed = False
if "ranked_candidates" not in st.session_state:
    st.session_state.ranked_candidates = None
if "job_text" not in st.session_state:
    st.session_state.job_text = None
if "job_info" not in st.session_state:
    st.session_state.job_info = None

with st.sidebar:
    st.markdown("""
    <div style='margin-bottom: 24px; padding-left: 8px;'>
        <h2 style='margin: 0; font-size: 20px; font-weight: 700; color: var(--text-main); display: flex; align-items: center; gap: 8px;'>
            <span style='font-size: 22px;'>🤖</span> AI Recruiter
        </h2>
        <div style='font-size: 12px; color: var(--text-secondary); margin-left: 32px;'>Assistant</div>
    </div>
    """, unsafe_allow_html=True)
    
    is_dashboard = st.session_state.active_tab == "Dashboard"
    is_candidates = st.session_state.active_tab == "Candidates"
    
    if st.button("🏠 Dashboard", key="sidebar_nav_dashboard", type="primary" if is_dashboard else "secondary", use_container_width=True):
        st.session_state.active_tab = "Dashboard"
        st.rerun()
        
    if st.button("👥 Candidates", key="sidebar_nav_candidates", type="primary" if is_candidates else "secondary", use_container_width=True):
        st.session_state.active_tab = "Candidates"
        st.rerun()

st.title("AI Recruiter Assistant")
st.markdown("""
<div style='margin-top: -12px; margin-bottom: 24px;'>
    <div style='font-size: 18px; font-weight: 600; color: var(--primary); margin-bottom: 4px;'>See Beyond the Resume</div>
    <div style='font-size: 14px; color: var(--text-secondary); line-height: 1.5;'>AI-powered resume intelligence that analyzes job descriptions, ranks candidates, and helps recruiters identify the best-fit talent in seconds.</div>
</div>
""", unsafe_allow_html=True)
st.divider()

if st.session_state.active_tab == "Dashboard":
    if not st.session_state.analysis_completed:
        col_left, col_right = st.columns([5, 3])
        
        with col_left:
            st.markdown("<div class='upload-container-card'>", unsafe_allow_html=True)
            st.subheader("📄 Upload Job Description")
            uploaded_file = st.file_uploader("Upload DOCX", type=["docx"], label_visibility="collapsed")
            
            analyze_button = st.button("🔍 Analyze Candidates", use_container_width=True, type="primary")
            st.markdown("<div style='text-align: center; font-size: 12px; color: var(--text-secondary); margin-top: 12px;'>🔒 Your data is secure and private</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            if analyze_button and uploaded_file is not None:
                with st.spinner("Reading Job Description..."):
                    job_text = read_job_description(uploaded_file)
                with st.spinner("Analyzing Job Description..."):
                    job_info = analyze_job_description(job_text)
                with st.spinner("Loading Candidates..."):
                    candidates = load_candidates(candidate_file)
                with st.spinner("Running AI Ranking Engine..."):
                    ranked_candidates = rank_candidates(candidates, job_text, job_info)
                
                st.session_state.job_text = job_text
                st.session_state.job_info = job_info
                st.session_state.ranked_candidates = ranked_candidates
                st.session_state.analysis_completed = True
                st.rerun()
                
        with col_right:
            st.markdown("""
            <div class="how-it-works-card">
                <div class="how-it-works-header">
                    <span class="sparkle-icon">✨</span>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 600;">How it works</h3>
                </div>
                <div class="stepper-container">
                    <div class="stepper-item">
                        <div class="stepper-badge-col">
                            <div class="stepper-number">1</div>
                            <div class="stepper-thin-line"></div>
                        </div>
                        <div class="stepper-content-card">
                            <span class="stepper-card-icon blue-theme">☁️</span>
                            <div class="stepper-card-text">
                                <h4>Upload Job Description</h4>
                                <p>Upload your job description in DOCX format.</p>
                            </div>
                        </div>
                    </div>
                    <div class="stepper-item">
                        <div class="stepper-badge-col">
                            <div class="stepper-number">2</div>
                            <div class="stepper-thin-line"></div>
                        </div>
                        <div class="stepper-content-card">
                            <span class="stepper-card-icon purple-theme">🧠</span>
                            <div class="stepper-card-text">
                                <h4>AI Analysis</h4>
                                <p>Our AI analyzes the job and finds the best matches.</p>
                            </div>
                        </div>
                    </div>
                    <div class="stepper-item">
                        <div class="stepper-badge-col">
                            <div class="stepper-number">3</div>
                        </div>
                        <div class="stepper-content-card">
                            <span class="stepper-card-icon amber-theme">🏆</span>
                            <div class="stepper-card-text">
                                <h4>Get Ranked Candidates</h4>
                                <p>View ranked candidates with match scores and skills.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    else:
        # Show results dashboard
        job_info = st.session_state.job_info
        ranked_candidates = st.session_state.ranked_candidates
        
        col_left, col_right = st.columns([1, 2])
        
        with col_left:
            st.subheader("📊 Job Analysis")
            st.write(f"**Role :** {job_info['role']}")
            st.write(f"**Experience :** {job_info['experience']}")
            st.write(f"**Location :** {job_info['location']}")
            st.write("**Required Skills**")
            if len(job_info["skills"]) == 0:
                st.warning("No Skills Detected.")
            else:
                for skill in job_info["skills"]:
                    st.write(f"✅ {skill}")
                    
        with col_right:
            st.subheader("🏆 Top Ranked Candidates")
            table = []
            top_candidates = ranked_candidates[:10]
            for rank, result in enumerate(top_candidates, start=1):
                table.append({
                    "Rank": rank,
                    "Candidate ID": result["candidate_id"],
                    "Headline": result["headline"],
                    "Final Score": round(result["final_score"], 4)
                })
            st.dataframe(table, use_container_width=True, hide_index=True)
            
            import io
            import pandas as pd
            
            export_data = []
            for r_rank, r_result in enumerate(ranked_candidates, start=1):
                export_data.append({
                    "Rank": r_rank,
                    "Candidate ID": r_result["candidate_id"],
                    "Headline": r_result["headline"],
                    "Final Score": round(r_result["final_score"], 4),
                    "Semantic Score": round(r_result.get("semantic_score", 0), 4),
                    "Experience Score": round(r_result.get("experience_score", 0), 4),
                    "Skill Score": round(r_result.get("skill_score", 0), 4),
                    "Behaviour Score": round(r_result.get("behaviour_score", 0), 4),
                    "Semantic Skill Score": round(r_result.get("semantic_skill_score", 0), 4),
                    "Key Strengths": "; ".join(r_result.get("reasons", [])),
                    "Missing Skills": "; ".join(r_result.get("missing", []))
                })
            
            df_export = pd.DataFrame(export_data)
            excel_buffer = io.BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                df_export.to_excel(writer, index=False, sheet_name='Ranked Candidates')
            excel_data = excel_buffer.getvalue()
            
            st.download_button(
                label="📥 Download Ranked Candidates (XLSX)",
                data=excel_data,
                file_name="ranked_candidates.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
            
            st.info("💡 Go to the **Candidates** tab in the sidebar to review detailed profile matches and breakdown analysis.")

elif st.session_state.active_tab == "Candidates":
    if not st.session_state.analysis_completed:
        st.info("📢 Please upload a Job Description and analyze candidates first.")
    else:
        ranked_candidates = st.session_state.ranked_candidates
        top_candidates = ranked_candidates[:10]
        
        candidate_options = []
        for index, result in enumerate(top_candidates, start=1):
            candidate_options.append(f"Rank {index} | {result['candidate_id']}")
            
        selected_candidate = st.selectbox("Select Candidate", candidate_options)
        selected_index = candidate_options.index(selected_candidate)
        result = top_candidates[selected_index]
        candidate = result["candidate"]
        
        st.divider()
        st.subheader("📈 AI Score Breakdown")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Semantic", round(result["semantic_score"], 3))
            st.metric("Experience", round(result["experience_score"], 3))
        with c2:
            st.metric("Skill", round(result["skill_score"], 3))
            st.metric("Behaviour", round(result["behaviour_score"], 3))
        with c3:
            st.metric("Semantic Skill", round(result["semantic_skill_score"], 3))
            st.metric("Final Score", round(result["final_score"], 3))
            
        st.divider()
        
        st.subheader("👤 Candidate Profile")
        profile = candidate["profile"]
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Experience", f"{profile.get('years_of_experience', 0)} Years")
            st.metric("Current Company", profile.get("current_company", "-"))
        with col2:
            st.metric("Current Role", profile.get("current_title", "-"))
            st.metric("Location", profile.get("location", "-"))
            
        st.markdown("### Professional Summary")
        st.write(profile.get("summary", "No summary available."))
        st.markdown("### 🛠 Technical Skills")
        skills = []
        for skill in candidate.get("skills", []):
            name = skill.get("name", "")
            if name:
                skills.append(name)
        if len(skills) == 0:
            st.info("No Skills Available")
        else:
            st.write(", ".join(skills))
            
        st.markdown("### 💼 Career History")
        career = candidate.get("career_history", [])
        if len(career) == 0:
            st.info("No Career History")
        else:
            for job in career:
                with st.expander(f"{job.get('title','')} | {job.get('company','')}"):
                    st.write(f"Industry : {job.get('industry','-')}")
                    st.write(f"Duration : {job.get('duration_months',0)} Months")
                    if job.get("description"):
                        st.write(job.get("description"))
                        
        st.markdown("### 🎓 Education")
        education = candidate.get("education", [])
        if len(education) == 0:
            st.info("No Education Found")
        else:
            for edu in education:
                st.write(f"**{edu.get('institution','')}**")
                st.write(f"{edu.get('degree','')} | {edu.get('field_of_study','')}")
                st.write("---")
                
        st.markdown("### 🧠 Candidate Strengths")
        for reason in result["reasons"]:
            st.success(reason)
            
        st.markdown("### ⚠️ Areas of Improvement")
        if len(result["missing"]) == 0:
            st.success("No Missing Skills")
        else:
            for skill in result["missing"]:
                st.warning(skill)
st.divider()
st.caption("AI Recruiter Assistant • Phase 9.5")