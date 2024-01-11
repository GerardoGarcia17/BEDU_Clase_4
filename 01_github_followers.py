import requests

BASE_URL = 'https://api.github.com/'

def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None
     
def download_avatar_user(avatar_url, username):
    response = requests.get(avatar_url)
    if response.status_code == 200:
        # Download image
        response_content = response.content
        filename = f'tmp/{username}.png'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None


username = input('Give me an username you want to extract the information:\n')
selected_user = get_github_user(username)
print(download_avatar_user(selected_user.get('avatar_url'),username))
    



    