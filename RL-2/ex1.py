import gym
import numpy as np
import cv2


#create frozen lake env
env=gym.make("FrozenLake-v0")

#create counter variables and Q matrix
obs_space=env.observation_space.n
act_space=env.action_space.n
Q= np.zeros([obs_space, act_space])
count=0
gamma=0.2
avg=0
episodes=1000


#iterate over N times
for episode in range(1,episodes):
    print "Iteration: ",episode
    state=env.reset()
    count=0
    reward=0
    done=False
    print "STATE: ",state
    while reward!=1:
        if done==True:
            break;
        action=np.argmax(Q[state])
        state2,reward,done,info=env.step(action)
        #print "INFO: ",state2,reward,done,info
        Q[state,action]=reward+gamma*np.max(Q[state2])
        state=state2
        #env.render()
        count+=1
        if episode>episodes/2:
            avg+=count
    print "Needed ", count, "moves till success"

print "Average moves: ",avg/episodes/2, "for %d iterations"%episodes

