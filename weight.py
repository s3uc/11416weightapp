import streamlit as st
import pandas as pd
import joblib

# 모델 불러오기
model = joblib.load("weight_model_male.pkl")

st.title("몸무게 예측 웹앱")

# 사용자 입력
height = st.number_input("키를 입력하세요 (cm)", min_value=100.0, max_value=250.0, value=170.0)
waist = st.number_input("허리둘레를 입력하세요 (cm)", min_value=40.0, max_value=200.0, value=80.0)
hip = st.number_input("엉덩이둘레를 입력하세요 (cm)", min_value=40.0, max_value=200.0, value=90.0)

# 예측 버튼
if st.button("몸무게 예측"):
    # DataFrame 생성
    input_data = pd.DataFrame(
        [[height, waist, hip]],
        columns=["키", "허리둘레", "엉덩이둘레"]
    )

    # 예측
    predicted_weight = model.predict(input_data)

    # 결과 출력
    st.success(f"예측 몸무게: {predicted_weight[0]:.1f} kg")