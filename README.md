# Amazon Product Scraper

This task, given to me by Banao is an Amazon product scraper developed using Python and BeautifulSoup. The script extracts specific product details from an Amazon page and saves the data into a CSV file. This project is designed to meet the following requirements:

- Extracts product details, including **Product Name**, **Price**, **Rating**, and **Seller Name** (if not out of stock).
- Saves the data in a structured CSV format.
- Code is optimized, modular, and well-commented for readability and maintainability.

### Project Files

```scrape_mod.py```: The main script that performs web scraping and data extraction from Amazon and writes the data to a CSV file.

```README.md```: Documentation file with an overview, requirements, and usage instructions.

### Requirements

This project uses Python3 and the following packages:

    requests
    BeautifulSoup4
    csv
    re (regular expressions)
    time

- Install the required packages by running:

```bash
pip install requests beautifulsoup4
```

### Features

- Extracts Product Information: Scrapes the Amazon page for product name, price, rating, and seller name (if available).
- Cleans Data: Processes ratings to remove unnecessary text, retaining only numeric values.
- CSV Output: Saves the scraped data in a CSV file, making it easy to review and analyze.
- Modular and Well-Commented Code: Each function is organized for a single responsibility and optimized for readability.

### Usage Instructions

- Clone the repository:

```bash
git clone https://github.com/mfonekpo/banao-scraping-2-.git
```

- Install the required modules
  
```bash
python3 -m pip install -r requirements.txt
```
- Run the script:

```bash
python scrape_mod.py
```
The script will create a file named products.csv in the project directory with the following columns:
1. Product Name
2. Price
3. Rating
4. Seller Name

### Project Structure

1. fetch_page_content: Fetches the HTML content of a given URL and returns a BeautifulSoup object for parsing.
2. parse_product_details: Loops through product items on the page, calls helper functions, and gathers product details.
3. extract_product_name, extract_price, extract_rating: Extract specific details for each product item.
4. fetch_seller_name: Navigates to each product’s detail page to retrieve the seller's name.
5. write_to_csv: Writes the scraped data into a CSV file with specified columns.
6. main: The main function that orchestrates the entire scraping process.

### Example Output

The resulting CSV (products.csv) will look like this:
| Product Name | Price | Rating | Seller Name |
|---|---|---|---|
| Product 1 | ₹499 | 4.2 | Seller A |
| Product 2 | ₹1299 | 4.0 | Out of Stock |


-----
### Demo Video

A short demonstration video is included, explaining the script's functionality and showing how it runs. The video was submitted to the instructor as a grading criteria