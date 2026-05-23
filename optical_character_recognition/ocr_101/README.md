# OCR

## What is OCR?

Simple system.
1. It takes an image that has the text
2. Automatically detects and text read it like a human would
3. Convert the text it read into a machine-readable (string encoded variable) format so it can be indexed, searched or processed later

## OCR is Hard

1. Humans write in different ways
2. There are different fonts and writing styles
3. Documents can be noisy, dirty or distorted
4. We have all problems of NLP compounded with fact that CV will never obtain 100% accuracy when reading a text from an image

---
- Goal is to get close to 100% accuracy but then apply some downstream rules and heuristics to cover for the deficiency of the OCR systems overall
- OCR is not a solved problem and it getting better everyday

## Applications of OCR

1. Automatic License Plate Recognition (ALPR)
2. Traffic Sign Recognition
3. Analyzing CAPTCHA's on websites
4. Extract information from business cards
5. Extract information from passport
6. Parse routing numbers, account numbers on bank cheques, currency notes
7. Understanding text in natural scenes such as photos captured from phones

## OCR vs OSD (Orientation and Script Detection)

1. Pre-cursor of the OCR
2. OSD is the pre-processing stage of analyzing the image for text meta-data, mostly looking out for orientation, writing styles, etc

---
- Text orientation is angle (in degrees) of the text
- Correction of the text orientation and angle is needed prior to OCR
- Script and Writing style refers to the set of characters used for writing and has to do with typed communication
    - Latin Language uses characters/symbols used in many European and western countries.
    - Arabic, Hebrew, Chinese, etc characters/symboles used are different than Latin characters.
- Any rules/assumptions an OCR system can make regarding a particular script/writing can make that OCR engine much more accurate
- OSD needed as a pre-processing stage to improve OCR accuracy

## General Guidelines for OCR performance improvement

1. Applying thresholding, morphological operations, etc, can help clean up images.
2. OCR engine should not be used as a generalized pre-processor for clearning up images
    > - For Example: We should not assume that a model or OCR algorithm say used for ALPR can be used to clean any texts present in any image (say PDF documents) by assuming that since its OCR, it can detect any text and help us pre-process images. OCR systems are rarely generalizable and hence needs fine-tuning based on applications.
3. OCR engines should be treated as 4th graders who are capable of reading text but need a nudge in right direction using pre/post processing techniques.
4. It's far easy for OCR to work well if there is good pre-processing done.
5. Likewise, the final results will be better with good post-processing since OCR systems will never be 100% accurate even with best pre-processing.
    > - Example 1: Can we use spell-checking to correct misspelled words?
    > - Example 2: Use RegEx to determine patters in my output OCR data. Extract only information needed (for example data/number from receipt)
    > - Example 3: Use custom rules. For instance based on License plate and state find a pattern that matches and can be used to narrow down ALPR results. 



