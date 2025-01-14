from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PAGE_MAPPER = {
    '/': ['pages', 'main_page.html'],
    '/contacts/': ['pages', 'contacts.html'],
    '/categories/': ['pages', 'category.html'],
    '/orders/': ['pages', 'category.html'],
}