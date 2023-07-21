# Text Alignment Function Documentation

## Introduction

The purpose of this Python function is to align two sequences of text, specifically a transcript and an original text. The underlying algorithm utilizes a substitution matrix to match characters between the transcript and the original text.

The main idea behind this function is to align the desired portions of text and obtain corresponding indices for further analysis. If both large texts are known, global alignment is suitable as it can match the entire text, effectively handling typos and repetitions. The code showcases the use of global alignment. In the future, local alignment could be used to match specific portions of the text and then apply precision corrections to them.

## Importance of Text Alignment

1. **Text Comparison and Difference Identification**: Aligning texts allows us to compare different versions of a text and identify changes, edits, deletions, and additions. For instance, one could align an old document version with its newer version to highlight modifications.

2. **Synchronizing Text with Other Media**: By aligning transcripts with the original spoken text, this function facilitates the creation of captions or subtitles for videos. This is particularly beneficial for improving accessibility for individuals with hearing impairments or non-native speakers. Additionally, the alignment technique can be employed to create audiobooks where text is synchronized with spoken words.

## Dependencies

The function requires the Biopython package and utilizes the `Bio.Align.substitution_matrices.Array` and `Bio.Align.PairwiseAligner` modules.

## Usage

```python
align(transcript, original_texts, log)
```

### Returns

- `original_indices` (list of lists): Returns a list of lists where each inner list represents a sentence with its start and end character indices in the original text.

## Example

Here's an example usage of the `align` function, Note that I have already set the separator '|' in the original text.

```python
transcript  = "سم الله ارحم عن ارحيم لم يكن الذين كفروا من أهل الكتعب والمشركيم منفكين حتىا تأتيهم البينة رسول من اللهيت نوصحفا مطهرة فيها كتب قيمة وما تفرق الذيل أوتوا الكتعب إلع من بعد ما جاءتهم البينةض ومعا أمروا إلاال يعبد الله مخلصين له الدين حنفاء مخلصين له الدين احنفاء ويقيم الصلاة ويؤت لزكاة وذل كديم القيمة إنن الذين كفروا من أهل الكتاب والمشركين فينير جهنم في نار جهنم خالدين فيها أولعئك هم شره البرية إن الذين أابل وعملوا الصالحات أولئك هم خير البنية جزاؤهم عند ربهم جنعات عدم جنات عدن تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم وربوا عنه ذعلك لمن خشي ربه"
original_texts =  "بسم الله الرحمن الرحيم|لم يكن الذين كفروا من أهل الكتاب والمشركين منفكين حتى تأتيهم البينة|رسول من الله يتلو صحفا مطهرة|فيها كتب قيمة|وما تفرق الذين أوتوا الكتاب إلا من بعد ما جاءتهم البينة|وما أمروا إلا ليعبدوا الله مخلصين له الدين حنفاء ويقيموا الصلاة ويؤتوا الزكاة وذلك دين القيمة|إن الذين كفروا من أهل الكتاب والمشركين في نار جهنم خالدين فيها أولئك هم شر البرية|إن الذين آمنوا وعملوا الصالحات أولئك هم خير البرية|جزاؤهم عند ربهم جنات عدن تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم ورضوا عنه ذلك لمن خشي ربه|"
log = True

original_indices = align(transcript, original_texts,log)
```

# Output

```
T: سم الله ارحم عن ارحيم لم يكن الذين كفروا من أهل الكتعب والمشركيم منفكين حتىا تأتيهم البينة رسول من اللهيت نوصحفا مطهرة فيها كتب قيمة وما تفرق الذيل أوتوا الكتعب إلع من بعد ما جاءتهم البينةض ومعا أمروا إلاال يعبد الله مخلصين له الدين حنفاء مخلصين له الدين احنفاء ويقيم الصلاة ويؤت لزكاة وذل كديم القيمة إنن الذين كفروا من أهل الكتاب والمشركين فينير جهنم في نار جهنم خالدين فيها أولعئك هم شره البرية إن الذين أابل وعملوا الصالحات أولئك هم خير البنية جزاؤهم عند ربهم جنعات عدم جنات عدن تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم وربوا عنه ذعلك لمن خشي ربه
O: بسم الله الرحمن الرحيم|لم يكن الذين كفروا من أهل الكتاب والمشركين منفكين حتى تأتيهم البينة|رسول من الله يتلو صحفا مطهرة|فيها كتب قيمة|وما تفرق الذين أوتوا الكتاب إلا من بعد ما جاءتهم البينة|وما أمروا إلا ليعبدوا الله مخلصين له الدين حنفاء ويقيموا الصلاة ويؤتوا الزكاة وذلك دين القيمة|إن الذين كفروا من أهل الكتاب والمشركين في نار جهنم خالدين فيها أولئك هم شر البرية|إن الذين آمنوا وعملوا الصالحات أولئك هم خير البرية|جزاؤهم عند ربهم جنات عدن تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم ورضوا عنه ذلك لمن خشي ربه|
T (aligned): -سم الله ا-رحم عن ا-رحيم لم يكن الذين كفروا من أهل الكتعب والمشركيم منفكين حتىا تأتيهم البينة رسول من الله-يت نو-صحفا مطهرة فيها كتب قيمة وما تفرق الذيل أوتوا الكتعب إلع من بعد ما جاءتهم البينةض ومعا أمروا إلاال يعبد الله مخلصين له الدين حنفاء مخلصين له الدين احنفاء ويقيم-- الصلاة ويؤت-- -لزكاة وذل- كديم القيمة إنن الذين كفروا من أهل الكتاب والمشركين فينير جهنم في نار جهنم خالدين فيها أولعئك هم شره البرية إن الذين -أابل وعملوا الصالحات أولئك هم خير البنية جزاؤهم عند ربهم جنعات عدم جنات عدن تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم وربوا عنه ذعلك لمن خشي ربه--
O (aligned): بسم الله الرحم--ن الرحيم|لم يكن الذين كفروا من أهل الكتاب والمشركين منفكين حتى- تأتيهم البينة|رسول من الله يت-لو صحفا مطهرة|فيها كتب قيمة|وما تفرق الذين أوتوا الكتاب إلا من بعد ما جاءتهم البينة-|وم-ا أمروا إلا ل-يعبدوا--- -ال----له------ ------مخلصين له الدين -حنفاء ويقيموا الصلاة ويؤتوا الزكاة وذلك -دين القيمة|إ-ن الذين كفروا من أهل الكتاب والمشركين ف--ي- --ن------ار جهنم خالدين فيها أول-ئك هم شر- البرية|إن الذين آمنوا وعملوا الصالحات أولئك هم خير البرية|جزاؤهم عند ربهم جن-ات عد---ن-- ----تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم ورضوا عنه ذ-لك لمن خشي ربه|
(0, 24) -> (0, 22) 3
T (A) -سم الله ا-رحم عن ا-رحيم
O (A) بسم الله الرحم--ن الرحيم|
T     سم الله ارحم عن ارحيم
O     بسم الله الرحمن الرحيم
(25, 93) -> (22, 91) 3
T (A) لم يكن الذين كفروا من أهل الكتعب والمشركيم منفكين حتىا تأتيهم البينة
O (A) لم يكن الذين كفروا من أهل الكتاب والمشركين منفكين حتى- تأتيهم البينة|
T     لم يكن الذين كفروا من أهل الكتعب والمشركيم منفكين حتىا تأتيهم البينة
O     |لم يكن الذين كفروا من أهل الكتاب والمشركين منفكين حتى تأتيهم البينة|
(94, 123) -> (91, 119) 5
T (A) رسول من الله-يت نو-صحفا مطهرة
O (A) رسول من الله يت-لو صحفا مطهرة|
T     رسول من اللهيت نوصحفا مطهرة
O     رسول من الله يتلو صحفا مطهرة
(124, 137) -> (119, 133) 5
T (A) فيها كتب قيمة
O (A) فيها كتب قيمة|
T     فيها كتب قيمة
O     |فيها كتب قيمة
(138, 194) -> (133, 190) 5
T (A) وما تفرق الذيل أوتوا الكتعب إلع من بعد ما جاءتهم البينةض
O (A) وما تفرق الذين أوتوا الكتاب إلا من بعد ما جاءتهم البينة-|
T     وما تفرق الذيل أوتوا الكتعب إلع من بعد ما جاءتهم البينةض
O     |وما تفرق الذين أوتوا الكتاب إلا من بعد ما جاءتهم البينة|
(195, 312) -> (190, 302) 11
T (A) ومعا أمروا إلاال يعبد الله مخلصين له الدين حنفاء مخلصين له الدين احنفاء ويقيم-- الصلاة ويؤت-- -لزكاة وذل- كديم القيمة
O (A) وم-ا أمروا إلا ل-يعبدوا--- -ال----له------ ------مخلصين له الدين -حنفاء ويقيموا الصلاة ويؤتوا الزكاة وذلك -دين القيمة|
T     ومعا أمروا إلاال يعبد الله مخلصين له الدين حنفاء مخلصين له الدين احنفاء ويقيم الصلاة ويؤت لزكاة وذل كديم القيمة
O     وما أمروا إلا ليعبدوا الله مخلصين له الدين حنفاء ويقيموا الصلاة ويؤتوا الزكاة وذلك دين القيمة|إن الذين كفروا من
(313, 408) -> (302, 398) 11
T (A) إنن الذين كفروا من أهل الكتاب والمشركين فينير جهنم في نار جهنم خالدين فيها أولعئك هم شره البرية
O (A) إ-ن الذين كفروا من أهل الكتاب والمشركين ف--ي- --ن------ار جهنم خالدين فيها أول-ئك هم شر- البرية|
T     إنن الذين كفروا من أهل الكتاب والمشركين فينير جهنم في نار جهنم خالدين فيها أولعئك هم شره البرية
O     أهل الكتاب والمشركين في نار جهنم خالدين فيها أولئك هم شر البرية|إن الذين آمنوا وعملوا الصالحات أ
(409, 459) -> (398, 448) 12
T (A) إن الذين -أابل وعملوا الصالحات أولئك هم خير البنية
O (A) إن الذين آمنوا وعملوا الصالحات أولئك هم خير البرية|
T     إن الذين أابل وعملوا الصالحات أولئك هم خير البنية
O     ولئك هم خير البرية|جزاؤهم عند ربهم جنات عدن تجري م
(460, 574) -> (448, 562) 13
T (A) جزاؤهم عند ربهم جنعات عدم جنات عدن تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم وربوا عنه ذعلك لمن خشي ربه-
O (A) جزاؤهم عند ربهم جن-ات عد---ن-- ----تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم ورضوا عنه ذ-لك لمن خشي ربه|
T     جزاؤهم عند ربهم جنعات عدم جنات عدن تجري من تحتها الأنهار خالدين فيها أبدا رضي الله عنهم وربوا عنه ذعلك لمن خشي ربه
O     ن تحتها الأنهار خالدين فيها أبدا رضي الله عنهم ورضوا عنه ذلك لمن خشي ربه|
[[1, 0, 22], [2, 22, 91], [3, 91, 119], [4, 119, 133], [5, 133, 190], [6, 190, 302], [7, 302, 398], [8, 398, 448], [9, 448, 562]]
```

Please note that this function currently uses a hardcoded mapping from Arabic to Latin characters (`letter_to_latin`). This mapping should be defined elsewhere in your code.

## Function Mechanism

1. The function starts by creating a substitution matrix where each character is matched with every other character. The score for matching a character with itself is 2, and with any other character is -1. The score for matching a space ' ' with a '|' character is also 2.

2. Then, both the `transcript` and `original_texts` are translated to their Latin equivalents (if they are Arabic) using the `letter_to_latin` mapping.

3. Subsequently, the function aligns the translated texts using pairwise alignment.

4. The aligned sequences are then translated back to their original characters.

5. It then identifies the indices of '|' characters in `aligned_original` and maps these indices to the `transcript` indices.

6. Finally, it returns a list of tuples where each tuple represents a sentence with its start and end character indices in the `transcript`.

## Logging

If the `log` parameter is set to `True`, the function will output the following details:

- The initial transcript and original texts.
- The aligned transcript and original texts.
- The mapping from indices in the aligned original texts to the transcript indices.

## Limitations

This function currently supports Arabic texts (along with English) only. For other languages, you may need to create your own character mapping dictionary (`letter_to_latin`).
