from cups import Cup
from cards import NumberCard
from cards import AssistCard
from cards import NumberDeck
from cards import AssistDeck
from player import Player
import random
import pygame


class Controller:
    def __init__(self):
        return None

class EventController:
    def __init__(self, player, screen):
        self.player = player  # The player object (human or AI)
        self.screen = screen  # The game screen to render on
        self.selected_card = None  # The card that is currently selected
        self.dragging = False  # Whether the player is dragging the card
        self.drag_offset = (0, 0)  # Offset between mouse position and card position
    
    def handle_events(self):
        """Handle all events related to mouse input (clicking, dragging, and dropping)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit the game

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse click event
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Check if a card is clicked on
                self.select_card(mouse_x, mouse_y)

            elif event.type == pygame.MOUSEMOTION:
                # Mouse motion event (dragging)
                if self.dragging and self.selected_card:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Update the position of the selected card
                    self.update_card_position(mouse_x, mouse_y)

            elif event.type == pygame.MOUSEBUTTONUP:
                # Mouse button release event (dropping)
                if self.dragging and self.selected_card:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Drop the card if it's released on the valid area
                    self.drop_card(mouse_x, mouse_y)

        return True
    
    def select_card(self, mouse_x, mouse_y):
        """Select a card from the player's hand when clicked."""
        for idx, card in enumerate(self.player.hand):
            # Check if the mouse click is inside the card's boundary
            card_x = 120 * idx + 10  # Example positioning for cards
            card_y = 450
            card_width, card_height = 100, 150

            if card_x <= mouse_x <= card_x + card_width and card_y <= mouse_y <= card_y + card_height:
                self.selected_card = card  # Select the card
                self.dragging = True  # Begin dragging the card
                self.drag_offset = (mouse_x - card_x, mouse_y - card_y)  # Offset for smooth dragging
                print(f"Selected card: {card}")
                break

    def update_card_position(self, mouse_x, mouse_y):
        """Update the position of the selected card as the mouse moves."""
        if self.selected_card:
            # Calculate the new position of the card, considering the offset
            card_x = mouse_x - self.drag_offset[0]
            card_y = mouse_y - self.drag_offset[1]
            self.selected_card.x = card_x
            self.selected_card.y = card_y
    
    def drop_card(self, mouse_x, mouse_y):
        """Drop the card in the play area and play it."""
        if self.selected_card:
            # In this example, we'll drop the card in a specific play area (you can modify the logic for validation)
            if 100 <= mouse_x <= 700 and 100 <= mouse_y <= 500:  # Example play area boundary
                print(f"Card {self.selected_card} played at position ({mouse_x}, {mouse_y})")
                self.player.play_card(self.selected_card)  # Play the card
            else:
                print("Card dropped outside of the play area. Try again.")
            
            self.selected_card = None  # Deselect the card
            self.dragging = False  # Stop dragging

class GameController:
    def __init__(self, player1, player2):
        self.players = [player1, player2]  # Player 1 and Player 2
        self.current_player = None  #so players can choose
        self.current_round = 1
        self.cups = self.create_random_cups()  # The 8 cups
        self.assist_deck = AssistDeck()  # Deck for Assist Cards
        self.number_deck = NumberDeck()  #Deck for number deck
        self.game_over = False
        self.start_game()

    def start_game(self):
        """Start the game and give initial cards to the players."""
        player1, player2 = self.players
        # Ask the players who will go first
        self.ask_player_choice()

        # First round setup
        self.deal_initial_cards(player1, player2)
        self.game_over = False
        self.current_round = 1
        self.play_round()

    def ask_player_choice(self):
        """Ask the players who will go first."""
        # Display prompt for selecting who goes first
        self.display_text("Who will go first?", 100, 100)
        self.display_text(f"1. {self.players[0].name}", 100, 150)
        self.display_text(f"2. {self.players[1].name}", 100, 200)
        
    pygame.display.update()
    
    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 100 <= pos[0] <= 200:
                    if 150 <= pos[1] <= 180:
                        choice = '1'
                    elif 200 <= pos[1] <= 230:
                        choice = '2'
            
            pygame.display.update()
        
        # Set the starting player based on the choice
    if choice == '1':
        self.current_player = 0  # Player 1 goes first
    else:
        self.current_player = 1  # Player 2 goes first

    def deal_initial_cards(self, player1, player2):
        """Deal initial cards to players according to the rules."""
        # Player 1 gets 2 Number Cards and 1 Assist Card
        player1.draw_card(self.number_deck.draw())
        player1.draw_card(self.number_deck.draw())
        player1.draw_card(self.assist_deck.draw())

        # Player 2 gets 3 Number Cards and 1 Assist Card
        player2.draw_card(self.number_deck.draw())
        player2.draw_card(self.number_deck.draw())
        player2.draw_card(self.number_deck.draw())
        player2.draw_card(self.assist_deck.draw())

    def create_random_cups(self):
        """Create 8 cups with random colors."""
        available_colors = ['grey', 'yellow', 'brown', 'blue', 'green']
        random.shuffle(available_colors)
        cups = []
        for i in range(8):
            color = available_colors[i % len(available_colors)]  # Recycle colors if necessary
            cups.append(Cup(color))
        return cups

    def play_round(self):
        """Play a round of the game."""
        while not self.game_over:
            self.play_turn()
            self.check_end_of_round()
            if self.game_over:
                self.tally_points()
                break

    def play_turn(self):
        """Manage a single player's turn (both phases: Assist Card Phase and Number Card Phase)."""
        print(f"Round {self.current_round}, {self.players[self.current_player].name}'s turn.")
        
        # Assist Card Phase
        self.assist_card_phase(self.players[self.current_player])

        # Number Card Phase
        self.number_card_phase(self.players[self.current_player])

        # Switch player after the turn
        self.current_player = (self.current_player + 1) % 2

    def assist_card_phase(self, player):
        """Handle the Assist Card Phase where a player plays assist cards."""
        print(f"{player.name} is in the Assist Card Phase.")
        while True:
            if not player.hand or all(card.card_type != 'assist' for card in player.hand):
                print(f"{player.name} has no more assist cards to play.")
                break
            # In a real game, there would be logic for the player to decide which card to play
            assist_card = player.play_assist_card()
            if assist_card:
                print(f"{player.name} played an Assist Card: {assist_card.ability}")
            else:
                print(f"{player.name} can't play any assist card.")
                break
        print(f"{player.name} has finished the Assist Card Phase.")

    def number_card_phase(self, player):
        """Handle the Number Card Phase where a player plays or draws number cards."""
        print(f"{player.name} is in the Number Card Phase.")
        if len(player.hand) < 10:  # Check for hand limit
            drawn_card = self.number_deck.draw()
            if drawn_card:
                player.draw_card(drawn_card)
                print(f"{player.name} drew a {drawn_card}")
            else:
                print("No more cards to draw.")
        else:
            print(f"{player.name} has a full hand. Can play a card.")
            number_card = player.play_number_card()  # Let the player decide which card to play
            if number_card:
                print(f"{player.name} played Number Card: {number_card.value} {number_card.color}")
            else:
                print(f"{player.name} skipped playing a card.")
        
    def check_end_of_round(self):
        """Check if the round is over (8 cups filled)."""
        if all(cup.is_filled for cup in self.cups):  # All cups are filled with kitties
            print("All cups are filled!")
            self.game_over = True

    def tally_points(self):
        """Calculate the winner based on the points in cups."""
        player1_points = self.calculate_player_points(self.players[0])
        player2_points = self.calculate_player_points(self.players[1])
        
        print(f"Final score - {self.players[0].name}: {player1_points}, {self.players[1].name}: {player2_points}")
        
        if player1_points > player2_points:
            print(f"{self.players[0].name} wins!")
        elif player2_points > player1_points:
            print(f"{self.players[1].name} wins!")
        else:
            print("It's a tie!")

    def calculate_player_points(self, player):
        """Calculate the points for a player based on filled cups."""
        points = 0
        for cup in self.cups:
            if cup.is_filled:
                if cup.color == "white":  # White cup: Points = Number card value
                    points += cup.filled_card.value
                elif cup.color == cup.filled_card.color:  # Matched color: Double points
                    points += 2 * cup.filled_card.value
                else:
                    points += 0  # Mismatch color: No points
        return points