class parking_gargage():
    tickets_avail = [1011, 1012, 1013, 1014, 1015,
                     1016, 1017, 1018, 1019, 1020, 1021, 1022]
    parking_spaces = [5, 7, 10, 21, 22, 46, 56, 72, 73, 74, 76, 81]
    current_ticket = {}
    temporary_list = []
    avail_tickets = 12
    avail_spaces = 12
    paid = True

    def main_menu(self):

        while True:
            print('\n')
            print('\n')
            print('\n*********************************************')
            print('*     Welcome to the RC Parking Garage!     *')
            print(
                f'* There are currently {self.avail_spaces} spaces available   *')
            print(
                f'* There are currently {self.avail_tickets} tickets available   *')
            print('*********************************************\n')
            response = input('Select: Take Ticket | Pay Ticket | Cancel ?\n')

            if response.lower() == 'take':
                self.take_ticket()

            if response.lower() == 'pay':
                self.pay_for_parking()

            if response.lower() == 'cancel':
                exit()

    def take_ticket(self):

        self.current_ticket.update(
            {self.tickets_avail.pop(): self.parking_spaces.pop()})
        self.avail_tickets = self.avail_tickets - 1
        self.avail_spaces = self.avail_spaces - 1
        self.paid = False
        print('\n')
        print('\n')
        print('\n*********************************************')
        print(
            f'Your ticket and parking space \nnumber are: {list(self.current_ticket.items())[-1]}.')
        print(f'Your ticket is not paid for yet.')

    def pay_for_parking(self):

        if self.paid == True:
            print('\n')
            print('\n')
            print('\n*********************************************')
            print('Your ticket is paid!')

        else:

            amount = float(input('How much do you owe for your ticket?\n'))
            res = input(f"Would you like to pay ${amount} now? (Y/N)\n")
            if res == 'y':
                self.paid = True
                self.avail_spaces = self.avail_spaces + 1
                self.avail_tickets = self.avail_tickets + 1
                print('Your ticket is paid')
                for k, v in self.current_ticket.items():
                    self.temporary_list.append(k)
                    self.temporary_list.append(v)
                if self.current_ticket:
                    self.current_ticket.popitem()
            elif res == 'n':
                print('Your ticket is not paid')
            else:
                print('Please enter "y" or "n"')
                self.pay_for_parking()

            self.parking_spaces.append(self.temporary_list.pop())
            self.tickets_avail.append(self.temporary_list.pop())
            print('\n')
            print('\n')
            print('\n*********************************************')
            print('Your ticket has been paid,\nyou have 15 min to leave!\n')
            print('Thank You for parking with us')
            self.leave_garage()

    def leave_garage(self):
        if self.paid == True:
            print('Have a nice day! :)')
        else:
            print("You haven't paid yet!")
            self.pay_for_parking()
