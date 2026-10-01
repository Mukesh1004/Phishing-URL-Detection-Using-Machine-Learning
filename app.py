import re
import joblib
import pandas as pd
import streamlit as st

FEATURES = [
    "URLLength", "SubdomainCount", "SpecialCharCount", "DigitRatio",
    "DomainLength", "HTTPS", "HasIP", "URLDepth", "HyphenCount", "DotCount"
]

MODEL_PATH = "trained_model.pkl"
model = joblib.load(MODEL_PATH)

def extract_features(url: str) -> dict:
    url = url.strip()
    domain_match = re.search(r"https?://([^/]+)", url, flags=re.I)
    domain = domain_match.group(1) if domain_match else url.split('/')[0]
    path = url.split('://', 1)[1] if '://' in url else url
    path_parts = [p for p in path.split('/') if p]
    special_chars = sum(1 for c in url if c in "@?&=#%_:")
    digit_ratio = sum(c.isdigit() for c in url) / max(len(url), 1)
    subdomain_count = max(domain.count('.') - 1, 0)
    domain_length = len(domain)
    https = int(url.lower().startswith('https://'))
    has_ip = int(bool(re.search(r"https?://(?:\d{1,3}\.){3}\d{1,3}", url)))
    url_depth = max(len(path_parts) - 1, 0)
    hyphen_count = url.count('-')
    dot_count = url.count('.')
    return {
        "URLLength": len(url),
        "SubdomainCount": subdomain_count,
        "SpecialCharCount": special_chars,
        "DigitRatio": digit_ratio,
        "DomainLength": domain_length,
        "HTTPS": https,
        "HasIP": has_ip,
        "URLDepth": url_depth,
        "HyphenCount": hyphen_count,
        "DotCount": dot_count,
    }

st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")
st.title("🛡️ Phishing URL Detection")
st.write("Enter a URL to classify it as **Phishing** or **Legitimate**.")

url = st.text_input("URL", placeholder="https://example.com/login")

if st.button("Predict"):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        data = extract_features(url)
        X = pd.DataFrame([data])[FEATURES]
        pred = int(model.predict(X)[0])
        st.subheader("Prediction")
        if pred == 0:
            st.error("🚨 PHISHING URL")
        else:
            st.success("✅ LEGITIMATE URL")
        with st.expander("Extracted features"):
            st.dataframe(X.T.rename(columns={0: "Value"}))
