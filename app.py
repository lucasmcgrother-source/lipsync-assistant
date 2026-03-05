import streamlit as st

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

def get_mouth_svg(viseme_key):
    mouths = {
        'lips_together': '''
            <ellipse cx="100" cy="148" rx="38" ry="6" fill="#c96060"/>
            <ellipse cx="100" cy="142" rx="38" ry="10" fill="#e08080"/>
            <ellipse cx="100" cy="154" rx="38" ry="10" fill="#e08080"/>
        ''',
        'mouth_open_wide': '''
            <ellipse cx="100" cy="148" rx="38" ry="28" fill="#8b1a1a"/>
            <ellipse cx="100" cy="126" rx="36" ry="8" fill="#f5f0e8"/>
            <ellipse cx="100" cy="168" rx="36" ry="8" fill="#f5f0e8"/>
            <ellipse cx="100" cy="142" rx="38" ry="12" fill="#e08080"/>
            <ellipse cx="100" cy="154" rx="38" ry="12" fill="#e08080"/>
        ''',
        'mouth_mid': '''
            <ellipse cx="100" cy="148" rx="38" ry="18" fill="#8b1a1a"/>
            <ellipse cx="100" cy="132" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="163" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="142" rx="38" ry="10" fill="#e08080"/>
            <ellipse cx="100" cy="154" rx="38" ry="10" fill="#e08080"/>
        ''',
        'mouth_narrow': '''
            <ellipse cx="100" cy="148" rx="28" ry="12" fill="#8b1a1a"/>
            <ellipse cx="100" cy="138" rx="26" ry="6" fill="#f5f0e8"/>
            <ellipse cx="100" cy="158" rx="26" ry="6" fill="#f5f0e8"/>
            <ellipse cx="100" cy="143" rx="28" ry="8" fill="#e08080"/>
            <ellipse cx="100" cy="153" rx="28" ry="8" fill="#e08080"/>
        ''',
        'lips_rounded': '''
            <ellipse cx="100" cy="148" rx="28" ry="22" fill="#8b1a1a"/>
            <ellipse cx="100" cy="130" rx="30" ry="10" fill="#e08080"/>
            <ellipse cx="100" cy="166" rx="30" ry="10" fill="#e08080"/>
            <ellipse cx="100" cy="138" rx="20" ry="8" fill="#f5f0e8"/>
            <ellipse cx="100" cy="158" rx="20" ry="8" fill="#f5f0e8"/>
        ''',
        'lips_rounded_slight': '''
            <ellipse cx="100" cy="148" rx="34" ry="16" fill="#8b1a1a"/>
            <ellipse cx="100" cy="134" rx="36" ry="9" fill="#e08080"/>
            <ellipse cx="100" cy="162" rx="36" ry="9" fill="#e08080"/>
            <ellipse cx="100" cy="142" rx="26" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="154" rx="26" ry="7" fill="#f5f0e8"/>
        ''',
        'teeth_lip': '''
            <ellipse cx="100" cy="148" rx="38" ry="18" fill="#8b1a1a"/>
            <ellipse cx="100" cy="132" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="134" rx="30" ry="5" fill="#f5efe8"/>
            <path d="M 62 148 Q 100 162 138 148" fill="#e08080"/>
            <ellipse cx="100" cy="142" rx="38" ry="8" fill="#e08080"/>
        ''',
        'tongue_teeth': '''
            <ellipse cx="100" cy="148" rx="38" ry="20" fill="#8b1a1a"/>
            <ellipse cx="100" cy="130" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="132" rx="28" ry="5" fill="#f5efe8"/>
            <ellipse cx="100" cy="155" rx="30" ry="10" fill="#d4827a"/>
            <ellipse cx="100" cy="142" rx="38" ry="9" fill="#e08080"/>
        ''',
        'teeth_close': '''
            <ellipse cx="100" cy="148" rx="38" ry="10" fill="#8b1a1a"/>
            <ellipse cx="100" cy="139" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="139" rx="30" ry="5" fill="#f5efe8"/>
            <ellipse cx="100" cy="157" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="157" rx="30" ry="5" fill="#f5efe8"/>
            <ellipse cx="100" cy="143" rx="38" ry="6" fill="#e08080"/>
            <ellipse cx="100" cy="153" rx="38" ry="6" fill="#e08080"/>
        ''',
        'lips_forward': '''
            <ellipse cx="100" cy="148" rx="24" ry="20" fill="#8b1a1a"/>
            <ellipse cx="100" cy="130" rx="26" ry="11" fill="#e08080"/>
            <ellipse cx="100" cy="166" rx="26" ry="11" fill="#e08080"/>
            <ellipse cx="100" cy="139" rx="16" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="157" rx="16" ry="7" fill="#f5f0e8"/>
        ''',
        'tongue_upper': '''
            <ellipse cx="100" cy="148" rx="38" ry="20" fill="#8b1a1a"/>
            <ellipse cx="100" cy="132" rx="36" ry="8" fill="#f5f0e8"/>
            <ellipse cx="100" cy="134" rx="28" ry="5" fill="#f5efe8"/>
            <ellipse cx="100" cy="136" rx="22" ry="8" fill="#d4827a"/>
            <ellipse cx="100" cy="163" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="142" rx="38" ry="9" fill="#e08080"/>
        ''',
        'tongue_tip': '''
            <ellipse cx="100" cy="148" rx="38" ry="20" fill="#8b1a1a"/>
            <ellipse cx="100" cy="130" rx="36" ry="8" fill="#f5f0e8"/>
            <ellipse cx="100" cy="148" rx="18" ry="10" fill="#d4827a"/>
            <ellipse cx="100" cy="158" rx="14" ry="6" fill="#d4827a"/>
            <ellipse cx="100" cy="163" rx="36" ry="7" fill="#f5f0e8"/>
            <ellipse cx="100" cy="142" rx="38" ry="9" fill="#e08080"/>
        ''',
        'back_throat': '''
            <ellipse cx="100" cy="148" rx="38" ry="26" fill="#8b1a1a"/>
            <ellipse cx="100" cy="124" rx="36" ry="8" fill="#f5f0e8"/>
            <ellipse cx="100" cy="172" rx="36" ry="8" fill="#f5f0e8"/>
            <ellipse cx="100" cy="148" rx="20" ry="16" fill="#6b0a0a"/>
            <ellipse cx="100" cy="142" rx="38" ry="12" fill="#e08080"/>
            <ellipse cx="100" cy="154" rx="38" ry="12" fill="#e08080"/>
        ''',
        'neutral': '''
            <path d="M 68 148 Q 100 155 132 148" fill="none" stroke="#c96060" stroke-width="4" stroke-linecap="round"/>
            <ellipse cx="100" cy="143" rx="32" ry="8" fill="#e08080"/>
            <ellipse cx="100" cy="153" rx="32" ry="8" fill="#e08080"/>
        ''',
    }

    inner = mouths.get(viseme_key, mouths['neutral'])

    return f'''
    <svg width="120" height="120" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <!-- Face -->
        <ellipse cx="100" cy="105" rx="82" ry="88" fill="#f5d5b0" stroke="#d4a574" stroke-width="2.5"/>
        <!-- Left eye -->
        <ellipse cx="72" cy="75" rx="11" ry="13" fill="white" stroke="#aaa" stroke-width="1.5"/>
        <circle cx="72" cy="76" r="6" fill="#3a3a3a"/>
        <circle cx="74" cy="74" r="2" fill="white"/>
        <!-- Right eye -->
        <ellipse cx="128" cy="75" rx="11" ry="13" fill="white" stroke="#aaa" stroke-width="1.5"/>
        <circle cx="128" cy="76" r="6" fill="#3a3a3a"/>
        <circle cx="130" cy="74" r="2" fill="white"/>
        <!-- Nose -->
        <ellipse cx="100" cy="112" rx="6" ry="4" fill="#d4a574"/>
        <!-- Mouth area -->
        <ellipse cx="100" cy="148" rx="40" ry="28" fill="#b05050" stroke="#903838" stroke-width="1.5"/>
        {inner}
    </svg>
    '''

# --- Streamlit UI ---
st.set_page_config(page_title="LipSync Assistant", page_icon="👄")
st.title("👄 LipSync Assistant")
st.markdown("*A lip articulation tool for ESL learners and lipreading practice*")
st.divider()

user_input = st.text_input("Type a word or sentence:", placeholder="e.g. hello, python, lipread")

# Plain English descriptions for each viseme
viseme_labels = {
    'lips_together': 'Lips pressed together',
    'mouth_open_wide': 'Mouth wide open',
    'mouth_mid': 'Mouth half open',
    'mouth_narrow': 'Mouth slightly open, spread wide',
    'lips_rounded': 'Lips rounded and forward',
    'lips_rounded_slight': 'Lips slightly rounded',
    'teeth_lip': 'Upper teeth on lower lip',
    'tongue_teeth': 'Tongue between teeth',
    'teeth_close': 'Teeth nearly touching',
    'lips_forward': 'Lips pushed forward',
    'tongue_upper': 'Tongue touches upper teeth',
    'tongue_tip': 'Tongue tip raised',
    'back_throat': 'Back of throat engaged',
    'neutral': 'Relaxed mouth position',
}

if user_input:
    chars = [c for c in user_input.lower() if c.isalpha()]
    if chars:
        st.subheader(f"Analyzing: '{user_input}'")
        st.caption("👆 Each face shows how your mouth should look when making this sound.")
        cols_per_row = 5
        for i in range(0, len(chars), cols_per_row):
            chunk = chars[i:i+cols_per_row]
            cols = st.columns(len(chunk))
            for col, char in zip(cols, chunk):
                viseme = viseme_map.get(char, 'neutral')
                svg = get_mouth_svg(viseme)
                label = viseme_labels.get(viseme, 'Relaxed mouth position')
                combined = f"""<div style='text-align:center'>
                    {svg}
                    <p style='font-size:18px; font-weight:bold; margin:4px 0 2px 0'>{char}</p>
                    <p style='font-size:11px; color:#666; margin:0; line-height:1.3'>{label}</p>
                </div>"""
                with col:
                    st.components.v1.html(combined, height=195)