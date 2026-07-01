# Imports
import qrcode
import requests


def is_valid_link(url):
    """ Return True if the URL is reachable, otherwise False. """
    try:
        # HEAD is lighter than GET because it doesn't download the page.
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.ok

    # If the request fails ( invalid URL, timeout, no connection, etc. )
    # try again with GET.
    except requests.RequestException:
        try:
            response = requests.get(url, allow_redirects=True, timeout=5)
            return response.ok
        except requests.RequestException as error:
            print(error)
            return False


def generate_qr_code(filename, url):
    """ Generate and save a custom QR code. """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Use inverted colors for a custom look.
    img = qr.make_image(
        back_color=(0, 0, 0),
        fill_color=(255, 255, 255),
    )

    img.save(f"{filename}.png")
    print(f'QR code saved as "{filename}.png"')


def ask_file_name():
    """ Ask the user for a valid output filename. """
    while True:
        file_name = input("How do you want to call the QR code image? ").strip()

        if not file_name:
            print("File name cannot be empty.")
            continue

        return file_name


def ask_url():
    """ Ask the user for a reachable URL. """
    while True:
        user_url = input("Enter your link here: ").strip()

        # Automatically prepend HTTPS if the user omitted the protocol.
        if not user_url.startswith(("http://", "https://")):
            user_url = "https://" + user_url

        if is_valid_link(user_url):
            return user_url

        print("\nThe link is not valid or unreachable. Please try again.\n")


def main():
    filename = ask_file_name()
    url = ask_url()

    generate_qr_code(filename, url)


if __name__ == "__main__":
    main()