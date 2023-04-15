class parking_gargage():
    tickets_avail = [1011, 1012, 1013, 1014, 1015,
                     1016, 1017, 1018, 1019, 1020, 1021, 1022]
    parking_spaces = [5, 7, 10, 21, 22, 46, 56, 72, 73, 74, 76, 81]
    current_ticket = {}
    temporary_list = []

    def main_menu(self):

        while True:

            print('\n*********************************************')
            print('*     Welcome to the RC Parking Garage!     *')
            print(
                f'* There are currently {len(self.parking_spaces)} spaces available   *')
            print('*********************************************\n')
            response = input('Select: Take Ticket | Pay Ticket | Cancel ?\n')

            if response.lower() == 'take':
                self.take_ticket()

            if response.lower() == 'pay':
                self.pay_for_parking()

            if response.lower() == 'cancel':
                # parking = False
                break

    def take_ticket(self):

        self.current_ticket.update(
            {self.tickets_avail.pop(): self.parking_spaces.pop()})
        print(
            f'\nYour ticket and parking space number are: {list(self.current_ticket.items())[-1]}.')

        print(self.current_ticket)

    def pay_for_parking(self):

        print('Thank You for parking with us')

        for k, v in self.current_ticket.items():
            self.temporary_list.append(k)

        for k, v in self.current_ticket.items():
            self.temporary_list.append(v)
        if self.current_ticket:
            self.current_ticket.popitem()
        else:
            self.leave_garage()

        print(self.current_ticket)

        if len(self.parking_spaces) >= 12:
            print('you have already paid!')
        else:
            self.parking_spaces.append(self.temporary_list.pop())
            self.tickets_avail.append(self.temporary_list.pop())

        print('Your ticket has been paid, you have 15 min to leave!')

        self.leave_garage()

    def leave_garage(self):
        print('Thank you have a nice day')
