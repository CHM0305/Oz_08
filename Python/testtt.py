from faker import Faker

# Faker 객체 생성, 원하는 로케일 설정 가능 (예: 'ko_KR'은 한국어)
fake = Faker('ko_KR')

# 가짜 이름 생성
print(fake.name())

# 가짜 주소 생성
print(fake.address())

# 가짜 이메일 생성
print(fake.email())

# 가짜 문장 생성
print(fake.sentence())
