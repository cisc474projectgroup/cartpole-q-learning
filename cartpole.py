import os
import math
import argparse
import gym
import env
from agent import Q, Agent, Trainer

def main(episodes, render, monitor,target =500):
    env = gym.make("cartpole-v474")

    q = Q(
        env.action_space.n, 
        env.observation_space, 
        bin_size=[8, 6, 8, 5],
        low_bound=[None, -0.5, None, -math.radians(50)],
        high_bound=[None, 0.5, None, math.radians(50)]
        )
    agent = Agent(q, epsilon=0.05)

    learning_decay = lambda lr, t: max(0.1, min(0.5, 1.0 - math.log10((t + 1) / 25)))
    epsilon_decay = lambda eps, t: max(0.01, min(1.0, 1.0 - math.log10((t + 1) / 25)))
    trainer = Trainer(
        agent, 
        gamma=0.99,
        learning_rate=0.5, learning_rate_decay=learning_decay, 
        epsilon=1.0, epsilon_decay=epsilon_decay,
        max_step=4000)

    if monitor:
        env.monitor.start(RECORD_PATH)

    trainer.train(env, episode_count=episodes, render=render)

    if monitor:
        env.monitor.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="train & run cartpole ")
    parser.add_argument("--episode", type=int, default=2000, help="episode to train")
    parser.add_argument("--render", action="store_true", help="render the screen")
    parser.add_argument("--monitor", action="store_true", help="monitor")

    args = parser.parse_args()

    main(args.episode, args.render, args.monitor,target = 500)
