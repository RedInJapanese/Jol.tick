import agent as a
import environment as pe
import main as m
import map as map
def train_agent(agent, environment, num_episodes):
    for episode in range(num_episodes):
        state = env.get_state()
        total_reward = 0

        while m.done == False:
            map.map_check()
            print('Act')
            action = agent.act(state)
            print(action)
            next_state, reward, done = environment.step(action)
            agent.memory.push(state, action, reward, next_state, done)
            agent.train()
            print('train')
            print(type(state))
            print(m.score)
            state = next_state
            m.score+= reward
        
        print(f"Episode {episode + 1}, Total Reward: {total_reward}")
# Initialize environment and agent
env = pe.PokemonEnvironment()
state_dim = 6    # Define the size of the state representation
action_dim = 4   # Define the number of possible actions
agent = a.DQNAgent(state_dim, action_dim)

# Train the agent
train_agent(agent, env, num_episodes=1000)