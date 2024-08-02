from googletrans import Translator
import time

print("Welcome to the translator")
wait = time.sleep(1)
print("This supports The languages Malayalam, Japanese, Korean, French, Hindi, Chinese, Spanish, Arabic, German, Russian, Portuguese, Italian, Indonesian, Vietnamese, and Swahili.")
wait = time.sleep(2)
Language = input("Enter the Language you want to translate to: ")
if Language == "Malayalam":
  def translate_to_malayalam(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ml')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  malayalam_translation = translate_to_malayalam(english_text)
  print(f"Malayalam translation: {malayalam_translation}")

if Language == "Japanese":
  def translate_to_japanese(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ja')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  japanese_translation = translate_to_japanese(english_text)
  print(f"Japanese translation: {japanese_translation}")

if Language == "Korean":
  def translate_to_korean(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ko')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  korean_translation = translate_to_korean(english_text)
  print(f"Korean translation: {korean_translation}")

if Language == "French":
  def translate_to_french(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='fr')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  french_translation = translate_to_french(english_text)
  print(f"French translation: {french_translation}")

if Language == "Hindi":
  def translate_to_hindi(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  hindi_translation = translate_to_hindi(english_text)
  print(f"Hindi translation: {hindi_translation}")

if Language == "Chinese":
  def translate_to_chinese(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='zh-cn')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  chinese_translation = translate_to_chinese(english_text)
  print(f"Chinese translation: {chinese_translation}")

if Language == "Spanish":
  def translate_to_spanish(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='es')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  spanish_translation = translate_to_spanish(english_text)
  print(f"Spanish translation: {spanish_translation}")

if Language == "Arabic":
  def translate_to_arabic(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ar')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  arabic_translation = translate_to_arabic(english_text)
  print(f"Arabic translation: {arabic_translation}")

if Language == "German":
  def translate_to_german(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='de')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  german_translation = translate_to_german(english_text)
  print(f"German translation: {german_translation}")

if Language == "Russian":
  def translate_to_russian(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ru')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  russian_translation = translate_to_russian(english_text)
  print(f"Russian translation: {russian_translation}")

if Language == "Portuguese":
  def translate_to_portuguese(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='pt')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  portuguese_translation = translate_to_portuguese(english_text)
  print(f"Portuguese translation: {portuguese_translation}")

if Language == "Italian":
  def translate_to_italian(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='it')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  italian_translation = translate_to_italian(english_text)
  print(f"Italian translation: {italian_translation}")

if Language == "Indonesian":
  def translate_to_indonesian(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='id')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  indonesian_translation = translate_to_indonesian(english_text)
  print(f"Indonesian translation: {indonesian_translation}")

if Language == "Vietnamese":
  def translate_to_vietnamese(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='vi')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  vietnamese_translation = translate_to_vietnamese(english_text)
  print(f"Vietnamese translation: {vietnamese_translation}")

if Language == "Swahili":
  def translate_to_swahili(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='sw')
    return translated.text
  text = input("Enter the text you want to translate: ")
  english_text = text
  swahili_translation = translate_to_swahili(english_text)
  print(f"Swahili translation: {swahili_translation}")
