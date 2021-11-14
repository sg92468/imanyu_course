import streamlit as st
from PIL import Image

st.title('顔認識アプリ')

uploaded_file = st.file_uploader("Choose an image...", type='jpeg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)


# import pandas as pd
# import numpy as np
# st.write('データフレーム')
# st.write(
#     pd.DataFrame({
#         '1st column': [1, 2, 3, 4],
#         '2nd column': [10, 20, 30, 40],
#     })
# )

# """
# # My 1st App
# ## マジックコマンド
# こんな感じでマジックコマンドを使用できる。Markdown対応。
# """

# if st.checkbox('Show DataFrame'):
#     chart_df = pd.DataFrame(
#         np.random.randn(20, 3),
#         columns = ['a', 'b', 'c']
#     )
#     st.line_chart(chart_df)