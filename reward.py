def compute_reward(state, action, next_state):
    if next_state is the goal:
        return 100  # Reward for reaching a goal
    elif next_state is an obstacle:
        return -10  # Penalty for hitting an obstacle
    else:
        return -1  # Small negative reward to encourage progress
