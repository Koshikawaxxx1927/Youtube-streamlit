import streamlit as st
import time

# st.title('Stremlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40],
# })

# st.write(df)
# st.dataframe(df, width = 100, height = 100)
# st.dataframe(df.style.highlight_max(axis = 0))
# st.table(df.style.highlight_max(axis = 0))

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

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns = ['a', 'b', 'c']
# )

# st.line_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns = ['lat', 'lon']
# )

# st.map(df)

# st.write('Display Image')
# if st.checkbox('Show Image'):
#     img = Image.open('E594728F-3622-41C1-9872-EFA0F6DE3E41.jpeg')
#     st.image(img, caption = 'Illusion', use_column_width=True)

# condition = st.slider('あなたの調子は', 0, 100, 50)
# 'あなたのコンディションは', condition

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text, 'です'

# list = list(range(1, 11))
# option = st.selectbox (
#     'あなたの好きな数字を教えてください',
#     list
# )

# 'あなたの好きな数字は', option, 'です'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(1, 100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

expander = st.expander('問い合わせ')
expander.write('問い合わせの解答')

left_columns, right_columns = st.columns(2)

button = left_columns.button('右カラムに表示')
if button:
    right_columns.write('右からむ表示')