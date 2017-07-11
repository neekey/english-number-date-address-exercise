import boto3
import random
from config import AWS_ACCESS_KEY_ID, AWS_REGION_NAME, AWS_SECRET_ACCESS_KEY
client = boto3.client(
    'polly',
    region_name=AWS_REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def get_available_voices(language_code):
    response = client.describe_voices(
        LanguageCode=language_code,
    )
    return response.get('Voices')


def get_available_english_voices():
    codes = ['en-AU', 'en-GB', 'en-GB-WLS', 'en-IN', 'en-US']
    voices = []
    for code in codes:
        voices += get_available_voices(code)
    return voices

available_voice_ids = [voice.get('Id') for voice in get_available_english_voices()]


def text_to_voice(text):
    return client.synthesize_speech(
        OutputFormat='mp3',
        Text=text,
        TextType='text',
        VoiceId=available_voice_ids[random.randint(0, len(available_voice_ids) - 1)]
    )


