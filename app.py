import streamlit as st

# Viseme map from our engine
viseme_map = {
    'p': 'lips_together', 'b': 'lips_together', 'm': 'lips_together',
    'f': 'teeth_lip', 'v': 'teeth_lip',
    'th': 'tongue_teeth',
    's': 'teeth_close', 'z': 'teeth_close',
    'sh': 'lips_forward', 'ch': 'lips_forward',
    't': 'tongue_upper', 'd': 'tongue_upper', 'n': 'tongue_upper',
    'l': 'tongue_tip',
    'r': 'lips_rounded_slight',
    'k': 'back_throat', 'g': 'back_throat',
    'a': 'mouth_open_wide',
    'e': 'mouth_mid',
    'i': 'mouth_narrow',
    'o': 'lips_rounded', 'u': 'lips_rounded',
}

# SVG mouth shapes for each viseme
mouth_shapes = {
    'lips_together': '''
        <ellipse cx="100" cy="100" rx="60" ry="8" fill="#e07070"/>
        <line x1="40" y1="100" x2="160" y2="100" stroke="#c05050" stroke-width="3"/>
    ''',
    'mouth_open_wide': '''
        <ellipse cx="100" cy="100" rx="60" ry="40" fill="#c03030"/>
        <ellipse cx="100" cy="108" rx="50" ry="20" fill="#800000"/>
        <rect x="50" y="82" width="100" height="12" rx="4" fill="white"/>
        <rect x="50" y="106" width="100" height="12" rx="4" fill="white"/>
    ''',
    'mouth_mid': '''
        <ellipse cx="100" cy="100" rx="60" ry="25" fill="#c03030"/>
        <ellipse cx="100" cy="106" rx="50" ry="14" fill="#800000"/>
        <rect x="52" y="84" width="96" height="10" rx="4" fill="white"/>
        <rect x="52" y="106" width="96" height="10" rx="4" fill="white"/>
    ''',
    'mouth_narrow': '''
        <ellipse cx="100" cy="100" rx="45" ry="15" fill="#c03030"/>
        <ellipse cx="100" cy="104" rx="36" ry="8" fill="#800000"/>
        <rect x="58" y="87" width="84" height="9" rx="4" fill="white"/>
        <rect x="58" y="104" width="84" height="9" rx="4" fill="white"/>
    ''',
    'lips_rounded': '''
        <ellipse cx="100" cy="100" rx="40" ry="30" fill="#c03030"/>
        <ellipse cx="100" cy="106" rx="30" ry="18" fill="#800000"/>
        <ellipse cx="100" cy="84" rx="40" ry="10" fill="#e07070"/>
        <ellipse cx="100" cy="116" rx="40" ry="10" fill="#e07070"/>
    ''',
    'lips_rounded_slight': '''
        <ellipse cx="100" cy="100" rx="50" ry="22" fill="#c03030"/>
        <ellipse cx="100" cy="106" rx="40" ry="12" fill="#800000"/>
        <ellipse cx="100" cy="84" rx="50" ry="10" fill="#e07070"/>
        <ellipse cx="100" cy="116" rx="50" ry="10" fill="#e07070"/>
    ''',
    'teeth_lip': '''
        <ellipse cx="100" cy="100" rx="60" ry="20" fill="#c03030"/>
        <rect x="45" y="84" width="110" height="10" rx="3" fill="white"/>
        <path d="M 40 100 Q 100 118 160 100" fill="#e07070"/>
    ''',
    'tongue_teeth': '''
        <ellipse cx="100" cy="100" rx="60" ry="22" fill="#c03030"/>
        <rect x="45" y="84" width="110" height="10" rx="3" fill="white"/>
        <ellipse cx="100" cy="104" rx="45" ry="12" fill="#e08080"/>
    ''',
    'teeth_close': '''
        <ellipse cx="100" cy="100" rx="58" ry="16" fill="#c03030"/>
        <rect x="46" y="86" width="108" height="10" rx="3" fill="white"/>
        <rect x="46" y="104" width="108" height="10" rx="3" fill="white"/>
    ''',
    'lips_forward': '''
        <ellipse cx="100" cy="100" rx="35" ry="25" fill="#c03030"/>
        <ellipse cx="100" cy="106" rx="25" ry="14" fill="#800000"/>
        <ellipse cx="100" cy="82" rx="35" ry="12" fill="#e07070"/>
        <ellipse cx="100" cy="118" rx="35" ry="12" fill="#e07070"/>
    ''',
    'tongue_upper': '''
        <ellipse cx="100" cy="100" rx="58" ry="22" fill="#c03030"/>
        <ellipse cx="100" cy="90" rx="45" ry="10" fill="#e08080"/>
        <rect x="46" y="108" width="108" height="10" rx="3" fill="white"/>
    ''',
    'tongue_tip': '''
        <ellipse cx="100" cy="100" rx="58" ry="24" fill="#c03030"/>
        <ellipse cx="100" cy="88" rx="30" ry="10" fill="#e08080"/>
        <rect x="46" y="108" width="108" height="10" rx="3" fill="white"/>
    ''',
    'back_throat': '''
        <ellipse cx="100" cy="100" rx="55" ry="28" fill="#c03030"/>
        <ellipse cx="100" cy="108" rx="40" ry="16" fill="#800000"/>
        <rect x="48" y="84" width="104" height="10" rx="3" fill="white"/>
        <rect x="48" y="106" width="104" height="10" rx="3" fill="white"/>
    ''',
    'neutral': '''
        <ellipse cx="100" cy="100" rx="55" ry="12" fill="#e07070"/>
        <path d="M 45 100 Q 100 112 155 100" fill="none" stroke="#c05050" stroke-width="2"/>
    ''',
}

def get_mouth_svg(viseme_key):
    inner = mouth_shapes.get(viseme_key, mouth_shapes['neutral'])
    return f'''
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <ellipse cx="100" cy="100" rx="90" ry="80" fill="#f5d5b0" stroke="#d4a574" stroke-width="3"/>
        <ellipse cx="72" cy="72" rx="12" ry="14" fill="white" stroke="#888" stroke-width="1.5"/>
        <ellipse cx="128" cy="72" rx="12" ry="14" fill="white" stroke="#888" stroke-width="1.5"/>
        <circle cx="72" cy="73" r="6" fill="#444"/>
        <circle cx="128" cy="73" r="6" fill="#444"/>
        <ellipse cx="100" cy="100" rx="62" ry="28" fill="#c06060" stroke="#a04040" stroke-width="2"/>
        {inner}
    </svg>
    '''

# --- Streamlit UI ---
st.set_page_config(page_title="LipSync Assistant", page_icon="👄")
st.title("👄 LipSync Assistant")
st.markdown("*A lip articulation tool for ESL learners and lipreading practice*")
st.divider()

user_input = st.text_input("Type a word or sentence:", placeholder="e.g. hello, python, lipread")

if user_input:
    chars = [c for c in user_input.lower() if c.isalpha()]
    if chars:
        st.subheader(f"Analyzing: '{user_input}'")
        cols_per_row = 5
        for i in range(0, len(chars), cols_per_row):
            chunk = chars[i:i+cols_per_row]
            cols = st.columns(len(chunk))
            for col, char in zip(cols, chunk):
                viseme = viseme_map.get(char, 'neutral')
                svg = get_mouth_svg(viseme)
                combined = f"<div style='text-align:center'>{svg}<p style='font-size:20px; font-weight:bold; margin:0'>{char}</p></div>"
                with col:
                    st.components.v1.html(combined, height=230)