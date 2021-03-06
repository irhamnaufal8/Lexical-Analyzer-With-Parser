import string
import streamlit as st

st.set_page_config(layout="wide")
custom_footer = """
<style>
footer{
    visinility:visible;
}
footer:after{
    content:' by Kelompok 6 IF-44-11 | Reynhard, Irham, Abdul';
    position:relative;
    color:#77c4a1;
}
.css-pxxe24.effi0qh1
{
    visibility:hidden;
}
.css-6awftf.e19lei0e1
{
    visibility: hidden;
}
.css-e370rw.e19lei0e1
{
    visibility: hidden;
}
.css-14xtw13.e8zbici0
{
    visibility: hidden;
}
.css-16j60pt.edgvbvh9
{
    background-color: #77c4a1;
    border-color: #77c4a1;
    color: white;
}
.css-16j60pt.edgvbvh9:hover
{
    background-color: white;
    color: #77c4a1;
    border-color: #77c4a1;
    transition: 0.4s;
}
.css-1q8dd3e.edgvbvh9
{
    background-color: #77c4a1;
    border-color: #77c4a1;
    color: white;
}
.css-1q8dd3e.edgvbvh9:hover
{
    background-color: white;
    color: #77c4a1;
    border-color: #77c4a1;
    transition: 0.4s;
}
</style>
"""

st.markdown(custom_footer,unsafe_allow_html=True)

col1, col2 = st.columns(2)



#initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40']

transition_table = {}

for state in state_list:
  for alphabet in alphabet_list:
    transition_table[(state, alphabet)] = 'error'
  transition_table[(state, '.')] = 'error'
  transition_table[(state, '#')] = 'error'
  transition_table[(state, ' ')] = 'error'

#spaces before input string
transition_table['q0', ' '] = 'q0'

#transition for new token
transition_table[('q40', 'a')] = 'q1'
transition_table[('q40', 'd')] = 'q7'
transition_table[('q40', 'e')] = 'q11'
transition_table[('q40', 'j')] = 'q13'
transition_table[('q40', 'k')] = 'q19'
transition_table[('q40', 's')] = 'q24'
transition_table[('q40', 'n')] = 'q29'
transition_table[('q40', 'b')] = 'q35'

#update the transition table for the following token: ammak
transition_table[('q0', 'a')] = 'q1'
transition_table[('q1', 'm')] = 'q2'
transition_table[('q2', 'm')] = 'q3'
transition_table[('q3', 'a')] = 'q4'
transition_table[('q4', 'k')] = 'q39'
transition_table[('q39', ' ')] = 'q40'
transition_table[('q39', '#')] = 'accept'
transition_table[('q40', ' ')] = 'q40'
transition_table[('q40', '#')] = 'accept'

#update the transition table for the following token: andi
transition_table[('q1', 'n')] = 'q5'
transition_table[('q5', 'd')] = 'q6'
transition_table[('q6', 'i')] = 'q39'


#update the transition table for the following token: daeng
transition_table[('q0', 'd')] = 'q7'
transition_table[('q7', 'a')] = 'q8'
transition_table[('q8', 'e')] = 'q9'
transition_table[('q9', 'n')] = 'q10'
transition_table[('q10', 'g')] = 'q39'

#update the transition table for the following token: erang
transition_table[('q0', 'e')] = 'q11'
transition_table[('q11', 'r')] = 'q12'
transition_table[('q12', 'a')] = 'q9'

#update the transition table for the following token: jangang
transition_table[('q0', 'j')] = 'q13'
transition_table[('q13', 'a')] = 'q14'
transition_table[('q14', 'n')] = 'q15'
transition_table[('q15', 'g')] = 'q16'
transition_table[('q16', 'a')] = 'q9'

#update the transition table for the following token: juku
transition_table[('q13', 'u')] = 'q17'
transition_table[('q17', 'k')] = 'q18'
transition_table[('q18', 'u')] = 'q39'

#update the transition table for the following token: kangkong
transition_table[('q0', 'k')] = 'q19'
transition_table[('q19', 'a')] = 'q20'
transition_table[('q20', 'n')] = 'q21'
transition_table[('q21', 'g')] = 'q22'
transition_table[('q22', 'k')] = 'q23'
transition_table[('q23', 'o')] = 'q9'

#update the transition table for the following token: sapatu
transition_table[('q0', 's')] = 'q24'
transition_table[('q24', 'a')] = 'q25'
transition_table[('q25', 'p')] = 'q26'
transition_table[('q26', 'a')] = 'q27'
transition_table[('q27', 't')] = 'q28'
transition_table[('q28', 'u')] = 'q39'

#update the transition table for the following token: ngandre
transition_table[('q0', 'n')] = 'q29'
transition_table[('q29', 'g')] = 'q30'
transition_table[('q30', 'a')] = 'q31'
transition_table[('q31', 'n')] = 'q32'
transition_table[('q32', 'd')] = 'q33'
transition_table[('q33', 'r')] = 'q34'
transition_table[('q34', 'e')] = 'q39'

#update the transition table for the following token: balli
transition_table[('q0', 'b')] = 'q35'
transition_table[('q35', 'a')] = 'q36'
transition_table[('q36', 'l')] = 'q37'
transition_table[('q37', 'l')] = 'q38'
transition_table[('q38', 'i')] = 'q39'

#lexical analysis
idx_char = 0
state = 'q0'
current_token = ''
index_kata = 1

with col1:
  st.image("https://mir-s3-cdn-cf.behance.net/project_modules/2800_opt_1/8627c832475371.5684d7c017609.jpg")

with col2:
  st.title("Mak-Cek")
  st.write("Aplikasi yang mengecek penulisan kata dan grammar pada Bahasa Makassar")
  st.caption("*noun yang tersedia: ammak, andi, daeng, jangang, juku, kangkong, sapatu.")
  st.caption("*verb yang tersedia: ngandre, balli, erang.")
  st.caption("*susunan grammar yang benar adalah noun-verb-noun.")
  sentence = st.text_input("Masukkan Kata", "")
  input_string = sentence.lower()+'#'
  input_temp = sentence.split()
  cek = st.button("Cek Hasil")

  while state!='accept' and cek:
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state == 'q39' and (input_string[idx_char+1] == ' ' or input_string[idx_char+1] == '#'):
        st.write("Kata Ke-" + str(index_kata) + ": " + current_token + " \U00002705")
        current_token = ''
        index_kata += 1
    if state == 'error':
        break;
    idx_char = idx_char + 1

#conclusion
if state == 'error':
  st.header("Lexical Analyzer")
  st.error(f'Kata **{input_temp[index_kata-1]}** Tidak Terdapat Pada Kamus')

if state == 'accept' and cek:
    st.header("Lexical Analyzer")
    st.success(f"Semua Kata yang Diketik:  *'{sentence}'* Terdapat pada Kamus")
    st.balloons()

#parser
token = sentence.lower().split()
token.append('EOS')

non_terminal = ['S', 'NN', 'VB']
terminal = ['ammak', 'andi', 'daeng', 'erang', 'jangang', 'juku', 'kangkong', 'sapatu', 'ngandre', 'balli']

parse_table = {}

parse_table[('S', 'ammak')] = ['NN', 'VB', 'NN']
parse_table[('S', 'andi')] = ['NN', 'VB', 'NN']
parse_table[('S', 'daeng')] = ['NN', 'VB', 'NN']
parse_table[('S', 'sapatu')] = ['NN', 'VB', 'NN']
parse_table[('S', 'jangang')] = ['NN', 'VB', 'NN']
parse_table[('S', 'juku')] = ['NN', 'VB', 'NN']
parse_table[('S', 'kangkong')] = ['NN', 'VB', 'NN']
parse_table[('S', 'erang')] = ['error']
parse_table[('S', 'ngandre')] = ['error']
parse_table[('S', 'balli')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'ammak')] = ['ammak']
parse_table[('NN', 'andi')] = ['andi']
parse_table[('NN', 'daeng')] = ['daeng']
parse_table[('NN', 'sapatu')] = ['sapatu']
parse_table[('NN', 'jangang')] = ['jangang']
parse_table[('NN', 'juku')] = ['juku']
parse_table[('NN', 'kangkong')] = ['kangkong']
parse_table[('NN', 'erang')] = ['error']
parse_table[('NN', 'ngandre')] = ['error']
parse_table[('NN', 'balli')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'ammak')] = ['error']
parse_table[('VB', 'andi')] = ['error']
parse_table[('VB', 'daeng')] = ['error']
parse_table[('VB', 'sapatu')] = ['error']
parse_table[('VB', 'jangang')] = ['error']
parse_table[('VB', 'juku')] = ['error']
parse_table[('VB', 'kangkong')] = ['error']
parse_table[('VB', 'erang')] = ['erang']
parse_table[('VB', 'ngandre')] = ['ngandre']
parse_table[('VB', 'balli')] = ['balli']
parse_table[('VB', 'EOS')] = ['error']

stack = []
stack.append('#')
stack.append('S')

idx_token = 0
symbol = token[idx_token]

while len(stack) > 0 and cek  :
  top = stack[len(stack)-1]
  #st.write('top = ', top)
  #print('symbol = ', symbol)
  if top in terminal :
    #st.write('top adalah simbol terminal')
    if top == symbol :
      stack.pop()
      idx_token += 1
      symbol = token[idx_token]
      if symbol == 'EOS' :
        #st.write('isi stack = ', stack)
        stack.pop()
    else :
        #st.write('error')
        break
  elif top in non_terminal :
    #st.write('top adalah simbol non terminal')
    if parse_table[(top, symbol)][0] != 'error' :
      stack.pop()
      symbol_push = parse_table[(top, symbol)]
      for i in range(len(symbol_push)-1, -1, -1) :
        stack.append(symbol_push[i])
    else : 
      #st.write('error')
      break
  else :
    #write('error')
    break
  #st.write('isi stack = ', stack, end='\n\n')

if symbol == 'EOS' and len(stack) == 0 and cek :
  st.header("Parser")
  st.success(f"Semua Kata yang Diketik:  *'{sentence}'* Sudah Sesuai Grammar")
elif  cek :
  st.header("Parser")
  st.error(f"Semua Kata yang Diketik: *'{sentence}'* Tidak Sesuai Grammar")