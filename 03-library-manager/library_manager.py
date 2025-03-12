import json
from pathlib import Path

class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

    def __str__(self):
        status = "Read" if self.read_status else "Unread"
        return f"{self.title} by {self.author} ({self.year}) - {self.genre} - {status}"

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'read_status': self.read_status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            author=data['author'],
            year=data['year'],
            genre=data['genre'],
            read_status=data['read_status']
        )

class LibraryManager:
    def __init__(self):
        self.books = []
        self.filename = "library.json"
        self.modified = False  # Flag to track changes
        self.load_library()

    def save_library(self):
        """Saves the library only if modifications were made."""
        if self.modified:
            try:
                with open(self.filename, 'w', encoding='utf-8') as f:
                    json.dump([book.to_dict() for book in self.books], f, indent=4)
                print(f"\n📚 Library saved to {self.filename}")
            except Exception as e:
                print(f"\n❌ Error saving library: {e}")

    def load_library(self):
        """Loads the library data from a JSON file."""
        try:
            if Path(self.filename).exists():
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(book_data) for book_data in data]
                print(f"\n📖 Library loaded from {self.filename}")
        except Exception as e:
            print(f"\n❌ Error loading library: {e}")
            self.books = []

    def add_book(self):
        """Adds a new book to the library."""
        print("\n=== 📕 Add a Book ===")
        title = input("Enter the book title: ").strip()
        author = input("Enter the author: ").strip()

        # Validate year input
        while True:
            try:
                year = int(input("Enter the publication year: "))
                break
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        genre = input("Enter the genre: ").strip()
        read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'

        self.books.append(Book(title, author, year, genre, read_status))
        self.modified = True
        print("✅ Book added successfully!")

    def remove_book(self):
        """Removes a book based on title."""
        print("\n=== ❌ Remove a Book ===")
        title = input("Enter the title of the book to remove: ").strip().lower()

        book_to_remove = next((book for book in self.books if book.title.lower() == title), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.modified = True
            print("✅ Book removed successfully!")
        else:
            print("❌ Book not found!")

    def search_book(self):
        """Searches for a book by title or author."""
        print("\n=== 🔍 Search for a Book ===")
        print("1. Search by Title")
        print("2. Search by Author")

        choice = input("Enter your choice: ").strip()
        search_term = input("Enter the search term: ").strip().lower()

        found_books = [
            book for book in self.books if
            (choice == "1" and search_term in book.title.lower()) or
            (choice == "2" and search_term in book.author.lower())
        ]

        if found_books:
            print("\n📚 Matching Books:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. {book}")
        else:
            print("❌ No matching books found!")

    def display_all_books(self):
        """Displays all books in the library."""
        print("\n=== 📚 Your Library ===")
        if not self.books:
            print("📖 Your library is empty!")
            return

        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def display_statistics(self):
        """Displays statistics about the library."""
        print("\n=== 📊 Library Statistics ===")
        total_books = len(self.books)
        if total_books == 0:
            print("📖 Your library is empty!")
            return

        read_books = sum(1 for book in self.books if book.read_status)
        percentage_read = (read_books / total_books) * 100

        print(f"📚 Total books: {total_books}")
        print(f"📖 Books read: {read_books} ({percentage_read:.1f}%)")

def main():
    library = LibraryManager()

    while True:
        print("\n=== 📕 Personal Library Manager ===")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.remove_book()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.display_all_books()
        elif choice == "5":
            library.display_statistics()
        elif choice == "6":
            library.save_library()
            print("\n👋 Goodbye! See you next time.")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
