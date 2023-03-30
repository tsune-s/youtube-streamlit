import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'done!!'

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expander = st.expander('PCの立ち上げがうまくできません')
# expander.write('（サポートデスクからの回答）　ググレカス')

# condi = st.slider('あなたの今の調子は',0,100,30)
# 'コンデション', condi

# text = st.text_input('しゅみは？')
# 'あなたの趣味＝', text


# option = st.selectbox(
#     'あなたが好きな数字をおしえてちょ、',
#     list(range(1,11))
# )

# 'あんたの好きな数字は、', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='hogehoge', use_column_width=True)


# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4,5],
#     '2列目':[10,20,30,40,50]
# })

# st.table(df.style.highlight_max(axis=0))

# """

# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


# df2 = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# st.map(df2)
