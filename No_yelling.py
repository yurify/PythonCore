def filter_words(st):
    new_st = st[0].upper() + st[1:].lower()
    return ' '.join(new_st.split())