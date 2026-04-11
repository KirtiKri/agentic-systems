#Create a string " python programming " and print the string after applying strip() and title() methods.
test = 'python programming'
print(test.strip().title())

#Write a program to check whether a given email (string) starts with "user" and contains "@".
email = 'user1234@gmail.com'
print(email.startswith('user'), '@' in email)

#Create a dictionary student = {'name': 'Alice', 'age': 22} and:
#Print all keys, values, and items separately.
student ={
    'name' : 'Alice',
    'age' : 22
 }
print(student.keys(), student.values(), student.items())

#Given a dictionary config = {'theme': 'dark'}, safely access the key 'font_size' using get() and print a default value if it does not exist.
config ={ 'theme' : 'dark'}
print(config.get('font_size'))
print(config.get('font_size', 15))

#Create a nested dictionary for a user with name and city, and safely access the city using chained get() methods.
info = { 
    'user' :{
        'name' : ' Kirti',
        'address' : {
            'city' : 'Munger'
        }
    }
}
print(info.get('user', {}).get('address', {}).get('city', 'Unknown'))
