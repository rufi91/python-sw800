import gym
import numpy as np


#create taxi env
env=gym.make("Taxi-v2")

#create counter variables and Q matrix
Q= np.zeros([500,6])
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
    print "STATE: ",state
    while reward!=20:
        action=np.argmax(Q[state])
        state2,reward,done,info=env.step(action)
        Q[state,action]=reward+gamma*np.max(Q[state2])
        state=state2
        #env.render()
        count+=1
        if episode>episodes/2:
            avg+=count
    print "Needed ", count, "moves till success"

print "Average moves: ",avg/episodes/2, "for %d iterations"%episodes
