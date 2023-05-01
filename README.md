# Solve CartPole-variation using Q-learning

Solve a modified CartPole environment on OpenAI Gym by simple q-learning algorithm.

We implemented a variation of the CartPole problem raised ​​by Barto, Sutton, and Anderson. The Q-learning approach is used to solve this continuous time-space problem where different periodic goals require different strategies. In our experiment, the cart has to balance the pole and is supposed to drive from left to right and oscillate near a single position. Since Q-learning is designed for solving discrete time-space problems, a function is introduced to transform continuous time-space to discrete with the idea of binning. Our result indicates that with the help of discrete-binning, Q-learning can better solve the CartPole parking problem in a generalized way. 

This repo is based on work of [icoxfog417](https://github.com/icoxfog417/cartpole-q-learning) where is single target.
The environment is [cartpole](https://github.com/cisc474projectgroup/cartpole).
The report of this project can be found [here](Q-learning(RL) for multiple stage problem.pdf)
## Run

```
python cartpole.py
```

* `--episode`: direct the episode count
* `--render`: render the GUI


### env.cartpole_474.py

Modified `step` function, includes new reward function:

    New end condiction.
    Reward based on posiiton.
    Reward baesd on momuntumun.

modified `render` function.

### agent.py

added reward static

added target_hit

added plt function

### cartpole.py
modified bin_size
modified `learning_rate_decay` and `epsilon_dacay`

