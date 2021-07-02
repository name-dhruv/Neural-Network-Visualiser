import requests
import json
import numpy as np
import streamlit as st
import os
import matplotlib.pyplot as plt

URI = 'http://127.0.0.1:5000'

st.title('Neural Network Visualizer')
st.sidebar.markdown('# Input')
st.set_option('deprecation.showPyplotGlobalUse', False)
if st.button('Pridict'):
    response = requests.post(URI, data={})
    response = json.loads(response.text)
    preds = response.get('prediction')
    image = response.get('image')
    # print(image)
    image=np.resize(image, (28, 28))
    # print(image)
    st.sidebar.image(image, width=150)
    # print(np.shape(image),np.shape(preds),preds)
    for layer, p in enumerate(preds):
        numbers = np.squeeze(np.array(p))
        plt.figure(figsize=(32, 4))
        l1=[]
        l2=[]
        if layer == 2:
            row = 1
            col = 10
            l1=list(map(lambda number: float("{:.3f}".format(number)), numbers))
        else:
            row = 2
            col = 16
            l1=list(map(lambda number: float("{:.3f}".format(number)), numbers[:16]))
            l2=list(map(lambda number: float("{:.3f}".format(number)), numbers[16:]))

        for i, number in enumerate(numbers):
            plt.subplot(row, col, i + 1)
            plt.imshow((number * np.ones((28, 28, 3))).astype('float32'), cmap='binary')
            plt.xticks([])
            plt.yticks([])
            if layer == 2:
                plt.xlabel(str(i), fontsize=40)

        plt.subplots_adjust(wspace=0.05, hspace=0.05)
        plt.tight_layout()
        st.subheader('Layer {}'.format(layer + 1),)
        st.text(l1)
        st.pyplot()
        if row==2:
            st.text(l2)

        st.text('')
        if layer == 2:
            st.text('Max prediction probability is: ')
            st.text(float("{:.3f}".format(max(numbers))))

            predict_index = np.argmax(numbers)
            st.text('The prediction is : ')
            st.subheader(predict_index)
