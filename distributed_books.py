def is_possible(books, students, max_pages):
    student_count = 1
    current_pages = 0

    for pages in books:
        if pages > max_pages:
            return False

        if current_pages + pages > max_pages:
            student_count += 1
            current_pages = pages

            if student_count > students:
                return False
        else:
            current_pages += pages

    return True


def distribute_books(books, students):
    if students > len(books):
        return -1

    low = max(books)
    high = sum(books)
    result = high

    while low <= high:
        mid = (low + high) // 2

        if is_possible(books, students, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


# Example usage
books = [12, 34, 67, 90]
students = 2

print("Minimum maximum pages:", distribute_books(books, students))
