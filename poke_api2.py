import requests
import image_lib
import os


poke_url = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    download_artwork('dugtrio', r'c:\temp')

def get_poke_info(poke_name):

    # Clean the Pokemon name parameter by:
    # - Converting to a string object, 
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    poke_name = str(poke_name).strip().lower()
 
    # Build the clean URL for the GET request
    url = poke_url + poke_name
 
    # Send GET request for Pokemon info
    print(f'Getting information for {poke_name}...', end='')
    resp_msg = requests.get(url)
 
    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
        return

    return

def get_poke_names(offset=0, limit=100000):

    query_str_param = {
        'offset' : offset,
        'limit' : limit
    }

    resp_msg = requests.get(poke_url, params=query_str_param)

    #get the results of all pokemon
    if resp_msg.status_code == requests.codes.ok:
        poke_dict = resp_msg.json()
        poke_name_list = [p['name'] for p in poke_dict['results']] 
        return poke_name_list
    else:
        print('failure')
        print(f'Responce Code: {resp_msg.status_code} ({resp_msg.reason})')
        return

def download_artwork(poke_name, save_dir):

    poke_info = get_poke_info(poke_name)
    if poke_info is None:
        return

    #get the art url
    artwork_url = poke_info['sprites']['other']['official-artwork']['front_default']
    image_byte = image_lib.download_image(artwork_url)
    if image_byte is None:
        return

    file_ext = artwork_url.split('.')[-1]
    image_path = os.path.join(save_dir, f'{poke_name}.{file_ext}')
    if image_lib.save_image_file(image_byte, image_path):
        return image_path

    
    return



if __name__ == '__main__':
    main()