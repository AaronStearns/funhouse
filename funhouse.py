import pandas as pd
import numpy as np


df = pd.read_csv (r'/data/funhouse_data.csv')
df = df.drop(['time', 'age'], 1) 

# Compute class probabilities:
pYesTicket = df[df['ticket'] == 'yes'].shape[0] / df.shape[0]
pNoTicket = df[df['ticket'] == 'no'].shape[0] / df.shape[0]

# Spider and sound frequencies
spider = df[df['spider'] == 'on'].shape[0]
sound = df[df['sound'] == 'on'].shape[0]

# Function to calculate conditional probabilities of spider/sound and ticket/no ticket
def calculateNumberGivenExistence(ticketYesNo, spiderOrSound, spiderOrSoundOnOff, yesOrNoTicket):
    p = df[(df['ticket'] == ticketYesNo) & (df[spiderOrSound] == spiderOrSoundOnOff)].shape[0] / yesOrNoTicket
    return p

# Function that creates tuples of the 4 params for calculateNumber... function, 
# creates dict based on computed values and gives descriptive key names
def createVariableDictionary(spiderOrSound):
    yesNo = np.repeat(np.array(["yes", "no"]), [2,2], axis=0)
    zippedPriorsVals = zip(yesNo, 
        np.repeat(spiderOrSound, 5, axis=0), 
        ['on', 'off', 'on', 'off'], 
        [pYesTicket, pYesTicket, pNoTicket, pNoTicket])
    priors = []
    for each in zippedPriorsVals:
        priors.append(calculateNumberGivenExistence(each[0], each[1], each[2], each[3]))

    spiderPriorsTitles = ['pSpiderGivenTicket', 'pNoSpiderGivenTicket', 'pSpiderGivenNoTicket', 'pNoSpiderGivenNoTicket']
    soundPriorsTitles = ['pSoundGivenTicket', 'pNoSoundGivenTicket', 'pSoundGivenNoTicket', 'pNoSoundGivenNoTicket']

    if spiderOrSound == 'spider':
        priorsDict = dict(zip(spiderPriorsTitles, priors))
    elif spiderOrSound == 'sound':
        priorsDict = dict(zip(soundPriorsTitles, priors))

    return(priorsDict)

########################################################

spiderPriors = createVariableDictionary('spider')
soundPriors = createVariableDictionary('sound')

pXGivenTicketYes = spiderPriors['pSpiderGivenTicket'] * soundPriors['pSoundGivenTicket'] * pYesTicket
pXGivenTicketNo = spiderPriors['pSpiderGivenNoTicket'] * soundPriors['pSoundGivenNoTicket'] * pNoTicket

pSpiderAndSound = spider * sound

probOfTicketPurchaseGivenSpiderAndSound = pXGivenTicketYes / pSpiderAndSound
probNoTicketPurchaseGivenSpiderAndSound = pXGivenTicketNo / pSpiderAndSound
