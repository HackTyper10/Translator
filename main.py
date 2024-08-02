from googletrans import Translator
import time

print("Welcome to the translator")
wait = time.sleep(1)
print("This supports Malayalam, Japanese, Korean, French, Hindi, and Chinese.")
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
