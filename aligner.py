import regex as re
from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices

letter_to_latin = {
        'ء': 'a',
        'آ': 'b',
        'أ': 'c',
        'ؤ': 'd',
        'إ': 'e',
        'ئ': 'f',
        'ا': 'g',
        'ب': 'h',
        'ة': 'i',
        'ت': 'j',
        'ث': 'k',
        'ج': 'l',
        'ح': 'm',
        'خ': 'n',
        'د': 'o',
        'ذ': 'p',
        'ر': 'q',
        'ز': 'r',
        'س': 's',
        'ش': 't',
        'ص': 'u',
        'ض': 'v',
        'ط': 'w',
        'ظ': 'x',
        'ع': 'y',
        'غ': 'z',
        'ف': 'A',
        'ق': 'B',
        'ك': 'C',
        'ل': 'D',
        'م': 'E',
        'ن': 'F',
        'ه': 'G',
        'و': 'H',
        'ى': 'I',
        'ي': 'J',
        '|': '|',
        ' ': ' '
    }


def align(transcript, original_texts, log):
    if(log):
      print('T:', transcript)
      print('O:', original_texts)
    # Using Substitution matrix to ensure that | and ' ' have same match scores. But had to conver to latin since biopython doesnt support arabic
    # Create a dictionary to map each letter to a unique Latin letter
    latin_to_letter = {v: k for k, v in letter_to_latin.items()}

    alphabet = "".join(list(letter_to_latin.values()))
    matrix = substitution_matrices.Array(alphabet=alphabet, dims=2)

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            # If the letters are the same, set the score to 1
            if alphabet[i] == alphabet[j]:
                matrix[(alphabet[i], alphabet[j])] = 2
            # If the letters are different, set the score to -1
            else:
                matrix[(alphabet[i], alphabet[j])] = -1

    matrix[(' ', '|')] = 2
    matrix[('|', ' ')] = 2

    aligner = PairwiseAligner()
    aligner.mode = 'global'
    aligner.substitution_matrix = matrix
    aligner.gap_score = -1
    # aligner.query_right_open_gap_score=-2
    aligner.query_extend_gap_score=-2

    # Use a list comprehension to create the result list
    a = "".join([letter_to_latin.get(letter, letter) for letter in transcript])

    b = "".join([letter_to_latin.get(letter, letter) for letter in original_texts])

    alns = aligner.align(a, b)
    aligned_transcript, aligned_original = alns[0][0] ,alns[0][1]

    aligned_transcript = "".join([latin_to_letter.get(letter, letter) for letter in aligned_transcript])
    aligned_original = "".join([latin_to_letter.get(letter, letter) for letter in aligned_original])
    if(log):
      print('T (aligned):', aligned_transcript)
      print('O (aligned):', aligned_original)

    indices = [i for i, x in enumerate(aligned_original) if x == "|"]
    indices = [(indices[i-1]+1 if i> 0 else 0, x) for i, x in enumerate(indices)]
    # print('Original boundaries:', indices)

    original_indicess = []
    lastAligned = 0
    for i, ind in enumerate(indices):
        start = ind[0]
        end = ind[1]+1
        alignCountTill = aligned_transcript[:end].count('-')
        characterEngIndex =end-alignCountTill

        if(log):
          print(ind, '->', (lastAligned, characterEngIndex), alignCountTill)
          print("T (A)",  aligned_transcript[start:end])
          print("O (A)", aligned_original[start:end])
          print("T    ",  transcript[lastAligned:characterEngIndex])
          print("O    ", original_texts[lastAligned:characterEngIndex])

        sentence_no = i + 1
        original_indicess.append(
            [sentence_no,
            lastAligned,
            characterEngIndex,
              ])
        lastAligned = characterEngIndex
    
    if(log):
      print(original_indicess)
    return original_indicess


def find_missing_letters(string):
    missing_letters = set()
    for letter in string:
        if letter not in letter_to_latin.keys():
            missing_letters.add(letter)

    return missing_letters


def prepare_text(s):
    s = re.sub(r'\n+', ' ', s)
    s = s.replace('.', '|')
    s = re.sub(r'[^\p{sc=Arabic}\p{N} |]', '', s)
    s = s.strip()
    s = s +" "

    missing_letters = find_missing_letters(s)
    print("Missing letters:", missing_letters)

    cleaned_string = ''.join(letter for letter in s if letter not in missing_letters)
    # s = [word for word in cleaned_string.split("|") if len(word) > 1]
    return s