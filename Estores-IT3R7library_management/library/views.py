from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Library, Author, Book, Member


# ============= HOME PAGE =============

def home(request):
    return render(request, 'library/home.html')


# ============= CREATE OPERATIONS =============

def create_library(request):
    if request.method == 'POST':
        library = Library.objects.create()
        return redirect('library_list')
    return render(request, 'library/create_library.html')


def create_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        date_birth_year = request.POST.get('date_birth_year')
        
        Author.objects.create(
            author_name=author_name,
            phone_number=phone_number,
            gender=gender,
            date_birth_year=date_birth_year
        )
        return redirect('author_list')
    return render(request, 'library/create_author.html')


def create_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        author_id = request.POST.get('author_id')
        library_id = request.POST.get('library_id')
        date_published = request.POST.get('date_published')
        
        author = Author.objects.get(author_id=author_id)
        library = Library.objects.get(library_id=library_id)
        
        Book.objects.create(
            book_name=book_name,
            author=author,
            library=library,
            date_published=date_published
        )
        return redirect('book_list')
    
    authors = Author.objects.all()
    libraries = Library.objects.all()
    return render(request, 'library/create_book.html', {
        'authors': authors,
        'libraries': libraries
    })


def create_member(request):
    if request.method == 'POST':
        member_name = request.POST.get('member_name')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        birth_year = request.POST.get('birth_year')
        book_id = request.POST.get('book_id')
        
        book = Book.objects.get(book_id=book_id)
        
        Member.objects.create(
            member_name=member_name,
            phone_number=phone_number,
            gender=gender,
            birth_year=birth_year,
            book=book
        )
        return redirect('member_list')
    
    books = Book.objects.all()
    return render(request, 'library/create_member.html', {'books': books})


# ============= READ OPERATIONS =============

def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library/library_list.html', {'libraries': libraries})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})


# ============= UPDATE OPERATIONS (BONUS) =============

def update_author(request, author_id):
    author = get_object_or_404(Author, author_id=author_id)
    
    if request.method == 'POST':
        author.author_name = request.POST.get('author_name')
        author.phone_number = request.POST.get('phone_number')
        author.gender = request.POST.get('gender')
        author.date_birth_year = request.POST.get('date_birth_year')
        author.save()
        return redirect('author_list')
    
    return render(request, 'library/update_author.html', {'author': author})


def update_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    
    if request.method == 'POST':
        book.book_name = request.POST.get('book_name')
        author_id = request.POST.get('author_id')
        library_id = request.POST.get('library_id')
        book.date_published = request.POST.get('date_published')
        
        book.author = Author.objects.get(author_id=author_id)
        book.library = Library.objects.get(library_id=library_id)
        book.save()
        return redirect('book_list')
    
    authors = Author.objects.all()
    libraries = Library.objects.all()
    return render(request, 'library/update_book.html', {
        'book': book,
        'authors': authors,
        'libraries': libraries
    })


def update_member(request, member_id):
    member = get_object_or_404(Member, member_id=member_id)
    
    if request.method == 'POST':
        member.member_name = request.POST.get('member_name')
        member.phone_number = request.POST.get('phone_number')
        member.gender = request.POST.get('gender')
        member.birth_year = request.POST.get('birth_year')
        book_id = request.POST.get('book_id')
        
        member.book = Book.objects.get(book_id=book_id)
        member.save()
        return redirect('member_list')
    
    books = Book.objects.all()
    return render(request, 'library/update_member.html', {
        'member': member,
        'books': books
    })


# ============= DELETE OPERATIONS =============

def delete_author(request, author_id):
    author = get_object_or_404(Author, author_id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'library/delete_author.html', {'author': author})


def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/delete_book.html', {'book': book})


def delete_member(request, member_id):
    member = get_object_or_404(Member, member_id=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'library/delete_member.html', {'member': member})


def delete_library(request, library_id):
    library = get_object_or_404(Library, library_id=library_id)
    if request.method == 'POST':
        library.delete()
        return redirect('library_list')
    return render(request, 'library/delete_library.html', {'library': library})
