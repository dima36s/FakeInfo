import Faker

faker = Faker('RU')
name = faker.name()
address = faker.address()
email = faker.email()
job = faker.job()
date = faker.date()

print(f'{name}\n{address}\n{email}\n{job}\n{date}')
