import map as map
import main as main
import pyautogui

class PokemonEnvironment:
    def __init__(self):
        # Initialize emulator interface (DeSmuME or similar)
        # Example: self.emulator = DeSmuME_Emulator_Interface() 
        self.state = [main.map, main.current_location, main.curr_coords, main.score, main.first, main.second]
    # def reset(self):
    #     # Reset the game (restart emulator or set to start state)
    #     # Example: self.emulator.reset_game()
        
    #     # Capture the initial state
    #     initial_state = self.get_state()
    #     return initial_state
    
    def step(self, action):
        # Send the action to the emulator (e.g., button press, movement)
        # Example: self.emulator.send_action(action)
        if action == 0:
            pyautogui.keyDown('up')
            pyautogui.keyUp('up')    
        if action == 1:
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')    
        if action == 2:
            pyautogui.keyDown('left')
            pyautogui.keyUp('left')    
        if action == 3:
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')       
        # Wait for the game to process the action and capture the next state
        next_state = self.get_state()

        # Compute the reward (e.g., did the agent make progress?)
        reward = self.compute_reward()
        
        # Determine if the episode is done (e.g., battle is over, agent reached a town)
        done = self.is_done()
        
        return next_state, reward, done
    #done
    def get_state(self):
        # Use Lua scripting in DeSmuME to capture game information (e.g., player position)
        # Example: lua_script_result = self.emulator.run_lua_script("get_player_state.lua")
        # Convert the result to a state representation (could be coordinates, HP, etc.)
        state = [main.map, main.current_location, main.curr_coords, main.score, main.first, main.second]
        return state
    #done
    def compute_reward(self):
        # Calculate reward based on the game state (e.g., reaching a goal or winning a battle)
        # Example: reward might be 1 if the agent reaches a certain location
        reward = 0
        if len(main.locations) > main.score:
            print("new location")
            reward += len(main.locations) - main.score
        main.score = len(main.locations) * 10
        if self.state[2] == main.goals[len(main.goals)-1]:
            main.goals.pop()
            main.score+=100
            print("goal")
            reward += 100
        if main.prev_coords != main.curr_coords:
            print("walkable spot found")
            main.score+=5
            reward+=5
        return reward
    
    def is_done(self):
        # Check if the game episode (battle or navigation) is finished
        main.done = True if len(main.goals) == 0 else False
        return main.done
