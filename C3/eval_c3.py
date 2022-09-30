class Calculator:
    def missing_addition_operator(self, index):  # using the index, check if the + exists
        if index == -1:
            return True
        return False

    def invalid_char_exists(self, expression):  # checks for any invalid characters
        for i in expression:
            if (not i.isnumeric()) and (i != '+' and i != '.' and i != '-'):
                return True
        return False
    
    def both_terms_exist(self, expression, index):  # check that there exists two terms based on the position of the index
        if index == 0 or index == (len(expression) - 1):
            return False
        return True
    
    def find_char(self, expression, char):       # finds index of a char given the expression
        return expression.find(char)

    def get_terms(self, expression, index):      # separates term from expression
        num_one = expression[0:index]
        num_two = expression[index+1:]
        return (num_one, num_two)
    
    def negative_term(self, term):               # checks for valid negative term
        if term[0] == '-':
            return True
        if self.find_char(term, '-') != -1:   # negative not at beginning of number
            return -1   # invlaid expression
        return False

    def float_or_int(self, term):                # given string term, turn into float or int
        if self.decimal_term(term):
            num = float(term)
        else:
            num = int(term)
        return num

    def terms_to_nums(self, terms):              # returns 2 item list with terms in number form
        nums = [0, 0]
        for i in range(2):  # for both terms
            temp = terms[i] # temp hold a term
            if self.negative_term(temp):      # if term is negative
                temp = temp[1:len(terms[i])]  # get rid of negative sign
                num = 0 - self.float_or_int(temp)   # 0 - number form of term to get negative
            else:   # not a negative number
                num = self.float_or_int(temp) # turn into number form
            nums[i] = num   # put number form of term into list

        return nums
    
    def decimal_term(self, term):           # checks for valid decimal term
        index = self.find_char(term, '.')
        if index == -1:
            return False
        return True

    def add_nums(self, nums):               # adds the numbers together
        num_one = nums[0]
        num_two = nums[1]
        return str(num_one + num_two)
    
    def eval(self, expression):
        ''' Insert your code to process the string input here '''
        index = self.find_char(expression, '+') # gets index of + operator
        
        if self.invalid_char_exists(expression):    # checks for invalid character
            return "Invalid Expression: invalid character found"    
        if self.missing_addition_operator(index):   # based on index, false if + DNE
            return "Invalid Expression: no addition operator found"
        if not self.both_terms_exist(expression, index):    # check that there are two terms
            return "Invalid Expression: a term is missing"

        # get terms
        terms = self.get_terms(expression, index)
        term_one = terms[0]
        term_two = terms[1]

        # check if invalid negative exists
        if self.negative_term(term_one) == -1 or self.negative_term(term_two) == -1:
            return "Invalid Expression: invalid '-' found"

        # turn terms into two item list of numbers
        nums = self.terms_to_nums(terms)
        return self.add_nums(nums)  # add the numbers and return the result

    def run(self):
        # Run until the user cancels, ctl + C
        while True:
            expression = input('Enter an infix addition statement: ')
            result = self.eval(expression)
            print(' = ', result)

if __name__ == "__main__":
    # If this file is run directly from the command line, run the calculator
    c = Calculator()
    c.run()

