import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tensorflow as tf

# 필요한 NLTK 데이터 다운로드 (처음 실행 시 한 번만)
# nltk.download('punkt')
# nltk.download('stopwords')

def preprocess_text(text):
    """
    텍스트 전처리: 특수 문자, 숫자, 불필요한 공백 제거 및 소문자 변환
    """
    # 소문자 변환
    text = text.lower()
    
    # 특수 문자 및 숫자 제거
    text = re.sub(r'[^a-zA-Z\s#]', '', text)
    
    # 불필요한 공백 제거
    text = ' '.join(text.split())
    
    return text

def extract_hashtags(text):
    """
    해시태그 추출
    """
    return re.findall(r'#\w+', text)

def analyze_hashtags(hashtags):
    """
    해시태그 분석: 예제로 간단한 빈도 분석을 제공합니다.
    """
    return nltk.FreqDist(hashtags)

if __name__ == '__main__':
    sample_text = "안녕하세요! Ucatch 프로젝트에 오신 것을 환영합니다. #Ucatch #AI #프로젝트"
    
    preprocessed_text = preprocess_text(sample_text)
    hashtags = extract_hashtags(preprocessed_text)
    
    print("Preprocessed Text:", preprocessed_text)
    print("Extracted Hashtags:", hashtags)
    
    hashtag_analysis = analyze_hashtags(hashtags)
    print("Hashtag Analysis:", hashtag_analysis.most_common())
