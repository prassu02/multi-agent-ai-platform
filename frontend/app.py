import streamlit as st
import requests

BACKEND_URL = "https://multi-agent-ai-platform-lmnr.onrender.com"

st.set_page_config(
    page_title="Multi-Agent AI Platform",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Platform")

# =========================
# PDF Upload
# =========================

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    try:

        with st.spinner("Uploading PDF..."):

            response = requests.post(
                f"{BACKEND_URL}/upload",
                files=files,
                timeout=120
            )

        st.write("Status Code:", response.status_code)

        st.write("Raw Response:", response.text)

        # SAFE JSON HANDLING
        try:
            data = response.json()

            if response.status_code == 200:
                st.success(
                    data.get(
                        "message",
                        "Upload successful"
                    )
                )
            else:
                st.error(data)

        except Exception:
            st.error("Backend did not return JSON")
            st.code(response.text)

    except Exception as e:
        st.error(str(e))

# =========================
# Chat Section
# =========================

query = st.text_input("Ask anything")

if st.button("Send"):

    if query.strip() == "":
        st.warning("Please enter a query")

    else:

        try:

            with st.spinner("Thinking..."):

                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={"query": query},
                    timeout=120
                )

            st.write("Status Code:", response.status_code)

            st.write("Raw Response:", response.text)

            # SAFE JSON HANDLING
            try:

                data = response.json()

                if response.status_code == 200:

                    st.success(
                        data.get(
                            "response",
                            str(data)
                        )
                    )

                else:
                    st.error(data)

            except Exception:
                st.error("Backend did not return JSON")
                st.code(response.text)

        except Exception as e:
            st.error(str(e))
