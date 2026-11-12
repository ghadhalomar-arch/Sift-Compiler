
import streamlit as st
import pandas as pd
from scanner import scan

st.set_page_config(
    page_title="Sift Compiler",
    layout="wide"
)

st.title("Sift Compiler")
st.subheader("Phase 1 - Lexical Analyzer")

sample = '''analysis Grades
load students from "students.csv" with (name text, score number, hours number)
let total = count(students)
keep students where score >= 60
show total
end'''

source = st.text_area(
    "Sift Code Editor",
    value=sample,
    height=250
)

if st.button("Run Scanner"):
    tokens, symbols, errors = scan(source)

    st.success("Scanning completed")

    st.metric("Total Tokens", len(tokens))

    tab1, tab2, tab3 = st.tabs([
        "Tokens", "Symbol Table", "Lexical Errors"
    ])

    with tab1:
        st.dataframe(
            pd.DataFrame(tokens, columns=["Type", "Line", "Lexeme"]),
            use_container_width=True
        )

    with tab2:
        symbol_rows = [
            {"Identifier": name, "First Line": line}
            for name, line in symbols.items()
        ]
        st.dataframe(
            pd.DataFrame(
                symbol_rows,
                columns=["Identifier", "First Line"]
            ),
            use_container_width=True
        )

    with tab3:
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("No lexical errors found")
