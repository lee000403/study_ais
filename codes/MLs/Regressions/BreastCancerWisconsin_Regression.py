# 예제 [[16.34, 87.21]]
# input() return str() -> float()

texture_mean = float(input('texture_mean : '))
perimreter_mean = float(input('perimeter_mean : '))

import pickle

with open('datasets/BreastCancerWisconsin_Regression.pkl','rb') as regression_file:
    loaded_model = pickle.load(regression_file)
    input_label = [[texture_mean, perimreter_mean]] # 학습했던 설명변수 형식
    result_predict = loaded_model.predict(input_label)
    print(('Predict radius_mean Result : {}'.format(result_predict)))
    pass