import io
import streamlit as st

st.markdown('# Подсчет суммы протонов')
st.markdown('##### Пример спектра: 1H NMR (400 MHz, CDCl3) δ 7.61–7.53 (m, 2H), 7.53–7.46 (m, 5H), 7.46–7.40 (m, 3H), 1.66 (s, 6H), 1.63 (s, 3H), 1.35 (s, 3H)')
nmr_h = st.text_area("Введите текстовое описание 1Н-ЯМР спектра", value="")
if st.button("Посчитать сумму протонов"):
    nmr_h = nmr_h.replace('\n', ' ')
    nmr_h_str = nmr_h
    nmr_h = nmr_h.replace(', rotamers)', ')')
    
    if nmr_h[-1:] in ['.', ';', ',', ':']:
        nmr_h = nmr_h[:-1]

    nmr_h = nmr_h.split(',')

    proton_list = []

    for i in nmr_h:
        if 'H)' in i:
            a = i.replace(' ', '')
            a = a.replace('H)', '')
            a = a.replace('.', '')
            a = a.replace(',', '')
            a = a.replace("'", '')
            a = int(a)
            proton_list.append(a)
    st.markdown(f'### Сумма протонов = {sum(proton_list)}')
    st.markdown(f'{nmr_h_str}')
    st.markdown(f'{proton_list}')


st.markdown('# Подсчет числа уникальных углеродов')
st.markdown('#### Пример спектра: 13C NMR (100 MHz, CDCl3) δ 167.5 (d, J = 44.4 Hz), 164.3 (d, J = 11.0 Hz), 146.1, 142.1, 132.21, 132.15, 127.5, 116.2, 77.2 (d, J = 261.9 Hz), 53.2, 21.9, 19.6.')
nmr_c = st.text_area("Введите текстовое описание 13C-ЯМР спектра", value="")
if st.button("Посчитать сумму уникальных углеродов"):
    nmr_c = nmr_c.replace('\n', ' ')
    nmr_c_str = nmr_c
    if nmr_c[-1:] in ['.', ';', ',', ':']:
        nmr_c = nmr_c[:-1]

    nmr_c = nmr_c.replace(',', '')
    nmr_c = nmr_c.split(' ')

    for i in nmr_c:
        if '(' in i:
            i_index = nmr_c.index(i)
            for j in nmr_c[i_index:]:
                if ')' not in j:
                    nmr_c.remove(j)
                else:
                    nmr_c.remove(j)
                    break

    carbon_list = []
    for i in nmr_c:
        if i[0].isdigit() and i[-1:].isdigit():
            carbon_list.append(float(i))
    st.markdown(f'## Число уникальных углеродов = **{len(carbon_list)}**')
    st.markdown(f'{nmr_c_str}')
    st.markdown(f'{carbon_list}')
    
