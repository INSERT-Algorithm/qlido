def solution(phone_book):
    phone_book.sort()
    for p in range(len(phone_book)):
        if p == (len(phone_book) - 1):
            break
        now = phone_book[p]
        next = (phone_book[p+1])[:len(now)]
        if now == next:
            return False
    return True


print(solution(["119", "97674223", "1195524421"]) == False)
print(solution(["123", "456", "789"]) == True)
print(solution(["12", "123", "1235", "567", "88"]) == False)
