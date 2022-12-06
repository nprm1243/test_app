import streamlit as st
import datetime
import json
import numpy as np
import pandas as pd

CONTEST_NAME = "MOBIUS 2022"
CONTEST_ROUND = "Vòng loại"
CONTEST_PART = "Trắc nghiệm"
STARTED = False

contestant_list = {"ID":[]}

# with open("contestants.json", "w") as outfile:
#     json.dump(contestant_list, outfile)

with open('D:\download\Source-20221205T115709Z-001\Source\contestants.json', 'r') as openfile:
    contestant_list = json.load(openfile)
with open('D:\download\Source-20221205T115709Z-001\Source\done.json', 'r') as openfile:
    done_list = json.load(openfile)

st.sidebar.title(f"Đề thi {CONTEST_NAME}")
st.sidebar.header(f"{CONTEST_ROUND}")
st.sidebar.subheader(f"Phần thi: {CONTEST_PART}")
st.sidebar.write(
    '''
    **Thể lệ**
    - Đề thi gồm 12 câu hỏi trắc nghiệm.
    - Câu trả lời đúng được tính 1 điểm, câu trả lời sai không tính điểm.
    - Bất cứ thí sinh nào bị phát hiện có gian lận sẽ bị hủy kết quả thi (tương ứng với 0 điểm).
    - Với phần thi trắc nghiệm, thí sinh tô kín ô tương ứng với đáp án ở phần điền đáp án. Với phần thi tự luận, thí sinh ghi đáp án vào ô ở phần điền đáp án.
    '''
)

ContestantForm = st.sidebar.form("Thông tin thí sinh")
name = ContestantForm.text_input("Họ và tên thí sinh:", "Nguyễn Văn A")
department = ContestantForm.text_input("Khoa bạn đang học:", "Toán - Tin học")
studentID = ContestantForm.text_input("Mã số sinh viên:", "11111111")
submitted = ContestantForm.form_submit_button("Bắt đầu thi")

placeholder = st.empty()
ContestSubmitted = False

if (studentID not in done_list["ID"]):
    QuestionForm = st.form("ĐỀ THI")
    answer = {"ID": studentID, "name": name, "question_1": [], "question_2": [], "question_3": [], "total": []}
    QuestionForm.write(
        f'''
        Chào mừng thí sinh {name} đến với cuộc thi {CONTEST_NAME} - {CONTEST_ROUND}
        '''
    )
    QuestionForm.header("ĐỀ THI")
    answer["question_1"].append(QuestionForm.selectbox(
        f'Nhà toán học nào từ chối giải Fields toán học?',
        ('', 'Srinivasa Ramanujan', 'James Maynard', 'Hugo Huh', 'Grigory Perelman')
    ))
    QuestionForm.write(
        f'''
        Cho đoạn mã sau: Kết quả của $x + 7.0$ là?
        ```c++
        float x=7.6;
        std::cout <<(int)x;
        '''
    )
    answer["question_2"].append(QuestionForm.selectbox(
        '',
        ('', '14.2', '1', '14.5', '15')
    ))
    QuestionForm.write(
        r'''
        Cho số phức $z$ thỏa: $\displaystyle (1 - \sqrt{7}i)|z| = \frac{2\sqrt{22}}{z} + \sqrt{3} i + \sqrt{21}$. Mệnh đề nào sau đây là đúng:

        a) $\dfrac{1}{2} < |z| < 1$

        b) $\dfrac{3}{2} < |z| < 2$

        c) $1 < |z| < \dfrac{3}{2}$

        d) $2 < |z| < \dfrac{5}{2}$
        '''
    )
    answer["question_3"].append(QuestionForm.selectbox(
        '',
        ('', 'a', 'b', 'c', 'd')
    ))
    ContestSubmitted = QuestionForm.form_submit_button("Nộp bài")

if (ContestSubmitted):
    result = pd.read_csv("D:/download/Source-20221205T115709Z-001/Source/result.csv")
    answer["total"] = [0]
    new_result = pd.concat([result, pd.DataFrame(answer)])
    new_result.to_csv("D:/download/Source-20221205T115709Z-001/Source/result.csv")
    st.header("Bài làm của bạn đã được ghi nhận")
    done_list["ID"].append(studentID)
    with open("D:\download\Source-20221205T115709Z-001\Source\done.json", "w") as outfile:
        json.dump(done_list, outfile)

if (submitted):
    if (studentID in contestant_list["ID"]):
        st.title("Mỗi thí sinh chỉ được tham gia thi 1 lần!")
        st.subheader("Trường hợp xảy ra sự số trong quá trình thi, thí sinh vui lòng báo lại ban tổ chức để có biện pháp xử lý kịp thời")
    else:
        contestant_list["ID"].append(studentID)
        with open("D:\download\Source-20221205T115709Z-001\Source\contestants.json", "w") as outfile:
            json.dump(contestant_list, outfile)