######################################################################
# Author: Julio Jijon
# Username: jijonj
#
# Assignment: HW09: UPC Barcodes with classes
#
# Purpose: Verify a barcode and draw it, if valid
#
######################################################################
# Acknowledgements: Dr. Scott Heggen, hw09_nascii.py

from operator import index


# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle


class UPC:
    def __init__(self, code):
        """
        creates the UPC object
        :param code: the code that the user inputs
        """
        self.wn = None
        self.setup_window()
        self.input_code = code

    def is_valid_input(self):
        """
        determine if the input is 12 digits long

        :return: True, False
        """
        if len(self.input_code) != 12:
            return False
        return True

    def is_valid_modulo(self):
        """
        validates the modulo check digit

        :return: True, False
        """
        even_num = []
        odd_num = []
        barcode_num = []

        for num in self.input_code:
            barcode_num.append(int(num))

        check_digit = barcode_num[11]
        barcode_num = barcode_num[:-1]

        counter = 0
        for number in barcode_num:
            counter += 1
            if counter % 2 != 0:
                odd_num.append(number)
            else:
                even_num.append(number)

        odd_num_multi = sum(odd_num) * 3
        sum_odd_even = odd_num_multi + sum(even_num)
        modulo_check = sum_odd_even % 10

        if modulo_check != 0:
            modulo_check = 10 - modulo_check

        if modulo_check != check_digit:
            return False

        return True

    def translate(self, digit, side):
        """
        translates the digit to its binary code

        :param digit: the individual digit in the barcode
        :param side: the 'side' in which the digit lies
        :return:
        """
        barcode_data = [
            ["0001101", "1110010"],
            ["0011001", "1100110"],
            ["0010011", "1101100"],
            ["0111101", "1000010"],
            ["0100011", "1011100"],
            ["0110001", "1001110"],
            ["0101111", "1010000"],
            ["0111011", "1000100"],
            ["0110111", "1001000"],
            ["0001011", "1110100"]
        ]
        return barcode_data[int(digit)][side]

    def setup_window(self):
        '''
        Sets up the turtle window and places the turtle at the starting location
        :return:
        '''
        self.wn = turtle.Screen()
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.goto(-450, 200)
        self.t.pendown()
        self.t.speed(0)

    def draw(self):
        """
        draws the barcode from the user given barcode
        :return:
        """
        counter = 0
        for number in self.input_code:
            counter += 1
            if counter < 6:
                self.draw_column(number, 0)
            else:
                self.draw_column(number, 1)
            # Move the turtle right after drawing each column
            self.t.penup()
            self.t.forward(5)  # Move forward 7 units (width of one column)
            self.t.pendown()

        self.t.hideturtle()

    def draw_column(self, number, side):
        """
        draws the individual column of each binary number
        :param number: the individual digit from the barcode
        :param side: which side of the barcode the digit lies on
        :return:
        """
        binary = self.translate(number, side)  # Get the binary translation
        for digit in binary:
            self.t.color("black")
            self.t.fillcolor("white" if digit == "0" else "black")
            self.t.begin_fill()
            self.draw_rectangle()
            self.t.end_fill()
            self.t.penup()
            self.t.forward(5)  # Move right by 10 units (width of square)
            self.t.pendown()

    def draw_rectangle(self):
        """
        draws an individual rectangle

        :return:
        """
        for i in range(2):
            self.t.forward(5)  # Length of each square side
            self.t.left(90)
            self.t.fd(200)
            self.t.left(90)

    def draw_error(self):
        """
        'writes' an error message using turtle
        :return:
        """
        self.t.write("This is not valid")

def main():
    """
    main function that asks the user for a barcode and draws it
    :return:
    """
    input_code = input("Enter a 12 digit code [0-9]: ")
    code = UPC(input_code.replace(" ", ""))

    while not code.is_valid_input():
        input_code = input("Please enter a 12 digit code [0-9]: ")
        code = UPC(input_code.replace(" ", ""))

    if code.is_valid_modulo():
        print("This is valid")
        code.draw()
        code.wn.mainloop()
    else:
        code.draw_error()
        code.wn.mainloop()


if __name__ == "__main__":
    main()
