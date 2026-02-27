# LipSync Assistant - Phase 2
# Mapping text to mouth shapes (visemes)

viseme_map = {
    'p': 'lips together',
    'b': 'lips together',
    'm': 'lips together',
    'f': 'upper teeth on lower lip',
    'v': 'upper teeth on lower lip',
    'th': 'tongue between teeth',
    's': 'teeth close together',
    'z': 'teeth close together',
    'sh': 'lips slightly forward',
    'ch': 'lips slightly forward',
    't': 'tongue behind upper teeth',
    'd': 'tongue behind upper teeth',
    'n': 'tongue behind upper teeth',
    'l': 'tongue tip up',
    'r': 'lips slightly rounded',
    'k': 'back of throat',
    'g': 'back of throat',
    'a': 'mouth open wide',
    'e': 'mouth mid open, spread',
    'i': 'mouth narrow, spread',
    'o': 'lips rounded',
    'u': 'lips rounded and forward',
}

def get_viseme(sound):
    return viseme_map.get(sound.lower(), 'neutral')

def analyze_word(word):
    print(f"\nAnalyzing: '{word}'")
    print("-" * 30)
    for char in word.lower():
        if char.isalpha():
            shape = get_viseme(char)
            print(f"  '{char}' → {shape}")

# Test it
analyze_word("hello")
analyze_word("python")
analyze_word("lipread")