def validate_mark(mark):
    if not isinstance(mark, int):
        return False, "Mark must be an integer."
    if not (0 <= mark <= 100):
        return False, "Marks must be interger between 0 and 100."
    return True, None

import random
import string

used_reg_nos = set()  # To track used registration numbers
def generate_reg_no(prefix):
    while True:
        random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        reg_no = f"{prefix}{random_code}"
        if reg_no not in used_reg_nos:
            used_reg_nos.add(reg_no)
            return reg_no
