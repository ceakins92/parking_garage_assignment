class parking_gargage():
    tickets_avail = []
    parking_spaces = []
    current_ticket = {}

    def process(self):
        pass
        # ARRIVAL / TAKING TICKET
        # user arrives, gets prompt to take ticket, pay ticket, or cancel
        # -- if user takes ticket, continue to take_tickets method
        # -- if user decides to cancel, then end loop
        #
        # PAYING FOR TICKET
        # user gets prompted to pay for ticket (maybe by ticket number?)
        # -- user input to type ticket number
        # ---- if paid already, continue to leave_garage method
        # ---- if not paid, ask them to "pay" or "cancel"
        # ------- if pay
        # ----------- continue to pay-for-parking method
        # ------- if cancel
        # ----------- return to main prompt

    def take_ticket(self):
        pass
        # - This should decrease the amount of tickets_avail available by 1
        # --- (maybe add randomizer to issue a ticket number?)
        # --- (maybe add a timer to calculate total that stops when they leave)
        # - This should decrease the amount of parking_spaces available by 1
        # - Print a statement thanking the user and telling them their car will be safe with us
        # - Return to main prompt

    def pay_for_parking(self):
        pass
        # - Display an input that waits for an amount from the user and store it in a variable
        # - If the payment variable is not empty then(meaning the ticket has been paid)
        #   -- Display a message to the user that their ticket has been paid and they have 15mins to leave
        #   -- This should update the "current_ticket" dictionary key "paid" to True
        # - Continue to leave_garage method

    def leave_garage(self):
        pass
        # - If the ticket has been paid, display a message of "Thank You, have a nice day"
        # - If the ticket has not been paid:
        #   -- Display an input prompt for payment
        #   -- Once paid, display message "Thank you, have a nice day!"
        # - Update parking_spaces list to increase by 1 (meaning add to the parkingSpaces list)
        # - Update tickets_avail list to increase by 1 (meaning add to the tickets list)
        # - Return to main prompt
