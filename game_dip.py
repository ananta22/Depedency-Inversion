from abc import ABC, abstractmethod
import random

print("=== RIZKY ANANTA AFADHILA - 21120122120029 ===")


class ChoiceGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass

class RandomChoiceGenerator(ChoiceGenerator):
    def generate(self) -> str:
        return random.choice(["batu", "kertas", "gunting"])

class Game(ABC):
    @abstractmethod
    def play(self):
        pass

class RockPaperScissorsGame(Game):
    def __init__(self, choice_generator: ChoiceGenerator):
        self.choice_generator = choice_generator

    def play(self):
        print("Selamat datang di Game Batu Kertas Gunting!")
        
        while True:
            player_choice = input("Silahkan Pilih batu, kertas, atau gunting (atau 'keluar' untuk berhenti): ").lower()
            
            if player_choice == 'keluar':
                print("Terima kasih telah bermain! :3")
                break
            
            if player_choice not in ["batu", "kertas", "gunting"]:
                print("Pilihan tidak valid. Coba lagi.")
                continue
            
            computer_choice = self.choice_generator.generate()
            
            print(f"Komputer memilih: {computer_choice}")
            
            if player_choice == computer_choice:
                print("Seri Cuyy!")
            elif (player_choice == "batu" and computer_choice == "gunting") or \
                 (player_choice == "kertas" and computer_choice == "batu") or \
                 (player_choice == "gunting" and computer_choice == "kertas"):
                print("Anda menang, GG!!")
            else:
                print("Komputer menang!")

def main():
    choice_generator = RandomChoiceGenerator()
    game = RockPaperScissorsGame(choice_generator)
    game.play()

if __name__ == "__main__":
    main()