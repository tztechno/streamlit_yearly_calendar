import streamlit as st
import calendar

def main():
    st.title("Yearly Calendar")
    
    # 年の入力
    year = st.number_input("Select Year", min_value=0, max_value=9999, step=1, value=2024)
    
    # カレンダーの生成
    cal = calendar.HTMLCalendar(calendar.MONDAY)
    html_cal = cal.formatyear(year, width=2)  # 2列6行の表示に変更
    
    # カレンダーの表示
    st.markdown(html_cal, unsafe_allow_html=True)
    # 左側の余白を狭めるためのCSS
    st.markdown(
        """
        <style>
        .row-widget.stHorizontal {
            margin-left: 0px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
    
    