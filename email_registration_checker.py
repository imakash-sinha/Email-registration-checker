import requests
from bs4 import BeautifulSoup
import argparse
import re
import time
from colorama import Fore, Style

REQUEST_DELAY = 2


def is_valid_email(email):
    # Regular expression pattern for validating email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


def check_registration(email, website):
    # Introduce a delay between requests to respect rate limits
    time.sleep(REQUEST_DELAY)

    # Make a GET request to the website's registration page
    try:
        response = requests.get(website)
        response.raise_for_status()  # Raise an exception for any HTTP error status codes
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {website}: {e}")
        return False

    # Parse the HTML content of the registration page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Search for elements that indicate email registration
    if soup.find('input', {'name': 'email', 'value': email}):
        return True
    else:
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Check email registration status on predefined websites.")
    parser.add_argument("email", help="Email address to check")
    parser.add_argument("--websites", nargs="+", default=[],
                        help="List of websites to check (default: all)")
    args = parser.parse_args()

    # Validate email format
    if not is_valid_email(args.email):
        print("Invalid email address.")
        return

    # Define predefined websites to check
    predefined_websites = {
        'aboutme': 'about.me',
        'adobe': 'adobe.com',
        'amazon': 'amazon.com',
        'anydo': 'any.do',
        'archive': 'archive.org',
        'armurerieauxerre': 'armurerie-auxerre.com',
        'atlassian': 'atlassian.com',
        'babeshows': 'babeshows.co.uk',
        'badeggsonline': 'badeggsonline.com',
        'biosmods': 'bios-mods.com',
        'biotechnologyforums': 'biotechnologyforums.com',
        'bitmoji': 'bitmoji.com',
        'blablacar': 'blablacar.com',
        'blackworldforum': 'blackworldforum.com',
        'blip': 'blip.fm',
        'blitzortung': 'forum.blitzortung.org',
        'bluegrassrivals': 'bluegrassrivals.com',
        'bodybuilding': 'bodybuilding.com',
        'buymeacoffee': 'buymeacoffee.com',
        'cambridgemt': 'discussion.cambridge-mt.com',
        'caringbridge': 'caringbridge.org',
        'chinaphonearena': 'chinaphonearena.com',
        'clashfarmer': 'clashfarmer.com',
        'codecademy': 'codecademy.com',
        'codeigniter': 'forum.codeigniter.com',
        'codepen': 'codepen.io',
        'coroflot': 'coroflot.com',
        'cpaelites': 'cpaelites.com',
        'cpahero': 'cpahero.com',
        'cracked_to': 'cracked.to',
        'crevado': 'crevado.com',
        'deliveroo': 'deliveroo.com',
        'demonforums': 'demonforums.net',
        'devrant': 'devrant.com',
        'diigo': 'diigo.com',
        'discord': 'discord.com',
        'docker': 'docker.com',
        'dominosfr': 'dominos.fr',
        'ebay': 'ebay.com',
        'ello': 'ello.co',
        'envato': 'envato.com',
        'eventbrite': 'eventbrite.com',
        'evernote': 'evernote.com',
        'fanpop': 'fanpop.com',
        'firefox': 'firefox.com',
        'flickr': 'flickr.com',
        'freelancer': 'freelancer.com',
        'freiberg': 'drachenhort.user.stunet.tu-freiberg.de',
        'garmin': 'garmin.com',
        'github': 'github.com',
        'google': 'google.com',
        'gravatar': 'gravatar.com',
        'imgur': 'imgur.com',
        'instagram': 'instagram.com',
        'issuu': 'issuu.com',
        'koditv': 'forum.kodi.tv',
        'komoot': 'komoot.com',
        'laposte': 'laposte.fr',
        'lastfm': 'last.fm',
        'lastpass': 'lastpass.com',
        'mail_ru': 'mail.ru',
        'mybb': 'community.mybb.com',
        'myspace': 'myspace.com',
        'nattyornot': 'nattyornotforum.nattyornot.com',
        'naturabuy': 'naturabuy.fr',
        'ndemiccreations': 'forum.ndemiccreations.com',
        'nextpvr': 'forums.nextpvr.com',
        'nike': 'nike.com',
        'odnoklassniki': 'ok.ru',
        'office365': 'office365.com',
        'onlinesequencer': 'onlinesequencer.net',
        'parler': 'parler.com',
        'patreon': 'patreon.com',
        'pinterest': 'pinterest.com',
        'plurk': 'plurk.com',
        'pornhub': 'pornhub.com',
        'protonmail': 'protonmail.ch',
        'quora': 'quora.com',
        'rambler': 'rambler.ru',
        'redtube': 'redtube.com',
        'replit': 'replit.com',
        'rocketreach': 'rocketreach.co',
        'samsung': 'samsung.com',
        'seoclerks': 'seoclerks.com',
        'sevencups': '7cups.com',
        'smule': 'smule.com',
        'snapchat': 'snapchat.com',
        'soundcloud': 'soundcloud.com',
        'sporcle': 'sporcle.com',
        'spotify': 'spotify.com',
        'strava': 'strava.com',
        'taringa': 'taringa.net',
        'teamtreehouse': 'teamtreehouse.com',
        'tellonym': 'tellonym.me',
        'thecardboard': 'thecardboard.org',
        'therianguide': 'forums.therian-guide.com',
        'thevapingforum': 'thevapingforum.com',
        'tumblr': 'tumblr.com',
        'tunefind': 'tunefind.com',
        'twitter': 'twitter.com',
        'venmo': 'venmo.com',
        'vivino': 'vivino.com',
        'voxmedia': 'voxmedia.com',
        'vrbo': 'vrbo.com',
        'vsco': 'vsco.co',
        'wattpad': 'wattpad.com',
        'wordpress': 'wordpress.com',
        'xing': 'xing.com',
        'xnxx': 'xnxx.com',
        'xvideos': 'xvideos.com',
        'yahoo': 'yahoo.com',
        'hubspot': 'hubspot.com',
        'pipedrive': 'pipedrive.com',
        'insightly': 'insightly.com',
        'nutshell': 'nutshell.com',
        'zoho': 'zoho.com',
        'axonaut': 'axonaut.com',
        'amocrm': 'amocrm.com',
        'nimble': 'nimble.com',
        'nocrm': 'nocrm.io',
        'teamleader': 'teamleader.eu'
    }

    # If specific websites are provided, use them; otherwise, use predefined websites
    websites_to_check = args.websites if args.websites else predefined_websites

    # Print header
    print(f"Checking email registration status for: {args.email}\n")

    # Iterate over websites and check registration status
    for name, url in websites_to_check.items():
        print(f"[*] Checking {name.capitalize()}...", end=" ")
        registered = check_registration(args.email, f"https://{url}")
        status = Fore.GREEN + "registered" + \
            Style.RESET_ALL if registered else Fore.RED + "not registered" + Style.RESET_ALL
        print(status)


if __name__ == "__main__":
    main()
