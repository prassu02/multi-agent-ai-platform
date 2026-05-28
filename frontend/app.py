import streamlit as st
import requests

BACKEND_URL = "https://multi-agent-ai-platform-lmnr.onrender.com"

st.title("Multi-Agent AI Platform")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# ================= UPLOAD =================

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    try:
        response = requests.post(
            f"{BACKEND_URL}/upload",
            files=files,
            timeout=120
        )

        st.write("Status Code:", response.status_code)

        # DEBUG RESPONSE
        st.write("Response Text:", response.text)

        if response.status_code == 200:
            data = response.json()

            if "message" in data:
                st.success(data["message"])
            else:
                st.success("Upload successful")

        else:
            st.error(f"Upload failed: {response.text}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

# ================= CHAT =================

query = st.text_input("Ask anything")

if st.button("Send"):

    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={"query": query},
            timeout=120
        )

        st.write("Status Code:", response.status_code)

        st.write("Response Text:", response.text)

        if response.status_code == 200:
            data = response.json()

            if "response" in data:
                st.success(data["response"])
            else:
                st.success(str(data))

        else:
            st.error(response.text)

    except Exception as e:
        st.error(str(e))
