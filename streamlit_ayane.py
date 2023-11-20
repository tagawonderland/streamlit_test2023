import time
import streamlit as st 
import numpy as np


st.title('はじめます')
st.write('田川です')

text = st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は'+text+'です')
condition = st.slider('あなたの今の調子は？',0,100,50)
option = st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
'あなたが選択したのは,',option,'です'
# st.sidebar.write('プログレスバーの表示')
# 'Start!'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration{i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)

'Done!!!'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

from PIL import Image
img = Image.open("room.jpg")
st.image(img,caption='生活場面',use_column_width=True)

import pandas as pd 
df = pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],columns = ['lat','lon',])
st.map(df)

import numpy as np 
df = pd.DataFrame(np.random.rand(20,3),columns = ['a','b','c'])
st.table(df.style.highlight_max(axis=0))
st.bar_chart(df)
