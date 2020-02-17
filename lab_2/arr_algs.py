
def find_min(lst):
    elements = set(lst)
    for elem in elements:
        lesser_elements_count = 0
        for curr_elem in elements:
            if elem < curr_elem:
                lesser_elements_count += 1
        if lesser_elements_count == len(elements) - 1:
            return elem

def find_sred(lst):
    znach = 0
    for elem in range (len(lst)):
        znach = znach + lst [elem]
    znach = znach / len (lst)
    return znach

mass = [200, 100, 20, 44, 15, 17, 15]
print(find_min(mass))
print(find_sred(mass))