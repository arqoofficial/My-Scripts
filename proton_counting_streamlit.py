import io
import streamlit as st

nmr = st.text_area("Введите текстовое описание 1Н-ЯМР спектра", value="")

if 'δ' in nmr:
    nmr = nmr[nmr.index('δ')+2:]

if st.button("Посчитать сумму протонов"):

    proton_list = []
    i = -1
        
    for symbol in nmr:
        i += 1
        if symbol == 'H' and nmr[i - 1] != ' ':
            number = nmr[i - 2:i]
            if ' ' in number:
                number = number[-1]
            proton_list.append(int(number))
    st.header(nmr)
    st.header(f'Сумма протонов = {sum(proton_list)}')
    st.header(proton_list)