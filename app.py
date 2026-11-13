import pandas as pd
import streamlit as st

from scanner import scan


# These examples are scanned, not executed in Phase 1.
SAMPLES = {
    "Grades": '''analysis Grades
load students from "students.csv" with (name text, score number, hours number)
let total = count(students)
keep students where score >= 60
show total
end''',
    "Sales - Sorting and Filtering": '''# Test case 3 - Sorting and Filtering

analysis Sales
load sales from "sales.csv" with (city text, amount number)
let limit = 100
keep sales where amount >= limit
sort sales by amount desc
show sales
end''',


    "Count Students": '''analysis StudentCount
load students from "students.csv" with (name text, score number, hours number)
let total = count(students)
show total
end''',

    "Filter and Sort Students": '''analysis PassingStudents
load students from "students.csv" with (name text, score number, hours number)
keep students where score >= 60
sort students by score desc
show students
end''',

    "Student Average": '''analysis StudentAverage
load grades from "grades.csv" with (name text, score number)
let student = "Amal"
keep grades where name == student
let total = sum(grades.score)
let countGrades = count(grades)
let average = total / countGrades
show average
end''',

    "Lexical Error Examples": '''analysis Errors
let result = 12abc
let aVeryLongIdentifierName = 5
show "missing quote
show @
end''',

}


def load_sample():
    """Update the editor safely before Streamlit renders its widget."""
    st.session_state["sift_source"] = SAMPLES[st.session_state["sample_choice"]]
    st.session_state["scan_result"] = None


st.set_page_config(
    page_title="Sift Compiler",
    layout="wide"
)

# Original heading and content order retained.
st.title("Sift Compiler")
st.subheader("Phase 1 - Lexical Analyzer")


if "sift_source" not in st.session_state:
    st.session_state["sift_source"] = ""

if "scan_result" not in st.session_state:
    st.session_state["scan_result"] = None


# Only new control: load the Sales test into the existing code editor.
st.selectbox(
    "Sample program",
    list(SAMPLES),
    index=None,
    placeholder="Select a sample program",
    key="sample_choice"
)
st.button(
    "Load Sample",
    on_click=load_sample,
    disabled=st.session_state.get("sample_choice") is None
)

source = st.text_area(
    "Sift Code Editor",
    key="sift_source",
    height=250
)

if st.button("Run Scanner"):
    if not source.strip():
        st.session_state["scan_result"] = None
        st.warning("Enter a Sift program before running the scanner.")
    else:
        try:
            tokens, symbols, errors = scan(source)
            if not isinstance(tokens, list) or not isinstance(symbols, dict) or not isinstance(errors, list):
                raise ValueError("Unexpected result format from scanner.py")
            st.session_state["scan_result"] = {
                "source": source,
                "tokens": tokens,
                "symbols": symbols,
                "errors": errors,
            }
        except Exception as exc:
            st.session_state["scan_result"] = None
            st.error(f"Scanner could not complete: {exc}")

result = st.session_state["scan_result"]
if result is not None:
    tokens = result["tokens"]
    symbols = result["symbols"]
    errors = result["errors"]

    if source != result["source"]:
        st.info("The editor has changed since the last scan. Click Run Scanner to update these results.")

    if errors:
        st.warning(f"Scanning completed with {len(errors)} lexical error(s).")
    else:
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
                st.error(str(error))
        else:
            st.success("No lexical errors found")
