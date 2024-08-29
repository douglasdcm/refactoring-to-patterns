# Original code
# The Console class is a singleton that is accessed inside of the "play" method from the
# Blackjack class. It is difficult to test the method as the Console classe is initialized
# in the middle of the method. So, it is not easy to mock or configure it outside of the method.
class HitStayResponse:
    def should_hit():
        pass


class Console:
    """Singleton class"""

    hit_stay_response = HitStayResponse()

    @staticmethod
    def obtain_hit_stay_response(self, input):
        return Console.hit_stay_response

    @staticmethod
    def set_player_response_strategy(self, new_hit_stay_response):
        Console.hit_stay_response = new_hit_stay_response


class Blackjack:
    def play(self):
        hit_stay_response: HitStayResponse = Console.obtain_hit_stay_response(
            input="any"
        )
        if hit_stay_response.should_hit():
            pass


# Code refactored
# The Console class was inlined in the methods of the class Blackjack so it is easier to set or
# obtain the values related to Hit Or Stay. The methods "obtain_hit_stay_response"
# and "set_player_response" expose the inlined singleton, so it is possible to configure it.
class HitStayResponseRefac:
    def read_from(self, input):
        self._hit_or_stay = input

    def should_hit(self):
        if self._hit_or_stay == "H":
            return True
        return False


class ConsoleRefac:
    hit_stay_response: HitStayResponseRefac = HitStayResponseRefac()

    @staticmethod
    def obtain_hit_stay_response(input) -> HitStayResponseRefac:
        # inlined singleton
        ConsoleRefac.hit_stay_response.read_from(input)
        return ConsoleRefac.hit_stay_response

    @staticmethod
    def set_player_response(new_hit_stay_response):
        # inlined singleton
        ConsoleRefac.hit_stay_response = new_hit_stay_response


class BlackjackRefac:

    def obtain_hit_stay_response(self, input):
        return ConsoleRefac.obtain_hit_stay_response(input)

    def set_player_response(self, new_hit_stay_response: HitStayResponseRefac):
        ConsoleRefac.set_player_response(new_hit_stay_response)

    def play(self):
        hit_stay_response: HitStayResponseRefac = self.obtain_hit_stay_response(
            input="any"
        )
        if hit_stay_response.should_hit():
            pass
