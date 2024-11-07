from bs4 import BeautifulSoup as bs
import requests
import csv
import re
import time

# URL of the Amazon product listing page
BASE_URL = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}


def fetch_page_content(url):
    """Fetches page content and returns a BeautifulSoup object."""
    response = requests.get(url, headers=HEADERS)
    return bs(response.content, 'html.parser')


def parse_product_details(soup):
    """Parses product details from the main listing page."""
    product_data = []

    # Locate all product items
    product_items = soup.find_all("div", {"data-component-type": "s-search-result"})
    
    # Loop through each product item
    for item in product_items:
        # Extract individual product details
        product_name = extract_product_name(item)
        price = extract_price(item)
        rating = extract_rating(item)
        seller_name = fetch_seller_name(item)

        # Append the details to the product data list
        product_data.append({
            "Product Name": product_name,
            "Price": price,
            "Rating": rating,
            "Seller Name": seller_name
        })
    
    return product_data


def extract_product_name(item):
    """Extracts and returns the product name."""
    name_tag = item.find("span", class_="a-size-base-plus a-color-base a-text-normal")
    return name_tag.text.strip() if name_tag else "N/A"


def extract_price(item):
    """Extracts and returns the price of the product."""
    price_tag = item.find("span", class_="a-price-whole")
    return price_tag.text.strip() if price_tag else "N/A"


def extract_rating(item):
    """Extracts and cleans the rating to return only the numeric part."""
    rating_tag = item.find("span", class_="a-icon-alt")
    if rating_tag:
        rating_match = re.search(r"(\d+(\.\d+)?)", rating_tag.text)
        return rating_match.group(0) if rating_match else "N/A"
    return "N/A"


def fetch_seller_name(item):
    """Fetches the seller's name by visiting the product detail page."""
    product_link_tag = item.find("a", class_="a-link-normal s-no-outline")
    if product_link_tag and 'href' in product_link_tag.attrs:
        product_url = f'https://www.amazon.in{product_link_tag["href"]}'
        product_soup = fetch_page_content(product_url)
        
        # Locate seller's name on the product detail page
        seller_name_tag = product_soup.find(id="sellerProfileTriggerId")
        time.sleep(1)  # Delay to avoid overwhelming Amazon with requests
        return seller_name_tag.text.strip() if seller_name_tag else "Out of Stock"
    
    return "Out of Stock"


def write_to_csv(data, filename="products.csv"):
    """Writes the product data to a CSV file."""
    fieldnames = ["Product Name", "Price", "Rating", "Seller Name"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"{filename} has been created successfully!")


def main():
    """Main function to execute the scraping process."""
    soup = fetch_page_content(BASE_URL)
    product_data = parse_product_details(soup)
    write_to_csv(product_data)


# Run the main function
if __name__ == "__main__":
    main()
